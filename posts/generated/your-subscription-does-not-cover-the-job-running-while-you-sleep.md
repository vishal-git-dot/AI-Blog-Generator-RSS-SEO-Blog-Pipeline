---
title: "Your subscription does not cover the job running while you sleep"
slug: "your-subscription-does-not-cover-the-job-running-while-you-sleep"
author: "Mirza Iqbal"
source: "devto_ai"
published: "Wed, 01 Jul 2026 14:39:37 +0000"
description: "The first messages came in overnight. I did not read them until breakfast. By then it was message after message, the same error text, from an automation I ha..."
keywords: "you, not, background, one, job, your, did, had"
generated: "2026-07-01T14:48:11.182813"
---

# Your subscription does not cover the job running while you sleep

## Overview

The first messages came in overnight. I did not read them until breakfast. By then it was message after message, the same error text, from an automation I had wired up myself. It had been talking to itself all night while I slept. Each of those messages was a background call to my coding agent. The automation read a notification, answered it, produced a new notification, then answered that one too. It fed itself until it hit a hard usage gate and started texting me the failure, again and again, until morning. I built that. Nobody handed me a broken system. I wired a small helper, walked away, and it turned into a machine whose only job by 2 in the morning was to fail loudly and repeatedly. If you have ever pointed a cron job, a webhook, or a background worker at an AI CLI, this is your story too. You will not see it coming, because the thing that runs up the cost is never the thing you are watching. You are watching the demo on your screen. The bill is being written by the process you forgot about. The part that changed everything Here is what stings. When I first lived this loop, it had no dollar cost. It slammed into a wall and stopped. Annoying, embarrassing, free. Then on 15 June the ground moved under all of us. Anthropic split background, headless usage into a separate metered pool that sits outside the flat subscription. The exact pattern I had already survived once, a background job reaching for the headless mode, stopped being covered by the plan I pay for and started drawing real, metered money. So the failure I thought I had closed came back wearing a price tag. That is the part worth sitting with. The pattern did not change. The economics under it did. The claim I will defend A Pro or Max subscription does not protect you the moment a background process reaches for the headless mode. The flat price covers you sitting at the keyboard, prompting, reading, correcting. It was never designed to cover a loop running at full speed without a human in the room. Most people read the plan name and assume a cap. There is a cap on the interactive part. The background part meters. The five shapes that do this After I traced mine, I went looking for the shapes that quietly run up an AI bill. Five come up again and again, and every one of them is something you would wave through in review because in isolation it looks harmless. The self-triggering loop. A background job reads an event, acts on it, and its own action produces a new event it then reads again. Left alone it feeds itself. Mine was answering its own error notifications, which produced more errors to answer. The retry storm. A transient failure, a 401, a timeout, a rate cap, gets retried with no limit. The call that failed for free once is not free when it runs in a tight loop. A backoff is one of those things everyone agrees with and nobody wires in until after it has bitten them. The parallel fan-out. You ask for a batch, the worker spawns one AI call per item, and a list you thought was small becomes a spend multiplier you never priced. Ten items is a rounding error. Ten thousand is a surprise invoice. The forgotten cron. The automation you set up months ago, before the billing changed underneath it, keeps running on the old assumption that the calls are covered. The assumption expired. The cron did not. Nobody told it the rules moved. The small-job blind spot. It is one line. It runs every few minutes. It feels too tiny to matter. Tiny, multiplied by a thousand runs a day, multiplied by a metered pool, stops being tiny. None of these is exotic. That is exactly why they slip through. Each one looks reasonable on its own, and the danger only shows up when it runs unattended, at speed, against a meter. What actually fixes it The fix is not a smarter prompt. The prompt was never the problem. The fix is a guard at the process boundary, the exact place where a background job is about to reach for the paid mode. I know this because I had already written that guard, tested it, and told other people to use it. And my own older automation, the one I forgot to bring under it, ran right past everything until morning. Knowing the failure mode did not save me. Wiring the guard into the one place I forgot did. So here is the reframe that stuck with me. You already review your code for correctness. You read a diff and ask whether it will break. Start reading your automations the same way, and ask a different question. What does this cost when it runs a thousand times without me watching. That question would have saved my night. It is the one I now ask before any background job is allowed near a paid call. Your turn What is the one background job you have running right now that you have not looked at since the billing changed? If this was useful I work through this in public, the wins and the freezes both, mostly on LinkedIn and YouTube . If the real version of building in the open is useful to you, that is where it lives. Find me on X , GitHub , and the work at next8n.com .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mjmirza/your-subscription-does-not-cover-the-job-running-while-you-sleep-hie

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
