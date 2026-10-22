---
title: "How to Export iOS App Store Reviews by Country (for Sentiment Analysis and ASO)"
slug: "how-to-export-ios-app-store-reviews-by-country-for-sentiment-analysis-and-aso"
author: "Scrape-Smith"
source: "devto_python"
published: "Thu, 22 Oct 2026 16:35:09 +0000"
description: "How to Export iOS App Store Reviews by Country App reviews are the most honest product feedback you will ever get, and also the most annoying to collect. App..."
keywords: "reviews, app, apple, you, store, feed, per, country"
generated: "2026-10-22T16:56:20.008248"
---

# How to Export iOS App Store Reviews by Country (for Sentiment Analysis and ASO)

## Overview

How to Export iOS App Store Reviews by Country App reviews are the most honest product feedback you will ever get, and also the most annoying to collect. App Store Connect only shows reviews for your own apps, one storefront at a time, and third-party ASO suites are priced for agencies. If you just want a spreadsheet of recent reviews for your app or a competitor's, there is a simpler route: Apple's own public customer-reviews RSS feed. This tutorial walks through that feed, exports reviews with the Apple App Store Reviews Scraper , and ends with a quick sentiment pass in Python. The feed behind it Apple publishes recent reviews for every app at a URL like: https://itunes.apple.com/us/rss/customerreviews/page=1/id=284882215/sortby=mostrecent/json us is the storefront, 284882215 is the app ID (Facebook here), and each page holds up to 50 reviews. There are up to 10 pages, so roughly the 500 most recent reviews per app per country. The JSON is awkward (every value is wrapped in a label object, and the first entry is sometimes app metadata rather than a review), which is why a small wrapper helps. Step 1: Find the app ID Open the app on apps.apple.com. The ID is the number after id in the URL: apps.apple.com/us/app/facebook/id284882215 . You can also paste the full URL into the actor. Step 2: Run it Open the actor and click Try for free . The prefilled input is one app, the us store and one page, so you get 50 real reviews in a few seconds: rating title appVersion updated 3 Finding post 584.0.0 2026-10-20 1 ... 584.0.0 ... Each row has appId , country , reviewId , title , text , rating (1–5), appVersion , author , updated and voteCount . Step 3: Add countries Reviews are per storefront. A German user's review only shows up in the de store. Add the markets you care about, one per line: us , gb , de , fr , jp , br ... Set maxPages to 10 to get everything Apple exposes. Tip: the appVersion column is gold. Group by version and you can see whether a release made ratings better or worse. Step 4: A five-minute sentiment check from apify_client import ApifyClient import pandas as pd client = ApifyClient ( " YOUR_APIFY_TOKEN " ) run = client . actor ( " scrape-smith/apple-app-store-reviews " ). call ( run_input = { " appIds " : [ " 284882215 " ], " countries " : [ " us " , " gb " , " ca " , " au " ], " maxPages " : 10 , }) df = pd . DataFrame ( client . dataset ( run [ " defaultDatasetId " ]). iterate_items ()) print ( df . groupby ( " appVersion " )[ " rating " ]. agg ([ " mean " , " count " ]). tail ( 5 )) low = df [ df . rating <= 2 ] print ( low [ " text " ]. str . lower (). str . extractall ( r " (crash\w*|login|ads?|slow|bug\w*) " )[ 0 ]. value_counts ()) The first print shows average rating per recent version. The second counts common complaint words in 1–2 star reviews. Crude, but it gets you 80% of the insight before you reach for an LLM. If you do want an LLM, the reviews CSV is a perfect prompt input ("cluster these complaints into themes"). Use cases Release monitoring : schedule it daily and alert on new 1-star reviews. Competitor research : mine competitors' reviews for missing features. ASO keyword research : real users' words are the words people search. NLP datasets for sentiment models. Support triage : route review complaints to the right team. Honest limitations Apple's feed only exposes about 500 recent reviews per app per country. For an app with millions of reviews, this is a rolling window, not the full history. Schedule regular runs if you want to build history over time. Ratings without written reviews aren't included; Apple doesn't publish them in the feed. No developer replies; the feed doesn't contain them. This is App Store only, not Google Play. Not affiliated with Apple. It reads a public feed and doesn't log in. Cost $0.0003 per review. The 50-review test costs 1.5 cents; 1,000 reviews is $0.30. Apify platform usage is included. Wrap-up For most "what are users saying?" questions, Apple's RSS feed plus a spreadsheet is enough. Try the App Store Reviews Scraper with the prefilled app, then replace it with yours or a competitor's. Scrape-Smith builds small, cheap data tools on public and official APIs.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/scrape-smith/how-to-export-ios-app-store-reviews-by-country-for-sentiment-analysis-and-aso-3nh6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
