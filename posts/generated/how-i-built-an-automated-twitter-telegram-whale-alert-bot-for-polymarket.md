---
title: "How I built an automated Twitter + Telegram whale alert bot for Polymarket"
slug: "how-i-built-an-automated-twitter-telegram-whale-alert-bot-for-polymarket"
author: "Manpreet Brar"
source: "devto_webdev"
published: "Mon, 10 Aug 2026 01:45:58 +0000"
description: "Built WhaleTrack — it tracks big Polymarket traders and alerts when they place large bets. Here's the technical stack behind the automated alert system. The ..."
keywords: "twitter, telegram, alert, polymarket, api, card, bot, tweet"
generated: "2026-08-10T02:10:38.790417"
---

# How I built an automated Twitter + Telegram whale alert bot for Polymarket

## Overview

Built WhaleTrack — it tracks big Polymarket traders and alerts when they place large bets. Here's the technical stack behind the automated alert system. The core loop (runs every 5 min): Polls Polymarket's API for recent trades across known whale wallets Detects new bets above $10K threshold Sends Telegram alert immediately Waits 10 min (Telegram subscribers get early access) Posts to Twitter with a visual card Tweet card generation: Puppeteer renders an HTML card → screenshot → PNG Uploaded via Twitter media API (v1.1) before posting text via v2 Falls back to text-only if Puppeteer fails One lesson on Twitter character limits: Twitter's 280 weighted char limit counts URLs as 23 chars regardless of length. My referral link was getting silently truncated because the tweet was ~336 weighted chars. Fixed by restructuring the tweet and adding a proper twitterLen() counter. Stack: 1.Node.js (single process, 24/7) 2.Bullpen CLI for Polymarket data 3.Puppeteer for card screenshots 4.Twitter API v1.1 (media) + v2 (tweets) 5.Telegram Bot API 6.Vercel for the web app Live at whaletrack.app. The full alert bot is ~1,200 lines of Node.js. Happy to share specific snippets if useful.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/manpreet_brar_264e408885a/how-i-built-an-automated-twitter-telegram-whale-alert-bot-for-polymarket-1ahp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
