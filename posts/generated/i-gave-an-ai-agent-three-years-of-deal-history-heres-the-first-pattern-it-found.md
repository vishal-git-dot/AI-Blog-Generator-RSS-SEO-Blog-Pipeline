---
title: "I Gave an AI Agent Three Years of Deal History. Here's the First Pattern It Found."
slug: "i-gave-an-ai-agent-three-years-of-deal-history-heres-the-first-pattern-it-found"
author: "Alex Boissonneault"
source: "devto_python"
published: "Thu, 15 Oct 2026 19:45:54 +0000"
description: "I connected Claude to a client's HubSpot pipeline through our MCP server, gave it three years of closed deal history, and asked one open question: "what shou..."
keywords: "stage, what, agent, question, deals, you, deal, than"
generated: "2026-10-15T21:09:19.876827"
---

# I Gave an AI Agent Three Years of Deal History. Here's the First Pattern It Found.

## Overview

I connected Claude to a client's HubSpot pipeline through our MCP server, gave it three years of closed deal history, and asked one open question: "what should I be worried about in this pipeline that isn't in the current dashboard." No leading question, no hint at what I already suspected. The first thing it flagged wasn't a number. It was a stage. What it actually found It noticed that a disproportionate share of deals that eventually closed had spent an unusually long stretch sitting in the same middle stage before moving, and that deals which spent longer than that stretch in that stage were far more likely to eventually go to Closed Lost than the ones that moved through quickly. Not "deals in this stage are risky," which is a fact you could get from a funnel chart. The specific claim was: time spent in this one stage , past a certain point, predicted the outcome better than any other single field in the record, including deal size and sales rep. That's a pattern a dashboard built to show funnel counts by stage will never surface, because a funnel chart answers "how many deals are in each stage right now," not "how long has each deal individually been sitting there, and does that duration itself carry signal." The agent wasn't running a smarter query, it was asking a different question of the same data. Why an agent finds this and a saved report doesn't A saved dashboard answers the question it was built to answer, forever, until someone rebuilds it. An agent with read access to the raw records and no fixed question can restate the question every time you ask it something new. The gap between those two things is the entire reason "AI reading your CRM" is worth building rather than just being a novelty: # Simplified shape of what the agent actually queried, once it decided # stage duration was worth checking def stage_duration_vs_outcome ( deals : list [ dict ]) -> dict : """ deals: [{stage, days_in_stage, outcome}, ...] outcome is ' won ' or ' lost ' . Groups by stage, then checks whether duration correlates with the eventual outcome inside that stage. """ from collections import defaultdict from statistics import mean by_stage = defaultdict ( lambda : { " won_days " : [], " lost_days " : []}) for d in deals : bucket = " won_days " if d [ " outcome " ] == " won " else " lost_days " by_stage [ d [ " stage " ]][ bucket ]. append ( d [ " days_in_stage " ]) return { stage : { " avg_days_won " : mean ( v [ " won_days " ]) if v [ " won_days " ] else None , " avg_days_lost " : mean ( v [ " lost_days " ]) if v [ " lost_days " ] else None , } for stage , v in by_stage . items () } No agent needed to write that function, I could write it myself in five minutes. What I wouldn't have done in five minutes is think to ask the question in the first place, across every stage, every rep, and every quarter, without a hypothesis already narrowing where I looked. That's the actual value: not a smarter calculation, a wider search. Where this connects back The underlying problem the agent surfaced (a stage that quietly concentrates risk) is the same pattern behind what gets lost after every discovery call when there's no structured way to capture why a deal stalled. It's also a direct instance of revenue leakage from architecture gaps : the CRM had the data the whole time, and nobody had asked it the right question. Try it on your own pipeline If you want to see what an agent finds in your own pipeline before you decide whether it's worth running for real, the MCP server is free to install: Install the free MCP server And if what it finds is the kind of thing you'd rather walk through with someone than read off a screen alone, book a call and bring what it surfaced. If you've pointed an agent at your own CRM with no leading question, I'd like to hear what it found that your dashboard hadn't shown you.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/artefactventures/i-gave-an-ai-agent-three-years-of-deal-history-heres-the-first-pattern-it-found-185

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
