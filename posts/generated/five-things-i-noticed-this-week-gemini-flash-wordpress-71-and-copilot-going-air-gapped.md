---
title: "Five things I noticed this week: Gemini Flash, WordPress 7.1, and Copilot going air-gapped"
slug: "five-things-i-noticed-this-week-gemini-flash-wordpress-71-and-copilot-going-air-gapped"
author: "MORINAGA"
source: "devto_webdev"
published: "Sat, 15 Aug 2026 06:19:38 +0000"
description: "Five things I noticed this week running content automation, three directory sites, and a cross-publish pipeline in parallel. Roughly in order of what I expec..."
keywords: "gemini, flash, copilot, running, three, publish, week, wordpress"
generated: "2026-08-15T06:47:15.232296"
---

# Five things I noticed this week: Gemini Flash, WordPress 7.1, and Copilot going air-gapped

## Overview

Five things I noticed this week running content automation, three directory sites, and a cross-publish pipeline in parallel. Roughly in order of what I expect to still matter in three months. 1. Gemini 3.7 Flash dropped while Gemini 3.5 Pro is still delayed Google released Gemini 3.7 Flash on August 13 — three weeks after 3.6 Flash. The benchmark number that caught my attention: 65.3% on DeepSWE v1.1, up from 49.0% on the prior version. That's a 16-point jump in a single-model coding eval in three weeks. Introductory pricing is $0.75 per 1M input tokens and $3.75 per 1M output through December 31, 2026, doubling on January 1. The Bloomberg framing was blunter: this shipped while Gemini 3.5 Pro is still not out. The Flash series is doing the work Google presumably wanted the Pro series to be doing. For my current stack I'm still on Claude Haiku for ETL — cost and latency are the deciding factors there. But Gemini Flash at this pricing is competitive for lightweight inference tasks where I'm paying per call rather than per seat. 2. WordPress 7.1 makes responsive styling a first-class editor concept WordPress 7.1 RC1 published last week with 145 fixes (57 in Editor, 88 in Core) and a final release scheduled for August 19 at WordCamp US in Phoenix. The feature worth understanding: responsive styling and interactive states — hover, focus, active — are now editor controls, not custom CSS. That removes an entire category of "write a block, then write breakpoint CSS to make it work on mobile" friction. I'm not running WordPress; all three sites are Astro SSG. But this matters indirectly. When WordPress makes something an editor control, the population of non-developers who can manage it without touching code grows substantially. Features that start as developer-only conventions in frameworks tend to follow the same path toward higher-level abstractions, and it's useful to see where that frontier currently sits. 3. GitHub GHES 3.22 takes Copilot CLI into air-gapped environments GitHub published the GHES 3.22 release candidate on August 11. The headline: Copilot CLI now works in disconnected, air-gapped enterprise installs, as a technical preview. Enterprise Teams — unified user and access management across all organizations — graduated to generally available in the same release. The air-gapped detail is the strategically interesting part. Cursor and Claude Code require internet access; they cannot follow code into regulated environments where outbound connectivity is blocked. GitHub is threading that gap by embedding Copilot into the self-hostable layer. If that pattern holds, the enterprise AI coding market in regulated sectors — finance, defense, healthcare — looks more like GitHub Copilot by default than any cloud-native tool. Whether air-gapped performance matches the cloud version is a question that only people inside those environments can actually answer. 4. Running two AI coding tools simultaneously stopped feeling unusual Multiple sources I read this week described the same two-tool pattern independently: Cursor for moment-to-moment coding flow, Claude Code for "big jobs" — extended refactors, multi-file investigations, spec-driven scaffolding. The pattern is common enough now to anchor articles explaining the division of labor. What I find notable isn't the tools themselves. Six months ago "which AI coding tool should I use" was the framing. The framing that shows up now is "which layer is this task for" — as if the category has stratified into complementary functions. That's a meaningful shift in how practitioners think about the space, and it happened quietly without anyone formally declaring that the competition phase was over. 5. Post-publish truth patrol is showing up in my commit history Six commits this week started with fix(corrections) or fix(truth) , all triggered by Codex review flagging claims in articles that couldn't be verified or were outright wrong. One example: a regex that ate YouTube video IDs in a correction pass. Another: an article asserting a sale-date range I couldn't actually support with data I had on hand. I didn't design post-publish truth patrol into the pipeline. The Codex review loop was added for pre-publish quality checks. It's now running corrections on published work and surfacing them as P2 findings. This week's correction cadence suggests the loop is catching drift that pre-publish checks missed — probably because some claims were supportable at write time and then became unsupportable as underlying data changed. Running a truth system that outlives the initial publish is different from running one that only fires before publication. I don't know yet whether this is a feature or evidence that the pre-publish pass isn't tight enough. Sources and further reading: Gemini 3.7 Flash launch post — Google's announcement with benchmark numbers 9to5Google: Gemini 3.7 Flash launches three weeks after last model — timeline and context GitHub GHES 3.22 release candidate — official changelog with air-gapped Copilot details WordPress 7.1 Release Candidate 1 — features and fixes list Gemini 3.7 Flash now in GitHub Copilot — same-day availability note Part of an ongoing 6-month experiment running three AI-curated directory sites. The technical claims here are real; this article was AI-assisted.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/morinaga/five-things-i-noticed-this-week-gemini-flash-wordpress-71-and-copilot-going-air-gapped-3hfo

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
