---
title: "I tried to use it this way and basically failed, the models aren't at the level where they can productively it"
author: "Andrej Karpathy (@karpathy)"
date: "2026-02-06"
url: "https://x.com/karpathy/status/2019851952033771710"
site: "x.com"
type: "post"
via: "fxtwitter"
---
I tried to use it this way and basically failed, the models aren't at the level where they can productively iterate on nanochat in an open-ended way. (Though one of the primary motivations for me writing nanochat is that I'd very much love for it to be used this way as a benchmark for agents, and I'd love it if it worked over time). I'm open to this just being skill issue.

E.g. here some of the things I'd be suspicious about:
- the zoo of torch compile flags can knowingly be abused to get +1% gains but often at the cost of +30min compile time. This is why modded-nanogpt prohibits torch compile kwarg engineering and why I haven't done any in nanochat either. i wouldn't reliably expect the model to notice, consider, or flag this kind of an issue or seek clarification.
- ns_steps=3 might be a tiny bit of speed, but does the model also volunteer to make sure quality doesn't fall too much?
- same thing for deleting .float() cast - sure you can remove it and get VRAM/speed gains but it's there for a clear reason (extra precision in the loss function). Removing it means you absolutely have to make sure that the lower precision is ok validation loss wise, in a highly controlled experiment.

Overall I'm still struggling with getting the models to do significantly more basic things. For example, Opus keeps incorrectly "cleaning up" my comments when it doesn't understand them even when it's completely unrelated to the task, rude! It keeps violating and ignoring CLAUDE .md instructions on coding style but when I ask, it correctly points out all the violations. I know, I'm supposed to be using some kind of a /cleanup. Yesterday it gave me a table of results and incorrectly reported which experiment worked best (the table showed xyz=20 was best and it incorrectly claimed that xyz=12 was). Basically - much simpler things still fail routinely than something open-ended like "improve nanochat". (I've been doing a lot of YELLING IN UPPER CASE and I think this could actually be a really good metric for A/B testing instead of the inline survey thing.). Still incredibly net useful with oversight and with clear, well-scoped tasks.

I definitely haven't given up on automatic closed-loop experiments with the models. It would be so glorious. I had 2 iterations that basically didn't work but I have ideas for the 3rd.
