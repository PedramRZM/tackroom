---
id: 2
title: Prove a project-specific verification recipe on one real journey
type: task
status: done
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

2026-11-16: Owner accepted the pilot and requested commit, merge and done status.
agent-dev-infra additions committed as `ffc402c` and fast-forwarded into their source branch
`task/013-scinito-coder-canary`; its unrelated memory edit was preserved. Its main branch
was not advanced across unrelated unmerged work. Tackroom evidence and completion are merged
to main. Full checks: 34 target tests, all 11 tackroom gates. Independent review confirmed
AC1–AC4 with no outstanding findings. No remote push. The completed plan is retired; the
recipe, patch, provenance and outcomes remain in the evidence directory.

2026-11-16: Pilot implementation and evidence are ready for owner review. Added five actual
CLI-process tests and a reproducible recipe in the isolated agent-dev-infra worktree; no
production code or existing tests changed. Full target checks pass 34 tests (baseline 29).
A deliberate dispatch-authorization defect fails three assertions; restoration passes all
five focused tests. Existing Python syntax gate passes/rejects/restores its fixtures. Fresh
Codex reproduces the focused and full commands, exit 0, no test skips/retries; static shared
harness checks pass. Evidence and reproducible patch:
`docs/evidence/2-project-verification-pilot/README.md`. The fresh archive has no Git HEAD;
source identity is independently byte-verified against the pinned revision and patch hashes.
This is CLI integration with fixture provider data, not live Coder/RBAC or web-app proof.
No commit, push or merge performed for task 2; both working branches remain available.

2026-11-16: Owner switched the pilot to `/home/pedrum/Dev/agent-dev-infra` rather than repair
Scinito's known baseline failures. New target baseline at `19b8f90` passes all repository
checks and 29 tests. Use its existing read-only Coder readiness CLI as the real user-facing
workflow; the controller is not deployed and there is no web UI. Exercise the actual CLI
process with a local external-Coder fixture, including ready/not-ready, denied reads and reset.
This proves local command behavior, not live fleet admission or company permissions.
Worktree: `/tmp/agent-dev-infra-tackroom-task2`, branch `task/tackroom-2-readiness-verification`;
preserve the original checkout's pre-existing memory edit. Scinito is unchanged.

2026-11-16: Baseline blocks implementation under the task skill: Scinito's
`scripts/agent/check` exited 1 before any app changes. Typecheck passed (10s); lint failed
(83s, 59 errors/527 warnings); Jest failed (5 suites, 24 tests; 158 suites/2579 tests passed;
7 snapshots passed). Question sent to owner: proceed with an isolated pilot while preserving
these pre-existing failures, or repair the baseline as separate work first? No Scinito files
were changed. Evidence: `docs/evidence/2-project-verification-pilot/scinito-baseline.txt`.
Tackroom branch `task/2-project-verification-pilot`; Scinito remains at `e4402c761` on edge.

2026-11-16: Owner requested the next task and selected Scinito at
`/home/pedrum/Dev/scinito`. Started on tackroom branch `task/2-project-verification-pilot`
after task 1 merged as `a82eacc`. Read Scinito's AGENTS.md, WORKFLOW.md and existing test
guidance; baseline checks are running before application changes. Scinito checkout starts at
`e4402c761` on `edge`, with pre-existing untracked `.agents/skills/` and `.codex/` preserved.
The completed plan is superseded by the retained evidence. Scope remains isolated local verification,
with no production data or unrelated application changes.

2026-11-16: Owner requires portable setups across all tasks, with Codex as the live test
harness here. AC4 distinguishes shared recipe/setup coverage from runtime validation; it
does not require unavailable Claude/OpenCode model access. The selected app and trusted
expectations stay the same. This does not authorize changes to an unselected app.

2026-11-15: Needs a chosen target application. Generic instructions cannot supply its seed
users, routes or trusted expected outputs.
