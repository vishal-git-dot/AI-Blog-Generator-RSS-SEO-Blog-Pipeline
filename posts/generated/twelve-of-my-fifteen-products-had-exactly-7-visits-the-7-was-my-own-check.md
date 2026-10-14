---
title: "Twelve of My Fifteen Products Had Exactly 7 Visits. The 7 Was My Own Check."
slug: "twelve-of-my-fifteen-products-had-exactly-7-visits-the-7-was-my-own-check"
author: "Sungsoo Youn"
source: "devto_ai"
published: "Wed, 14 Oct 2026 04:10:03 +0000"
description: "A field note from the autonomous Claude Code agent I run every day on one Windows PC. The numbers come from its own ledgers, not from memory. Free to read fi..."
keywords: "window, products, check, agent, code, page, claude, every"
generated: "2026-10-14T04:22:01.695990"
---

# Twelve of My Fifteen Products Had Exactly 7 Visits. The 7 Was My Own Check.

## Overview

A field note from the autonomous Claude Code agent I run every day on one Windows PC. The numbers come from its own ledgers, not from memory. Free to read first: a PDF sample of the book behind this setup — its first 3 chapters: https://dbsoul.gumroad.com/l/autonomous-ai-agents-claude-code-free-sample My agent sells fifteen small products on a Korean digital storefront. One of its goals is a traffic number: the sum of the total-visits figure that the storefront dashboard shows for each product. The target is 240. This note is about what that number is made of. First: it was a window, not a day On September 17 the goal ledger said 1,219. The dashboard said 177. The agent had been treating the dashboard figure as one day of visits and adding up seven days of it. But the figure is a rolling window. The values went up and down from day to day (one product read 29, then 22, then 12), and the buttons for choosing a period were disabled (they are a paid-plan feature). Adding seven snapshots of a window counted the same visit up to seven times. The fix was to read only the latest snapshot. The ledger has done that since. Second: the floor was the agent Four days later the agent looked at each product instead of the total. Over twelve measured days, twelve of the products never moved much: their daily minimums were 4 to 9 and their maximums 9 to 11. Only three products ever went higher. A flat line across a dozen items is worth explaining before it is read as a little traffic. So the agent searched its own code for scheduled jobs that open the products' public pages, and found a daily check at 08:30 that opens every product page once and confirms the buy button is there. A floor of 7 is what one check a day looks like if the window is seven days long. The storefront does not say how long the window is; the floor is consistent with seven. The search was not complete That search looked at the scheduled jobs whose purpose was to check pages. When this note was audited, the auditor traced every call in the code that opens a public product page instead. It found more: Jobs at 09:45, 18:40 and 19:00 open the main paid guide's public page to read its price. Jobs at 09:45 and 18:40 open the full-collection bundle's public page. They do this in a browser that is logged in as the seller. Whether the storefront counts a logged-in seller as a visitor has never been measured. The latest row The October 1 row in the traffic ledger: Total: 135 Twelve products: exactly 7 each The full-collection bundle: 22. The main paid guide: 20. The free edition: 9. Fifteen products times 7 is 105. So at most about 30 of the 135 visits in the window came from anyone other than the 08:30 check. For the twelve products sitting at exactly 7, it is close to zero. For the bundle and the main guide, part of what sits above 7 may be the other jobs. The ledger cannot split the two. The goal of 240 includes the 105 floor. To reach it, visits from anyone other than the 08:30 check would have to go from at most about 30 to about 135 per window: at least four and a half times what they are now. The rules Know whether a dashboard number is a count or a window before you add it up. Watch it for a few days: a window goes down as well as up. Subtract your own monitoring. Any health check that loads a public page is a visitor to some counters. Find every place your code opens the page, not only the jobs built to check pages. A price lookup is a page visit too. A flat line across many items at the same value can be a probe. Find the probe before you read the line as demand. Where this comes from. Every post here comes from one setup I run daily: a CLAUDE.md, memory files the agent reads before it touches anything, and a separate auditor agent that returns PASS or FAIL. The first 3 chapters of the book that walks through it are free as a PDF: https://dbsoul.gumroad.com/l/autonomous-ai-agents-claude-code-free-sample The full edition is 11 chapters plus 4 ready-to-use templates (CLAUDE.md starter, memory files, auditor checklist, measurement guide) and a hands-on section for every chapter, $19 as a PDF: https://dbsoul.gumroad.com/l/autonomous-ai-agents-claude-code Questions about the setup are welcome in the comments — I'll answer with what actually happened, not theory.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dbsoul/twelve-of-my-fifteen-products-had-exactly-7-visits-the-7-was-my-own-check-434

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
