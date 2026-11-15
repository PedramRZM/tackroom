# UI craft in the harness

The owner wants small, coordinated details that make an interface responsive and deliberate.
The portable template lacked UI craft guidance even though the installed personal `ui-design`
skill had substantial coverage. Copying that whole skill would import unrelated house rules,
framework assumptions and considerable context. The new `ui-craft` skill keeps a short entry
point and loads craft, motion/vocabulary and verification references only when applicable.

The different name also avoids the known personal/project skill-name collision. No global
personal configuration was changed. Every `tools/setup` run now creates `.agents/skills/` links,
including the default and OpenCode-only paths. `--codex` only adds Codex-specific configuration.
The template's shared `AGENTS.md` points directly to UI craft for agents without skill discovery.
The links are also present in `template/.agents/skills/` itself, so copying the template with
symlinks preserved works without running the installer. Codex does not need a `.codex/skills/`
directory; `.codex/` holds its configuration, hooks and agent definitions.

## Every requested detail

The original list contains 22 distinct entries, with 19 repeated. These are applicability
criteria, not a demand to add every visual effect to every application.

| Original item | Implementation in `ui-craft/references/` | Proof to select |
|---|---|---|
| 1 Interruptible animation | `motion.md`: retargeting and last intent | Mid-motion reversal |
| 2 Layout stability / aspect ratio | `craft.md`: stable layout | Held image/font/data response, rectangle comparison |
| 3 Appropriate icons / stroke balance | `craft.md`: type, icons, color | Rendered icon/label inspection and accessible names |
| 4 Actionable empty states | `craft.md`: waiting and empty states | First use/no-results/all-clear/retry journeys |
| 5 Font-sensitive line height | `craft.md`: type roles | Real font/locale/wrapping and spacing overrides |
| 6 44 px touch targets | `craft.md`: touch policy, standards distinction | Actual hit regions and edge taps |
| 7 Restrained colors | `craft.md`: semantic palette budget | Role inventory and contrast/meaning review |
| 8 Skeleton loading | `craft.md`: predictable structure | Fast/slow/error swap geometry, no flicker |
| 9 Optimistic actions | `craft.md`: reconciliation and recovery | Rejection/reordering/retry and newer-state preservation |
| 10 Gorilla interaction tests | `verification.md`: stress versus guerrilla usability | Repeatable rapid sequence, final state and console |
| 11 Important items first in stagger | `motion.md`: choreography | First useful content immediate, bounded total, reading order |
| 12 Weak device, battery, reduced motion | `motion.md`: constrained devices | Preference emulation, controlled throttling, physical low-power test |
| 13 Tooltip delay then instant peers | `motion.md`: warmup/hysteresis | First/peer/reset timing and focus behavior |
| 14 Tabular numbers | `craft.md`: digits plus reserved width | 9→10 / 99→100 / localized values |
| 15 Horizontal/vertical scroll fades | `craft.md`: overflow affordance | Start/end/no-overflow, RTL and pointer behavior |
| 16 Safe polygons | `motion.md`: intent corridor | Diagonal path, flipped placement, deliberate exit |
| 17 shadcn lint | `verification.md`: official `@shadcn/lint` | Valid/invalid class policy fixtures in a compatible consuming app |
| 18 Morph for slides | `motion.md`: container continuity and slides | Skip/reverse/reduced motion; tool-specific support |
| 19a Shared gallery transitions | `motion.md`: shared identity/crop/focus | Open/back/interruption/missing image/multiple instances |
| 19b UI glossary | `motion.md`: vocabulary table | Choose a precise term and expected behavior in the brief |
| 20 Animation names / rubberband | `motion.md`: vocabulary and resistance | Boundary behavior, settling and purpose |
| 21 Icon-button crossfades | `motion.md`: contextual state changes | Fixed slot, rapid toggle, semantic state, no first-mount flourish |

## Placement and evidence

- **Skill:** non-obvious choices with scenario and failure mode. Conditional references keep
  always-loaded `AGENTS.md` to a single UI routing line. Source: harness principles 4/6 and Emil's
  *Agents with Taste*.
- **Existing verification:** `verify` points to the craft cases; `write-tests` lists the lint
  candidate. No duplicate plan or mandatory review agent. Source: principles 1/8 and the prior
  verification workflow. Browser assertions, static rules and taste review answer different questions.
- **Deterministic tooling:** adopt `@shadcn/lint` in Tailwind v4 projects, or the existing stack's
  equivalent. Pin/configure it and prove selected policies reject known-bad examples. It is
  not installed in this framework-neutral repository, and no new universal UI hook is justified.
- **Research maintenance:** practitioner indexes and the lint README join `tools/refs watch`.
  Reconsider guidance after actual project outcomes; high taste alignment earns attention,
  not immunity from contradiction or technical checks.

These placement choices are judgments grounded in [principles](principles.md),
[testing](testing.md) and the [research register](../refs/notes/2026-11-15-ui-craft.md).
That register links the saved sources, additional patterns, dates and extraction limitations.

## What would establish effectiveness

The current change establishes coverage, packaging and reviewability. It does not establish
better UX. Pilot on a real application: preselect defects and tasks, compare runs with/without
the skill, and record defects caught, false positives, verification time and token cost. Use
independent review and task outcomes rather than a self-awarded beauty score. Remove guidance
that adds ritual without improving results. Actual usability claims need representative users.

The [verification record](evidence/ui-craft/README.md) distinguishes repository checks, the
blocked Claude scratch trial, successful live Codex skill-read/review trial, OpenCode discovery,
independent scenario rehearsal and untested product behavior.
