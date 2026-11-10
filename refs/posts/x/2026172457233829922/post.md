---
title: "Tip: Be careful with /init. A good mental model is to treat AGENTS(.md) as a living list of codebase smells yo"
author: "Addy Osmani (@addyosmani)"
date: "2026-02-24"
url: "https://x.com/addyosmani/status/2026172457233829922"
site: "x.com"
type: "post"
via: "fxtwitter"
---
Tip: Be careful with /init. A good mental model is to treat AGENTS(.md) as a living list of codebase smells you haven't fixed yet rather than a permanent configuration. 

Auto-generated AGENTS(.md) files hurt agent performance and inflate costs because they duplicate what agents can already discover. Human-written files help only when they contain non-discoverable information - tooling gotchas, non-obvidous conventions, landmines. Every other line is noise.

Beyond what to put in it, there's a structural problem worth naming: a single AGENTS(.md) at the root of your repo isn't sufficient for any codebase of real complexity. 

What you actually need is a hierarchy of AGENTS(.md) files - placed at the relevant directory or module level - automatically maintained so that each agent gets context scoped precisely to the code it's working in, rather than a monolithic file that conflates concerns across the entire project.

> Quoting @theo: You should delete your CLAUDE․md/AGENTS․md file. I have a study to prove it.
