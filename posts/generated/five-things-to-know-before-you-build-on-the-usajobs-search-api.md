---
title: "Five things to know before you build on the USAJOBS Search API"
slug: "five-things-to-know-before-you-build-on-the-usajobs-search-api"
author: "Your Evenings Data"
source: "devto_python"
published: "Sat, 31 Oct 2026 11:32:33 +0000"
description: "USAJOBS publishes an official Search API ( data.usajobs.gov/api/Search ) for US federal job announcements. We built a scheduled job feed on it, and these are..."
keywords: "pay, jobs, you, api, usajobs, before, search, federal"
generated: "2026-10-31T11:58:36.462227"
---

# Five things to know before you build on the USAJOBS Search API

## Overview

USAJOBS publishes an official Search API ( data.usajobs.gov/api/Search ) for US federal job announcements. We built a scheduled job feed on it, and these are the details that shaped the code. Disclosure: the hosted version at the end is ours, and we charge for it. 1. Pay comes with an interval code Each pay range comes with a RateIntervalCode : PA for per year, PH for per hour, plus PD , PW , BW and PM for daily, weekly, biweekly and monthly. To compare jobs on salary, convert everything to a yearly figure. We use 2,087 hours for a year of hourly pay (the federal standard), 260 days, 52 weeks, 26 pay periods or 12 months. Filter on the top of the range, or you'll drop hourly jobs that pay well. 2. One query stops at 10,000 results The API won't page past 10,000 results for one query. A broad search such as "all jobs posted this month" can hit that limit without telling you. Narrow it by location, agency, occupational series or a posted-within window, and log it whenever a query reaches the limit, so a short result is never mistaken for a complete one. 3. Ask for public jobs explicitly Many announcements are open only to current federal employees or particular groups. If your users are the general public, request WhoMayApply=Public . It's also the only option the API serves to a key that hasn't been given extra authorisation. 4. Codes need a lookup table Schedule, appointment, service type and travel come back as codes. Map them to words (Full-time, Permanent, Competitive, Occasional travel) before anyone downstream sees them, or every consumer ends up writing their own mapping. 5. Announcements contain contact details Rows can carry an agency contact email and phone number, and the announcement text can include more of them, sometimes with a named person. Unless your use case needs them, drop the contact fields and mask emails and phone numbers in free text. Don't store full announcement text by default. The hosted version (disclosure: we built it) Our Apify Actor, Government Jobs API: USAJOBS , does all five for you: Yearly pay is worked out for every row with a standard pay interval, and the salary filter runs before you're charged. A free scan_limit row tells you when a search hit the 10,000 limit. Public jobs only , with codes turned into words. Contact details are dropped and masked by default. No API key is needed on your side. Monitor mode returns only jobs it hasn't returned before. Pricing: $0.002 per job, plus $0.01 for a monitor run that finds new jobs (base prices; higher Apify plans pay less). { "keywords" : [ "data scientist" ], "locations" : [ "Washington, District of Columbia" ], "radiusMiles" : 25 , "postedWithinDays" : 14 , "minSalaryUsd" : 100000 } Not an official USAJOBS or OPM product, and not endorsed by any federal agency. Always check the official announcement on usajobs.gov before you apply.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/yourevenings/five-things-to-know-before-you-build-on-the-usajobs-search-api-30i4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
