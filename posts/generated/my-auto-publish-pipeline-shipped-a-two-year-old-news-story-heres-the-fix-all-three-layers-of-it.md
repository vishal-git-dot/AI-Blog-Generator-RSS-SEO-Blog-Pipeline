---
title: "My Auto-Publish Pipeline Shipped a Two-Year-Old News Story. Here's the Fix — All Three Layers of It."
slug: "my-auto-publish-pipeline-shipped-a-two-year-old-news-story-heres-the-fix-all-three-layers-of-it"
author: "Jennifer Smith"
source: "devto_ai"
published: "Thu, 30 Jul 2026 19:39:23 +0000"
description: "I run a content pipeline that finds industry news, has an LLM judge score it, and publishes what clears the bar. Fully automated, Cloudflare Workers and D1, ..."
keywords: "one, you, check, story, content, judge, two, news"
generated: "2026-07-30T19:40:47.701968"
---

# My Auto-Publish Pipeline Shipped a Two-Year-Old News Story. Here's the Fix — All Three Layers of It.

## Overview

I run a content pipeline that finds industry news, has an LLM judge score it, and publishes what clears the bar. Fully automated, Cloudflare Workers and D1, one operator: me. It runs daily and the whole point is that I don't babysit it. In July it published a news story from 2024 as if it had just happened. Nobody was harmed. One item, niche site, caught on a routine quality check within a few days, unpublished. But "the robot posted two-year-old news and nothing stopped it" is the kind of failure that quietly costs a site its credibility, and it deserved a real postmortem instead of a shrug. What went wrong turned out to be more interesting than I expected, and the fix ended up being three layers instead of the one I planned to write. What actually went wrong The pipeline already had two mechanisms that should have caught this. There was a recency check. But when I built it, the stale-content problem I was seeing was old product releases resurfacing on aggregator sites. So the year-sanity check ran against product items. News items took a different path through the gate and never met it. The check had no bug. It was standing at the wrong door. There was an LLM judge. It scores every item before publication: relevant? interesting? worth the reader's time? It read the 2024 story and scored it well — because the story was relevant and interesting. I had never asked the judge whether the story was current. That question wasn't in the rubric, so it wasn't asked. A human editor has a reflexive "hang on, when is this from?" An LLM judge has exactly the reflexes you wrote down and none you didn't. Upstream, an aggregator had resurfaced the old story with a fresh feed timestamp. Everything downstream took the feed's word for it. Two guards, both working as designed, both blind to this one. The fix My first draft of the fix was one line: extend the year check to news items. Done, ship it. I've shipped enough one-line fixes to know that the incident you just had is rarely the exact incident you'll have next, so it became three thinner layers instead. Each one covers a different way the other two fail. Layer 1: widen the deterministic check. The year-sanity check now runs against every content type that passes the gate, not just the type that misbehaved historically. When a deterministic guard misses, check its scope before its logic — in my experience the case almost always walked around the guard, not through it. Layer 2: put recency in the judge's rubric. The judge now explicitly evaluates currency: when did this event happen, does its age undermine its value, penalize items whose event date sits far behind the feed date. This is the layer that catches what rules can't express. It only works for dimensions you remember to name. Rubrics are like tests that way — they encode the failures you've already imagined, and nothing else. Layer 3: extract the event date from the content itself. This one goes at the root cause: trusting upstream metadata. A resurfaced story arrives wearing a fresh timestamp; the packaging lies even when the content doesn't. The pipeline now tries to pull the actual event date out of the item's text and compares it to the feed's claimed freshness. Disagreement gets flagged for me instead of published. It's also the flakiest of the three layers — date extraction from prose fails in fun ways — which is exactly why the two blunter layers stand in front of it. Any one of these would have caught July's incident. I've watched each kind of layer fail before, though: deterministic checks miss on scope, judges miss on rubric gaps, extraction misses on weird input. So it's all three. What I'd tell anyone running auto-publish Your failure modes are public. A bad batch job embarrasses you in a log file. A bad publish embarrasses you in front of readers. Budget your quality-gate effort by audience size, not code size. LLM judges have no instincts. Every implicit check a human editor does for free has to be written into the rubric explicitly. The judge will hand out perfect scores along every axis you specified while the item fails one you didn't. Don't trust a timestamp you didn't compute. Feed metadata describes the feed's behavior, not the content's age. If freshness matters, derive it from the content. The item came down, the three layers shipped the same week, and the pipeline went back to running unattended — which is the whole point. One person can run automated publishing. The tax is that every incident has to buy a structural fix, not a patch for the instance. Patch the instance and you've just scheduled the next one.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jenatechio/my-auto-publish-pipeline-shipped-a-two-year-old-news-story-heres-the-fix-all-three-layers-of-it-4750

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
