---
title: "Notes: monthly hashtag report for the docs community"
slug: "notes-monthly-hashtag-report-for-the-docs-community"
author: "douzatan"
source: "devto_ai"
published: "Tue, 07 Jul 2026 14:42:36 +0000"
description: "Internal notes for the community pulse report I put together each month for our open-source project. We watch a small set of hashtags to see where people are..."
keywords: "report, hashtag, month, posts, only, two, reel, keep"
generated: "2026-07-07T14:49:42.588587"
---

# Notes: monthly hashtag report for the docs community

## Overview

Internal notes for the community pulse report I put together each month for our open-source project. We watch a small set of hashtags to see where people are talking about the project and which content formats actually travel. Writing the process down so I stop rebuilding it from memory every four weeks, and so whoever inherits this after me isn't starting cold. What the report needs Post count per tracked hashtag, compared to the previous two months Top 15 posts by engagement — public accounts only Caption text, for a rough keyword frequency pass Format breakdown (image / carousel / reel) Nothing that fingerprints a private individual. Aggregate figures only. Keep it boring and keep it comparable. The value is in the month-over-month line, not in any single number. Options tested Instaloader (Python). Good library, readable docs, did the job for a while. Broke on me twice in one quarter — once on a login challenge, once when rate limits tightened and my loop was too greedy. Perfectly fine if you enjoy the occasional maintenance evening. I stopped enjoying them around the third patch. Official Graph API. The sanctioned route, and the right answer if it fits. It doesn't fit us: hashtag search is scoped to business accounts you manage plus a narrow recent window, so the historical, cross-account view this report depends on isn't reachable. Ruled out on capability, not principle. Hosted browser tool — current pick. Using the Instagram hashtag scraper from AllyHub. Runs as an extension inside my own logged-in session and exports CSV, so there's no proxy or session file for me to keep alive. First run per hashtag is a touch slower while it learns the page; after that the setup is saved and re-runs are one click. It rode through a profile-page redesign in June without any intervention from me — reads the live page instead of a selector I wrote down last spring — which is the specific reason it's still on this list and the other two aren't. Monthly procedure Run collection for each tracked hashtag. ~15 min total end to end. Do it over coffee. Drop the exported CSVs into data/YYYY-MM/ . Run make report (the pandas script lives in the repo). Eyeball the top-posts table for anything obviously misparsed — duplicate rows, a reel with a suspiciously round like count, that kind of thing. Ship the report to the mailing list. Delete raw caption data once the report is out. Keep aggregates only. Rules we follow Public data only, and only accounts posting under our project hashtags. Request volume stays low. This is a monthly pulse check, not surveillance. No personal data retained beyond the reporting window — see step 6, it's not optional. Re-read the platform ToS each quarter. If the rules move, the procedure moves with them. If in doubt about whether something belongs in the report, leave it out. Open questions [ ] Reel engagement counts look inconsistent between collection runs. Verify against a couple of known posts before trusting any reel trend line. [ ] One of the five hashtags is basically noise now — mostly unrelated posts. Consider dropping it next month. [ ] Automate step 4? Leaning no. The manual eyeball has caught two bad exports that a naive check would have waved through. Cheap insurance. [ ] Worth adding a simple diff against last month's top posts, so recurring high performers are easy to spot? Maybe. Low priority. Notes to self The whole report is about 90 minutes of work now, and roughly two-thirds of that is the writing and interpretation — which is the part worth doing. When collection starts eating more than 20 minutes, something upstream has changed and it's worth stopping to look rather than pushing through. Past me learned that the expensive way.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/douzatan/notes-monthly-hashtag-report-for-the-docs-community-1l6b

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
