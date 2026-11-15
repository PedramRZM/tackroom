# tackroom

Dotfiles for coding agents. A tack room is where riders keep, mend and fit the harness,
bridle and saddle before a ride. This repository does the same job for coding agents: it
holds the instruction files, settings, hooks, skills, subagents, memory and workflow that make
Claude Code (and, less tested, Codex and OpenCode) work well on a real project. Every piece
comes with the research it is based on.

## The idea

Coding agents can do a lot, but you can't count on them. The same model does good work in one
repository and makes a mess in another, and the difference is mostly not the model. It is the
setup around it: whether the agent can check its own work, what it is stopped from doing, what
it knows about the project, what it remembers from last time, and who reviews the result. That
setup is called the harness.

A harness is just files: markdown, JSON, a few scripts. So you can treat it like any other
configuration. You can version it, review it, test it, and carry it from project to project.
This repository is one such harness, written down with reasons.

The thinking behind it, in order of how much it matters:

1. **An agent is only as good as the check it can run.** The most consistent finding across
   the research is that a single command that says "this is healthy" or "this is broken, here
   is why" improves results more than a better prompt, more effort or a bigger model. The check
   should print almost nothing when things pass and say exactly what failed when they don't, so
   it costs little context to run often.
2. **Rules that must always hold go in code, not in prose.** A model can skip an instruction,
   however it is worded. If something must never happen (reading secret files, force-pushing,
   deleting the repository), a hook or a permission blocks it. Prose is kept for preferences
   and judgement.
3. **A hook is a guardrail, not a wall.** A determined or confused agent can get around a hook
   through the shell. Real safety comes from what the agent cannot reach: a sandbox, and
   credentials kept out of its environment. The template says this plainly instead of
   overselling its hooks.
4. **Instructions are short, and get shorter.** Instruction files are read at the start of
   every session, and every line competes for the model's attention. Newer models do better
   with less: Anthropic cut over 80% of Claude Code's own system prompt with no measured loss.
   The template's `AGENTS.md` is a skeleton under 50 lines, and removing guidance is preferred
   to adding it.
5. **Whoever wrote the code doesn't get to grade it.** An agent that checks its own work tends
   to approve it. Review comes from a separate agent with fresh context, given the task and the
   original branch rather than the author's summary, and told to look for what is wrong. Tests
   that define "done" can be locked so they can't be edited to pass.
6. **Work lives in files, not in the chat.** Tasks, plans, evidence and handoff notes are
   plain files or tracker issues. A new session, a different model or a person can pick up
   where the last one stopped.
7. **Memory has to be corrected, not just collected.** Notes an agent writes in the middle of
   a task are sometimes wrong, and the next session trusts them. So memory is plain markdown in
   git, and a separate pass (`/dream`) rereads finished sessions, fixes the notes, and proposes
   changes to the instructions for you to accept or reject.
8. **Each project owns its copy.** You copy the template into a project and then it is that
   project's code. There is no package to install and nothing to keep in sync. Projects differ,
   and harness parts go out of date as models improve, so each project should prune and adapt
   its own copy. Take improvements from here by hand when you want them.
9. **Everything says how far to trust it.** Each part says whether it was run and observed,
   written from documentation only, or not done. A setup that claims more than it has shown
   teaches you to stop checking.

`docs/principles.md` goes through each of these in detail: what the template does, the
sources behind it, where the sources disagree, and how well it has been tested.

## Where the ideas come from

Almost nothing here is original. It is collected from the people who build these tools and the
people who use them heavily, then cross-checked:

- **Anthropic**: the engineering and research blog, the Claude Code team's blog, and the Claude
  Code documentation. The main sources for checks, hooks, skills, sandboxing, context, memory
  and long-running agents.
- **People on the Claude Code team and around it**, mostly from their posts: Boris Cherny,
  Thariq Shihipar, Addy Osmani.
- **OpenAI**, for its harness-engineering account (Ryan Lopopolo) and the Codex documentation.
- **AI Native DevCon (June 2026)**: 57 talks and clips on skills, context, memory,
  verification, teams and security, transcribed.
- **Practitioners writing from experience**: Simon Willison, Andrej Karpathy, Kent C. Dodds,
  Steve Yegge, Geoffrey Huntley, Peter Steinberger and others.

That comes to about 1,650 talks, articles, docs and posts, indexed in `refs/INDEX.md` with
author, date and URL. Each topic is distilled in `refs/notes/` with short quotes and locators,
so a claim can be traced back to the sentence it rests on. Where the sources disagree, the notes
and `docs/principles.md` say so. Two examples: whether adversarial review is worth its cost,
and how many skills a repository should have at all. Anything without a source is labelled as a
judgement call.

The research also decided what is left out:

- **Language and framework rules.** The docs say to write down only what the agent can't find
  by reading the code. Add a rule in a project when the same correction keeps coming up.
- **Role-named subagents** (planner, architect, tester). Several independent teams found them
  unhelpful. Subagents earn their cost by isolating context and by reviewing independently.
- **A spec framework.** None of the frontier teams in the research uses one as its process.
- **MCP servers by default.** A command-line tool with a few lines of usage beat an MCP server
  in six independent accounts, and connected servers take up context even when idle.

`prompts/README.md` collects prompts that named people shared as things to type, quoted word for
word with their sources. The check verifies the quotes against the saved texts.

## How it is set up

| Path | What it is |
|---|---|
| `template/` | The harness. It mirrors a project root, so its files go where they would live in your project. |
| `docs/` | Why the template is shaped this way, with citations. Start with `principles.md`. |
| `refs/` | The research: the index of sources and the distilled notes. |
| `prompts/` | Reusable prompts, quoted from their authors. |
| `tools/` | `setup` copies the template into a project. `refs` fetches and indexes the research. |

This repository runs on its own template. The root `.claude/`, `CLAUDE.md` and
`scripts/agent/` files are copies of `template/`, and the check fails if they drift apart.

### What a project gets

- **Instructions**: `AGENTS.md` is the single file every harness reads. `CLAUDE.md` is one
  line that imports it, so Claude Code, Codex and OpenCode share the same text.
- **A check**: `scripts/agent/check`, the one command for "is this healthy". The `verify` skill
  runs it, and a hook runs it again when a turn ends with changed files.
- **Guardrails**: hooks that block reading secret-looking files, wide deletes, force-pushes,
  pushes to protected branches and merges. Sandbox settings are included, switched off until
  you have checked they work on your machine.
- **Skills**: twelve of them, each doing one thing. The model can call eight of them: `spec`,
  `task`, `verify`, `write-tests`, `performance`, `ui-craft`, `second-opinion` and `wrap-up`. Four only run
  when you start them, so they cost no context until then: `kickoff`, `dream`, `careful` and
  `lock-tests`.
  [UI craft](docs/ui-craft.md) covers stable states, visual detail and intent-aware interactions.
- **A reviewer**: a subagent that gets the task and the base branch, and tries to show the
  change is wrong.
- **A workflow**: `WORKFLOW.md` describes how a task moves from idea to merged pull request.
  Tasks have acceptance criteria written as checks, live in GitHub issues or in files, and end
  with evidence on the pull request.
- **A ratchet**: `scripts/agent/ratchet` guards any number you care about (bundle size, queries
  per request, a score), so it can only get better.
- **Memory**: notes in `.agents/memory/`, an inbox for new lessons, and the `dream` pass that
  corrects them.
- **Other harnesses and models**: Codex and OpenCode config, and
  `scripts/agent/claude-with glm|deepseek|kimi|kimi-code` to run Claude Code against other
  vendors' endpoints.

`template/README.md` lists every file and what to do with it after copying.

## Put it in a project

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

For a brand-new project, `/kickoff` takes you from an idea to a small, running repository that
an agent can work in.

## How far to trust it

Run and observed on one machine (Ubuntu 24.04, Claude Code 2.1.322): the hooks, skills and
agents loading, the memory rules, task selection, the setup script and one full dream pass.

Codex UI-skill discovery and a read-only fixture review have now run; OpenCode discovers the
same shared skill. See [UI-craft evidence](docs/evidence/ui-craft/README.md).
Written from documentation but not fully run: the broader Codex configuration, the vendor launchers, the Bash
sandbox configuration and claiming tasks on GitHub. Each of those files says so at the top.

Not done at all: evals for the skills, and a real task taken through the whole workflow. The
three newest skills (`kickoff`, `write-tests`, `performance`) have only been validated for
format, not used. `docs/keeping-current.md` lists the gaps in order.

## The research texts

The saved texts are other people's writing, so they are not in this repository. Git tracks
only each source's `meta.json` (URL, author, date). To read a source locally, fetch it with
`tools/refs` (see `refs/README.md`). The `prompts-verbatim` check needs the sources that
`prompts/README.md` cites, and fails on a fresh clone until they are fetched.

## Docs

- `docs/principles.md`: the principles, what each rests on, and how well it is tested
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

## License

MIT, see `LICENSE`. That covers the template, tools and docs. Quotes in `refs/notes/` and
`prompts/README.md` remain their authors' and are credited where they appear.
