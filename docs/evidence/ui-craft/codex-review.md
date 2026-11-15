Reviewed [fixture.html](/tmp/tackroom-ui-craft-portable-20261115/fixture.html) without editing it or running the page. I read the project’s ui-craft skill and its craft, motion and verification references, plus write-tests’ [tool reference](/tmp/tackroom-ui-craft-portable-20261115/.agents/skills/write-tests/references/verification-tools.md) and the verify skill. No packages were installed.

**Source findings**

| Location | Concrete defect or risk | Expected behavior |
|---|---|---|
| [Lines 15–17](/tmp/tackroom-ui-craft-portable-20261115/fixture.html:15) | `moving` discards menu activations for 600 ms. Rapid open→close leaves it open. | Every activation updates intent immediately; motion can reverse and settles to the latest request. |
| [Lines 4–11](/tmp/tackroom-ui-craft-portable-20261115/fixture.html:4) | Closing only clips the panel; Save remains keyboard-focusable. Menu lacks `aria-expanded`; no focus recovery is implemented. | Closed content is unavailable to focus and assistive technology; expanded state stays accurate. Closing while focus is inside returns it to Menu. |
| [Line 18](/tmp/tackroom-ui-craft-portable-20261115/fixture.html:18) | “Saved” appears before success. Neither HTTP errors nor rejected requests are handled; repeated activation sends more requests. | Show honest pending/success/failure states, preserve context, and offer retry without duplicate effects. If optimistic, visibly reconcile failure and prevent stale responses overwriting newer state. |
| [Lines 3, 10–11](/tmp/tackroom-ui-craft-portable-20261115/fixture.html:3) | Both text buttons have fixed 24 px dimensions despite longer labels, including “Saved.” | Labels fit, including zoom/localization; hit areas meet the project’s 44×44 CSS px house target and remain unobstructed. This is distinct from WCAG AA’s 24×24 minimum with exceptions. |
| [Lines 6, 12, 19](/tmp/tackroom-ui-craft-portable-20261115/fixture.html:12) | Image geometry is unreserved; the counter grows from two to three digits without a reserved slot or explicit tabular figures. | Loading, loaded and failed images retain their frame. Counter changes preserve surrounding positions; tabular figures alone do not reserve extra digits. Actual shifts require measurement. |
| [Lines 4–8](/tmp/tackroom-ui-craft-portable-20261115/fixture.html:4) | Broad `transition: all`, animated width, and an unconditional 800 ms spatial entrance; no reduced-motion path. | Use only purposeful, explicitly scoped motion—or instant changes. Reduced motion removes spatial travel while preserving functionality; state never waits for animation completion. |
| [Lines 1, 13](/tmp/tackroom-ui-craft-portable-20261115/fixture.html:1) | No mobile viewport metadata; “No items.” is permanent and provides no recovery or next step. | Use device-width layout. Empty content reflects the actual state and offers the relevant action. Whether this is first use, filtered results or a completed queue needs product context. |

**Compact verification plan**

Use the destination app’s existing runner and design primitives. Proposed browser sizes are 390 px and 1440 px, adjusted to supported devices. Exact application commands remain unverified because this fixture has no root application manifest or configured test runner.

| Smallest sufficient check | Examples and expected result | Evidence |
|---|---|---|
| Focused component/integration tests with controlled `/save` responses | Pending→success, HTTP failure, network rejection, double activation and retry satisfy the save behavior above. Test reordered responses only if concurrent attempts are supported. | Assertions on visible status, recovery and resulting saved state; confirm regression tests fail before the fix. |
| One focused browser interaction scenario | Rapid open→close→open **during motion**, then ten toggles; final intent wins. Tab cannot enter closed content; expanded state, keyboard activation and focus recovery work. Recheck Save after reopening. | Timestamped trace and assertions, plus console output. Use actual pointer input at stable coordinates; automation’s stability waits can otherwise conceal interruption bugs. |
| One deterministic layout/state pass | Hold/release/fail the image; exercise 9→10 and 99→100; test longest supported labels, zoom and text-spacing overrides. Image/counter geometry stays stable, labels remain readable, controls are reachable, and no unintended horizontal overflow appears. | Before/after rectangles and screenshots with fixed fonts/data/browser; check target edges for obstruction. Do not rely on CLS alone. |
| Accessibility and motion pass in the running app | Reduced motion before load and changed while open; all controls still work without spatial animation. Scan closed/open/error states with existing axe integration; manually check focus, zoom and status announcements. | Scan results and interaction observations. Screenshots are visual inspection unless compared with a reviewed baseline; automated scans do not establish full accessibility. |

For Tailwind v4, `motion-safe`/`motion-reduce` can express the motion policy, but hiding motion must also remove the JavaScript lockout. [Tailwind documentation](https://tailwindcss.com/docs/hover-focus-and-other-states#prefers-reduced-motion)

For lint, reuse existing types/lint first. Consider **`@shadcn/lint`**, an ESLint/Oxlint plugin supporting Tailwind v4 without requiring shadcn/ui, only where the destination design system needs token or component-policy enforcement. Start with applicable arbitrary-value/component-restyling rules; prove an approved semantic class passes and forbidden values/restyles fail. Invalid component variants belong in type checks. This adds configuration and exception-maintenance cost; it is not a universal `shadcn lint` command. [Official README](https://github.com/shadcn-ui/lint)

Plain CSS/`@apply`, imported values, unknown spreads and parent-selector styling require explicit coverage or documented gaps. If CSS remains, a narrow existing Stylelint policy can prohibit `transition: all`. Lint cannot prove target size, contrast, interruption or recovery. [Analysis limits](https://github.com/shadcn-ui/lint/blob/main/docs/how-it-works.md)

I ran only the project check entry point:

```text
no checks configured: edit scripts/agent/check
```

It exited **3**, so no types, lint or tests passed. After correction, run the configured full check and retain its output alongside browser evidence. Real-device edge taps, low-power performance and assistive-technology behavior remain unverified; browser emulation cannot establish them. User comprehension would require representative-user observation.