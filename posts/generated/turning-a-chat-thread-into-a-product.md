---
title: "Turning a Chat Thread into a Product"
slug: "turning-a-chat-thread-into-a-product"
author: "John Polacek"
source: "devto_ai"
published: "Tue, 11 Aug 2026 13:06:00 +0000"
description: "ShowReco started as a chat thread. I was trying to find movies and shows to watch that weren't just the same old junk that streaming platforms kept recommend..."
keywords: "profile, you, every, model, showreco, one, your, chat"
generated: "2026-08-11T13:17:02.102016"
---

# Turning a Chat Thread into a Product

## Overview

ShowReco started as a chat thread. I was trying to find movies and shows to watch that weren't just the same old junk that streaming platforms kept recommending. It worked really well, you can see the chat here for yourself. The problem with a chat thread is it eventually runs out of context. It forgets everything I told it. All the ratings, and the nuance of everything we discussed gets lost. So I built the chat thread into a product. The Taste Profile I worked on the memory system first. Every 5 ratings the app re-reads everything you've rated and rewrites a profile document: one sentence that sums you up, the ways you differ from other fans of the same genres, your lanes, your turn-offs, your dealbreakers. The model rewrites its own memory, but there are guards on it. It snapshots the old profile before every rewrite. It can add nuance but it can't delete an established lane on little evidence. The first real bug was a queue of 29 dramas. I had rated about nine things, most of them drama, so the profile over prioritized. The generator was told to ground every pick in the profile, so it read "not in the profile" as "exclude everything not in this narrow lane for this user". The adjustment was to have the profile assess its own confidence now and enforce that a genre you were never shown is unknown, not rejected. The model is encouraged to ask for ratings on content where it lacks info. Asking Better Questions Getting the app to ask me things to figure out my taste was the key. Most people like The Bear , so a good rating tells you almost nothing. On ShowReco, every rating is lined up against the IMDb score instead, and when the gap hits 1.5 the app opens a conversation about why. That's the good stuff. There are still always going to be gotchas. A real user (me) had rated five horror titles, but somehow with horror appearing nowhere in my profile. Every rating had been filed under a lane with no genre in the name, the lane list was full, yada yada. The bug was that it was never going to ask about or recommend a horror movie or show because of this. So we did a second probe. It finds a genre your ratings are loud about and your profile is silent about, has the model write the question, picks titles to settle it, and requires the next profile rewrite to answer. Working With the Agent I built almost all of ShowReco with a coding agent, much of it on my phone, shipped to production, and tested it myself. A tight feedback loop that was both fun and effective. A model's training data is older than your project. It will write confidently against the version of a library it learned instead of the one you installed. A rule at the top of my AGENTS.md is to read the real docs for the actual version before writing any code. That one line takes out a whole category of confident wrong answers. For anything bigger than a small change we write a plan into a markdown first, starting with the real data from production, and I read the plan instead of the diff. Use the smartest model you have as the orchestrator and let it hand building to others. Fable holds the plan and reviews what comes back, and it spins up Opus and Sonnet subagents to do the implementation. Two things I never had to ask for. It comments as it goes, and the comments are nearly all why rather than what, which matters because the next session has no memory of the evening that produced some odd looking guard clause. It also writes tests (there are 806 of them now). Simple Auth and Users Just use Clerk . Don't overthink. Flat-File Databases There is no database. Every user is a folder of JSON files in S3. Again, keep it simple. If you don't need realtime, store data in S3. Cheap. Reliable. Fast. For ShowReco, reading your taste profile is one GET. Writing it is one PUT, conditional on the S3 ETag (so if two things hit the same file at once the loser retries instead of overwriting). This works because everything is scoped to one person. Nothing in the app queries across users. If I needed leaderboards or search this would be a bad idea. Then I'd probably reach for Convex . Tracking Every Token Every model call writes its token counts to a usage file, split by day, by operation, and by model. Chat, queue rebuild, profile distill, calibration, web search, all counted separately. I put that in early, before I needed it. A great decision. When it comes to price, don't guess. Track everything. Knowing cost per operation can shape a free tier around real numbers. For ShowReco, rating is unlimited because it is virtually free. Queue rebuilds run on the cheap model until a profile has enough signal to be worth the expensive one, which is also what makes every new signup cheap to serve (my first seven signups cost between 0.8 and 7.7 cents each, median about 2 cents). Admin Panel I have admin pages (protected routes just for me) with analytics, funnel, retention, attribution, finance, user activity, etc. There is nothing about this app I can't go look up and figure out how to make better. I would never have hand built all these admin pages for a product with so few users, but it's just so damn easy and useful. Will ShowReco grow? I don't know. I built an app to serve my own needs and that was fun. Not too worried about it! I am shipping features to make it better all the time. Give it a try at showreco.com and tell me what it gets wrong about you!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/johnpolacek/turning-a-chat-thread-into-a-product-p95

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
