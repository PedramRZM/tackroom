---
id: 4
title: Trial an opt-in deterministic task-completion check
type: task
status: inbox
priority: p3
epic: 0
blocked-by: [2]
interactive: false
created: 2026-11-15
---

## Goal

Determine whether a per-task completion gate prevents a demonstrated missed check without
adding redundant work or confusing model judgment with independently executed verification.

## Context

`refs/notes/2026-11-13-anthropic-staff-setup-audit.md`, current Claude hooks and goal docs,
`template/.claude/hooks/stop-check.py`, and task 2's failure evidence.

## Acceptance criteria

AC1. Define which state is gated: Claude internal task, response stop or tracker transition.
Check: document the event and its scope against current official docs.
AC2. In scratch only, a failing check blocks the intended completion and a passing check
allows it. Check: actual event results for failure, success, absent check, timeout and crash.
AC3. Bound repeated execution and test unrelated tasks. Check: a loop cannot silently consume
an unlimited budget, and missing checks never count as passing.
AC4. Recommend adoption or rejection with evidence. Check: compare added runtime with missed
checks caught; document that workspace hooks are not an external tamper-proof boundary.

## Constraints

Opt-in experiment first; no blanket Stop-hook expansion. `/goal` judgment alone does not
execute an independent check, and textual turn limits are not hard process budgets.

## Out of scope / do not change

Production CI policy and automatic issue closure.

## Notes

2026-11-15: Conditional experiment inherited from the prior staff audit, not a required feature.
