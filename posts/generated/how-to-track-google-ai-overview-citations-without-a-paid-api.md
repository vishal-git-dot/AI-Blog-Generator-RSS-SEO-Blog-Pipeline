---
title: "How to Track Google AI Overview Citations Without a Paid API"
slug: "how-to-track-google-ai-overview-citations-without-a-paid-api"
author: "Tim Zinin"
source: "devto_ai"
published: "Mon, 28 Sep 2026 13:25:03 +0000"
description: "The problem When a buyer asks Perplexity or ChatGPT "best CRM for a small business," the answer links to a handful of sources — a review site, a vendor's doc..."
keywords: "model, com, best, per, perplexity, crm, small, business"
generated: "2026-09-28T13:27:07.932682"
---

# How to Track Google AI Overview Citations Without a Paid API

## Overview

The problem When a buyer asks Perplexity or ChatGPT "best CRM for a small business," the answer links to a handful of sources — a review site, a vendor's docs, a competitor's blog. Those citations are the new backlinks, and SEO teams increasingly need to know which domains and exact URLs get cited for their category queries. Checking this manually means opening each AI chat, asking the same buyer-intent prompts over and over, and copying the cited links into a spreadsheet — slow, non-reproducible, and impossible to compare across models. Dedicated GEO (Generative Engine Optimization) platforms track this, but they charge hundreds of dollars a month in seats, as the README points out with examples like Ahrefs Brand Radar, Profound and Otterly. What the actor does The AI Overview Citation Tracker issues grounded retrieval checks against configurable LLMs and returns one evidence-backed observation per query × model pair. From the README: Three grounded engines by default : perplexity/sonar (built-in web search), plus openai/gpt-4o-mini and google/gemini-2.5-flash with OpenRouter's openrouter:web_search server tool. No API key required. Without a key, the defaults run through the Apify-billed dependency runner fayoussef/bulk-llm-runner , whose model usage bills to your Apify account at cost. An optional OpenRouter key (BYOK) enables direct provider access and custom models; the actor never resells or marks up model usage. Structured evidence per row : cited domains and normalized public URLs, a snippet of the model's answer, token usage and provider-reported cost when available, evidence mode ( structured_url_annotations , inline_url_fallback , or none ), coverage and confidence scores, explicit data gaps, and a conservative recommended action. Any language — set lang and the grounded model answers natively. Billing is honest: rows where a model call fails come back found: false with the reason and are not billed. Each model multiplies rows — 10 queries across 2 models is 20 billed rows, not 10 — and the contract deliberately sets safeToAutomate: false so a single observation never becomes an automatic content decision. Example: input and output Documented input — two buyer queries against one grounded model: { "queries" : [ "best project management software" , "what is the capital of France" ], "models" : [ "perplexity/sonar" ] } A real row from a real run, quoted from the README: { "recordType" : "ai_overview_citation_observation" , "schemaVersion" : "2.0" , "query" : "best crm for small business" , "model" : "perplexity/sonar" , "lang" : "en" , "found" : true , "citedDomains" : [ "pcmag.com" , "zapier.com" , "techradar.com" , "fitsmallbusiness.com" , "fayedigital.com" ], "citedUrls" : [ "https://www.pcmag.com/picks/the-best-small-business-crm-software" , "https://zapier.com/blog/best-crms-for-small-business/" ], "answerSnippet" : "The **best CRM for a small business depends on your priorities**, but the most consistently recommended options in 2026 are **Bigin by Zoho CRM** ..." , "promptTokens" : 33 , "completionTokens" : 398 , "summary" : "perplexity/sonar on \" best crm for small business \" : cites 5 sources: pcmag.com, zapier.com, techradar.com, fitsmallbusiness.com, fayedigital.com." , "checkedAt" : "2026-07-28T15:50:06.215Z" } Pricing and the free limit Pay-per-event on the free tier: $0.005 per run start plus $0.02 per query × model row . A 10-query run against one model costs $0.005 + 10 × $0.02 = $0.205 . Apify's free plan gives $5 of usage credits per month, so $5 covers about 24 such runs — roughly 240 citation observations (model usage is billed separately by the dependency runner or your OpenRouter key; the README's canary measured about $0.014 for one perplexity/sonar query, capped at $0.03). Try it Paste your buyer queries, pick a grounded model, and press Start — no card needed on the free plan: AI Overview Citation Tracker For AI agents and MCP The actor takes JSON in and returns a flat, machine-checkable row per query × model pair, callable from the Apify API, the SDKs, or the hosted Apify MCP server whose setup the README documents. An agent can route rows directly on found , citationEvidenceMode , confidenceBand and retryable — for example sending structured_url_annotations rows to an analyst queue and inline_url_fallback or none rows to verification — while safeToAutomate: false keeps it from turning one observation into autonomous outreach or edits.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/timmyzinin/how-to-track-google-ai-overview-citations-without-a-paid-api-50hp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
