---
name: verify
description: Prove a change works before calling it done. Runs the project's checks, exercises the changed behaviour the way a user or caller would, and reports evidence for each acceptance criterion. Use after any code change, before a commit or pull request, and when asked to verify, test, check that it works, or prove it.
---

# Verify

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

If any step fails, fix the cause and start again from step 1. Do not hand back work that is
partly verified without saying which part.

Use the pre-implementation verification plan when one exists. Report an uncovered criterion
as a gap; do not substitute a cheaper check that cannot establish the same result.

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

Identify the tested revision (and uncommitted changes), environment or preview, and necessary
data/role. One line per criterion, then checks, then what you could not verify:

    AC1  pnpm test cart.test.ts            4 passed
    AC2  /cart at 412px and 1440px         total updates on quantity change, console clean (screenshots: ...)
    Checks  scripts/agent/check            all 3 checks passed
    Not verified  payment webhook          needs the provider sandbox key

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
call, and keep this section pointing at it.
