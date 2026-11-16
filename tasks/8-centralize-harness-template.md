---
id: 8
title: Centralize shared harness content and catalog optional capabilities
type: task
status: done
priority: p1
epic: 7
blocked-by: []
interactive: false
created: 2026-11-16
---

## Goal

Maintain shared harness content once under `template/`, with reproducible agent adapters and
a catalog that distinguishes the common base from optional app/stack capabilities.

## Context

Read `docs/specs/selective-harness-installation.md` and decision 0001.
Current paths: `template/.claude/skills/`, `template/.agents/skills/`,
`template/.claude/hooks/`, `template/.codex/hooks.json`, and agent briefs under each adapter.
`tools/setup`, `tools/check-skill-setup.py`, `tools/check-codex-agents.py`, and
`scripts/agent/check` rely on those paths. Root copies are used for dogfooding.

## Acceptance criteria

AC1. Shared skills/resources, instruction text, reviewer briefs and hook logic have one
maintained template source. Check: a scratch source edit reaches every applicable adapter
through the documented generation/linking process; parity checks detect stale generated copies.

AC2. The catalog identifies every currently shipped skill as base or optional and lists
applicability and dependencies. UI craft is optional. Check: catalog validation rejects missing
resources, unknown dependencies and cycles; every entry resolves to its canonical source.

AC3. Agent adapters contain only necessary discovery/configuration differences and can refer
to shared files without requiring another agent's setup. Check: generate each agent's layout
in isolation, parse its config and resolve all installed hook/skill/brief references.

AC4. Dogfooding and the current local setup remain usable during migration. Check: run the
documented regeneration, `scripts/agent/check`, and fresh `tools/setup` scratch installs;
all pass with the new canonical layout and no independent shared-content edits.

AC5. Maintainers can reproduce the layout and distinguish shared content from adapters.
Check: update `template/README.md`, `.agents/README.md`, relevant harness docs and root-copy
instructions; source citations remain intact and new design choices are labelled judgement calls.

## Verification plan

Before coding, map the criteria to existing parity/setup checks and missing fixture cases.
Review the canonical layout and catalog proposal with the owner before adopting it. Record
live Codex evidence and static checks/runtime limits for other agents per the existing decision.

## Constraints

Change template sources first. Generated files may be checked in if their regeneration and
drift detection are deterministic. Do not remove agent-specific permissions or pretend that
unsupported controls have equivalents. Keep project-side Python compatible with 3.10.

## Out of scope / do not change

Remote fetching, the new selection interface, changing skill behavior, and new skill authoring.

## Notes

2026-11-16: Completed; the owner explicitly authorized finishing the epic, marking its tasks done and merging to main. Evidence: `docs/evidence/7-selective-harness/README.md`; 24 installer tests, 13 full checks, independent review, actual GitHub install/update and final live Codex read. Claude runtime remains blocked by account verification; other limitations are recorded.
