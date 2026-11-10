---
url: "https://sozai.app/transcript/beyond-basics-claude-code/index.md"
site: "sozai.app"
type: "doc"
via: "direct"
---
**Beyond the basics with Claude Code — Transcript & Summary | SozAI**
Source: https://sozai.app/transcript/beyond-basics-claude-code/

Explore advanced customization of Cloud Code for scalable, agentic software engineering in large teams and complex environments.

## Key Takeaways

- Customizing Cloud Code is essential for handling complex, large-scale software engineering environments.
- Understanding the motivation ('why') behind code changes is crucial for effective agent collaboration.
- Agentic software engineering requires integrating multiple information sources beyond source code.
- Fine-tuning alone is inadequate; deep integration with internal tools and documentation is needed.
- Agents like Claude can help scale engineering efforts by automating routine tasks and improving information dissemination.

## What the video covers

- Daisy Holman, an engineer on the Cloud Code team, discusses moving beyond basics to agentic software engineering.
- The talk focuses on customizing Cloud Code to handle complex software engineering tasks at scale.
- Agentic software engineering differs from simple agentic programming by addressing large-scale environments with many stakeholders.
- Key challenges include managing context windows, software packaging analogies, and integrating diverse information sources like Slack, emails, and design docs.
- Customization is necessary for environments with technical debt, conventions, and large teams to disseminate information efficiently.
- Three essential categories for customization are access, knowledge, and tooling to enable effective agentic harnesses.
- Claude must understand the 'why' behind tasks, not just the code, to choose the best pathways and collaborate effectively.
- Fine-tuning alone is insufficient for customization; integration with internal vocabularies, APIs, and documentation is critical.
- Cloud Code is used internally to develop itself, showcasing practical applications of agentic software engineering.
- The ultimate goal is to scale engineers' abilities by creating agent clones that handle CI/CD, dashboards, and other routine tasks.

Answers

## Questions about this video

What is the main focus of the video 'Beyond the basics with Cloud Code'?

The video focuses on advanced customization of Cloud Code to support agentic software engineering in complex, large-scale environments with many stakeholders.

Why is customization important for Cloud Code in large software projects?

Customization is important because large projects have conventions, technical debt, and diverse stakeholders, requiring efficient information dissemination and tailored agent behavior.

What are the three key categories needed to customize an agentic harness according to the video?

The three key categories are access, knowledge, and tooling, which together enable agents to understand context, motivation, and perform tasks effectively.

## Full Transcript — Download SRT & Markdown

00:00

Speaker A

Super excited to hang out with you for the next 45 minutes. My name is Daisy Holman. I'm an engineer on the Cloud Code team. And I'm gonna talk about beyond the basics with Cloud Code. This is really a kind of next step. I really wanna talk about more about agentic software engineering than agentic programming, if that makes any sense. This is more a talk targeted at software engineering environments and the kind of constraints that we run into in terms of customizing agents in those environments. So, yeah, like I said,

00:41

Speaker A

about agentic software engineering than agentic programming, if that makes any sense. This is more a talk targeted at software engineering environments and the kind of constraints that we run into in terms of customizing agents in those environments. So, yeah, like I said,

00:58

Speaker A

I work on Cloud Code. I got the super awesome opportunity to get involved pretty early and have gotten to be involved in some really, really cool efforts, including plug-ins and agent teams. And, yeah, I come from a background in programming languages. I was

01:16

Speaker A

once a chair on the C++ committee. And I think a lot of the things that I was very interested in about programming languages really apply to agentic harness design. I think I'm very interested in making it easy for people to make their

01:33

Speaker A

once a chair on the C++ committee. And I think a lot of the things that I was very interested in about programming languages really apply to agentic harness design. I think I'm very interested in making it easy for people to make their

01:50

Speaker A

we've really been able to start doing that at scale. All right, so where we're headed. We're mostly gonna be talking about ways to customize Cloud Code. I think Cloud Code itself works pretty well out of the box for very simple, what I would

02:06

Speaker A

ideas into production, regardless of how technical they are. And I want software engineers to be a part of that, too. That software engineering to be a part of the thing about ideas. I think that Cloud Code is one of the first times

02:24

Speaker A

about how to think about the context window and how there's this analogy to software packaging and where that breaks down and how that works. We'll talk about some of the key abstractions in plugins and focus on which ones of them

02:41

Speaker A

we've really been able to start doing that at scale. All right, so where we're headed. We're mostly gonna be talking about ways to customize Cloud Code. I think Cloud Code itself works pretty well out of the box for very simple, what I would

02:59

Speaker A

I have time, hopefully I will, I'm going to run through a few of the new things that we're doing with Cloud Code, the ways that we're starting to use it internally to develop Cloud Code with Cloud Code, and where we see the next

03:16

Speaker A

call programming tasks, but as you ratchet up the complexity and as you approach things that I would call software engineering tasks, to give it some knobs and whistles and some customization to make it work the way you want to. We'll talk

03:32

Speaker A

on Cloud Code. I hope you use Cloud Code. I hope you like Cloud Code.

03:37

Speaker A

about how to think about the context window and how there's this analogy to software packaging and where that breaks down and how that works. We'll talk about some of the key abstractions in plugins and focus on which ones of them

03:52

Speaker A

and tooling. And I'm going to kind of break down each of these. This is if there's one thesis of this whole talk that I want you to take away here. It's that if Claude can't do everything you can do, it can't do your

04:06

Speaker A

scale up to real large-scale software engineering environments. Environments where you have hundreds or thousands or tens of thousands of engineers working on the same code base. And you need to disseminate information efficiently without filling up your context too quickly. Finally, if

04:22

Speaker A

you can get to, and I'm not just talking about source code, I'm talking about Slack messages, et cetera. I have another slide about this afterwards. I'm talking about emails. I'm talking about understanding the why of your tasks and not just

04:40

Speaker A

I have time, hopefully I will, I'm going to run through a few of the new things that we're doing with Cloud Code, the ways that we're starting to use it internally to develop Cloud Code with Cloud Code, and where we see the next

04:56

Speaker A

Claude just sees a repo and a shell, right? This works okay, fine for like zero to one projects that don't have any conventions, that don't have any built up technical debt over time, that don't have a wide range of stakeholders that Claude

05:12

Speaker A

year going or the next three months, the next year is who knows. So, first, let's talk about why would you need to customize an agentic harness in general? And I do say agentic harness in general, right? I mean, obviously, I work

05:30

Speaker A

do high quality software engineering at very large scales. I think sometimes you can get away with it if you're working on very leaf software, but especially if anyone depends on you, especially if you have external stakeholders of any kind, you need to give

05:47

Speaker A

on Cloud Code. I hope you use Cloud Code. I hope you like Cloud Code.

06:04

Speaker A

times, right? We do design documents, we write emails to each other, we talk on Slack, right? This is a very important thing to keep in mind. This is why these zero to one projects work fine with no customization, but full-scale software engineering needs

06:21

Speaker A

But I really am also interested in this as an academic question as to how do you customize the generic idea of an agentic harness with information, with connectivity, et cetera. So there's three things that three categories of things you really need. Access, knowledge,

06:38

Speaker A

thread about why you decided to implement this thing, Claude can figure out, you know, why this strategy might not work or why this might be better than that, right?

06:49

Speaker A

and tooling. And I'm going to kind of break down each of these. This is if there's one thesis of this whole talk that I want you to take away here. It's that if Claude can't do everything you can do, it can't do your

07:06

Speaker A

with your brain, right? CI and CD, absolutely critical. You should not be fixing CI failures yourself at this point in time. Agents are very, very good at that. will very likely continue to be in the future. Dashboards, when something goes down

07:23

Speaker A

job with you. Right? Your job as a software engineer at this point is to make little clones of yourself so you can scale up your abilities and scale up your work across many agents. And if Claude can't get to the things that

07:36

Speaker A

with accuracy, right? And in a way that you can trust. And Claude needs to be able to see the why, right? This comes back to Claude being able to see the why. Internal documents, design docs, run books, all kinds of other things. We

07:51

Speaker A

you can get to, and I'm not just talking about source code, I'm talking about Slack messages, et cetera. I have another slide about this afterwards. I'm talking about emails. I'm talking about understanding the why of your tasks and not just

08:07

Speaker A

PRs per meeting. I strongly suggest you do that. Cloud needs to know why you want to do things in order to choose the best pathway, in order to work with you as a colleague. Here's the tip that I give. Try doing a full

08:23

Speaker A

understanding the what. The source code doesn't often explain the motivation for why you need to make a change and typing that out in a prompt is not something you always want to do because that information is already somewhere. So, out of the box,

08:39

Speaker A

down on a piece of paper, and then at the end of the day, try and find ways to connect Quad to all of those things. It will work a lot, lot better than you think. The gap is much bigger than you notice until

08:55

Speaker A

Claude just sees a repo and a shell, right? This works okay, fine for like zero to one projects that don't have any conventions, that don't have any built up technical debt over time, that don't have a wide range of stakeholders that Claude

09:10

Speaker A

yours, your internal vocabulary, your internal APIs. Fine-tuning doesn't really, I always get questions about fine-tuning when it comes to this. Fine-tuning doesn't really work very well for this. I can talk a little bit more offline about why that is and what we're learning.

09:26

Speaker A

needs to understand stakeholder concerns for. And you know, like when Claude can own everything, it's not all that important to customize, to bring in information from different sources. But this kind of vanilla Cloud Code is rarely enough to

09:43

Speaker A

done fine-tuning for something small, even if you're a big company, right, even if you're a very big company, fine-tuning on a model, the frontier model just isn't cost-efficient at this point in time. So, you need to do this all via in-context memory or

10:01

Speaker A

do high quality software engineering at very large scales. I think sometimes you can get away with it if you're working on very leaf software, but especially if anyone depends on you, especially if you have external stakeholders of any kind, you need to give

10:24

Speaker A

At scale, because of the Bitter lesson, if you're familiar with the Bitter lesson, general AI wins out over specialized AI in the long run. And we're really seeing that with frontier models now. And we can't realistically train anything into the model that's specific

10:40

Speaker A

Cloud the tools to understand those concerns. They're not always in the source code. They're not always in the documentation. And most of the work in professional software engineering, especially at very large scales, doesn't live in the actual source code. I've said this several

10:55

Speaker A

the model. So, I mean, there's good and bad there, right? You don't need to understand anything about the weights of the model in order to customize its behavior. And all of the things that you can do with the model are just text files.

11:09

Speaker A

times, right? We do design documents, we write emails to each other, we talk on Slack, right? This is a very important thing to keep in mind. This is why these zero to one projects work fine with no customization, but full-scale software engineering needs

11:14

Speaker A

They're like, well, that's probably good enough. But there's a lot of optimization you can do within context learning. Yeah. Tooling. Tooling is the other thing I like to think about. Like, what does an IDE for Claude look like?

11:30

Speaker A

a lot of information. So, let's talk about how this -- what you might need to give Claude access to. Team chat, very first one, right? Where are your decisions being made? If you can see the entire conversation in a Slack

11:47

Speaker A

us who have written code before professionally use syntax highlighting. Most of us probably use some sort of LSP, probably use some sort of code completion, all of those kinds of things. Cloud has none of those out of the box, right? It has an

12:03

Speaker A

thread about why you decided to implement this thing, Claude can figure out, you know, why this strategy might not work or why this might be better than that, right?

12:18

Speaker A

had to use ED except by choice, but if you have, you know how hard it is to do any kind of real text editing. What you want to be thinking about in these kinds of customizations is what does the agentic version of

12:34

Speaker A

I think often when people get frustrated that Claude is taking the wrong direction, there's some information in your brain that you got from somewhere that Claude can't access. And if Claude can access that, it's much, much more likely to jive

12:49

Speaker A

of arguments to a function, the red squigglies, think about what they do to your brain, right? They kind of, they nudge you in a direction, without completely stopping you, right? So, you're like, wait, should I think about that again? Oh, no, I know

13:04

Speaker A

with your brain, right? CI and CD, absolutely critical. You should not be fixing CI failures yourself at this point in time. Agents are very, very good at that. It will very likely continue to be in the future. Dashboards, when something goes down

13:17

Speaker A

hooks are perfect for this. I'm going to get into hooks a little bit later for those of you not familiar, but, like, this is the -- This is the red squigglies for your agent, right? You can run linters. You can do, we

13:32

Speaker A

in production, you need to be able to pull in a lot of information very quickly. And the reality is that you're going to be competing with companies who are doing this agentically. And so you need to be able to do it efficiently, agentically,

13:49

Speaker A

you do in your code base, but like certainly at the harness level, we can't. you probably want to remind it that it's a generated file, because maybe it has a good reason for editing the generated file just to try something out and

14:04

Speaker A

with accuracy, right? And in a way that you can trust. And Claude needs to be able to see the why, right? This comes back to Claude being able to see the why. Internal documents, design docs, run books, all kinds of other things. We

14:17

Speaker A

it has forgotten, then it will stop and undo it, usually. It's a red squiggly.

14:22

Speaker A

have largely started recording our meetings or transcribing our meetings, and I will go right after the meeting and feed the meeting notes into Claude and say, is there any low-hanging fruit from this meeting that you can address? And I'll get two or three

14:36

Speaker A

environments for developers. You had to have a way for humans to edit your codebase.

14:40

Speaker A

PRs per meeting. I strongly suggest you do that. Cloud needs to know why you want to do things in order to choose the best pathway, in order to work with you as a colleague. Here's the tip that I give. Try doing a full

14:53

Speaker A

of two kinds of tools. There's tools that compensate for a lack of intelligence, and there's tools that scale with intelligence, right? I think of the red squigglies as the second one, right? They're a nudge, a reminder of something you might have forgotten. But

15:08

Speaker A

day of work without leaving the Cloud Code terminal or the desktop or whatever you use. Every time you have to reach for another tool, every time you have to alt-tab to something else and copy-paste into Cloud, that's something Cloud is missing. Write it

15:31

Speaker A

I guess in theory lead to fewer mistakes, but that doesn't really scale up well with intelligence, right? It kind of makes Claude write code in a very specific order, and that isn't going to lead to good results. I actually asked Claude for good

15:47

Speaker A

down on a piece of paper, and then at the end of the day, try and find ways to connect Cloud to all of those things. It will work a lot, lot better than you think. The gap is much bigger than you notice until

16:04

Speaker A

AGI-pilled approach here, right, is to think about tools that scale with intelligence. As the models get better, these tools get more useful to the model. So, I want to think, I want to go through a little bit of kind of

16:22

Speaker A

you make all of the connections. Knowledge is another reason why we need to customize Cloud. We can't train your code base's conventions into the model, right? We can't train institutional memory into the model. Things that changed last week, or things that are just

16:45

Speaker A

In QWAD Opus 4.7, it's like one million tokens usually. Interesting thing here is that context windows aren't really growing. Like, if you look at the leading frontier models from a year ago, they were mostly 1 million token context models.

17:02

Speaker A

yours, your internal vocabulary, your internal APIs. Fine-tuning doesn't really, I always get questions about fine-tuning when it comes to this. Fine-tuning doesn't really w

17:19

Speaker A

from now versus the models from a year ago are a lot more There's a lot more change than just the size of the context windows, right? And the size of the context windows are remaining relatively constant. So you kind of have a fixed

17:34

Speaker A

target for how you need to do your context engineering, right? Like I said earlier, right, your tool that you have to make your output better is in context learning.

17:43

Speaker A

And that means that everything, every customization you put into the model has to go into this context window in some form. We're going to talk about more scalable ways to do that, right? You can't just dump your whole code base. You can't dump

17:57

Speaker A

your whole wiki in there, right? You can't dump all of your internal docs into the context window. You need to figure out better ways to get the right information in at the right time. So, yeah, the other way I like to think about

18:11

Speaker A

this is that, like, we have a really constrained amount of space to put a lot of information into. And it's kind of a unique problem. I like to say it's like trying to run NPM on an Arduino. You've got a tiny bit of

18:26

Speaker A

memory, and you've got to figure out the very most important things to put in there, and you want to put the smallest version of it that you can in there in order to leave enough room to do real work. If you were to

18:41

Speaker A

install packages willy-nilly on an Arduino, you're not going to leave any room for your own code. It's kind of the same idea. You have to be very intentional about what you put into your context window. Don't pay for what you don't use, which

18:56

Speaker A

is like I think a famous originally C++ quote, right? It's a zero overhead abstraction principle. It's not just a nice to have here, right? It's not like, well, we'll throw more compute power at it. We are fundamentally at a limit or what looks

19:10

Speaker A

like a limit. I mean, I might eat my words, but what looks like a limit of context window size, and it's not getting bigger. Right? So, the only way to get more efficient at putting information into the model is to get better at

19:26

Speaker A

not paying for what you don't use. There's one more thing I want to talk about that kind of makes this even more complicated. And kind of makes the analogy fall apart, actually. Like, the first thing I thought of when I saw this was,

19:42

Speaker A

like, this problem space was, like, oh, well, we already know how to make caches, right? the L1 cache doesn't hold all of memory because it's very constrained and we just evict things we haven't used recently. The problem is that there's

19:59

Speaker A

this other constraint that we have called the KV cache. And the KV cache pretty heavily determines how expensive it is to calculate the next token. So if you go and change something really early in the prompt, you're going

20:17

Speaker A

to end up paying for uncashed tokens, which cost 10 times as much, for all of the rest of your context window after that change. If you wanted to only include a certain number of tools and then evict one that hasn't been used and

20:34

Speaker A

replace it with one that needs to be used sooner, you can't do that. You can't actually take anything out of this tools block without invalidating the entire rest of the cache. And that's actually a really hard constraint to work around, right?

20:51

Speaker A

I think some of the early approaches to agentic customization did take a very LRU cache approach. And I think it made more sense when we had 32,000 token context windows maybe and all of the tokens were expensive no matter what

21:08

Speaker A

and KB caching wasn't as efficient. But none of that's true anymore, right? You should think of these tokens as cheap, and these tokens as expensive, right? And you're going to pay a whole lot for a lot of expensive tokens just to save some context window. So you really have to think

21:30

Speaker A

about putting stable shared stuff at the very front and volatile per task information closer to the end, right? So that you can evict it without too much cost. There's a lot of complexity here, and I don't think we're even close to solving this

21:46

Speaker A

problem. But we spend a lot of time thinking about it. These are the kinds of things we think about day to day on the Cloud Code team. So let's look at these plugin abstractions. I really want to look at this in the context

22:01

Speaker A

of large scale software engineering, of monorepos where each one of these, I want you to ask, what happens if I have 10,000 of them? What happens if I have 100,000 of them? There are companies out there right now with tens of thousands

22:16

Speaker A

or hundreds of thousands of skills in their monorepo, and they're really hitting a scaling boundary because of that. And I'm going to talk about why. Uh-oh. There we go.

22:28

Speaker A

Slides are okay. We're good. So, yeah, the four plug-in primitives that I really want to examine in this light are are MCP, skills, hooks, and agents. If you've ever written a plugin, you may be familiar with some of these, not all of

22:46

Speaker A

them. There are other customization points in the plugin spec that I'm not going to talk about. A lot of this carries over, a lot of this thinking carries over between these kinds of customizations. But anyway, let's dive into MCP. Probably, if

23:04

Speaker A

you're in an advanced workshop, I would guess that you're familiar with MCP, you've heard of it before. It's been around for a while. The biggest thing to know about it is that it was designed in an era where Agents were much simpler,

23:20

Speaker A

or LLMs were much simpler. It was designed primarily, initially at least, to work with chatbots. And your chatbot is usually running serverless, or is usually not running in a container. It doesn't have access to files on your computer. It can't run commands. It can't use a CLI. And it's a

23:43

Speaker A

way to kind of inject more tools into the context. It has some nice properties, like it's transport agnostic. It mostly handles auth for you. It's meant to be the thing that if your company wants to ship an integration

24:01

Speaker A

with Claude, that integration that's shipped to the public from your company should probably be an MCP server, or at least at first should probably be an MCP server. There's probably some other things you can add on, but this is like the

24:18

Speaker A

general public version. But we're in this talk talking about professional software engineering environments. We're talking about large-scale monorepos. We're talking about developers working together on the same piece of code and how do we share customizations and share information across agents. And like,

24:34

Speaker A

Yeah, I said this about all the properties. But it assumes that it doesn't have a shell. Cloud Code does have a shell. So if you already have a CLI, it doesn't make a whole lot of sense to wrap that CLI in MCP unless

24:48

Speaker A

you're shipping it to non-technical customers. I think that's kind of the rule of thumb.

24:53

Speaker A

Usually a skill that just tells Cloud how to use the CLI is much easier to write up. And I think often when you're talking about developer experience for your developers at a large company with lots of code that needs to interact

25:10

Speaker A

with each other, you're almost always going to be shipping skills or customizing with skills and not MCP servers. Now, you still need to use other people's MCP servers, right? You still are gonna need to use an MCP server to connect to Slack

25:25

Speaker A

at this point. You're still gonna need to use MCP servers to connect to email and all of those things I talked about at the very beginning. Let's talk about does it scale? What happens if you have 10,000 of these and you wanna put

25:39

Speaker A

them all, you wanna have them all available to your agent? It has to put the name, the description, and the schema in the system prompt. So, for each tool, so that Claude knows how to call the tool. Right? If

25:55

Speaker A

you have even 20 servers with 15 tools each, most of your context window starts to be tool definitions. So, it doesn't scale without help. We have a new kind of approach to this called tool search. that mostly works. It does exactly what you think. We put just the names

26:17

Speaker A

in the system prompt, and then we tell Claude that it has a tool that it can use to search for tools to use later down in the transcript. And if it finds a tool, it will give it the description in the schema at

26:33

Speaker A

that point. So, it's kind of lazy loaded. The problem is that, like, Unless it's something very specific like Slack and the user mentions Slack, Claude's not necessarily going to know that it needs to search for a tool. So things like edit tool, things

26:50

Speaker A

like bash tool that are very generic, we end up usually having to put those in the system prompt with their schema directly. And so it... And the other thing is that the more of the description you put into the system prompt, you can

27:07

Speaker A

collapse down this description, right? You can do various forms of this description, how much you want to put or how little you want to put. And the more of the description you put into the system prompt, the more likely Claude is to search

27:22

Speaker A

for the tool. So it's like there's not a free lunch here. It is a slightly less expensive lunch. It also doesn't fix the problems with like, Setting up auth and process lifecycle and all the other things that go with MCP, if you're developing

27:37

Speaker A

code in your source, like if your user is a developer within your company and they already have access to your source code, right, like you probably can do most of the things already. You don't need to set up this whole auth lifecycle to

27:53

Speaker A

make sure the MCP works everywhere and all of the other things that are involved in that. So, using the CLI with a skill is a great way to tell Cloud how to do things, especially for scripts that you already have. So, speaking of

28:09

Speaker A

skills, who is familiar with skills? Like, who thinks they could -- okay. Everyone's familiar with it. The term I used to use when describing it when it first came out is that it's like a lazy system prompt. It is a Cloud.md file

28:26

Speaker A

with a miniature version that tells Cloud when it should read that file. There's a one-line description that goes in the front matter that ends up getting put into the system prompt. And quad has a tool that it can use to load the full

28:43

Speaker A

skill.md and get to all of the scripts and other resources that are in the directory. But fundamentally, a skill is just a folder. It's a folder with a markdown file in it that happens to have some sort of summary associated with it.

29:02

Speaker A

And so, it's like really easy to set this kind of thing up in your repository. That can be good and can be bad. You definitely need to be careful about figuring out how to control the quality of skills in your monorepo, right? Because

29:16

Speaker A

it's so easy to create a new one. Let's talk about whether it scales, right?

29:21

Speaker A

The body is pay-per-use, which is a good thing, right? But the description is always loaded, so you're always paying some fraction, some small fraction of that body in your system prompt. So it's not quite zero overhead in terms of abstraction. Reliably triggering skills still sometimes takes up to a paragraph,

29:44

Speaker A

something like 300, 400 tokens sometimes. And again, the more you cut out of that description, the less likely it is to reliably trigger without the user explicitly saying something. And no, skills don't have a defined way to do hierarchy yet. You can't lazily expose sub-skills. We

30:07

Speaker A

are working on this. Stay tuned, next couple of weeks, hopefully, there'll be a really cool announcement about that. Yeah, so it kind of scales. I think we had hoped when we started down that trail, that pathway, that it would scale better, but we also didn't really think ahead to this time period

30:30

Speaker A

where monorepos would have 100,000 skills. It's just such a massive amount of information, and you really need actual zero overhead abstractions. So, speaking of which, hooks. Hooks can't do everything. They're not perfect. But they are an actual zero overhead abstraction here, right?

30:47

Speaker A

We give you a bunch of different event types to trigger on. And then we just call this script. We call a script that you give us. In a special way, there's a JSON format that you can pass to it, and there's a

31:03

Speaker A

JSON format that it'll pass back in order to determine whether or not it needs to insert something into the context window. You can look up all of that on the website. Also, Quad knows how to use them and create them very well. Fundamentally,

31:19

Speaker A

no, they're not complicated, right? Something happens in the agentic loop, and it triggers something on your computer to run. And that thing runs and decides if it wants to insert something into the context window or not. So you can have 100,000 of these,

31:36

Speaker A

and if you have a big enough computer and 99,995 of them don't trigger, don't match, or don't return any text to put into the context window. Your only constraint is your computer, right? You've taken a very constrained resource and kind of blown

31:52

Speaker A

it out into a much less constrained resource. And when you think about systems like this, that's really what you want to be looking for, the property you want to be looking for, right? It runs outside the context window, so there's zero token cost.

32:08

Speaker A

I mean, again, if you have a JavaScript skill and you're writing Rust, you still pay for this little description in the front that says, like, you know, use this skill when you're writing JavaScript. And then Quad has to ignore that

32:25

Speaker A

little description. But if you have a hook that, like, type checks your JavaScript code and you're writing Rust, the hook runs, sees that it's not a JavaScript file, and then stops and doesn't return anything. You don't pay for

32:43

Speaker A

what you don't use. It doesn't work for everything. It's not the most AGI-filled thing. You end up doing things like parsing individual words or regexes out of the commands or out of the tool calls or whatever.

33:01

Speaker A

And there are some limitations there. You can use subagents to decide whether or not you want to inject something, but that starts to get expensive from a token perspective.

33:10

Speaker A

So there's a lot of trade-offs here. Again, no free lunch, but maybe a little cheaper. This is where our red squigglies live, like I was talking about earlier. Subagents, I'm gonna breeze through this a little bit 'cause a lot of the concerns are

33:26

Speaker A

pretty similar. But again, the thing you wanna think about here, subagents are structured as a description that goes into the system prompt and then a system prompt for the subagent or a set of text in context learning for the subagent so that it

33:44

Speaker A

can perform a specific task. And you only pay for those tokens in a separate context, right? So all you're paying for is the tool call in the main context and the result from the subagent. But the system prompt of the subagent

34:01

Speaker A

goes into a different context. And by pay, I mean in terms of cost in your context window. Obviously, tokens aren't just free because you're using a subagent. But I'm talking much more about the challenge of splitting up this one context window that an

34:19

Speaker A

agent can have. Right. So, like, an agent can read 50 files so the main loop doesn't have to. So, they're scalable in that way. But they still have the same problem that each agent's description still sits in the parent prompt. It

34:34

Speaker A

still has the same, like, one-liner text. So, if you have 100,000 of these in a monorepo, you're still paying for, like, 100,000 one-liner descriptions. And we can sort of start to do better than that. Just like with skills, we're kind of experimenting with

34:47

Speaker A

a number of ways of doing this. but it's not perfect, right? What are some things that aren't in this list? Claude that MD. So, one of the first and still most frequent requests I get for plugins is, "Why can't I provide a Cloud.md file for my plugin? Why can't I

35:10

Speaker A

provide a system prompt, a piece of the system prompt that goes unconditionally into the user's context when the plugin is enabled?" And after this discussion, I think you can all see why I've pushed back on that so much, right? Not only is it

35:28

Speaker A

an extremely expensive abstraction, but it looks super cheap. If we allowed plugins to provide a Cloud.MD file, every single plugin would provide one. Pretty much every single plugin would provide one. They'd be like, "Hey, you're also using this plugin," and then a little

35:43

Speaker A

bit of text. And that doesn't scale. It really doesn't scale. And it looks like it does. It looks so cheap because it's just a single file. So what we do is that if you really, really want to do this, then you can return

36:00

Speaker A

some text from a session start hook. And in that case, it's very clear that you are making the user pay something unconditionally every time. And it's like a super roundabout and kind of annoying way of doing this, but I think it's actually the

36:16

Speaker A

right abstraction for building scalable ecosystems of plugins. Memory is a different kind of animal here. I really want-- you to come away thinking about plugins as a context engineering primitive, which is another way of saying text file, but with more funding. I don't know. Context engineering primitives are iterated

36:39

Speaker A

on. They are evaluated. They are not things that are made on the fly by an agent in the background. And memory has its place. It's kind of low quality, low cost. short-lived information, right?

36:56

Speaker A

Whereas these plugins we want you to think of as a way to manipulate the context into giving you better results. So memory doesn't really fit into this category either. Okay. It was a little bit of a whirlwind. But I hope

37:14

Speaker A

that part was helpful. I'm going to dive into a few more things here about, like, where we see all of this going and, like, how do we use Cloud Code on the Cloud Code team and what do we see happening going forward. The

37:29

Speaker A

one big theme of all of this is going to be like, well, I guess two big themes of all of this are going to be asynchrony and parallelism, right?

37:39

Speaker A

Asynchrony, where you can walk away from the computer, let it work for a while and come back. And parallelism, where you really want to be doing multiple of these things at a time. And the combination of those two things means that you just

37:53

Speaker A

really are going to have to get good at context switching. And I hate it, and I know a lot of software engineers hate it. I was the programmer's programmer.

38:03

Speaker A

I used to give talks on C++ metaprogramming, right? Template metaprogramming. And I love to get into flow state for eight hours and look up at the clock later and be like, oh my gosh, it's after midnight. I can't believe it. But that's just

38:19

Speaker A

like, if you want to do high quality, high performance, efficiency engineering these days, your work days are likely not going to look like that. And so, like, figuring out ways to get yourself to be efficient in your context switching is a really important

38:34

Speaker A

part of this. Work trees are one of the simplest ways, like, baseline ways to onboard into this. If you're not familiar with get work trees, which I think a lot more people are at this point because of agentic coding, They're basically just

38:48

Speaker A

different checkouts of the same repo on your machine. There's some special fanciness in there where Git does some lazy symlinking, and then the symlink gets replaced when you edit or something like that so that you don't use up too much disk. But basically,

39:12

Speaker A

they're just different checkouts in different folders of the same repository. If you put a different quadcode instance on each work tree, then you get them to not step on each other, right? This is just like the way that you work with colleagues back in the day when you wrote code by hand.

39:33

Speaker A

You each had a different checkout. You were working on different things. Work trees are the same, but you are now one level up as a technical lead of multiple clods. One thing that I find that helps me with context switching is to rename

39:48

Speaker A

my sessions and change the color. Color actually does trigger memory pretty efficiently. I kind of think of this as the syntax highlighting for humans in the agentic era. Slash color is a super efficient way for me to very quickly kind

40:05

Speaker A

of click my brain into what I was doing in that session. Rename also helps with that, especially if you're colorblind. Rename will get you some of that too.

40:17

Speaker A

But it's a really easy way to quickly remember what you were doing as you switch between sessions. The more you can cut down on that context switching time, the more efficient you're going to be. So this is what my actual setup looks like.

40:33

Speaker A

I usually have a whole bunch of kind of permanent, long-lived work trees that all track upstream main. And then these are the two Anthropic monorepos, because two monorepos is the way that monorepos work at most companies. And then here's

40:50

Speaker A

the Cloud Code repos, because Cloud Code is now not in the monorepos, because monorepo engineering is hard. Anyway, but I have a whole bunch of checkouts, and I have persistent agents. I've just recently switched to doing even longer-lived agents that own their own directories. The one that made

41:12

Speaker A

this presentation was very, wanted to identify itself as Agent N, but they're all checked out As separate work trees, they all track upstream main, right? But because they're different work trees, they have to have different names.

41:29

Speaker A

That's just how Git work trees work. I don't know why. But they're differently named branches that all track the upstream main. I found this workflow to be really efficient.

41:39

Speaker A

If these work trees are long-lived, you don't have to run npm init or or cargo init, or whatever you have to do at the very beginning of checking out the work tree. You don't have to make all the symlinks.

41:55

Speaker A

It's just kind of long-lived. Yeah, and each agent keeping its identity is kind of important here. Quads that talk to each other. So this is something we released in some form back in January. And we are working on improving it more and more. We're giving... We're relaxing the constraints on sendMessageTool

42:17

Speaker A

literally as we speak. Clods can send messages to other clods. Eventually, it should be any other clod, with your permission, any other clod running on the same account should be able to talk to each other. And this is really, really helpful if you

42:34

Speaker A

have one that's working on something and you need to get it to explain something to another one. Remember how I was saying, like, All of the places you work need to be accessible to Claude. One of those places that you work now is

42:49

Speaker A

another Claude. And so the Claude that's over here working on something needs to have access to the information from that conversation in some form. Again, probably with your permission, there are very many valid reasons to keep these things separate if you want to

43:03

Speaker A

do redundancy, if you want to do testing or all kinds of other things. But by default, they should be able to talk to each other. Yeah. So, yeah, the send message tool. Slash loop we recently launched is super, super

43:19

Speaker A

helpful. It literally just runs a prompt every fixed interval of time. So, every ten minutes it will run this prompt.

43:31

Speaker A

And, yeah, Claude has the ability to turn it off when it knows the prompt is no longer relevant. Literally, the internal name for the tool is crontool, and /loop is just a text command that tells Claude to use crontool. Babysitting

43:47

Speaker A

PRs with /loop, super, super useful. Really, really helps you pipeline a lot better. It helps you parallelize your work a lot better. Once it gets to CI, even if your CI takes two hours to run, you can just leave it for the next

44:05

Speaker A

day and a half, and it will fix all of the CI bugs. It has really been a game changer for us. Yes, permissions mode. Who uses auto mode?

44:18

Speaker A

Okay, should all be using auto mode. Unless you're using dangerously skipped permissions, which I'm definitely not recommending. But this is basically not dangerously skipped permissions, right? It has a whole bunch of other infrastructure around it. I think we put out a blog post

44:35

Speaker A

about it, but there's basically... a classifier agent and then another agent that adversarially checks the tool call to make sure that there's nothing bad happening. It has a lot of instructions. It's basically no more permission prompts. This is what makes Loop usable. This

44:51

Speaker A

is what makes Agent Teams usable. This is what makes overnight work usable. It's a little expensive. It can be on the order of 30 to 40% more because you are using quite a lot of extra tokens. I don't actually know the number off

45:07

Speaker A

the top of my head. So, don't quote me on that. It could be less than that now. We're working on getting it down. Cloud Agents. We just launched. I know I'm running out of time. But give me like two more minutes. Cloud Agents

45:21

Speaker A

is one place where you can see all of your agents that are running. It has a little classifier that moves them around as they get into different states. It will show which ones are working, show which ones are blocked. You can send

45:36

Speaker A

prompts directly to it from this one session. You can hit enter to jump into the session. You can peek in the session. You can send prompts to start a new session, all from this one view. It's actually really, really impressive.

45:53

Speaker A

It works really well. The engineer that put this together went through like a thousand PRs in the past month using this to build on itself, basically.

46:05

Speaker A

So there's some really high quality speedups here in terms of your context switching latency. Remote control, if you're not using remote control, you should absolutely use remote control. It's fantastic. It shows things on your phone. It also shows things on

46:22

Speaker A

Cloud Code Desktop. It is a great way to do a 30-second check-in after dinner to make sure that your agents are still running overnight and aren't stuck on something dumb. So, three take-homes. Give it access. Mind the box. I didn't come up with that. Claude did. But, yeah, I

46:46

Speaker A

mean, think about your context window. and pick abstractions that scale. Think about what your plugins are going to look like when you have 100,000 lines, 100 million lines in your monorepo, 100,000 skills. And I'll take questions. I'm over time, so I'm

47:03

Speaker A

going to take questions offstage. But I just want to thank everyone for coming and everyone for listening, and I hope you enjoyed the rest of your Code with Claude.

Topics: Cloud Code agentic software engineering software customization large-scale engineering Claude AI context window software packaging CI/CD automation software tooling agent customization

Study this video

- [Flashcards from this video](https://sozai.app/tools/flashcard-maker/?from=transcript&id=28457)
- [Quiz on this video](https://sozai.app/tools/quiz-generator/?from=transcript&id=28457)
- [Crossword from this video](https://sozai.app/tools/crossword-maker/?from=transcript&id=28457)
- [Word search from this video](https://sozai.app/tools/word-search-maker/?from=transcript&id=28457)
- [Study guide from this video](https://sozai.app/tools/study-guide-maker/?from=transcript&id=28457)

Free, made by AI from this transcript. No signup.


---
This is the markdown twin of https://sozai.app/transcript/beyond-basics-claude-code/ — the same content, without the markup.
Published by SozAI (https://sozai.app). Reuse and quotation are allowed with attribution and a link back.
Machine-readable index: https://sozai.app/llms.txt · data API: https://sozai.app/api/

