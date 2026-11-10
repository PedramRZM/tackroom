---
title: "4/ Use hooks to deterministically run logic as part of the agent lifecycle"
author: "Boris Cherny (@bcherny)"
date: "2026-03-30"
url: "https://x.com/bcherny/status/2038454343519932844"
site: "x.com"
type: "post"
via: "fxtwitter"
---
4/ Use hooks to deterministically run logic as part of the agent lifecycle

For example, use hooks to:
- Dynamically load in context each time you start Claude (SessionStart)
- Log every bash command the model runs (PreToolUse)
- Route permission prompts to WhatsApp for you to approve/deny (PermissionRequest)
- Poke Claude to keep going whenever it stops (Stop)

See https://code.claude.com/docs/en/hooks
