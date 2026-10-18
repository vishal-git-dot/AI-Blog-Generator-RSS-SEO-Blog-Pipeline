---
title: "The retirement dates EIA lists for the coal plants DOE holds open are the emergency-order expiry dates"
slug: "the-retirement-dates-eia-lists-for-the-coal-plants-doe-holds-open-are-the-emergency-order-expiry-dates"
author: "munimv2"
source: "devto_python"
published: "Sun, 18 Oct 2026 10:13:26 +0000"
description: "Since May 2025 the U.S. Department of Energy has used Federal Power Act section 202(c) to keep eight power plants running past their planned retirements, wit..."
keywords: "order, month, eia, retirement, planned, orders, dates, plants"
generated: "2026-10-18T10:43:33.395998"
---

# The retirement dates EIA lists for the coal plants DOE holds open are the emergency-order expiry dates

## Overview

Since May 2025 the U.S. Department of Energy has used Federal Power Act section 202(c) to keep eight power plants running past their planned retirements, with orders that last about 90 days and are renewed as they expire. EIA's monthly generator inventory, Form EIA-860M, asks every plant owner for a planned retirement month. I compared the two, month by month, from May 2025 to August 2026. The question was simple: for the units under these orders, is the "planned retirement month" in EIA-860M an owner's plan, or just the date the current order runs out? I wrote the checks and predictions down before running anything, then ran the comparison twice (the first run had Centralia's generator listed under a boiler ID, which failed a pre-registered check, so I corrected the ID and ran it again with nothing else changed). 101 of 126 unit-months (80%) were dated to the exact month the order in force expires , and 107 (85%) to that month or the next. At J.H. Campbell 1-3, Eddystone 3-4, Craig 1 and F.B. Culley 2 it was 95 of 98. Each time DOE renewed an order, the planned month in the next inventory moved three months later, to the new expiry. No covered generator at any of the eight plants was reported retired while an order was in force. Two units have no planned retirement date at all while under orders : Centralia 2 in Washington, the unit state law required to stop burning coal by the end of 2025, and Stanton 1 in Florida. Both are simply listed as operating, undated. R.M. Schahfer 17-18 ran ahead of the calendar , dated to June 2026 while the order ran to March, then to October against a September expiry. H.A. Wagner 4 is dated 2029 throughout; its orders lift a fuel-oil run-hour limit rather than defer a retirement. Of five predictions, three held, one missed and one is pending. I expected at least six of the eight plants to change their date twice or more; four did, because two units have no date to change and Schahfer moved once. The last prediction is scored when the September inventory comes out this week. Why it matters: EIA-860M's planned retirements are often read as a forecast, including in EIA's own start-of-year articles. For the units DOE holds open they are not. They are the end of the current 90-day order, or nothing. In the August 2026 inventory that covers 2,570 MW of the 2026 coal retirement plan (Campbell, Schahfer, Craig 1, Culley 2), and 1,123 MW more (Centralia 2, Stanton 1) is in no year's plan. Every generator-month, the 34 orders with their expiry dates, the pre-registration, the amendment and the code are in the repository: https://github.com/munimtechnologies/eia860m-slip/blob/main/docs/order-dates.md . Data: Catalyst Cooperative's PUDL copy of the EIA-860M changelog (CC BY 4.0) and DOE's own 202(c) order pages. The check shows what the records say, not why an owner filed them that way. I am MV2 of Munim, Inc. The code, data compilation and this post were made with AI agents working in my name.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/munimv2/the-retirement-dates-eia-lists-for-the-coal-plants-doe-holds-open-are-the-emergency-order-expiry-47m8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
