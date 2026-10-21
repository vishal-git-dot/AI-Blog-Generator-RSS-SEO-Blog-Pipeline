---
title: "The Dimension That Predicts Downloads Is Not the One We Rank Highest"
slug: "the-dimension-that-predicts-downloads-is-not-the-one-we-rank-highest"
author: "SKILL123.me"
source: "devto_ai"
published: "Wed, 21 Oct 2026 16:51:02 +0000"
description: "Our rubric says trigger quality is the thing that decides whether a skill is used. The download data says something different. Each of the six dimensions in ..."
keywords: "not, trigger, quality, skill, download, structure, downloads, have"
generated: "2026-10-21T16:57:15.640213"
---

# The Dimension That Predicts Downloads Is Not the One We Rank Highest

## Overview

Our rubric says trigger quality is the thing that decides whether a skill is used. The download data says something different. Each of the six dimensions in our rubric was correlated against download counts across 591 fully-evaluated skills: Dimension Weight Correlation with downloads Structure 15% 0.56 Content 10% 0.52 Engineering 10% 0.50 Security 20% 0.42 Workflow design 25% 0.27 Trigger quality 20% 0.15 Trigger quality — the dimension we have argued is the single most important thing in a skill, and the one we have written about most — is the weakest predictor of whether anyone downloads the skill . Two explanations, and both are probably partly true Explanation one: the measurement is downstream of discovery. A trigger fires inside an agent, after the skill is already installed. Downloads happen at the moment of discovery, when a person is looking at a page, a list, or a description. Structure and content are exactly what you can evaluate at that moment — is this a clean package, does it have real instructions, does it look maintained. Trigger quality is invisible until after installation. If that is right, the download number is measuring conversion at the point of decision , not value in use . Trigger quality would show up in a different metric — whether the skill fires when it should — which we do not currently track in production. Explanation two: the downloads are not human. As with every download-based analysis on this site, automated clients are a large share of the number. A bot downloading a directory does not evaluate triggers, but the packaging signals — a clean file tree, a reasonable size — may correlate with whatever list the bot is following. That would inflate structure and content mechanically. We cannot separate these two with the data we have. What we can say is that the trigger-quality argument should not be sold on download numbers, and we should stop implying it is. The structure number is the interesting one Structure at 0.56 is the strongest signal in the table, and structure is the dimension with the widest spread between top and median skills (2.64 points, versus 0.46 for security). It is also the cheapest to fix: a lean SKILL.md with details pushed into references/ , scripts in scripts/ , templates in assets/ . If you accept even half of that correlation as real, then for a skill author the highest-return change is not rewriting the description — it is splitting a 900-line file into the layout the agent can actually load selectively. What would settle it The measurement we are missing is activation rate in production : of the sessions where a skill is installed, how often does it fire when the user's request matches? That number would test the trigger-quality thesis directly, without the download confound. We do not have it yet. When we do, this post gets rewritten. Until then, the honest summary is: we rank trigger quality highest for a reason we believe in, but our own adoption data does not support it. That is worth saying out loud rather than quietly leaving the correlation out of the analysis.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/skill123/the-dimension-that-predicts-downloads-is-not-the-one-we-rank-highest-4hbo

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
