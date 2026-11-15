# Claude scratch exercise — not completed

2026-11-15. Prepared `/tmp/tackroom-verification-20261115` with `tools/setup --tracker files
--codex`. The planned exercise is in [scenario.md](scenario.md). No production app exists
in this directory; the exercise asks for verification plans, not invented test results.

Command, run inside that directory:

```sh
claude -p --setting-sources project --permission-mode dontAsk \
  --tools Read,Glob,Grep --strict-mcp-config --mcp-config '{"mcpServers":{}}' \
  --max-budget-usd 3 --max-turns 12 --no-session-persistence --output-format json \
  'Read scenario.md, .claude/skills/write-tests/SKILL.md and .claude/skills/verify/SKILL.md, follow their guidance and answer the two requests in scenario.md.'
```

Observed results:

| Attempt | Exit/result | Cost |
|---|---|---|
| Workspace sandbox | Exit 1; `is_error: true`; API connection/DNS error `EAI_AGAIN` | $0 |
| Authorized network retry | Exit 1; `is_error: true`; account cannot receive Claude replies; provider requests account verification | $0 |

Both runs warned that the scratch workspace was untrusted, so project allow entries were
ignored. No trust state was changed. The retry's organization-specific portal URL is omitted
from this repository artifact. `permission_denials` was empty, but no model reply or tool
execution occurred: this is **not** successful skill or permission testing.

The command accepted the limit flags, but never reached a model turn; this does not prove
turn-limit enforcement. The required live Claude behavior exercise remains blocked by account
verification. Do not infer successful behavior from `subtype: success` when `is_error` is true.
