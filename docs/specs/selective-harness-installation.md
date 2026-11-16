# Selective harness installation

## Outcome

From an existing app's directory, a developer can install tackroom's common harness, choose
Codex, Claude Code and/or OpenCode, and add only the skills relevant to that app. The installer
can fetch the template from GitHub without a local tackroom checkout. All common content has
one maintained source under `template/`.

Scope is authorized in [decision 0001](../decisions/0001-selective-harness-installation.md).
This document specifies future behavior; it does not describe a shipped CLI.

## Starting point

- `tools/setup` copies missing files from a local checkout, preserves existing files, supports
  dry run and tracker selection, and adds Codex/OpenCode through flags. It always copies
  Claude's setup and every skill.
- `template/AGENTS.md` is shared; `template/CLAUDE.md` imports it. Shared skill discovery uses
  `template/.agents/skills/` links to `template/.claude/skills/`.
- `template/.codex/hooks.json` calls scripts under `.claude/hooks/`. Reviewer briefs have
  repeated prose across `.claude/agents/`, `.codex/agents/` and `.opencode/agents/`.
- Root `.agents/skills/`, `.claude/` and `.codex/` include dogfooding copies. They must become
  reproducible from the canonical sources, without independent edits to shared prose.
- `tools/check-skill-setup.py`, `tools/check-codex-agents.py`, and `scripts/agent/check` encode
  the existing paths and parity rules. Migrate those checks with the layout.

## Required behavior

1. **One source.** Common instructions, skills including their references/scripts, reviewer
   briefs and hook implementations live once in `template/`. Agent-specific metadata,
   permissions and event mappings remain small adapters. Unsupported controls are explicit;
   adapters must not claim identical enforcement where the agents differ.
2. **Base plus options.** A discoverable catalog identifies the common base, optional skills
   and app/stack profiles, their applicability and dependencies. UI craft is opt-in for UI
   applications and absent from a base-only backend/CLI installation. Profiles reuse the same
   skill sources; they do not fork them. Inventory the existing skills before classifying them.
3. **Select the target.** Installation defaults to the current app directory, can target an
   explicit directory, and supports one or more selected agents independently. Interactive
   selection is optional; documented explicit inputs must work unattended. Missing required
   selection must explain the choices without silently selecting every agent or optional skill.
4. **Review and preserve.** Dry run reports additions, kept files and unresolved conflicts
   without changing the project. Existing project instructions, settings, skills and memory
   are preserved; report collisions and any resulting incomplete setup. Repeated installation
   is safe. Keep the existing tracker choices and avoid modifying global agent configuration.
5. **Remote source.** A documented bootstrap works from an app without cloning tackroom.
   Default to this repository's `main`; accept a specific revision for reproducible installs.
   Resolve the requested revision once and fetch all selected content from that same commit.
   Include hidden files, resources, executable modes and working adapter paths. GitHub raw
   files are permitted; downloading the research corpus is unnecessary.
6. **Failure is visible.** Unknown selections, missing dependencies and failed or malformed
   downloads fail clearly. Fetch and validate selected content before applying it; network
   failure must leave the destination unchanged. Reject paths escaping the destination,
   including through existing symlinks. Never report an incomplete installation as successful.

## Examples to prove

| Request | Expected result |
|---|---|
| Codex + base in a backend app | Base and Codex adapter; no UI craft or Claude/OpenCode setup |
| Claude + UI craft in a web app | Same base, UI craft with resources, Claude adapter |
| All three agents + UI craft | One common source in the installed project, working discovery for each agent |
| Existing app with local instructions and skills | Local bytes preserved, conflicts reported |
| Dry run or failed remote download | No destination changes |
| Install a fixed revision twice | Same selected source; second run preserves local files |

Use disposable fixtures for these examples. Follow the existing multi-harness validation
decision: live Codex where available, installation and configuration checks for all three,
and explicit runtime limits. Static parity does not prove model behavior.

## Delivery

[Epic 7](../../tasks/7-selective-harness-installation.md) has three ordered tasks:

1. [8: Centralize content and define the catalog](../../tasks/8-centralize-harness-template.md).
2. [9: Implement selective local installation](../../tasks/9-selective-local-installation.md).
3. [10: Ship remote bootstrap and documentation](../../tasks/10-github-harness-bootstrap.md).

Before implementation, propose the public command/runtime and canonical layout/catalog format
for owner review. Prefer extending `tools/setup` if it meets the requirements without an
additional distribution service. Exact flags and any package-manager wrapper remain open.
These choices do not block filing inbox tasks; no task is marked ready by this spec.

## Boundaries and evidence

No cross-project registry, automatic sync/update, destructive migration of installed projects,
global setup, package registry requirement, new agent support, or new stack-specific skill
authoring. Existing manual-copy and local-setup users need a documented migration path.
Update stale documentation about the shipped layout when it changes, not during planning.

Shared harness and skill rationale: `docs/other-harnesses.md`, `docs/ui-craft.md`,
`docs/tasks.md`, `refs/notes/harness-codex-opencode-standards.md`, and the source registers
linked from those docs. The installer architecture and profile defaults are judgement calls;
do not present them as findings from the research. Any changed skill or rule retains its
existing source attribution.
