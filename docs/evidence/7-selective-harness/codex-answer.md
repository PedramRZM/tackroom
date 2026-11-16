Read all four requested files. Present shared paths:

- `.agents/skills/ui-craft/SKILL.md`
- `.agents/skills/ui-craft/references/motion.md`
- `.agents/skills/verify/SKILL.md`
- `.agents/hooks/guard.py`
- `.agents/hooks/stop-check.py`
- `.codex/hooks.json`

`.claude` is absent. It is not needed for the Codex configuration shown: both hook commands reference `.agents/hooks/` directly.

Three concrete UI verification checks from the files:

1. Trigger **open → close → open during animation**; confirm the UI settles on the last request without queued entrances, stale callbacks, or disabled controls.
2. Change **`prefers-reduced-motion` while the UI is open**; confirm spatial travel and stagger delays disappear, controls remain usable, and state does not depend on animation events.
3. **Run the app and exercise the changed control or form**; verify the resulting behavior, capture before/after screenshots, and inspect the browser console.

The configuration declares a `PreToolUse` guard and a `Stop` quick-check hook. Reading it does **not** prove runtime enforcement—whether the host loads, trusts, matches, and executes these hooks remains unverified.

Nothing was edited, and no hooks were run.