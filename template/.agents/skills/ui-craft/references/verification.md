# Prove the details

Use the project's existing browser runner and lint setup. In the task's verification plan,
select the rows that match the changed surface and replace generic controls with actual names.
Keep screenshots for appearance and traces/assertions for behavior; neither replaces the other.

| Risk | Reproduction and expected evidence |
|---|---|
| Interruptions | Open/close/reopen a drawer before it settles; rapid button/icon toggles; last intent wins, no stuck overlay, duplicate request or lost focus |
| Tooltip intent | First hover waits; cross directly to a peer and it opens immediately; leave the group, wait for reset, and first delay returns; focus/Escape work |
| Fragile submenu | Traverse diagonally through the gap, then away; submenu stays during approach and dismisses on departure; repeat after collision flip and with keyboard |
| Layout shift | Hold image/font/data responses, capture reserved boxes, release, compare; loading/error/empty swaps preserve intended geometry |
| Numbers / labels | Exercise 9→10, 99→100, longest timer and locale separators; surrounding positions and button bounds stay stable |
| Touch / obstruction | Measure actual hit area at phone width, tap its edges, test neighboring controls and keyboard-open view; small artwork may sit in a 44 px button |
| Type | Longest supported strings, accents/scripts, zoom and WCAG spacing overrides; no clipped descenders, labels or controls |
| Optimism | Delay/reject/reorder responses; test double activation and retry; rollback is visible and cannot overwrite a newer success |
| Loading / empty | Fast/slow/error responses, first-use and no-results; no flashing skeleton, misleading success or dead end; action actually works |
| Motion preference | Reduced motion before load and while open; all content remains usable without spatial motion or animation-end dependencies |
| Performance | Repeat sidebar/menu interactions under controlled CPU/network throttling; inspect long frames and input latency; report device/conditions, not just “smooth” |
| Scroll fades | Start/middle/end, no overflow, RTL, resize and keyboard focus; fade disappears at reached edges and never eats a click |
| Gallery / morph | Open, interrupt, go back, missing image and reduced motion; stable identity, crop, final state and focus restoration |
| Visual restraint | Inventory semantic color/type/icon roles and inspect rendered combinations; optical weight and accent hierarchy need judgment |

“Gorilla” here means focused interaction stress: choose a short repeatable sequence (for example
ten rapid open/close cycles), assert the final state and collect console errors. Increase the
stress only if the failure warrants it. This differs from **guerrilla usability testing**, in
which people try tasks; an agent clicking controls is not evidence that users understand them.

## Avoid misleading browser evidence

- Browser automation may wait for an element to stop moving before clicking. For an
  interruption test, capture stable trigger coordinates and send actual pointer events during
  motion (or test the independent Escape control). Record timestamps/state so the test proves
  overlap. Dispatching a DOM event alone bypasses hit testing and does not prove touch usability.
- Measure `getBoundingClientRect()` for controls and changing slots, computed line height and
  `fontVariantNumeric`, plus `scrollWidth/clientWidth` for overflow. Bounds alone do not prove
  unobstructed hit areas: check interaction/overlap. A font property alone does not prove the
  font contains tabular figures; compare rendered values too.
- CLS excludes some shifts soon after input. A good CLS value can miss an annoying drawer or
  counter jump. Compare the affected rectangles before/after and inspect the recording as well.
  Register a layout-shift observer before loading when supported; lack of support is not zero.
- Use the runner's reduced-motion emulation, delayed network routes and deterministic fixtures.
  Throttling is a lab condition, not proof of low-battery behavior on a physical phone.
- Choose the app's supported phone/desktop widths, themes and locales. Review screenshot
  differences against the intended change; never regenerate baselines simply to get green.

## Deterministic lint: @shadcn/lint

The official [shadcn-ui/lint](https://github.com/shadcn-ui/lint) package is `@shadcn/lint`, an
ESLint/Oxlint plugin for Tailwind v4 design systems; shadcn/ui components are not required.
It can constrain token classes, component use and variants according to configured policy.
It is not a universal `shadcn lint` command or a rendered design-quality judge.

For a compatible project, read the installed version's official README/SETUP, inspect its
tokens/components and existing lint config, then select rules for demonstrated gaps. Pin the
dependency using that project's package manager; run it through the normal lint/check command
and CI. No unconditional dependency belongs in this framework-neutral template.

Prove configuration with a valid semantic class, a forbidden raw/arbitrary value and a
disallowed component/restyle in the supported syntax. Check invalid component variants with
the type checker; do not assume lint checks variant prop validity. Check that each negative
case actually fails. Review exemptions and token-definition changes. Document blind spots:
plain CSS/`@apply`, imported class values, unknown spreads and parent-selector restyling may
escape analysis. It cannot prove contrast, hit targets, interruption, recovery or good taste.
For other stacks use the existing equivalent; the neighboring `write-tests` tool reference
describes tested ESLint/Stylelint policies. Repeated failures earn a rule, not another warning.

Sources: [official lint README](https://github.com/shadcn-ui/lint),
[lint analysis limits](https://github.com/shadcn-ui/lint/blob/main/docs/how-it-works.md),
[Playwright actionability](https://playwright.dev/docs/actionability),
[visual comparisons](https://playwright.dev/docs/test-snapshots),
[web.dev CLS](https://web.dev/articles/optimize-cls),
[WCAG evaluation](https://www.w3.org/WAI/test-evaluate/).
The scenario matrix and ten-cycle example are local verification choices.
