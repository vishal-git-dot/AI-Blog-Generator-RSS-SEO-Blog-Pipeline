---
title: "How I Built a Sales Agent That Actually Remembers Your Prospects"
slug: "how-i-built-a-sales-agent-that-actually-remembers-your-prospects"
author: "Deepak Paswan"
source: "devto_python"
published: "Sat, 04 Jul 2026 12:40:41 +0000"
description: "Copy this entire block and paste it into Dev.to: Every sales tool I've used has the same problem: it forgets everything the moment you close the tab. Your CR..."
keywords: "agent, hindsight, every, session, sales, prospect, memory, across"
generated: "2026-07-04T13:45:59.768195"
---

# How I Built a Sales Agent That Actually Remembers Your Prospects

## Overview

Copy this entire block and paste it into Dev.to: Every sales tool I've used has the same problem: it forgets everything the moment you close the tab. Your CRM has notes, sure. But your AI assistant? Blank slate every single conversation. Ask it about a prospect you've been working for three months and it treats them like a stranger. I built something different. A sales agent that remembers every objection, every discussion, every commitment — across sessions, across restarts, across days. What It Does Deal Intelligence Agent is a sales assistant built on three layers: Hindsight for persistent memory across sessions cascadeflow for intelligent model routing and cost control FastAPI + React for the backend and UI A sales rep opens a prospect, has a conversation, ends the session. Next day, different server instance, they ask "what objections has Acme raised?" — the agent recalls exactly what was discussed, including specific dollar amounts and concerns raised days ago. The Memory Problem Most AI agents store conversation history in memory. That works fine until the server restarts, the session ends, or you switch devices. Then everything is gone. Hindsight solves this with a persistent memory bank per entity. Each prospect gets their own bank: def _bank_id ( self , prospect_id : str ) -> str : return f " prospect- { prospect_id } " Every exchange gets retained after each turn: client . retain ( bank_id = bank_id , content = f " [ { role . upper () } ] [ { timestamp } ] { content } " ) Before each response, the agent recalls relevant context: results_raw = client . recall ( bank_id = bank_id , query = query ) if hasattr ( results_raw , ' results ' ) and results_raw . results : memories = [ r . text for r in results_raw . results [: max_results ]] Key lesson: Hindsight returns a RecallResult object, not a list or dict. I spent two hours debugging because my parser was doing isinstance(results, list) checks that always failed silently. Always print the raw response shape before writing your parser. The Before and After Session 1 — no prior context: Rep: "They objected to the $50K price" Agent: "I don't have prior context on this prospect. Can you tell me more about their concerns?" memory_source: none memories_recalled: 0 Session 2 — after server restart, completely new session: Rep: "What objections has Acme raised?" Agent: "Acme raised a price objection of $50,000 in our last discussion..." memory_source: hindsight memories_recalled: 5 That delta — generic to specific — is the entire value proposition. Without Hindsight's agent memory , session 2 is identical to session 1. With it, the agent compounds knowledge over time. Intelligent Routing With cascadeflow Running every query through a 70B model is expensive and unnecessary. cascadeflow handles routing automatically: route_result = await self . router . route_query ( messages = messages , complexity_hint = self . _estimate_complexity ( message ), ) Simple queries → llama-3.1-8b-instant at $0.00005 per call Complex analysis → llama-3.3-70b-versatile at $0.00032 per call Every decision is logged — model selected, cost, complexity, reasoning. Most sales conversations are simple status checks. Only strategic analysis needs the expensive model. Across 100 queries the cost difference is significant. Session Summaries via Hindsight reflect() After each conversation, the agent synthesizes everything: result = client . reflect ( bank_id = bank_id , query = " Summarize key points, objections raised, " " deal stage, and recommended next action. " ) Output is a structured summary — discussion points, prospect sentiment, objections, and a specific next action. This becomes the handoff document between sessions. Three Things I'd Do Differently Test your recall parser against the actual response object on day one. Don't assume the shape. Print the raw response first. Add a health check endpoint. I had Hindsight silently falling back to local memory for hours without knowing. A simple retain-then-recall test at startup would have caught this immediately. Classify intent instead of counting words. My complexity heuristic uses word count. Classifying the request type — question vs analysis vs drafting — is more reliable. What's Next The current version handles single-rep conversations. The obvious next step is multi-rep shared memory — where a prospect's history is visible across the entire sales team. Code: github.com/dpkpaswan/deal-intelligence-agent Hindsight docs: hindsight.vectorize.io cascadeflow docs: docs.cascadeflow.ai

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dpkpaswan/how-i-built-a-sales-agent-that-actually-remembers-your-prospects-443e

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
