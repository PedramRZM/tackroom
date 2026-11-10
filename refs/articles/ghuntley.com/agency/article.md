---
title: "nobody should type code by hand anymore. here's what's left."
author: "Geoffrey Huntley"
date: "2026-10-13"
url: "https://ghuntley.com/agency/"
site: "Geoffrey Huntley"
type: "article"
via: "direct"
---
# nobody should type code by hand anymore. here's what's left.

Josh Wulf and I talked loop engineering for four episodes. The models stopped being the constraint a long time ago; what's left is vision, verification and agency. Delete your skill packs, put the whole system under test, and revisit everything that used to be hard.

Josh Wulf has been running a show called [Agentic Engineering](https://www.youtube.com/@AgenticEngineeringwithJoshWulf?ref=ghuntley.com), and he asked me on. Josh spent ten years at Red Hat, three years as a tech recruiter in Brisbane, and the last year sprinting down the same road I have, sounding a bit crazy to most people around him. We talked for about an hour and a half. He cut it into four parts, and they all dropped today.

Here's the gist of all four, written up properly and in order, with chapter links at the bottom if you want to jump to a specific part of the conversation.

There's no place in the world now for a software engineer who types code by hand.

## part 1: is coding over?

### nobody knows what happens next

Josh opened by calling me the LLM whisperer. I'll take it, but let's be clear: no one knows what the hell will happen. I'm a little bit older, I've worked in developer tooling for a long time, and I'm just a little better informed. That's it.

Here's the timeline. December 2024, I'm a tech lead at Canva. Everyone there loves JetBrains. I start using Cursor, start running my first loops by hand, and think, *"ooh, JetBrains and IDEs don't exist in the future."* You get used to being called a little bit crazy. JetBrains just [reported its first-ever net loss](https://ghuntley.com/kodak/). Sure, they've been investing, but in my circles, no one is typing code into an IDE anymore. If you hang around a group that still loves their IDEs, you're not hanging around a well-informed group.

In February last year I discovered filesystem-as-state, the first of the loops: the idea of autonomously building things. It spooked me. The first thing I did with it was publish the Z80 post.

Not enough people understood that post at the time. Take an existing application, clean-room it into specifications, then rebuild the software from those specifications, much like the way AMD's CPUs came out of Intel's. It's not legal in every jurisdiction, and you have to take the right approach. But did you see all the Photoshop clones that came out in the last week? That's just the Z80 idea, implemented.

A year and a half later, services and MCPs exist whose whole job is rebuilding existing software, and a couple of published papers cite it.

The idea underneath is infinite software. If you're selling software without infrastructure or some other lock-in, you're hosed. So the real question is: what is a moat in software now? What is investable in software now?

### the travelator

Then came *Dear Student*. ThePrimeagen covered it, the juniors started paying attention, and I ended up in SF, at the pub, at a couple of meetups, realizing I couldn't sit on Ralph any longer because someone else would write it up first. By November, Boris was talking about using Ralph and loops in Claude Code. January was the real inflection point: it crossed into the mainstream, and business leaders started to understand what was happening.

It still hasn't crossed into the dark matter developers, and that concerns me deeply. If you've been applying yourself and staying curious, you have a two-year head start on everyone else. You can't just pick up the latest model and be good at this. It takes theory of mind, and the more you apply yourself, the more you see what's possible, which makes you more ambitious, which makes you see more.

Josh's story fits that exactly. He tried autocomplete-style Copilot, thought it was rubbish, and turned it off. Then a friend who heads AI at a couple of companies told him their engineers were getting good results. The first thing Josh did was have it clone a Java testing framework into Node.js. It wasn't great, but it was maybe 80% as good as he was, and it never stopped. It doesn't need to eat or sleep, and it doesn't lose focus. So he figured out what the missing 20% was: completeness and verification, because the models would leave stubs and partial implementations. Do the 20% instead of the 100%, and you've got scale.

Same for me. I'm no maximal AI glazer. I explicitly distrust the tools. The difference is that I internalized two years ago that the line was coming, and I've been expanding what I think is possible ever since. The models from a year ago were already good enough to displace software developers, and they keep getting better. We don't get stubs anymore. It still comes down to the operator's skill.

The travelator of tech moves on, as it always has. My deepest concern is the people who haven't even stepped on it. They're not aware it's moving, and they're completely unaware that some people are sprinting on it.

And you know how the employment market works. "Five years of React experience required." They're going to put minimum years of AI experience on job ads. If you wait for the models to be perfect before you start, there'll be juniors who are cheaper than you, who have been playing with this substrate, with a whole portfolio of cool things and maybe a couple of conference talks. Same story as always. Josh, who wrote those mathematically impossible job ads as a recruiter, reckons he got two years of LLM experience into one by doing more hours every day and more days every week.

### managers, burnout and retirement projects

A couple of days ago I published the post I'd been putting off for five or six months. If you're an engineering manager and you're not creating time for your team to play with AI, you're setting them up to be replaced. It got 500,000 unique views in 24 hours.

You join a company to de-risk your life. If a company has banned AI outright, quit and don't join one like it. You trade time and skills for money, and you need skills that will be employable for you and your family. You could try to change the culture, but plenty of employers are already with the program and will likely pay you more.
