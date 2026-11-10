---
title: "Give your agent a way to verify its work. This can dramatically improve the quality of output."
author: "Addy Osmani (@addyosmani)"
date: "2026-10-17"
url: "https://x.com/addyosmani/status/2111604705340326393"
site: "x.com"
type: "post"
via: "fxtwitter"
---
Give your agent a way to verify its work. This can dramatically improve the quality of output.

With this process in place, Claude Code was able to write 90%+ of its code itself. When generating software at a faster rate than you can review it, the bottleneck shifts to proving that it works. @bcherny and team invested enough in verification, we've been able to move fast while maintaining stability.

Code reviews aren't going away, but you need to think of it differently. One human reading through line-by-line is no longer going to work as a gate, it needs to evolve into a multi-layered verification system, built with fast deterministic feedback loops for your agents. 

This is where e2e tests, feature maps (as @poteto has been advocating), property tests and multi-agent adversarial reviews come in. These all provide opportunities to catch errors early and fix them before things get out of hand.

You don't have enough eyeballs for the amount of code being written so your focus needs to be on product intent, risk assessment and evaluating evidence rather than reviewing code. Delegate the code checking work to your automated tests, scale your approvals based on risk, and turn your test failures into living evaluations. This approach helps maintain speed without losing reliability.

Let the agents do what they do best and let you focus on what makes you irreplaceable: judgement, direction, and ownership. We tried to capture how we handle code review and verification in this writeup. Hopefully it's helpful.

> Quoting @ClaudeDevs: Claude writes about 90% of Claude Code's code.
> 
> From June to September, merged PRs more than doubled while the share reverted fell by more than 40%.
> 
> We wrote about how we changed code review to get there, and how to adopt it:
> 
> https://claude.dev/blog/solving-code-review-at-anthropic/
