---
title: "oh yeah i should have linked autoresearch probably"
author: "Andrej Karpathy (@karpathy)"
date: "2026-03-09"
url: "https://x.com/karpathy/status/2031137476438548874"
site: "x.com"
type: "post"
via: "fxtwitter"
---
oh yeah i should have linked autoresearch probably
https://github.com/karpathy/autoresearch
(you don't "use it" directly, it's just a recipe/idea - give it to your agent and apply to what you care about.)

and the tweet about it that went mini-viral over the weekend with more context
https://x.com/karpathy/status/2030371219518931079

> Quoting @karpathy: I packaged up the "autoresearch" project into a new self-contained minimal repo if people would like to play over the weekend. It's basically nanochat LLM training core stripped down to a single-GPU, one file version of ~630 lines of code, then:
> 
> - the human iterates on the prompt (.md)
> - the AI agent iterates on the training code (.py)
> 
> The goal is to engineer your agents to make the fastest research progress indefinitely and without any of your own involvement. In the image, every dot is a complete LLM training run that lasts exactly 5 minutes. The agent works in an autonomous loop on a git feature branch and accumulates git commits to the training script as it finds better settings (of lower validation loss by the end) of the neural network architecture, the optimizer, all the hyperparameters, etc. You can imagine comparing the research progress of different prompts, different agents, etc.
> 
> https://github.com/karpathy/autoresearch
> Part code, part sci-fi, and a pinch of psychosis :)
