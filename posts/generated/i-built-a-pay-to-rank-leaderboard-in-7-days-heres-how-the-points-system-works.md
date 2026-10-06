---
title: "I built a pay-to-rank leaderboard in 7 days - here's how the points system works"
slug: "i-built-a-pay-to-rank-leaderboard-in-7-days-heres-how-the-points-system-works"
author: "Martin Valchev"
source: "devto_webdev"
published: "Tue, 06 Oct 2026 22:26:43 +0000"
description: "One evening I noticed sites charging $10k+ for the top spot on a simple "pay to rank" wall. I thought: the idea is fun, but the pricing locks out every indie..."
keywords: "points, you, your, day, free, days, payments, ranking"
generated: "2026-10-06T22:32:41.711197"
---

# I built a pay-to-rank leaderboard in 7 days - here's how the points system works

## Overview

One evening I noticed sites charging $10k+ for the top spot on a simple "pay to rank" wall. I thought: the idea is fun, but the pricing locks out every indie maker who would actually enjoy it. So I built Outclimbed - a public leaderboard where you list your website or X profile and climb by earning points. It took about 4 days to build and roughly a week to get fully production-ready. Here's how it works under the hood and the design decisions behind it. The stack Supabase - database and auth Vercel - hosting Resend - transactional email Umami (self-hosted) - privacy-friendly analytics Dodo Payments - payments (more on why below) Nothing exotic. The interesting part was never the stack, it was the ranking logic. Designing the points system The hard problem with any leaderboard: if only money counts, it's boring. If only activity counts, it's easy to game and the top gets stale. I ended up mixing permanent and decaying points. Permanent points (paid) Listing costs $10 and gives 10 points Extra points are $1 each They never decay, and the listing stays forever Earned points (decaying) Every listing gets a personal share link 1 point per visitor through that link - fades gradually over 30 days 5 points for every person you refer who lists - fades over 6 months Decay was the key decision. Without it, whoever had one viral day would sit on top forever. With it, the board stays alive: you have to keep showing up to keep your spot, while paid points act as a stable floor. Daily boards The all-time board favours early and big players. So I added daily boards : each UTC day has its own ranking based only on that day's activity, and it closes at midnight UTC. Past days stay browsable, so even a small project can "win a day" and point to it. That turned out to be a much better hook than the all-time ranking. Adding a free tier Paid-only entry was a real barrier, so I shipped a free option: Join at 0 points and climb with your share link Free listings are removed after 3 months, unless they buy points or get verified Verification = placing the Outclimbed badge on your site, which also gives +30 points The badge does double duty: it rewards the maker and gives the board backlinks and visibility. Win-win instead of a pure paywall. The payments plot twist My first payment provider turned me down after reviewing the product, classing it as paid advertising / directory placement under their acceptable use policy. Lesson for anyone building something similar: check your payment provider's acceptable use policy before you build , especially if you sell placement, ranking or visibility. I migrated to Dodo Payments as merchant of record and everything has worked since. What I'd do differently Think about payment compliance on day 1, not day 5 Launch the free tier from the start - it's the easiest way to fill an empty board Build daily boards early - they give new users a realistic way to win Try it If you have a side project or an X profile, you can join for free and see how far your share link takes you. I'd love feedback on the decay model - would you weight visits and referrals differently? Let me know in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/martinvalchev/i-built-a-pay-to-rank-leaderboard-in-7-days-heres-how-the-points-system-works-491m

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
