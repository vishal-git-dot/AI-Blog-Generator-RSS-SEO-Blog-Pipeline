---
title: "Google Jobs results as JSON, for $1 per 1,000 jobs (no proxies, no browser)"
slug: "google-jobs-results-as-json-for-1-per-1000-jobs-no-proxies-no-browser"
author: "eden"
source: "devto_python"
published: "Wed, 14 Oct 2026 16:40:13 +0000"
description: "Google Jobs is the best free job index on the web. It pulls listings from LinkedIn, Indeed, company career sites and hundreds of smaller boards into one sear..."
keywords: "jobs, job, google, you, apify, one, data, per"
generated: "2026-10-14T16:54:47.639020"
---

# Google Jobs results as JSON, for $1 per 1,000 jobs (no proxies, no browser)

## Overview

Google Jobs is the best free job index on the web. It pulls listings from LinkedIn, Indeed, company career sites and hundreds of smaller boards into one search. What it does not have is an API. The scrapers that fill that gap tend to break: they drive a browser through Google, get blocked, and you pay for failed runs. In October 2026 the most used one on the Apify Store failed 19% of its runs and charged $0.35 to $0.90 per 100 jobs, and another succeeded in only 1 of 500 runs in a month. So I built one that does not scrape Google from a browser at all. It reads Google Jobs through a commercial search-data API, so there are no proxies to rotate and nothing to break. This post shows how to use it. What you get per job You send one or more searches and a country, optionally a city. You get one record per job: { "query" : "data engineer" , "country" : "US" , "position" : 1 , "title" : "Senior Data Engineer" , "company" : "Acme Corp" , "location" : "Austin, TX" , "contract_type" : "Full-time" , "salary" : "$140K–$180K a year" , "salary_min" : 140000 , "salary_max" : 180000 , "salary_currency" : "USD" , "salary_period" : "year" , "posted_ago" : "2 days ago" , "source" : "LinkedIn" , "apply_url" : "https://..." } (Example of the output format.) What to expect from real data: in a test of 3 US searches (30 jobs), Google showed a salary on 5 of the 30 jobs. Many apply links go straight to the company's own career site. The full job description text is not included; the apply_url leads to it. Run it The tool is the Google Jobs Scraper Actor on Apify. From the console Open the Actor, type your searches, pick a country, optionally a city such as Austin,Texas , and press Start. Results appear as a table you can export to CSV, Excel or JSON. From curl curl -X POST "https://api.apify.com/v2/acts/hirepulse~google-jobs-scraper/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \ -H "Content-Type: application/json" \ -d '{"queries": ["data engineer"], "country": "US", "location": "Austin,Texas", "max_jobs_per_query": 50}' From Python from apify_client import ApifyClient client = ApifyClient ( " YOUR_APIFY_TOKEN " ) run = client . actor ( " hirepulse/google-jobs-scraper " ). call ( run_input = { " queries " : [ " account executive " , " sales development representative " ], " country " : " GB " , " employment_types " : [ " fulltime " ], }) for job in client . dataset ( run [ " defaultDatasetId " ]). iterate_items (): print ( job [ " title " ], " | " , job [ " company " ], " | " , job . get ( " salary " )) From an AI agent Add Apify's MCP server with this one tool to Claude, Cursor or any MCP client: https://mcp.apify.com?tools=hirepulse/google-jobs-scraper Then ask: "Which companies in Austin are hiring data engineers this week, and what do they pay?" Pricing $0.005 per search that returns jobs. Searches with no results are free. $0.001 per job. 100 jobs from one search cost about $0.11. You need an Apify account. You can try it on the free Apify plan: each free run returns the first 10 jobs of your first search. Full results need a paid Apify plan , because every search has a real data cost. Related If you track specific companies rather than roles, the ATS Job Scraper reads every open job, with full descriptions, straight from a company's Greenhouse, Lever, Ashby or Workable board, and tells you what changed since the last run.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ystudio3d/google-jobs-results-as-json-for-1-per-1000-jobs-no-proxies-no-browser-5e9k

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
