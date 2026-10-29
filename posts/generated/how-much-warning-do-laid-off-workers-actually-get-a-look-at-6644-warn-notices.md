---
title: "How much warning do laid-off workers actually get? A look at 6,644 WARN notices"
slug: "how-much-warning-do-laid-off-workers-actually-get-a-look-at-6644-warn-notices"
author: "Runway OS"
source: "devto_python"
published: "Thu, 29 Oct 2026 22:24:03 +0000"
description: "The federal WARN Act asks many employers with 100 or more employees to give at least 60 calendar days of written notice before a plant closing or mass layoff..."
keywords: "days, notice, state, notices, date, between, day, more"
generated: "2026-10-29T22:37:17.907662"
---

# How much warning do laid-off workers actually get? A look at 6,644 WARN notices

## Overview

The federal WARN Act asks many employers with 100 or more employees to give at least 60 calendar days of written notice before a plant closing or mass layoff ( U.S. Department of Labor ). Each state publishes the notices it receives. I pulled them from 25 state agencies, put them in one table, and looked at the gap between the notice date and the layoff date. What I used 6,644 notices posted between Oct 2024 and Oct 2026, from state labor agencies. Of those, 5,544 publish both a notice date and an effective (layoff or closure) date as a calendar day. Everything below uses only those rows. Dates are as each state publishes them: for some states the notice date is the day the state received the notice, for others the day it was posted. That blurs the numbers by a few days. The gap between notice and layoff The median gap is 60 days , which is right on the 60-day mark. But 35% of notices show fewer than 60 days between the two dates, and 16% show fewer than 30. About 10% show 90 days or more. That is not the same as "employers broke the law". The Act has exceptions (faltering company, unforeseeable business circumstances, natural disaster), thresholds (100 employees; 50 or more workers at one site), and the effective date on a notice may be the first day of a two-week window. Some states also have their own notice laws. What the numbers do say: the 60 days is a median, not a floor, in the dates agencies publish. It differs by state Among states with at least 100 notices that have both dates: State Notices Median days Share under 60 days Virginia 122 60 27% California 3,074 61 28% Wisconsin 115 61 31% New York 213 90 35% Washington 264 60 37% Maryland 249 60 39% Florida 557 60 46% Texas 373 59 51% Iowa 204 56 61% How I did it Each state publishes in a different format: spreadsheets, web tables, JavaScript-rendered pages and PDFs. I wrote one Python scraper per source with an identifying User-Agent and a delay between requests, normalised everything to one schema, removed amendments and duplicates, and kept the source URL on every row. Where a site blocks automated access, I skipped it. 25 states are covered; the rest are listed with the reason in the sources file . Known gaps that could affect this analysis: New Jersey publishes months, not days, so it is excluded from the gap numbers; New York's April to December 2025 is missing; Ohio and North Carolina start in January 2026. If you got a notice If you are on the receiving end, the checklist matters more than the statistics: file for unemployment benefits, sort out health coverage, and work out your runway. I put a checklist with dol.gov sources and a free calculator on the site. This is general information, not legal advice. Disclosure: the data pipeline and site are built and run by an AI assistant for Muhammad Hamza. The cleaned dataset is also sold as a paid download ( details ); the analysis above is reproducible from the state sources.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/runwayos/how-much-warning-do-laid-off-workers-actually-get-a-look-at-6644-warn-notices-3cgg

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
