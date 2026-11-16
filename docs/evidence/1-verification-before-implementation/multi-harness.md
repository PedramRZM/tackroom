# Portable verification planning — 2026-11-16

Base: `9f88d9a`. Implementation branch: `task/1-verification-portability`. The original
implementation is already committed in that history. The owner accepted this follow-up and
requested its commit, merge to main and task 1 done status on 2026-11-16.

## Required scope

The owner clarified that **all tasks must produce multi-harness setups**, while Codex is the
available live validation harness on this machine. Task 1 therefore requires shared packaging
for Claude Code, Codex and OpenCode plus live Codex planning. Static checks do not prove other
harnesses' runtime behavior, and unavailable model access does not block portable setup work.
This supersedes both the original mandatory Claude trial and the agent's mistaken expansion
to mandatory live trials in all three harnesses.

## Results

| Target | Observed result | Limit |
|---|---|---|
| Shared installation | Fresh `tools/setup --tracker files --codex --opencode` succeeded; shared skill links and references installed | Installation does not prove model compliance |
| Codex 0.169.0 | Both planning runs exited 0; actual command events read both skills, the verification reference and UI craft material; AC1–4 supported by review | Project-local config was disabled as untrusted; this does not exercise hooks/permissions |
| Claude Code | Fresh bounded run exited 1 with account restriction, `is_error: true`, $0 | No model response; runtime unavailable and not a gate under clarified scope |
| OpenCode 1.3.10 | Two exploratory runs returned plans, exit 0; initial run read both skills and reference | Plans failed behavioral/quality requirements; do not claim effective instruction following |

The OpenCode calls were made before the owner clarified that only Codex should be relied on
for live validation. The configured OpenCode provider did return output; this observation
does not change the owner's intended validation policy. No further OpenCode calls are needed.

### Codex criterion evidence

- AC1: [initial plan](codex-plan-20261116-first.md) gives viewer API denial with unchanged
  storage, approver success with persisted state, failure rollback, and real download content.
  It identifies unknown endpoints, fixtures, startup and reset commands rather than claiming
  application checks ran.
- AC2: separate CSS, JS/TS inline-style and utility-class enforcement; valid/invalid fixtures,
  namespaces, exceptions, dynamic-analysis gaps, setup and maintenance costs.
- AC3: separates interaction assertions, inspected versus compared screenshots, automated
  accessibility plus manual paths, and unverified representative-user usability.
- AC4: BDD examples and TDD loops are distinct from test levels; no compulsory Cucumber;
  copy-only work reuses existing checks without new tests or dependencies.
- AC5: the existing source audit remains applicable. The trial's proposed additional guidance
  was a local judgment candidate and was removed after it failed to resolve the observed gaps.
- AC6: fresh shared setup, live Codex reads/planning, repository validators and explicit
  per-harness limits above. See [final check output](checks-20261116.txt).

An independent read-only reviewer inspected both harnesses' actual reads and final plans,
confirmed Codex AC1–4 and OpenCode's deficiencies, and independently ran all 11 repository checks.

## Reproduction

The [scenario](scenario.md) was unchanged in every run. Initial scratch:
`/tmp/tackroom-verification-multi-20261116-EJdOcj`; candidate scratch:
`/tmp/tackroom-verification-recheck-20261116-NK3flt`.
Both were installed with `tools/setup <scratch> --tracker files --codex --opencode`, received
the scenario file, and were initialized with `git init -q`. The candidate additionally had
the [five-line change](rejected-omission-audit.diff); it is not in the final template.

Run from the scratch directory, using the same prompt for both harnesses:

```sh
timeout --signal=TERM --kill-after=10s 180s \
  codex exec --ignore-user-config --ephemeral --sandbox read-only --json --color never \
  -o <plan-output.md> \
  'Read scenario.md, .agents/skills/write-tests/SKILL.md and .agents/skills/verify/SKILL.md, follow their guidance and answer the two requests in scenario.md.'
```

The recorded OpenCode invocation, for reproduction when that runtime is available:

```sh
OPENCODE_CONFIG_CONTENT='{"permission":{"edit":"deny","bash":"deny","task":"deny","external_directory":"deny"},"agent":{"plan":{"steps":12}}}' \
  timeout --signal=TERM --kill-after=10s 180s \
  opencode --pure run --agent plan --format json \
  'Read scenario.md, .agents/skills/write-tests/SKILL.md and .agents/skills/verify/SKILL.md, follow their guidance and answer the two requests in scenario.md.'
```

No model was selected or global trust/account configuration changed. Codex used its runtime
default with user config ignored; the JSONL did not identify the model, so no model-comparison
claim is made. OpenCode exports identify `google/gemini-3-flash-preview` for both runs.
The timeouts did not fire. OpenCode's reported costs were $0.04921655 and $0.0228999;
these are reported estimates, not verified billing. Codex dollar cost was not reported.
Token usage is retained in [initial events](multi-harness-first-events.json) and
[candidate events](multi-harness-candidate-events.json).

These records preserve successful command/tool inputs, output hashes and completion usage.
Full stdout/stderr remain at each scratch path plus `-codex.jsonl`, `-codex-stderr.txt`,
`-opencode.jsonl`, `-opencode-stderr.txt` and `-opencode-export.json`. Claude's separate command
and result are in [its attempt record](claude-attempt.md#2026-11-16-retry).

## Failed candidate retained as negative evidence

[Initial OpenCode output](opencode-plan-20261116-first.md) substituted CSS grep for token
enforcement, omitted JS/utility fixtures and costs, and omitted visual-baseline, accessibility
and human-usability limits. It lacked persistence checks on denied/successful API calls.

The candidate added an explicit final-plan audit for those omissions. In the fresh
[candidate run](opencode-plan-20261116-candidate.md), OpenCode read the changed skill but
still omitted those requirements; it also did not read the supporting reference. A download
handler call count would not prove a valid download, and its suggested `/invoices/i` heading
assertion would accept the old text. No actual application tests were written or weakened.

The [Codex candidate plan](codex-plan-20261116-candidate.md) still covered AC1–4. Nevertheless,
the added guidance did not fix the targeted failure, so it was removed from all copies.
The final skill content matches the successful initial Codex run. This is one initial and
one candidate sample per harness on a repeated scenario, not a held-out comparison or proof
of generalized improvement. Task 3 retains that evaluation responsibility.

## Remaining limits

No running invoice app, browser journey, usability study, full hook/permission lifecycle,
vendor launcher live endpoint or comparative benchmark was exercised. Setup discovery and
configuration checks remain distinct from these claims. The owner selected Scinito for task 2;
task 3 needs its controlled trial. Epic 0 is not complete.
