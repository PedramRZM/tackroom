---
id: 12
title: Add a coverage-preserving prune-tests skill
type: task
status: inbox
priority: p2
epic:
blocked-by: []
interactive: false
created: 2026-11-19
---

## Goal

Give a developer a repeatable way to decide which tests are redundant or obsolete and to demonstrate that pruning preserves regression coverage.

## Context

Use the canonical skills in `template/.agents/skills/` and the existing `write-tests`, `lock-tests` and `verify` guidance. Discovery and installation use per-skill metadata, `tools/setup` and `tools/render-harness`. Use a scratch project for the trial.

## Acceptance criteria

1. **AC1.** The optional `prune-tests` skill is discoverable through the Tackroom catalog and can be installed in a scratch project. Verify via `tools/setup --list`, a selective install and the generated adapters for supported harnesses.
2. **AC2.** Given a fixture containing equivalent checks, a unique boundary case, a flaky test and an apparently obsolete contract, the skill produces an evidence-backed disposition for each. Identify the retained assertion covering a proposed removal, preserve unique cases, and flag flaky or disputed behavior for investigation.
3. **AC3.** Trial one consolidation in the fixture. Record the affected suite before and after, and show that the retained check still fails for the behavior being protected. A pass count or shorter runtime alone cannot establish equivalent coverage.
4. **AC4.** Run Tackroom's repository check and document the scratch trial. Supply the published upstream revision for downstream installation.

## Constraints

Limit changes to the shared skill, its discovery metadata and supporting examples/checks. Pruning a failing check merely to turn a build green conflicts with the existing verification workflow.
