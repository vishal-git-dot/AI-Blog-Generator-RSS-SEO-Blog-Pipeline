---
title: "My directory's "New" page sorts by a date I don't own. Its freshest row is 31 days old."
slug: "my-directorys-new-page-sorts-by-a-date-i-dont-own-its-freshest-row-is-31-days-old"
author: "Mindutil"
source: "devto_webdev"
published: "Wed, 18 Nov 2026 00:36:45 +0000"
description: "Every directory has a /new page, and mine has a sentence on it that I never re-read: "Check back often — new tools are added every week." I went to look at w..."
keywords: "new, page, days, date, newest, sort, publishedat, directory"
generated: "2026-11-18T00:48:50.459865"
---

# My directory's "New" page sorts by a date I don't own. Its freshest row is 31 days old.

## Overview

Every directory has a /new page, and mine has a sentence on it that I never re-read: "Check back often — new tools are added every week." I went to look at what my newest page actually contains today, and the top row was published October 18, 2026 . That is 31 days ago, on a page whose whole job is freshness. Here's the part that made me laugh: the page is not broken. It is sorting exactly as I told it to. I just told it to sort by a date I don't own. What "newest" means in my code The directory is 4,323 AI tool listings. The sort behind the newest view is three lines: case "newest" : return [ { publishedAt : "desc" } , { createdAt : "desc" } ] ; createdAt is the row entering my database. publishedAt is — per the comment I wrote next to the column in the schema — "Original publication date on the source site ". It comes from the upstream directory I ingest from, and it is the primary key of the sort. So /new-ai-tools doesn't mean "new to me". It means "new at the place I copy from", and the reader can't see that field anywhere: the cards render name, logo, rating, pricing badge. No date. One page promise, two possible meanings, and the sort picks the one I control least. How old is "new"? I ran the numbers over the whole database this morning (read-only, date computed from the same publishedAt column): Listings whose source publish date is within count share 30 days 0 0% 60 days 188 4.3% 90 days 257 5.9% 1 year 827 19.1% 2 years 1,555 36.0% older than 2 years 2,768 64.0% Median publishedAt is March 15, 2024 — 2.7 years before today. Mean age 2.4 years. So the collection is a backlog with a "New" tab on top of it, which is normal for a directory built by ingestion and worth saying out loud instead of papering over with a page that implies a cadence. The lag is the real number Comparing publishedAt to createdAt for each row tells me how stale a listing was at the moment I ingested it: median lag: 957 days 90th percentile: 1,345 days rows already more than a year old at ingest: 3,445 of 4,323 (79.7%) When I "added" something, it had usually been public for two and a half years. That's fine as an archive. It is not fine as a promise, and the promise is what's in the H2. The newest page is a staircase, not a stream The 24 rows on page one of /new-ai-tools today carry only five distinct dates: 2026-10-18 (5 rows), 10-13 (6), 10-07 (6), 10-02 (4), 09-30 (3). The source publishes in weekly-ish batches, so a sort on its publish date gives you a staircase — a jump of six "new" tools, then silence for four days, then another six. Any reader who subscribes to that page learns the upstream's editorial calendar, not mine. Two more dates on the page that don't mean what they look like Each tool page renders "Added" and "Last updated". A few live pages, fetched today without cookies: chatgpt : Added Sep 30, 2026 / Last updated Nov 16, 2026 capcut : Added Sep 30, 2026 / Last updated Nov 17, 2026 midjourney : Added Sep 30, 2026 / Last updated Nov 14, 2026 Those "last updated" values are real, and they do not mean the description changed. updatedAt is bumped whenever the crawler touches the row — 4,177 of 4,323 rows have updatedAt > publishedAt , and createdAt in my local copy spans exactly three distinct dates, because the directory was built in three crawl runs. A timestamp that moves when nobody edited anything is not a content signal; it's pipeline noise wearing a label a reader will interpret as editorial attention. The same lag shows up in death detection. The dead-tool bucket holds 405 listings, and the newest publishedAt among them is January 24, 2026 — so a tool has to have been around for months before it can even be flagged as gone. Zero of the 24 newest rows are flagged, which is either good news or the same blind spot pointed the other way; last week's link audit found 4 supposedly-live listings whose domains no longer resolve, so I'd bet on blind spot. What I'm changing None of this is shipped yet, so I'm writing it as a list rather than a changelog: Split the two meanings. "New to AIVerse" sorts by createdAt ; "Recently released" sorts by publishedAt . Different pages, different promises, so the sort key matches the headline. Put the date on the card. A "new" listing without a visible date is a claim; with one it's a measurement. Delete the cadence sentence until the crawl genuinely adds something weekly. Today it added zero in seven days. Rename "Last updated" to something that survives an audit — "record touched by the pipeline" is ugly and true, and I'd rather be ugly and true than have a page claim editorial attention it isn't spending. The honest summary: my directory is 64% older than two years, ingests at a two-and-a-half-year median lag, and had a page titled "New" whose newest row was 31 days stale. All four problems are copy-and-sort-key problems, not data problems — which is why I keep writing these audits up on the site itself, the newest-tools view is here if you want to check my dates instead of trusting my table. If you run anything with an "updated" or "new" surface fed by ingestion, the question worth asking is which of your timestamps a reader can actually defend — and whether the field driving your sort is one you own.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/li_yi_dcec96bf2647dec1b7e/my-directorys-new-page-sorts-by-a-date-i-dont-own-its-freshest-row-is-31-days-old-1hae

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
