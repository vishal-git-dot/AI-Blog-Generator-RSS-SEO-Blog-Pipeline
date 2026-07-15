---
title: "Building a Telegram crypto-alert bot with Redis Streams — and the false-positive problem nobody warns you about"
slug: "building-a-telegram-crypto-alert-bot-with-redis-streams-and-the-false-positive-problem-nobody-warns-you-about"
author: "SerhiiBogomaz"
source: "devto_python"
published: "Wed, 15 Jul 2026 13:31:27 +0000"
description: "I've been building a side project for the last few months — a Telegram bot that watches crypto prices and pings you when something you care about happens (pr..."
keywords: "state, redis, you, tick, crypto, alert, price, every"
generated: "2026-07-15T13:53:37.359640"
---

# Building a Telegram crypto-alert bot with Redis Streams — and the false-positive problem nobody warns you about

## Overview

I've been building a side project for the last few months — a Telegram bot that watches crypto prices and pings you when something you care about happens (price crosses a threshold, a coin hits a new ATH, volume spikes, whatever). Nothing groundbreaking on the surface, but getting it reliable turned into a much more interesting engineering problem than I expected. Wanted to write up the parts that actually taught me something. Stack: Python 3.12, aiogram 3 for the bot layer, PostgreSQL for storage, Redis for everything hot-path, Docker for deployment. The pipeline Market data comes in from CoinGecko every 5 minutes via APScheduler, gets normalized, and lands on a Redis Stream ( crypto:prices_stream ). A worker reads it with a consumer group ( XREADGROUP ), fans out per-coin to every active subscription watching that coin, and runs each one through a small pipeline: a guard (is this condition active, has cooldown passed) → a checker (does the condition actually hold) → an accumulator → and if all that passes, a push to a second stream ( crypto:notification_stream ) that a separate worker drains to actually send the Telegram message. Two streams instead of one queue was a deliberate choice — price ingestion and notification delivery have completely different failure modes and completely different consumers. Decoupling them means a slow Telegram API call never backs up price processing, and a CoinGecko hiccup never blocks notifications that are already queued. The false-positive problem This is the part I didn't expect to spend the most time on. Crypto prices are noisy — checking "is price >= threshold" on every 5-minute tick sounds simple, but it isn't, because there are two very different kinds of alert semantics hiding inside one word ("trigger"): Holding conditions (price threshold): should fire every tick the condition holds, so users get reminded, but not so often it's spam. Crossing conditions (% change over a period, ATH/ATL, daily breakout): should fire once when the state flips, not on every subsequent tick where the crossed state is still true. Get this wrong and you either spam users into muting the bot, or you silently drop the one alert they actually wanted. I ended up modeling each checker as a small state machine: it reads its previous state from a JSONB column, computes the new state, and returns both the trigger decision and the state to persist — checkers themselves hold zero in-memory state, which also means they're trivially restartable and testable in isolation with no mocking needed beyond the state dict. On top of that, single-tick signals turned out to be genuinely noisy — a 5-minute price wobble can look identical to the start of a real move. The fix was a "confirm_checks" counter: a condition has to hold for N consecutive ticks before it fires, and the counter resets to zero on any non-triggering tick. Combined with a per-condition cooldown after firing, this cut false positives dramatically without adding real latency for genuine moves (most of them stay confirmed well past N ticks anyway). Reliability details that mattered more than I expected A few things that seemed like nice-to-haves during design turned out to matter a lot in practice: XAUTOCLAIM on every tick. If a worker process dies between XREADGROUP and XACK , that message just sits in the consumer's pending entries list forever unless something reclaims it. A periodic XAUTOCLAIM with a 30s idle threshold closes that gap — worker restarts (which happen, especially during deploys) stop silently losing in-flight messages. Deferred cache/notification writes until after DB commit. Each pipeline run happens inside its own session; Redis writes (cache sync, notification push) are buffered in memory and only flushed after the transaction actually commits. Otherwise a rolled-back DB write could still produce a notification for data that technically doesn't exist yet. Cache-miss reconciliation. Redis runs allkeys-lru , so under memory pressure a subscription detail key can get evicted independently of the index that references it. Instead of silently treating that as "no active subscription," a miss triggers a Postgres lookup to reconcile — restore to cache if still active, drop from the index if genuinely gone. An evicted cache entry should never be the reason a user misses an alert. Watchdog + circuit breaker on the workers. Each stream consumer runs under a supervisor that restarts it with exponential backoff on crash, but stops retrying after 10 crashes in 30 minutes rather than restart-looping forever and hammering the DB/Redis. What I'd do differently If I started over, I'd model the checker state machine (holding vs. crossing vs. first-tick-safe) explicitly from day one instead of discovering the distinction empirically per alert type. Also would've put the confirm-check accumulator in from the start — retrofitting stateful accumulation onto checkers that were originally written as pure functions took more care than it should have. If anyone's dealt with similar noisy-signal problems (trading systems, monitoring/alerting, IoT sensor thresholds) I'd be curious how you handled the holding-vs-crossing distinction — did you converge on something similar, or a different model entirely? Full architecture writeup (with the Redis key reference, DB schema, and middleware stack) is up on GitHub Pages if anyone wants the deeper dive: https://serhiibogomaz.github.io/crypto-alert-bot/

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/serhiibogomaz/building-a-telegram-crypto-alert-bot-with-redis-streams-and-the-false-positive-problem-nobody-ane

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
