# tackroom

**One source for your coding-agent harness. Install the parts your project needs.**

tackroom is a research-grounded collection of instructions, skills, hooks, agent roles and
workflows for **Claude Code, Codex and OpenCode**. Its CLI builds each agent's native setup
from a shared template, then installs it into your project. Explicit updates bring in upstream
harness changes while preserving local edits, project memory and dream reports.

A tack room is where riders keep and maintain their equipment. This repository serves that
purpose for coding agents: a place to understand, improve and reuse the setup around them.

[Quick start](#quick-start) · [Updates](#update-an-existing-project) ·
[Philosophy](#philosophy) · [Source layout](#one-source-generated-adapters) ·
[Extending the harness](#extend-the-harness) · [Documentation](#documentation)

## Why a harness?

An agent needs more than a model and a prompt. It needs to know how a project works, how to
check a change, which actions require care, how work is tracked, and what previous sessions
learned. Those surrounding instructions and tools form its **harness**.

tackroom makes that setup explicit and reviewable. It favors small files, executable checks
and clear limits over a large framework. The project owns its installed files; tackroom is
neither a hosted agent platform nor a service that manages your repositories.

## Quick start

Run from the project you want to set up. The installer needs **Python 3.10+**, **curl**, GitHub
network access and a filesystem supporting symlinks. The workflow targets Linux, macOS and WSL;
the recorded end-to-end tests ran on Ubuntu. Install your chosen coding-agent client separately.
Git is recommended for the harness workflow, but not required just to copy the setup.

```sh
cd /path/to/your-project
set -o pipefail  # bash/zsh: propagate a failed download
curl -fsSL https://raw.githubusercontent.com/PedramRZM/tackroom/main/tools/install | python3 - --agents codex
```

No tackroom clone, package manager or global configuration change is required. The command
resolves `main` to a commit and prints that revision. It downloads the installer and selected
source files from that commit, verifies their contents, and generates native configuration.

For a UI application using all three agents:

```sh
curl -fsSL https://raw.githubusercontent.com/PedramRZM/tackroom/main/tools/install | python3 - --agents claude,codex,opencode --profile ui
```

Use `--dry-run` before applying an installation. Use `--list` to see agents, base skills,
optional capabilities and profiles. Review downloaded code before executing it if that is your
normal policy; the bootstrap and installer are small Python scripts under [`tools/`](tools/).

### Finish the project setup

1. Fill in `AGENTS.md`: project purpose, exact commands and the gotchas an agent cannot infer.
2. Replace the placeholder in `scripts/agent/check` with your actual checks, then run it.
3. Keep the appropriate tracker line in `WORKFLOW.md`. Choose `--tracker files` or
   `--tracker issues` explicitly when installing if needed.
4. Start the selected agent and review its project trust/configuration prompts.

Installing a configuration does not make it trusted or prove its hooks are active. Existing
files are preserved and reported, so resolve any installation conflicts before relying on the
setup. The installer does not commit your project or change your global agent settings.

## Choose what to install

The common base is included for every selected agent. UI, performance and new-project
capabilities are optional; the CLI does not infer a stack or silently install every skill.

| Selection | What it provides |
|---|---|
| Common base | Instructions, workflow, checks, memory skeleton, shared hooks and agent roles |
| Base skills | `spec`, `task`, `write-tests`, `verify`, `second-opinion`, `wrap-up`, `dream`, `careful`, `lock-tests` |
| `--profile ui` or `--skills ui-craft` | UI states, layout, typography, motion and interaction verification |
| `--profile new-project` or `--skills kickoff` | Take a new project idea to a small, running repository |
| `--skills performance` | Measure a performance problem, improve it and verify the gain |

Select agents independently with `--agents claude`, `--agents codex`, `--agents opencode`,
or a comma-separated combination. Codex-only installation does not create a `.claude/`
directory. Dependencies and skill resources travel with each selected capability.

| Option | Behavior |
|---|---|
| `[project-directory]` | Install into an explicit existing directory; defaults to the current directory |
| `--agents <names>` | Select one or more agents; required for a new untracked project |
| `--skills <names>` | Add optional skills; repeat the option or use comma-separated names |
| `--profile <names>` | Select groups of skills for an app type |
| `--tracker files\|issues` | Choose task storage; defaults to issues for a GitHub origin, files otherwise |
| `--list` | Show the available catalog without modifying the project |
| `--dry-run` | Preview additions, updates, retained files and conflicts without writing |
| `--ref <branch\|tag\|SHA>` | Select a GitHub revision; defaults to `main` |
| `--update` | Update unchanged managed files, remembering the project's previous selections |

Profiles currently cover UI applications and new projects. They reuse the same skill sources;
there are no separate React, Python or Rust copies of the shared harness. Skills should apply
only where their guidance is relevant, and projects should remove guidance they do not need.

## Update an existing project

Run this from the project to get the latest version of its selected harness:

```sh
curl -fsSL https://raw.githubusercontent.com/PedramRZM/tackroom/main/tools/install | python3 - --update
```

The CLI remembers selections and installed source fingerprints in
`.agents/tackroom-install.json`. Keep that file in version control with the harness.
It contains no memory or transcript content.

| Existing content | What an update does |
|---|---|
| Harness file unchanged locally | Applies the upstream version |
| Locally edited harness file, upstream unchanged | Keeps the customization |
| Both local and upstream versions changed | Keeps the local file and reports a conflict |
| Existing memory, inbox, index, dream reports, transcripts, project docs and tasks | Preserves them; never replaces or deletes project knowledge |
| File removed upstream or no longer selected | Retains it and reports it; no automatic pruning |

Conflicts return exit code **2**. Nonconflicting files can still update; compare the named paths
with the printed source commit and merge manually. There is no force-overwrite switch.
`AGENTS.md`, `WORKFLOW.md` and your customized check script follow the same preservation rules.

Use `--update --dry-run` to preview. Downloads and source validation finish before project
writes begin, so a failed download leaves project files and tracking unchanged. Individual
file writes are atomic; local disk or permission failures can leave earlier files installed.
Run updates while other tools are not changing the same files, and rerun after resolving a failure.

For a project without tracking, run an installation with explicit selections once. Missing
files are installed, identical files can be adopted, and different existing files remain
untouched. See the [installation guide](docs/installation.md) for legacy layouts and conflicts.

There is **no central registry, background sync or cross-project management**. Updates happen
only when you run the command in a project. For reproducible installs, pass a full commit SHA
with `--ref`; pin the bootstrap URL to that SHA as well when you need the bootstrap itself fixed.

## Philosophy

The template is opinionated about the process, but its reasoning is available for inspection.
Each principle links to the research and implementation notes in [the design rationale](docs/principles.md).

1. **Make verification executable.** A project-specific check command is more useful than a
   promise to “be careful.” A change should end with evidence that someone else can reproduce.
2. **Separate writing from judging.** Tests, actual user journeys and independent review can
   expose mistakes that the author shares with its own explanation. No single check proves everything.
3. **Use code for enforceable boundaries.** Hooks and permissions can block defined actions;
   prose expresses preferences. A hook is a guardrail, not a sandbox or an external trust boundary.
4. **Keep instructions small.** Session-start text competes for attention. Put task-specific
   detail in skills and references, and remove guidance the code already makes clear.
5. **Keep work durable.** Tasks, decisions, evidence and handoffs belong in project files or a
   tracker, so another person or agent can continue without reconstructing a conversation.
6. **Treat memory as something to maintain.** Sessions append observations; the dream workflow
   reviews and corrects them. An installer must never treat project knowledge as replaceable boilerplate.
7. **Share sources, respect host differences.** A skill or agent brief is authored once.
   Native configuration is generated, while unsupported permissions or hooks remain explicitly unsupported.
8. **Let the project own its setup.** Installed files are editable. Updates preserve local
   choices instead of enforcing a global configuration or silently resetting a project.
9. **State the limits of the evidence.** Configuration parsing, skill discovery, model behavior
   and enforcement are different claims. A successful install should not be presented as proof of all four.

These are design choices informed by research, not a guarantee that one harness improves every
model or project. Packaging, profile defaults and update policy are explicitly documented as
product judgments in the [decision record](docs/decisions/0001-selective-harness-installation.md).

## One source, generated adapters

There are no `.claude/`, `.codex/` or `.opencode/` setup directories in `template/`.

```text
template/
├── AGENTS.md                       # Shared project instructions
├── WORKFLOW.md                     # Shared task workflow
├── .agents/
│   ├── adapters.json               # Native configuration definitions
│   ├── skills/<name>/
│   │   ├── SKILL.md                # One skill body
│   │   ├── install.json            # Applicability, dependencies and profiles
│   │   └── references/             # Optional supporting material
│   ├── briefs/<name>.md            # One agent-role instruction body
│   ├── briefs/<name>.json          # Description and supported native metadata
│   ├── hooks/                      # Shared executable hook logic
│   └── memory/                     # Initial project-memory skeleton
├── scripts/agent/                  # Check, task selection and supporting tools
├── docs/                           # Initial decision/spec/plan structure
├── tasks/                          # Optional file tracker
└── .github/                        # PR and optional issue templates
```

The installer discovers the source files and renders only the selected native setup. Claude
skill discovery points to the same `.agents/skills/` content that Codex and OpenCode read.
Agent-role instructions render into each host's required format; native permissions and event
mappings remain host-specific. No generated adapter copy or download manifest is maintained
inside the template.

This repository also uses its own harness. Its root shared paths point to the canonical
sources; native runtime files are generated and gitignored. Refresh them with:

```sh
tools/render-harness --write --dogfood
```

## Extend the harness

**Add or edit a skill in one folder:** `template/.agents/skills/<name>/`. Keep the skill text
and resources there, with an `install.json` such as:

```json
{
  "base": false,
  "applies_to": "Projects that need this capability",
  "requires": ["verify"],
  "profiles": {}
}
```

The CLI discovers the folder automatically; there is no second catalog or per-agent copy to
edit. `profiles` maps profile names to descriptions. Dependencies must name existing skills
and cannot form cycles. Keep `SKILL.md` front matter valid and its name consistent with the folder.

**Change an agent role once:** edit its body and metadata under `template/.agents/briefs/`.
The CLI builds supported native role files from that body. **Change native configuration** in
`template/.agents/adapters.json`, and **change shared hook logic** in `template/.agents/hooks/`.
Native syntax differences do not imply equivalent runtime support across agents.

New guidance should trace to the research in `refs/` and explain its reasoning in `docs/`.
Label unsupported choices as judgments. Prefer a focused improvement or removal to accumulating
more instructions. Refresh dogfooding outputs and run the checks before submitting a change.

## Work from a local checkout

```sh
git clone https://github.com/PedramRZM/tackroom.git
cd tackroom
tools/render-harness --write --dogfood
tools/setup /path/to/project --agents codex --profile ui --dry-run
tools/setup /path/to/project --agents codex --profile ui
```

`tools/setup` uses the checkout's local template. Add `--remote` to fetch GitHub instead.
`tools/setup /path/to/project --update` applies local source changes with the same preservation
rules as the public bootstrap.

Legacy `--codex` and `--opencode` flags mean “add to Claude with all skills” and print a notice.
Use `--agents` for independent selection. `--legacy` explicitly requests the old default;
a bare new installation now requires a selection. Copying `template/` alone does not generate
native configuration—use the CLI. See [migration details](docs/installation.md#local-checkout-and-compatibility).

## Verification and supported scope

```sh
scripts/agent/check           # Full repository checks and native validators
scripts/agent/check --quick   # Skip the slower native validators
python3 tools/test_setup.py  # Focused installer/update regression suite
```

The check covers compilation, configuration parsing, canonical-source/native-output parity,
installation and update behavior, guard tests, instruction limits, source quotes and validators.
The repository's tooling also uses `uv` for Python 3.11+ parsing checks and Claude Code for its
native validators; the installer itself needs only Python 3.10's standard library.

Current installation evidence includes **24 regression tests**, an independent review, and
actual GitHub bootstrap/install/update runs. Fixtures cover one-agent and combined selections,
resources, modes, links, dry runs, local edits, protected project data, bad downloads and malformed
remote file trees. See [the acceptance evidence](docs/evidence/7-selective-harness/README.md).

| Target | Observed validation | Remaining limits |
|---|---|---|
| Codex | Native configuration parses; shared files read in bounded live scratch runs | Untrusted project configuration was disabled; full hook/permission lifecycle is unverified |
| Claude Code | Generated installation, configuration checks and native validators | Latest live probe stopped at account verification before a model response |
| OpenCode | Generated installation and configuration checks | No live model trial for this installer change |

Claude-specific skill hooks and tool restrictions do not automatically become equivalent
controls elsewhere. The dream exporter currently targets Claude transcripts; Codex role
availability does not establish a complete native Codex dream workflow. Vendor launchers have
not been exercised against live endpoints. See [portability and limitations](docs/other-harnesses.md).

## Research and attribution

The library draws on published work from Anthropic, OpenAI, agent-tool maintainers and
practitioners, together with conference talks and saved primary documentation. Sources are
indexed in [`refs/INDEX.md`](refs/INDEX.md); topical notes connect individual claims to their
sources and record disagreements and limits. [`prompts/`](prompts/README.md) contains attributed,
verbatim prompt examples rather than unattributed rewrites.

Saved third-party article text and transcripts are not distributed in git. The repository
tracks source metadata; use `tools/refs` to fetch texts locally. A fresh clone cannot pass the
`prompts-verbatim` check until the sources cited by `prompts/README.md` have been fetched.
See [the research workflow](refs/README.md) before adding or refreshing sources.

## Documentation

| Guide | Covers |
|---|---|
| [Installation and updates](docs/installation.md) | Commands, revision pinning, preservation, conflicts and migration |
| [Principles](docs/principles.md) | Design choices, source evidence and tradeoffs |
| [Claude Code](docs/claude-code.md) | Native settings, trust, hooks and sandbox considerations |
| [Other harnesses](docs/other-harnesses.md) | Codex/OpenCode portability and known differences |
| [Tasks and workflow](docs/tasks.md) | Acceptance criteria, trackers, review and handoff |
| [Testing](docs/testing.md) | Verification planning, test selection and evidence |
| [UI craft](docs/ui-craft.md) | Interface behavior, visual details and relevant checks |
| [Memory and dreaming](docs/memory-and-dreaming.md) | Memory ownership, correction and review |
| [Starting projects](docs/new-project.md) | Kickoff, scope and architectural decisions |
| [Loops](docs/loops.md) | Native goals, execution limits and bounded runs |
| [Keeping current](docs/keeping-current.md) | Source maintenance and known validation gaps |

## License

[MIT](LICENSE) covers the original template, tools and documentation. Quoted third-party material
remains its authors' work and is attributed at its source.
