# Loops

The task, verification plan and evidence requirements are shared across harnesses. Native
continuation controls differ; a skill file alone does not implement persistent execution.

## Goals across harnesses

| Harness | Entry point | What this template supplies |
|---|---|---|
| Codex CLI, IDE and desktop | Native `/goal <objective>`; view/edit/pause/resume/clear controls | Shared task criteria, `write-tests` planning and `verify` evidence |
| Claude Code | Native `/goal <condition>` | The same workflow; its evaluator judges conversation evidence rather than running checks |
| OpenCode | `opencode run` or its interactive agent session | The same shared skills and workflow; Claude's `/goal` and CLI flags are not portable |
| A harness without persistent goals | Invoke the shared task skill or ask it to follow `WORKFLOW.md` | The task/check/review loop within its supported execution; no promise of automatic continuation |

Do not install a custom `goal` skill over either native command. Start goals only when the user
requests them. State the outcome, constraints and executable verification, and keep the task
file as the durable specification. A goal does not expand permissions or replace the checks.
Codex source: [long-running work](https://learn.chatgpt.com/docs/long-running-work) and
[command reference](https://learn.chatgpt.com/docs/developer-commands?surface=cli), saved under
`refs/articles/learn.chatgpt.com/`. Local inspection on 2026-11-15 found Codex CLI 0.169.0 and
`goals stable true`; this verifies availability, not the entire goal lifecycle.

The Claude Code sections below describe **Claude Code's** native loop mechanisms. Their slash-command
syntax and evaluator behavior must not be assumed to apply to Codex or OpenCode. In particular,
a prose “stop after N turns” is a requested condition, not a hard execution limit. Headless
limits and their local verification are described below.

## Bounded headless work across harnesses

The research-backed workflow is shared through `AGENTS.md`, `WORKFLOW.md` and
`.agents/skills/`; execution controls belong to each harness. A fresh combined installation
was checked on 2026-11-16: Codex 0.169.0 and OpenCode 1.3.10 both discovered all 12 project
skills, and the installer checks verified their reference files. This proves availability,
not model compliance with every instruction. Codex still requires project and hook trust;
an untrusted project's skills can be visible while its configuration is disabled.

| Harness | Native control | Evidence and limit |
|---|---|---|
| Claude Code 2.1.323 | `--max-turns` in print mode | Enforced against a synthetic continuing tool loop; not a tool timeout |
| Codex 0.169.0 | `goals.max_goal_token_budget`; App Server goal `tokenBudget` | Setting accepted by strict config and returned by `config/read`; token exhaustion not exercised. No equivalent `--max-turns` flag is listed for `codex exec` |
| OpenCode 1.3.10 | Agent `steps` | Installed parser accepted `steps: 2`; runtime behavior not exercised. Current docs describe a final text-summary step, not a process timeout |
| Other clients | Their own documented controls | Shared instructions do not install a scheduler, goal engine or runtime limiter |

Codex's budget applies to native goals; do not assume an ordinary `codex exec` prompt creates
one or inherits goal-budget enforcement. OpenCode's current docs use V2 configuration while
this machine has V1: the agent map is `agents` in V2 and `agent` in V1. Do not copy Claude's
flags or V2 configuration blindly into another CLI. Sources: [Codex configuration](https://learn.chatgpt.com/docs/config-file/config-reference),
[App Server goals](https://learn.chatgpt.com/docs/app-server#manage-a-thread-goal), and
[OpenCode steps](https://opencode.ai/docs/agents/#steps), saved in `refs/articles/`.

For a wall-clock boundary independent of model judgment, these **GNU/Linux examples** wrap
one task invocation in GNU `timeout`. Twenty minutes and a ten-second shutdown grace are
example budgets, a local judgment to adjust for the task:

```sh
timeout --signal=TERM --kill-after=10s 20m \
  codex exec --sandbox workspace-write --json \
  'Read .agents/skills/task/SKILL.md and work task 42 following WORKFLOW.md. Show verification evidence.'

timeout --signal=TERM --kill-after=10s 20m \
  opencode run --format json \
  'Read .agents/skills/task/SKILL.md and work task 42 following WORKFLOW.md. Show verification evidence.'
```

These are ordinary headless task prompts, not invocations of native goal mode. Review project
trust and task-specific permissions first; these commands do not bypass approvals or sandboxing. The same wrapper
can surround the Claude recipe below, alongside its native turn cap. On macOS, GNU coreutils
provides `gtimeout`; Windows needs an equivalent supervisor. Those platforms were not tested.

With GNU coreutils 9.4, real Codex and OpenCode processes pointed at stalled local test
endpoints both exited 124 after about ten seconds with a ten-second timeout. Exit 124 means
timeout; 137 can mean forced kill. Treat either as interrupted work and inspect files and
child processes before resuming. The wrapper does not roll back edits, enforce a dollar cap,
or guarantee cleanup of detached processes or remote jobs. See the
[GNU manual](https://www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html)
and [cross-harness probe record](../refs/notes/2026-11-16-headless-goal-limits.md#cross-harness-follow-up).

## Claude Code loop mechanisms

A loop is an agent repeating cycles of work until a stop condition is met. This is the Claude
Code team's own definition and classification
([`refs/articles/claude.com/resources-articles-getting-started-with-loops/article.md`](https://claude.com/resources/articles/getting-started-with-loops)), with the
forms that fit this template. Nothing here runs on its own until you type it.

| Loop | You hand off | Stops when | Reach for |
|---|---|---|---|
| Turn-based | the check | the agent judges it is done | the `verify` skill, the Stop hook |
| Goal-based | the stop condition | a model judges the condition met or work blocked; runtime limits are separate | `/goal` |
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
([goal documentation](https://code.claude.com/docs/en/goal), saved in
`refs/articles/code.claude.com/docs-en-goal-md/`). So a condition needs one measurable end
state, the check that shows it, and constraints on the work.

    /goal scripts/agent/check passes and its full output is shown in this conversation, or stop after 15 turns

    /goal every acceptance criterion of task 42 has its check's output shown here and a draft pull request is open with the Evidence section filled in; or the task is marked needs-human; or stop after 30 turns

    /goal the homepage Lighthouse performance score is 90 or above, shown by the report summary printed here; do not remove features to get there; stop after 8 tries

The turn/try clauses above are requests interpreted from the transcript, not enforced
counters or timers. A separate model judging a reported test result does not independently
execute that test. The working agent must run the check and show its output; use the headless
CLI limits below when execution must be bounded independently of that judgment.

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
pieces, a local version looks like this (choose the turn budget for the task):

    claude -p "/goal Run scripts/agent/next-task --claim. If it prints no task, say so and stop. Otherwise work that one task following WORKFLOW.md until a draft pull request is open whose Evidence section covers every acceptance criterion with output shown here, or the task is marked needs-human." --max-turns 40 --output-format json --permission-mode dontAsk

`dontAsk` denies tools that require approval; configure only the permissions this task needs
before running it unattended. A goal or a turn cap grants no additional permissions.

`--max-turns` is a CLI-enforced limit on agentic turns in print mode, separate from the goal
evaluator's turn count. It defaults to unlimited. This recipe supplies one prompt; with
streamed input, queued messages can start another turn with a fresh limit. A turn cap is not
a wall-clock timeout and does not bound how long an individual tool runs. If elapsed time
must be bounded, use a process supervisor with its own timeout and child-process policy.

Optional `--max-budget-usd 5.00` stops at a client-side estimate of spend. The estimate can
differ from the bill and spend can overshoot the threshold; leave headroom. It is not a strict
billing ceiling. See the [CLI reference](https://code.claude.com/docs/en/cli-reference), saved
in `refs/articles/code.claude.com/docs-en-cli-reference-md/`.

Local verification on 2026-11-16: Claude Code 2.1.323 accepts and enforces `--max-turns`, despite
omitting it from `--help`. A scratch `/goal` run against a local synthetic API stopped with
exit 1 and JSON `subtype: error_max_turns`; caps of 1 and 2 allowed 1 and 2 model requests,
respectively. Its `num_turns` field reported 2 and 3, so do not interpret that field as the
number of requests made. A cap result means work was interrupted, not completed: inspect the
result and repository before resuming. This did not test a live provider, dollar-cap behavior,
goal-evaluator decisions or background-process cleanup. See the
[probe record](../refs/notes/2026-11-16-headless-goal-limits.md).

Before leaving something like that running, the docs' five questions
(`refs/notes/claude-code-docs-extending.md` 1.10):

1. What does done look like? (The goal condition.)
2. Can it check its own work? (`scripts/agent/check` has real commands in it.)
3. What may it touch? (A sandbox or a separate machine; no credentials in reach; the guard
   refuses pushes to protected branches and the ask rule refuses merges.)
4. What stops it? (The enforced CLI turn limit; optionally an estimated-spend limit and an
   external timeout. The goal condition alone is model-judged.)
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
