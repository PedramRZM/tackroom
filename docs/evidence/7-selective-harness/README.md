# Selective installation and safe updates

Implementation starts at `43b7f19` on `task/7-selective-harness-installation`. The owner requested
completion/publication and added two requirements during implementation: explicit updates that
preserve project knowledge, and a fully agent-neutral template with native output built by the
CLI. Task 11 and decision 0001 record those scope changes.

## Acceptance evidence

| Criteria | Check and observed result |
|---|---|
| 8 AC1 | `test_source_edit_propagates_and_stale_adapter_detected`: edit one reviewer body, detect all three stale native outputs, update, identical new body in each; no native template directories |
| 8 AC2 | Catalog/dependency/resource tests reject unknown/cyclic dependencies and missing resources; `--list` distinguishes nine base skills, three optional skills and profiles |
| 8 AC3 | Each-agent/all-agent install matrix; `tools/check-codex-agents.py` parses native configs and compares briefs with their canonical body; hooks resolve under `.agents/` |
| 8 AC4 | `tools/render-harness --write --dogfood`, generated root parity, legacy selections and full repository checks pass |
| 8 AC5 | `docs/installation.md`, template README, AGENTS and harness docs name the single sources and generated outputs; original source citations retained |
| 9 AC1 | CLI tests exercise current/explicit targets, catalog output, missing selection and invalid names with no writes |
| 9 AC2 | All three agents alone/combined, base-only vs UI profile, complete resources and links; adding a skill only in its folder works without a second registry |
| 9 AC3 | Custom files and legacy links retained; malformed protected files and broken customized links report incomplete (exit 2), not success |
| 9 AC4 | Dry-run actions equal actual additions; byte/mode/link snapshots unchanged during dry run; escaping paths and aliases into project memory rejected |
| 9 AC5 | Static config/parity and bounded Codex file-reading probe; see runtime evidence and explicit trust limitations below |
| 9 AC6 | Legacy flags retain Claude-plus-all-skills behavior and print a notice; bare new install requires selection; docs explain copying sources now requires CLI generation |
| 10 AC2–5 | HTTP fixture proves one ref lookup, fixed commit payloads, local/remote byte/mode/link equivalence, pinned rerun, hash/missing/invalid/disconnected/truncated-tree failures with unchanged destination |
| 10 AC1, AC6 | Published bootstrap exercise is recorded separately after publication; no local checkout is used by that command |
| 11 AC1 | `--update` uses remembered choices; identical rerun snapshot remains unchanged |
| 11 AC2 | Old/new source fixtures update unchanged files, retain local changes as conflicts, restore missing harness files; unchanged upstream does not flag valid customizations |
| 11 AC3 | Upstream changes to even unedited memory/doc/task skeletons do not replace project data; dream report and transcripts retained; tracked updates do not recreate missing memory |
| 11 AC4 | Existing files adopted only when identical; differing local content stays untracked, preserved and reported on future updates |
| 11 AC5 | Dry-run/update and all download failures preserve file/state snapshots; published install/update is recorded separately |

Run `python3 tools/test_setup.py`: 24 tests pass. Full `scripts/agent/check` output is in
[checks.txt](checks.txt). Source and root runtime inventory are checked without a generated
catalog in git. The default Python here is 3.10; native TOML parse checks use the repository's
existing 3.11+ uv wrapper.

## Independent review and negative evidence

A fresh-context read-only reviewer ran all checks and reproduced three missed failure cases:
protected index paths that were directories/dangling links, unconditional optional-UI guidance,
and broken customized instruction links accepted when upstream was unchanged. The index-path
regression was observed failing for both shapes before its fix. All are fixed and covered;
UI references are conditional rather than making UI craft part of the base.

The final review found no Important issues. It ran all 24 tests and independently injected
truncated root tree, duplicate blob entries, source symlink modes and invalid Git blob hashes.
Each failed before destination mutation. It verified adding a skill changes only its folder.
No reviewer modified repository files.

Initial selected-install CLI tests failed against the previous installer because `--agents`
and `--profile` did not exist. The implementation made them pass. A resource-validation bug
mistook external URLs for relative files; the parser now skips URLs, and the existing skill
corpus plus a missing-resource fixture cover the distinction.

## Runtime limits

The initial bounded Codex 0.169 probe exited 0 and actually read UI craft, its motion resource,
verify and generated Codex hook configuration in a scratch project without `.claude/`.
[runtime.json](runtime.json) retains commands and output hashes; [answer](codex-answer.md)
retains its response. Project config was untrusted/disabled, so this is evidence of readable
shared files and usable paths, not hook enforcement or model compliance beyond this example.
The final published-source probe is recorded with the public exercise.

Claude 2.1.323 was attempted with project-only settings, two-turn and $0.10 caps, and an external
60-second timeout. It exited 1 with account verification required (403), no model response and
reported cost $0. No account/global trust settings were changed. OpenCode received installation
and native config checks only. Vendor launchers were not run against live endpoints. Full
trusted hook/permission lifecycle and live OpenCode model behavior remain unverified.

## Limits of updates

Updates are explicit and per-project, with no background/global registry. Local edits require
manual conflict resolution; obsolete files are reported and retained, not pruned. A download
failure is mutation-free. A local write/permission failure can leave earlier files installed;
individual regular-file writes are atomic and rerunning reconciles them. Concurrent writers
are unsupported; run while the project is not changing. Git blob verification establishes
consistency with the pinned tree, not signed provenance or a trust boundary against a modified
installer or local tracking file.
