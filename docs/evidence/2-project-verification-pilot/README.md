# Project verification pilot — agent-dev-infra

2026-11-16. Owner switched from Scinito to agent-dev-infra after Scinito's known baseline
failures. This pilot exercises the existing read-only Coder readiness CLI, not the proposed
controller or live company infrastructure. No browser UI or persistent application database
exists in this selected command-line application; the isolated provider fixture supplies
seed/reset state and CLI output supplies user-facing artifacts.

## Source and reproduction

Target base: `19b8f90b709f45ef886909b94d5cf0c9185f746e`. Additions are committed as `ffc402c` and preserved in
[agent-dev-infra.patch](agent-dev-infra.patch): a five-test process suite and its local recipe.
Working copy: `/tmp/agent-dev-infra-tackroom-task2`, branch
`task/tackroom-2-readiness-verification`. Original checkout's memory edit was preserved.
On owner approval, `ffc402c` was fast-forwarded into its source branch
`task/013-scinito-coder-canary`. No unrelated infrastructure branches were merged to main.
Tackroom task 2 was accepted for completion and local merge; nothing was pushed remotely.

To reproduce in a separate checkout at that revision, apply the saved patch, then run:

```sh
python3 -m unittest discover -s tests -p test_coder_readiness_process.py -v
scripts/agent/check
```

The recipe is `docs/readiness-verification.md` in the patched target. Python 3.10.13 was used;
all runtime test dependencies are standard-library modules. The first command creates local
provider fixtures, starts the actual CLI as a subprocess, asserts health/results, reseeds and
verifies reset, then removes its temporary directories. It does not use the real Coder binary.
No package installation, app deployment, infrastructure mutation or paid provider call occurs.

## Acceptance evidence

| Criterion | Evidence | Result and limit |
|---|---|---|
| AC1 | [CLI journey output](cli-journey.json), focused suite and documented recipe | Ready → unhealthy → reseed → ready; caller-visible JSON and state-preservation assertions pass. CLI invocation is start/health; no service/database lifecycle is claimed |
| AC2 | [Deliberate defect red](readiness-defect-red.txt), [restored green](readiness-defect-green.txt), [mutation record](negative-control.json) | Setting dispatch authorization true causes three assertion failures, exit 1; restoring it yields five passes, exit 0. Denied provider read and malformed JSON return application exit 1 without raw provider data |
| AC3 | [Valid policy fixture](policy-valid.txt), [invalid](policy-invalid.txt), [restored](policy-restored.txt) | Existing repository checker accepts compatible Python, rejects `except*` under the Python 3.10 policy, then passes after removal. This is the existing syntax gate, not a new style/type/UI linter |
| AC4 | [Fresh Codex execution](fresh-codex-events.json), [summary](fresh-codex-summary.md), [source manifest](reproduction-manifest.json), [harness checks](harness-static.txt) | Fresh process ran focused tests (5) and full suite (34), both exit 0; no skips or test retries. Shared paths/configuration checked statically; no live Claude/OpenCode claim |

Expected outcomes are independently specified by the existing readiness test contract and
shared-Coder runbook: observations must never grant task dispatch or establish free capacity.
The added tests execute the real application process; only the external Coder executable is
replaced. The older unit tests still own exhaustive state mapping; this suite covers process
launch, argument forwarding, exit/output handling, fixture preservation and reset.

The [baseline](agent-dev-infra-baseline.txt) passed 29 tests; the
[final target check](agent-dev-infra-final.txt) passed 34. Existing tests were not edited.
Tackroom's [final check](tackroom-final.txt) passed all 11 gates.
Independent review reproduced the suite and challenged additional defects: accepting a failed
provider read and ignoring unhealthy workspace state both failed the new tests. Restored
source passed. The five-line failed guidance experiment from task 1 is unrelated to this pilot.
Final evidence review confirmed AC1–AC4 with no outstanding findings.

## Fresh session details

Fresh directory: `/tmp/readiness-fresh-codex-a8av27g9`. It was extracted from `git archive`
of the base and received the saved patch, then `git init -q`. Because there is no commit in
that extracted checkout, Codex correctly reported `git rev-parse HEAD` failure. Source
identity is established separately: every base file was byte-compared with `git show` at the
recorded revision, both additions match their hashes, and the patch hash is in the manifest.
This Git metadata limitation did not fail either test command or change its expected result.

Codex 0.169.0 was invoked with `--ignore-user-config --ephemeral --sandbox workspace-write`,
`approval_policy="never"`, JSON events and a 180-second GNU timeout with ten-second kill grace.
Prompt: read `AGENTS.md` and the recipe; run the focused unittest command and full check;
use only fixture Coder, without changing project files, installing packages, committing,
pushing or contacting infrastructure. The process exited 0 without timing out.
It redirected bytecode caches to `/tmp`; actual commands and outputs are retained in the
execution record. Raw JSONL/stderr remain next to the fresh directory with suffixes
`-events.jsonl` and `-stderr.txt`. The transcript summary is retained verbatim, including its
source-identity limitation. Actual tool events, not that summary alone, establish execution.

CLI configuration files parsed and all 12 shared skills were present. Codex/Claude task,
write-tests and verify paths resolve to the same source files; OpenCode can use the shared
paths but this repository ships no OpenCode-specific configuration. This does not certify
automatic skill selection, hooks or permissions in any harness.

## Limits and Scinito history

This is offline CLI integration with synthetic provider responses, not live Coder/RBAC,
fleet admission, Scinito startup, durability, a deployed controller or a browser journey.
No screenshot/preview is applicable; actual CLI outputs are retained. The static gate covers
tool syntax plus existing JSON/role/link checks, not typing, general lint or design quality.
No production data, Coder lifecycle operation or vendor launcher endpoint was used.

The rejected Scinito target remains unchanged at `e4402c761`: typecheck passed, but baseline
lint had 59 errors/527 warnings and Jest had 24 failures across five suites. Full runner output
is retained in [scinito-baseline.txt](scinito-baseline.txt); each failed command is limited by
that runner to its last 60 lines, with trailing whitespace removed for Git. The user selected this alternate target instead of repairing
those unrelated failures. No Scinito failures were suppressed and no Scinito files changed.
