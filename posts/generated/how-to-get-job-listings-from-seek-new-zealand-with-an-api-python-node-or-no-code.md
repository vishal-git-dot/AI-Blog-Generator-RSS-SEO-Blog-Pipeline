---
title: "How to get job listings from SEEK New Zealand with an API (Python, Node or no code)"
slug: "how-to-get-job-listings-from-seek-new-zealand-with-an-api-python-node-or-no-code"
author: "Big Man"
source: "devto_python"
published: "Mon, 09 Nov 2026 05:08:24 +0000"
description: "SEEK is New Zealand's biggest job board. If you want its listings in a spreadsheet, a database or an automation (a morning feed of new jobs in your region, s..."
keywords: "job, seek, apify, client, salary, scraper, run, jobs"
generated: "2026-11-09T05:39:49.712768"
---

# How to get job listings from SEEK New Zealand with an API (Python, Node or no code)

## Overview

SEEK is New Zealand's biggest job board. If you want its listings in a spreadsheet, a database or an automation (a morning feed of new jobs in your region, salary benchmarking, or a list of companies hiring right now), copying ads by hand doesn't scale. This tutorial uses Seek NZ Job Scraper , an Apify actor I built that reads SEEK's own JSON search API for seek.co.nz. It needs no browser and no proxy, so a run takes seconds. The full examples are on GitHub: auto-actor/seek-nz-job-scraper . What people use it for A fresh list of jobs in one region every morning, pushed to a Google Sheet or Slack. Salary benchmarking by classification or region. Lists of companies that are hiring right now (the company field), for sales or recruiting. Input { "keywords" : "carpenter" , "where" : "Auckland" , "maxItems" : 50 } keywords and where work the way they do on seek.co.nz; maxItems caps the number of jobs. Python """ Run Seek NZ Job Scraper on Apify and print the results. pip install apify-client export APIFY_TOKEN=... # Apify Console -> Settings -> Integrations python example.py """ import os from apify_client import ApifyClient client = ApifyClient ( os . environ [ " APIFY_TOKEN " ]) run = client . actor ( " daedal_quintuplet/seek-nz-job-scraper " ). call ( run_input = { " keywords " : " carpenter " , " where " : " Auckland " , " maxItems " : 50 } ) jobs = client . dataset ( run [ " defaultDatasetId " ]). iterate_items () for job in jobs : print ( job [ " title " ], " | " , job [ " company " ], " | " , job . get ( " salary " ) or " no salary listed " , " | " , job [ " url " ]) Node.js // Run Seek NZ Job Scraper on Apify and print the results. // // npm install apify-client // APIFY_TOKEN=... node example.js (token: Apify Console -> Settings -> Integrations) const { ApifyClient } = require ( ' apify-client ' ); async function main () { const client = new ApifyClient ({ token : process . env . APIFY_TOKEN }); const run = await client . actor ( ' daedal_quintuplet/seek-nz-job-scraper ' ). call ({ " keywords " : " carpenter " , " where " : " Auckland " , " maxItems " : 50 }); const { items } = await client . dataset ( run . defaultDatasetId ). listItems (); for ( const job of items ) { console . log ( job . title , ' | ' , job . company , ' | ' , job . salary || ' no salary listed ' , ' | ' , job . url ); } } main (). catch (( err ) => { console . error ( err ); process . exit ( 1 ); }); No code: one HTTP request Works from n8n, Make, Zapier or curl: curl -X POST "https://api.apify.com/v2/acts/daedal_quintuplet~seek-nz-job-scraper/run-sync-get-dataset-items?token= $APIFY_TOKEN " \ -H "Content-Type: application/json" \ -d '{"keywords": "carpenter", "where": "Auckland", "maxItems": 50}' What you get One row per job: Field Meaning id SEEK job id title Job title company Advertiser locations One or more locations salary Salary text as shown on SEEK, when the ad states one workTypes Full time, Part time, Contract/Temp, Casual/Vacation classifications SEEK classification listingDate When the ad was listed (ISO 8601) teaser First lines of the ad bulletPoints Up to three selling points, often empty isFeatured Paid placement flag url Link to the ad Only the fields SEEK returns in search results are included, not the full ad text. Price $0.001 per job ($1 per 1,000), paid per result, with no monthly fee. Apify's free plan includes $5 of usage a month, which is enough to try it. If you need Australian jobs, there's a matching Seek AU Job Scraper . Links: Store page · GitHub examples

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hmm_bigman/how-to-get-job-listings-from-seek-new-zealand-with-an-api-python-node-or-no-code-23ki

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
