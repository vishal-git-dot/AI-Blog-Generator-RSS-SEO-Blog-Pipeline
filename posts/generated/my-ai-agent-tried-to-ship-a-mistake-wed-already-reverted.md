---
title: "My AI agent tried to ship a mistake we'd already reverted"
slug: "my-ai-agent-tried-to-ship-a-mistake-wed-already-reverted"
author: "Mason Delan"
source: "devto_python"
published: "Mon, 06 Jul 2026 03:47:27 +0000"
description: "A month ago we added a card_token column to the users table so a background job could retry failed Pro charges. It lasted about two days. Storing card data i..."
keywords: "selvedge, you, agent, your, card, data, users, own"
generated: "2026-07-06T04:05:09.364693"
---

# My AI agent tried to ship a mistake we'd already reverted

## Overview

A month ago we added a card_token column to the users table so a background job could retry failed Pro charges. It lasted about two days. Storing card data in your own database drops you into PCI-DSS (the compliance standard that kicks in the moment card data touches your systems), so we pulled it and moved to Stripe-managed payment methods. Last week the charges started failing again. New Claude Code session, no memory of any of that. Its plan? Add a card_token column to users and retry. I don't really blame the agent. It had the context the first time and it was right. The problem is that context died when the session closed. That's the part I never see mentioned about building with agents: the code sticks around, the reasoning doesn't. People leave a trail without trying. A commit message, a PR comment, the Slack thread before it. Agents don't, and the prompt that explained everything is gone by morning. So I built Selvedge to hold onto the reasoning. What happened the second time Selvedge is a local MCP server the agent calls as it works. There's a four-line block in our CLAUDE.md that says, roughly: before you touch an entity, check if we've been here before. $ selvedge prior-attempts users.card_token users.card_token Prior attempt 28 days ago ( reverted after 2 days ) Reasoning Added to store card tokens for one-click retries. Outcome REVERTED — kept card data out of our own DB to stay clear of PCI-DSS scope ; moved to Stripe-managed methods. So it didn't add the column. It charged off_session against the saved Stripe PaymentMethod instead. Charge retried, no card data in our database, done. We paid for that lesson once. How it works The agent writes down why live, in the moment, from the same context that made the change. That's the whole trick. A lot of the "git blame for AI" tools take your diff afterward and ask a second model to explain it. That's a guess. It reads well, but you can't really build on it. Selvedge stores what the agent actually meant, in its own words. It's 8 tools, over MCP and as a plain CLI: prior_attempts , blame , diff and history for reading the past; log_change to record a change; and changeset , search and stale_decisions for working with what's stored. Data sits in a SQLite file under .selvedge/ next to your code. No account, no telemetry, no network calls in the core, and zero LLM calls in that core path (on purpose). Your reasoning text is whatever the agent wrote, stored as-is. You don't have to be a "real" engineer for this to pay off. If you can run pip install and paste four lines into a file, you're set: pip install selvedge selvedge setup New in v0.3.9 selvedge export --format agent-trace writes your history out as Agent Trace v0.1.0, the open attribution format from Cursor and Cognition AI — and selvedge import reads it back, so your history round-trips instead of being stuck inside Selvedge. Export it, hand it to another tool, import it back. Selvedge does the live capture; the format is shared. Try it pip install selvedge && selvedge setup If you've ever reopened your own AI-built project and thought "wait, why did I do it like this," that's the whole pitch. git blame tells you what changed and when. Selvedge tells you why, after the session and the model that wrote it are both long gone. selvedge.sh · pip install selvedge · github.com/masondelan/selvedge I'm building this in the open. If you run it and it breaks, I want to hear about it.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/masondelan/my-ai-agent-tried-to-ship-a-mistake-wed-already-reverted-4737

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
