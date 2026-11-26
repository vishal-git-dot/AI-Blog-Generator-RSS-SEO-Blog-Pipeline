---
title: "Add Google Jobs to career-ops with one portals.yml entry"
slug: "add-google-jobs-to-career-ops-with-one-portalsyml-entry"
author: "krammer liu"
source: "devto_ai"
published: "Thu, 26 Nov 2026 07:37:43 +0000"
description: "career-ops is an open-source AI job search agent. It scans job sources, scores each posting against your CV, and keeps a tracker. Out of the box it reads com..."
keywords: "actor, data, engineer, jobs, run, career, one, apify"
generated: "2026-11-26T07:44:38.398302"
---

# Add Google Jobs to career-ops with one portals.yml entry

## Overview

career-ops is an open-source AI job search agent. It scans job sources, scores each posting against your CV, and keeps a tracker. Out of the box it reads company ATS boards (Greenhouse, Ashby, Lever and others). I wanted it to also see Google Jobs, because one Google Jobs search shows postings from LinkedIn, Indeed, Glassdoor, niche boards and company career pages together. career-ops already ships an apify provider plugin that can run any Apify Actor and map its output into the scanner. So this needs no code: one plugin switch, one token, and one portals.yml entry. Disclosure: I built the Actor used here ( Google Jobs Scraper on Apify ). It is a paid tool, billed per results page of up to 10 jobs. Prices are on the Actor page. 1. Turn on the apify plugin cp config/plugins.example.yml config/plugins.yml In config/plugins.yml , set: plugins : apify : enabled : true Then put your Apify API token in .env (Apify Console → Settings → API & Integrations): APIFY_TOKEN = your_token_here 2. Add a Google Jobs entry to portals.yml Add this under tracked_companies: in your portals.yml . Change the query and location to your own search. tracked_companies : - name : "Google Jobs — Data Engineer (Remote, US)" provider : apify actor : krammer/google-jobs-scraper input : queries : [ "data engineer" ] locations : [ "United States" ] remoteOnly : true datePosted : "7d" maxResultsPerSearch : 20 timeout_ms : 300000 field_map : title : title url : apply_options.0.link company : company location : location description : description Notes on the entry: url: apply_options.0.link — the Actor returns every place you can apply as a list of {title, link} . The plugin reads dotted paths, so this takes the first apply link. description: description — the plugin saves the full job description under jds/ , so the evaluation step reads the real JD instead of re-fetching the page. datePosted accepts any , 24h , 3d , 7d or 30d . maxResultsPerSearch goes up to 200. timeout_ms: 300000 gives the Actor run 5 minutes. The plugin default is 3 minutes. Your normal title_filter still applies to these results. 3. Run the scan node scan.mjs --dry-run This is the output from my run (career-ops a8ea6d1 , Node 26, 2026-11-25), trimmed: Companies scanned: 1 Total jobs found: 18 Filtered by title: 3 removed Duplicates: 0 skipped New offers added: 15 New offers: + Block | Remote Senior Data Engineer, Product | Oakland, CA + Eliassen Group | Remote Data Engineer: AWS, PySpark & Pipelines | Little Rock, AR + Afresh | Remote Staff Data Engineer, Analytics | Temecula, CA + Defense Unicorns | Remote Data Engineer - Agentic AI | Knoxville, TN + Integral | Data Engineer - AI & Machine Learning | Tysons, VA + Providence | Senior Data Engineer | Plainview, TX + Nelnet | Data Engineer - Full-time | Highlands Ranch, CO ... The Actor returned 18 jobs for 20 requested. It also wrote 18 job descriptions to jds/ . Remove --dry-run to save the results, then run the career-ops pipeline to score them. More than one search Each tracked_companies entry is one Actor run. To cover several roles or cities, put them in the same entry. The Actor runs every query in every location: input : queries : [ "data engineer" , "analytics engineer" ] locations : [ "Seattle, WA" , "Austin, TX" ] maxResultsPerSearch : 20 That is 4 searches in one run. What else the Actor returns career-ops only maps title, URL, company, location and description. The Actor also returns parsed salary ( salaryMin , salaryMax , salaryCurrency , salaryPeriod ), postedDate , jobTypes and workMode (remote / hybrid / on-site). If you use the data outside career-ops, those fields are in the same dataset.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/krammer/add-google-jobs-to-career-ops-with-one-portalsyml-entry-3bih

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
