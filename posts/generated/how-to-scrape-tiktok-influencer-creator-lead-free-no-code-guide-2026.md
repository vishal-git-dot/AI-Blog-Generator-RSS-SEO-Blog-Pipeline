---
title: "How to Scrape TikTok Influencer & Creator Lead — Free No-Code Guide (2026)"
slug: "how-to-scrape-tiktok-influencer-creator-lead-free-no-code-guide-2026"
author: "Logiover"
source: "devto_python"
published: "Tue, 14 Jul 2026 19:13:29 +0000"
description: "If you need to pull TikTok Influencer & Creator Lead data at scale and there's no clean official API, this guide shows how to export it to JSON, CSV or Excel..."
keywords: "creator, tiktok, lead, influencer, apify, finder, csv, excel"
generated: "2026-07-14T19:26:51.411616"
---

# How to Scrape TikTok Influencer & Creator Lead — Free No-Code Guide (2026)

## Overview

If you need to pull TikTok Influencer & Creator Lead data at scale and there's no clean official API, this guide shows how to export it to JSON, CSV or Excel in a couple of minutes — with no scraping code to maintain. We'll use the TikTok Influencer & Creator Lead Finder , a hosted scraper on the Apify platform. You only need a free Apify token — no TikTok Influencer & Creator Lead login, no proxies, no reverse-engineering. What data you get Each run returns structured records with fields like: username nickname followerCount email phone region verified foundForKeyword profileUrl secUid avatar followingCount heartCount videoCount Results are paginated automatically — you can pull thousands of rows per run and export them as JSON, CSV, Excel, JSONL or XML . Option 1 — No code (Apify Console) Open the actor: https://apify.com/logiover/tiktok-creator-lead-finder Click Try for free . Leave the input empty for a broad sample, or set the fields below. Run it, then Export the dataset as CSV/JSON/Excel. Option 2 — Node.js npm install tiktok-creator-lead-finder const scrape = require ( " tiktok-creator-lead-finder " ); ( async () => { const items = await scrape ({}, { token : process . env . APIFY_TOKEN }); console . log ( items . length , " results " ); console . log ( items [ 0 ]); })(); Option 3 — Python pip install tiktok-creator-lead-finder from tiktok_creator_lead_finder import scrape items = scrape ({}, token = " YOUR_APIFY_TOKEN " ) print ( len ( items ), " results " ) print ( items [ 0 ]) Grab a free token at https://console.apify.com/account/integrations . Input options Field Type What it does searchQueries array Niche keywords maxCreatorsPerQuery integer Max creators per keyword enrichProfiles boolean Enrich each creator's profile minFollowers integer Min followers maxFollowers integer Max followers requireEmail boolean Only creators with an email maxResults integer Max results proxyConfiguration object Proxy Common use cases Build a fresh TikTok Influencer & Creator Lead dataset for analysis or dashboards Feed TikTok Influencer & Creator Lead records into your own app, CRM or spreadsheet Monitor changes on a schedule and get alerts via webhooks Enrich leads or research with up-to-date TikTok Influencer & Creator Lead data Automation & export Because it runs on Apify, you can schedule it, trigger it via webhook, and pipe results into Google Sheets, S3, Zapier, Make or n8n . Every run's dataset is downloadable as CSV, JSON, JSONL, Excel or XML. FAQ Do I need an API key? Only a free Apify token. No TikTok Influencer & Creator Lead account needed. How many results can I get? Thousands per run; raise the limit to pull more. Is it an official TikTok Influencer & Creator Lead API? No — it's an unofficial, maintained alternative when there's no official or affordable API. Can I export to CSV/Excel? Yes — JSON, CSV, JSONL, Excel and XML. ▶️ Run the TikTok Influencer & Creator Lead Finder on Apify: https://apify.com/logiover/tiktok-creator-lead-finder 📚 Docs & code examples: https://github.com/logiover/tiktok-creator-lead-finder 🧰 More scrapers: https://apify.com/logiover

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/l0gi0ver/how-to-scrape-tiktok-influencer-creator-lead-free-no-code-guide-2026-5b3b

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
