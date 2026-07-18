---
title: "How to Scrape TikTok Email & Profile — Free No-Code Guide (2026)"
slug: "how-to-scrape-tiktok-email-profile-free-no-code-guide-2026"
author: "Logiover"
source: "devto_python"
published: "Sat, 18 Jul 2026 07:25:47 +0000"
description: "If you need to pull TikTok Email & Profile data at scale and there's no clean official API, this guide shows how to export it to JSON, CSV or Excel in a coup..."
keywords: "email, tiktok, profile, apify, scraper, csv, excel, run"
generated: "2026-07-18T08:00:40.325052"
---

# How to Scrape TikTok Email & Profile — Free No-Code Guide (2026)

## Overview

If you need to pull TikTok Email & Profile data at scale and there's no clean official API, this guide shows how to export it to JSON, CSV or Excel in a couple of minutes — with no scraping code to maintain. We'll use the TikTok Email & Profile Scraper (Bulk) , a hosted scraper on the Apify platform. You only need a free Apify token — no TikTok Email & Profile login, no proxies, no reverse-engineering. What data you get Each run returns structured records with fields like: username nickname followerCount heartCount email phone language verified profileUrl userId secUid privateAccount bio bioLink Results are paginated automatically — you can pull thousands of rows per run and export them as JSON, CSV, Excel, JSONL or XML . Option 1 — No code (Apify Console) Open the actor: https://apify.com/logiover/tiktok-profile-email-scraper Click Try for free . Leave the input empty for a broad sample, or set the fields below. Run it, then Export the dataset as CSV/JSON/Excel. Option 2 — Node.js npm install tiktok-profile-email-scraper const scrape = require ( " tiktok-profile-email-scraper " ); ( async () => { const items = await scrape ({}, { token : process . env . APIFY_TOKEN }); console . log ( items . length , " results " ); console . log ( items [ 0 ]); })(); Option 3 — Python pip install tiktok-profile-email-scraper from tiktok_profile_email_scraper import scrape items = scrape ({}, token = " YOUR_APIFY_TOKEN " ) print ( len ( items ), " results " ) print ( items [ 0 ]) Grab a free token at https://console.apify.com/account/integrations . Input options Field Type What it does profiles array TikTok profiles onlyWithEmail boolean Only profiles with an email maxConcurrency integer Max concurrency maxResults integer Max results proxyConfiguration object Proxy Common use cases Build a fresh TikTok Email & Profile dataset for analysis or dashboards Feed TikTok Email & Profile records into your own app, CRM or spreadsheet Monitor changes on a schedule and get alerts via webhooks Enrich leads or research with up-to-date TikTok Email & Profile data Automation & export Because it runs on Apify, you can schedule it, trigger it via webhook, and pipe results into Google Sheets, S3, Zapier, Make or n8n . Every run's dataset is downloadable as CSV, JSON, JSONL, Excel or XML. FAQ Do I need an API key? Only a free Apify token. No TikTok Email & Profile account needed. How many results can I get? Thousands per run; raise the limit to pull more. Is it an official TikTok Email & Profile API? No — it's an unofficial, maintained alternative when there's no official or affordable API. Can I export to CSV/Excel? Yes — JSON, CSV, JSONL, Excel and XML. ▶️ Run the TikTok Email & Profile Scraper (Bulk) on Apify: https://apify.com/logiover/tiktok-profile-email-scraper 📚 Docs & code examples: https://github.com/logiover/tiktok-profile-email-scraper 🧰 More scrapers: https://apify.com/logiover

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/l0gi0ver/how-to-scrape-tiktok-email-profile-free-no-code-guide-2026-1bgg

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
