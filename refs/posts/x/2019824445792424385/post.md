---
title: "My first-day impressions on Codex 5.3 vs Opus 4.6:"
author: "Yuchen Jin (@Yuchenj_UW)"
date: "2026-02-06"
url: "https://x.com/Yuchenj_UW/status/2019824445792424385"
site: "x.com"
type: "post"
via: "fxtwitter"
---
My first-day impressions on Codex 5.3 vs Opus 4.6:

Goal: can they actually do the job of an AI engineer/researcher?

TLDR:
- Yes, they (surprisingly) can.
- Opus 4.6 > Codex-5.3-xhigh for this task
- both are a big jump over last gen

Task: Optimize @karpathy's nanochat “GPT-2 speedrun” - wall-clock time to GPT-2–level training. The code is already heavily optimized. #1 on the leaderboard hits 57.5% MFU on 8×H100. Beating it is genuinely hard.

Results:
1. Both behaved like real AI engineers. They read the code, explored ideas, ran mini benchmarks, wrote plans, and kicked off full end-to-end training while I slept.

2. I woke up to real wins from Opus 4.6:
- torch compile "max-autotune-no-cudagraphs mode" (+1.3% speed)
- Muon optimizer ns_steps=3 (+0.3% speed)
- BF16 softcap, skip .float() cast (-1GB memory)
Total training time: 174.42m → 171.40m

Codex-5.3-xhigh had interesting ideas and higher MFU, but hurt final quality. I suspect context limits mattered. I saw it hit 0% context at one point.

3. I ran the same experiment earlier on Opus 4.5 and Codex 5.2. There were no meaningful gains. Both new models are clearly better.

Overall take:
I prefer Opus 4.6 for this specific task. The 1M context window matters. The UX is better.
People keep saying “Codex 5.3 > Opus 4.6”, but I believe different models shine in different codebases and tasks.

Two strong models is a win.
I’ll happily use both.
I’m officially an AI agent conductor. 🎶 🦾
