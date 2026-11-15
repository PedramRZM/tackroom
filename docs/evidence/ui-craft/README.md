# UI craft verification — 2026-11-15

Revision: base `23183fe` plus the uncommitted UI-craft change. Environment: this repository on
Ubuntu, Python 3.10-compatible template, installed Claude CLI. No application was changed.

## Criteria selected before the scratch trial

| Criterion | Check | Result |
|---|---|---|
| Every owner example is represented | Compare the 22-row coverage table with skill references; independent source reviewers | Covered, including both items numbered 19 |
| Sources and policy boundaries are explicit | Read 25 saved extracts; review dates, qualifiers and lint limits | Register records paths/locators and extraction caveats; variant testing corrected to type checking |
| Portable installation includes references | `tools/setup /tmp/tackroom-ui-craft-20261115 --codex` | `copied 49 files, linked 12 skills into .agents/skills` |
| Template itself exposes skills, with or without installer | `python3 tools/check-skill-setup.py` | Direct copy, default/Codex/OpenCode/combined installs, resources, dry-run and existing files pass |
| Codex reads the actual installed skill and references | Codex CLI 0.169 read-only fixture review | Exit 0; commands read `.agents/skills/ui-craft` and all three references; findings and plan saved |
| OpenCode discovers the installed skill | `opencode debug skill` in combined scratch install | Exit 0; `ui-craft` location is `.agents/skills/ui-craft/SKILL.md` |
| Skill format is valid | Skill-creator `quick_validate.py` on template skill | `Skill is valid!` |
| Model can apply guidance to a realistic flawed surface | Headless Claude scratch trial using `scenario.txt` | Blocked before a model response by provider account verification |
| Independent rehearsal finds actionable risks and appropriate checks | Separate agent reads skill, fixture and scenario, without an expected answer | Findings below; static review only |
| Existing harness checks remain healthy | Full `scripts/agent/check`, before and after | See `checks.txt` for final output |
| New source watch entries resolve | `tools/refs watch` | Emil 7, Jakub 10, Rauno 19 listed; lint page detected; 48 total new/changed including existing sources |

The watch state was not marked seen: discovering a URL is not reviewing it. The refreshed
research index contains 1,843 items after the portability source follow-up. The template's
always-loaded instructions gained one routing line; craft details remain in conditional references.

## Reproducible scratch trial

[`fixture.html`](fixture.html) is intentionally flawed, not a shipped UI or a proposed fix.
[`scenario.txt`](scenario.txt) is the exact trial prompt. It exercises `ui-craft`, `write-tests`
and `verify` together. After copying those files into a fresh setup directory:

```sh
claude -p --setting-sources project --output-format json "$(cat scenario.txt)" > result.json
```

Observed exit code: 1. Result fields: `is_error: true`, empty `permission_denials`, cost 0.
Provider text: “API Error: Your account can't receive replies from Claude right now.” It points
to Anthropic's account verification portal. The CLI also reported that three project allow
entries were ignored because the scratch workspace was not trusted. No global trust settings
were changed. This is a failed trial, not evidence that the skills were loaded or exercised.

## Independent scenario rehearsal

A separate agent was given the raw fixture, scenario and skill paths. It inspected files,
without running the page. Its findings included:

- The 600 ms `moving` guard discards the latest open/close intent.
- Width plus `transition: all` animates layout; the 800 ms entrance lacks reduced motion.
- Clipped closed-panel content stays focusable and the toggle lacks `aria-expanded`.
- Buttons specify 24 × 24, below the house touch policy; real hit areas still need measurement.
- Image geometry and the width needed for 99→100 are unreserved.
- Save claims success immediately, ignores HTTP/network failure and permits repeat requests.
- The empty state offers no useful action; mobile viewport configuration is absent.

Its plan selected in-motion pointer events with timestamps/final-state assertions; network
boundary tests for failure/retry; rectangle comparisons with delayed media; reduced-motion,
zoom and touch checks; and a working empty-state journey. It correctly warned that Tailwind
class lint does not cover the fixture's plain CSS. It did not claim browser execution.

This demonstrates useful explicit application of the instructions in one agent rehearsal.
It is not an isolated installed-Codex run, an automatic skill-routing eval, a comparison with
the skill absent, or proof of improved UX. No skill-effectiveness claim follows from it.

## Not verified

No complete Codex/OpenCode hook/permission workflow, vendor launcher against a live endpoint,
actual UI browser journey, physical phone/low-power test or observed user usability ran for this
change. `@shadcn/lint` was researched, not installed or executed in a consuming application.
Claude's behavioral trial remains blocked by the provider. These are distinct from the passing
repository validators and independent static rehearsal.

## Live Codex and OpenCode follow-up

Fresh combined setup: `/tmp/tackroom-ui-craft-portable-20261115`, 51 files and 12 skill links.
Codex command (no global trust edits or bypass flags):

```sh
codex exec --sandbox read-only --skip-git-repo-check --ephemeral --json \
  -C /tmp/tackroom-ui-craft-portable-20261115 \
  -o /tmp/tackroom-ui-codex-review.md - < scenario.txt
```

The trial completed with exit 0. Its executed reads—not just its self-report—loaded the shared
skill, all three references, `write-tests` and `verify`. See [Codex review](codex-review.md)
and [discovery/read evidence](portability.txt). It found dropped input, focusable hidden content,
premature success, missing recovery, small buttons, unstable media/numbers and reduced-motion
gaps. It correctly separated planned checks from executed checks. Its call to the scratch
`scripts/agent/check` exited 3: `no checks configured: edit scripts/agent/check`. This proves
the template does not pretend an empty project has application checks; it is not a passed UI test.

OpenCode's debug skill inventory independently reports the same skill at the shared path.
No OpenCode model call was made. The new repository check initially failed on default setup
(`missing shared skill kickoff`), then passed after making links unconditional. A further
assertion covers the literal template links and direct copy to catch the owner's reported gap.
