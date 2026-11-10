---
title: "I've got an agent in a loop optimizing a renderer with the goal to minimize frame times (and tests to measure)"
author: "Mitchell Hashimoto (@mitchellh)"
date: "2026-05-28"
url: "https://x.com/mitchellh/status/2060088112257372610"
site: "x.com"
type: "post"
via: "fxtwitter"
---
I've got an agent in a loop optimizing a renderer with the goal to minimize frame times (and tests to measure). It got times down from 88ms to 2ms and allocations down from ~150K to 500. Sounds good, right? Wrong. This is exactly why agent psychosis is a big fucking problem.

As an experiment, I rewrote the Ghostty core render state in Go, with access to identically laid out data structures as Ghostty and the exact same validation tests. I made a purposely naive renderer (simple, correct, but slow). 88ms per frame with 150,000 allocations (horrendous, lol)!

I then kickstarted a Ralph loop to bring the frame times down. I told it it can't modify input data structures or the public API or tests (they're correct), but it can do anything else it wants. It got to work.

It has worked for about 4 hours. I've spent around $350 on this experiment so far. The results? 

88ms => 1.5ms
150K allocs => ~500 allocs

Incredible right? Nope.

My hand-written renderer I ported has frame times (same benchmark) of ~20us (0.020ms) and 0 allocations in the update path.

This is the problem with psychosis and lacking systems understanding. If you don't understand the system, you're going to accept that this is an incredible result. If you understand the system, you'll see better solutions immediately and can do roughly 75x better on throughput. 

The people who blindly trust agent output are in the former camp. They're sheeple, overdrinking from a fountain of mediocrity. 

Standard disclaimer: I use AI all the time. I like AI. The point I'm making is to not blindly accept results. Think. Analyze. Learn.
