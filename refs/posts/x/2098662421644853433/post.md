---
title: "How do you hold the bar on production agent code?:"
author: "Addy Osmani (@addyosmani)"
date: "2026-09-12"
url: "https://x.com/addyosmani/status/2098662421644853433"
site: "x.com"
type: "post"
via: "fxtwitter"
---
How do you hold the bar on production agent code?:

1. Agree on the outcome and the constraints first. 

What does "done" look like? what must it not touch? is the simpler design is to refactor or reuse what you already have? Then let Claude cook. You do not need a long planning ritual on the latest models. You do need to reject a bad change before it becomes a PR.

2. Give Claude a way to check its work. 

Put the exact build, test, and lint commands in there. Turn the things you reject in review into skills: /verify, e2e, schema checks and so on. Run those before you open the PR. Use /code-review. I've said that quality now lives in the constraints you put around your agents and think this is worth spending time on.

3. Your job is the design and the bar. 

Blast radius decides how much you read. Throwaway code with a small blast radius can be a black box. Production code should have a higher bar than if a human wrote it, especially anything that touches money, auth, or user data.

4. When Claude misses, don’t quietly fix it by hand. Have it write the lesson into CLAUDE.md or a skill. 

If it still misses, use the latest frontier model, turn effort to higher or have Claude pay down the debt and make the codebase easier to work in.

You can start with one check you already run today on every PR. The rest compounds from there.

> Quoting @bcherny: Hey ████,
> 
> I think there is room for both.
> 
> 1. Prototypes and other throw-away code can be treated as totally black box. If you’re going to throw it away anyway, and if the blast radius of it breaking is low, it doesn’t need to be perfect.
> 2. Production code written by Claude should have a higher bar than if it was written by a human. At Anthropic, we have many guardrails in place to make sure this is happening: lots of lint rules, lots of tests, Claude-driven end to end tests, Claude-powered fuzzers running daily, automated code reviews and security reviews, automated code refactoring, and so on. Without these, you can end up with a mess that is hard to maintain down the line. Luckily, the model makes it increasingly easy to do these well — run a few daily routines, use Claude Code Review, etc.
> 
> Your job is to hold the bar on code quality. If Claude’s code doesn’t meet the bar, try:
> - Using the latest frontier model (Opus 5 or Fable 5.1)
> - Increase effort to high or xhigh
> - Invest in your CLAUDE.md and skills to succinctly teach Claude how to work in your codebase
> 
> If all else fails, steer Claude more when you work with it, or have Claude fix accumulated debt and rewrite your codebase to make it easier to work with. Or, wait for the next model.
> 
> Best,
> Boris
