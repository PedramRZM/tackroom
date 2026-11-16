# Claude scratch exercise — not completed

Current scope, clarified by the owner on 2026-11-16: Claude model access is unavailable on this
machine. Portable setup work uses live Codex verification plus shared packaging/configuration
checks. The unsuccessful attempts below remain evidence of an unverified Claude runtime, not
a completion gate under the revised task. See [current evidence](multi-harness.md).

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

## 2026-11-16 retry

Revision: `9f88d9a` (`main`), resumed on `task/1-verification-claude-evidence`.
Created `/tmp/tackroom-verification-20261116-mLhEw1`, installed it with
`tools/setup /tmp/tackroom-verification-20261116-mLhEw1 --tracker files --codex` (exit 0),
copied the unchanged `scenario.md` above, and ran `git init -q` there. Repeated the command
above with `timeout 180` as an additional process bound. Repository baseline:
`scripts/agent/check` → all 11 checks passed.

Result: exit 1; `type: result`, `subtype: success`, `is_error: true`, `num_turns: 1`,
`total_cost_usd: 0`, `permission_denials: []`. The result says the account cannot receive
Claude replies and directs the owner to the Anthropic Verification Portal. The account-specific
URL is omitted. No model response or successful skill exercise occurred; the reported turn
count and empty denial list do not prove tool execution. AC6 remains incomplete.

Raw output is local at `/tmp/tackroom-verification-20261116-mLhEw1-result.json`;
stderr is at `/tmp/tackroom-verification-20261116-mLhEw1-stderr.txt`. No trust state or account
settings were changed. This retry did not run Codex, application browser tests, vendor
launchers against live endpoints or the comparative benchmark.
