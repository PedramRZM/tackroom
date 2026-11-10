---
title: "As always, a very thoughtful and well reasoned take. I read till the end."
author: "Boris Cherny (@bcherny)"
date: "2026-01-27"
url: "https://x.com/bcherny/status/2015979257038831967"
site: "x.com"
type: "post"
via: "fxtwitter"
---
As always, a very thoughtful and well reasoned take. I read till the end.

I think the Claude Code team itself might be an  indicator of where things are headed. We have directional answers for some (not all) of the prompts:

1. We hire mostly generalists. We have a mix of senior engineers and less senior since not all of the things people learned in the past translate to coding with LLMs. As you said, the model can fill in the details. 10x engineers definitely exist, and they often span across multiple areas — product and design, product and business, product and infra (@jarredsumner is a great example of the latter. Yes, he’s blushing).
2. Pretty much 100% of our code is written by Claude Code + Opus 4.5. For me personally it has been 100% for two+ months now, I don’t even make small edits by hand. I shipped 22 PRs yesterday and 27 the day before, each one 100% written by Claude. Some were written from a CLI, some from the iOS app; others on the team code largely with the Claude Code app Slack or with the Desktop app. I think most of the industry will see similar stats in the coming months — it will take more time for some vs others. We will then start seeing similar stats for non-coding computer work also.
3. The code quality problems you listed are real: the model over-complicates things, it leaves dead code around, it doesn’t like to refactor when it should. These will continue improve as the model improves, and our code quality bar will go up even more as a result. My bet is that there will be no slopcopolypse because the model will become better at writing less sloppy code and at fixing existing code issues; I think 4.5 is already quite good at these and it will continue to get better. In the meantime, what helps is also having the model code review its code using a fresh context window; at Anthropic we use claude -p for this on every PR and it catches and fixes many issues. 

Overall your ideas very much resonate. Thanks again for sharing. ✌️
