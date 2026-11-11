# Loops

A loop is an agent repeating cycles of work until a stop condition is met. This is the Claude
Code team's own definition and classification
([`refs/articles/claude.com/resources-articles-getting-started-with-loops/article.md`](https://claude.com/resources/articles/getting-started-with-loops)), with the
forms that fit this template. Nothing here runs on its own until you type it.

| Loop | You hand off | Stops when | Reach for |
|---|---|---|---|
| Turn-based | the check | the agent judges it is done | the `verify` skill, the Stop hook |
| Goal-based | the stop condition | a model confirms the condition, or the cap is hit | `/goal` |
| Time-based | the trigger | you cancel it, or the work completes | `/loop`, a scheduled task |
| Proactive | the prompt | each task meets its goal; the routine runs until turned off | a schedule plus `/goal` plus a workflow |

The article's advice on choosing: start with the simplest one, and move up only when you are the
bottleneck for a specific piece (the check, the stop condition, the trigger).

## Turn-based: make the agent's own check better

Every prompt is already a loop. What improves it is the verification step. In this template
that is `scripts/agent/check`, the `verify` skill, and the Stop hook, which sends a failing
quick check back to the agent once before it can finish.

When a result is not good enough, the article's instruction is to fix the system, not only the
instance: add the missing check to `scripts/agent/check`, or the missing gotcha to `verify`.

## Goal-based: `/goal`

`/goal` keeps the session working until a small model judges the condition met. That judge
reads only the conversation; it cannot run anything
(`refs/notes/claude-code-docs-extending.md` 4.3). So a condition needs one measurable end
state, the check that shows it, and a cap.

    /goal scripts/agent/check passes and its full output is shown in this conversation, or stop after 15 turns

    /goal every acceptance criterion of task 42 has its check's output shown here and a draft pull request is open with the Evidence section filled in; or the task is marked needs-human; or stop after 30 turns

    /goal the homepage Lighthouse performance score is 90 or above, shown by the report summary printed here; do not remove features to get there; stop after 8 tries

Deterministic criteria work best: a test count, a score, a command's exit status. `/goal` does
not change the permission mode. One goal per session.

## Time-based: `/loop`

Re-runs a prompt on an interval inside an open session, for work that depends on something
outside the repository.

    /loop 10m check the pull request for this branch: address review comments, fix failing CI, and stop when it is approved and green

    /loop          (no prompt: Claude Code's built-in maintenance loop for the current branch)

It runs only while the session is open and idle, expires after seven days, and each run is
another turn in the same conversation, so start it from a fresh session
(`refs/notes/claude-code-docs-extending.md` 4.4). Match the interval to how often the thing you
are watching changes.

## Proactive: one task per run, unattended

The combination the article describes for recurring, well-defined work. With this template's
pieces, a local version looks like:

    claude -p "/goal Run scripts/agent/next-task --claim. If it prints no task, say so and stop. Otherwise work that one task following WORKFLOW.md until a draft pull request is open whose Evidence section covers every acceptance criterion with output shown here, or the task is marked needs-human. Stop after 40 turns." --permission-mode auto

Before leaving something like that running, the docs' five questions
(`refs/notes/claude-code-docs-extending.md` 1.10):

1. What does done look like? (The goal condition.)
2. Can it check its own work? (`scripts/agent/check` has real commands in it.)
3. What may it touch? (A sandbox or a separate machine; no credentials in reach; the guard
   refuses pushes to protected branches and the ask rule refuses merges.)
4. What stops it? (The turn cap; add `--max-budget-usd` for a money cap.)
5. Where does the result go and who signs off? (A draft pull request. You merge.)

Run it in a git worktree or a cloud session so it cannot collide with your own work: several
agents in one checkout is a documented way to lose work
(`refs/notes/devcon-4-security-runtime-misc.md`, finding 3).

Cloud scheduled tasks (`/schedule`) run from a fresh clone on Anthropic's side, at most hourly.
They see committed files only, and cannot see local transcripts or uncommitted work.

## Keeping loops from getting expensive

From the same article and Anthropic's cost posts (`refs/notes/anthropic-claude-dev-blog.md`
(g)):

- Right-size the primitive. Small tasks do not need loops or several agents.
- Effort before model: medium by default, low for mechanical work, high where hidden edge cases
  matter. On one benchmark, running at low and re-running failures at high beat running
  everything at high on both pass rate and cost.
- Pilot before a large run. A workflow can start hundreds of agents.
- Scripts for deterministic work: running a script is cheaper than reasoning through its steps.
- Review usage: `/usage` breaks it down by skill, subagent and MCP server.

## What is not here

- **Dynamic workflows.** Useful when work outgrows a handful of subagents or findings need
  cross-checking. The template ships none: the dream pass is small enough to run as two kinds
  of subagent, and the script API is only partly documented
  (`refs/notes/claude-code-docs-extending.md`, ambiguities).
- **The Ralph loop** (a shell loop feeding one prompt forever). Its author says it is not for
  existing codebases (`refs/notes/task-backlog-epic-management.md`, comparison table).
- **Agent teams.** Experimental, about seven times the tokens, and the docs advise against
  enabling them in shared settings (`refs/notes/claude-code-docs-extending.md`, decisions).
