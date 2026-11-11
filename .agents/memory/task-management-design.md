---
name: task-management-design
description: The task, backlog, epic and unattended-selection design in the template (WORKFLOW.md, tasks/, issue forms, next-task), the evidence behind it and its limits. Read before changing how work is tracked or picked up.
---

# Task management design

## The rule set

From `refs/notes/task-backlog-epic-management.md` (58 sources read in full):

- The tracker holds what to do and its state. The repo holds how to work and what was decided. The
  pull request holds the evidence.
- Two levels only. An epic is a parent. A task is sized to one context window and one PR.
- Acceptance criteria are a numbered list, `AC1..ACn`, each with its check.
- Agents do not edit the Goal or the criteria. They do not close issues or merge. The owner sets `ready`.
- Unattended selection is a script, not model judgement: open, ready, unassigned, unblocked, then
  priority, then age.
- Multi-session work keeps one plan file, `docs/plans/<id>-<slug>.md`, on the task branch.

## What the template ships (2026-11-10)

- `template/WORKFLOW.md`: the loop. The owner keeps one tracker line (issues or files) and deletes the other.
- `template/tasks/TEMPLATE.md`: front matter `id`, `title`, `type` (task or epic), `status`
  (inbox, ready, in-progress, needs-human, in-review, done), `priority` (p0 to p3), `epic`,
  `blocked-by`, `interactive`, `created`. Body sections: Goal, Context, Acceptance criteria, Edge
  cases, Constraints, Out of scope, Notes.
- `template/tasks/README.md`, and `template/tasks/` as the files tracker.
- `template/scripts/agent/next-task`: `--list`, `--claim`, `--github`. Exit 0 with a task, 1 when none.
  The branch name is `task/<id>-<slug>`.
- `template/.github/ISSUE_TEMPLATE/task.yml` and `epic.yml` (YAML parse-checked with pyyaml via uv),
  `template/.github/pull_request_template.md`, `template/scripts/agent/github-labels`.
- The session-start hook reads the task id from the branch name and names the plan file ([[template-hooks-and-guard]]).

## Test evidence

- `next-task` on eight sample task files: `--list` returned tasks 3, 8 and 5. The epic, the done
  task, the blocked task, the inbox task and the interactive task were excluded. After a claim, the
  next pick was 8. With nothing eligible it exited 1.
- The `--github` path ran only a read-only `gh issue list` shape check against `cli/cli`.

## Limits

- `gh` 2.88.1 has no `--parent`, `--blocked-by`, or sub-issue JSON fields, though GitHub's docs
  describe them. The GitHub selection query is untested beyond that shape check.
- Backlog.md 1.52.0 is installed locally. Seven of the owner's repos already use a `backlog/`
  folder (for example carshenas, cashcool, dojino, kava, truing). The file tracker is therefore a
  first-class option, not only a fallback.
- No source measures tracker choice against outcomes. The one controlled spec study is a vendor's.
- Linear is the tracker the frontier sources name. GitHub Issues is equivalent here by feature
  parity only (an inference).

Related: [[repo-purpose-and-scope]], [[process-lessons]].
