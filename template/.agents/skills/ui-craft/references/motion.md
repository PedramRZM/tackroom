# Motion, intent and vocabulary

## Behavior before effect

Animations must yield to input: open→close→open while moving must settle to the last request,
without queued entrances, stale callbacks or disabled controls. CSS transitions can retarget;
springs can retain velocity when the implementation supports it. Keyframes, WAAPI and libraries
can also work when cancellation/retargeting is explicit. Never wait for animation completion
to commit essential application state. A snapshot/view transition is not automatically a live,
interruptible shared-element animation; test its input and interruption behavior.

Prefer transform and opacity, explicitly named rather than `transition: all`. They are a
performance starting point, not a guarantee: profile large layers, blur and compositing costs.
Motion should explain origin, hierarchy or feedback. Repeated keyboard actions and frequently
used menus often work better instantly. House timing starting points: feedback 100–160 ms,
small overlays 150–250 ms, larger spatial changes 250–400 ms. Tune by distance and frequency.

For a stagger, reveal the important content first while preserving reading/focus order. Keep
the first useful item immediate and cap the total sequence; do not multiply delays across a
long list. Priority-first choreography is our preference, not a universal ordering law.

Sources: [Emil, Toast](https://emilkowal.ski/ui/building-a-toast-component),
[Rauno, Responsive Gestures/Frequency & Novelty](https://rauno.me/craft/interaction-design),
[Jakub, Details](https://jakub.kr/writing/details-that-make-interfaces-feel-better).

## Intent-aware interactions

- **Tooltip warmup / hysteresis:** delay the first hover; once a tooltip is open, neighboring
  tooltips appear immediately without replaying the entrance. Reset after leaving the group
  for a short cooldown. Keyboard focus must expose help promptly; essential information cannot
  depend on hovering. Reuse the library's delay group/provider rather than per-tooltip timers.
- **Safe polygon / prediction cone:** moving diagonally toward a submenu must not close it
  when the pointer briefly leaves its trigger. Use the primitive's corridor when available;
  test narrow gaps, placement flips and neighboring targets. It must still dismiss when the
  pointer leaves intentionally and must not block unrelated clicks. Keyboard menus need their
  own focus/Escape behavior. Do not assume every component library enables this by default.
- **Origin-aware popover:** use the resolved placement's transform origin so the popup grows
  from its trigger even after collision handling flips its side. Avoid scale-from-zero flourishes.
- **Press feedback:** acknowledge press immediately; a small scale or color response can help.
  Commit ordinary button actions on activation/release so dragging away can cancel.
- **Gesture handoff:** scrolling inside a drawer must not accidentally become a dismiss drag
  at the top. Emil's implementation uses a short guard after scrolling, release velocity and
  one active touch. Treat its 100 ms guard as an example to test, not a platform standard.
- **Contextual icon crossfade:** when an icon changes state, fade old/new glyphs within one
  fixed slot. Keep the label/control size stable, suppress initial-mount flourish, and expose
  the real state semantically. Static icons beside labels do not need animation.
- **Attention-aware expiry:** pause transient message timers while the page is hidden and
  while the message is hovered/focused. Preserve an accessible route to important information.
- **Hover bridges:** gaps between related floating items should not repeatedly collapse the
  group. Extend its safe hover region without covering unrelated controls.
- **Pointer capture:** keep a drag attached when the pointer leaves its original bounds;
  handle cancellation and release capture on completion. Do not steal ordinary page scrolling.

Sources: [Emil, Seven tips](https://emilkowal.ski/ui/7-practical-animation-tips),
[Drawer case study](https://emilkowal.ski/ui/building-a-drawer-component),
[Toast, The big little details](https://emilkowal.ski/ui/building-a-toast-component),
[FloatingDelayGroup](https://floating-ui.com/docs/FloatingDelayGroup),
[safePolygon](https://floating-ui.com/docs/useHover).

## Reduced motion and constrained devices

Honor `prefers-reduced-motion` with a complete still or short opacity-only path. Remove spatial
travel, parallax, rubberband overshoot and stagger delays; preserve status and direct control.
No state may depend on a motion event firing. Test the preference changing while the UI is open.

Weak hardware and low-power mode are separate from motion preference. Use modest effects by
default, stop offscreen/background decorative loops, and profile CPU/network throttling plus
a real supported phone in low-power mode when available. Drop costly blur/shimmer before
dropping information. Do not require battery or memory detection: browser support and signals
are incomplete. An optional explicit reduced-effects setting is more honest than claiming
automatic low-battery detection everywhere. Use elapsed time, not frame counts, for custom motion.

Sources: [MDN reduced motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion),
[Vercel, Performance](https://vercel.com/design/guidelines).
The fallback/device policy is local judgment.

## Vocabulary: choose by purpose

| Term | Use / caution |
|---|---|
| Interruptibility / retargeting | Reverse from the current presentation; do not replay from the start |
| Spring, damping, stiffness, velocity | Describe physical settling; more bounce is not automatically better |
| Ease-out / ease-in-out | Immediate response / travel between positions; tune rather than copying a curve |
| Rubberbanding / resistance | Diminishing movement past a drag boundary; retain a clear reachable limit |
| Shared element / object constancy | Keep a gallery image identifiable from thumbnail to detail and back |
| Shared layout / FLIP | Animate between measured layouts (First, Last, Invert, Play); avoid scale-distorted text |
| Container transform / morph | One surface becomes another; preserve identity, crossfade changed contents |
| Origin-aware pop-in | Overlay expands from its actual anchor, including flipped placement |
| Crossfade | Blend state changes in a stable slot; avoid a flash of both readable labels |
| Stagger / choreography | Sequence a group; reading order and time-to-useful-content constrain it |
| Exit choreography | A quieter/quicker departure when appropriate; must not trap focus or input |
| Direct manipulation | Follow the finger continuously, then settle with release intent |
| Snap points / momentum | Discrete resting places chosen using distance and velocity |
| Anticipation / follow-through / overshoot | Expressive motion vocabulary; rarely useful on frequent utility actions |
| Progressive disclosure | Reveal detail when needed without losing the task's context |
| Hysteresis / hover intent | Remember recent intent to avoid twitchy open/close or repeated delays |
| Optical alignment | Align perceived shapes/weight, not only their rectangular boxes |
| Scroll affordance | Fade, cut-off content or scrollbar signals that more is available |

For galleries, use stable item identity, keep shared-layout IDs unique within each simultaneous
state, preserve crop/aspect ratio and return focus to the
originating thumbnail; handle unloaded images and reverse navigation. For slides or step-based
interfaces, morph persistent objects and crossfade new content rather than sliding everything.
In presentation tools, Morph is the analogous transition; support depends on the tool/version.
Neither slides nor gallery morphs should block skipping ahead or the reduced-motion path.

Terms and demonstrations: [Animations vocabulary](https://animations.dev/vocabulary),
[Jakub, Shared layout](https://jakub.kr/work/shared-layout-animations),
[Rauno, Fluid Morphing](https://rauno.me/craft/interaction-design).
Use these names to specify purpose and behavior, not to demand every effect in a screen.
