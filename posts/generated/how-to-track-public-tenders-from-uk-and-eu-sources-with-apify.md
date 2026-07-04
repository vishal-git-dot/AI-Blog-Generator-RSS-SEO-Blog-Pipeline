---
title: "How to Track Public Tenders from UK and EU Sources with Apify"
slug: "how-to-track-public-tenders-from-uk-and-eu-sources-with-apify"
author: "Eren Yeager"
source: "devto_webdev"
published: "Sat, 04 Jul 2026 08:32:57 +0000"
description: "Public tenders and RFPs can be valuable, but checking different procurement portals manually is slow. A bid team, public-sector sales team, or GovCon consult..."
keywords: "apify, you, actor, can, tender, use, not, public"
generated: "2026-07-04T08:44:47.976115"
---

# How to Track Public Tenders from UK and EU Sources with Apify

## Overview

Public tenders and RFPs can be valuable, but checking different procurement portals manually is slow. A bid team, public-sector sales team, or GovCon consultant usually needs to answer a few practical questions quickly: Who is the buyer? What is the opportunity? When is the deadline? Where is the official source? Is this worth reviewing? In this walkthrough, I’ll show a simple way to collect public tender records from UK and EU sources into a structured dataset using Apify. Actor used here: https://apify.com/fascinating_lentil/global-government-contracts-aggregator What This Actor Supports The Global Government Contracts & Tenders Scraper currently supports: UK Contracts Finder EU TED SAM.gov, when you provide your own SAM.gov API key For this tutorial, we’ll use UK Contracts Finder and EU TED because they do not require an API key for a first test. Step 1: Open the Actor Open the actor on Apify: https://apify.com/fascinating_lentil/global-government-contracts-aggregator Click Try for free or open it in Apify Console if you are already logged in. Step 2: Use a Small First Input Start with a small run so the test stays quick and easy to inspect. { "sources" : [ "uk_contracts_finder" , "ted" ], "keywords" : [ "software" ], "noticeStatus" : "active" , "maxResults" : 10 , "proxyConfiguration" : { "useApifyProxy" : false } } What the fields mean: sources : procurement sources to search keywords : search terms such as software , cybersecurity , or facilities management noticeStatus : use active for open opportunities maxResults : total records to save proxyConfiguration : proxy is usually not needed for official APIs Step 3: Run the Actor Click Start . When the run finishes, open the Output tab. You should see a table of tender or contract records. Important fields include: source contractId title buyerName buyerCountry buyerRegion noticeType stage procurementMethod contractValue currency publishedDate deadlineDate status classificationCodes description contractUrl Step 4: Review One Result A useful tender digest should start with decision fields, not every possible field. Example digest item: Title: Roof Chiller Replacement At UCG Paddington Buyer: United Colleges Group Region: England / London Notice type: Tender Stage: Tender Procurement method: Open procedure Published: 2026-06-27 Deadline: 2026-07-20 Status: Active Source: UK Contracts Finder Official URL: https://www.contractsfinder.service.gov.uk/Notice/78662a62-9ddd-45eb-bdfa-e27352391e6e-903748 For a bid team, the main question is not just “can we scrape it?” The better question is: Can we quickly decide whether this opportunity is worth opening? That is why buyer, deadline, location, category, value, status, and official URL matter so much. Step 5: Export the Data From the Apify dataset, you can export results as: CSV Excel JSON HTML table API response For a manual workflow, CSV or Excel is enough. For an automated workflow, you can use the Apify API or connect the actor output to another tool. Step 6: Turn It Into a Weekly Digest Once the records are structured, you can filter them into a weekly digest. Useful filters: keyword country or region deadline window notice type procurement stage estimated value CPV or category code buyer name A simple digest format could look like this: Weekly Software Tender Digest 1. Tender title Buyer: ... Deadline: ... Region: ... Value: ... Why review: matches software keyword and deadline is still open. Official URL: ... You can build this manually first: Run the actor once per week. Export the dataset to CSV. Filter for relevant records. Send a short email or report to your team. Later, you can automate it: Schedule the actor on Apify. Store previously seen contractId values. Keep only new opportunities. Send the digest by email or webhook. Practical Tips Start narrow. A search for software is easier to validate than a broad “all tenders” feed. Keep maxResults small until you like the output format. Use active status when your goal is live opportunities. Use the official source URL as the final source of truth. Do not depend on contract value alone. Many public notices do not publish a clean value. Responsible Use This workflow is designed for official public procurement records. Do not use it to collect private information, build personal contact lists, or bypass access controls. Always check the source terms, local rules, and your organization’s procurement compliance requirements. Final Thought The useful product here is not just “scraping tenders.” The useful product is a clean opportunity list that helps someone decide what to review next. If you work with procurement, GovCon, public-sector sales, or bid writing, I’d be interested in your view: Which fields matter most when deciding whether a tender is worth opening? Actor link: https://apify.com/fascinating_lentil/global-government-contracts-aggregator

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/eren_yeager_9a2ae92830309/how-to-track-public-tenders-from-uk-and-eu-sources-with-apify-13pl

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
