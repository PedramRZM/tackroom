---
title: "On DeepWiki and increasing malleability of software."
author: "Andrej Karpathy (@karpathy)"
date: "2026-02-11"
url: "https://x.com/karpathy/status/2021633574089416993"
site: "x.com"
type: "post"
via: "fxtwitter"
---
On DeepWiki and increasing malleability of software.

This starts as partially a post on appreciation to DeepWiki, which I routinely find very useful and I think more people would find useful to know about. I went through a few iterations of use:

Their first feature was that it auto-builds wiki pages for github repos (e.g. nanochat here) with quick Q&A:
https://deepwiki.com/karpathy/nanochat
Just swap "github" to "deepwiki" in the URL for any repo and you can instantly Q&A against it. For example, yesterday I was curious about "how does torchao implement fp8 training?". I find that in *many* cases, library docs can be spotty and outdated and bad, but directly asking questions to the code via DeepWiki works very well. The code is the source of truth and LLMs are increasingly able to understand it.

But then I realized that in many cases it's even a lot more powerful not being the direct (human) consumer of this information/functionality, but giving your agent access to DeepWiki via MCP. So e.g. yesterday I faced some annoyances with using torchao library for fp8 training and I had the suspicion that the whole thing really shouldn't be that complicated (wait shouldn't this be a Function like Linear except with a few extra casts and 3 calls to torch._scaled_mm?) so I tried:

"Use DeepWiki MCP and Github CLI to look at how torchao implements fp8 training. Is it possible to 'rip out' the functionality? Implement nanochat/fp8.py that has identical API but is fully self-contained"

Claude went off for 5 minutes and came back with 150 lines of clean code that worked out of the box, with tests proving equivalent results, which allowed me to delete torchao as repo dependency, and for some reason I still don't fully understand (I think it has to do with internals of torch compile) - this simple version runs 3% faster. The agent also found a lot of tiny implementation details that actually do matter, that I may have naively missed otherwise and that would have been very hard for maintainers to keep docs about. Tricks around numerics, dtypes, autocast, meta device, torch compile interactions so I learned a lot from the process too. So this is now the default fp8 training implementation for nanochat
https://github.com/karpathy/nanochat/commit/e569b59f92aea06bf8fc1c48489b3cc2e57189f4

Anyway TLDR I find this combo of DeepWiki MCP + GitHub CLI is quite powerful to "rip out" any specific functionality from any github repo and target it for the very specific use case that you have in mind, and it actually kind of works now in some cases. Maybe you don't download, configure and take dependency on a giant monolithic library, maybe you point your agent at it and rip out the exact part you need. Maybe this informs how we write software more generally to actively encourage this workflow - e.g. building more "bacterial code", code that is less tangled, more self-contained, more dependency-free, more stateless, much easier to rip out from the repo (https://x.com/karpathy/status/1941616674094170287) 
There's obvious downsides and risks to this, but it is fundamentally a new option that was not possible or economical before (it would have cost too much time) but now with agents, it is. Software might become a lot more fluid and malleable. "Libraries are over, LLMs are the new compiler" :). And does your project really need its 100MB of dependencies?

> Quoting @karpathy: How to build a thriving open source community by writing code like bacteria do 🦠. Bacterial code (genomes) are:
> 
> - small (each line of code costs energy)
> - modular (organized into groups of swappable operons)
> - self-contained (easily "copy paste-able" via horizontal gene transfer)
> 
> If chunks of code are small, modular, self-contained and trivial to copy-and-paste, the community can thrive via horizontal gene transfer. For any function (gene) or class (operon) that you write: can you imagine someone going "yoink" without knowing the rest of your code or having to import anything new, to gain a benefit? Could your code be a trending GitHub gist?
> 
> This coding style guide has allowed bacteria to colonize every ecological nook from cold to hot to acidic or alkaline in the depths of the Earth and the vacuum of space, along with an insane diversity of carbon anabolism, energy metabolism, etc. It excels at rapid prototyping but... it can't build complex life. By comparison, the eukaryotic genome is a significantly larger, more complex, organized and coupled monorepo. Significantly less inventive but necessary for complex life - for building entire organs and coordinating their activity. With our advantage of intelligent design, it should possible to take advantage of both. Build a eukaryotic monorepo backbone if you have to, but maximize bacterial DNA.
