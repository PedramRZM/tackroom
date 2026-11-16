---
id: 10
title: Bootstrap the selected harness from GitHub without a local checkout
type: task
status: done
priority: p1
epic: 7
blocked-by: [9]
interactive: false
created: 2026-11-16
---

## Goal

Use a documented command from any app directory to fetch and install the selected tackroom
harness from GitHub, including a reproducible fixed-revision option.

## Context

`docs/specs/selective-harness-installation.md`, decision 0001, task 9's installer and
task 8's catalog. Source repository: `PedramRZM/tackroom`; default branch: `main`.
The owner permits GitHub raw downloads. Root README and `template/README.md` describe setup.

## Acceptance criteria

AC1. A documented bootstrap works without a tackroom checkout or access to its local files.
Check: run it from a fresh scratch app with only the documented prerequisites and install
Codex/base and a UI-capability example from the published GitHub source; record exact commands.

AC2. Default `main` and an explicit revision resolve to one commit per installation, reported
to the user. Check: a fixture changes the branch between requests and proves selected payloads
still come from one commit; a fixed-revision run reproduces the same selected source files.

AC3. Remote and local installation use the same catalog and selection rules. Check: compare
installed file bytes, executable modes, resource completeness and resolved discovery paths
for equivalent selections at the same revision; exclude research and unselected capabilities.

AC4. Fetch failures and invalid payloads fail before destination changes. Check: fixtures for
HTTP failure, unavailable revision, interrupted content, malformed catalog, missing selected
file and escaping paths all exit nonzero with actionable errors and an unchanged destination.

AC5. Installation is reviewable and preserves project ownership. Check: remote dry run and
rerun against a customized fixture retain local bytes and show conflicts, matching task 9;
the bootstrap neither commits changes nor installs global configuration or background updates.

AC6. Published instructions match the shipped installer and its limits. Check: full
`scripts/agent/check`, the remote scratch exercise after publication, and documented prerequisites,
revision selection, base/UI examples, supported adapters and untested agent runtime behavior.

## Verification plan

Use a local HTTP fixture for deterministic errors and revision consistency, plus one actual
published-source installation. Record the publication step and commit used; if implementation
is not yet on main, test the task revision and report the remaining main verification plainly.
Do not treat a local fixture as evidence that the public bootstrap works.

## Constraints

Review any new public command/distribution dependency with the owner before committing to it.
Fetch only installer metadata and selected template content. Preserve the existing no-sync
scope. Source commit identity provides reproducibility; it is not a claim of signed provenance.

## Out of scope / do not change

Package registry publication, hosted services, fleet management, automatic upgrades and new agents.

## Notes

2026-11-16: Completed; the owner explicitly authorized finishing the epic, marking its tasks done and merging to main. Evidence: `docs/evidence/7-selective-harness/README.md`; 24 installer tests, 13 full checks, independent review, actual GitHub install/update and final live Codex read. Claude runtime remains blocked by account verification; other limitations are recorded.
