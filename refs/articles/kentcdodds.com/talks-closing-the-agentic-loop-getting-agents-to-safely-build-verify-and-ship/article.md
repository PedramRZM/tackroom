---
title: "Closing the Agentic Loop: Getting Agents to Safely Build, Verify, and Ship by Kent C. Dodds"
date: "2014-01-30"
url: "https://kentcdodds.com/talks/closing-the-agentic-loop-getting-agents-to-safely-build-verify-and-ship"
site: "Kentcdodds"
type: "article"
via: "direct"
---
Mostly on [location](https://kcd.im/map), sometimes remote.

Search talks by topics

The Last Software Engineer

I'm not here to tell you software engineering is ending soon. Nobody can put a reliable date on that, and pretending otherwise is a distraction. But we also have to admit something humbling: a year ago, most of us would not have predicted coding agents would be this good. That should make us less confident about predicting what they'll be able to do one year, or five years, from now.

So let's use "The Last Software Engineer" as a thought exercise. If AI keeps taking over more of the implementation work, what remains most human and valuable for us to do? In this talk, we'll take one step back from the hypothetical end and focus on the durable skill that has always separated great engineers from merely productive ones: judgment.

The future belongs not to people who only know how to build, but to people who know what should be built. We'll talk about product engineering, accountability, trade-offs, constraints, evaluation, and how to keep making software worth having in an AI era.

Keywords

ai, product engineering, software development, career

Presentations

- 2026-11-17
- 2026-11-02
- 2026-09-24
- 2026-07-09
- 2026-07-06

Resources

I Built Your Personal Software Ecosystem

What if you had your own npm registry, your own GitHub, your own cron system, your own email address, and your own database? And what if your favorite AI assistant could build software with all of it on your behalf?

That's Kody: a personal assistant platform where every user gets a fully isolated software ecosystem. Your AI writes packages into your own git repos, publishes them to your personal package registry with real versioned imports, schedules your jobs, runs your long-lived services and workflows, receives email at your own address, and stores everything in storage only you can touch.

I built this entirely on Cloudflare, because Cloudflare is the only place it could be built. This is a technical deep dive into what happens when you take the newest parts of the developer platform to their limits: sandboxing AI-authored user code with Worker Loaders, per-user git hosting with Artifacts, modeling "one of everything per user" with namespaced Durable Objects, and composing D1, KV, R2, Vectorize, Queues, Workflows, and Email Routing into a true multi-tenant platform. If AI agents are going to build and run software for everyone, this is what the infrastructure underneath looks like. You can start building it today.

cloudflare, ai, architecture, assistant, agent, infrastructure

- 2026-11-16
- 2026-10-21
- 2026-09-17

Closing the Agentic Loop: Getting Agents to Safely Build, Verify, and Ship

Agents can write code. That's not the hard part anymore. The hard part is trusting what they ship. In this hands-on workshop, I'll show you the loop I run every day: agents safely build, verify, and deploy the outcomes I want, and that loop is hooked up to signal (my own ideas, user feedback, bug reports, and friction) so it keeps itself going. I haven't read 1% of the code in my product, and agents author and merge most of the PRs. That only works because of the system around them.

We'll start by running autopilot (`npx kcd-skills@latest autopilot`) on a real repo, yours if you want, and use the questions it asks to lay the foundation: invariants, decision records that say when it's OK to change them, a primitives catalog, and an AGENTS.md that's a router, not a novel. Then we'll get into verification. That means separate reviewer agents, PR templates that have you review systems instead of code, cloud agents with their own computers that show their work, and a control CLI your agents maintain for themselves. Finally, we'll limit the blast radius with feature flags, health checks, and backups you've actually restored, and wire up the loops that keep it all moving. Bring a laptop and a repo you own.

What you'll walk away with:

- An autopilot plan for your own repo, with each step your agents can take on next
- A primitives catalog and invariants your agents actually follow
- A PR template built around intent, one-way vs. two-way doors, and system diagrams, so you review systems instead of code
- A verification setup: an AI reviewer, agents that test the running app, and a control CLI they maintain
- A blast-radius checklist: flags with an owner, a metric, and a removal condition, health checks after deploy, and tested restores
- The loops that keep it going: bug reports, user feedback, friction, and nightly cleanup

ai, agent, mcp, workflows

- 2026-11-10
- 2026-11-02
- 2026-10-27
- 2026-10-19

You Own the Outcome: Product Engineering in the Age of AI

Agents are great at output: the code, the files, the diff. What they can't do for you is own the outcome, which is what that code actually does for the people using it. That's the work that's left for us, and I think it's the most valuable work there is.

In this live-coded Distillery talk (with Q&A), I'll show how I build product with agents as collaborators today: building shared understanding first, asking for options with trade-offs and one-way vs two-way doors, making the product calls myself, and letting gates and AI reviewers check the work instead of reading every diff. On stage I shipped a real Kody capability, `webhookSyntheticDispatch`, to production.

Given at Distillery's coworking space (Humboldt 1967, Palermo) with the React Buenos Aires community.

ai, live coding, product engineering

Thinking in Primitives: How to make your agents produce better results with looser specs

The tighter you have to specify, the worse or less findable your primitives are. A good playground lets you give a job, not a massive spec.

In this talk, I'll show what a primitive actually is, how to design ones agents can find and compose, and how to make sure they use them instead of inventing one-offs. We'll look at create / combine / delete / expand moves for shaping the playground, and why looser specs are the scoreboard that your system is designed for agents—not just a hope that prompting harder will fix missing building blocks.

ai, agent, primitives, workflows

Building with Remix 3

Remix 3 wakes Remix up in a completely new direction: a batteries-included, zero-dependency, bundler-free framework built around Web APIs, runtime-first design, and one cohesive `remix` package. In this live-coded talk, I'll use the current beta to build a real app and explore the full stack: serving requests, routing, data schemas, forms and file uploads, sessions, auth, storage, middleware, the CLI, testing, and UI.

Along the way, we'll talk about what it means for Remix 3 to avoid critical dependencies and static-analysis magic, and how model-first design changes framework APIs for humans and AI agents.

remix, web, full-stack, ai, live coding

- 2026-05-07

Build a Free Agent

Most AI assistants are still just chats with tool access. This talk shows a different approach: using MCP as a personal runtime. I'll walk through how Kody uses `search`, `execute`, and `open_generated_ui` to discover capabilities, run sandboxed workflows, manage and use memory, keep secrets out of prompts, and turn generated interfaces into reusable software.

The goal isn't a better model. It's making AI assistants portable, secure, and actually useful across MCP hosts. In this talk, you'll learn that with the right primitives, you can create a highly capable assistant without paying an extra cent for inference.

ai, mcp, assistant, agent, security

- 2026-04-20

How I Build Web Applications in 2026

I've never had so much fun developing software than I have in the last few months. And I'm going to show you why. In this talk, I'll share my favorite workflows for building a web application using AI with modern tools. By the end of the experience, we'll have a real-world application that we built using AI along with deep full-stack web expertise. And you'll leave with ideas of ways to integrate your web expertise with the power of AI to build excellent user experiences for the web.

ai, cursor, web development, full-stack, workflows

- 2026-02-05

React Router's take on RSC

React Server Components have changed how we think about building React applications. In this lightning talk, Kent will explore how React Router is embracing RSC and what this means for the future of routing in React applications. This talk will dive into how RSC has simplified React Router's architecture and enables powerful new patterns for data loading, streaming, and code splitting.

We'll see how React Router has evolved to work seamlessly with React Server Components, making it easier than ever to build full-stack React applications with excellent performance and developer experience.

react, react router, rsc, server components, lightning

The New User Interaction Model

We are entering a new era of user interaction. It's being built right before our very eyes and changing rapidly. As crazy as it sounds, soon each one of us will get our own Jarvis capable of performing actually useful tasks for us with a completely different user interaction mechanism than we're used to.

But someone's gotta give Jarvis the tools to perform these tasks, and that's where we come in.

In this talk, Kent will show how this AI assistant user interaction model is shaping out to be, help us catch the vision of what this future could look like, and our role in it.

mcp, ai, keynote

- 2025-10-14
- 2025-06-11
- 2025-04-23
- 2025-04-03

Interactive MCP with React Router

Model Context Protocol is a powerful way to extend AI with context from the outside world, but right now the interaction with an AI is mostly text-based. Text is fine for answering simple questions, but when it comes to things like "help me find a good shirt for my kid's spider-man themed birthday party" or "get me directions to the nearest taco stand," we need much more. Clients like ChatGPT do have UIs for maps and things, but it's pretty limited and bespoke because it's built case-by-case by ChatGPT engineers.

As we extend the model with more context and capabilities via MCP, we can also extend it with a proper user interface using React Router and MCP UI getting the best of both worlds. A powerful agent + a great UI.

In this talk, Kent will demonstrate how to create an MCP server with React Router and expose great UI capabilities to the model. We're still early days for this, but the future is going to be awesome.

mcp, ai, agent, UI, React Router

Please Make Jarvis (so I don't have to)

The advent of AI signals a "Post-Browser Era," where intelligent "Jarvis clients" will supersede traditional browsers, interacting with a vast network of MCP (Model Context Protocol) services. While MCP provides a standardized communication layer, realizing the true "Jarvis experience"—an AI that understands, anticipates, and acts seamlessly across all facets of our lives—requires building the sophisticated client itself.

This talk moves beyond MCP infrastructure to define the characteristics of a true Jarvis, illustrate its potential through compelling use-cases, and identify the key challenges. It's a call to action for developers and visionaries to construct this pivotal AI interface, bridging the gap between powerful MCP services and the end-user dream.

mcp, ai, agent

Principles-Based Programming

Programming is often thought of as a purely technical endeavor—writing code to solve specific problems. But what if there's a deeper, more meaningful way to approach it? Principles-Based Programming explores the foundational philosophies that guide our decisions as developers. Using The Epic Programming Principles as a starting point, this talk dives into what principles are, why they matter, and how embracing them can transform the way you think about and write code.

Attendees will leave with an understanding of how principles provide a compass for navigating the complexities of software development. They'll be inspired to not only consider the principles shared but also craft their own to guide their personal or team development processes.

principles, life, career

Of Things Epic

Let's talk about how things are going in the world of Epic Web and the Epic Stack.

react, epic web, epic stack

Building Modern Web Apps with Epic Stack

Learn about what the Epic Stack is, and how to use it to build modern web apps.

react, remix, epic stack

Abracadabra: The Vanishing Network

The network that stands between our server and the client is what causes the most complexity in our development process. Whether it be the initial UI we generate on the server, the API calls we make as the user navigates around, or the form submissions our user makes, keeping the application responsive and up-to-date is a massive chore.

What would it be like if all of that complexity just disappeared? Freaking great, that's what it would be like. And React Server Components and Actions are what's making that possible. In this talk we'll look into how that's happening and how we can take advantage of this amazing developer experience to deliver even better user experiences.

keynote, react

- 2024-11-20

And Now You Understand React Server Components

You want to keep up with the future of React. React has evolved over the years and continues to push the component model further and further. Out of all the evolutions of React, server components are certainly the biggest advancement. It expands the component model further than ever before and as a result, requires some rethinking. Seasoned React developers need to unlearn the way we used to do things to be able to understand the improvements that React Server Components offer.

In this talk, Kent will guide you through React Server Components start to finish so you can understand how React Server Components work and set you off on your journey into the future of components everywhere!

web

- 2024-09-13
- 2024-06-14
- 2024-06-14

How to be an Epic Web Dev

In this Keynote, Kent C. Dodds will share key takeaways from his life experience that enabled him to have an extraordinary industry impact and success. You do not want to miss these key insights. Prepare to take notes and find ways to apply his life lessons to your own life.

keynote, personal

Stop Lying to your Users

Chances are your app is lying to your users. I know you don't mean it. Building truthful apps is hard. But you've been lied to by so many other apps you use and it is extremely frustrating. This frustration not only makes everyone's day worse, but it also makes users get out of that app as quickly as possible which for most apps is bad for the bottom line.

So what's the lie? Well you'll have to come to the talk to find out! Don't worry though, I'll not only explain to you what the lie is, but I'll also show you how to correct it and delight your users in a way that moves the needle.

meetup, web, performance

- 2024-02-21

Making Felix Felicis

Bring your wand and potions ingredients, because we're going to make liquid luck! In my career, I've worked extremely hard, but I've also experienced a lot of what some might call "luck." Some of what I've done is reproducible, and some of it is not. But I've learned a lot about how to increase my "luck surface area" and then make the most of the opportunities that come my way. In this talk, I'll share the ingredients I've used to make my own luck, and I hope it can help you make yours. Don't forget to bring your spell book!

keynote, career

- BYU Guest Lecture2024-04-15
- 2023-05-27

What Makes the Web Epic

The web is a special platform. It's different from anything else you can build on as a result of its openness and freedom from a central authority. It's about collaboration and cooperation. As a result, there's a degree of freedom we have on the web despite its weaknesses.

In this talk, I want to explain why you should double-down your investment in web technologies in your own career and company offerings. If you do, we can keep the web epic for many years to come.

keynote, web

The Epic Stack

Modern web development is fantastic. There are so many great tools available!

Modern web development is exhausting. There are so many great tools available!

Each of these sentiments is true. What's great is that most of the time, it's hard to make a choice that is wrong. Seriously. The trade-offs of most of the frameworks and tools you could use to build your application fit within the constraints of the vast majority of apps.

Despite this, engineers consistently struggle with analysis paralysis.

Let's talk about this, and a solution I am working on for it.

keynote, web, remix

Caching for Cash 🤑

It's often said that the two hardest problems in programming are caching, naming things, and off by one errors. Some degree of caching is required in almost every application to drastically improve performance. Unfortunately, not only is it easy to get wrong, there are also lots of different layers and methods to implement caching with different trade-offs.

In this talk, Kent will explain the key principles of caching. We'll go through several real world examples of issues where caching is a great solution. We'll also explore different approaches and their associated trade-offs. We'll cover a ton of ground here. This one's gonna be fun!

caching, remix, web

React Router + Vite is a framework

I once [posted](https://x.com/kentcdodds/status/1678762503420153857): "React Router + Vite is a framework". In this talk I'll explain what I mean. We'll talk about a couple different ways you can define "framework" and where the "React Router + Vite" combo fits in complete with an example you can poke around at.

react, vite, react router

The Web's Next Transition

The web. What started as a document sharing platform has evolved into an application platform. The web has been through a number of transformations over the years. From static HTML files to dynamic server-generated HTML responses. Then to REST or GraphQL APIs consumed by JavaScript-heavy clients with the Jamstack. The web is entering a completely new transformation. Modern infrastructure and techniques have changed the rules of what it means to make an excellent user experience. In this new future, what's old is new and what's modern is lacking.

In this keynote, Kent C. Dodds will show you how this transformation will impact your user experience, your development productivity, and your business goals. The future of the web is distributed. It's faster. It's cheaper. It's exciting. Kent will show you what you can do to stay in front of it (and no, it's not web3).

keynote, remix, web

- 2023-03-27
- 2022-11-17
- 2022-10-28

Bringing Back Progressive Enhancement

One fun (sometimes frustrating) part of the web is that your application must run on countless variations of devices with different configurations, screen sizes, and capabilities. Over the years, technology has improved and we've been given some really awesome APIs to *enhance* our applications to make them more useful despite the uniquely challenging (and awesome) distribution mechanism of the web.

Unfortunately, when we use these new features of the web platform to *enable* our application, we limit our application's usefulness to the trade-offs of those features which has surprisingly negative impacts (even if the device itself supports those features).

In this talk, we're going to learn the true scope of Progressive Enhancement and what can be gained by using tools and techniques that allow features of the web to *enhance* your user's experience rather than *enable* it.

keynote, remix, react, html, progressive enhancement

Full Stack Components

Remix is a web framework that gives you the simple mental model of a Multi-Page App (MPA) but the power and capabilities of a Single-Page App (SPA). One of the big challenges of SPAs is network management resulting in a great deal of indirection and buggy code. This is especially noticeable in application state which Remix completely eliminates, but it's also an issue in individual components that communicate with a single-purpose backend endpoint (like a combobox search for example).

In this talk, Kent will demonstrate how Remix enables you to build complex UI components that are connected to a backend in the simplest and most powerful way you've ever seen. Leaving you time to chill with your family or whatever else you do for fun 😎.

remix

Building Excellent User Experiences with Remix

Remix is a Web Framework that uses the web platform to enable you to build excellent user experiences. In this talk I'm going to show you what makes Remix so special and how the user experiences you build with Remix are excellent by default.

react, remix

- Cox Communications Meetup2022-08-17
- Code for Ukraine Tech Beetup #32022-04-13
- Tesla Frontend Meetup2022-04-01
- 2022-03-31
- 2022-03-31
- Austin Software Tech Talk2022-03-23
- 2022-03-17
- Farfetch Webinar2022-03-04
- Remix Uppsala2022-03-01
- 2022-02-18
- 2022-01-19

AHA Testing 💡

There's a spectrum of abstraction and tests are no less important to consider your abstractions than anything else. In this quick talk, we'll look at what it takes to make sure you avoid hasty abstractions (AHA!).

lightning, testing

Server-side Auth with Remix, Prisma, and the Web Platform

In this talk, we'll get a live coded demo of building custom hand-rolled authentication. When you have the right tools (and we do), authentication can be quite simple and secure. This is more (and better) than just: "Install this library and you're good to go." When we're done we'll have our own auth code that can evolve with our ever-changing requirements without a need to learn some library-specific APIs. We'll be leveraging the Web Platform the way it was meant to be done to give us simple and secure server-side authentication for the web.

keynote, remix, prisma

Stream Away the Wait

When implementing the design of a user interface, we often finish before remembering that not everyone's running the app's services locally on their device. There's going to be network latency, long running database queries, and large datasets that can slow down the experience. We can and should do everything we can to speed things up, but not all of this is within our control. This means we need to start thinking about pending states. But pending UI is terrible.

In this talk, Kent will walk us through building a pending experience that is quite delightful. Ultimately taking advantage of React 18's new streaming APIs and a soon-to-be-released API in Remix to give a top-notch user and developer experience. Prepare to have your mind blown.

keynote, remix

Shipping to the Edge

The landscape of the web has evolved drastically since the first website was published to the World Wide Web in 1991. Over the years, the pendulum has swung from servers rendering HTML to JavaScript-heavy clients and now it's swinging toward something more in the middle.

What about the web today is enabling us to overcome the shortcomings of the web of the past? In this talk, we'll get a little peak into the history of each of these stages of the web and what that means for anyone building on the web platform in the future.

keynote

The Stack of the Future

When a brilliant idea strikes, you want to hit the ground running and focus on building out your idea. Unfortunately, for any ambitious project, it takes a significant amount of time configuring the tools you'll ultimately need to make your idea a reality. Far too often we either under prepare and our MVP-shortcuts end up being a pain in the neck for the next few years if we're successful, or we spend so much time in the setup process that we lose all motivation.

In this talk, I'll show you how Remix can help you get started with a solid foundation so you can focus on building out your ideas. And when your MVP turns into a money maker, you won't feel like you have to rewrite your app from scratch! And for those of you starting new projects from scratch on a regular basis, I'll show you how you can make your own Remix stack to create these projects just like you want them again and again.

Developing a Remix app... Offline

I love riding my onewheel up to the mountains where there's no internet/cell service and working on my app. But my app uses tons of 3rd party services and two databases to get things done. In this talk I'll walk you through how I manage to still work offline and enjoy nature!

react, msw, docker

The Power of Forms

The web has been able to do mutations for a really long time and we've been `preventDefault`-ing in our JavaScript SPAs. But if you build your backend to support both the `fetch`-submit type of form submission as well as the default behavior, then you can make your app work without JavaScript or before the JavaScript has finished loading! Let's explore how Remix makes this possible.

Remix and Progressive Enhancement

We like to talk about how Remix sites work well without JavaScript in the browser, but there's gotta be a reason to ship some JavaScript right? In this talk, I'll show you the amazing things you can do once you have JavaScript on the client. Progressive enhancement FTW!

Super Simple Start to Remix

Remix has me more excited about building better websites than anything else since I started using React back in 2015. I have so much to say about it, but for this blog post, we're going to remove as many distractions as possible and give remix the "super simple start" treatment. So, even though Remix has a fancy npm init remix thing you can run (which is much easier than what I'm going to show you), we're going to skip that and build a simple remix app from absolutely nothing to running so we can inspect each bit required to get it going.

Don't Solve Problems, Eliminate Them

Humans are natural problem solvers and we're good enough at it that we've survived over the centuries and become the dominant species of the planet. Because we're so good at it, we sometimes become problem seekers too–looking for problems we can solve. Those who most successfully accomplish their goals are the problem eliminators. Let's talk about the distinction between solving and eliminating problems with examples from inside and outside the coding world.

keynote, career, software

How I Built a Modern Website in 2021

I just released a complete rewrite of my website. This isn't your regular developer blog though. You can actually log in, record some audio for a podcast, choose a "team" to be a part of, connect with discord, and much more. I'm using some of the coolest modern tech around including React, Remix, Prisma, Postgres, Redis, Fly.io, tailwind, TypeScript, and more!

I want to take you on a tour of some of the highlights and talk about some of the problems I faced and decisions I had to make while building a brand new modern website in 2021.

Practically Testing

This talk is about how testing uses the same currency as everything else we do for the product: our time. And we need to decide how much time we invest relative to the ROI of everything else we can do.

testing

Testing Library

This should be a fun one, as Kent C. Dodds ([@kentcdodds](https://x.com/kentcdodds)) is joining us to talk us about Testing Library, and to give us a live demo. You should bring fun questions, like, how did you come up with the name Testing Library? Maybe bring some real questions too, as Testing Library is a pretty powerful library you're probably using in production.

react, testing

Managing State Management

Application State Management is one of the hardest parts of building and maintaining React Applications. The number of options you have is numerous and the reason is that it's just such a hard problem with so many nuances and trade-offs. One thing that makes application state management harder is when we aren't thoughtful about how that state is organized and categorized in our app. There are different kinds of state and they require different approaches for management. When you try to treat all app state exactly the same is when problems come into play.

Let's talk about what some of those categories are and how we can drastically simplify our application code and improve our app's performance by thinking about and organizing our state differently.

react, state

Consume ➡️ Build ➡️ Teach

How do you level up? How do you jumpstart your learning when getting into something new? Nobody has more than 24 hours a day, so how do you maximize the impact of your limited time?

In this keynote, I'm going to tell you a bit of my own story, and some tips and tricks that I've learned so you can be as productive as you can be at learning new things and solidifying that knowledge so it's there when you need it.

career, keynote

Confident React

We want to make sure that when we ship new code, our users can use the application. The best way we've found to do that is to write automated tests that run before we deploy a new version of the app. But if our tests aren't doing exactly what the user will do, then how do we really know that things will work when users interact with our apps? Let's rethink what it means to ship applications with confidence and what it takes to get there. With improved tools and practices, we can be more certain that what we're shipping to our users will work the way it's intended.

- YYC Dev2020-09-15
- 2018-08-31

AHA Programming

Are you the kind of programmer who prefers to never see the same code in two places, or do you make liberal use of copy/paste? Many developers swear by the Don't Repeat Yourself (DRY) philosophy while others prefer to Write Everything Twice (WET). But which of these produces more maintainable codebases? I've seen both of these approaches lay waste to codebases and I have a new ideology I would like to propose to you: Avoid Hasty Abstractions (AHA). In this keynote, we'll talk about abstraction and how you can improve a codebase by applying and creating abstractions more thoughtfully as well as how to get yourself out of a mess of over or under-abstraction.

software development, abstraction, keynote

- 2019-10-16

Simply React

One of the things I love about React is how easy it is to encapsulate UI code into a component. I love this because it makes reuse of those components easy. But is it easy? I've made my fair share of components that had to accept a bunch of props to handle a growing list of different use cases resulting in a complex render function full of conditional statements and a confusing API for people using this "reusable" component. Eventually it becomes too much and I had to make a new version of the same component to handle slightly different use cases. Lots of code/bug duplication there because my reusable component wasn't reusable enough.

There are patterns that have emerged in React that allow you to promote code reuse without sacrificing the simplicity or flexibility of the component. In this talk we'll go over 5 of these patterns that will make your React components more useful.

react

- JS@PayPal (internal conference)2018-05-10

Why React Hooks

In October, the React team announced a new feature coming 🔜 to React called "hooks." In this talk we'll go over what this feature is and why this feature is necessary. We'll also see a real-world example of an application that uses React hooks.

- 2019-02-12
- 2019-01-26

Managing an Open Source Project

Awesome! You've made it big! You've published an open source project and people are actually using it to make the world a better place. Achievement unlocked! Great job! But wait... what's this? An issue? Oh, it's just a bug. Pretty quick and easy. Fixed, released, done, #likeaboss 😎. What's this? A PR? How cool! Wait... That's not quite right... Oh, a question! Cool! And another! And another... eh... and another... Uh oh... You think you've just sold your soul to this project.

You start an open source project to scratch your own itch and suddenly other people start using it and they need your help. This can easily start eating up your time big time and before you know it, your kids/dogs start feeling neglected.

I've had to deal with this in a few projects and I've learned a thing or two about work/life/oss balance. I have a few tricks that help you make the project manage itself a bit more while still being friendly and helpful to users of the project. Let's chat.

open source, soft skills

- 2019-09-20
- 2016-10-27
- 2016-05-14

- [video](https://youtu.be/jKI1Kj5VXqE) (practice run at a meetup)

Building the Open Source Community We Want

What kind of world do you want to live in? The world of Open Source Software is supremely vast, and it's growing. We can't sit idly by, coding alone in our closets with an attitude of "if you want something done right, you have to do it yourself." We don't want to live in a world like that. The community we want to build around OSS requires intentional effort to maximize the happiness of everyone involved. And the rewards of working toward that goal are serene. I'd like to personally welcome you to the open source community. Bring your distinctiveness and help to make our world a better place.

open source

Application State Management

For the last few years of using React, we as a community have been trying to solve the hard problem of application state management with React when we already had one all along. React itself is a state management library.

You can use features and practices that have been a part of React for a long time and it will change the way you think about state management for your React apps. In other words: you probably don't need Redux, MobX, or any state management library other than React. Let's explore how that's possible and why you might want to think twice before reaching for an abstraction.

- 2019-09-17

React Hook Pitfalls

The hooks honeymoon phase is over. We were able to overlook our confusion as a reasonable familiarity issue, but now it's time to get real about the pitfalls of React Hooks. Hooks lead to a better user experience and fewer bugs for sure, but without the right foundational understanding of them and certain JavaScript semantics, we'll probably cause other problems in the process of using hooks.

In this talk, we'll explore some of the gotchas of using hooks, why those things are problems, and how to think about hooks so we develop an intuition for how to use hooks while avoiding the pitfalls.

Testing Implementation Details

This is basically the talk version of my blog post [Testing Implementation Details](https://kcd.im/imp-deets).

testing, react

Requisite React

React  is a brilliant JavaScript library for building simple and complex user interfaces. In our eagerness to apply  React  to our most complex of problems and ship solutions today, we can get lost in the 🌲🌲🌲 forest of abstractions 🌲🌲🌲. When it comes to leveling up our skills in anything, I find the most effective method is to take a step back and understand the foundational fundamentals. To strip away all abstraction until what we're left with is the bare bones. [The better you understand an abstraction, the more effective you will be at using it.](https://x.com/kentcdodds/status/1074724545003581440) In this talk, we'll get more effective at using React Hooks, React Suspense, and JSX.

LIVE! Learn React Hooks with Kent C. Dodds

There's a lot of chatter about React Hooks. They really change the game, but they are also a totally new mind-bending approach in some cases. In this webinar, I'll go over what React Hooks are, why they're useful, and demo what you can do with them.

A Render Prop by Any Other Name

Can Vue use Render Props? Does React have a concept like Directives? Can Angular go Renderless the way the young 'uns do? All my developer friends in that other framework keep using words I don't understand. Help! Join Kent C. Dodds, Isaac Mann and Divya Sasidharan as they demonstrate UI component patterns that are common across React, Angular and Vue. Consider this your language primer before a trip to a foreign framework land. You'll see that we're all talking about the same concepts, even when we use different words.

react, vue, angular

React... Suspense...

React Suspense is coming and it's going to be awesome. It's currently in alpha and you can play around with it. In this talk we'll focus on the fundamentals of how React Suspense works.

The introduction to React you've been missing

In this talk I teach React from scratch in a single `index.html` file with no magic up my sleeves. We start with a basic Hello World in vanilla JavaScript and incrementally iterate through React APIs and JSX. We continue with introducing more of React's APIs.

react, jsx, intro

How to React

Learning React can be confusing. React is a library, but even more than that, React is an ecosystem of tools that you piece together to create a program. This is a powerful property of the React community, however that ecosystem can be frustratingly distracting when you're a newcomer trying to get your feet wet. The key to avoiding this frustration and confusion is to learn React (and its ecosystem) in the right order.

In this talk, we'll go over what that order is and give a roadmap so you can have a vision of where you're going. Let's learn how to React!

- 2018-06-08
- 2018-03-30

PayPal and Node Tooling

This is a keynote at JS@PayPal about how PayPal is investing in JavaScript, NodeJS, and tooling.

node, keynote

How open source has made me and the stuff I make better

The open source community and ecosystem have made me a better software developer and helped me develop better software. I get to see how other people work. Other people get to see how I work. It encourages me to put forth my best effort, think critically about the software I'm creating, and ensure it has great documentation. It's also easier to develop software in an isolated environment like an open source project.

In this talk, we'll see how open source can help improve your skills and improve the software that you create. This makes you a much more skilled, marketable, and gives you work that you can share with the public and contribute to the open source ecosystem.

How to Open Source Your Stuff

Building things so they work well in isolation, then piece them together to make the full application makes building applications easier. One thing that really helps with this kind of strategy is to open source your stuff. In this talk, we'll take a look at an existing application, identify a good candidate component for open sourcing, and then go through the process of creating an open source project for that component and add it as a project dependency. By the end that component of the application will be easier to work on and contribute to and we'll also have it open for the rest of the world to contribute and improve the software which once had bugs that were just as private as the original project repository.

open source, live coding

- 2018-04-13
- 2016-10-27
- JS@PayPal2015-12-16

Write tests. Not too many. Mostly integration.

Automated tests are an important part of raising your confidence when releasing software. They can speed you up or slow you down depending on how you write them and which form of testing you focus your test writing on.

In this talk, we'll cover the value of automated testing and where your efforts should be focused to strike the best balance of confidence and effort.

- 2017-11-21

All about macros with babel-plugin-macros 🎣

Customize babel without configuration or ejecting from create-react-app

babel

Writing custom Babel and ESLint plugins with ASTs

The Abstract Syntax Tree. It sounds a lot worse than it is. It's actually quite simple and enables some powerful tools. BabelJS uses it to transform your code from ES.Next to ES5. ESLint uses it to lint your code. And with a knowledge of how it works, you can extend these and other tools to do some mind bustingly powerful things. Prepare to be amazed by ASTs!

ECMAScript, babel, eslint, live coding

- 2016-06-23
- 2016-01-14

Maintainable CSS in React

I no longer care about: specificity, CSS linters, CSS preprocessors, vendor prefixing, removing unused CSS, finding CSS dependencies and dependents. I now care more about: whether it's fast enough, whether it's small enough, whether it's familiar enough. These are some of my trade-offs. Because I use CSS-in-JS. I've made trade-offs because I write HTML-in-JS. Despite these, I still do it, because the cost is minimal enough, and the benefit is great enough. Let's tell stories, talk use-cases, explore trade-offs, and inspire more innovation to make the CSS-in-JS trade-offs less trade-offy.

glamorous, css, css-in-js, react

Tools of modern JavaScript projects

The cry of JavaScript fatigue still echoes in the minds of developers everywhere as they try to wade through the waters of outdated blog posts, tutorials, Stack Overflow answers, and GitHub repos. Just when things seem to start settling in JavaScript, something new comes to shake things up a little bit. I'll be you tour guide as we navigate through the tooling set up of a modern JavaScript project that's leveraging these tools in a way that actually enhances the experience of users using the project and developers working on it.

javascript, tools

- 2017-07-13

Faster JavaScript

The more code you have, the more problems you have. One of these is the ability to learn the code. Code often has logic to handle edge cases which can distract a new contributor from the core logic of the code, making it challenging to learn. Another one of the problems with more code that's specific to JavaScript and the browser is the more you send over the wire to the browser, the slower it goes. This is due to network latency primarily, but also parsing, evaluating, and keeping relevant variables in memory.

With a really interesting technique called [program slicing](https://en.wikipedia.org/wiki/Program_slicing), we can build tools to help to mitigate some of these problems. In this talk, I'm going to give you a peek at a tool I've been working on called `slice-js` 🍕. I'm super excited about the implications for a project like this!

javascript, babel

Testing React

I hope you're excited about testing! We all know we need to get testing better, but it can be really hard to know how and what to test. We'll learn about the four inputs to React components (user input, props, data, and context) and how to test for each of them. You'll discover that if you slightly modify the way you're writing your components, you can make them much easier to test. We'll be using the new super fast, simple, and feature full Jest testing framework with enzyme and snapshot testing. I hope you like code. You're gonna see some here!

react, testing, live coding

- 2016-10-21
- JS@PayPal2016-09-23
- 2016-08-11

Zero to 60 in software development: How to jumpstart your career

Our industry has a problem. We have a "talent shortage," so we're loading the industry with new developers from various bootcamps, but they're having trouble finding jobs because many companies are unwilling to hire and train them. So these new developers are left to themselves to try and find ways to develop the skills they need to be "marketable."

I graduated from college in April 2014, just shy of two years ago. In that time, I've been able to learn a ton, build a bunch of stuff, teach workshops, create egghead screencasts, speak at conferences, and generally contribute quite a bit to the JavaScript community. In this talk, I'll cover some solid principles of things that I've learned in my experience. This will help new-comers to jumpstart their career. And help old-timers know how they can help new-comers.

soft skills

- [BYU AIS club](http://ais.byu.edu) Value Added Forum2016-10-13

More than you want to know about ES6 Modules

ES6 Modules have been standardized and many have already started using them. They have a lot of benefits over CommonJS, AMD, and Globals.

Unfortunately, there are many ways to deal with modules with this new syntax and it can be a bit confusing. In this talk, we'll explore the different ways you can use the new syntax and when you'd use the different methods. We'll also investigate what's going on at a high level. Buckle up for a firehose of ES6 information.

ES6, babel

- 2016-08-12
- [Modern Web Remote Meetup](https://www.bigmarker.com/modernweb/ES6-Modules-Mastering-Chrome-Developer-Tools-and-more) (video on the event page)2016-03-19

The First Pull Request

"Feel free to submit a pull request." For some, this is a welcome invitation, but for many developers, pull requests are intimidating, discouraging them from contributing to the community. Kent Dodds demonstrates how easy and fun it is to create a pull request as a first timer.

To open source newcomers: You, open source newcomer, can be a valuable contributor to the open source community. We need you here. We want your input and contributions. But getting over that initial hump of contributing can be a real challenge. I call this the first-timer's dilemma. You want to contribute, but you don't know how, or you're afraid your pull request (PR) won't get merged. You'll learn that it's less frightening and easier to get started than you think, as you become familiar with the common patterns and processes you need to understand in order to contribute to an open source project.

To open source project maintainers: You, open source project maintainer, are the lifeblood of the open source community. Developers power open source. The more people finding, reporting, and fixing bugs or adding/removing features the better. You have the power to help newcomers overcome the first-timer's dilemma. You'll see what challenges first-timers often face and how with just a few extra minutes of your time, you can help tear down these barriers and make your project more friendly to contributors (including first-timers).

Whether you'e new to open source or a pro, Kent will help you as we strive to make the open source community more open and friendly.

What we can learn about testing from the wheel

Knowing what and how to test is almost more difficult than actually writing the test. If you write only end-to-end tests, you'll struggle with reliability and speed. If you write only unit tests, you'll struggle with surprising bugs integrating things together. In this ignite talk, we'll take these concepts away from code for a moment to see how we would test a wheel. Prepare for an enlightening, entertaining 5 minutes 😀.

testing, lightning

Learning JavaScript and Staying Marketable

Angular is amazing and has contributed to a major change in the landscape of frontend web development forever. But frameworks come and go. Even though Angular 1.x will still be around for a few years, it will eventually be totally antiquated and you'll need to show off other kinds of skills to attract employers. What if there were a way that you could learn skills you need to both be effective Angular developers today and develop skills that will make you marketable for many more years to come? Spoiler, I'm talking about JavaScript. Let's go over why that's important and a few ways to accomplish this.

- 2015-11-24

JSON powered Forms

We're all really tired of writing the same code for every form. You need a label here and an input here and make sure their IDs are the same and unique and now you want me to add validation!? Daah! I got fed up with this pretty quick and found that I enjoy writing JavaScript a lot more than repeating myself with HTML. If you're like me, then you'll love angular-formly. In this talk, we'll see how you can very easily represent your model with a form using a few lines of JavaScript. You want validation, conditional fields, or custom templates? You need to react to changes to a field? Piece of cake. So come on, and let's make fields less painful and more delightful.

ES6, Webpack, Karma, and Code Coverage

Setting up test coverage reporting with ES6 and Karma

babel, testing, webpack, live coding

ES6

Kent C. Dodds is going to be introducing ECMAScript 6, which is the next version of JavaScript. If you want to look ahead, check this out: [github.com/lukehoban/es6features](https://github.com/lukehoban/es6features)

Angular 2: Built for Huge, Long-lasting Applications

Angular 2 is built for huge web applications that stand the test of time. To accomplish this, Angular 2 utilizes the latest and greatest web technologies like ES6 modules/classes and Web Components. Come get a preview of what this looks like with egghead.io instructor Kent C. Dodds as he live codes an application using the pre-release alpha version of Angular 2.

Moxee: Enforcing modularity in AngularJS

Moxee will create tests for you which will ensure that no injectable function is requiring anything that the module doesn't provide on its own (or via one of its dependencies).

- 2015-03-26

Using ReactJS with existing AngularJS codebase

ReactJS is an amazing View library that promises (and delivers) high performance, composability, and maintainability. AngularJS is an amazing MV\* framework. Tons of shops have adopted and totally bought into AngularJS for their entire frontend application. They're loving it, but some are finding that as these applications get bigger, they can become unwieldy, unperformant, and difficult to reason about. Many of these problems can be solved by doing things better with angular, but not all of them.

In this talk, we'll go over why you don't need to re-write your whole application to get some of the wins of React and that it actually is quite easy to integrate the two. We'll talk about where it makes sense to bring in React to an existing Angular codebase and how it works well.

Intro to AngularJS

AngularJS is one of the most popular frontend frameworks out there right now. If you haven't tried it yet, prepare to be amazed! Here's what we'll cover:

1. Templates/Expressions - Your View
2. Module - Your app's namespace
3. Directives - DOM Interface
4. Filters - Display utils
5. Scope - What on earth is this thing!?
6. Controllers - The View Model
7. Services - Common utilities
8. Working with third-party modules
9. Routing - Single Page App with state in the URL
10. Firebase & AngularFire - A full web application with no server setup required!

We'll be following through a repository hosted on GitHub. There's a branch for each concept, so you can play around with the code and then catch right back up with the next branch. So come on, and let's learn AngularJS!

- 2015-02-03
- 2014-06-06

Improving UX with GenieJS

I believe that people are so much more productive when they don't need to use the mouse to click on something. One implementation intended to help with this is keyboard shortcuts. Unfortunately, these are limited to the number of sensible keys and key combinations and can be difficult for users to discover, remember, and use. Normally, only super users will ever use them. The goal of genie is to address the problems with keyboard combinations.

Genie is a simple library to emulate the same kind of behavior seen in apps like Alfred (for macOS: [alfredapp.com](https://alfredapp.com)). Essentially, you register actions associated with keywords. Then you can request the genie to perform that action based on the best keyword match for a given keyword. This allows a user to type what they want to have happen and select from a list of the best matches for what they typed to perform an action. Over time, the genie will learn the actions more associated with specific keywords and those will be come first when a list of matching actions is requested. Check it out at [github.com/kentcdodds/genie](https://github.com/kentcdodds/genie)

- 2014-02-06

Watch your Watchers

If you're not careful (especially with your ng-repeats) your watch count in your app can grow pretty quick. This isn't a problem itself, but its what that does to your digest cycle. Lots of watchers makes your digest cycle take longer. In my talk, we'll talk about what Angular 1.3 is doing to help solve this problem, the problem their solution presents, a solution to that problem, and what can be done for pre-Angular 1.3 code.

Sharing code between Ionic and Web Angular Apps

This was an impromptu talk while we were waiting for the actual speakers to come, so I'm not on the schedule.

JWT: Not Your Grandma's Cookies

Cookies and sessions are the traditional way to keep track of user state on the server, but it can bite you later. JSON Web Tokens (JWT) is a stateless way to deal with users. I'll show how to use `$httpInterceptors` to make this easy as pie. :-)

Start with Epic Product Engineer, then explore the rest of my courses.

Learn product engineering: judgment, constraints, and what should be built.

Learn to build AI-powered applications.

Become a full stack web dev.

The most comprehensive guide for pros.

Learn smart, efficient testing methods.
