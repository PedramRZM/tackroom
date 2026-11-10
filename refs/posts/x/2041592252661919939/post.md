---
title: "👋 Appreciate the feedback."
author: "Boris Cherny (@bcherny)"
date: "2026-04-07"
url: "https://x.com/bcherny/status/2041592252661919939"
site: "x.com"
type: "post"
via: "fxtwitter"
---
👋 Appreciate the feedback.

Since we introduced Claude Code at Anthropic, engineering velocity has increased hundreds of %, and the rate at which it is increasing is itself accelerating.

The velocity is very much not performative -- we're actively trying to figure out how to build effectively when all of the code is written by Claude. Claude has  accelerated the pace at which we ship, and as a result we've been hitting all sorts of new bottlenecks: code review and regression prevention, CI and merge queues, source control reliability, etc. We're working through each of these as they come up, and now have good answers for a number of them.

One of these bottlenecks is figuring out how to best communicate new features to our users. My pov is we need to be doing much better here. The problem isn't that we are releasing quickly, the problem is that we should design features in a way where you don't need to know about them to benefit from them. This is the case for much of what we build, and we need to make it the case for all of it.

To share how we think about it, there's a few ways to approach it from a product design pov:
- Make it so the model can do things for you (eg. enter plan mode, invoke skills, configure your settings)
- Generalize features rather than create new parallel features
- Make features opt-in until we do the above
- Have Claude monitor feature usage and brainstorm/build ways to improve usage while simplifying the system

We try to do all of the above, but as you said, it's not perfect yet, and this is something we're working through. If you prefer a lagging version, you can also use the Claude Code stable release (not latest). We're intentionally being open about what we're seeing, since our customers are seeing the same thing and at least part of our job is helping companies navigate this new way of doing engineering.

Re: source code leak -- it was unintentional, but was also human error. There was a subtle bug that missed several rounds of manual review. We're working on how we can better catch it automatically next time.
