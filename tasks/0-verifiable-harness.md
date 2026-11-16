---
id: 0
title: Make harness verification deliberate and measurable
type: epic
status: in-progress
priority: p1
epic:
blocked-by: []
interactive: false
created: 2026-11-15
---

## Goal

An agent chooses evidence for the intended result and code quality before implementing,
then presents reproducible results without redefining success. Keep only additions whose
value survives a real-project trial.

## Context

`docs/specs/verification-before-implementation.md`,
`refs/notes/2026-11-15-verification-workflow-audit.md`, and tasks 1–5.

## Acceptance criteria

AC1. Portable guidance covers behavior examples, test levels, tools and UI evidence in Claude
Code, Codex and OpenCode. Check: task 1's shared setup checks, live Codex scratch results and
explicit validation limits for the other harnesses.
AC2. A real project can reproduce a critical journey and a deliberate failure from the
documented setup. Check: task 2's evidence.
AC3. Guidance has measured usefulness and costs against the previous version. Check: task 3's
comparison, including negative results and a keep/prune recommendation.

## Constraints

No cross-project registry, sync, fixed model choice, compulsory paid services or fixed test ratios.
Claude Code, Codex and OpenCode are all in scope. Keep their evidence and limitations explicit
through every child task. Codex is the available live validation harness on this machine;
use packaging/configuration checks for other targets and state untested runtime behavior.
Unavailable Claude/OpenCode model access is not a completion gate for portable setup work.

## Out of scope / do not change

Tasks 4 and 5 are optional experiments; they are not required for epic acceptance.

## Notes

2026-11-16: Owner clarified that all tasks must produce multi-harness setups, while only Codex
is available for live validation here. Removed the agent's over-scoped requirement to pass
live model trials in every harness. Task 1 has live Codex and shared packaging evidence;
other runtime limitations and an exploratory failed OpenCode plan remain recorded. Task 2
still needs the owner-selected app; task 3 remains the later usefulness comparison.

2026-11-16: Owner requested starting this epic. Resumed its first required child, task 1,
on `task/1-verification-claude-evidence` from `main` at `9f88d9a`. Baseline all 11 checks
passed. Fresh scratch setup succeeded, but the bounded Claude exercise again exited 1
before a model response: account verification is required ($0). Task 1 remains needs-human;
restore Claude account access before retrying. Task 2 also still requires the owner to name
the target application and authorize its modifications. No epic acceptance is claimed.

2026-11-15: Created from the owner's request. Implementation proceeds on task 1, not this epic.
