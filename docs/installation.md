# Install and update the harness

Run these commands **inside your app**. You need Python 3.10+, curl, network access to GitHub,
and a filesystem supporting symlinks (Linux, macOS or WSL). No tackroom clone or package install
is needed. Git is optional; without it, task tracking defaults to files.

```sh
# In bash/zsh, retain download failures when piping to Python.
set -o pipefail
curl -fsSL https://raw.githubusercontent.com/PedramRZM/tackroom/main/tools/install | python3 - --agents codex
```

Choose one or more agents: `claude`, `codex`, `opencode`. For a UI app using all three:

```sh
curl -fsSL https://raw.githubusercontent.com/PedramRZM/tackroom/main/tools/install | python3 - --agents claude,codex,opencode --profile ui
```

Preview with `--dry-run`. List the catalog with `--list`. Use an explicit directory as the
positional argument, `--tracker files|issues` to choose task storage, and `--ref <commit-or-tag>`
to pin a version. Branch references resolve once; the installer and payloads use the printed
commit SHA. The CLI reads the pinned template tree from GitHub and verifies raw downloads against its Git
blob hashes before changing project files. This checks source consistency, not signed provenance.

After installation, fill in `AGENTS.md`, put real checks in `scripts/agent/check`, select the
tracker line in `WORKFLOW.md`, and review your agent's project trust prompts. The check script
is a placeholder until customized. Installing configuration does not imply it has been trusted.

## Get the latest changes

From the same project, run:

```sh
curl -fsSL https://raw.githubusercontent.com/PedramRZM/tackroom/main/tools/install | python3 - --update
```

The project-local `.agents/tackroom-install.json` remembers agent/skill/profile/tracker choices
and source fingerprints. Keep it in version control with the harness. It contains no project
memory or report content. Nothing is registered centrally, and no background process runs.

- A harness file unchanged since installation can receive the upstream version.
- A locally edited harness file is kept. If upstream also changed, it is reported as a conflict
  with exit code 2; if upstream is unchanged, the customization is simply retained. Other
  nonconflicting files can still install/update. Compare the named path with the printed source
  commit and merge manually; there is no force-overwrite switch. Customized `AGENTS.md`,
  `WORKFLOW.md` and `scripts/agent/check` follow this same rule.
- Existing `.agents/memory/` content (including index, inbox and transcripts), dream reports,
  `docs/` and `tasks/` are never replaced or deleted. Initial installs seed missing template
  skeletons only; subsequent tracked runs do not recreate missing project-data files.
- Files removed upstream or excluded by a changed selection remain in the project and are
  reported as retained. Updates do not prune old files or uninstall an agent.
- `--dry-run --update` previews changes without modifying files or tracking. Failed downloads
  likewise leave the project unchanged. Individual file writes are atomic; a local disk or
  permission failure midway is reported and may leave earlier files installed. Rerun after fixing it.

Without prior tracking, run with `--agents ...` once. Missing files install, matching files
become tracked, and different existing files stay untracked and are reported. Legacy internal
skill links are preserved. Broken or escaping links need manual correction before installation;
paths escaping the project are refused. Run updates while other tools are not editing the same files.

## Common base and optional capabilities

Every selected agent gets the same common instructions, memory skeleton and nine base skills:
`spec`, `task`, `verify`, `write-tests`, `second-opinion`, `wrap-up`, `dream`, `careful`, `lock-tests`.
The last three retain their existing host-specific limitations; availability is not enforcement.

| Optional skill | Select directly | Profile | Applies to |
|---|---|---|---|
| UI craft | `--skills ui-craft` | `--profile ui` | Apps with interfaces, any framework |
| Kickoff | `--skills kickoff` | `--profile new-project` | Starting an application |
| Performance | `--skills performance` | — | Work with a measured performance target |

Repeat options or use comma-separated names. Dependencies are selected automatically. No stack
is inferred. The catalog can grow with researched capabilities; there are no fabricated
framework-specific skills. On subsequent runs omitted options retain their previous values;
`--skills ''` or `--profile ''` clears an optional selection without deleting its existing files.

## Local checkout and compatibility

```sh
/path/to/tackroom/tools/setup --agents codex --profile ui --dry-run
/path/to/tackroom/tools/setup --agents codex --profile ui
/path/to/tackroom/tools/setup --update
```

A local checkout uses its local template; add `--remote` to fetch GitHub. In a new project,
selection is required: the old bare `tools/setup <dir>` now explains `--agents` and exits.
`--legacy` explicitly reproduces the old default (Claude and all skills). The old `--codex`
and `--opencode` flags still mean **add to Claude with all skills** and print a compatibility
notice. Use `--agents codex` for Codex alone. Do not mix legacy and new selection flags.
The template now contains only canonical sources, so copying it alone does not create native
agent configuration. Existing manually copied projects should run the installer with explicit
selections once to adopt matching files safely. Local differences are kept and reported.

## Maintain the source

There are no `.claude/`, `.codex/` or `.opencode/` directories in `template/`.

- **Skill:** edit `template/.agents/skills/<name>/SKILL.md` and its resources. Its sibling
  `install.json` declares base/optional, applicability, dependencies and profiles. Add a new
  skill in that one folder; the CLI discovers it automatically. No second registry to edit.
- **Agent instructions:** edit `template/.agents/briefs/<name>.md`; the sibling JSON holds
  its description and supported native metadata. The CLI emits native agent files from it.
- **Hooks:** edit `template/.agents/hooks/` once; each native adapter references these scripts.
- **Config:** edit `template/.agents/adapters.json`. Only native syntax and supported controls
  differ by host. The CLI builds the requested native files from these definitions.

No generated template or download manifest is checked in. Local installs discover source files;
remote installs discover the pinned template tree. Every source edit is picked up automatically.
`tools/render-harness --write --dogfood` refreshes this repository's own runtime files, then
`scripts/agent/check` checks them. These root native files are generated and gitignored;
canonical source files are the only maintained text. Root skill pointers are symlinks, and
project memory and root `AGENTS.md` stay local.

Packaging and base/profile classification are product judgement calls, authorized in
[decision 0001](decisions/0001-selective-harness-installation.md). Shared guidance retains the
research cited in [principles](principles.md), [UI craft](ui-craft.md) and
[other harnesses](other-harnesses.md). GitHub ref resolution uses its documented
[get-commit endpoint](https://docs.github.com/en/rest/commits/commits#get-a-commit).

Template inventories use GitHub's [Git trees endpoint](https://docs.github.com/en/rest/git/trees#get-a-tree), restricted to the template subtree.
