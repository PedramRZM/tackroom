---
title: "In Claude Code v2.1.30, we introduced /debug, a built-in skill for Claude to read your session's debug logs an"
author: "Dickson Tsai (@dickson_tsai)"
date: "2026-02-05"
url: "https://x.com/dickson_tsai/status/2019314348632555651"
site: "x.com"
type: "post"
via: "fxtwitter"
---
In Claude Code v2.1.30, we introduced /debug, a built-in skill for Claude to read your session's debug logs and troubleshoot your session. Great for chatting through issues like "/debug why didn't my hook trigger?" or "/debug why did my tool call fail?"

How did /debug come about? Last week, I was observing a group of users onboarding onto Claude Code. I saw that when something unexpected occurred, it wasn't easy for us to figure out the cause from the limited TUI display. Meanwhile, it was a chore to locate the logs. What if we simply gave Claude access to it from within the TUI? That way, it can use its tools to scan the logs and/or pull in the claude-code-guide subagent. The user can also /rewind when they're done debugging.

This feature is only as useful as what's in the debug logs. We're open to suggestions about what else we should add to them! Then, /debug should get better over time.
