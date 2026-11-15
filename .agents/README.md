# .agents/

Files that agents in any harness share.

- `memory/`: the project's long-term memory. `_index.md` is the catalogue, `inbox.md` is where a
  session notes something worth keeping, and the other files are written by the `dream` pass.
  Outside that pass the files are read-only to agents (a hook enforces it in Claude Code and
  Codex). Changes always arrive as a git diff for you to review.
- `skills/`: links to the skills in `.claude/skills/`, shipped in the template and installed by
  every `tools/setup` run for harnesses that look here (including Codex and OpenCode). References travel with each
  skill. Other agents can read the `SKILL.md` directly through the shared `AGENTS.md` pointer.
- `dream-report.md`: the latest proposals from the `dream` pass, waiting for a decision.
