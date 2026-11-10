---
title: "I'm not very happy with the code quality and I think agents bloat abstractions, have poor code aesthetics, are"
author: "Andrej Karpathy (@karpathy)"
date: "2026-03-21"
url: "https://x.com/karpathy/status/2035173492447224237"
site: "x.com"
type: "post"
via: "fxtwitter"
---
I'm not very happy with the code quality and I think agents bloat abstractions, have poor code aesthetics, are very prone to copy pasting code blocks and it's a mess, but at this point I stopped fighting it too hard and just moved on. The agents do not listen to my instructions in the AGENTS.md files. E.g. just as one example, no matter how many times I say something like:

"Every line of code should do exactly one thing and use intermediate variables as a form of documentation"

They will still "multitask" and create complex constructs where one line of code calls 2 functions and then indexes an array with the result. I think in principle I could use hooks or slash commands to clean this up but at some point just a shrug is easier.

Yes I think LLM as a judge for soft rewards is in principle and long term slightly problematic (due to goodharting concerns), but in practice and for now I don't think we've picked the low hanging fruit yet here.
