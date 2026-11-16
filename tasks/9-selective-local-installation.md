---
id: 9
title: Install selected agents and app capabilities from the shared template
type: task
status: inbox
priority: p1
epic: 7
blocked-by: [8]
interactive: false
created: 2026-11-16
---

## Goal

Run the installer in an existing app and choose the common base, agent adapters and optional
capabilities without installing unrelated setups or overwriting project-owned files.

## Context

`docs/specs/selective-harness-installation.md`, task 8's catalog/layout, `tools/setup`,
`tools/check-skill-setup.py`, `template/README.md` and the root README installation instructions.
Today Claude and all skills are mandatory; Codex/OpenCode and tracker selection use flags.

## Acceptance criteria

AC1. The documented command targets the current directory by default or an explicit project,
lists available selections, and accepts unattended agent/capability choices. Check: CLI fixtures
cover both targets, help/catalog output, unknown selections and missing required input with
clear errors and no mutation on invalid input.

AC2. Install exactly the selected adapters, base and optional capabilities plus their declared
dependencies. Check: scratch fixtures for Codex-only, Claude-only, OpenCode-only and all three;
base-only excludes UI craft, opting in includes its resources, and no discovery link is broken.

AC3. Existing project files, memory, directories and dangling links are preserved. Check:
compare fixture bytes before/after an install and rerun; list kept files/conflicts and clearly
report incomplete setup instead of claiming success when a collision breaks required paths.

AC4. Dry run produces an accurate change report without writing files. Check: compare its
reported additions/kept paths with an actual run in an equivalent fixture, including tracker
files and ignore-file additions; reject destination escapes through paths or parent symlinks.

AC5. The chosen agents discover the shared installed content and configuration remains valid.
Check: `scripts/agent/check`, the selection matrix, and a bounded live Codex scratch probe;
record other agents' static/configuration checks and untested runtime behavior explicitly.

AC6. Existing setup users have an explicit compatibility or migration path. Check: exercise
documented legacy invocations and new base/UI examples, preserving tracker choice and existing
files; intentional interface changes are explained in help and installation docs.

## Verification plan

Review the public command/runtime proposal before implementation. Extend existing setup
fixtures with exact installed-file expectations, collision cases and no-write assertions.
Record commands and expected outputs before coding, without changing these criteria.

## Constraints

One shared catalog drives selection; no per-agent skill forks. No global configuration changes.
Do not infer an app stack and silently add optional capabilities. Projects own installed copies.

## Out of scope / do not change

GitHub bootstrap, automatic updates, registry/sync, and destructive migration of existing apps.
