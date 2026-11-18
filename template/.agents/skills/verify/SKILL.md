---
name: verify
description: Prove a change works before calling it done. Runs the project's checks, exercises the changed behaviour the way a user or caller would, and reports evidence for each acceptance criterion. Use after any code change, before a commit or pull request, and when asked to verify, test, check that it works, or prove it.
---

# Verify

Verification workflow v2 — 2026-11-17.

A successful edit is not evidence. Work is verified when someone who did not write it could
look at what you show and agree it works.

## What counts as proof

1. **The checks pass.** Run `scripts/agent/check` (the full run, not `--quick`) and keep its output.
2. **The behaviour was exercised.** For each acceptance criterion, or each behaviour you
   changed when there is no task, run the check that proves it:
   - a bug fix: the test or reproduction that failed before the fix now passes. If there was
     no failing test, write one, and confirm it fails with the fix removed;
   - an API or CLI change: call it and show the response or output;
   - anything a user sees: run the app and use the feature. Click the control, submit the
     form, read the result. Take a screenshot before and after, and read the browser console.
3. **Nothing nearby broke.** Exercise the closest existing behaviour that shares code with the change.

On failure, record the cause and attempt, fix it, and rerun the focused check first. Run the
full checks again before handoff. After three unsuccessful repair rounds on the same check,
stop with the output, attempts and smallest reproduction; follow a stricter project limit
(such as stopping after the same fix fails twice). Do not retry unchanged code for a green run.

Use the pre-implementation verification plan when one exists. Report an uncovered criterion
as a gap; do not substitute a cheaper check that cannot establish the same result.
Read the diff against a pinned base revision, including staged, unstaged and relevant new files.
Apply matching reliability checks from the base revision's `REVIEW.md`, when present. Report
the matched rule IDs, results and gaps; proposed rule edits do not replace the current rubric.

Use the project's verification instructions to choose the environment, fixtures and evidence
location. Record the tested revision and observed results so the reviewer can repeat the check.

## UI and product evidence

For changed UI, use `ui-craft` if installed to select craft criteria and browser stress
recipes (interruption, delayed loads, optimistic failure, touch and reduced motion). If absent,
offer the optional UI profile and use the checks below with the project's existing tools. Keep the
results in the existing verification plan; do not create a second competing checklist.

Choose evidence for the changed risks; the neighboring skill's
[tool reference](../write-tests/references/verification-tools.md) explains selection.
These checks answer different questions:

- **Behavior:** assert the result after the interaction, including relevant failure/empty/
  permission states. A screenshot of a button does not prove its action succeeded.
- **Visual:** inspect the rendered result at relevant viewport sizes and themes. Where
  screenshot regression tests exist, stabilize browser/fonts/data and review each changed
  baseline against the task; a new baseline is not automatically correct.
- **Accessibility:** scan the relevant rendered states and test keyboard/focus/zoom as needed.
  Automated passes do not establish full accessibility; name untested assistive-technology paths.
- **Usability:** assess task completion, clarity and recovery. Agent review identifies concerns;
  claims about real users need observation of representative users, or remain unverified.
- **Performance:** when affected, compare the agreed budget in a controlled environment.
  Distinguish lab results from field behavior; a score is not proof of the whole experience.

## Report

Identify the tested commit and pinned base, environment, and necessary data/role. For an
uncommitted tree, retain a diff and a content-hashed snapshot/manifest of relevant files,
including new files; HEAD plus a dirty flag cannot identify what was tested. Keep artifacts
outside the snapshot or exclude them explicitly. One line per criterion, then checks and gaps:

    AC1  pnpm test cart.test.ts            4 passed
    AC2  /cart at 412px and 1440px         total updates on quantity change, console clean (screenshots: ...)
    Checks  scripts/agent/check            all 3 checks passed
    Not verified  payment webhook          needs the provider sandbox key

Record status as **verified**, **partial**, or **none**, plus evidence location and reason for
any gap. These are evidence records, not automatic commit stamps or an enforced gate. A skill
invocation alone is not proof. A review verdict covers only its recorded commit or snapshot;
later edits require affected checks and review to be refreshed before handoff.

Paste the lines the command printed. Do not describe a result you did not see.
Include skips, quarantines and retry-green/flaky results rather than hiding them in a pass
count. Review changed expectations, snapshots and gate configuration against the requested
behavior. Re-run affected evidence after further edits; final checks must cover the final tree.
For UI changes, say whether visual evidence is inspection or a comparison with a reviewed
baseline, what accessibility was checked, and whether usability was observed with users or
remains unverified. This does not require a user study for every change.

## Gotchas

- The Stop hook runs only the quick checks. A full run is still yours to do.
- Tests are the judge. A test that fails is information; changing or skipping it to get a pass
  is not verification. If the test is wrong, say so and stop.
- A passing test suite written in the same session as the code proves less than it looks:
  it encodes the same assumptions. Prefer a check that existed before, a reproduction from the
  task, or the running app.
- With the Bash sandbox on Linux, a sandboxed command cannot reach a dev server on the host's
  localhost, and Chromium will not start. Use the browser tool for UI checks, and if a test
  command needs the network or a browser, say so instead of reporting it as a code failure.
- Long output buries the result. Prefer quiet flags and show the summary lines plus any failure.

## This project

Add what is specific to this repository as it is discovered. The most useful things to have
here are the ones that let an agent drive the real app without help:

- how to start it, and how to tell it is healthy;
- how to sign in as a seed user, and what that user can reach;
- for each main feature: how to get to it, the data it needs, what a correct result looks like;
- the command that resets state.

When these steps are repeated often, put them in one small command-line script the agent can
call, and keep this section pointing at it. Reuse the project's feature map if one exists.
When changing this recipe, try a clean start, reset and repeat run; retain duration and a
deliberate failure's diagnostics (failed step, expected/actual result, logs or trace). Prove
setup failure cannot be reported as a passing smoke test.
