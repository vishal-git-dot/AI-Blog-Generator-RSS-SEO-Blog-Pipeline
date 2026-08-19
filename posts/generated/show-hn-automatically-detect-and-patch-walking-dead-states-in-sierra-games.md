---
title: "Show HN: Automatically detect and patch walking-dead states in Sierra games"
slug: "show-hn-automatically-detect-and-patch-walking-dead-states-in-sierra-games"
author: "wkfauna"
source: "hackernews"
published: "Wed, 19 Aug 2026 01:58:33 +0000"
description: "Hi HN, I've become lazier in my old age and struggle to replay my favorite Sierra games from the 80s and 90s because I keep getting into those situations whe..."
keywords: "game, sierra, automatically, states, those, you, king, quest"
generated: "2026-08-19T06:52:53.078582"
---

# Show HN: Automatically detect and patch walking-dead states in Sierra games

## Overview

Hi HN, I've become lazier in my old age and struggle to replay my favorite Sierra games from the 80s and 90s because I keep getting into those situations where I need an item from 3 acts ago, I have no save game handy, and now I gotta make dinner. So I'm building the Lucasartsifier: a static analysis tool that decompiles Sierra resource files, automatically finds those states, automatically generates code to prevent the player from getting into those states, then emits loose patch files that can be placed alongside the original game resources. There's no game-specific code involved; all the logic is generic, though of course Sierra introduces new idioms and mechanics in every game so every new supported game needs a bunch of engine work. So for example in Leisure Suit Larry 2, the patched game prevents you from boarding the cruise ship until you have both the sunscreen and the Grotesque Gulp. Without them you die on the raft 3 play-hours later. So far this works on Leisure Suit Larry 2 (SCI0), King's Quest 4 (SCI0), King's Quest 6 (SCI1.1), and Laura Bow 2 (SCI1.1). I'm currently working on King's Quest 5 (SCI1.0). This is work done with Claude -- I do the design and playtesting and it does the rest :D Any feedback, play testing, and suggestions would be great! Comments URL: https://news.ycombinator.com/item?id=49355607 Points: 30 # Comments: 12

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://github.com/katiahayati/lucasartsifier/

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
