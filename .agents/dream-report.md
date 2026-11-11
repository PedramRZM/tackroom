# Dream report: 2026-11-11

Sessions analyzed: 1 of 1   Not analyzed: none
Memory: 8 topic files added and indexed, one stale open item rewritten; review with `git diff .agents/memory`

## Proposals

### 1. AGENTS.md records a workaround for the owner's secrets hook that the owner's own rules forbid
Seen in: 1 session (20261110-1849-c6618e80.txt)
Evidence: hook said `BLOCKED ... would read credentials`; the agent answered "Writing these files with the file tool instead", and AGENTS.md later made that a convention. `~/.claude/CLAUDE.md` says: if a hook stops you, don't route around it, explain and let the owner run it.
Proposed change: Rung 3, `AGENTS.md` Gotchas. Reword the "owner's own hooks reject shell commands..." bullet to end with "If a hook blocks a command, stop and tell the owner; do not switch tools to get past it. Test fixtures that need such words are written by the owner." (Or ask the owner whether file-tool writes of fixtures are in fact allowed, and say so explicitly.)
Why this rung: the line is read every session and currently contradicts the owner's global rule; no check can detect it.

### 2. Large feature built before confirming scope (sync engine and registry, later deleted)
Seen in: 1 session, with real damage (a tool, a module and 11 tests built, then removed)
Evidence: owner: "i dont want to make this a single source of truth among all projects ... i dont need orchestration over projects here."; agent then ran `rm -f tools/projects tools/projects.py tools/tests/test_projects.py`.
Proposed change: none new. AGENTS.md already states "This repository does not manage other projects ... decided by the owner", which prevents a repeat.
Why this rung: already covered at rung 3.

## Considered and left in memory
- Bash sandbox enabled without checking bubblewrap/AppArmor: already in AGENTS.md Gotchas and `docs/claude-code.md`.
- Extractor drops tables and code, duplicate refetched folders left unindexed, no `tools/refs index` after the jina refetch: single session, no damage; a candidate for a check later if it recurs (`tools/refs index` failing on duplicate slugs).
