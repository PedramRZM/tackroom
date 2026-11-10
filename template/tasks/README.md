# tasks/

One file per task, used when this repository tracks work in files instead of an issue tracker
(see `WORKFLOW.md`). Delete this folder if the repository uses issues.

- Create a task by copying `TEMPLATE.md` to `<id>-<slug>.md`, with the next free id.
- An epic is the same file with `type: epic`; its tasks point at it with `epic: <id>`.
- Only the user changes `status` to `ready`. Agents set `in-progress`, `needs-human` and
  `in-review`. A task becomes `done` when its pull request is merged.
- `scripts/agent/next-task` prints the task to work on next: ready, not blocked by an unfinished
  task, not interactive, highest priority first, then lowest id. `--claim` marks it in progress.
- Agents do not edit the Goal or the Acceptance criteria. Questions go under Notes with the
  status set to `needs-human`.
- Done tasks stay in the folder as a record. Move them to `tasks/done/` when the list gets long.
