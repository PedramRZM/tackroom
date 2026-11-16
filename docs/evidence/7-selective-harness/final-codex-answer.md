Read all three requested files. No files were edited and no hooks were run.

The actual repository skill directories under `.agents/skills/` are:

- `careful`
- `dream`
- `lock-tests`
- `second-opinion`
- `spec`
- `task`
- `verify`
- `wrap-up`
- `write-tests`

`.codex/skills` and `.claude` are absent. No `.claude` or `ui-craft` directory was found anywhere in the repository.

The guidance explicitly handles optional UI craft:

- [verify/SKILL.md](/tmp/tackroom-public-p57fbc0j/codex/.agents/skills/verify/SKILL.md) says to use `ui-craft` **if installed**. If absent, offer the optional UI profile and use the provided behavior, visual, accessibility, usability, and performance checks with existing project tools.
- [verification-tools.md](/tmp/tackroom-public-p57fbc0j/codex/.agents/skills/write-tests/references/verification-tools.md) likewise makes its `ui-craft` reference conditional and supplies fallback guidance. Its tool suggestions are candidates, not required dependencies.

[.codex/hooks.json](/tmp/tackroom-public-p57fbc0j/codex/.codex/hooks.json) is **readable configuration**, declaring:

- `PreToolUse`, matching `Bash|apply_patch`, invokes `.agents/hooks/guard.py`.
- `Stop` invokes `.agents/hooks/stop-check.py`.
- Its description claims hooks require review and trust before execution and after script changes.

Those declarations do **not establish runtime enforcement**: reading this file does not prove the runtime loads it, trust was granted, matchers cover current tools, or scripts execute successfully. None of that was tested. The verification reference also explicitly says workspace hooks are feedback, not tamper-proof independent enforcement.