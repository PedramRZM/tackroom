# template/

The agent-neutral source of the harness. There are no native agent setup directories here.
The CLI reads these sources and builds native configuration only in the destination project.
See [installation and updates](../docs/installation.md).

| Source | Author here once |
|---|---|
| `AGENTS.md`, `WORKFLOW.md` | Common instructions and task workflow |
| `.agents/skills/<name>/SKILL.md` and resources | Skill text, references and scripts |
| `.agents/skills/<name>/install.json` | That skill's base/optional status, applicability, dependencies and profiles |
| `.agents/hooks/` | Shared hook implementations |
| `.agents/briefs/<name>.md` and sibling JSON | Shared agent instructions, description and supported native metadata |
| `.agents/adapters.json` | Native configuration definitions; CLI builds selected output files |
| `scripts/agent/` | Check placeholder, task selection, ratchet and optional vendor launcher |
| `.agents/memory/`, `docs/`, `tasks/` | Initial project skeletons; existing knowledge is never updated |
| `.github/` | PR template and optional issue tracker forms |
| `gitignore.additions` | Missing entries appended to a project's ignore file |

Add or edit a skill only in its folder. The CLI discovers it without a separate maintained
catalog or generated manifest. Common briefs render into native agent files at install time;
Claude discovery links point to the same `.agents/skills/` read by Codex and OpenCode.
Native controls still differ; no equivalent enforcement is claimed where a host lacks it.

For this repository's own runtime, run `tools/render-harness --write --dogfood`, then
`scripts/agent/check`. Generated native root files are gitignored. They are outputs, not sources.
Copying this directory alone no longer installs native configuration: use the CLI to generate it.

After installation, customize `AGENTS.md` and `scripts/agent/check`, select the workflow tracker,
and review native trust prompts. Later `--update` remembers choices, updates unchanged harness
files, preserves local edits, and never overwrites existing memory, dream reports or project notes.
