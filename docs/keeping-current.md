# Keeping this current

The sources agree that a setup like this goes stale: models improve and make parts of it
unnecessary, tools rename things, and guidance written for one model constrains the next
(`docs/principles.md`, principle 12). This is the routine for keeping it honest. All of it is
manual, on purpose.

## When something new is published

    tools/refs watch            # what is new or changed since the last mark
    tools/refs article <url>... --collection <name>     # save what is worth keeping
    tools/refs video <id>...    --collection <name>
    tools/refs post <url>...    --collection <name>
    tools/refs index            # rebuild refs/INDEX.md
    tools/refs watch --mark     # record the current state as seen

`watch` reads `refs/sources/watch.toml`: the Claude Code team's blog, Anthropic's articles and
guides, the Claude Code docs index, Anthropic's engineering page, and the Claude Code changelog.
Add a site there when a new source earns a place.

After saving, read the new item and ask one question: does it change anything in `template/`
or contradict something in `docs/`? If so, change the template, update the doc and its citation,
and note it in the relevant file under `refs/notes/`.

## At a new model release, and every three to six months

Anthropic's own advice is to review instructions, skills and hooks on that rhythm, and Boris
Cherny describes deleting them and re-adding only what the model still gets wrong
(`refs/notes/anthropic-claude-com-practice.md`, finding 10;
`refs/notes/talks-anthropic-and-others.md`, finding 2).

1. Run `/doctor` in a project that uses the template. It flags outdated or conflicting
   instruction files and estimates what the skills cost in context.
2. For each skill: does the model now do this without it? Turn the skill off for a few real
   tasks and compare. Delete what no longer changes the result.
3. For each line in a project's `AGENTS.md`: is it still true, and has it mattered lately?
4. For each hook rule: has it fired? A rule that never fires is either working as a deterrent
   or dead weight; check the cases it was written for.
5. Re-read `docs/claude-code.md` against the changelog since the last review. Settings keys,
   permission behaviour and defaults change between versions.
6. Re-check the vendor model names in `scripts/agent/claude-with` and `opencode.json`.

## Weekly, per active project

`/dream`, then review `git diff .agents/memory` and `.agents/dream-report.md`. Accept
proposals one at a time. See `docs/memory-and-dreaming.md`.

The existing report already captures human corrections and their disposition. Link measured
agent failures and explicit owner corrections from the inbox; do not create a second feedback
store. [Task 3's trace](evidence/3-verification-workflow-evaluation/feedback.md) shows both,
including a correction that needs no additional instruction. Recording a lesson is not proof
that it prevents recurrence; evaluate a proposed change before adopting it.

## Changing the template

- Edit canonical files in `template/`, run `tools/render-harness --write --dogfood`, then run
  `scripts/agent/check`. The check fails if generated root outputs are stale.
- Try a changed hook, skill or settings file in a scratch project before relying on it:
  `tools/setup /tmp/<name> --agents claude,codex,opencode`, then exercise it with the available harness.
  Here Codex is the live validation target; retain static packaging checks for Claude Code
  and OpenCode and state their runtime gaps. See the
  [owner's validation scope](decisions/multi-harness-validation.md).
- A project does not update itself in the background. Run `tools/setup <project> --update`
  for explicit local-source updates, or use the [GitHub update command](installation.md).
  Preview with `--dry-run`; locally edited files and project knowledge remain protected.

## Known gaps

Things the sources recommend that this repository does not have yet, most important first:

1. **Representative evals for the skills.** The sources treat an eval as the test of a skill and the gate for
   changing one (`refs/notes/devcon-1-skills-context-memory.md` (a);
   `refs/notes/anthropic-claude-dev-blog.md` (i)). Start small: ten to twenty real prompts per
   skill that should and should not trigger it. Task 3's bounded synthetic comparison is
   initial evidence, not a representative benchmark or a skill-discovery evaluation.
2. **A run of the whole task loop on real work**, and a few weeks of dream passes, to find out
   what in `WORKFLOW.md` is friction. The same goes for `kickoff` on a real idea.
3. **Two research passes were stopped early**: testing and performance, and new projects and
   stack selection. `docs/testing.md` and `docs/new-project.md` say which parts rest on few
   sources (server-side performance, random-input testing, any comparison of stacks).
4. **Vendor launchers have not been run against live endpoints.** Codex now has bounded
   task 1 planning and task 2 implementation evidence; the full hook/permission lifecycle
   and comparative Claude/OpenCode effectiveness remain unverified.
5. **The sandbox has not been run** on the build machine (`docs/claude-code.md`).
6. **Saved articles sometimes lose tables, code blocks and figures.** Notes that relied on a
   live page say so.
7. **About a dozen talks had no captions**, including both "What's new in Claude Code"
   sessions (`refs/notes/talks-anthropic-and-others.md`, "Failed or missing").
