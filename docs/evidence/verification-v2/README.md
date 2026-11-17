# Verification v2 evidence — 2026-11-17

Base: `8531d468da44b9a53ed0d5418db9647ece9c415c`. Candidate: uncommitted working tree,
identified by [review input hashes](review-manifest.json); review is provisional. Evidence
files are excluded from those hashes to avoid self-reference. Review ran before committing;
the owner subsequently authorized commit and push to main. No release tag, external project
update or global trust change is part of this work.

Status: **partial**. Repository checks and packaging pass; the available live planning test
has three omissions, Claude model access is unavailable, and improved effectiveness is unmeasured.
This is a guidance revision, not proof of a protected verification gate.

## Checks and installation

Baseline full checks passed all 13 after retrying outside the sandbox. The initial sandbox
attempt failed six checks because uv could not write its cache and network fixtures could not
bind a local socket. No code changes were used to turn those environmental failures green.
Final [full check output](checks.txt) is retained; `git diff --check` also passed.

`tools/setup /tmp/tackroom-v2-smoke-afppbmii --agents claude,codex,opencode --tracker files`
installed the shared skills, workflow and new REVIEW.md byte-for-byte. All three generated
reviewer adapters contained the pinned-target instructions. A subsequent `--update` preserved
a customized REVIEW.md and project memory. [Assertions and output](install.txt),
[installed input hashes](installed-manifest.json). An independent reviewer reproduced these
checks in another scratch project and passed all 13 repository checks on its frozen target.

## Live planning trial

The [five scenarios](scenario.md) and [rubric](rubric.md) were written before the model runs.
They are exposed planning cases, not a held-out comparison. No application implementation,
browser journey or real migration was tested by these prompts.

From the installed scratch directory, Claude was run with:

```sh
timeout --signal=TERM --kill-after=5s 90s claude -p --setting-sources project \
  --permission-mode plan --output-format json \
  'Read scenario.md and the installed guidance it names. Answer all five cases. Do not edit files, commit, push, or run any live application actions.'
```

Exit 1, account restriction, `is_error: true`, reported cost $0. No model response and no
successful Claude behavior claim. [Result](claude.json) omits the account-specific portal link;
[stderr](claude-stderr.txt) is retained.

Codex was then run with:

```sh
timeout --signal=TERM --kill-after=5s 180s codex exec --ignore-user-config --ephemeral \
  --sandbox read-only --json --color never -o <codex-plan.md> \
  'Read scenario.md and the installed guidance it names. Answer all five cases. Do not edit files, commit, push, spawn agents or run any live application actions.'
```

Exit 0. [Events](codex-events.jsonl) show successful reads of the scenario, WORKFLOW.md,
REVIEW.md, all three requested skills and the verification-tools reference. The model used
the runtime default; no model ID was pinned or effectiveness comparison attempted. Reported
usage: 81,701 input tokens (54,016 cached), 809 output, 13 reasoning output; no billing claim.
The [warning](codex-stderr.txt) says project config was disabled as untrusted. This tests
explicit skill reading and planning, not automatic discovery or hook/permission behavior.

| Case | Result against the prewritten rubric | Evidence in the retained answer |
|---|---|---|
| Migration | Pass | Pins old revision, same inputs/errors/side effects, replay data, limited normalization and approved exceptions |
| Rubric / moving target | Partial | Base rubric, exact B and dirty snapshot addressed; does not explicitly say reuse the reviewer and prior findings |
| Repeated failure / flakes | Pass | Escalates after three, discloses retry-green, rejects deletion and requires approved quarantine |
| Local / preview handoff | Partial | Keeps local checks, evidence, human preview steps/data and no inferred CI gate; does not explicitly attach results/screenshots to the task |
| New-file change / gate | Partial | Refreshes checks/review and hashes new content, observe-first adoption; does not explicitly record verified/partial/none and gaps for this case |

[Full answer](codex-plan.md). Two complete and three partial cases; do not score omitted items
as inferred passes. We have not added more prompt reminders or rerun until green. The template
contains the missing directions, but one planning trial cannot establish reliable compliance.

## Independent review and limits

The reviewer used a frozen snapshot rather than moving branch names, verified 68/68 initial
input hashes, independently ran checks and installation/update probes, and found no Important
defect in the guidance itself. It flagged the missing final evidence record and stale reviewer
invocation metadata. This record supplies the evidence; metadata now requests pinned IDs or a
frozen snapshot. Follow-up review confirmed those fixes and caught an overgenerous score for
case 4: the answer lists handoff contents but omits explicit publication to the task. The table
above uses the corrected independent score. The final affected review confirmed all findings
resolved. No extra prompt reminder was added to force a pass. Source hashes identify the
reviewed template; the later owner-authorization wording change in the comparison is recorded
separately in the manifest.

Concurrent owner work added preview fixture/configuration details during this task. Those
changes were preserved and included in the final input manifest; they are owner-directed
policy, not a claim derived from the article.

Not run: live Claude behavior (account-blocked), live OpenCode, full Codex hook/permission
lifecycle, a real application's smoke/reset/failure harness, protected external enforcement,
or vendor launchers against live endpoints. Codex planning did run; older memory saying
Codex has never run is historical and does not describe this trial. No claim of v2 quality
uplift or of reduced reviewer time is made.
