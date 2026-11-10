---
title: "We do not have multi-agent systems today. Ultra mode is still one trained system delegating to itself."
author: "Ryan Lopopolo (@_lopopolo)"
date: "2026-09-24"
url: "https://x.com/_lopopolo/status/2103143806807728626"
site: "x.com"
type: "post"
via: "fxtwitter"
---
We do not have multi-agent systems today. Ultra mode is still one trained system delegating to itself.

What comes next has not been invented yet. https://x.com/i/article/2103139600067657728

## Article: Beyond Delegation: The Agent as Tool


Half-baked thought I’ve been chewing on: basically no “true” multi-agent systems have gotten traction. The stuff that actually works at scale today—Claude ultracode, Astra/Sol ultra, etc.—is really subagent delegation internal to a single harness, and I suspect a big part of why it works is that the behavior is inside the training loop.

I don’t really think of that as multi-agent. If an agent is a parameterized program over capabilities, those systems are still basically one program—more like green threads/cooperative multitasking inside a process.

Separately, I’m at least a medium-term believer that RL is not, in fact, all you need. There’s still a ton of juice in applied AI from building agents that are much more capable in a named domain than a general model + harness can be.

The interesting consequence is that those domain agents can themselves become tools. I’m shipping an agent; I’m going to package that agent as a tool and let Claude/Codex/etc collaborate with it. Coding agents already rationally reach for capable tools, and right now the most capable tools happen to be other coding agents.

I have no idea exactly what emerges from this. My agent can ask the caller questions, we can do bidirectional context sharing/distillation, etc., while the thing on the other end remains a black box from the model lab’s perspective.

We don’t really have the higher-order primitives for this yet. “Set up a bidirectional stream between two agents built by different people, with useful semantics for delegation, steering, context exchange, and eventually training” is not a normal thing you can do today. MCP feels more like the syscall layer than the answer. We’re missing the equivalent of mach ports/XPC/process spawning for agents.

In the fullness of time I don’t think any one lab closes over the whole system. We’re going to need ways for models to learn to delegate to and interoperate with agents their own post-training teams cannot directly modify as part of hill climbing. That feels like a pretty important platform surface to go invent.
