---
title: "How to scrape Glassdoor jobs and salaries into Excel or Python (no login, no API key)"
slug: "how-to-scrape-glassdoor-jobs-and-salaries-into-excel-or-python-no-login-no-api-key"
author: "Norbert Sobala"
source: "devto_python"
published: "Mon, 19 Oct 2026 21:31:36 +0000"
description: "Glassdoor is one of the few job boards that shows a salary range next to the job : either the employer's own or a Glassdoor estimate. It also shows the compa..."
keywords: "jobs, you, salary, glassdoor, only, per, data, job"
generated: "2026-10-19T22:10:53.096692"
---

# How to scrape Glassdoor jobs and salaries into Excel or Python (no login, no API key)

## Overview

Glassdoor is one of the few job boards that shows a salary range next to the job : either the employer's own or a Glassdoor estimate. It also shows the company rating . That makes the data useful beyond job hunting. Two common uses: Salary benchmarking. What do product managers in Berlin actually get offered? Sales and recruiting. Which companies are hiring right now, and for which roles? A company opening five sales positions this month is usually a company with budget. Glassdoor has no public API for this, and logged-out visitors only see the first page of results. This guide uses a ready-made scraper on Apify that handles both problems. You can get the data without writing any code, or call it from Python. What you get Every job comes back as one clean record: Field Example title Product Manager (m/w/d) company Lokalleads GmbH location / country Berlin, Germany salaryMin / salaryMax 60000 / 60000 salaryCurrency / salaryPeriod EUR / year salaryIsEstimate false (set by the employer, not a Glassdoor estimate) salaryYearlyMinEur 60000 (normalised to EUR per year, so you can compare countries) remote hybrid easyApply true postedAt 2026-10-14 You can also turn on: Full descriptions , which add the whole job text, employment type and industry. Company signals , which add one summary record per company: open roles, jobs posted in the last 7 days, remote share and median salary. This is handy for spotting companies that are scaling up. Option 1: no code (2 minutes) Open Glassdoor Jobs Scraper and click Try for free . Type your search, e.g. product manager , choose a location ( Berlin ) and a country. Optionally tick Only jobs with salary , Remote only , or a date range such as Posted in the last 7 days . Click Start . When the run finishes, export to Excel, CSV or JSON , or send the data straight to Google Sheets. When we ran "product manager" in Berlin , 10 jobs came back in under a minute. Two of them had a salary published by the employer: €60,000 and €72,000 a year. The employers ranged from small agencies to Bundesdruckerei and Berliner Sparkasse. How many listings carry a salary depends on the country. Several US states require pay ranges in job ads, so US searches usually return far more numbers than German ones. If you only want listings with pay, tick Only jobs with salary . Option 2: Python pip install apify-client pandas from apify_client import ApifyClient import pandas as pd client = ApifyClient ( " YOUR_APIFY_TOKEN " ) # Console → Settings → API & Integrations run = client . actor ( " liveclaude/glassdoor-jobs-scraper " ). call ( run_input = { " searchQueries " : [ " data analyst " , " data engineer " ], " locations " : [ " London " ], " country " : " gb " , " postedWithin " : " week " , " onlyWithSalary " : True , " maxJobsPerSearch " : 200 , }) jobs = list ( client . dataset ( run [ " defaultDatasetId " ]). iterate_items ()) df = pd . DataFrame ( jobs ) # median advertised salary per search, in EUR per year print ( df . groupby ( " searchQuery " )[[ " salaryYearlyMinEur " , " salaryYearlyMaxEur " ]]. median ()) df . to_excel ( " glassdoor_jobs.xlsx " , index = False ) The salaryYearlyMinEur and salaryYearlyMaxEur fields are already converted to euros per year. That lets you compare London with Sydney or New York without converting anything yourself. Keep it fresh automatically Add a Schedule in Apify, for example every Monday at 8:00, and turn on Only new jobs . Each run then returns only listings you haven't seen before. From there you can push new jobs to Slack or email as alerts, or append them to a Google Sheet and keep a running salary tracker. Make, Zapier and n8n work too if you want the data in a CRM. What does it cost? You pay per result: $0.50 per 1,000 jobs , and $3 per 1,000 if you also want full descriptions. Platform costs are included. A weekly tracker of a few hundred jobs costs cents. Apify's free plan includes monthly credit, which is enough to try it. A note on responsible use The scraper collects only what Glassdoor shows publicly to logged-out visitors. It does not log in and does not collect reviews written by individuals. If you store data about people (for example, recruiters' names in descriptions), treat it according to GDPR or your local law. Questions or a missing field? Open an issue on the Actor page . Requests usually ship within a few days. This tutorial was written with AI assistance and checked by the author. All numbers come from a real run of the scraper.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/norbertso/how-to-scrape-glassdoor-jobs-and-salaries-into-excel-or-python-no-login-no-api-key-5352

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
