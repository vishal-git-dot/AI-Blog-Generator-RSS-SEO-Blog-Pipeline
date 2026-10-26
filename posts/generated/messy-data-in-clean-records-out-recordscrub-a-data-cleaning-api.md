---
title: "Messy data in, clean records out: RecordScrub, a data-cleaning API"
slug: "messy-data-in-clean-records-out-recordscrub-a-data-cleaning-api"
author: "DSP"
source: "devto_python"
published: "Mon, 26 Oct 2026 04:03:46 +0000"
description: "Every project eventually inherits the same spreadsheet: emails in three different cases, phone numbers formatted six ways, names like "DOE, john michael", an..."
keywords: "phone, every, john, cleaning, doe, you, rapidapi, free"
generated: "2026-10-26T04:10:10.667896"
---

# Messy data in, clean records out: RecordScrub, a data-cleaning API

## Overview

Every project eventually inherits the same spreadsheet: emails in three different cases, phone numbers formatted six ways, names like "DOE, john michael", and the same customer entered twice. Cleaning it by hand, or with a pile of regexes you don't quite trust, is nobody's favorite afternoon. RecordScrub is a small API we built at DSP to do that job in one call. It's live on RapidAPI now, with a free tier. What it does Email validation & normalization , single or batch, with valid/invalid stats and a plain-language reason for every rejection Phone normalization to E.164 , powered by Google's libphonenumber, so (312) 555-0142 becomes +13125550142 Name normalization , "DOE, john michael" → John Michael Doe , with first/last split out US address normalization , state codes, ZIP+4, standardized street suffixes Batch record cleaning , send CSV-style records, get snake_case keys, per-field cleaning, and exact dedupe on the fields you choose, with a duplicate report showing what was dropped and why Every dropped or altered value comes back with a _warnings explanation. No silent data loss. A taste curl -X POST https://record-scrub.p.rapidapi.com/v1/normalize/phone \ -H "X-RapidAPI-Key: YOUR_KEY" \ -H "Content-Type: application/json" \ -d '{"phone": "(312) 555-0142"}' { "original" : "(312) 555-0142" , "normalized" : "+13125550142" , "valid" : true , "country_code" : 1 , "national_format" : "(312) 555-0142" } And the batch cleaner, deduplicating on email + phone: { "records" : [{ "name" : "John Doe" , "email" : "john@example.com" , "phone" : "+13125550142" }], "stats" : { "received" : 2 , "returned" : 1 , "duplicates_removed" : 1 }, "duplicates" : [{ "index" : 1 , "duplicate_of" : 0 , "record" : { "..." : "..." }}]} How it's built FastAPI, completely stateless. Requests are processed in transit and nothing is stored , so there's no database to leak from. It runs on a free-tier host, so the first call after a quiet spell can take a few extra seconds while it wakes up; after that it's fast. Pricing Every endpoint is available on every plan, including the free tier. No feature gates, no Pro-only cleaners, no endpoint held back to force an upgrade. Upgrading simply gets you more requests per month: start free with 100 requests a month, move up to Pro at $10/month for 5,000, and scale from there if your batch volume grows. You pay for volume, not for access. Try it: https://rapidapi.com/darksundarker/api/record-scrub Feedback very welcome, especially the "I wish it also cleaned X" kind. That's how the v2 list gets written.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/darksun159/messy-data-in-clean-records-out-recordscrub-a-data-cleaning-api-3ce7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
