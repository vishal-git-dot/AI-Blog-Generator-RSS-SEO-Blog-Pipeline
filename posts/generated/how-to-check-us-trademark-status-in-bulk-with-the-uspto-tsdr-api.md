---
title: "How to Check US Trademark Status in Bulk with the USPTO TSDR API"
slug: "how-to-check-us-trademark-status-in-bulk-with-the-uspto-tsdr-api"
author: "Scrape-Smith"
source: "devto_python"
published: "Thu, 22 Oct 2026 16:42:02 +0000"
description: "How to Check US Trademark Status in Bulk with the USPTO TSDR API If you manage more than a handful of US trademarks, for clients or your own brands, you know..."
keywords: "status, uspto, key, api, tsdr, you, trademark, your"
generated: "2026-10-22T16:56:20.007589"
---

# How to Check US Trademark Status in Bulk with the USPTO TSDR API

## Overview

How to Check US Trademark Status in Bulk with the USPTO TSDR API If you manage more than a handful of US trademarks, for clients or your own brands, you know the routine: open TSDR, paste a serial number, read the status, copy it into a spreadsheet, repeat. It's fine for five marks. It's a lost afternoon for two hundred. The USPTO has an official API for exactly this, called TSDR (Trademark Status & Document Retrieval). This tutorial explains how to get access, what it returns, and how to run bulk lookups with the USPTO Trademark Status Lookup actor without writing any code. Step 1: Get a free USPTO API key TSDR requires an API key. It is free: Go to https://account.uspto.gov/api-manager and sign in with (or create) a USPTO.gov account. Request a TSDR API key. Copy the key somewhere safe. The key is personal and rate limited to 60 requests per minute. That's why this actor is "bring your own key": you stay in control of your own access and quota, and nothing is shared. Step 2: Collect serial numbers TSDR looks up marks by 8-digit serial number (the application number), such as 78787878 . If you only have a registration number, look it up once on tsdr.uspto.gov to find the serial. Most docketing exports already include serials. Step 3: Run the lookup Open the actor , paste your serial numbers one per line, and paste your key into the API key field (it's stored as a secret input). Click Start . Each successful row contains: Field Example meaning serialNumber 78787878 markText The word mark status e.g. "Registered", "Abandoned", "Published for opposition" statusDate When the status last changed filingDate , registrationDate , registrationNumber Key dates and number owner Current owner name goodsServices Goods & services descriptions If you run without a key (or with a wrong one), each row comes back as a free error row saying HTTP 401 - API key required/invalid . That's deliberate: you can test the tool safely before setting up the key, and you're never charged for failures. Step 4: Automate a weekly status report Schedule the actor weekly and export to Google Sheets, or from Python: from apify_client import ApifyClient client = ApifyClient ( " YOUR_APIFY_TOKEN " ) serials = [ line . strip () for line in open ( " portfolio.txt " ) if line . strip ()] run = client . actor ( " scrape-smith/uspto-trademark-status " ). call ( run_input = { " serialNumbers " : serials , " apiKey " : " YOUR_USPTO_KEY " , }) for r in client . dataset ( run [ " defaultDatasetId " ]). iterate_items (): if " error " in r : print ( " CHECK " , r [ " serialNumber " ], r [ " error " ]) else : print ( r [ " serialNumber " ], r [ " status " ], r [ " statusDate " ]) Store last week's output and diff it: any row whose status or statusDate changed is something a human should look at (an office action, publication, registration, or abandonment). Who this is for Small IP practices that want a status sheet without a docketing system. Brand owners with a portfolio across product lines. Due diligence before acquiring a business or licensing a brand. Competitive watch : track competitors' pending applications as they move through examination. Honest limitations You need your own USPTO key. There's no way around that, and that's a good thing. The USPTO limit is 60 requests per minute, so the actor paces itself at about one lookup per second. 1,000 marks take about 17 minutes. It looks up known serial numbers. It is not a clearance search by mark name. Status text comes straight from USPTO. It is not legal advice; deadlines should still be checked by an attorney. Not affiliated with the USPTO. Cost $0.004 per successful lookup; errors are free. 100 marks is $0.40, 1,000 marks is $4. Apify platform usage is included. Wrap-up The TSDR API turns trademark status checks from a copy-paste chore into a scheduled report. If you'd rather not write the plumbing, the USPTO Trademark Status Lookup does it with your own key in a couple of clicks. Scrape-Smith builds small, cheap data tools on public and official APIs.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/scrape-smith/how-to-check-us-trademark-status-in-bulk-with-the-uspto-tsdr-api-15ie

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
