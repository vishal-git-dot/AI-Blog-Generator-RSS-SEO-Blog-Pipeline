---
title: "How to get every open job from any company's career site (Greenhouse, Lever, Ashby, Personio & co.)"
slug: "how-to-get-every-open-job-from-any-companys-career-site-greenhouse-lever-ashby-personio-co"
author: "Julian"
source: "devto_python"
published: "Wed, 18 Nov 2026 00:47:15 +0000"
description: "If you want to track jobs at specific companies (for job alerts, a niche job board, "hiring signals" for sales, or competitor research), you don't need to sc..."
keywords: "slug, jobs, ats, job, api, com, greenhouse, https"
generated: "2026-11-18T00:48:50.457807"
---

# How to get every open job from any company's career site (Greenhouse, Lever, Ashby, Personio & co.)

## Overview

If you want to track jobs at specific companies (for job alerts, a niche job board, "hiring signals" for sales, or competitor research), you don't need to scrape job portals. Most companies publish their openings through an applicant tracking system (ATS) , and most ATS vendors offer a public feed so the jobs can be embedded on the company's own website. Those feeds are meant to be read, return JSON or XML, and need no login. 1. Find out which ATS a company uses Open the careers page and look at where the "Apply" links point: You see ATS boards.greenhouse.io/<slug> or job-boards.greenhouse.io/<slug> Greenhouse jobs.lever.co/<slug> Lever jobs.ashbyhq.com/<slug> Ashby <slug>.jobs.personio.de (or .com ) Personio, very common in Germany and Austria <slug>.recruitee.com Recruitee apply.workable.com/<slug> Workable careers.smartrecruiters.com/<CompanyId> SmartRecruiters <slug>.breezy.hr Breezy HR assets loaded from teamtailor-cdn.com Teamtailor The <slug> in that URL is what you need for the feed. 2. Call the feed ATS Public endpoint Greenhouse https://boards-api.greenhouse.io/v1/boards/{slug}/jobs?content=true Lever https://api.lever.co/v0/postings/{slug}?mode=json Ashby https://api.ashbyhq.com/posting-api/job-board/{slug}?includeCompensation=true Workable https://apply.workable.com/api/v1/widget/accounts/{slug}?details=true SmartRecruiters https://api.smartrecruiters.com/v1/companies/{id}/postings Recruitee https://{slug}.recruitee.com/api/offers/ Personio https://{slug}.jobs.personio.de/xml?language=en (XML) Breezy HR https://{slug}.breezy.hr/json Teamtailor https://{career-site-host}/jobs.rss (RSS) Greenhouse and Lever also run EU instances ( boards-api.eu.greenhouse.io , api.eu.lever.co ); if a slug returns nothing, try those. Here is a minimal, dependency-free Python script for three of them: import json , urllib . request FEEDS = { "greenhouse" : "https://boards-api.greenhouse.io/v1/boards/{slug}/jobs" , "lever" : "https://api.lever.co/v0/postings/{slug}?mode=json" , "ashby" : "https://api.ashbyhq.com/posting-api/job-board/{slug}" , } # Identify yourself: some feeds reject anonymous default clients. UA = { "User-Agent" : "my-job-alerts/1.0 (+https://example.com/contact)" } def jobs ( ats , slug ) : req = urllib . request . Request ( FEEDS [ ats ] . format ( slug = slug ) , headers = UA ) with urllib . request . urlopen ( req , timeout = 20 ) as r : data = json . load ( r ) if ats == "greenhouse" : return [ ( j [ "title" ] , j [ "location" ] [ "name" ] , j [ "absolute_url" ] ) for j in data [ "jobs" ] ] if ats == "lever" : return [ ( j [ "text" ] , j [ "categories" ] . get ( "location" , "" ) , j [ "hostedUrl" ] ) for j in data ] if ats == "ashby" : return [ ( j [ "title" ] , j . get ( "location" , "" ) , j [ "jobUrl" ] ) for j in data [ "jobs" ] ] for ats , slug in [ ( "greenhouse" , "stripe" ) , ( "lever" , "palantir" ) , ( "ashby" , "linear" ) ] : found = jobs ( ats , slug ) print ( f "{slug}: {len(found)} open jobs, e.g. {found[0] if found else '-'}" ) When I ran it on 18 November 2026, it printed 791 jobs for Stripe, 301 for Palantir and 33 for Linear. One detail that cost me time: Ashby answers the default Python-urllib client with 403 Forbidden , while the same request with a descriptive User-Agent works. Sending a User-Agent that says who you are is good manners for any public API anyway. A longer script that covers more ATS (incl. the XML and RSS feeds) is in the companion repo: github.com/goldfoot/career-site-jobs-api . 3. The annoying parts Every ATS has its own format. Salary comes in at least three shapes; "remote" is a boolean in one feed, a string in another and hidden in the location text in a third. Slugs. stripe.com → Greenhouse slug stripe , but many companies use odd slugs, several boards or an EU instance. Which ATS at all? For a list of 500 company domains, you first have to detect the ATS of each one. New vs. already seen. For alerts, you need to remember which jobs you have already reported. Descriptions. Some feeds need an extra request per job for the full text. 4. Or use a ready-made Actor I packaged all of this as the Career Site Jobs Scraper on Apify (disclosure: I built it) . You pass company domains or career-page URLs; it detects the ATS (13 platforms, including Pinpoint, Gem and softgarden), normalizes everything into one format and can return only jobs that are new since the last run. It costs $0.003 per job returned, and filters run before anything is charged. # pip install apify-client import os from apify_client import ApifyClient client = ApifyClient ( os . environ [ "APIFY_TOKEN" ] ) run = client . actor ( "goldfoot/ats-jobs-feed" ) . call ( run_input = { "companies" : [ "stripe.com" , "linear.app" , "jobs.lever.co/palantir" ] , "titleKeywords" : [ "engineer" ] , "locations" : [ "Germany" , "remote" ] , "onlyNewJobs" : True , # remembers jobs between runs → alerts "monitorId" : "my-watchlist" , } ) for job in client . dataset ( run [ "defaultDatasetId" ] ) . iterate_items ( ) : print ( job [ "companyName" ] , "|" , job [ "title" ] , "|" , job [ "location" ] , "|" , job [ "url" ] ) If you're interested in Germany, Austria and Switzerland specifically: I also run a weekly index of these feeds. The 16 November 2026 refresh held 45,562 open jobs from 4,471 employers , searchable through the DACH Jobs API ($0.002 per job) and browsable for free at wer-stellt-ein.de . Questions about a specific ATS or a feed I haven't covered? Ask in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/goldfoot/how-to-get-every-open-job-from-any-companys-career-site-greenhouse-lever-ashby-personio-co-53ko

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
