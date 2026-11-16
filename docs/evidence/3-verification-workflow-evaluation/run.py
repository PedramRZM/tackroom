#!/usr/bin/env python3
"""Explicit, bounded Codex evaluation; running this spends model usage."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import time

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
REVISIONS = {"old": "b8ce42c", "new": "9731d98", "candidate": "9731d98"}


def git(*args):
    return subprocess.check_output(["git", "-C", str(REPO), *args])


def guidance(root, config):
    revision = REVISIONS[config]
    paths = git("ls-tree", "-r", "--name-only", revision,
                "template/.claude/skills/write-tests", "template/.claude/skills/verify",
                "template/.claude/skills/ui-craft").decode().splitlines()
    for path in paths:
        target = root / ".agents/skills" / Path(path).relative_to("template/.claude/skills")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(git("show", revision + ":" + path))
    if config == "candidate":
        path = root / ".agents/skills/write-tests/SKILL.md"
        anchor = "addition with its limits and maintenance cost; do not install a catalog of tools by default.\n"
        reminder = (HERE.parent / "1-verification-before-implementation/rejected-omission-audit.diff").read_text()
        lines = [line[1:] for line in reminder.splitlines() if line.startswith("+") and not line.startswith("+++")]
        original = path.read_text()
        assert original.count(anchor) == 1
        path.write_text(original.replace(anchor, anchor + "\n" + "\n".join(lines).strip() + "\n"))
    files = sorted((root / ".agents/skills").rglob("*"))
    return {str(p.relative_to(root)): {"sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
                                     "bytes": p.stat().st_size, "lines": len(p.read_text().splitlines())}
            for p in files if p.is_file()}


def run(config, repetition, planning=False):
    name = ("planning-" if planning else "coding-") + config + "-" + str(repetition)
    output = HERE / "runs" / name
    output.mkdir(parents=True, exist_ok=False)
    root = Path(tempfile.mkdtemp(prefix="tackroom-eval-" + name + "-"))
    if planning:
        shutil.copy(HERE / "planning.md", root / "task.md")
    else:
        shutil.copytree(HERE / "fixture", root, dirs_exist_ok=True)
        (root / "scripts/agent/check").chmod(0o755)
    manifest = guidance(root, config)
    subprocess.run(["git", "init", "-q", str(root)], check=True)
    subprocess.run(["git", "-C", str(root), "add", "."], check=True)
    command = ["timeout", "--signal=TERM", "--kill-after=10s", "180s", "codex", "exec",
               "--ignore-user-config", "--ephemeral", "--sandbox", "read-only" if planning else "workspace-write",
               "-c", 'approval_policy="never"', "-m", "gpt-6.1-sol", "-c", 'model_reasoning_effort="low"',
               "--json", "--color", "never", "-o", str(output / "answer.md"),
               "Read task.md and the named skills, then carry out the request. Work only in this scratch directory."]
    start = time.monotonic()
    with (output / "events.jsonl").open("w") as stdout, (output / "stderr.txt").open("w") as stderr:
        result = subprocess.run(command, cwd=root, stdout=stdout, stderr=stderr)
    metadata = {"config": config, "revision": git("rev-parse", REVISIONS[config]).decode().strip(),
                "fixture": "planning.md" if planning else "fixture", "root": str(root),
                "command": command, "exit": result.returncode, "elapsed_seconds": round(time.monotonic()-start, 3),
                "guidance": manifest}
    if not planning:
        final = output / "final"
        shutil.copytree(root, final, ignore=shutil.ignore_patterns(".git", ".agents", "__pycache__"))
        judged = subprocess.run(["python3", str(HERE / "score.py"), str(final)], capture_output=True, text=True)
        (output / "score.json").write_text(judged.stdout)
        (output / "score-stderr.txt").write_text(judged.stderr)
        metadata["score_exit"] = judged.returncode
        metadata["suite_exits"] = []
        for attempt in (1, 2):
            with (output / f"suite-{attempt}.txt").open("w") as stream:
                try:
                    checked = subprocess.run(["sh", "scripts/agent/check"], cwd=final, stdout=stream,
                                             stderr=subprocess.STDOUT, timeout=30)
                    metadata["suite_exits"].append(checked.returncode)
                except subprocess.TimeoutExpired:
                    metadata["suite_exits"].append(124)
        (output / "change.diff").write_bytes(subprocess.check_output(["git", "diff"], cwd=root))
    (output / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n")
    print(json.dumps({k: v for k, v in metadata.items() if k not in ("guidance", "command")}), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", choices=REVISIONS)
    parser.add_argument("repetition", type=int)
    parser.add_argument("--planning", action="store_true")
    args = parser.parse_args()
    run(args.config, args.repetition, args.planning)
