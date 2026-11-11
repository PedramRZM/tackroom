"""Fetch reference material (articles, docs, video transcripts, X posts) into refs/.

Run through the wrapper so dependencies and isolation flags are applied:

    tools/refs article <url>... [--tag T] [--collection C] [--via auto|direct|jina] [--force]
    tools/refs video <id-or-url>... [--tag T] [--collection C] [--force]
    tools/refs playlist <playlist-url> [--tag T] [--collection C] [--max-minutes N] [--force]
    tools/refs post <x-url-or-id>... [--tag T] [--collection C] [--force]
    tools/refs index
    tools/refs watch [--mark]

Every item lands in its own directory with a meta.json, so parallel runs never
write the same file. `index` rebuilds refs/INDEX.md from those meta.json files.
`watch` reads refs/sources/watch.toml and reports URLs that appeared, and pages
whose text changed, since the last `watch --mark`.

Everything downloaded is untrusted text: nothing here executes or imports it.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import re
import subprocess
import sys
import tomllib
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFS = ROOT / "refs"
UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/130.0 Safari/537.36"
)
# Public Invidious instances that proxy YouTube captions. YouTube blocks direct
# caption requests from many IPs; the first instance that returns text wins.
INVIDIOUS = [
    "yt.chocolatemoo53.com",
    "inv.nadeko.net",
    "invidious.nerdvpn.de",
    "invidious.f5.si",
]
MIN_ARTICLE_CHARS = 600


# ---------------------------------------------------------------- helpers


def http_get(url: str, timeout: int = 40, accept: str | None = None) -> tuple[int, str, bytes]:
    """Return (status, content_type, body). Never raises for HTTP errors."""
    headers = {"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"}
    if accept:
        headers["Accept"] = accept
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.headers.get("Content-Type", ""), resp.read()
    except urllib.error.HTTPError as err:
        return err.code, err.headers.get("Content-Type", "") if err.headers else "", b""
    except Exception as err:  # network errors, timeouts, bad TLS
        return 0, f"error: {err}", b""


def decode(body: bytes, content_type: str = "") -> str:
    match = re.search(r"charset=([\w-]+)", content_type or "")
    for enc in filter(None, [match.group(1) if match else None, "utf-8", "latin-1"]):
        try:
            return body.decode(enc)
        except (UnicodeDecodeError, LookupError):
            continue
    return body.decode("utf-8", errors="replace")


def slugify(text: str, limit: int = 80) -> str:
    text = urllib.parse.unquote(text).lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text[:limit].strip("-") or "index"


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def write_item(directory: Path, meta: dict, files: dict[str, str | bytes]) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    for name, content in files.items():
        path = directory / name
        if isinstance(content, bytes):
            path.write_bytes(content)
        else:
            path.write_text(content, encoding="utf-8")
    meta = {k: v for k, v in meta.items() if v not in (None, "", [])}
    meta["fetched_at"] = now()
    (directory / "meta.json").write_text(
        json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def front_matter(meta: dict) -> str:
    lines = ["---"]
    for key in ("title", "author", "date", "url", "site", "type", "via"):
        if meta.get(key):
            lines.append(f"{key}: {json.dumps(str(meta[key]), ensure_ascii=False)}")
    lines.append("---\n")
    return "\n".join(lines)


def report(status: str, ident: str, detail: str = "") -> None:
    print(f"{status:<8} {ident}  {detail}".rstrip(), flush=True)


# ---------------------------------------------------------------- articles


def article_dir(url: str) -> Path:
    parts = urllib.parse.urlsplit(url)
    host = parts.netloc.lower().removeprefix("www.")
    path = parts.path.strip("/")
    slug = slugify(path.replace("/", "-")) if path else "index"
    if parts.query:
        slug = f"{slug}-{hashlib.sha1(parts.query.encode()).hexdigest()[:6]}"
    return REFS / "articles" / host / slug


def via_jina(url: str) -> tuple[str, dict]:
    status, ctype, body = http_get(f"https://r.jina.ai/{url}", timeout=90)
    if status != 200 or not body:
        return "", {}
    text = decode(body, ctype)
    meta: dict = {}
    head, sep, content = text.partition("Markdown Content:")
    if not sep:
        return text.strip(), meta
    for line in head.splitlines():
        if line.startswith("Title:"):
            meta["title"] = line[6:].strip()
        elif line.startswith("Published Time:"):
            meta["date"] = line[15:].strip()[:10]
        elif line.startswith("Warning:"):
            meta["warning"] = line[8:].strip()
    return content.strip(), meta


def via_direct(url: str) -> tuple[str, dict, str]:
    """Return (markdown, meta, kind). kind is html, text, pdf or '' on failure."""
    status, ctype, body = http_get(url)
    if status != 200 or not body:
        return "", {"warning": f"http {status} {ctype}"[:120]}, ""
    lowered = ctype.lower()
    if "pdf" in lowered or body[:5] == b"%PDF-":
        return "", {}, "pdf"
    text = decode(body, ctype)
    is_plain = any(t in lowered for t in ("markdown", "text/plain", "json", "toml", "yaml"))
    if is_plain or re.search(r"\.(md|mdx|txt|toml|json|ya?ml)$", urllib.parse.urlsplit(url).path):
        title = re.search(r"^#\s+(.+)$", text, flags=re.M)
        return text, {"title": title.group(1).strip() if title else None}, "text"

    import trafilatura  # imported lazily: only the article path needs it

    extracted = trafilatura.extract(
        text,
        url=url,
        output_format="markdown",
        include_links=True,
        include_tables=True,
        with_metadata=True,
        favor_recall=True,
    )
    if not extracted:
        return "", {"warning": "extraction returned nothing"}, "html"
    meta: dict = {}
    body_md = extracted
    if extracted.startswith("---"):
        _, block, body_md = extracted.split("---", 2)
        for line in block.strip().splitlines():
            key, _, value = line.partition(":")
            value = value.strip().strip('"')
            if key in ("title", "author", "date", "sitename", "description") and value:
                meta["site" if key == "sitename" else key] = value
    return body_md.strip(), meta, "html"


def headings(markdown: str) -> int:
    return len(re.findall(r"(?m)^#{1,4} \S", markdown))


def cmd_article(args: argparse.Namespace) -> int:
    failures = 0
    for url in args.items:
        directory = article_dir(url)
        if (directory / "meta.json").exists() and not args.force:
            report("exists", url, str(directory.relative_to(ROOT)))
            continue
        markdown, meta, via = "", {}, ""
        if args.via in ("auto", "direct"):
            markdown, meta, kind = via_direct(url)
            via = "direct"
            if kind == "pdf":
                markdown = ""
        # Some sites mark headings up in a way the extractor drops. A long article that came
        # back with no section headings is worth a second attempt through the reader proxy.
        flat = via == "direct" and len(markdown) > 4000 and headings(markdown) < 2
        if (len(markdown) < MIN_ARTICLE_CHARS or flat) and args.via in ("auto", "jina"):
            jina_md, jina_meta = via_jina(url)
            better = len(jina_md) > len(markdown) if not flat else headings(jina_md) >= 3
            if better and len(jina_md) >= MIN_ARTICLE_CHARS:
                markdown, via = jina_md, "jina"
                meta = {**{k: v for k, v in jina_meta.items() if v}, **{k: v for k, v in meta.items() if v}}
        if len(markdown) < MIN_ARTICLE_CHARS:
            failures += 1
            report("FAILED", url, f"{len(markdown)} chars; {meta.get('warning', '')}")
            continue
        record = {
            "type": "doc" if "/docs" in url or url.endswith((".md", ".txt")) else "article",
            "url": url,
            "title": meta.get("title"),
            "author": meta.get("author"),
            "date": meta.get("date"),
            "site": meta.get("site") or urllib.parse.urlsplit(url).netloc,
            "description": meta.get("description"),
            "via": via,
            "chars": len(markdown),
            "tags": args.tag,
            "collection": args.collection,
            "warning": meta.get("warning"),
        }
        write_item(directory, record, {"article.md": front_matter(record) + markdown + "\n"})
        report("saved", url, f"{len(markdown)} chars via {via} -> {directory.relative_to(ROOT)}")
    return 1 if failures else 0


# ---------------------------------------------------------------- videos


def video_id(value: str) -> str:
    match = re.search(r"(?:v=|youtu\.be/|/shorts/|/live/)([\w-]{11})", value)
    if match:
        return match.group(1)
    if re.fullmatch(r"[\w-]{11}", value):
        return value
    raise SystemExit(f"not a YouTube id or url: {value}")


def parse_vtt(vtt: str) -> list[tuple[float, str]]:
    """Return (start_seconds, text) lines with rolling-caption repeats removed."""
    lines: list[tuple[float, str]] = []
    timing = re.compile(r"(?:(\d+):)?(\d{2}):(\d{2})[.,](\d{3})\s+-->")
    start = 0.0
    in_cue = False
    for raw in vtt.splitlines():
        raw = raw.strip()
        match = timing.match(raw)
        if match:
            hours, minutes, seconds, millis = match.groups()
            start = int(hours or 0) * 3600 + int(minutes) * 60 + int(seconds) + int(millis) / 1000
            in_cue = True
            continue
        if not raw:
            in_cue = False
            continue
        if not in_cue:
            continue
        text = html.unescape(re.sub(r"<[^>]+>", "", raw)).strip()
        text = re.sub(r"\s+", " ", text)
        if text and (not lines or lines[-1][1] != text):
            lines.append((start, text))
    return lines


def transcript_markdown(lines: list[tuple[float, str]], window: int = 60) -> str:
    paragraphs: list[str] = []
    bucket: list[str] = []
    bucket_start = 0.0
    for start, text in lines:
        if bucket and start - bucket_start >= window:
            paragraphs.append(_stamp(bucket_start) + " " + " ".join(bucket))
            bucket = []
        if not bucket:
            bucket_start = start
        bucket.append(text)
    if bucket:
        paragraphs.append(_stamp(bucket_start) + " " + " ".join(bucket))
    return "\n\n".join(paragraphs)


def _stamp(seconds: float) -> str:
    seconds = int(seconds)
    hours, rest = divmod(seconds, 3600)
    minutes, secs = divmod(rest, 60)
    return f"[{hours}:{minutes:02d}:{secs:02d}]" if hours else f"[{minutes:02d}:{secs:02d}]"


def captions_from_invidious(vid: str) -> tuple[str, str, str]:
    """Return (vtt, track_label, host) from the first instance that has text."""
    for host in INVIDIOUS:
        status, ctype, body = http_get(f"https://{host}/api/v1/captions/{vid}", timeout=30)
        if status != 200 or not body:
            continue
        try:
            tracks = json.loads(decode(body, ctype)).get("captions", [])
        except (json.JSONDecodeError, AttributeError):
            continue
        english = [t for t in tracks if str(t.get("languageCode", "")).startswith("en")]
        # Human-written tracks first; auto-generated last.
        english.sort(key=lambda t: "auto-generated" in t.get("label", ""))
        for track in english:
            label = track.get("label", "")
            url = f"https://{host}/api/v1/captions/{vid}?label={urllib.parse.quote_plus(label)}"
            status, ctype, body = http_get(url, timeout=60)
            text = decode(body, ctype) if status == 200 else ""
            if "-->" in text:
                return text, label, host
    return "", "", ""


def video_meta(vid: str) -> dict:
    url = f"https://www.youtube.com/watch?v={vid}"
    status, ctype, body = http_get(
        "https://www.youtube.com/oembed?format=json&url=" + urllib.parse.quote(url, safe="")
    )
    if status == 200 and body:
        try:
            data = json.loads(decode(body, ctype))
            return {"title": data.get("title"), "author": data.get("author_name")}
        except json.JSONDecodeError:
            pass
    return {}


def save_video(vid: str, args: argparse.Namespace, extra: dict | None = None) -> bool:
    directory = REFS / "videos" / vid
    if (directory / "meta.json").exists() and not args.force:
        report("exists", vid, str(directory.relative_to(ROOT)))
        return True
    vtt, label, host = captions_from_invidious(vid)
    if not vtt:
        report("FAILED", vid, "no English captions from any mirror")
        return False
    lines = parse_vtt(vtt)
    body = transcript_markdown(lines)
    meta = {**video_meta(vid), **(extra or {})}
    record = {
        "type": "video",
        "url": f"https://www.youtube.com/watch?v={vid}",
        "title": meta.get("title"),
        "author": meta.get("author"),
        "date": meta.get("date"),
        "duration": meta.get("duration"),
        "site": "youtube.com",
        "via": f"invidious:{host}",
        "caption_track": label,
        "words": len(body.split()),
        "tags": args.tag,
        "collection": args.collection,
    }
    header = front_matter(record) + f"# {record.get('title') or vid}\n\n"
    header += f"Caption track: {label}. Timestamps mark the start of each paragraph.\n\n"
    write_item(directory, record, {"captions.vtt": vtt, "transcript.md": header + body + "\n"})
    report("saved", vid, f"{record['words']} words ({label}) {record.get('title', '')}")
    return True


def cmd_video(args: argparse.Namespace) -> int:
    results = [save_video(video_id(item), args) for item in args.items]
    return 0 if all(results) else 1


def cmd_playlist(args: argparse.Namespace) -> int:
    fmt = "%(id)s\t%(duration)s\t%(title)s"
    proc = subprocess.run(
        ["uvx", "yt-dlp", "--flat-playlist", "--print", fmt, args.items[0]],
        capture_output=True,
        text=True,
        check=False,
    )
    rows = [line.split("\t", 2) for line in proc.stdout.splitlines() if line.count("\t") >= 2]
    if not rows:
        report("FAILED", args.items[0], proc.stderr.strip()[-200:])
        return 1
    ok = True
    for vid, duration, title in rows:
        seconds = int(float(duration)) if duration.replace(".", "").isdigit() else 0
        if args.max_minutes and seconds > args.max_minutes * 60:
            report("skipped", vid, f"{seconds // 60} min > --max-minutes: {title}")
            continue
        extra = {"title": title, "duration": f"{seconds // 60}:{seconds % 60:02d}"}
        ok = save_video(vid, args, extra) and ok
    return 0 if ok else 1


# ---------------------------------------------------------------- X posts


def cmd_post(args: argparse.Namespace) -> int:
    failures = 0
    for item in args.items:
        match = re.search(r"(?:status|statuses)/(\d+)", item) or re.fullmatch(r"(\d+)", item)
        if not match:
            report("FAILED", item, "no status id")
            failures += 1
            continue
        post_id = match.group(1)
        directory = REFS / "posts" / "x" / post_id
        if (directory / "meta.json").exists() and not args.force:
            report("exists", post_id, str(directory.relative_to(ROOT)))
            continue
        status, ctype, body = http_get(f"https://api.fxtwitter.com/status/{post_id}")
        tweet = {}
        if status == 200 and body:
            try:
                tweet = json.loads(decode(body, ctype)).get("tweet") or {}
            except json.JSONDecodeError:
                tweet = {}
        if not tweet.get("text") and not tweet.get("article"):
            report("FAILED", post_id, f"http {status}")
            failures += 1
            continue
        author = tweet.get("author") or {}
        handle = author.get("screen_name", "")
        parts = [tweet.get("text", "").strip()]
        article = tweet.get("article") or {}
        if article:
            parts.append(f"## Article: {article.get('title', '')}\n")
            blocks = ((article.get("content") or {}).get("blocks")) or []
            parts.append("\n\n".join(b.get("text", "") for b in blocks if b.get("text")))
            if article.get("preview_text") and not blocks:
                parts.append(article["preview_text"])
        quote = tweet.get("quote") or {}
        if quote.get("text"):
            quoted_by = (quote.get("author") or {}).get("screen_name", "")
            parts.append(f"> Quoting @{quoted_by}: " + quote["text"].replace("\n", "\n> "))
        media = [m.get("url") for m in ((tweet.get("media") or {}).get("all") or []) if m.get("url")]
        if media:
            parts.append("Media: " + ", ".join(media))
        text = "\n\n".join(p for p in parts if p)
        created = tweet.get("created_at", "")
        try:
            date = dt.datetime.strptime(created, "%a %b %d %H:%M:%S %z %Y").date().isoformat()
        except ValueError:
            date = created
        record = {
            "type": "post",
            "url": tweet.get("url") or f"https://x.com/{handle}/status/{post_id}",
            "title": (tweet.get("text", "") or article.get("title", "")).strip().split("\n")[0][:110],
            "author": f"{author.get('name', '')} (@{handle})",
            "date": date,
            "site": "x.com",
            "via": "fxtwitter",
            "chars": len(text),
            "likes": tweet.get("likes"),
            "replying_to": tweet.get("replying_to_status"),
            "tags": args.tag,
            "collection": args.collection,
        }
        write_item(directory, record, {"post.md": front_matter(record) + text + "\n"})
        report("saved", post_id, f"@{handle} {date} {len(text)} chars")
    return 1 if failures else 0


# ---------------------------------------------------------------- index


def cmd_index(_: argparse.Namespace) -> int:
    items = []
    for meta_path in sorted(REFS.glob("**/meta.json")):
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        # The texts are gitignored, so the name comes from the type, not from what is on disk.
        name = {"video": "transcript.md", "post": "post.md"}.get(meta.get("type"), "article.md")
        meta["path"] = str((meta_path.parent / name).relative_to(REFS))
        items.append(meta)
    titles = {"article": "Articles", "doc": "Documentation", "video": "Video transcripts", "post": "X posts"}
    out = [
        "# Reference index",
        "",
        "Generated by `tools/refs index`. Do not edit by hand.",
        "",
        f"{len(items)} items. Notes distilled from these live in `notes/`. The local files are",
        "not in git; `tools/refs` fetches them (see `README.md`).",
        "",
    ]
    for kind, heading in titles.items():
        group = [i for i in items if i.get("type") == kind]
        if not group:
            continue
        group.sort(key=lambda i: (i.get("collection") or "", i.get("site") or "", i.get("date") or "", i.get("title") or ""))
        out += [f"## {heading} ({len(group)})", "", "| Title | Author | Date | Collection | Local file |", "|---|---|---|---|---|"]
        for item in group:
            title = (item.get("title") or item["url"]).replace("|", "\\|")[:110]
            author = (item.get("author") or item.get("site") or "").replace("|", "\\|")[:40]
            out.append(
                f"| [{title}]({item['url']}) | {author} | {(item.get('date') or '')[:10]} | "
                f"{item.get('collection') or ''} | `{item['path']}` |"
            )
        out.append("")
    (REFS / "INDEX.md").write_text("\n".join(out), encoding="utf-8")
    report("indexed", "refs/INDEX.md", f"{len(items)} items")
    return 0


# ---------------------------------------------------------------- watch


def listed_urls(source: dict) -> list[str] | None:
    """URLs a source currently lists, or None if the listing could not be read."""
    status, ctype, body = http_get(source["list"], timeout=60)
    if status != 200 or not body:
        return None
    text = decode(body, ctype)
    # Sitemaps, llms.txt files, feeds and plain HTML indexes all reduce to "every URL in the text".
    found = re.findall(r"https?://[^\s<>\"')\]]+", text)
    if source.get("base"):
        found += [urllib.parse.urljoin(source["base"], h) for h in re.findall(r'href="(/[^"#?]+)"', text)]
    pattern = re.compile(source["include"])
    return sorted({u.rstrip("/") for u in found if pattern.search(u)})


def cmd_watch(args: argparse.Namespace) -> int:
    config_path = REFS / "sources" / "watch.toml"
    config = tomllib.loads(config_path.read_text(encoding="utf-8"))
    state_dir = REFS / "sources" / "seen"
    state_dir.mkdir(parents=True, exist_ok=True)
    news = 0
    for source in config.get("list", []):
        name = source["name"]
        seen_path = state_dir / f"{name}.txt"
        seen = set(seen_path.read_text(encoding="utf-8").split()) if seen_path.exists() else set()
        current = listed_urls(source)
        if current is None:
            report("FAILED", name, f"could not read {source['list']}")
            continue
        fresh = [u for u in current if u not in seen]
        report("source", name, f"{len(current)} listed, {len(fresh)} new")
        for url in fresh:
            print(f"  new  {url}")
        news += len(fresh)
        if args.mark:
            seen_path.write_text("\n".join(sorted(seen | set(current))) + "\n", encoding="utf-8")
    for page in config.get("page", []):
        name = page["name"]
        hash_path = state_dir / f"{name}.sha256"
        status, ctype, body = http_get(page["url"], timeout=60)
        if status != 200 or not body:
            report("FAILED", name, f"http {status}")
            continue
        digest = hashlib.sha256(body).hexdigest()
        previous = hash_path.read_text(encoding="utf-8").strip() if hash_path.exists() else ""
        if digest != previous:
            news += 1
            report("changed" if previous else "new", name, page["url"])
        else:
            report("same", name)
        if args.mark:
            hash_path.write_text(digest + "\n", encoding="utf-8")
    report("done", "watch", f"{news} new or changed" + ("" if args.mark else " (run with --mark to record this state)"))
    return 0


# ---------------------------------------------------------------- cli


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)
    for name, func in (("article", cmd_article), ("video", cmd_video), ("playlist", cmd_playlist), ("post", cmd_post)):
        p = sub.add_parser(name)
        p.add_argument("items", nargs="+")
        p.add_argument("--tag", action="append", default=[])
        p.add_argument("--collection", default="")
        p.add_argument("--force", action="store_true")
        if name == "article":
            p.add_argument("--via", choices=("auto", "direct", "jina"), default="auto")
        if name == "playlist":
            p.add_argument("--max-minutes", type=int, default=0)
        p.set_defaults(func=func)
    sub.add_parser("index").set_defaults(func=cmd_index)
    watch = sub.add_parser("watch")
    watch.add_argument("--mark", action="store_true", help="record the current state as seen")
    watch.set_defaults(func=cmd_watch)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
