---
title: "Google Ads Transparency Center API: export a competitor's Google ads"
slug: "google-ads-transparency-center-api-export-a-competitors-google-ads"
author: "Aniruddha Garje"
source: "devto_python"
published: "Sun, 11 Oct 2026 04:03:53 +0000"
description: "Google's Ads Transparency Center shows the ads that advertisers run with Google, and lets you filter them by Search, YouTube, Shopping, Maps and Play. You ca..."
keywords: "ads, run, you, text, shown, com, google, one"
generated: "2026-10-11T05:08:30.392475"
---

# Google Ads Transparency Center API: export a competitor's Google ads

## Overview

Google's Ads Transparency Center shows the ads that advertisers run with Google, and lets you filter them by Search, YouTube, Shopping, Maps and Play. You can browse it by advertiser or website. If you want those ads as data, to watch competitors or build a swipe file, here is what I learned exporting them, and the request I use. How long competitors keep an ad running I exported 10 US ads each for three CRM companies: hubspot.com, salesforce.com and zoho.com (run saWgrSwy1OvGlOGjZ). The median days shown was 319.5 for HubSpot, 195 for Salesforce and 757.5 for Zoho. When you study a competitor, read the longest-running ads first. Across a larger run of 4,578 ads, the median days shown was 164 for text ads, 52 for image ads and 21 for video ads (run CmLk2DJUK1igwGucM). One website can have several advertisers The 10 hubspot.com ads came from 3 advertiser accounts. So search by website domain when you want everything a brand runs, and by advertiser ID when you want exactly one account. You can also search by name. A search for Shopify found Shopify Inc.; its 30 ads were 13 text, 13 video and 4 image, the earliest first shown on 2022-08-13 (run VKplR3pJxcOgnEisJ). Most text ads come back as images This surprised me the most. In the CRM export, 27 of the 30 ads were text ads, and 26 of those 27 came back as images. In the larger run, 2,866 of 2,958 text ads (96.9%) were images. The Transparency Center publishes most text ads as one rendered picture, so there is often no headline to copy as text. My export marks each ad's content status, so you know which ads hold text and which hold only an image URL. It does not read text out of images. Video ads are easier. 30 Sony Music Entertainment video ads all came with a YouTube link and first and last shown dates (run qT42FaC6ihuBOgQVE). Dates you can rely on firstShown, lastShown and daysShown came back for every ad in the regions I measured, the US and "anywhere" (runs KX1cJFN14b0BG3Kxk and MrvckmGUntglLNYnJ). One limit to know: the Transparency Center shows per-region first-shown dates and impression ranges only for EU countries. Outside the EU you get a per-region last-shown date. The request I use I built an Apify Actor for this, so my export is one HTTP request. You need an Apify account and your API token in the APIFY_TOKEN environment variable. import os import requests url = " https://api.apify.com/v2/acts/garje~google-ads-transparency-scraper/run-sync-get-dataset-items " run_input = { " domains " : [ " hubspot.com " , " salesforce.com " , " zoho.com " ], " region " : " US " , " maxAdsPerDomain " : 10 , " includeCreativeContent " : True , " proxyConfiguration " : { " useApifyProxy " : True }, } resp = requests . post ( url , params = { " format " : " csv " }, json = run_input , headers = { " Authorization " : f " Bearer { os . environ [ ' APIFY_TOKEN ' ] } " }, timeout = 300 , ) resp . raise_for_status () with open ( " ads.csv " , " wb " ) as f : f . write ( resp . content ) I ran the same request with 2 ads for one domain, and it returned a CSV with 2 ads (run hxovNrfVkZSYua84X). The price is $1.50 per 1,000 ads, and you are charged only for rows saved. Watch for new ads Add "onlyNewSince": "2026-10-01" to the input and you get only ads first shown after that date. Run it weekly and move the date forward, and you see each new creative as it launches. If you would rather click than code, the competitor comparison is saved as a public example you can run: Google ads of three competing brands in one table . Sources What Where it comes from Median days shown for the three CRM brands, 3 advertisers, 26 of 27 text ads as images run saWgrSwy1OvGlOGjZ Median days shown by format, 96.9% of text ads as images run CmLk2DJUK1igwGucM Shopify by name run VKplR3pJxcOgnEisJ Sony Music video ads with YouTube links run qT42FaC6ihuBOgQVE Dates on every ad, US and anywhere runs KX1cJFN14b0BG3Kxk and MrvckmGUntglLNYnJ The request above, 2 ads run hxovNrfVkZSYua84X I built the Google Ads Transparency scraper used above, and every week I check it against the live site. I drafted this article with AI help; every number comes from the runs in the table.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/garje/google-ads-transparency-center-api-export-a-competitors-google-ads-4fag

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
