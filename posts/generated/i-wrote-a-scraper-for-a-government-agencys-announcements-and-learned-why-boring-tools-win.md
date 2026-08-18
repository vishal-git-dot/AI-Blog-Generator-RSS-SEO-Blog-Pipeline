---
title: "I wrote a scraper for a government agency's announcements — and learned why boring tools win"
slug: "i-wrote-a-scraper-for-a-government-agencys-announcements-and-learned-why-boring-tools-win"
author: "Prime Sieve"
source: "devto_python"
published: "Tue, 18 Aug 2026 06:02:08 +0000"
description: "I wrote a scraper for a government agency's announcements — and learned why boring tools win Every morning at 6 AM, a small Python script on one VPS checks t..."
keywords: "one, you, scraper, file, cron, when, agency, announcements"
generated: "2026-08-18T06:52:25.239163"
---

# I wrote a scraper for a government agency's announcements — and learned why boring tools win

## Overview

I wrote a scraper for a government agency's announcements — and learned why boring tools win Every morning at 6 AM, a small Python script on one VPS checks the Indonesian food agency's announcement page. If there's something new, it saves the record to a JSON file. That's the whole job. I built it because I wanted to track food-policy announcements without refreshing a website by hand. It runs on: One VPS — no cluster, no Kubernetes cron — five lines in a crontab plain JSON files — no database, no ORM static hosting — the output is a public page anyone can browse That's the entire stack. Here's why it's deliberately boring. The machine A single Linux box. My scraper pulls a few hundred records a day — that does not need a fleet. A fleet is a problem you get to have when thousands of people use your tool. When that happens, I'll rent a second box and update a config file. The scheduler 0 6 * * * cd /home/ubuntu/scraper && ./run.sh >> logs/cron.log 2>&1 Cron gets mocked for being ancient. It deserves respect: it has never crashed, never needed a migration, and every sysadmin alive can read it. The output { "id" : "12345" , "title" : "Bapanas: rice stock stable" , "published" : "2026-08-16" } Plain files. When a tool's whole job is fetch and reshape , the database is a file. Static hosting is free, fast, and impossible to take down by accident. What I learned Boring code is never debugged at 2am. Fancy stacks break in fancy ways. Files and cron break in ways you can see in one cat . Logs are your friend. Every run writes to logs/cron.log . When something breaks, the first question is always "what did the last run say?" — and the answer is in a text file. Ship the smallest thing that works. I was tempted to add a queue, a worker pool, a dashboard. None of it was needed. The scraper ran for 40 days before I touched it again. Public data deserves public tools. This one reads government announcements — no ToS risk, no auth, no ethical gray zone. It's open source because there was no reason not to be. The honest part The first version broke on the third day. The agency changed their HTML slightly. My selector was too strict, so it matched nothing and the script "succeeded" with zero records. Fix: validate output. If a run returns zero records when it should return some, that's an error, not a success. Now the script fails loudly instead of failing quietly. ERROR: 0 records scraped, expected > 0 — aborting, not overwriting data That one line has saved me more times than any framework ever has. The point If you're building a product with users, concurrent jobs, and real state — go rent the fleet, you'll need it. But if you're a solo developer shipping a small data tool, the most expensive thing you can do is reach for the enterprise stack before the problem asks for it. The repo is public: bapanas-news-tracker — 2,000+ posts, one file, no API key, no browser. I'm Prime Sieve — I build small data tools and write about them. More at apify.com/Prime-Sieve .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/primesieve/i-wrote-a-scraper-for-a-government-agencys-announcements-and-learned-why-boring-tools-win-2blk

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
