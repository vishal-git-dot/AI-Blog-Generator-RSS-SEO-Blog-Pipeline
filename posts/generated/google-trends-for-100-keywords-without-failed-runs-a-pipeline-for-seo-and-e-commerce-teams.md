---
title: "Google Trends for 100 keywords without failed runs: a pipeline for SEO and e-commerce teams"
slug: "google-trends-for-100-keywords-without-failed-runs-a-pipeline-for-seo-and-e-commerce-teams"
author: "Omar Khandji"
source: "devto_python"
published: "Tue, 13 Oct 2026 22:21:32 +0000"
description: "If you run SEO or an online shop, you probably check Google Trends for a list of keywords every week: which products are rising, which queries are about to b..."
keywords: "google, keywords, keyword, run, trends, you, per, apify"
generated: "2026-10-13T22:28:13.078544"
---

# Google Trends for 100 keywords without failed runs: a pipeline for SEO and e-commerce teams

## Overview

If you run SEO or an online shop, you probably check Google Trends for a list of keywords every week: which products are rising, which queries are about to break out, which country is heating up. Doing that by hand for 100 keywords means 100 tabs. Doing it with a script usually means rate limits and half-empty results. Here is the short version: pass a list of keywords (or a Google Sheet) to one API call, and get one row per keyword with the direction, the % change, the top regions and the rising "breakout" queries already computed. The answer first I built a Google Trends Scraper on Apify . It reads Google Trends directly, works through your list four keywords at a time (each on its own Google session), and retries a keyword that Google rate-limits on a fresh session at the end of the run, up to two more times. A keyword that still fails comes back as an error row and is never charged. Measured on Apify on 7 October 2026, United States, with regions and related queries on: Test Keywords delivered Run time 40 keywords 40 of 40 64 seconds 100 keywords 100 of 100 3 min 39 s A run accepts up to 1,000 keywords. Working Python snippet from apify_client import ApifyClient client = ApifyClient ( " <YOUR_APIFY_TOKEN> " ) run = client . actor ( " om_kh/google-trends-scraper " ). call ( run_input = { " searchTerms " : [ " standing desk " , " ergonomic chair " , " monitor arm " ], " geo " : " US " , " timeRange " : " past_90_days " , " includeRelated " : True , " includeRegions " : True , }) for item in client . dataset ( run [ " defaultDatasetId " ]). iterate_items (): print ( item [ " keyword " ], item [ " trendDirection " ], item [ " changePct " ]) The inputs that matter for a keyword-list workflow: searchTerms : your keywords, up to 1,000 per run. spreadsheetId : a link or ID of a Google Sheet shared as "Anyone with the link". The first column is read, one keyword per row, so your team keeps the list in a sheet instead of in code. geo : two-letter country code ( US , FR , GB ...). Empty means worldwide. timeRange or customTimeRange ( 2025-01-01 2025-12-31 ). searchProperty : web , youtube , news , images or shopping . E-commerce teams often want shopping . compare : group keywords by 5 on the same 0-100 scale, like typing them together on Google Trends. maxTotalChargeUsd : a hard cost cap for the run. What the output looks like One row per keyword. This is the real example from the Actor's README (YouTube searches, year 2025, labels in French because language was fr ; lists cut to their first entries): { "type" : "keyword" , "keyword" : "chatgpt" , "geo" : "US" , "timeRange" : "2025-01-01 2025-12-31" , "searchProperty" : "youtube" , "comparedWith" : [ "claude ai" ], "averageInterest" : 60.1 , "peakInterest" : 100 , "peakDate" : "2025-08-03T00:00:00Z" , "latestInterest" : 53 , "trendDirection" : "rising" , "changePct" : 20.5 , "topRegions" : [{ "region" : "Virginie" , "code" : "US-VA" , "value" : 100 }], "relatedQueriesRising" : [{ "query" : "deepseek" , "value" : 104850 , "formattedValue" : "Record" }], "status" : "ok" } trendDirection and changePct are computed for you, so you can sort 100 or 1,000 keywords by momentum in a spreadsheet in seconds. The rising related queries include Google's "Breakout" queries, the earliest signal of a new trend. Values are Google's relative scale (100 is the peak for the period and place), not absolute search volumes. Run it on a schedule with Make or n8n You do not need to host any Python. In Make or n8n, use the Apify module/node and build three steps: Run an Actor : pick om_kh/google-trends-scraper , set spreadsheetId to your keyword sheet and geo to your market. Schedule the scenario every Monday morning. Get Dataset Items : use the default dataset of the run from step 1. Google Sheets: Add a Row : map keyword , trendDirection , changePct , peakDate and latestInterest to columns. Sort the results tab by changePct and the products or topics gaining momentum are at the top. Pricing $2 per 1,000 keyword rows, no start fee. The first 3 results of every run are free, a keyword Google could not return is not charged, and paid Apify plans get lower tier prices (see the Pricing tab). A 100-keyword weekly check is about $0.20 per run. Limits Google Trends values are relative, not search volumes. Very rare keywords may return no data; they are reported and not charged. For lists over 50 keywords, leave includeRelated on only if you need it, since it adds requests. Metro areas exist for the United States only. It reads public, aggregated data; use it in line with the terms that apply to you. MCP AI agents can call it through https://mcp.apify.com as om_kh/google-trends-scraper , so an assistant can check whether a topic is growing before it recommends it. More Actors and guides: https://omarkhandji-commits.github.io/apify-actor-catalogue/guides/ Disclosure: I built this Actor.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/omar_khandji_0135ce9388bb/google-trends-for-100-keywords-without-failed-runs-a-pipeline-for-seo-and-e-commerce-teams-59b2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
