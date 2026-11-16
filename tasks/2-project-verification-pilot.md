---
id: 2
title: Prove a project-specific verification recipe on one real journey
type: task
status: inbox
priority: p1
epic: 0
blocked-by: [1]
interactive: true
created: 2026-11-15
---

## Goal

A fresh session can start one selected real application, seed/reset its isolated data and
verify a critical user journey without inventing setup or accepting screenshots as behavior proof.

## Context

Task 1, `template/.claude/skills/verify/SKILL.md` (This project),
`refs/notes/2026-11-13-claude-team-bdd-e2e.md`, and the selected app's existing test commands.

## Acceptance criteria

AC1. A documented command or existing helper starts, seeds, checks health and resets the app.
Check: a fresh session reproduces it from the documented revision.
AC2. One important journey and one failure/permission case have independent expected results.
Check: recorded failure before a deliberate defect is removed and success after, with assertions.
AC3. Relevant code/design rules have known-good and known-bad fixtures. Check: the selected
linter rejects the violation and accepts a valid example, with documented coverage limits.
AC4. Evidence identifies revision, environment, roles/data, command exits, skip/retry counts
and UI artifacts. Check: another session reproduces the result; if a preview is necessary,
its deployment identity matches the tested revision. Keep the recipe usable from Claude Code,
Codex and OpenCode. Reproduce it live with Codex here; check the other harness entry points
and configuration statically, with unavailable runtime verification explicitly recorded.

## Constraints

Owner selects the app and authorizes its modifications. Reuse installed tools; do not build
cross-project management or assume this template repo is an application.

## Out of scope / do not change

Large E2E suites, hosted artifact services and production data.

## Notes

2026-11-16: Owner requires portable setups across all tasks, with Codex as the live test
harness here. AC4 distinguishes shared recipe/setup coverage from runtime validation; it
does not require unavailable Claude/OpenCode model access. The selected app and trusted
expectations stay the same. This does not authorize changes to an unselected app.

2026-11-15: Needs a chosen target application. Generic instructions cannot supply its seed
users, routes or trusted expected outputs.
