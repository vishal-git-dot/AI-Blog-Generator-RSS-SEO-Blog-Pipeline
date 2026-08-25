---
title: "My bot logged a fresh decision every 5 minutes for over an hour. The price it was deciding on never moved once."
slug: "my-bot-logged-a-fresh-decision-every-5-minutes-for-over-an-hour-the-price-it-was-deciding-on-never-moved-once"
author: "WWP"
source: "devto_python"
published: "Tue, 25 Aug 2026 06:11:28 +0000"
description: "Another one from the same one-person-AI-company setup I've written about before: Claude Code builds and maintains the code, several agents run unattended on ..."
keywords: "every, same, log, nothing, bot, price, one, api"
generated: "2026-08-25T06:56:03.871151"
---

# My bot logged a fresh decision every 5 minutes for over an hour. The price it was deciding on never moved once.

## Overview

Another one from the same one-person-AI-company setup I've written about before: Claude Code builds and maintains the code, several agents run unattended on a schedule, nobody's watching in real time. This one's from earlier in the project than the incidents I've posted about before, and it's the simplest of the bunch - which is what makes it worth writing up. The setup A crypto trading bot polls a broker's API every 5 minutes, pulls the last hour of price bars, and decides whether to buy, sell, or hold based on recent price movement. Every cycle, it logs its decision - symbol, price, reasoning - to a file. That log was the only thing anyone (human or otherwise) was checking to confirm the bot was doing its job. What actually happened The code asked the broker's API for "the last N bars" by passing a limit parameter and nothing else - no explicit start time. That seemed like a reasonable way to ask for "the most recent bars." It wasn't. Without an explicit start time, the API silently returned a fixed window - bars starting from midnight UTC that day, sorted oldest-first - instead of the most recent N bars. Two very different requests that happen to share a limit parameter, with no error, no warning, nothing in the response shape that would tip you off. Practical effect: the bot kept asking every 5 minutes, kept getting an answer, and for over an hour that answer was exactly the same set of bars - the same price, to three decimal places, cycle after cycle. The log showed a fresh timestamp and a fresh "decision" every 5 minutes the whole time. Nothing about the log looked wrong. It just wasn't true - the bot wasn't deciding anything based on current information, it was re-deciding the same stale snapshot over and over and calling it live. I only caught it by actually looking at the price values across consecutive log entries during an unrelated review and noticing they were identical - not "similar," identical to the decimal. Why this one's worth separating from the others I've written before about two other incidents from this same project - a safety check that fired correctly but never got logged, and a scheduled task that crashed for three weeks while still reporting success. Those both involved something breaking. This one didn't. The bug was in a single missing keyword argument to an API call, the API itself never errored, the process never crashed, nothing timed out. Every individual component did exactly what it was told to do. The bot was, by every internal measure it had, working. That's the part that generalizes past this one API's quirk: "the log says something happened every cycle" and "something meaningfully different happened every cycle" are not the same claim, and nothing about a healthy-looking log distinguishes them. A monitoring setup built around "did the process log something recently" - which is most of what I had at the time - is structurally blind to this exact failure mode. It would need to check whether the content changed, not just whether output kept arriving on schedule. What I'm taking from it Between this and the other two incidents, I've now got three distinct ways an unattended agent looked completely fine from the outside while doing nothing useful: a real result that never got recorded, a crash that got recorded as success, and correct-looking output that was quietly frozen. Three different bugs, same underlying gap - nothing was checking "is the actual work still happening," only "is the process still running." Curious whether others running scheduled/unattended agents have run into the frozen-but-technically-successful version specifically - it's the quietest of the three failure modes I've hit, in the sense that there's no error anywhere to eventually trip over. You'd only catch it by actually reading the values, which is exactly the kind of check nobody does once something's been running fine for weeks.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/tatsuyawwp/my-bot-logged-a-fresh-decision-every-5-minutes-for-over-an-hour-the-price-it-was-deciding-on-never-2g2m

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
