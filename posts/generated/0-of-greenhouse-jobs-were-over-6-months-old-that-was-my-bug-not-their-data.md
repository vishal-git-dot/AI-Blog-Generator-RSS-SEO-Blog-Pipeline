---
title: "0% of Greenhouse jobs were over 6 months old. That was my bug, not their data"
slug: "0-of-greenhouse-jobs-were-over-6-months-old-that-was-my-bug-not-their-data"
author: "Radar Labs"
source: "devto_python"
published: "Fri, 23 Oct 2026 20:55:58 +0000"
description: "I spent a week assuming my scraper was fine. Then a sanity check told me 0% of Greenhouse postings were older than six months, which is not a thing that happ..."
keywords: "days, not, you, older, than, board, greenhouse, postings"
generated: "2026-10-23T21:14:15.042423"
---

# 0% of Greenhouse jobs were over 6 months old. That was my bug, not their data

## Overview

I spent a week assuming my scraper was fine. Then a sanity check told me 0% of Greenhouse postings were older than six months, which is not a thing that happens on a real job board. The culprit was one field. And it is not exotic — if you have ever scraped a job feed, you have probably made the same mistake. The mistake is updated_at Our Greenhouse connector read: postedAt = row . get ( " updated_at " ) or row . get ( " created_at " ) That reads fine. It is wrong twice over. First, the Greenhouse board API does not return created_at for a job, so the fallback never fires. Second — and this is the part that matters — updated_at is when a recruiter last touched the requisition , not when the job went live. Here is what that does to real data. Account Executive, AI Native came back with a recent updated_at . Its actual first_published is 2024-12-20 . A req opened in 2024 and edited yesterday looks one day old. The fix is one line: postedAt = ( row . get ( " first_published " ) or row . get ( " created_at " ) or row . get ( " updated_at " )) first_published exists. It was just not the field we reached for. What it changed Same 259 companies, same day, only the date field changed: with updated_at with first_published median age 22 days 51 days older than 180 days 5.5% 14.2% Greenhouse older than 180 days 0.0% 14.5% The Greenhouse number is the tell. No board has zero stale reqs. 0.0% was not a finding, it was a bug report: the freshness signal had been pinned to "last edited", so every edit reset the clock. If you are filtering scraped jobs by age, or building an "only new since last run" delta on top of posted_at , this bug is silent and total. Every stale req comes back as new, forever. The full age distribution (6,833 postings that publish a salary) Measured 2026-10-24 from each board's own first-published field: p10: 8 days median: 51 days p90: 236 days oldest: 2,628 days (just over seven years) older than 30 days: 65.9% older than 90 days: 30.1% older than 180 days: 14.2% older than a year: 4.9% So the median "open" role has been open for close to two months. Nearly a third are past a quarter, and one in seven is past half a year. Boards differ, and the difference is the date semantics Board Postings Median age p90 Oldest >180d Date field Greenhouse 4,063 52d 236d 2,628d 14.5% first_published Ashby 2,615 46d 215d 1,325d 12.7% createdAt Lever 155 77d 527d 2,230d 30.3% publishedAt Lever postings are older on median and much older in the tail. That is either a different hiring style or a board that keeps reqs visible after the hire — I cannot tell which from the data, so I am not going to dress it up as a conclusion. Companies with the longest-running open reqs (minimum five dated postings): Secureframe median 442 days , Zilliz 430, Character 310, Delfina 299. A stale listing is not proof of a fake job either. Plenty of teams keep a rolling req open for a role they hire into continuously. But if you are a candidate sorting by "newest", a rolling req sorted by updated_at will follow you around forever. The general rule Before you trust any posted_at , answer two questions about it: Which field is it? first_published / createdAt / publishedAt are posting dates. updated_at / modified_at are edit dates. Mixing them is the bug above. Does the board even have the first kind? If it only exposes last-modified, your ages are understated and no amount of downstream maths will fix it — report it separately rather than averaging it in with boards that do it right. A cheap sanity test that would have caught this in minutes: compute the share of postings older than six months, per board. If any real board comes back at 0%, you are not measuring what you think you are measuring. The age numbers and the per-company breakdown live at radarlabs.surge.sh/freshness.html , regenerated weekly from the companies' own public feeds. The underlying postings, with dates and salary ranges, are a free CC BY 4.0 CSV — 6,833 rows across 259 companies. If you would rather not run the scraping yourself, the same data is available as a paid Apify Actor, and I would rather you read the free CSV first and decide whether it is worth $0.0015 a row.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sdijjxcfs/0-of-greenhouse-jobs-were-over-6-months-old-that-was-my-bug-not-their-data-40ee

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
