---
title: "How I Built a Financial Data API Using SEC EDGAR and Python in 2 Days with no prior experience."
slug: "how-i-built-a-financial-data-api-using-sec-edgar-and-python-in-2-days-with-no-prior-experience"
author: "Jethro Kirk"
source: "devto_python"
published: "Fri, 26 Jun 2026 09:26:07 +0000"
description: "I first became aware of a gap in the market a couple weeks ago while scrolling Reddit. Hoardes of people were enquiring after structured earnings transcript ..."
keywords: "data, guidance, every, api, sec, edgar, transcript, free"
generated: "2026-06-26T09:38:14.828129"
---

# How I Built a Financial Data API Using SEC EDGAR and Python in 2 Days with no prior experience.

## Overview

I first became aware of a gap in the market a couple weeks ago while scrolling Reddit. Hoardes of people were enquiring after structured earnings transcript data without paying $149/mo from the organisations that provide it, those organisations also didn't offer any historical data older than 2022. So I sat with Opus and began to study how such tool are structured and built - two days later I have the finished product (filingapi.dev). Here's how I built it: Disclosure: this is my own project. The Problem Financial transcript data is locked behind expensive paywalls. Financial Modeling Prep charges $149/mo for transcript access. Bloomberg requires enterprise contracts. The few free tools on Apify are broken or abandoned. Meanwhile, SEC EDGAR is completely free, has no rate limits worth worrying about, and contains every 8-K filing from every public company. The data is there — it just needs parsing. Architecture SEC EDGAR → Scraper → Parser → SQLite → FastAPI → Customer The stack is simple: FastAPI for the API layer SQLite for storage (good enough for MVP) httpx for async HTTP requests BeautifulSoup for HTML parsing Stripe for billing Step 1: EDGAR CIK Resolver Every company on EDGAR has a CIK number. SEC publishes a JSON file mapping tickers to CIKs: pythondef get_cik_by_ticker(self, ticker: str) -> str: resp = self.client.get( " https://www.sec.gov/files/company_tickers.json " ) data = resp.json() for entry in data.values(): if entry["ticker"].upper() == ticker.upper(): return str(entry["cik_str"]).zfill(10) Step 2: Pulling 8-K Filings With the CIK, you can pull every filing from the submissions API: pythonresp = self.client.get( f" https://data.sec.gov/submissions/CIK{cik}.json " ) filings = resp.json()["filings"]["recent"] Filter for form == "8-K" and you have every material event filing. Step 3: The Real Value — Exhibit 99.1 The 8-K itself is just a notice. The actual earnings press release is in Exhibit 99.1, attached to the filing. I built a fetcher that hits the filing index page, finds the 99.1 link, and downloads the full press release. This is where the guidance language lives: "revenue of $111.2 billion", "raised guidance", "record earnings per share". Step 4: Guidance Language Extraction I scan every sentence in the exhibit for forward-looking keywords: pythonGUIDANCE_KEYWORDS = [ "guidance", "outlook", "forecast", "expects", "revenue of", "earnings per share", "record revenue", "raised guidance", "lowered guidance", "margin pressure", ] def extract_guidance(self, text: str) -> list[dict]: sentences = re.split(r'(?<=[.!?])\s+', text) results = [] for sent in sentences: matched = [kw for kw in GUIDANCE_KEYWORDS if kw in sent.lower()] if matched and len(sent) > 30: results.append({"text": sent, "keywords": matched}) return results Step 5: Earnings Call Transcripts For transcripts, I scrape Motley Fool's free archive. Each transcript page has a consistent structure — tags with speaker names. The scraper identifies speakers, separates prepared remarks from Q&A, and tags roles (CEO, CFO, Analyst). The key discovery: the container with the transcript body is always the with the most direct children. Not the tag — that's a related content card. Step 6: On-Demand Fetching Instead of pre-scraping every company, I built an on-demand system. Client requests a ticker → check database → miss → scrape → store → return. Next request is instant from cache. This means the API covers any US-listed company without maintaining a massive scraping pipeline. What It Returns A real request for NVDA guidance: bashcurl -H "X-API-Key: YOUR_KEY" \ https://filingapi.dev/v1/filings/NVDA/guidance Returns every forward-looking sentence from NVIDIA's press releases, with keywords flagged. No manual reading required. Deployment VPS: $6/mo Vultr instance (1 vCPU, 1GB RAM) Nginx reverse proxy Let's Encrypt for HTTPS Systemd service that survives reboots Cron job running daily ingestion at 6am UTC Total infrastructure cost: $6/mo + $10/yr for the domain. What I Learned EDGAR is underrated. Zero anti-bot measures, free, comprehensive. Most fintech startups charge hundreds for data that's sitting there for free. Ship the differentiator first. Transcript APIs already exist. Guidance language extraction from 8-K exhibits doesn't. Lead with what's unique. On-demand beats batch. Caching on first request is better than trying to pre-scrape 8,000 companies before launch. Try It The API is live at filingapi.dev with a free tier (50 requests/day, instant signup). Currently covering ~460 tickers with 1,400+ parsed filings. Docs: filingapi.dev/docs Happy to answer questions about the build or take feature requests.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jethro_kirk_94cce29b139fa/how-i-built-a-financial-data-api-using-sec-edgar-and-python-in-2-days-with-no-prior-experience-1n29

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
