---
id: 0
title: Make harness verification deliberate and measurable
type: epic
status: inbox
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

AC1. Portable guidance covers behavior examples, test levels, tools and UI evidence. Check:
task 1's checks and scratch results.
AC2. A real project can reproduce a critical journey and a deliberate failure from the
documented setup. Check: task 2's evidence.
AC3. Guidance has measured usefulness and costs against the previous version. Check: task 3's
comparison, including negative results and a keep/prune recommendation.

## Constraints

No cross-project registry, sync, fixed model choice, compulsory paid services or fixed test ratios.

## Out of scope / do not change

Tasks 4 and 5 are optional experiments; they are not required for epic acceptance.

## Notes

2026-11-15: Created from the owner's request. Implementation proceeds on task 1, not this epic.
