---
title: "--help on your CLI is all you need for LLM context until you don't."
author: "Geoffrey Huntley"
date: "2026-10-09"
url: "https://ghuntley.com/tier/"
site: "Geoffrey Huntley"
type: "article"
via: "direct"
---
# --help on your CLI is all you need for LLM context until you don't.

Here's something I've been meaning to write up for a while. It's kind of late, but I'm going to lean into the whole MCP vs. CLI argument because I have a perspective others might find interesting.

What's the actual difference between an MCP server and a regular old CLI program with a \`--help\` flag? Feels to me like a CLI program written with agents in mind solves the same problems without inventing anything new?

[https://x.com/adamwathan/status/1968738637358522629](https://x.com/adamwathan/status/1968738637358522629?ref=ghuntley.com)

Developer tooling companies can be sorted into two tiers: S-tier (winning) and F-tier (losing). The Rubik for wherever a company falls into the S tier or F tier has got everything to do with the model weights.

An S-tier company is in the training weights. Let's take GitHub, for example. Now, we can yak about problems with GitHub till the cow comes home, but one thing is true: these models know how to interface with GitHub because that behavior is in the model weights themselves. They don't need any skills or an MCP to get outcomes. You can just use the CLI.

You are S-tier once you can do a prompt like this without any skills or MCP:

prompt: Use the GH cli to create a repository, commit the changes, push to origin, set the reposistory to public and update the repository description.

Now, if you're a brand new developer tooling company and you're not in the model weights yet, you've got a couple of choices. First, you'll have to ask users to download and install some sort of skill pack, or maybe even a CLI, which adds a lot of friction for users compared with the DevX of an S-tier company.

So, what do you do? It's simple.

Start by developing a really good CLI, and on that CLI, work on and optimize your `--help` section. What you want to do is measure whether a model can achieve outcomes by walking the help verb across all the subverbs, then optimize the language used by choosing whatever works best, so the model can achieve the outcomes with the fewest tool calls. This can be automated through a loop or an auto-research loop.

Once you have this bare-bones foundation, the next step is to publish documentation for this CLI online and then focus on ASEO (Agentic Search Engine Optimization) for agents `web_search_tool`. Again, from this point forward, the goal is to look at the journey a single agent takes and optimize it so the agent can get all the information it needs in a single web search tool. If it has to walk through your documentation, you're not doing a good enough job. Keep optimizing.

To take this to the next level, you should enter into a business contract with the labs. Perhaps you've already got a contract with the labs for inferencing. You want to lean on them to include your CLI documentation in their next training run.

If you nail these things, then you're well on the path to becoming an S-tier developer tooling company. The best part is that it doesn't require users to download or install a skill pack, configure an MCP, or deal with any of that junk.

ps. socials
