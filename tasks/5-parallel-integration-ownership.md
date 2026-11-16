---
id: 5
title: Make parallel integration and review finding validation explicit
type: task
status: inbox
priority: p3
epic: 0
blocked-by: []
interactive: false
created: 2026-11-15
---

## Goal

When parallel work is justified, one owner verifies the combined result and checks candidate
review findings before presenting them as defects.

## Context

`template/WORKFLOW.md`, `template/.claude/skills/second-opinion/SKILL.md`, reviewer briefs,
and `refs/notes/2026-11-13-anthropic-staff-setup-audit.md` recommendations 2 and 4.

## Acceptance criteria

AC1. Optional guidance assigns separate edit scopes/worktrees and one integration owner.
Check: a scratch exercise with two independent changes has no conflicting writes/builds.
AC2. Combined checks run after integration. Check: demonstrate a combined failure missed by
individual checks, then retain the corrected final run.
AC3. Findings are reproduced/deduplicated and unsupported ones are labeled uncertain.
Check: seed one real defect and one plausible false finding; report which survived and why.
AC4. Keep the existing supervision limit and make specialist reviewers conditional on risk.
Check: record latency/cost and compare useful findings with the current single reviewer.

## Constraints

No automatic multi-agent swarm, fixed role hierarchy or cross-project orchestrator.

## Out of scope / do not change

Global agent configuration or additional paid services.

## Notes

2026-11-16: Owner requires multi-harness setups for every task. Keep ownership and review
guidance shared across Codex, Claude Code and OpenCode; exercise it live in Codex here and
check other harness packaging/configuration without claiming unrun runtime equivalence.

2026-11-15: Optional follow-up; existing independent review remains the default.
