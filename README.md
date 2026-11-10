# claude--template

My agentic coding setup, kept in one place: a project template for Claude Code (with Codex and
OpenCode add-ons), the research it is built from, and notes on why each piece is there. Nothing
here manages other repositories. A project gets the template by copying it, and owns it from
then on.

## What is in here

| Path | What it is |
|---|---|
| `template/` | Mirrors a project root. Instruction files, Claude Code settings, hooks, skills and agents, project memory, task tracking, Codex and OpenCode config, vendor launchers. |
| `prompts/` | Prompts worth reusing, quoted from the people who shared them, with sources. |
| `docs/` | Why the template is shaped this way, with citations into `refs/`. Start with `principles.md`. |
| `refs/` | The research: about 1,650 saved talks, articles, docs and posts, with notes per cluster in `refs/notes/`. |
| `tools/` | `refs` fetches and indexes research. `setup` copies the template into one project. |

## Use it in a project

    tools/setup ~/Dev/my-app                 # Claude Code; picks issues or files for tasks
    tools/setup ~/Dev/my-app --codex --opencode --tracker files --dry-run

It copies files that are not there yet and lists the ones it left alone. It never overwrites,
commits or keeps track of anything. Copying by hand works just as well:
`cp -rn template/. ~/Dev/my-app/`.

Then, in the project:

1. Fill in `AGENTS.md`: the name, the three commands, the first gotcha. Keep it short.
2. Put the project's real commands in `scripts/agent/check` and run it.
3. In `WORKFLOW.md`, keep the tracker line that applies.
4. Start Claude Code there once and accept the trust prompt, so the hooks and allow rules load.
5. Optional: `/sandbox` to switch on the Bash sandbox (see `docs/claude-code.md` first).

## What you get

- **A check the agent must pass.** `scripts/agent/check`, run by the `verify` skill and by a
  hook when a turn ends with changed files.
- **Guardrails enforced by hooks**, not by asking: no reading secret-looking files, no wide
  deletes, no force-push, no push to a protected branch, no merging.
- **Eleven skills**: `spec`, `task`, `verify`, `write-tests`, `performance`, `second-opinion`,
  `wrap-up`, and four you start yourself: `kickoff`, `dream`, `careful`, `lock-tests`.
- **A ratchet** for any number you care about (`scripts/agent/ratchet`): bundle size, queries
  per request, a score. It can only get better.
- **A workflow** (`WORKFLOW.md`): epics and tasks with acceptance criteria that are checks, in
  issues or in files, with evidence on the pull request.
- **Memory that corrects itself**: notes in `.agents/memory/`, and a `dream` pass that reviews
  finished sessions, fixes the notes and proposes changes to the instructions.
- **Other models**: `scripts/agent/claude-with glm|deepseek|kimi|kimi-code`.

## How far to trust it

Run and observed on one machine (Ubuntu 24.04, Claude Code 2.1.322): the hooks, the skills and
agents loading, the memory rules, task selection, the setup script, and one full dream pass.

Written from documentation and not run: everything for Codex, the vendor launchers, the Bash
sandbox configuration, and claiming tasks on GitHub. Each of those files says so at the top.

Not done at all: evals for the skills, and a real task taken through the whole workflow. The
three newest skills (`kickoff`, `write-tests`, `performance`) have only been validated for
format, not used.
`docs/keeping-current.md` lists the gaps in order.

## Docs

- `docs/principles.md`: the twelve principles, what each rests on, and how well it is tested
- `docs/claude-code.md`: the Claude Code files, what belongs in personal settings, the sandbox
- `docs/memory-and-dreaming.md`: the memory tiers and the dream pass
- `docs/loops.md`: turn, goal, time and proactive loops, with the lines to type
- `docs/tasks.md`: tasks, backlog and epics
- `docs/new-project.md`: from an idea to an agent-ready repository; choosing stack and architecture
- `docs/testing.md`: what to test, how to get a model to write real tests, performance
- `docs/other-harnesses.md`: Codex, OpenCode, vendor CLIs, and GLM, DeepSeek and Kimi models
- `docs/keeping-current.md`: the upkeep routine and known gaps

## The research

`refs/README.md` explains the layout and the fetch tool. `refs/INDEX.md` lists every saved item.
The saved texts are other people's writing, kept for private reference: keep this repository
private, or stop tracking `refs/articles`, `refs/videos` and `refs/posts` before publishing it.
