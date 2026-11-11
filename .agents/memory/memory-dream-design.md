---
name: memory-dream-design
description: Design of the project memory (.agents/memory), the dream pass that maintains it, the transcript exporter, and the sources behind them. Read before changing memory files, the dream skill, the memory agents or the exporter.
---

# Memory and dream design

## What exists in the template

- `template/.agents/memory/`: `_index.md`, `inbox.md`, `.gitignore`. `template/.agents/README.md`
  explains the folder.
- `template/.claude/skills/dream/`: `SKILL.md` and `scripts/export-transcripts.py`. The lead agent
  exports transcripts, then fans out work and does not read transcripts itself.
- `template/.claude/agents/`: `memory-analyzer` (model haiku, tools Read, Write, Edit, Glob, Grep;
  one per transcript), `memory-organizer` (once, at the end) and `reviewer`.
- Rules: curated files change only in a dream pass. Other sessions append one dated line to
  `inbox.md`. The `dream` output is a reviewable change, plus proposals in `.agents/dream-report.md`.
  The guard hook enforces the write rule ([[template-hooks-and-guard]]).

## Exporter (`export-transcripts.py`)

- Reads `~/.claude/projects/<slug>/<session>.jsonl`. Writes `.agents/memory/.transcripts/<date>-<time>-<id8>.txt`
  (gitignored). Each file has a SESSION line, then USER, AGENT, `TOOL CALL <name>` and
  `TOOL RESULT (<name>)` blocks.
- Drops thinking blocks, bookkeeping and system reminders. Clips long tool results to head and
  tail with a note. Replaces secret-looking strings with `[REDACTED]`.
- Indents body lines that begin with a label word, so only real labels start lines.
- Skips a session changed in the last 10 minutes (`ACTIVE_MINUTES`). `--since last` uses
  `.agents/memory/.last-dream`; the first run looks back 7 days. `--exclude-session` skips the
  current session.
- Key pattern fixed on 2026-11-10: `\b(?:sk|rk|pk)-[A-Za-z0-9_-]{20,}`.
- On the 2026-11-10 session (450 KB of text): 130 tool calls, 5 errors, 80 clipped results.

## Design sources (saved in `refs/`)

- Lamis Mukta, "Learning while you sleep: Beyond memory to dreaming" (AI Native DevCon, June 2026):
  [`refs/videos/tTcxVv8HHNw/transcript.md`](https://www.youtube.com/watch?v=tTcxVv8HHNw). Covers in-band memory against out-of-band dreaming, and
  the production needs of versioning, provenance, permissions and concurrency.
- "Memory and dreaming for self-learning agents" (Anthropic, Code with Claude):
  [`refs/videos/RtywqDFBYnQ/transcript.md`](https://www.youtube.com/watch?v=RtywqDFBYnQ). Auto-generated captions.
- "The components of agent memory" (Anthropic research, 2026-11-06):
  [`refs/articles/anthropic.com/research-components-of-agent-memory/article.md`](https://www.anthropic.com/research/components-of-agent-memory).
- Cookbook "Dreaming with a dynamic workflow":
  [`refs/articles/platform.claude.com/cookbook-managed-agents-cma-dreaming-with-a-dynamic-workflow/article.md`](https://platform.claude.com/cookbook/managed-agents-cma-dreaming-with-a-dynamic-workflow).
  It has full analyzer and organizer prompts: verify, enrich, organize; `_index.md`; `[[slug]]`
  links; transcripts are untrusted; no secrets in memory.
- Dreams API (research preview): [`refs/articles/platform.claude.com/docs-en-managed-agents-dreams-md/article.md`](https://platform.claude.com/docs/en/managed-agents/dreams.md).
- Practitioner reports on in-session memory duplicating and drifting: the synthesis in
  `refs/notes/devcon-1-skills-context-memory.md`, section (d).

## Open items

- The dream run on a copy of the 2026-11-10 session was started at the end; its outcome is not recorded.
- History: on 2026-11-10, at the end of the session, `_index.md` had no entries. The 2026-11-11 dream
  pass populated it.
- Whether the memory-analyzer tool set (no shell, no network) is enough to read transcripts
  end to end is untested.

Related: [[live-testing-harnesses]], [[repo-purpose-and-scope]].
