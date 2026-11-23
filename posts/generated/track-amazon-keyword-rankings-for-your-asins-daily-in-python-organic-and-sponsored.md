---
title: "Track Amazon keyword rankings for your ASINs daily in Python, organic and sponsored"
slug: "track-amazon-keyword-rankings-for-your-asins-daily-in-python-organic-and-sponsored"
author: "Aurelix Solutions"
source: "devto_python"
published: "Mon, 23 Nov 2026 23:20:42 +0000"
description: "An Amazon seller's daily question is short: for my main keywords, where do my products sit today, and did they move. Reading whole search results to find one..."
keywords: "keyword, asin, amazon, run, daily, per, rank, apify"
generated: "2026-11-23T23:39:37.002843"
---

# Track Amazon keyword rankings for your ASINs daily in Python, organic and sponsored

## Overview

An Amazon seller's daily question is short: for my main keywords, where do my products sit today, and did they move. Reading whole search results to find one ASIN wastes pages and money; what matters is one row per keyword and ASIN with its position and the change. This post tracks keyword/ASIN pairs from Python and turns them into a daily schedule with a Slack digest. Disclosure: I'm Aurelix, and I built Amazon Keyword Rank Tracker , the tool used here. It's a paid tool (prices below). What each row holds keyword , asin , marketplace , found . organic_position (the middle of 3 independent visits), organic_position_best and organic_position_worst , organic_positions (each visit), organic_page , sponsored_position and sponsored_page , overall_position (every card, ads included). previous_organic_position , organic_change (+3 = up three places), sponsored_change , changed , first_check . pages_checked , not_found_note , plus the card's title , price , rating and reviews_count . Positions for a few pairs pip install apify-client import os from apify_client import ApifyClient client = ApifyClient ( os . environ [ "APIFY_TOKEN" ] ) run = client . actor ( "aurelix/amazon-keyword-rank-tracker" ) . call ( run_input = { "tracks" : [ "wireless earbuds | B09FT58QQP, B0CXG87GYK" , "yoga mat | B07H9PDL2Y" ] , "maxPages" : 5 , "stateKey" : "my-ranks-daily" , } ) for r in client . dataset ( run [ "defaultDatasetId" ] ) . iterate_items ( ) : print ( f "{r['keyword']:18} {r['asin']} organic {r['organic_position'] or '-':>4} (page {r['organic_page'] or '-'})" f " sponsored {r['sponsored_position'] or '-':>4} change {r['organic_change'] or 0:+}" ) Reading stops once every ASIN of a keyword has an organic position, so you pay only for the pages needed. An ASIN deeper than maxPages comes back with found false and a note. Every morning, only the moves Keep the same stateKey , save the input as a task and schedule it daily. Add "onlyChanges": True to get only pairs whose position moved (the first 10 unchanged pairs per run are free), and a slackWebhookUrl for a digest of the biggest moves. Limits Positions are what logged-out visitors were served; the order varies from visitor to visitor (even a top-5 ASIN can be missing from one visit), so each keyword is read in 3 visits and changed is true only when this run's range of visits does not overlap the previous run's. Datacenter visitors see fewer ads than shoppers, so sponsored positions are often empty. amazon.com, .ca and .in on the default proxy; .co.uk, .de and .co.jp need the residential add-on. Cost $0.60 per 1,000 results pages read plus $1 per 1,000 keyword/ASIN rows on Apify's free plan (from $0.50 and $0.80 on paid plans), plus a start fee per run. A one-ASIN check at the default 3 visits reads about 3 pages, about $0.0028. Current prices are on the Store page . Use it from an AI assistant Through Apify's hosted MCP server, Claude, ChatGPT or Cursor can run it from a request like "where does B09FT58QQP rank on Amazon for 'wireless earbuds' today?". Server URL: https://mcp.apify.com/?tools=aurelix/amazon-keyword-rank-tracker . Links Amazon Keyword Rank Tracker on the Apify Store

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/aurelix_solutions/track-amazon-keyword-rankings-for-your-asins-daily-in-python-organic-and-sponsored-eba

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
