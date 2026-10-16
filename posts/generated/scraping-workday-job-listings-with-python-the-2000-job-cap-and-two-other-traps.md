---
title: "Scraping Workday job listings with Python: the 2,000-job cap and two other traps"
slug: "scraping-workday-job-listings-with-python-the-2000-job-cap-and-two-other-traps"
author: "hiver"
source: "devto_python"
published: "Fri, 16 Oct 2026 16:07:22 +0000"
description: "Plenty of large employers post their openings on Workday careers sites, the *.myworkdayjobs.com and *.myworkdaysite.com pages: NVIDIA, Target, CVS Health, Fi..."
keywords: "jobs, site, job, page, workday, com, you, nvidia"
generated: "2026-10-16T16:24:14.484031"
---

# Scraping Workday job listings with Python: the 2,000-job cap and two other traps

## Overview

Plenty of large employers post their openings on Workday careers sites, the *.myworkdayjobs.com and *.myworkdaysite.com pages: NVIDIA, Target, CVS Health, Fidelity and Workday itself among them. Workday's documented REST API is for the employer's own HR systems and needs a login, so it is no help if you just want the public job list. The careers page, though, loads its jobs from a JSON endpoint that every visitor's browser calls, and you can call it too. Paging through that endpoint looks like a five-minute job. On a big site it isn't, and the loop fails without an error: you get a CSV that looks complete and isn't. Below are the three things we hit on NVIDIA's careers site on 2026-10-16, and a free standard-library script that handles them. The endpoint curl -s -X POST \ "https://nvidia.wd5.myworkdayjobs.com/wday/cxs/nvidia/NVIDIAExternalCareerSite/jobs" \ -H "Content-Type: application/json" \ -d '{"limit": 20, "offset": 0, "appliedFacets": {}, "searchText": ""}' The URL comes straight from the careers page: https://<tenant>.wdN.myworkdayjobs.com/<site> becomes https://<tenant>.wdN.myworkdayjobs.com/wday/cxs/<tenant>/<site>/jobs . (For wdN.myworkdaysite.com/recruiting/<tenant>/<site> it is https://wdN.myworkdaysite.com/wday/cxs/<tenant>/<site>/jobs .) Each reply has up to 20 jobPostings (title, locationsText , postedOn , externalPath ), a total , and facets , the site's own filters with a count per value. Trap 1: total is only on the first page Page 1 said "total": 2000 . The page at offset 20 said "total": 0 . A loop that re-reads total on every page stops after the second page. Read it once, from page 1. Trap 2: one search stops at 2,000 jobs, and then starts over NVIDIA's job-family filter counts added up to 2,718 open jobs, but page 1 reported 2,000. Past that, the endpoint did not return an empty page: at offset 2,000 it returned page 1 again, with "total": 2000 . So a loop that pages until it gets an empty page never ends, and a loop that trusts total silently drops about 700 jobs. The fix is to split the search. Pick the facet whose counts add up to the most jobs (for NVIDIA, jobFamilyGroup , 15 values), run one search per value with "appliedFacets": {"jobFamilyGroup": ["<id>"]} , and merge the results by externalPath . That gave 2,715 distinct jobs in about 4.5 minutes from our server, with a 0.2 second pause between requests. If one value is still at 2,000 on a bigger site, split it again by a second facet such as locationMainGroup . Trap 3: the list is a summary In the list, 1,028 of those 2,715 jobs (38%) had a location of just "2 Locations", "3 Locations" and so on, and 1,601 (59%) said "Posted 30+ Days Ago". A country filter on that text misses every multi-location job, and you can't sort by date. Each job's own record ( GET .../wday/cxs/<tenant>/<site> plus the job's externalPath ) has the real location , additionalLocations , country and startDate . It costs one request per job, so fetch it only when you need it. The script hiver-data/workday-jobs-scraper on GitHub has workday_jobs.py : Python 3.9+, no dependencies, MIT licensed, with offline tests that fake all three behaviours. python3 workday_jobs.py https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite # 2000 reported (the cap); splitting by jobFamilyGroup: 15 values, 2718 jobs # 2715 jobs -> workday_jobs.csv python3 workday_jobs.py https://wd1.myworkdaysite.com/en-US/recruiting/fmr/FidelityCareers --details --max 50 With --details , a row looks like this (real output, 2026-10-16): title,locations,country,posted,time_type,id "Software Engineer, DGX Cloud AI Infrastructure" , "US, CA, Santa Clara; US, TX, Austin; US, OR, Remote; US, WA, Remote; US, WA, Redmond" ,United States of America, 2026-10-15 ,Full time,JR 2019248 In the list, that job's location was just "5 Locations"; the record names all five. Many companies, or only their names The script reads one Workday site whose URL you already have. If you track a list of employers, some on Workday and some on Greenhouse, Lever, iCIMS or Oracle, and you only know their names, we (hiver) built the Workday Jobs Scraper & API on Apify for that. It finds each company's career board, does the splitting and the per-job record reads above, adds descriptions and pay ranges where the posting has them, and returns one table for all the companies. It costs $0.03 per company for up to 1,000 jobs and $0.01 per further 1,000 on Apify's free plan, so a site of NVIDIA's size is $0.05. Companies it cannot find cost nothing. Notes This reads only the public job listings each company publishes for job seekers. Keep the pause between requests and don't hammer a site; the script backs off on 429 and 5xx replies. Not affiliated with Workday or with any employer named here. The numbers are from one site on one day. If the endpoint behaves differently on a site you try, open an issue on the repo with the careers URL.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hiver/scraping-workday-job-listings-with-python-the-2000-job-cap-and-two-other-traps-19pg

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
