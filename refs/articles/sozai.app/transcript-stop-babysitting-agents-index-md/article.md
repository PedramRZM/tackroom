---
url: "https://sozai.app/transcript/stop-babysitting-agents/index.md"
site: "sozai.app"
type: "doc"
via: "direct"
---
**Stop babysitting your agents — Transcript & Summary | SozAI**
Source: https://sozai.app/transcript/stop-babysitting-agents/

Learn how to stop babysitting AI agents like Claude by improving tooling, verification, and autonomous loops for efficient software development.

## Key Takeaways

- High-quality documentation and tool integration are foundational for effective AI agent management.
- Verification processes modeled after human workflows help AI agents self-check and improve reliability.
- Parallelizing AI agents' work increases efficiency and throughput.
- Background loops allow fully autonomous AI operation, minimizing human intervention.
- Rethinking tooling for AI agents is essential as they become primary code authors.

## What the video covers

- Sid Boudesaria, founding engineer of Cloud Code, discusses strategies to reduce manual oversight of AI agents like Claude.
- Emphasizes the importance of high-quality Cloud MD files and integrating daily tools like Slack, Asana, and Datadog with Cloud Code.
- Recommends setting up remote environments on Cloud Code Web to ensure continuous compute independent of local devices.
- Highlights the shift from human-centric tooling to agent-centric tooling as AI agents now write most code.
- Explains that while many human tools translate well for agents, agents lack some human assumptions, requiring new approaches.
- Introduces a roadmap focusing on verification, multi-agent parallelization, and background loops to automate workflows.
- Verification involves teaching Claude to check its own work similarly to how humans verify code through compiling, testing, and debugging.
- Multi-agent strategies allow running many Claudes in parallel with confidence in their output.
- Background loops enable Claude to autonomously run continuous tasks without human keyboard input, removing bottlenecks.
- The talk encourages thinking about what agents need from codebases that humans take for granted to improve agent efficiency.

## Chapters

1. 00:00 Introduction and Context
2. 01:45 Tools and Human vs Agent Coding
3. 04:53 Verification and Iteration Process
4. 10:16 Demo: Verification Loop in Action
5. 26:12 Advanced Verification and Multi-Agent Work
6. 29:00 Cloud Agents and Remote Sessions
7. 33:51 Managing PRs and Automation with Routines

Answers

## Questions about this video

What is the main goal of the talk 'Stop babysitting your agents'?

The main goal is to provide strategies to reduce manual oversight of AI agents like Claude, enabling them to work more autonomously and efficiently.

Why is a high-quality Cloud MD file important?

A high-quality Cloud MD file significantly improves the Cloud Code experience by providing clear, structured information that helps AI agents understand and work with the codebase better.

What are background loops in the context of AI agents?

Background loops are autonomous cycles that allow AI agents like Claude to continuously run tasks and improve their work without requiring constant human input, removing the keyboard as a bottleneck.

## Full Transcript — Download SRT & Markdown

00:16

Speaker A

My name is Sid Boudesaria. I'm one of the founding engineers of Cloud Code. And today, I'm excited to be here to talk to you guys about how you can stop babysitting your agents. As models have been getting smarter,

00:33

Speaker A

I've noticed that we're increasingly spending a larger percentage of our time staring at the screen, waiting for Cloud to finish its work, or just acting as a glorified QA tester for Cloud. And this can be quite unsatisfying and also

00:50

Speaker A

just an inefficient use of your time. And my goal for this talk is to give you strategies and help you take back some of this time so that you can manage your agents better. You can also think of this as a more advanced Cloud Code talk, so a Cloud Code

01:14

Speaker A

301-type university class. And because of that, we have some prerequisites and some table stakes that everyone here should have at least heard about if not implemented for your own projects. Starting with a very high-quality Cloud MD file.

01:31

Speaker A

This is the single highest leverage thing that you can do to improve your Cloud Code experience. So if you haven't done this yet, I highly encourage you to try it out. Number two is connecting your tools to Cloud Code. A good

01:45

Speaker A

rule of thumb is that if a tool is useful for you in your day-to-day life, it will also be useful for Cloud. So things like Slack, Asana, Linear, Datadog, BigQuery, all of these things help Cloud stitch together a much richer context for itself, and it's able to perform much better if

02:06

Speaker A

you give it access to these tools. And finally, setting up your remote environment on Cloud Code Web. This makes it so that the compute that's running your Cloud Code is separated or decoupled from your laptop. So you can close

02:24

Speaker A

your laptop, your laptop could die, you could spill some water on your laptop, and your Cloud Code sessions will still continue because they're running in the cloud. I'd love to see a show of hands here. How many people use Cloud Code every day?

02:41

Speaker A

Okay, that's almost everyone. How many people have completed the first two things here? So high-quality CloudMD and you've connected your tools. Okay, it's about 50%, I'd say. And then how many people have done all three?

02:59

Speaker A

Okay, if you haven't raised your hand at all, don't worry, you'll still get some value out of the stock, but I would encourage you to start with these three things first. OK, so why does your tooling need to change? Most software tooling

03:19

Speaker A

so far was built with humans in mind. Whether it's linters, IDEs, Prettiers, Type Checkers, even compilers, they were mostly written with the goal of making humans and human teams faster. But the problem now is that humans aren't writing most of our code anymore. It's agents. So we

03:45

Speaker A

have to take a step back, zoom out, and reconsider our tooling. And when you do that, there's some good news, and then there's some bad news. The good news is that a lot of these tools that we've built for ourselves translate over pretty

04:00

Speaker A

well for agents as well. So things like Prettiers and Linters and Symbol servers, Claude and agents can end up using these things quite effectively, and they serve them pretty well. But the bad news is that we also have blind spots. As human beings, we have some assumptions that we make about

04:23

Speaker A

our tooling and our toolchain that Claude doesn't have. And for that reason, it's important to ask the question, what does an agent need from your code base that a human takes for granted? And I'd love for you guys to keep that question in

04:37

Speaker A

mind as we continue to the rest of the talk, because it kind of frames frames the goal of not babysitting your agents as much in a much more clear way. So this is our roadmap for today.

04:53

Speaker A

We'll be talking about three distinct things that build on top of each other. And when you take all of these three things together, they become incredibly powerful and give you a set of tools that can help you work in a way that

05:08

Speaker A

We just haven't worked before as human beings. So we'll be talking about verification, which is how to teach clot to check its own work. Once clot can check its own work and be more reliable, we can now run many clods at the

05:25

Speaker A

same time and be confident that they'll be doing the right thing. So we'll be talking about strategies for multi-clotting or parallelizing your work. And then finally, we'll end with background loops. And background loops are a way for you to completely take your keyboard

05:39

Speaker A

out of the hot path. So your keyboard is not the bottleneck anymore, and Claude just keeps running in the background in a loop doing useful work for you.

05:56

Speaker A

So I'd like to start the verification section with a brainstorm for a minute or so. I'd like everyone here to think about the last software project or feature that you worked on. And while you were working on that feature, how did you check

06:13

Speaker A

your own work? And I don't just mean how did you check the final output of your work, but I also mean how did you iterate on your work in a way that gave you confidence that you will end up in a place where

06:25

Speaker A

you're expecting to go. So let's take 30 seconds. If you have a pen and paper in front of you, feel free to jot this down. If you have a laptop and you want to, like, put this in your notes. Let's take 30 seconds

06:34

Speaker A

together and just come up with your last project and how you verified your work there.

07:07

Speaker A

I see some typing slowing down. So hopefully you've had a chance to think about it a little bit. It's OK if you haven't completely. But I've found that most software engineering tasks can be broken down into the series of steps that you see

07:23

Speaker A

on the screen. Some combination or sequence or subset of these things enable you to check your own work and build software. So you start with designing and writing code. You then usually end up building your code, running your compilers, type checkers, et cetera. If they fail, you go

07:46

Speaker A

back and change your code again and do that in a loop. Then you might run your executable, whether that's a Docker container or a CLI application or a web server. And then you might check for side effects. So if you're running a

08:02

Speaker A

web server, you might spin up your browser. And you might see if the UI elements are showing up in the correct place. You might even look for logs to see if it's a specific log that you're looking for present in your logs. Or

08:16

Speaker A

you might check the database to see what the state is and if state has been manipulated correctly. And then hopefully you'll run unit tests to make sure that you haven't made any regressions and your feature hasn't broken some other feature. And hopefully you

08:30

Speaker A

also added new unit tests for the thing that you're working on. And then finally, you deploy the staging. Or if you're really brave, you go straight to prod. And that's usually how humans verify their work and build software. And what's

08:46

Speaker A

interesting is that the same exact playbook can be used by Claude quite effectively to also verify its own work and build software. So as we go through the rest of this presentation, it's helpful to think about teaching Claude how to do

09:04

Speaker A

things in a similar way that you would do them. And the only thing that's required is giving Claude the right tools and instruction set to make this possible.

09:18

Speaker A

OK, so we've talked about verification, how humans do verification, and how Claude should theoretically do verification. But loops are really what makes the whole thing go around.

09:31

Speaker A

And this is arguably the most important slide in this presentation. So if you haven't been paying attention yet, this is a good time to get started. A loop essentially is an autonomous circuit that you can complete for Claude, and it allows

09:48

Speaker A

Claude to hill climb on a given task or a given success criteria. So you can think about it as giving Claude access to tools to verify its own work and to write code. And what Cloud will do is it will write

10:04

Speaker A

some code. It will check if there's a failure. If there's a failure, it will debug that failure and write some more code. And then it keeps doing that in a loop again and again and again until it gets to a success state. And

10:16

Speaker A

when it finally gets to a success state, you can be confident that the PR that it's sending you is higher quality and will actually work. So in this image that you see on the screen, I faced an issue recently where

10:32

Speaker A

on my personal website, the signup button stopped working. And what I told Claude was to make the signup button work. And this is kind of what it did. There's more steps here too, but for brevity's sake, it basically started writing some code. It

10:47

Speaker A

built my app. It clicked my signup button, opened up a browser, and saw that clicking the signup button isn't really doing anything. It doesn't take you anywhere. So then it decided to read some logs. and it found out what the problem was, it

11:01

Speaker A

fixed the code, reloaded the app, and kept doing that until it got to a successful state. And finally, what it came up with was a PR that indeed worked.

11:11

Speaker A

So the most important thing to take away from this slide is that wherever possible, our goal now is to get Claude into a loop by giving it the tools and instructions that are required for it to work effectively.

11:29

Speaker A

So verification comes in many flavors. We talked about UX verification. But you can have backend verification. You may want to verify your entire app end-to-end, including infra. And the core concept here remains the same. You want to give Cloud the tools and

11:45

Speaker A

the instructions to get it into a loop. And once you figure that piece out, all three all three of these flavors merge into one. You don't have to be very specific about the instructions you give Claude. As long as

11:58

Speaker A

it has all the right tools and instructions, it'll be able to verify all of these things. We've talked a lot about theory, and we've talked a lot about hypotheticals and jargon, but I wanted this slide to be a little bit more concrete.

12:14

Speaker A

What does it actually mean to give Claude the instructions and the tools to make it go in a loop? And it usually boils down to four things. And I'll go through the frontend or UX section from this slide. The first thing is to

12:28

Speaker A

run your application. So for a frontend application or a frontend verification loop, this might correspond to running your dev server. So running npm run start or whatever your dev server might be, it just spins up a dev server. Once

12:44

Speaker A

the dev server is up, you want Claude to actually use the web server. And the way it does that is by opening up a browser. My personal MCP tool of choice for this is the Claude and Chrome MCP tool. You can access this

12:58

Speaker A

with slash Chrome if you're using Claude code. You can also use Playwright, or there's a bunch of other browser control MCPs that you can use to do that. Once Claude can... drive your browser, the next step is to prove that something works. So if it's a fix it's working on, you

13:18

Speaker A

want to take a screenshot before the fix and after the fix and make sure that it's the right state. And finally, there's unblocking it.

13:29

Speaker A

So if you've ever tried to create a verification loop in a production app, you'll very quickly find that there are some blockers you run into. And some of the common blockers are, for example, auth and state. So auth basically means

13:47

Speaker A

you want to give Cloud an identity that it can log into to your web application so it can actually start to use your app. And then state means you may want to pre-configure some state. For example, if you have an e-commerce store, you

13:59

Speaker A

may want to populate the inventory for that store for Cloud to be able to use your app meaningfully. And this isn't very novel. In fact, in traditional software engineering too, when you write end-to-end tests, writing these state setup scripts are quite

14:14

Speaker A

common. The only difference here is that you want to give Clawd access to these scripts, and you want to make them dynamic. You don't want to be too prescriptive about what these scripts are doing, and that allows Clawd to do a much wider

14:27

Speaker A

variety of things than you can do with static scripts. OK, so we know what a verification loop now is. We know how to write one. How do you package it? How do you distribute the script to your colleagues,

14:43

Speaker A

to your coworkers, even to your future self? And one of the best ways of doing this is by using a skill. You can think of a skill as just a way to store some arbitrary context about a specific topic. And in this case,

14:58

Speaker A

that topic happens to be a verification loop. The interesting thing about skills also is that you can make them self-improving. So if you put in instructions into your skill about improving the skill every time Claude hits a blocker, you will end

15:14

Speaker A

up creating this self-documenting, self-improving skill which everyone on your team can contribute to, not just you. And this makes it really powerful. This is actually how we do verification in the Claude Code team as well. We have a single verification skill,

15:29

Speaker A

and the skill is explicitly told to keep documenting itself. So every time someone runs into a blocker, the skill will go back in and edit itself so that next time when you or your colleague run into the same issue, it's not

15:44

Speaker A

a problem. Okay, so we're going to jump into a demo next. But before the demo, I want to talk about what the application that I'm going to be using. There is a a type tester application called MonkeyType. How many of you have heard of MonkeyType? Okay,

16:07

Speaker A

I thought so. It's a niche community. But it's basically a type tester where it shows you a bunch of words, as you can see, and you have to type those words as accurately and as fast as possible. And the application just tracks your

16:21

Speaker A

stats for you. I like this as a demo app because it is representative of a real-world full-stack app. It's written in TypeScript with an express backend and MongoDB and Redis as persistence layers. And it's open source. So you guys can

16:38

Speaker A

go to monkeytype.com right now. You can even check out the source code if you want. But what we'll be doing in this demo is we'll be creating a verification loop live. So we'll tell Claude to spin up a new dev server. We'll tell

16:51

Speaker A

it to go and use the Chrome MCP to check some of its work. Once we create the verification skill, we'll also create a new feature and ask Cloud to use the verification skill to verify itself. So let's get started with the demo. So we can switch over to my laptop screen.

17:18

Speaker A

OK. So this is a brand new Cloud Code session. I've already done the homework of setting up MonkeyType locally. I've also installed some dependencies and curated a ClaudeMD because I didn't want to do that in front of you guys and waste

17:31

Speaker A

your time. So let's tell Claude to spin up the dev server. Okay, so it says the dev server is already running, and that's right, because I started it right before our talk. And let's go and check out what's on the

17:51

Speaker A

front end. So... If we go here, monkey type opens up. I can start typing, and there's a little timer that shows up. I'm not very good at typing, so there's a lot of typos here. But it's essentially what I

18:07

Speaker A

would expect. Let's also check out the backend link. This just returns a JSON, and it just basically means that the backend is up and running, which is good. The next thing I'm going to do is I'm going to make sure that my Chrome MCP is enabled. And the way you

18:27

Speaker A

do that is just slash Chrome. And as you can see here, it says status enabled, extension installed, which is exactly what we're looking for. If you don't have it installed, it'll take you to the setup guide, and you can install it for yourself.

18:43

Speaker A

And now I'm going to say use the Chrome MCP to make sure that the front end is working. Make it quick, please. OK. And what we should see now is that this is the tab that Claude is using.

19:05

Speaker A

And it should call the Chrome MCP tool. So if you go back here, we can see two Chrome MCP tool calls. I can Control-O and see exactly what it did. navigate it to localhost 3000, and then it's looking at the contents of the tab, which is great. But we

19:29

Speaker A

want to do something more exciting. Just looking at a static web page isn't very helpful. So let's say, can you... Actually, before I do that, I'm going to resize these so you guys can see what's happening in the background.

19:45

Speaker A

Okay. Can you try typing and make sure... everything works. OK. So Claude apparently is also not very good at typing. But it typed in something, and it says that typing works. That's great. Let's do one more thing. Let's say, can you also use the settings and

20:16

Speaker A

change something? Okay, so it navigated to the Settings page, and it's changing the difficulty to export. Not a good idea based on how it performed.

20:38

Speaker A

Okay, and it claims that the setting has persisted, and it's able to verify that. So that's great. What we did so far is we just held Claude's hand and told it exactly what to do. So you would spin up the

20:53

Speaker A

dev server, go and do these two or three things that we care about. And that's basically verification. What I can do next is I can tell Claude to take all the learnings from this session and put it into a skill file. So I

21:08

Speaker A

can say, take everything we learned and put it into a skill file in top Claude demo verification.

21:23

Speaker A

I didn't have to give it the full path, but I chose to anyway. OK, let's see. It wants to create a new directory.

21:38

Speaker A

OK, so it's now proceeding to write a fairly large scale.md file. And if you look at what's inside this file, we'll just skim through it real quick. It says, number one, bring up the stack, which is basically what we did.

21:52

Speaker A

It has some commands to do that. So it has Docker Compose, blah, blah, blah.

21:58

Speaker A

Then it loads up the Chrome MCP tools, because that's what we told it to do next. And then finally, there is a smoke test where it's using the browser tools to actually check its own work. So I'm going to go ahead and

22:13

Speaker A

say yes. Great. So that must have looked quite simple, and it really is. Creating a verification loop is simple.

22:25

Speaker A

There were a few blockers that came up along the way when I was setting up this demo. We don't have to talk about those right now, but I'm sure that if you were to do this yourself, you can probably get this up and

22:34

Speaker A

running within five to 10 minutes. What I'll do next is, because both Claude and I are so bad at typing, I'm going to tell Claude to make a confetti animation every time I mistype, and then use the verification skill that we

22:51

Speaker A

just created to verify its own work. So let's say, every time I mistype, please show me a confetti animation and use the skill that we just created to verify your work.

23:23

Speaker A

So it's going to do its thing, figure out where to write this code, and then hopefully the demo gods will be with us tonight OK, so it wants to write some files. I'm going to switch on auto mode

24:00

Speaker A

so it doesn't have to ask me for every file edit. OK, this is interesting. It created the feature, and then it realized that there were a couple of lint errors. So you see this like, oh, excellent errors too. And then it proceeded to fix those errors next.

24:38

Speaker A

And then it's verifying itself again. So you see the verification loop in action now, where it wrote some code. It encountered some issues.

24:51

Speaker A

It fixed those issues by writing some more code, and it kind of went in a circle doing that until it came to a good state. So let's test it out ourselves as well. OK, it's still doing something. Let's let it stop.

25:36

Speaker A

Okay, so we do see the confetti showing up. It put us on expert mode, which is why it keeps disappearing on me. But effectively, Claude was able to do the job and fix its own lint errors. We're running short of time, so I'm not going to let this finish, but

25:59

Speaker A

hopefully that gives you a taste of how powerful a verification loop can be and how Claude can continue to hill climb on a task if you give it the right instructions and tools to do so. Let's switch back over to the slides now.

26:15

Speaker A

The key takeaway here is you should try to hold Claude's hand and show it how to do verification. And once you've taught it how to do verification, it can very easily summarize those learnings into a skill file, which you can then

26:32

Speaker A

package and distribute for your future self and for your teammates. Okay, so now that we have mastered verification, we can graduate to multi-clotting or parallelizing our work more effectively.

26:56

Speaker A

The problem that arises when you try to run too many clod instances at the same time is that they all eat at your attention, and your attention is a scarce resource. I personally find that more than four to five sessions open

27:11

Speaker A

simultaneously takes a big load on my brain, and I can't really function beyond that.

27:17

Speaker A

So what are some ways that we can scale that, and what are some ways that some strategies we can use to multi-cloud more effectively? There's four things that we'll talk about today. There's the Cloud Code desktop app. which

27:33

Speaker A

provides you a GUI and makes it easier to manage multiple sessions. There is Agent View. So if you love the terminal, like I do, and you want to stay in the terminal, then we have Cloud Agents that provide you

27:49

Speaker A

some of the same benefits of the desktop app inside the terminal. You can also run Cloud in the cloud. So if you run it on our website, Cloud is now running in our cloud as opposed to your laptop. And finally, there's remote

28:06

Speaker A

control, which is my favorite feature. And we'll talk more about this when we get to it. So this is a screenshot of what the desktop app looks like. On the left, you have a sidebar. And the sidebar has all your sessions across all

28:20

Speaker A

surfaces. So it has your sessions that are running locally in the terminal. It has your sessions running in the cloud. It has your sessions running in all Git repos.

28:30

Speaker A

And so it becomes the central control plane for working with Cloud and your sessions.

28:37

Speaker A

You can also pin sessions. You can rename them. You can color your sessions differently.

28:43

Speaker A

And all of these things effectively are just solving the problem of grabbing your attention.

28:48

Speaker A

If you rename a session to something that's memorable to you, when you come back to it, you know what that session was doing. So these are all kind of ways to just make protect your attention more. If you love the terminal,

29:08

Speaker A

this used to be how you would multicloud. This is a setup of how I used to multicloud, at least. I used to have a TMux window manager with four panes, and each pane would work on a different work tree. This works, honestly,

29:25

Speaker A

but it is a lot to manage. Who here knows what Tmux is? Okay, great. That's a lot of people. And who here knows what Worktrees are? Great, about 50%. So you have to kind of manage Worktrees and Tmux yourself,

29:43

Speaker A

which works, and I think I'm used to it now, but it's also not the most convenient thing. We can do better. And what we arrived at was Claude Agents. This is a feature that we released, I think, a week ago,

30:00

Speaker A

maybe a little bit more than a week. And the way you access it is just say Cloud Agents instead of Cloud. And it opens up this view, which is very similar to the desktop sidebar that we saw before. And this view lists all

30:14

Speaker A

your sessions that are running on your local computer. It also sorts them by the degree of attention that they require. So if a session needs your immediate attention, and if it's blocked on, let's say, a permission prompt or a question or some input

30:28

Speaker A

that it needs from you, it'll show up right at the top. If a session is running or if a session has completed its desired success date, it'll be further down. You can also customize it. So you can, again, pin sessions. You can rename

30:41

Speaker A

sessions. You can reorder them. And again, this is a way to just manage your workload and manage your attention a little bit better.

30:54

Speaker A

Cloud Code on the Web. We've talked about this a little bit, but the main goal here is how do you decouple your laptop with your Cloud Code sessions? I find it quite annoying that when I'm walking from meeting to meeting, I have to

31:09

Speaker A

have my laptop open and just walk like this everywhere. When I'm driving back home, I'm also annoyed because there's no internet and I can't leave my laptop open in my car. Having your sessions be running in the cloud is really

31:26

Speaker A

nice. You don't have to worry about the compute that it's actually running on. And if you haven't given Cloud Code on the Web a shot, just go to cloudai.com and it's pretty easy to get started. And finally, remote control. As I said earlier, this is my favorite feature. And remote control

31:49

Speaker A

essentially gives you the option to control any session running on any surface with your phone. The way to get started with remote control is you just go to wherever you're running your Cloud Code session and say slash remote dash control.

32:06

Speaker A

And once you do that, it will pop up on your mobile app. It will also send you notifications. So if Cloud needs some help from you or needs your input, your phone will buzz And you could be in your car. You could be

32:19

Speaker A

doing whatever you want. And you could just give Claude the input that it needs.

32:27

Speaker A

I am running short on time, so I'm going to skip this demo, unfortunately. But I was just going to show you Claude agents as part of this demo. So if you haven't given Claude agents a try, just give it a shot.

32:43

Speaker A

OK, so we've talked about how to make Cloud more reliable by making it or giving it the skills to verify its own work. We've also talked about how do you multi-Cloud more effectively. But even that isn't quite satisfying.

33:02

Speaker A

You still have to actually spin up a new session. You have to have a goal in mind, and whether it's on the desktop app or the terminal or web, you have to go and spin up a new session. How do you remove yourself

33:15

Speaker A

from the loop even more? And that's what this next session is going to be about. So as software engineers, we have a lot of different tasks. And not all of these tasks are writing code for a specific new feature or a bug that you're working on. A lot of this is just

33:35

Speaker A

bookkeeping in some ways. So personally, I'm spending a lot of my time now babysitting my PRs. I think we all have a lot more PRs now that we're able to generate with the help of Cloud and AI, and these PRs need to merge.

33:51

Speaker A

But before merging, you need to get through your review comments, you need to get through merge conflicts, you need to get through CI failures. There's a lot that goes on, and if you have 20 or 30 of these PRs you're trying to merge

34:02

Speaker A

in a day, you can easily end up spending hours on babysitting these. Updating docs is another good one. As we increase our velocity of shipping features and shipping fixes, we also need to keep up with docs. Similarly, triaging, monitoring feedback, and

34:20

Speaker A

just in general keeping CI green, these are all things that you kind of need to do every day, but they don't necessarily need you in the loop. They just need to be running in some sort of loop. And that's where the slash loop

34:36

Speaker A

command comes in. So slash loop is a way to run a prompt at a specific interval in Cloud Code. So you can say slash loop 10 minutes and babysit my open PRs. And what this will do is the Cloud Code,

34:54

Speaker A

the session that's running the slash command will wake up every 10 minutes. It will run this prompt. And if you have your Cloud MDs and your tools defined and set up correctly, it will be able to figure out what to do by itself.

35:06

Speaker A

So you don't really have to be babysitting and monitoring your PRs manually. Routines. Routines are basically slash loop, but running remotely. So we talked about Cloud Code on the web before and how that uses a remote container to run

35:28

Speaker A

your sessions. Routines live and work in the same containers. The way you set up routines is by going to the web app or the desktop app. You'll see a little routines Routines tab out there. And you can set up a new

35:43

Speaker A

routine quite easily. You can have a time-based trigger or you can have an event-based trigger. And both of those triggers can lead to a new Cloud Code session opening up with a specified prompt. So for example, we have a routine that updates

35:59

Speaker A

our docs every day for the Cloud Code team. We also have a routine that looks at our issues and feedback that's coming in and posts on our Slack channel.

36:10

Speaker A

every six hours. So this can be quite useful to do routine tasks that don't necessarily require you in the loop.

36:26

Speaker A

Cool. So once you stack all of these three skills together, you end up at this system which is able to do a lot of work even without you having to manually be on your keyboard. And that really is the ultimate goal, is that

36:43

Speaker A

you can kind of spend your attention and your time on the tasks that you care about. And everything else can just be delegated to Claude with high reliability and a high degree of confidence. Cool.

36:58

Speaker A

So that's all I have for you guys. Thank you so much, and I hope you enjoyed the talk.

Topics: Cloud Code Claude AI AI agents software verification automation tool integration background loops parallel processing developer productivity AI tooling

Study this video

- [Flashcards from this video](https://sozai.app/tools/flashcard-maker/?from=transcript&id=28470)
- [Quiz on this video](https://sozai.app/tools/quiz-generator/?from=transcript&id=28470)
- [Crossword from this video](https://sozai.app/tools/crossword-maker/?from=transcript&id=28470)
- [Word search from this video](https://sozai.app/tools/word-search-maker/?from=transcript&id=28470)
- [Study guide from this video](https://sozai.app/tools/study-guide-maker/?from=transcript&id=28470)

Free, made by AI from this transcript. No signup.


---
This is the markdown twin of https://sozai.app/transcript/stop-babysitting-agents/ — the same content, without the markup.
Published by SozAI (https://sozai.app). Reuse and quotation are allowed with attribution and a link back.
Machine-readable index: https://sozai.app/llms.txt · data API: https://sozai.app/api/

