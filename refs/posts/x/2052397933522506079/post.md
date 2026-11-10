---
title: "AI slop is good, actually. Slop is what enables fast parallel experimentation. The etiquette and skill is unde"
author: "Mitchell Hashimoto (@mitchellh)"
date: "2026-05-07"
url: "https://x.com/mitchellh/status/2052397933522506079"
site: "x.com"
type: "post"
via: "fxtwitter"
---
AI slop is good, actually. Slop is what enables fast parallel experimentation. The etiquette and skill is understanding the boundaries of where slop exists and the extent to which it should be cleaned up and how.

A few examples:

I’m working on the internals of some system right now. The API and GUI of this thing is fully zero shame slop. It’s horrible. But it lets me focus on the core quality while shipping a usable piece of alpha quality software to testers (transparent about the slop frontend). 

Similarly, this system has plugins. We sent agents in Ralph loops overnight to generate dozens of plugins. The plugins are slop. The quality is bad. The plugin API/SDK is absolutely not done.

But we can test a full GUI with a full plugin ecosystem. When we change the API, we can regenerate them all. The cost of change is just tokens, the velocity is incomparable to before.

I built Terraform. We tested and shipped TF 0.1 with about 3 very weak providers. Because we ran out of time. Building was slow. And when we changed our SDK the cost was immense. Totally different today, 10 years later. Today, I would’ve slop generated 100 providers (again, with transparency and cleanup later, but just to prove it out).

As an anti example, I would not PR this (without prior warning) to another project. I would not throw this onto customers without full review or transparency (as I’m already doing). I would not accept first pass slop. It’s almost never right. 

Slop is a tool. And like anything else it’s not blanket bad or good. The context is everything.
