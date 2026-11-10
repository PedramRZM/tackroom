# Tasks, backlog and epics

The preference this template encodes, and what it rests on. The contract agents follow is
`template/WORKFLOW.md`; this file is the reasoning. The research is
`refs/notes/task-backlog-epic-management.md` (58 sources).

## The shape

- **The tracker holds what to do and its state. The repository holds how to work and what was
  decided. The pull request holds the proof.** Both frontier teams that published details
  ended up with this split: OpenAI moved from plans in the repository to a tracker as the
  control plane, and Anthropic's routine and playbook examples use a tracker for the queue
  (notes, finding 5 and "What frontier teams say they do").
- **Two levels: epic and task.** A task fits one context window and one pull request. That is
  the most repeated rule in the set (finding 2).
- **Acceptance criteria are checks.** Each is a behaviour plus the command, test or UI step
  that proves it, written before work starts and judged by something other than the agent that
  did the work (finding 3).
- **You mark tasks ready and you merge.** Agents stay out of both ends (finding 7). They also
  never edit the goal or the criteria: Anthropic's long-running harness allowed changes to one
  field of its feature list for the same reason.
- **Selection is a rule, not a judgement.** `scripts/agent/next-task` takes ready, unclaimed,
  unblocked tasks by priority, then age (finding 6).
- **Evidence goes on the pull request**, one line per criterion, as output or screenshots
  (finding 8).
- **A plan file only for work that spans sessions**, one per task, deleted at merge. Plans that
  nest, multiply or outlive their task rot (findings 9 and 10).
- **Discovered work becomes a new inbox item** instead of widening the current task
  (finding 16).

## Two places a task can live

| | Issues | Files |
|---|---|---|
| Where | GitHub issues from the task form; GitLab works the same way with `glab` | `tasks/<id>-<slug>.md` |
| State | labels and assignee | the `status` field |
| Epics | a parent issue with sub-issues | a file with `type: epic`; tasks point to it |
| Seen from | anywhere, phone included; one board across repositories | the repository only |
| Unattended cloud runs | work, since issue state is not tied to a branch | only see what is merged |
| Offline | no | yes |

The research recommends issues as the primary system. This template treats files as an equal
option, because several of the owner's repositories are not on GitHub and some have no remote.
The format, states and rules are identical, so a project can move from one to the other.

A project that already uses Backlog.md can keep it: it is the same idea (one file per task,
acceptance criteria, a board) with its own CLI. The notes compare it with the alternatives.

## When to write more than a task

- **A spec** in `docs/specs/` when the work crosses a module or service boundary, changes a
  schema or public API, or will be split across several tasks. Under about 150 lines, and
  about what must be true, not how to code it: in Anthropic's harness, detailed technical plans
  written up front were where errors entered and then cascaded (notes, "When to write a spec").
- **A decision record** in `docs/decisions/` for architecture, the data model or
  infrastructure, written first and reviewed by you before implementation. Decision records
  are the documentation that keeps its value (finding 18).

## What was not adopted

- **Spec frameworks** (Spec Kit, Kiro, BMAD, Taskmaster) as the process. None of the frontier
  teams in the corpus uses one, and independent write-ups report heavy markdown overhead on
  small changes (findings 11 and the comparison table).
- **The harness's built-in todo list** as the record. It is local to one machine and is being
  retired on newer models (finding 13).
- **Beads.** It has the one thing issues lack, an atomic claim, and becomes worth its weight if
  you ever run more than about three agents in one repository.

## How strong the evidence is

Weaker than the confidence of the conventions suggests, and the notes say so:

- No source measures tracker choice against outcomes.
- The one controlled comparison of spec workflows comes from a vendor.
- Treating GitHub Issues as equivalent to the Linear setups the frontier teams describe is an
  inference from feature parity.
- The limit of about three concurrent sessions is several people's report of their own
  capacity, not a measurement.

## What was run

- `scripts/agent/next-task` on sample task files: selection order, blocked and interactive
  tasks excluded, claiming.
- The GitHub read query, against a public repository.
- Not run: claiming a GitHub issue, sub-issue and blocked-by handling (the installed `gh`
  2.88.1 lacks those flags, so a `blocked` label stands in), and the whole loop on a real task.
