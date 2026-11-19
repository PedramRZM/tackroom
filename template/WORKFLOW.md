# Workflow

How a piece of work moves from idea to merged, for any agent in any harness and for the person
supervising. The tracker holds what to do and its state. The repository holds how to work and
what was decided. The pull request holds the proof.

## Where tasks live

Pick one per repository and delete the other line:

- **Issues** (GitHub, or GitLab with `glab`): each task is an issue created from the task form.
  State is carried by labels and the assignee.
- **Files**: each task is `tasks/<id>-<slug>.md`, created from `tasks/TEMPLATE.md`. State is the
  `status` field. Use this for repositories without an issue tracker, or for offline work.

Both use the same task format, the same states and the same rules below.

## Shape of the work

- **Epic**: a goal too large for one pull request. It states the outcome, what is in and out of
  scope, and how you will know it is finished. No code is written against an epic directly.
- **Task**: one change that fits one context window and one pull request. It belongs to an epic
  or stands alone. Two levels only.
- **Acceptance criteria**: a numbered list inside the task, `AC1`, `AC2`, ... Each one is a
  behaviour plus the check that proves it (a command, a test name, or a UI step with the
  expected result). Few and separately checkable beats many and vague.

A spec in `docs/specs/` is written only for work that crosses a module or service boundary,
changes a schema or public API, or will be split across several tasks. Otherwise the task body
is the spec. A decision about architecture, data or infrastructure is recorded first, on its
own, in `docs/decisions/`, and reviewed before implementation starts.

## States

| State | Issues | Files | Who sets it |
|---|---|---|---|
| Inbox | open, no status label | `status: inbox` | anyone, including agents |
| Ready | label `ready` | `status: ready` | the user only |
| In progress | assignee + label `in-progress` | `status: in-progress` | the agent that takes it |
| Needs human | label `needs-human` + a comment with the question | `status: needs-human` + the question under Notes | the agent |
| In review | open pull request that closes the task | `status: in-review` | the agent |
| Done | closed by the merge | `status: done` | the user, by merging |

Priority is `p0` (first) to `p3`. A task marked `interactive` is ready but is done with the user
present, never by an unattended run.

## The loop for one task

1. **Pick.** Take the task you were given. If none was named, run `scripts/agent/next-task`: it
   lists ready tasks that are unclaimed and unblocked, highest priority first, oldest first.
   Take the first one. Do not choose by preference.
2. **Read.** The task and its comments or notes, the plan in `docs/plans/` if one exists, the
   last twenty commits on the branch, and any decision record the task names.
3. **Claim.** Mark it in progress and create the branch `task/<id>-<slug>`.
4. **Confirm the starting point.** Run `scripts/agent/check` before changing anything, so a
   failure that was already there is not mistaken for yours.
5. **Plan, when the task needs it.** A task that will span sessions or touches several parts
   gets `docs/plans/<id>-<slug>.md`: purpose, steps, progress, dead ends, decisions. A small
   task needs no plan file. Before implementation, use `write-tests` to map the criteria to
   concrete examples, expected results, appropriate checks/tools and required setup. Keep this
   in the task or existing plan. Reuse working tools and identify missing quality gates.
6. **Build in small steps.** For a bug or meaningful new behavior, confirm a focused test
   fails for the right reason, then implement and refactor while it passes. Trivial changes
   can use existing checks and direct evidence. Commit after each step that leaves the checks passing.
7. **Verify.** Use `verify` (workflow v2): cheap focused checks first, full local checks before
   push or PR, then evidence for each criterion and the assembled changed flow. Apply matching
   reliability checks from the pinned base's `REVIEW.md`. Record verified/partial/none and gaps.
8. **Get a second opinion on larger work.** For a task that needed a plan, have a fresh-context
   reviewer check a fixed commit against the criteria and base rubric before the user looks.
   Reuse that reviewer for repair rounds. An uncommitted snapshot review is provisional; do
   not commit just to obtain review when the owner has not authorized commits.
9. **Open the pull request** with the evidence section filled in: one line per criterion, with
   the command and its output or the screenshot, and a line for anything not verified.
10. **Hand over.** Mark the task in review. If you must stop before a pull request exists, push
    the branch and leave a handoff note on the task: state, what is done, the next step, what
    is blocking, the branch name.

## Rules that hold throughout

### Verification environment and evidence

Use the project's documented test environments and checks. Record the tested revision,
the environment, the results for each acceptance criterion and any outstanding failures.
Projects decide when to open a draft PR and where to publish evidence.

When verification and independent review pass, consider a task-sized Dream before human review.
If the task exposed a regression, repeated failure or owner correction, run the Dream skill’s
`scheduled-dream.py handoff --evidence PATH` on the verified findings and include the proposed
lesson in the handoff. Defer an unavailable retrospective to weekly Dream. Leave the tested
revision intact and hand the PR to the human reviewer for the merge decision.
Ask for human input when a decision or a concrete blocker prevents further progress.

### Review and repair

Use one reviewer across follow-up rounds with previous findings and the intervening diff.
A changed commit or working tree invalidates the old verdict for the changed scope. Check
the final tree before handoff. Stop after three unsuccessful repairs of a check, or sooner
when the same fix has failed twice; report attempts and reproduction evidence.

Project owners maintain `REVIEW.md`: diff trigger, check, rationale, incident/PR source and
owner for each rule. Proposed rubric or gate edits cannot approve themselves. Workspace
hooks and base-file reads are feedback, not tamper-proof enforcement; a trusted gate needs
reviewed policy outside the implementer's write access. New blocking gates start in observe
mode and need measured false positives and owner approval before enforcement.

### Task boundaries

- The task's goal and acceptance criteria are the user's. If one is wrong or cannot be met, say
  so on the task, mark it needs-human and stop. Do not edit them to fit the code.
- A task is done when the user merges. Agents do not merge, do not close tasks and do not mark
  their own criteria as met without showing the check.
- Tests are the judge. Do not weaken, skip or delete one to get a pass. If a test is wrong,
  that is a finding to report.
- One task per session, and a new session for a new task.
- Work found along the way that is outside the task is filed as a new inbox task that says
  where it was discovered.
- A lesson that will come up again goes to `.agents/memory/inbox.md`, not into the plan.
- When a plan's task is merged, move any lasting decision into `docs/decisions/` and delete
  the plan file in the same pull request. Git keeps the history.

## Limits

At most three agent sessions at once across everything you supervise, and at most one of them
on work you would call hard. An unattended run does one task and stops.
