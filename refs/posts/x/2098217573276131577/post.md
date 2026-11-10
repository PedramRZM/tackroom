---
title: "Hey ████,"
author: "Boris Cherny (@bcherny)"
date: "2026-09-11"
url: "https://x.com/bcherny/status/2098217573276131577"
site: "x.com"
type: "post"
via: "fxtwitter"
---
Hey ████,

I think there is room for both.

1. Prototypes and other throw-away code can be treated as totally black box. If you’re going to throw it away anyway, and if the blast radius of it breaking is low, it doesn’t need to be perfect.
2. Production code written by Claude should have a higher bar than if it was written by a human. At Anthropic, we have many guardrails in place to make sure this is happening: lots of lint rules, lots of tests, Claude-driven end to end tests, Claude-powered fuzzers running daily, automated code reviews and security reviews, automated code refactoring, and so on. Without these, you can end up with a mess that is hard to maintain down the line. Luckily, the model makes it increasingly easy to do these well — run a few daily routines, use Claude Code Review, etc.

Your job is to hold the bar on code quality. If Claude’s code doesn’t meet the bar, try:
- Using the latest frontier model (Opus 5 or Fable 5.1)
- Increase effort to high or xhigh
- Invest in your CLAUDE.md and skills to succinctly teach Claude how to work in your codebase

If all else fails, steer Claude more when you work with it, or have Claude fix accumulated debt and rewrite your codebase to make it easier to work with. Or, wait for the next model.

Best,
Boris
