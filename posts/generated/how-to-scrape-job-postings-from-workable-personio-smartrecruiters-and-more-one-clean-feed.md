---
title: "How to Scrape Job Postings from Workable, Personio, SmartRecruiters and More (One Clean Feed)"
slug: "how-to-scrape-job-postings-from-workable-personio-smartrecruiters-and-more-one-clean-feed"
author: "Scrape-Smith"
source: "devto_python"
published: "Thu, 22 Oct 2026 16:32:26 +0000"
description: "How to Scrape Job Postings from Workable, Personio, SmartRecruiters and More Building a niche job board, tracking which competitors are hiring, or finding co..."
keywords: "job, ats, company, jobs, you, companies, workable, personio"
generated: "2026-10-22T16:56:20.008854"
---

# How to Scrape Job Postings from Workable, Personio, SmartRecruiters and More (One Clean Feed)

## Overview

How to Scrape Job Postings from Workable, Personio, SmartRecruiters and More Building a niche job board, tracking which competitors are hiring, or finding companies that just opened a "Head of Data" role all start the same way: you need job postings from many company career pages, in one consistent format. The good news is that most applicant tracking systems (ATS) publish official public job feeds so their customers' jobs can be syndicated. The bad news is that every ATS does it differently: Personio speaks XML, Teamtailor RSS, Workable and Recruitee JSON with different field names, SmartRecruiters a paginated REST API, and BambooHR its own list format. This tutorial shows how to pull all six into one normalized table with the ATS Jobs Scraper . Supported ATS and how to identify them Look at a company's careers page URL: ATS Careers URL looks like Input Workable apply.workable.com/ huggingface workable:huggingface Recruitee bunq .recruitee.com recruitee:bunq Personio acme .jobs.personio.de personio:acme Teamtailor polestar .teamtailor.com teamtailor:polestar SmartRecruiters jobs.smartrecruiters.com/ Ubisoft2 smartrecruiters:Ubisoft2 BambooHR bitly .bamboohr.com/careers bamboohr:bitly You can type ats:slug or just paste the careers URL. Mixing ATS in one run is fine. Tip: if a company's careers page is on its own domain, click any job. The apply link usually reveals which ATS is behind it. Step 1: Run the example Open the actor and click Try for free . The prefill includes a few real companies and a limit of 20 jobs per company. Within seconds: ats company title location remote postedAt teamtailor Polestar Head of Customer Engagement Benelux Beesd, Netherlands false 2026-10-15 workable Hugging Face ... Remote true ... Every row has the same fields regardless of source: ats, companySlug, company, id, title, location, city, country, remote, department, employmentType, experienceLevel, postedAt, url, applyUrl, description . If an ATS doesn't expose a field, it's null rather than missing. Step 2: Filter keyword : case-insensitive title filter, e.g. engineer or sales . onlyNewSince : skip jobs posted before a date. Combine with a daily schedule to get only new jobs each day. includeDescription : on by default. Turn it off for faster, title-only runs. Step 3: Daily "new jobs" feed from apify_client import ApifyClient import datetime yesterday = ( datetime . date . today () - datetime . timedelta ( days = 1 )). isoformat () client = ApifyClient ( " YOUR_APIFY_TOKEN " ) run = client . actor ( " scrape-smith/multi-ats-jobs-feed " ). call ( run_input = { " companies " : [ line . strip () for line in open ( " companies.txt " ) if line . strip ()], " onlyNewSince " : yesterday , " keyword " : " data " , " includeDescription " : False , }) for job in client . dataset ( run [ " defaultDatasetId " ]). iterate_items (): if " error " not in job : print ( f ' { job [ " company " ] } : { job [ " title " ] } ( { job [ " location " ] } ) { job [ " url " ] } ' ) Pipe that into Slack, email, or a static site generator and you have a niche job board backend. Use cases Niche job boards (remote, climate, Rust, EU startups) from hundreds of career pages. Competitive intelligence : hiring is a leading indicator. A competitor posting ten sales roles in Germany is telling you something. Sales prospecting : companies hiring for a role often need tools for that role. Recruiting research and labour-market analytics. Honest limitations Only these six ATS. Greenhouse, Lever, Ashby and Workday aren't covered by this actor. You need the company slug. The tool doesn't discover companies for you; you bring the list. Some ATS don't publish a posted date (so onlyNewSince can't filter those), and some don't expose remote flags. If a company disables its public feed or the slug is wrong, you get a free error row for that company and the rest continue. These are official public feeds meant for syndication, but check each company's terms if you republish job content, and always link to the original apply URL. Cost Pay per result: $0.005 per company feed fetched plus $0.001 per job. The test run costs about three cents. 1,000 jobs from 20 companies is $1.10. Platform usage is included. Wrap-up Six ATS, six formats, one table. If you're building anything on top of job data, try the ATS Jobs Scraper with the prefilled companies and then paste in your own list. Scrape-Smith builds small, cheap data tools on public and official APIs.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/scrape-smith/how-to-scrape-job-postings-from-workable-personio-smartrecruiters-and-more-one-clean-feed-25mh

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
