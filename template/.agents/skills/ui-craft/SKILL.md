---
name: ui-craft
description: Build or review UI details that make interactions stable, responsive and deliberate. Use for screens, loading and empty states, typography, icons, touch controls, menus, galleries and animation polish.
---

# UI craft

Start with the project's components, design tokens and supported devices. Reuse their behavior
before building another primitive. This skill carries craft decisions; `write-tests` and
`verify` carry the evidence workflow. It does not prescribe a visual brand or frontend stack.

## Apply to the changed surface

1. Identify the task people perform, its frequency, input methods and failure states. Read only
   the relevant reference sections below. Translate applicable details into examples in the
   existing verification plan, including the expected result and how to observe it.
2. Build stable loading, empty, error and long-content states alongside the successful state.
   Use the project's type, color, space and motion tokens; define missing roles centrally.
3. Implement the behavior before decoration. A fast repeat action must remain responsive
   during motion. Preserve context, focus and user input through pending and failed requests.
4. Exercise relevant cases from the verification reference in the running product. Record
   measured facts, interaction results and remaining taste questions separately. For a larger
   change, pass those criteria to the existing reviewer; a separate design agent is optional.

| Read when | Reference |
|---|---|
| Layout, fonts, icons, colors, loading, empty states, optimism | [Craft](references/craft.md) |
| Motion, tooltips, menus, gestures, reduced motion; naming an effect | [Motion and vocabulary](references/motion.md) |
| Planning checks or reviewing the finished surface; selecting UI lint | [Verification](references/verification.md) |

## Gotchas

- These are contextual techniques, not a requirement to put every effect on every screen.
  Use the applicable patterns; explain a deliberate exception in the existing task/plan.
- A skeleton does not fix latency, an icon does not replace a label, and animation does not
  make a frequent action better by itself. Measure the resulting interaction.
- Numeric defaults labelled house choices are starting tokens, not accessibility standards.
  Recheck typography and optical balance when the font, locale or icon family changes.
- Read current official documentation for the installed library version before using its APIs.
  Do not copy framework/version assumptions from examples in personal skills.
- A static pass cannot prove good UI. Do not report real-device, low-power or user testing
  when only browser emulation or an agent review ran.
