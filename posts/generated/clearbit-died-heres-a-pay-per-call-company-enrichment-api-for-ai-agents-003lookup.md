---
title: "Clearbit died. Here's a pay-per-call company enrichment API for AI agents ($0.03/lookup)"
slug: "clearbit-died-heres-a-pay-per-call-company-enrichment-api-for-ai-agents-003lookup"
author: "Tuf Ti"
source: "devto_python"
published: "Tue, 16 Jun 2026 16:39:22 +0000"
description: "Clearbit's free API shut down April 30, 2025. The replacement (HubSpot Breeze Intelligence) requires an enterprise contract that starts around $20K/year. If ..."
keywords: "company, com, api, cinderwright, json, https, stripe, post"
generated: "2026-06-16T17:05:59.748347"
---

# Clearbit died. Here's a pay-per-call company enrichment API for AI agents ($0.03/lookup)

## Overview

Clearbit's free API shut down April 30, 2025. The replacement (HubSpot Breeze Intelligence) requires an enterprise contract that starts around $20K/year. If you're building AI agents that need company context from a domain name, you've probably felt this gap. I built a pay-per-call alternative: POST a domain, get back structured JSON. No subscription. No contract. $0.03 per lookup. How it works import requests resp = requests . post ( ' https://api.ideafactorylab.org/company-info ' , json = { ' domain ' : ' stripe.com ' } ) print ( resp . json ()) Returns: { "domain" : "stripe.com" , "name" : "Stripe" , "description" : "Stripe is a financial infrastructure platform for businesses." , "industry" : "fintech" , "founded_year" : 2010 , "headquarters" : "San Francisco, CA" , "employee_range" : "1000+" , "social_links" : { "twitter" : "https://twitter.com/stripe" , "linkedin" : "https://linkedin.com/company/stripe" }, "tech_signals" : [ "AWS" , "React" ], "confidence" : "medium" } Powered by AI synthesis from public web data. Honest framing: this is not a database like Clearbit was. It's real-time extraction from the company's public homepage. Coverage is excellent for any company with a real web presence. For AI agents specifically If you're using LangChain, CrewAI, or the OpenAI Agents SDK, the Cinderwright tool wraps this (and 2,838 other services) in a single tool your agent can call in plain English: from cinderwright.langchain import CinderwrightTool tool = CinderwrightTool ( api_key = " sk_cw_... " ) # Agent calls: "company info for anthropic.com" # Tool routes to /company-info automatically Also shipping: URL to Markdown ($0.005/page) While I was at it, I added a URL-to-Markdown endpoint. Same idea: POST a URL, get back clean readable text stripped of navigation, ads, and boilerplate. Useful for RAG pipelines that need to read web pages. resp = requests . post ( ' https://api.ideafactorylab.org/url-to-markdown ' , json = { ' url ' : ' https://example.com ' } ) print ( resp . json ()[ ' markdown ' ]) Get a free key $0.10 free credit, no deposit, no credit card: curl -X POST https://api.ideafactorylab.org/proxy/setup \ -H 'Content-Type: application/json' \ -d '{"wallet": "0xYourBaseWallet"}' Or try the free demo with no key at all: import cinderwright print ( cinderwright . demo ( ' company info for apple.com ' )) Links PyPI: pypi.org/project/cinderwright Source: github.com/cinderwright-ai/cinderwright-api Browse all 2,838 services: api.ideafactorylab.org/discover

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/tufti/clearbit-died-heres-a-pay-per-call-company-enrichment-api-for-ai-agents-003lookup-52p2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
