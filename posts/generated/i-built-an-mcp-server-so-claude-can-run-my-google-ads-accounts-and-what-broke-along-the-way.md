---
title: "I built an MCP server so Claude can run my Google Ads accounts (and what broke along the way)"
slug: "i-built-an-mcp-server-so-claude-can-run-my-google-ads-accounts-and-what-broke-along-the-way"
author: "Quinten Van Meirvenne"
source: "devto_python"
published: "Tue, 28 Jul 2026 19:04:08 +0000"
description: "I'm a growth marketing consultant, not a professional developer. I manage Google Ads and Meta accounts for e-commerce brands, and until last year my reportin..."
keywords: "server, tool, one, mcp, assistant, you, has, every"
generated: "2026-07-28T19:39:37.248220"
---

# I built an MCP server so Claude can run my Google Ads accounts (and what broke along the way)

## Overview

I'm a growth marketing consultant, not a professional developer. I manage Google Ads and Meta accounts for e-commerce brands, and until last year my reporting routine was fourteen browser tabs, a spreadsheet export and an afternoon I never got back. Then MCP happened. The Model Context Protocol lets you hand an AI assistant a set of tools it can actually call: not "here is my data, please summarize", but "go query the account yourself". So I built my own MCP server on top of the Google Ads API, and later Meta, GA4 and Search Console. It now has around a hundred tools and runs my monthly reporting, audits and a good chunk of optimization work. This post is about the three design choices that mattered and the three things that bit me. If you are a marketer who codes a little, or a developer who wants to see what MCP looks like outside the demo zone, this is for you. Design choice 1: passthrough beats wrappers My first instinct was to build a neat wrapper tool for every report I needed: get_campaigns, get_keywords, get_search_terms. That lasted a week. Every new question needed a new tool, and the assistant was always one tool short. The fix was embarrassingly simple: expose the query language itself. Google Ads has GAQL, a SQL-ish language that can answer almost anything. One passthrough tool replaced a dozen wrappers: @mcp.tool () def google_query ( customer_id : str , gaql : str ) -> str : """ Run a raw GAQL query against a Google Ads account. """ client = get_client () service = client . get_service ( " GoogleAdsService " ) rows = service . search ( customer_id = customer_id , query = gaql ) return format_rows ( rows ) The assistant writes better GAQL than I do. A question like "which search terms burned money without converting last month" becomes: SELECT search_term_view . search_term , metrics . cost_micros , metrics . conversions FROM search_term_view WHERE segments . date DURING LAST_30_DAYS ORDER BY metrics . cost_micros DESC Keep wrappers for the genuinely complex flows (campaign creation has real guardrails in my server). For reading data, passthrough wins. Design choice 2: never trust a write you didn't re-read Reads are safe. Writes are where an agent quietly ruins your week. Early on, two of my mutation tools (changing a campaign's network settings and switching bidding strategy) reported success while changing absolutely nothing. The API accepted the request, the tool said "applied", and the account stayed exactly as it was. I only caught it because I happened to check the UI. Since then my server has one iron rule: every write is followed by a read of the same resource, and the assistant compares the two. If the follow-up query does not show the new value, the write failed, whatever the response said. This one habit has caught more silent failures than any amount of error handling. The second guardrail: destructive or expensive operations (pausing campaigns, touching budgets) stay behind explicit confirmation. The assistant proposes, I approve. Boring, and exactly how I want my ad spend handled. Design choice 3: a memory file for mistakes The most valuable file in the whole setup is not code. It is a plain markdown file called learned-errors.md. Every time a bug costs me more than ten minutes, the session ends by logging one line: date, context, what went wrong, and the rule that prevents it next time. The assistant reads that file at the start of every session. It sounds trivial. It compounds. My assistant no longer repeats the mistakes from March, because March is written down. Three things that bit me The name collision. I had import google_audit at the top of the file and a tool function named google_audit below it. The function definition shadowed the module, and suddenly google_audit.run_audit() failed with "'function' object has no attribute". Alias your imports when a tool shares the name. No hot reload. An MCP server loads its code once, when the client starts it. I lost an evening staring at a fix that "didn't work" because the old process was still running. The ritual now: quit the client fully, verify the module imports cleanly in the venv, then restart. One bad import kills everything. When I added new connectors without installing their packages in the venv, the whole server crashed on startup. Not just the new feature: all hundred tools gone. Now every dependency change ends with venv/bin/python -c "import my_server" before I restart anything. Should you build your own? If a maintained MCP server already covers your platform, use that one. Building your own makes sense when the workflow itself is your edge: my server encodes how I audit accounts, which n-grams I mine from search terms, what a report should look like before a client sees it. The payoff is real. Monthly reports that took an afternoon now draft themselves while I make coffee, and I stay the editor instead of the spreadsheet operator. For a one-person consultancy, that is the difference between billing hours and losing them. If you are curious about the marketing side of this setup, I write about that at mindyourgrowth.be . Questions about the server itself: ask away in the comments, I read them.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/quinten_vanmeirvenne_2fd/i-built-an-mcp-server-so-claude-can-run-my-google-ads-accounts-and-what-broke-along-the-way-n4i

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
