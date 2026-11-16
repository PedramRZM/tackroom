# Craft by surface

The house choices below express the owner's taste. Sources explain the mechanisms, not proof
that this combination improves every product. Use existing project tokens in place of examples.

## Stable layout and numbers

Reserve image geometry with intrinsic `width`/`height` or a deliberate `aspect-ratio` frame.
Reserve late charts, embeds and loading slots too. Preserve the frame on error/empty results;
test both before and after fonts and media load. A guessed fixed height must still allow long
copy and zoom. Prefer intrinsic sizing and `min-block-size` over clipping.

Changing counters, timers and aligned numeric columns use `font-variant-numeric: tabular-nums`
in a supporting font. This equalizes digits, not digit counts, signs or separators: reserve
the widest realistic formatted value, including localization. Keep pending button geometry
and its original label stable. Preserve reading position during background refresh; let a
person reveal new items rather than inserting them above what they are reading.

Sources: [web.dev CLS](https://web.dev/articles/optimize-cls),
[Vercel, Layout/Content/Performance](https://vercel.com/design/guidelines).

## Type, icons and color

- Define font family, size, weight and line height together per type role. Body copy generally
  needs more relative leading than large headings; use unitless line heights, then inspect
  the actual font, line length, scripts and wrapping. There is no universal font-size formula.
  House starting ranges, if there are no tokens: body 1.4–1.6, headings 1.1–1.3. These are
  judgments to tune, not compliance thresholds. Do not force multiline labels into fixed boxes.
- Verify text-spacing overrides without lost content or controls: line height 1.5, paragraph
  spacing 2em, letter spacing .12em and word spacing .16em. WCAG specifies resilience to user
  overrides; it does not require these as the authored design values.
- Choose a consistent icon family and semantic meaning. Balance perceived icon stroke with
  label weight at the rendered size; optical alignment can differ from geometric centering.
  Do not equate a CSS font-weight number to a stroke width. Decorative icons stay out of the
  accessible name; icon-only controls need names. Reuse icons, avoid arbitrary emoji decoration.
- House color budget: neutral surfaces/text, one main accent family, plus semantic status
  colors when needed. Brand and accent may differ. Count semantic roles rather than pixels
  in photos or antialiasing. Charts can need more colors; distinguish categories with labels
  or shapes too. Color restraint never justifies low contrast or color-only status.
- Use space and type hierarchy before adding borders and cards. For nested rounded surfaces,
  consider concentric radii (inner radius approximately outer radius minus inset), then inspect
  visually. This is a useful construction, not a rule for unrelated overlapping surfaces.
- Consider balanced heading wraps and prettier paragraph wraps where supported; check real
  copy rather than inserting brittle manual breaks. A subtle inset image outline can separate
  media from its surface without changing the image's dimensions.

Sources: [Jakub, Details](https://jakub.kr/writing/details-that-make-interfaces-feel-better),
[Vercel, Layout/Design](https://vercel.com/design/guidelines),
[Butterick, Line spacing](https://practicaltypography.com/line-spacing.html),
[WCAG text spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html).

## Waiting, empty states and optimism

- Use a skeleton when the upcoming structure is predictable; match its actual geometry. Avoid
  generic bars unrelated to the result. Keep useful existing content during refresh, distinguish
  it as stale when needed, and prevent a stale response from replacing a newer result.
- Delay a pending indicator enough to avoid a flash on fast responses; never delay immediate
  press feedback. Tune a short delay with measured latency. Do not hold useful results hostage
  to a skeleton animation. Static placeholders are a valid reduced-motion version. Long waits
  need honest progress/status and cancellation where supported, not endless shimmer.
- Distinguish first use, no matches, a completed queue and an error. Offer the relevant next
  action: create/import, clear filters, or retry. Keep the query and filters on no matches.
  An all-clear state need not manufacture more work. Several empty modules should not produce
  a wall of competing primary buttons.
- Optimism is for likely, reversible success with a predictable local result, such as saving
  an item. Reconcile with the server, handle failure visibly and preserve input. A retry must
  not duplicate the action. Test rapid toggles and out-of-order responses: an old failure must
  not roll back a newer success. Do not fabricate final payment, permission or inventory results.
- Undo needs a real reversible operation and an accessible recovery path; a disappearing toast
  alone is a poor place for the only recovery action. Announce important async status without
  repeatedly interrupting assistive technology.

Source: [Vercel, Interactions/Content](https://vercel.com/design/guidelines).
[Carbon, Empty states](https://www.carbondesignsystem.com/building-blocks/core/patterns/empty-states)
supports distinct empty states and action restraint. Concurrency and indicator tuning are
local engineering judgments.

## Touch, overflow and context

Use at least 44 × 44 CSS px hit areas for touch controls as the house default; the visible icon
can be smaller. Check spacing, overlap and obstruction, not only bounding boxes. WCAG 2.2 AA
target size is 24 × 24 with exceptions; 44 × 44 is the enhanced AAA criterion with exceptions.
An apparent missed tap can also come from an overlay, gesture cancellation or a blocked main
thread. Diagnose it rather than only enlarging the icon.

Horizontal or vertical scroll fades hint at hidden content. Show a fade only on an edge with
more content, remove it when everything fits, and avoid covering text or focus rings. Overlaid
decoration must not intercept input. Keep scrolling discoverable and keyboard operable; test
RTL and high zoom. Do not hide scrollbars merely to look polished.

Preserve meaningful filters in the URL and restore scroll/focus on return from detail. Keep
dragged content readable beside/above the finger when precision matters, and offer keyboard
and tap alternatives. Use platform controls before custom gesture machinery.

Sources: [WCAG minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html),
[enhanced](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html),
[Rauno, Touch Content Visibility](https://rauno.me/craft/interaction-design),
[Jakub, Details](https://jakub.kr/writing/details-that-make-interfaces-feel-better),
[Bramus, Scroll shadows](https://www.bram.us/2019/10/24/pure-css-scroll-shadows-vertical-horizontal/),
[Vercel, Interactions](https://vercel.com/design/guidelines).
