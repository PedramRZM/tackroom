# Task 1 evidence

2026-11-15. Base: `main` at `b8ce42c`; branch:
`task/1-verification-before-implementation`. Changes are uncommitted.

- [Final repository output](checks.txt): all 10 checks passed.
- [Scenario](scenario.md): unchanged between the two read-only Codex exercises.
- [First plan](codex-plan-first.md): useful planning, but omitted explicit usability limits.
- [Recheck plan](codex-plan-recheck.md): after a three-line reporting clarification, explicitly
  distinguishes visual baselines and leaves representative-user usability unverified.
- [Execution record](codex-execution.md): successful commands reading the exact shipped skills
  and reference, output hashes, completion events and runtime limitations.
- [Claude attempts](claude-attempt.md): no model response; account verification remains required.

Independent reviewer verdict after the recheck: no implementation defects found; AC1–5
supported; AC6 incomplete solely because the live Claude exercise is blocked. The reviewer
also reproduced fresh `tools/setup --codex` packaging and compared affected files across all
three copies. Issue-form YAML parses with unique IDs; skill validators and `git diff --check`
pass. Fifteen new reference metadata records are indexed in the corpus (1,817 items).

The plan files are verbatim model output, so any relative links inside them refer to the
scratch workspace, not this evidence folder. No actual invoice application was present.
The exercises show instruction-following in a planning scenario, not a measured quality gain.
Project configuration was untrusted/disabled in Codex; no hook/permission or goal-lifecycle
verification is claimed. Vendor launchers were not run against live endpoints.

To resume: restore Claude account access, use a fresh scratch copy from `tools/setup`, repeat
the recorded scenario and bounded command, inspect actual tool reads and results, then request
owner review. Do not mark the task done based only on the successful Codex planning exercise.
