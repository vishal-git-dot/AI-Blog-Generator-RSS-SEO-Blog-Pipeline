---
title: "SAM.gov API Without an API Key: Pull Today’s Federal Contract Opportunities in Python"
slug: "samgov-api-without-an-api-key-pull-todays-federal-contract-opportunities-in-python"
author: "Loomwise"
source: "devto_python"
published: "Thu, 19 Nov 2026 15:20:07 +0000"
description: "SAM.gov's official Opportunities API wants an API key and caps you at a small number of requests per day. Most capture teams do not need that API at all. Eve..."
keywords: "set, api, aside, sam, gov, opportunities, you, extract"
generated: "2026-11-19T15:31:03.967319"
---

# SAM.gov API Without an API Key: Pull Today’s Federal Contract Opportunities in Python

## Overview

SAM.gov's official Opportunities API wants an API key and caps you at a small number of requests per day. Most capture teams do not need that API at all. Every night SAM.gov publishes a public daily extract of active contract opportunities. You can read it with no key, no login and no 10-request limit. That extract is what small businesses and capture teams actually want: title, agency, NAICS, set-aside, posted date, response deadline and a link back to the notice. What one day looks like A sample pulled from the Nov 8, 2026 extract ( 150 notices ) looked like this: Field In this sample Posted date All 150 on 2026-11-08 With a set-aside 79 of 150 Small Business set-aside 57 SDVOSB set-aside 11 WOSB set-aside 5 HUBZone set-aside 4 Top agency Dept of Defense (141) Four of those 150 notices were construction NAICS ( 23* ), including VA roof-equipment railings and a fluoroscopy-room prep job set aside for SDVOSB primes. Why people search for a "SAM.gov API" They usually want one of three things: A daily bid list filtered by NAICS and set-aside (this article). Sources Sought / pre-RFP signals (separate workflow). Who already won (that lives in FPDS / award data, not the opportunities extract). If you only need (1), skip the keyed API. No-code path Open the Federal Opportunities tool on Apify, set for example: { "naicsCodes" : [ "238220" , "236220" , "541511" ] , "setAsides" : [ "SBA" , "SDVOSBC" , "WOSB" ] , "postedWithinDays" : 7 , "maxResults" : 500 } Download Excel or CSV, or schedule it daily into Google Sheets. Price is $0.90 per 1,000 results (Apify free plan covers a few thousand a month). Sample data: loomwise.app/data/government-contract-leads . Python with the Apify client from apify_client import ApifyClient client = ApifyClient ( ) run = client . actor ( "loomwise/federal-opportunities" ) . call ( run_input = { "naicsCodes" : [ "238220" , "236220" ] , "postedWithinDays" : 3 , "maxResults" : 200 , } ) for opp in client . dataset ( run [ "defaultDatasetId" ] ) . iterate_items ( ) : print ( opp [ "postedDate" ] , opp [ "naicsCode" ] , opp . get ( "setAside" ) , opp [ "title" ] [ : 80 ] ) You still get structured fields ( title , agency , noticeType , naicsCode , setAside , responseDeadline , link ) without ever requesting a SAM.gov API key. Data: SAM.gov public opportunities extract. Not affiliated with GSA or SAM.gov. Always confirm dates and eligibility on the notice page before you bid.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/loomwise/samgov-api-without-an-api-key-pull-todays-federal-contract-opportunities-in-python-21b1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
