---
title: "How to pull every open job at a company from Greenhouse, Lever, Ashby and Workable (no scraping)"
slug: "how-to-pull-every-open-job-at-a-company-from-greenhouse-lever-ashby-and-workable-no-scraping"
author: "Kleb Data"
source: "devto_webdev"
published: "Fri, 20 Nov 2026 23:33:24 +0000"
description: "Most startups and a large share of tech companies host their careers page on one of a few applicant tracking systems (ATS): Greenhouse, Lever, Ashby, Workabl..."
keywords: "jobs, api, greenhouse, https, com, company, stripe, lever"
generated: "2026-11-20T23:51:31.228844"
---

# How to pull every open job at a company from Greenhouse, Lever, Ashby and Workable (no scraping)

## Overview

Most startups and a large share of tech companies host their careers page on one of a few applicant tracking systems (ATS): Greenhouse, Lever, Ashby, Workable or SmartRecruiters. Each of them publishes a public JSON job-board API meant for embedding. That means you do not need a headless browser or a proxy to get a company's open jobs. You need the right URL. The endpoints ATS Careers page looks like Public JSON Greenhouse boards.greenhouse.io/stripe https://boards-api.greenhouse.io/v1/boards/stripe/jobs?content=true Lever jobs.lever.co/spotify https://api.lever.co/v0/postings/spotify?mode=json Ashby jobs.ashbyhq.com/openai https://api.ashbyhq.com/posting-api/job-board/openai?includeCompensation=true Workable apply.workable.com/acme https://apply.workable.com/api/v1/widget/accounts/acme?details=true SmartRecruiters jobs.smartrecruiters.com/acme https://api.smartrecruiters.com/v1/companies/acme/postings?limit=100 Try one: curl -s "https://boards-api.greenhouse.io/v1/boards/stripe/jobs" | jq '.jobs | length' The annoying part Every system names things differently: Greenhouse returns HTML that is escaped twice, and has no employment type. Lever gives createdAt as a millisecond timestamp and puts location under categories . Ashby has a real isRemote flag and a compensation summary; the others mostly do not. SmartRecruiters pages by 100 and its list has no description. If you track 50 companies you end up writing five parsers and a "which ATS is this company on" detector. One schema for all five I wrapped this in a small Apify actor that takes careers URLs (or greenhouse:stripe , or just stripe ) and returns one flat schema: { "company" : "Stripe" , "ats" : "greenhouse" , "title" : "Backend Engineer, Payments" , "location" : "Seattle, San Francisco, New York City" , "remote" : false , "department" : "Engineering" , "postedAt" : "2026-09-09T14:50:29.000Z" , "url" : "https://stripe.com/jobs/search?gh_jid=7123456" } It has filters for title keywords, location, remote-only and "posted after", so a daily run can return only new jobs. A run over six AI companies returned 472 engineering and research jobs in 3 seconds. Actor: https://apify.com/kleb-data/company-jobs-api Ready-made example (OpenAI, Anthropic, Scale AI, Perplexity, Cohere, Databricks): https://apify.com/kleb-data/company-jobs-api/examples/ai-company-jobs-openai-anthropic-more-remote-filter It is free right now apart from Apify platform usage, which is well under a cent per run. What it does not cover Workday, iCIMS and custom career sites. Workday has no public job-board API and blocks server requests, so I left it out rather than work around it. Ideas for using it A daily "new jobs at my target companies" digest Hiring signals for sales: who just opened five data-engineering roles A niche job board for one sector A tool an AI agent can call to answer "what is this company hiring for" If your target companies use an ATS I have not covered and it has a public API, tell me which one.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kleb_data/how-to-pull-every-open-job-at-a-company-from-greenhouse-lever-ashby-and-workable-no-scraping-70j

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
