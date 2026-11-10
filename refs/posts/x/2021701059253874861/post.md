---
title: "9/ Set up hooks"
author: "Boris Cherny (@bcherny)"
date: "2026-02-11"
url: "https://x.com/bcherny/status/2021701059253874861"
site: "x.com"
type: "post"
via: "fxtwitter"
---
9/ Set up hooks

Hooks are a way to deterministically hook into Claude's lifecycle. Use them to:
- Automatically route permission requests to Slack or Opus
- Nudge Claude to keep going when it reaches the end of a turn (you can even kick off an agent or use a prompt to decide whether Claude should keep going)
- Pre-process or post-process tool calls, eg. to add your own logging

Ask Claude to add a hook to get started.

Learn more: https://code.claude.com/docs/en/hooks
