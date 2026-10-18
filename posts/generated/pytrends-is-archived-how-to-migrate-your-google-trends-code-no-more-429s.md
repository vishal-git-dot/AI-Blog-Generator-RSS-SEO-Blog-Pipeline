---
title: "pytrends is archived: how to migrate your Google Trends code (no more 429s)"
slug: "pytrends-is-archived-how-to-migrate-your-google-trends-code-no-more-429s"
author: "Rimu Labs"
source: "devto_python"
published: "Sun, 18 Oct 2026 03:23:35 +0000"
description: "For years pytrends was how Python developers got Google Trends data. Its GitHub repository is now archived (read-only), and the last release on PyPI, 4.9.2, ..."
keywords: "pytrends, google, trends, past, keyword, client, now, your"
generated: "2026-10-18T03:57:53.279645"
---

# pytrends is archived: how to migrate your Google Trends code (no more 429s)

## Overview

For years pytrends was how Python developers got Google Trends data. Its GitHub repository is now archived (read-only), and the last release on PyPI, 4.9.2, came out in April 2023. Google rate-limits Trends heavily, so pytrends scripts that used to work now stop with HTTP 429 "Too Many Requests" errors, and nobody is fixing the library any more. This post maps each pytrends call to a maintained alternative, so you can migrate without rewriting your analysis. Your options Keep pytrends and slow down. Sleep between requests, retry with backoff and send fewer keywords per payload. That can keep a small script alive, but it breaks again whenever Google changes the internal endpoints pytrends relies on. The official Google Trends API. Google announced an official API in July 2025. It's an alpha with access by application only, so most projects can't use it yet. A maintained hosted API. We maintain a Google Trends Scraper on Apify. It paces and retries requests for you and returns the same data pytrends did, as JSON. You call it from Python with Apify's official client. pytrends calls and their replacements pytrends Google Trends Scraper build_payload(kw_list, timeframe, geo, cat, gprop) Input searchTerms , timeRange , geo , category , searchType interest_over_time() interestOverTime : [{date, value, isPartial}] . Set "compare": true to put up to 5 keywords on one 0-100 scale, like a multi-keyword payload interest_by_region() interestByRegion : [{geoCode, geoName, value}] related_queries() relatedQueries.top and relatedQueries.rising trending_searches() , realtime_trending_searches() "mode": "trendingNow" with trendingGeos , e.g. ["US", "GB"] related_topics() , top_charts() , suggestions() Not available Timeframes: now 1-H → past-hour , now 4-H → past-4-hours , now 1-d → past-day , now 7-d → past-7-days , today 1-m → past-30-days , today 3-m → past-90-days , today 12-m → past-12-months , today 5-y → past-5-years , all → since-2004 . A custom "2026-01-01 2026-06-30" becomes startDate and endDate . gprop: "" → web , images , news , froogle → shopping , youtube . Before and after A typical pytrends script: from pytrends.request import TrendReq pytrends = TrendReq ( hl = " en-US " , tz = 360 ) pytrends . build_payload ([ " crm " , " erp " ], timeframe = " today 12-m " , geo = " US " ) df = pytrends . interest_over_time () # one column per keyword The same DataFrame from the maintained API ( pip install apify-client pandas ): import pandas as pd from apify_client import ApifyClient # apify-client 3.x client = ApifyClient ( " YOUR_APIFY_TOKEN " ) run = client . actor ( " rimulabs/google-trends-insights " ). call ( run_input = { " searchTerms " : [ " crm " , " erp " ], " compare " : True , # one 0-100 scale, like a pytrends payload " timeRange " : " past-12-months " , " geo " : " US " , " sections " : [ " interestOverTime " ], }) rows = [ { " date " : p [ " date " ], " keyword " : r [ " keyword " ], " value " : p [ " value " ]} for r in client . dataset ( run . default_dataset_id ). iterate_items () for p in r [ " interestOverTime " ] ] df = pd . DataFrame ( rows ). pivot ( index = " date " , columns = " keyword " , values = " value " ) Each keyword record also carries a plain-language summary in insights (average, latest and peak interest, and whether the trend is rising, falling or stable), so you may not need your own smoothing code. Trending searches run = client . actor ( " rimulabs/google-trends-insights " ). call ( run_input = { " mode " : " trendingNow " , " trendingGeos " : [ " US " , " GB " ], " maxTrendingPerGeo " : 20 , }) A real result for the US on 18 October 2026, shortened: { "geo" : "US" , "title" : "oilers" , "approxTraffic" : "1000+" , "publishedAt" : "2026-10-18T03:00:00.000Z" , "news" : [{ "title" : "Zach Hyman tallies goal for Edmonton Oilers on the power play" , "source" : "ESPN" }] } Things that work differently No session to manage. There's no TrendReq , cookies or proxy settings to look after. Each run is one request from your side. Batch keywords freely. Without compare , each keyword gets its own report on its own 0-100 scale, which is what most monitoring jobs want. Values are still relative. Google Trends reports interest from 0 to 100, not search volumes, whichever tool you use. Cost: $3.00 per 1,000 keyword reports, or $0.50 per 1,000 trending searches. A daily job tracking 20 keywords costs about $1.80 a month. The full guide, kept up to date, is at rimulabs.com/guides/pytrends-alternative . Disclosure: Rimu Labs builds and maintains the Actor in this post. It was written by the AI assistant for Rimu Labs and checked against real runs on 18 October 2026. Questions or corrections: support@rimulabs.com .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rimulabs/pytrends-is-archived-how-to-migrate-your-google-trends-code-no-more-429s-4e63

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
