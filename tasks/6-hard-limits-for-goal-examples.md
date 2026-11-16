---
id: 6
title: Distinguish model-judged goal limits from hard execution limits
type: task
status: done
priority: p1
epic: 0
blocked-by: []
interactive: false
created: 2026-11-15
---

## Goal

Readers of the unattended-loop recipe do not mistake a prose turn limit for enforced runtime control.

## Context

`docs/loops.md` goal table and unattended recipe; saved goal and best-practices docs;
`refs/notes/2026-11-15-verification-workflow-audit.md` corrections.

## Acceptance criteria

AC1. Documentation distinguishes transcript-only model judgment from independent execution,
and uses a supported hard headless limit. Check: verify the installed CLI and current primary
docs, run a bounded harmless scratch command, and record cap behavior and limits honestly.

## Constraints

No default model changes, provider calls or universal unattended permissions.

## Out of scope / do not change

Loop implementation or a new scheduler.

## Notes

2026-11-15: Found during task 1's source audit. The current recipe puts a 40-turn cap only in
prose. Saved current docs describe `--max-turns` and `--max-budget-usd`; installed CLI help
lists the latter but not the former, so verify actual support before publishing an example.

2026-11-16: Owner requested task 6. Working on `task/6-hard-limits-for-goal-examples`;
baseline `scripts/agent/check`: all 11 checks passed.

2026-11-16: Owner requested merge and completion, then required cross-harness verification
before merging. That follow-up is recorded below; completion is authorized by the owner.

## Verification plan

2026-11-16 follow-up: Owner paused the requested merge to require cross-harness evidence.
Verify fresh combined setup and actual Codex/OpenCode skill discovery without model calls;
check each installed CLI and primary documentation for its own limit semantics. Exercise an
external wall-clock timeout against harmless stalled local transports where no equivalent
headless turn flag is established. Record discovery, config acceptance and runtime enforcement
as separate claims; do not call a synthetic or discovery test a live model-behavior test.

AC1: Compare current primary goal/CLI docs with installed Claude Code help/version, then
exercise a one-turn headless cap in a disposable project using a local synthetic API response
that requests a harmless read. Expected: the CLI stops with a limit result instead of issuing
another model request. This tests CLI enforcement without provider calls; it cannot establish
live billing behavior or goal-evaluator quality. Record the exact invocation, result, version
and fixture limits. Inspect the prose/recipe for the distinction between model judgment and
execution, then run `scripts/agent/check` and `git diff --check`. Existing checks and direct
documentation review suffice; no production code or new permanent test suite is planned.

## Evidence and handoff

2026-11-16: AC1 implemented in `docs/loops.md`; details and primary-source links are in
`refs/notes/2026-11-16-headless-goal-limits.md`. Refreshed the saved CLI and goal docs through
`tools/refs`. Claude Code 2.1.323 omits `--max-turns` from help but accepts and enforces it.
Scratch `/goal` probes with local synthetic tool responses and caps 1 and 2 made exactly 1
and 2 local Messages requests, then exited 1 with `error_max_turns`, `terminal_reason:
max_turns`, and no permission denials. Reported `num_turns` was 2 and 3. The headless recipe
now uses `--max-turns 40`, separates it from model-judged clauses, and explains estimated-cost
overshoot, wall-clock limits and interrupted-work handling.

Initial verification: baseline and post-change `scripts/agent/check` both printed `all 11 checks
passed`; `git diff --check` passed. No provider calls, live dollar-cap test, full goal-evaluator
test or Codex target-harness run. Vendor launchers were not run against a live endpoint.
This is documentation only: template files, hooks, skills, settings and default models were
not changed. The scratch probe used `--bare`, so it is not template-hook evidence.

Cross-harness follow-up: fresh combined setup exposed all 12 shared skills to actual Codex
0.169.0 and OpenCode 1.3.10 discovery APIs. Shared installation/reference checks and Codex role
parity passed. Codex accepted its native goal-budget setting, but the untrusted scratch
project's config remained disabled; OpenCode loaded its reviewer/permissions and accepted
`steps: 2`. Real headless Codex/OpenCode processes against stalled local transports exited
124 after 10.02/10.07 seconds under GNU timeout. A harmless SIGTERM-ignoring control verified
forced-kill escalation. No provider calls or persistent configuration changes were made.

`docs/loops.md` now supplies per-harness limit semantics and bounded Codex/OpenCode recipes;
`docs/other-harnesses.md` links the evidence. The probe record separates actual discovery,
configuration acceptance and runtime enforcement from untested live model/hook behavior.
Other named clients were not installed, so their behavior remains documentation-only.

Completion: owner-authorized local merge into `main`; task marked done with the verified
scope and remaining limits above. No push or remote pull request was requested.
