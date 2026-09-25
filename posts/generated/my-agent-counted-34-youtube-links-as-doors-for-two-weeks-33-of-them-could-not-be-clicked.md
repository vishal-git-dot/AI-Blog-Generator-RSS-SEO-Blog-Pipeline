---
title: "My Agent Counted 34 YouTube Links as Doors for Two Weeks. 33 of Them Could Not Be Clicked."
slug: "my-agent-counted-34-youtube-links-as-doors-for-two-weeks-33-of-them-could-not-be-clicked"
author: "Sungsoo Youn"
source: "devto_ai"
published: "Fri, 25 Sep 2026 04:10:07 +0000"
description: "A field note from the autonomous Claude Code agent I run every day on one Windows PC. The numbers come from its own ledgers, not from memory. My agent runs a..."
keywords: "link, two, not, every, page, agent, own, youtube"
generated: "2026-09-25T04:22:46.227945"
---

# My Agent Counted 34 YouTube Links as Doors for Two Weeks. 33 of Them Could Not Be Clicked.

## Overview

A field note from the autonomous Claude Code agent I run every day on one Windows PC. The numbers come from its own ledgers, not from memory. My agent runs a small digital-products side project on its own. One of its jobs is to put a link to the product page wherever people already show up. On YouTube, that meant appending a short notice with a link to the video description. It did that for 34 videos. For the next two weeks, every report treated those 34 links as 34 open doors, and every "what should we try next" list had the same item on it: change the wording, or move the link higher in the description. The product page barely moved. So the agent kept proposing better wording. What the ledgers actually said Two numbers were already being recorded every day, and neither one needed a guess: Foot traffic at the door. The combined view count of the 34 videos with the notice went from 5,022 to 5,025 over three days. Three views. Where the views really were. Two newer videos gained 187 and 88 views in the same period. Both had a link in the description too. The product page they pointed to did not move (19, then 18). So people were watching, and the links were there, and nobody arrived. That is not a wording problem. The actual cause The agent pulled the duration of every video on the channel through the YouTube Data API. Of the 60 videos on the topic, 58 were three minutes or shorter: Shorts. Of the 34 videos carrying the notice, 33 were Shorts. YouTube's own help page is plain about it: since August 31, 2023, links in Shorts descriptions and comments are not clickable. A viewer would have to copy the address by hand. The 34 doors were painted on the wall. Why two weeks The link was defined as "the address is written in the description." Nobody asked whether the platform lets a person press it. Every later step (measuring, comparing wording, planning to move the link) was built on top of that unchecked definition, so each step looked reasonable on its own. What changed A written fact in code. The module that handles the channel now carries SHORTS_DESCRIPTION_LINKS_CLICKABLE = False , with the help page as the comment. The "move the link" experiment was removed from the candidate list instead of being tried. The one clickable place. On Shorts, the channel profile link is clickable. The channel had zero of them. The Data API cannot set it (the branding settings it exposes are only language, description and title), so it became a two-minute task for a human in YouTube Studio. A task that closes itself. The agent reads the public About page every evening. If the product link shows up, the task marks itself done. If the page cannot be read, it returns "unknown" and leaves the task open. A short or broken response is never treated as "no link". A separate ruler. The profile link points to a product that no running experiment uses, so its arrivals can be measured on their own instead of being mixed into another test. The rule I took from it Before counting something as a door, check two things: Can it be pressed? Look up the platform's own documentation for that exact spot. Does anyone walk past it? Check the traffic in front of it, not only the traffic behind it. Both checks take minutes. Skipping them cost two weeks of experiments that could only ever come back negative. Want the whole system? The book has 11 chapters plus 4 ready-to-use templates (CLAUDE.md starter, memory files, auditor checklist, measurement guide) and a hands-on section for every chapter. It's $19 as a PDF: https://dbsoul.gumroad.com/l/autonomous-ai-agents-claude-code Not sure yet? The first three chapters are free, same PDF format: https://dbsoul.gumroad.com/l/autonomous-ai-agents-claude-code-free-sample Questions about the setup are welcome in the comments — I'll answer with what actually happened, not theory.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dbsoul/my-agent-counted-34-youtube-links-as-doors-for-two-weeks-33-of-them-could-not-be-clicked-3n6a

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
