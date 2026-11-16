---
id: 7
title: Install a shared harness selectively from any app
type: epic
status: inbox
priority: p1
epic:
blocked-by: []
interactive: false
created: 2026-11-16
---

## Goal

Install tackroom from within any project, selecting its agents and relevant app capabilities,
from one maintained template on GitHub.

## Context

`docs/specs/selective-harness-installation.md`,
`docs/decisions/0001-selective-harness-installation.md`, `tools/setup`, and tasks 8–10.

## Acceptance criteria

AC1. Common harness content has one maintained source, with small supported agent adapters and
a catalog separating base from optional capabilities. Check: task 8's generation/parity and
catalog checks pass; UI craft is explicitly optional.

AC2. A developer selects agents and capabilities without installing unrelated setups or
overwriting project-owned files. Check: task 9's scratch matrix covers each agent alone,
all three together, base-only, UI craft, dry run and existing-file conflicts.

AC3. A documented command installs from GitHub in an app without a tackroom checkout.
Check: task 10's published-source scratch run records its resolved commit and working files;
pinned-source and failed-download checks pass.

## Constraints

All tasks stay in the inbox until the owner marks them ready. Preserve the project's ownership
of installed files and the supported Codex/Claude Code/OpenCode scope. Use the validation
policy in `docs/decisions/multi-harness-validation.md` and report runtime gaps.

## Out of scope / do not change

Cross-project management, background updates, global configuration and authoring new skills.

## Notes

2026-11-16: Filed from the owner's request. Suggested order: 8 → 9 → 10. Publishing these
planning files to main does not mean the installer has been implemented.
