---
id: 11
title: Update installed harness files while preserving project knowledge and local edits
type: task
status: done
priority: p1
epic: 7
blocked-by: [9, 10]
interactive: false
created: 2026-11-16
---

## Goal

Run one update command to get the latest selected harness without changing a project's
memory, dream reports, transcripts, notes or locally customized harness files.

## Context

Owner's explicit follow-up while implementing epic 7 authorizes local update tracking and
sync. This supersedes the epic's original no-update scope, not its prohibition on fleet
management. Extend tasks 9–10's installer and bootstrap, not a separate sync tool.

## Acceptance criteria

AC1. An update remembers the installed agents, skills, profiles and tracker when no selection
is supplied. Check: install once, update with only `--update`, and compare selected paths.

AC2. Unmodified harness files receive upstream changes; local edits are preserved and reported
as conflicts. Check: old/new source fixtures with clean, customized, missing and already-current
files; a second update makes no unintended changes. Never delete obsolete local files silently.

AC3. Existing memory, dream reports, transcripts and project notes are never replaced or removed,
even if they still match an originally installed skeleton. Check: before/after byte snapshots
of those paths across an upstream change, both with and without prior install tracking.

AC4. Untracked existing projects can install missing files and establish tracking without
adopting different local content as overwriteable. Check: legacy fixture with local settings,
instructions and memory retains all existing bytes; later updates still preserve those edits.

AC5. Dry run and failed downloads leave project files and update tracking unchanged.
Check: local/HTTP fault fixtures and a real published GitHub update; document one-command
update, conflicts, protected data and no automatic pruning or global registry.

## Verification plan

Use deterministic old/new catalog fixtures and project snapshots plus a published bootstrap
install/update from a fresh app. State stores source fingerprints, not project content.

## Out of scope

Background synchronization, cross-project registry, forced overwrite and automatic merging
of user edits. No automatic removal of installed files or project data.

## Notes

2026-11-16: Completed; the owner explicitly authorized finishing the epic, marking its tasks done and merging to main. Evidence: `docs/evidence/7-selective-harness/README.md`; 24 installer tests, 13 full checks, independent review, actual GitHub install/update and final live Codex read. Claude runtime remains blocked by account verification; other limitations are recorded.
