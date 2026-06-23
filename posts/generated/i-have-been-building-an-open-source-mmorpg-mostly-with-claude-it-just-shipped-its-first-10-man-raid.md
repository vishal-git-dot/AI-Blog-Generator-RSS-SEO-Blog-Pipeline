---
title: "I have been building an open-source MMORPG mostly with Claude. It just shipped its first 10-man raid"
slug: "i-have-been-building-an-open-source-mmorpg-mostly-with-claude-it-just-shipped-its-first-10-man-raid"
author: "WorldofClaudecraft"
source: "devto_webdev"
published: "Tue, 23 Jun 2026 04:00:00 +0000"
description: "World of Claudecraft is a free, browser-based MMORPG. No download, no signup wall, you open a tab and you are in. It is open source, and most of it has been ..."
keywords: "you, not, have, open, just, first, raid, has"
generated: "2026-06-23T04:02:13.418911"
---

# I have been building an open-source MMORPG mostly with Claude. It just shipped its first 10-man raid

## Overview

World of Claudecraft is a free, browser-based MMORPG. No download, no signup wall, you open a tab and you are in. It is open source, and most of it has been built by working alongside Claude rather than writing every line by hand. I started it partly to see how far that approach could actually go. An MMORPG is a bad first choice for a solo project. Persistent server, real-time combat, an item system, zones, quests, party logic, all of it at once. The usual advice is that one person should not attempt this. That was most of the appeal. What I did not expect was how much the hard part stayed exactly where it always was. The AI moved the bottleneck, it did not remove it. Generating a combat function is fast. Working out why loot felt wrong in a 10-man group is not. A concrete example from this release. We just shipped v0.12.0, which adds Nythraxis, the first 10-man raid. On the first few test runs, loot was quietly broken for half the raid. The cause was a single constant. PARTY_MAX was still hardcoded to 5 from the old dungeon code, so the loot engine never accounted for players six through ten. No error, no crash, just five people wondering where their drops went. That is the kind of bug no amount of fast code generation saves you from. You still have to hold the whole system in your head. A few things I have taken from it so far: -Scope is still the enemy, not implementation speed. Typing faster just means you reach the genuinely hard design questions sooner. -Open source changed how I build. Knowing the repo is public keeps me honest about legibility, which has caught more than one lazy decision. -Shipping content on a cadence, zones then dungeons then a raid, keeps the thing alive in a way a single big launch never would have. It is live now on the Claudemoon realm if you want to poke at it, and the repo is public too. Happy to go deep in the comments, the combat model and the content pipeline are the parts people usually ask about. A question for other builders here. For those of you leaning on AI heavily in your stack, where has it actually moved your bottleneck, and where has it left it completely untouched? I am increasingly convinced the honest answer to the second part is "everywhere that matters", but I would like to be proven wrong.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/woclaudecraft/i-have-been-building-an-open-source-mmorpg-mostly-with-claude-it-just-shipped-its-first-10-man-raid-59k1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
