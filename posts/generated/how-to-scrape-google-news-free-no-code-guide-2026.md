---
title: "How to Scrape Google News — Free No-Code Guide (2026)"
slug: "how-to-scrape-google-news-free-no-code-guide-2026"
author: "Logiover"
source: "devto_python"
published: "Sat, 18 Jul 2026 07:26:51 +0000"
description: "If you need to pull Google News data at scale and there's no clean official API, this guide shows how to export it to JSON, CSV or Excel in a couple of minut..."
keywords: "google, news, apify, scraper, string, csv, excel, run"
generated: "2026-07-18T08:00:40.324467"
---

# How to Scrape Google News — Free No-Code Guide (2026)

## Overview

If you need to pull Google News data at scale and there's no clean official API, this guide shows how to export it to JSON, CSV or Excel in a couple of minutes — with no scraping code to maintain. We'll use the Google News Scraper - Articles by Keyword, Real URLs , a hosted scraper on the Apify platform. You only need a free Apify token — no Google News login, no proxies, no reverse-engineering. What data you get Each run returns structured records with fields like: title source publishedAt originalUrl description thumbnailUrl query sourceDomain Results are paginated automatically — you can pull thousands of rows per run and export them as JSON, CSV, Excel, JSONL or XML . Option 1 — No code (Apify Console) Open the actor: https://apify.com/logiover/google-news-scraper Click Try for free . Leave the input empty for a broad sample, or set the fields below. Run it, then Export the dataset as CSV/JSON/Excel. Option 2 — Node.js npm install apify-google-news-scraper const scrape = require ( " apify-google-news-scraper " ); ( async () => { const items = await scrape ({}, { token : process . env . APIFY_TOKEN }); console . log ( items . length , " results " ); console . log ( items [ 0 ]); })(); Option 3 — Python pip install google-news-scraper from google_news_scraper import scrape items = scrape ({}, token = " YOUR_APIFY_TOKEN " ) print ( len ( items ), " results " ) print ( items [ 0 ]) Grab a free token at https://console.apify.com/account/integrations . Input options Field Type What it does queries array Search keywords / topics to monitor topic string Topic category (optional, instead of queries) geoLocation string Location-based news (optional) topHeadlines boolean Or get top headlines (overrides everything) language string Language country string Country / region maxArticles integer Max articles per query/feed timeWindow string Time window fromDate string From date (ISO 8601, optional) toDate string To date (ISO 8601, optional) includeSources array Include only these sources (optional) excludeSources array Exclude these sources (optional) Common use cases Build a fresh Google News dataset for analysis or dashboards Feed Google News records into your own app, CRM or spreadsheet Monitor changes on a schedule and get alerts via webhooks Enrich leads or research with up-to-date Google News data Automation & export Because it runs on Apify, you can schedule it, trigger it via webhook, and pipe results into Google Sheets, S3, Zapier, Make or n8n . Every run's dataset is downloadable as CSV, JSON, JSONL, Excel or XML. FAQ Do I need an API key? Only a free Apify token. No Google News account needed. How many results can I get? Thousands per run; raise the limit to pull more. Is it an official Google News API? No — it's an unofficial, maintained alternative when there's no official or affordable API. Can I export to CSV/Excel? Yes — JSON, CSV, JSONL, Excel and XML. ▶️ Run the Google News Scraper - Articles by Keyword, Real URLs on Apify: https://apify.com/logiover/google-news-scraper 📚 Docs & code examples: https://github.com/logiover/google-news-scraper 🧰 More scrapers: https://apify.com/logiover

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/l0gi0ver/how-to-scrape-google-news-free-no-code-guide-2026-2jfk

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
