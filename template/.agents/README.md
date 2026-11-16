# .agents/

Files that agents in any harness share.

- `memory/`: the project's long-term memory. `_index.md` is the catalogue, `inbox.md` is where a
  session notes something worth keeping, and the other files are written by the `dream` pass.
  Outside that pass the files are read-only to agents (a hook enforces it in Claude Code and
  Codex). Changes always arrive as a git diff for you to review.
- `skills/`: canonical shared skills and their resources. Claude's discovery links point here;
  Codex and OpenCode discover this directory directly. Only selected optional skills are installed.
- `hooks/` and `briefs/`: shared hook implementations and agent instructions. Native agent
  files are generated during installation; host-specific controls still differ.
- `tackroom-install.json`: installed source fingerprints and selections for explicit updates.
  Keep it with the project. Updates preserve local edits and never replace existing memory,
  reports, transcripts or project notes. It contains no memory or transcript content.
- `dream-report.md`: the latest proposals from the `dream` pass, waiting for a decision.
