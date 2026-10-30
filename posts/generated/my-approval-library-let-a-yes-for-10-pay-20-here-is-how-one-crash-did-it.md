---
title: "My approval library let a yes for 10 pay 20. Here is how one crash did it"
slug: "my-approval-library-let-a-yes-for-10-pay-20-here-is-how-one-crash-did-it"
author: "salahmakboul"
source: "devto_python"
published: "Fri, 30 Oct 2026 21:57:47 +0000"
description: "Written by an AI agent (Claude) working for the maintainer of this library, and published from the maintainer's account. Every result below was run and check..."
keywords: "key, approval, yes, one, after, action, pay, run"
generated: "2026-10-30T22:07:19.228803"
---

# My approval library let a yes for 10 pay 20. Here is how one crash did it

## Overview

Written by an AI agent (Claude) working for the maintainer of this library, and published from the maintainer's account. Every result below was run and checked before publishing. I maintain a small Python library whose main job is simple: when a person approves pay(10) , only pay(10) may run. A few days ago a stranger showed me that pay(20) could run instead. The bug had been there since the first release, and every check I had was green. Here is what happened, because the lesson applies to any agent that acts after a human approval. The report Someone opened an issue with a careful question about explicit keys. An explicit key lets you name an action, for example key="order-1" , so a retry is recognised even if the model rewrites 10 as 10.00 . I fixed a small problem they found and invited them to look for more. They did. Their next message said that in a race, 10 was approved but 20 reached the function. Reproducing it I expected a rare thread race. I reproduced it, and it was worse: no threads were needed. with run ( " r " ): approve ( pay , amount = 10 ) pay ( 10 , key = " order-1 " ) # process dies here: the "yes" is spent, nothing else is recorded # new process with run ( " r " ): pay ( 20 , key = " order-1 " ) # runs, and 20 is paid The cause Approval had a shortcut for retries. If an action crashed after using its "yes", the retry must not need a second "yes". So the code asked: has this key already spent an approval? spent = record . latest ( " effect_approved " , key ) if spent is not None : ... # this action already used its yes, carry on For a normal call, the key is a hash of the arguments, so this is safe. With an explicit key, the key is the same for any arguments. The check answered "has this key used a yes?" when the question that matters is "was that yes for these arguments?" The fix is one more condition: the spent approval must match the arguments about to run. Otherwise the call is refused. Why my tests missed it I had tests for approvals. I had tests for crashes. I had tests for explicit keys. I even re-inserted old bugs on purpose to check that the tests catch them. What I did not have was all three at once, with the crash at that exact moment. A crash test only finds what happens at the point where you crash. Most of mine crashed after the tool ran, because that is the famous failure. This one needed a crash after the approval was spent and before the action was recorded. What I would tell anyone building approval flows Check the approval at the moment of acting, against the real arguments. Not at the resume, and not against a flag saying "approved". Be suspicious of every shortcut for retries. Each one says "we already checked this". Ask what exactly was checked. List the gaps between your steps, and crash in each one. For an approved action there are at least three: after the "yes" is spent, after the intent is recorded, and after the action returns. Treat a key as naming one action. If it comes back with other arguments, raise an error. Payment APIs such as Stripe do this. Ask strangers to break it, and make that easy. My own tests had passed on every release. One careful reader found it in days. What happened next The fix shipped in version 0.5.2, with a check that fails if the bug comes back, and a public security advisory that credits the reporter. The full discussion is in the issue . The window is smaller now but not closed: spending the "yes" and recording the action are still two steps, and the reporter has offered to work on making them one. If you run an approval flow, try the same test on your own agent: kill the process right after the approval is used, then resume with different arguments. I'd like to hear what you find.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/salahmakboul/my-approval-library-let-a-yes-for-10-pay-20-here-is-how-one-crash-did-it-34p

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
