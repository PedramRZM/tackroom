---
title: "I feel this way most weeks tbh. Sometimes I start approaching a problem manually, and have to remind myself “c"
author: "Boris Cherny (@bcherny)"
date: "2025-12-26"
url: "https://x.com/bcherny/status/2004626064187031831"
site: "x.com"
type: "post"
via: "fxtwitter"
---
I feel this way most weeks tbh. Sometimes I start approaching a problem manually, and have to remind myself “claude can probably do this”. Recently we were debugging a memory leak in Claude Code, and I started approaching it the old fashioned way: connecting a profiler, using the app, pausing the profiler, manually looking through heap allocations. My coworker was looking at the same issue, and just asked Claude to make a heap dump, then read the dump to look for retained objects that probably shouldn’t be there; Claude 1-shotted it and put up a PR. The same thing happens most weeks.

In a way, newer coworkers and even new grads that don’t make all sorts of assumptions about what the model can and can’t do — legacy memories formed when using old models — are able to use the model most effectively. It takes significant mental work to re-adjust to what the model can do every month or two, as models continue to become better and better at coding and engineering.

The last month was my first month as an engineer that I didn’t open an IDE at all. Opus 4.5 wrote around 200 PRs, every single line. Software engineering is radically changing, and the hardest part even for early adopters and practitioners like us is to continue to re-adjust our expectations. And this is *still* just the beginning.
