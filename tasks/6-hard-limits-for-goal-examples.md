---
id: 6
title: Distinguish model-judged goal limits from hard execution limits
type: task
status: inbox
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
