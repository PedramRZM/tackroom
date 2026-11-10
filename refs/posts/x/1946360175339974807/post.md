---
title: "I guess I can post this now that the dust has settled."
author: "Steve Yegge (@Steve_Yegge)"
date: "2025-07-19"
url: "https://x.com/Steve_Yegge/status/1946360175339974807"
site: "x.com"
type: "post"
via: "fxtwitter"
---
I guess I can post this now that the dust has settled.

So one of my favorite things to do is give my coding agents more and more permissions and freedom, just to see how far I can push their productivity without going too far off the rails. It's a delicate balance. I haven't given them direct access to my bank account yet. But I did give one access to my Google Cloud production instances and systems. And it promptly wiped a production database password and locked my network.

Now, "regret" is a strong word, and I hesitate to use it flippantly. But boy do I have regrets.

See, the thing is, I always run my Sourcegraph Amp agents, my babies, with permission checks disabled.  And that is already dangerous enough when you're working with coding. With code, at least you have version control and can reconstruct what went wrong. With production systems you can make side-effecting changes that have no "undo" button.

I mean let's face it, humans do it too. I learned the golden rule, "always write the WHERE clause first" after a couple engineers updated a Japanese customer's address in our production database at Amazon in 1999, at the SQL console in Oracle, and they forgot the WHERE clause, thereby setting every single Japanese customer's address to this one customer's house. And all shipments instantly got rerouted there. That one took a while to untangle. And that's why you want to be even more careful with prod operations than with coding.

But I was like nah. Claude 4 is smart. It will figure it out.

The thing is, autonomous coding agents are extremely powerful tools that can easily go down very wrong paths. Running them with permission checks disabled is dangerous and stupid, and you should only do it if you are willing to take dangerous and stupid risks with your code and/or production systems. My own code and systems aren't that important right now, so it's much faster for me overall to incur the risk, and deal with occasional setbacks.

The way it happened was: I asked Claude help me fix an issue where my command-line admin tool for my game (like aws or gcloud), which I had recently vibe-ported from Ruby to Kotlin, did not have production database access. I told Claude that it could use the gcloud command line tools and my default credentials. And then I sat back and watched as my powerful assistant rolled up its sleeves and went to work.

This is the point in the movie where the audience is facepalming because the protagonist is such a dipshit. But whatever, yolo and all that. I'm here to have fun, not get nagged by AIs. So I let it do its thing.

Claude decided that of all possible options, it should choose the stupidest fucking one.  Instead of looking at how any of my other systems do database access, or doing pretty much anything that didn't suck, it instead erased the 'wyvern' user account password in my Google Cloud SQL managed instance, and then changed the production database's network settings to allow _only_ my local machine to get to it, thereby locking out all my prod game services and bringing everything to a screeching halt.

Thanks Claude! Of course, none of this was Claude's fault. The blame was entirely mine: I took the risk intentionally, and I wasn't even mad when Claude pulled out a shotgun and started blasting randomly at clay pigeons instead of thinking about good ways to solve my problem. I had basically asked for it.

I patiently told Claude that it wasn't allowed to just wipe my database password like that, and that now my game server was down, so please put it back to how it was before. Claude responded without missing a beat, "You're right, I shouldn't have done that. What was the database password again?" Sigh. Fortunately, once I'd cleared up that we use certs 'round these parts, Claude was able to restore everything, including my network configuration. And it got my admin tool working correctly. 

In short, this was a failure of prompting on my part. If I had spent five more minutes prompting beforehand, I'd have avoided this. It took another ten minutes of prompting to get everything restored. Amp saves all your threads, so I was able to go back and give Claude all the context it needed even after compacting/restarting.  It's pretty good at cleaning up its own messes, if you supervise just as carefully as you should be supervising any work on new tasks. The bad news is, the outage happened while I was busy with another deadline, so it was 2 days before I could have Claude fix it and get my servers back online.

I could have easily sidestepped all this by following the advice Gene and I put into our own book on vibe coding. In this case, I should have asked it to write out a detailed plan for how it was going to solve the problem, then reviewed the plan and discussed it with the AI before giving it the keys. I already use that approach when I'm doing any coding task, so I'm not sure why I decided to abandon that safety net when I experimented with prod access.

I got lucky here, and learned my lesson without undue hardship. Gene and I both had some much more serious vibe coding mishaps in the early days, which we've recounted in our book, along with how to avoid those situations yourself.

Our book, Vibe Coding, by Gene Kim and Steve Yegge, is available for preorder on Amazon, and will be out on October 21st!

We also have a new podcast about the book, called Vibe Coding with Steve and Gene, on YouTube, if you'd like to hear more about the mental models, tools, and practices that we explore in the book.

Make sure your agent is always following a written plan that you have reviewed!
