---
title: "Get every new Xing job, with salaries, into a spreadsheet every morning"
slug: "get-every-new-xing-job-with-salaries-into-a-spreadsheet-every-morning"
author: "Ángel Panadero Rodríguez"
source: "devto_python"
published: "Fri, 06 Nov 2026 22:38:50 +0000"
description: "If you work with the German, Austrian or Swiss job market, whether in recruiting, HR tech, labour-market research or a job board, you have probably wanted Xi..."
keywords: "job, you, jobs, xing, scraper, get, every, apify"
generated: "2026-11-06T22:54:48.602565"
---

# Get every new Xing job, with salaries, into a spreadsheet every morning

## Overview

If you work with the German, Austrian or Swiss job market, whether in recruiting, HR tech, labour-market research or a job board, you have probably wanted Xing's job ads as data instead of web pages. Xing is the leading professional network in the DACH region, with around half a million active job postings at any time and thousands of new ones every day. In this post I show how to get them as clean JSON, CSV or Excel. That includes salary ranges, remote/hybrid information and career level, and a daily feed that only returns the jobs published since yesterday. You don't need to write a scraper: we'll use a ready-made one on Apify, called from Python. What you get for each job { "title" : "Python Developer Financial Services (all genders)" , "company" : "Exxeta" , "companySize" : "1.001-5.000 Mitarbeitende" , "city" : "Berlin" , "workplace" : "hybrid" , "employmentType" : "FULL_TIME" , "careerLevel" : "Mit Berufserfahrung" , "discipline" : "IT und Softwareentwicklung" , "language" : "de" , "salaryMin" : 59000 , "salaryMax" : 86000 , "salaryCurrency" : "EUR" , "salaryIsEstimate" : true , "datePosted" : "2026-09-17T05:36:36Z" , "applyUrl" : "https://career.exxeta.com/..." , "description" : "..." } Salaries are the interesting part. Many employers don't publish one, so Xing shows its own estimate instead. The data keeps them apart with salaryIsEstimate , so you can choose whether to trust estimates. 1. Get a token Create a free Apify account and copy your API token from Settings → API & Integrations . The free plan includes monthly credits, and the scraper costs $1 per 1,000 jobs, so testing is basically free. pip install apify-client export APIFY_TOKEN = "your-token" 2. Search by keyword and city import os from decimal import Decimal from apify_client import ApifyClient client = ApifyClient ( os . environ [ " APIFY_TOKEN " ]) run = client . actor ( " angelrxdriguez/xing-jobs-scraper " ). call ( run_input = { " mode " : " search " , " keywords " : [ " python " ], " locations " : [ " Berlin " ], " maxItems " : 50 }, max_total_charge_usd = Decimal ( " 0.10 " ), # hard cap for this run ) dataset_id = run . default_dataset_id # run["defaultDatasetId"] on apify-client < 3 for job in client . dataset ( dataset_id ). iterate_items (): print ( job [ " title " ], " | " , job [ " company " ], " | " , job . get ( " workplace " ), " | " , job . get ( " salaryMax " )) Every keyword is searched in every city you list, and a single search can return more than 1,000 jobs. 3. Filter before you pay The filters run inside the scraper, so jobs that don't match are skipped and not charged. For example, English-language remote or hybrid jobs that pay at least €60k: run_input = { " mode " : " search " , " keywords " : [ " software engineer " , " data engineer " ], " locations " : [ " Berlin " , " München " , " Hamburg " ], " languages " : [ " en " ], " workplace " : [ " remote " , " hybrid " ], " minSalary " : 60000 , } If you're an English speaker looking for a job in Germany, that one query already saves you an evening of scrolling. 4. A daily feed of only the new jobs This is the mode I use the most. Instead of searching, feed mode reads Xing's public sitemaps, which list every active job, and onlyNewJobs remembers what you already received. Schedule it once a day and each run returns only the jobs published since the previous one: run_input = { " mode " : " feed " , " feedCities " : [ " Berlin " , " Hamburg " , " München " ], " feedKeywords " : [ " entwickler " , " developer " , " engineer " ], " onlyNewJobs " : True , " stateKey " : " my-daily-feed " , } The examples repo has a complete script that appends the new jobs to a CSV, ready for cron or Windows Task Scheduler. You can also skip code entirely: create a schedule in the Apify Console and connect the results to Google Sheets, Make or n8n. A note on doing this responsibly The scraper only uses pages that Xing's robots.txt allows for all crawlers. It collects job ads, not people's profiles, and it removes e-mail addresses and phone numbers from descriptions by default, so you don't end up storing recruiters' personal data. If you're in the EU, that matters for GDPR. Links Scraper: apify.com/angelrxdriguez/xing-jobs-scraper Examples in Python, Node.js and plain HTTP: github.com/angelrxdriguez/xing-jobs-api I built this scraper, so feedback is very welcome, especially on which fields or filters would make it more useful for you.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/angelrxdriguez/get-every-new-xing-job-with-salaries-into-a-spreadsheet-every-morning-3cjc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
