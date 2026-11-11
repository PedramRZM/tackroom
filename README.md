# tackroom

Dotfiles for coding agents. A tack room is where the harness, bridle and saddle are kept,
mended and fitted before a ride. This repository is the same thing for agent harnesses: the
instruction files, settings, hooks, skills, subagents, memory and workflow that make Claude
Code (plus Codex and OpenCode) work well on a real project, with the research behind every
piece.

## The ideology

Coding agents are capable but unreliable. Most of what makes them useful is not the model.
It is the harness around it: what it can check, what it is not allowed to do, what it
remembers, and who reviews its work. A harness is configuration, so it can be versioned,
reviewed and shared like dotfiles. That is what this repository does.

The rules behind it:

- **Copy, don't sync.** A project gets the template by copying it and owns the files from
  then on. There is no package, no registry and no update channel. Projects drift, and that
  is fine. Pull improvements in by hand when you want them.
- **Every piece is backed by evidence.** A rule, hook or skill traces to a source in `refs/`
  (talks, docs, posts and essays from the people building and using these tools), and
  `docs/` cites it. Anything without a source is labelled a judgement call.
- **Enforce, don't ask.** If something must always or never happen, it is a hook, a
  permission or a check, not a sentence in a prompt. Prose is for preferences.
- **Give the agent a check it must pass.** One command answers "is this healthy?". It is
  quiet when things pass and loud when they fail, and it runs again when a turn ends.
- **The writer does not grade its own work.** Reviews come from fresh-context subagents
  whose job is to prove the change wrong, and tests that define "done" can be locked.
- **Short instructions, pruned often.** Instruction files are read every session, so every
  line has a cost. Removing guidance is preferred to adding it.
- **State lives in files.** Tasks, plans, evidence and memory are plain files or tracker
  issues, not conversation history, so any session (or another harness) can pick work up.
- **Memory corrects itself.** Notes are plain markdown. A periodic `dream` pass reads
  finished sessions, fixes the notes and proposes changes to the instructions.
- **Say how far to trust it.** Every part says whether it was run, only written from docs,
  or not done.

`docs/principles.md` sets out twelve principles, each with its sources and test status.

## How it works

| Path | What it is |
|---|---|
| `template/` | Mirrors a project root. Instruction files, Claude Code settings, hooks, skills and agents, project memory, task tracking, Codex and OpenCode config, vendor launchers. |
| `docs/` | Why the template is shaped this way, with citations into `refs/`. Start with `principles.md`. |
| `refs/` | The research index: about 1,650 talks, articles, docs and posts (URL, author, date), plus distilled notes per topic in `refs/notes/`. |
| `prompts/` | Prompts worth reusing, quoted word for word from the people who shared them, with sources. |
| `tools/` | `setup` copies the template into a project. `refs` fetches and indexes the research. |

The repository runs on its own template. The root `.claude/`, `CLAUDE.md` and
`scripts/agent/` files are copies of `template/`, and the check fails if they drift apart.

### Put it in a project

    tools/setup ~/code/my-app                 # Claude Code; asks whether tasks live in issues or files
    tools/setup ~/code/my-app --codex --opencode --tracker files --dry-run

It copies the files that are missing and lists the ones it left alone. It never overwrites,
commits or keeps track of anything. Copying by hand works too:
`cp -rn template/. ~/code/my-app/`.

Then, in the project:

1. Fill in `AGENTS.md`: the name, the three commands, the first gotcha. Keep it short.
2. Put the project's real commands in `scripts/agent/check` and run it.
3. In `WORKFLOW.md`, keep the tracker line that applies.
4. Start Claude Code there once and accept the trust prompt, so the hooks and allow rules load.
5. Optional: run `/sandbox` to turn on the Bash sandbox (read `docs/claude-code.md` first).

### What you get

- **A check the agent must pass.** `scripts/agent/check` is run by the `verify` skill, and by
  a hook when a turn ends with changed files.
- **Guardrails enforced by hooks**: no reading secret-looking files, no wide deletes, no
  force-push, no push to a protected branch, no merging.
- **Eleven skills**: `spec`, `task`, `verify`, `write-tests`, `performance`,
  `second-opinion` and `wrap-up`, plus four you start yourself: `kickoff`, `dream`,
  `careful` and `lock-tests`.
- **A ratchet** for any number you care about (`scripts/agent/ratchet`), such as bundle
  size, queries per request or a score. The number can only get better.
- **A workflow** (`WORKFLOW.md`): epics and tasks whose acceptance criteria are checks, kept
  in issues or in files, with evidence on the pull request.
- **Memory that corrects itself**: notes in `.agents/memory/`, plus the `dream` pass.
- **Other models**: `scripts/agent/claude-with glm|deepseek|kimi|kimi-code`.

### The research

`refs/INDEX.md` lists every source with its URL. `refs/notes/` holds the distilled findings,
with quotes and locators. The texts themselves are other people's writing, so they are not
in this repository: git tracks only each item's `meta.json`. To read a source locally, fetch
it with `tools/refs` (see `refs/README.md`). The `prompts-verbatim` check needs the sources
that `prompts/README.md` cites.

## How far to trust it

Run and observed on one machine (Ubuntu 24.04, Claude Code 2.1.322): the hooks, skills and
agents loading, the memory rules, task selection, the setup script and one full dream pass.

Written from documentation but not run: everything for Codex, the vendor launchers, the Bash
sandbox configuration and claiming tasks on GitHub. Each of those files says so at the top.

Not done at all: evals for the skills, and a real task taken through the whole workflow. The
three newest skills (`kickoff`, `write-tests`, `performance`) have only been validated for
format, not used. `docs/keeping-current.md` lists the gaps in order.

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

## Checks

    scripts/agent/check           # compile, config parsing, guard tests, size limits, validators
    scripts/agent/check --quick   # skip the slower validators
