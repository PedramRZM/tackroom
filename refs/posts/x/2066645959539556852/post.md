---
title: "My heuristic is that any diff an agent generates over ~1500 lines is too big and is indicative that the proble"
author: "Mitchell Hashimoto (@mitchellh)"
date: "2026-06-15"
url: "https://x.com/mitchellh/status/2066645959539556852"
site: "x.com"
type: "post"
via: "fxtwitter"
---
My heuristic is that any diff an agent generates over ~1500 lines is too big and is indicative that the problem needs to be decomposed. This is my general pattern now for feature work:

1. Try to implement the whole feature, loosely guided. I call this the "draw the owl" prompt in reference to the meme. Expect garbage, you're going to get garbage.

2. If the diff is less than 1500 lines, review it and iterate normally. If the diff is more than 1500 lines, prompt the agent to decompose the problem into atomic, incremental, reviewable tasks. Simultaneously, do this yourself.

3. Agents will very often make these tasks way too specific to the shape they solved. You need to massage it into the right general shape. Do that.

4. Kick off new agents to work on those incremental things (as parallelized as possible). Apply the same rules.

5. At a certain, point, repeat the "draw the owl" prompt. At some point, you will get beneath your review-ability threshold.

This has been producing consistently high quality, maintainable, reviewable chunks of code that have a good handoff to either merge as-is or human refinement.

And with the latest frontier models at xhigh thinking, these are all slow enough that you can usually have multiple going concurrently while you are actively reviewing others or working on your own tasks.

HITL (human-in-the-loop) agents are still super important, especially for feature work. Features touch the human boundary in terms of UI, API, etc. And net new stuff can introduce pathologies in the architecture that violate desired invariants (these should be represented in specs or tests but we aren't perfect!).

I know a lot of the leading edge agentic discourse is about "loops" and agents driving agents continuously. I do some of that (will report on that later). But, in terms of raw daily get-shit-done type of work, this is my most rewarding pattern at the moment.
