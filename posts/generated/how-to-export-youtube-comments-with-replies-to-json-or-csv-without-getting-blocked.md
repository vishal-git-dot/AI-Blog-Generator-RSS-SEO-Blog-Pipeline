---
title: "How to export YouTube comments (with replies) to JSON or CSV without getting blocked"
slug: "how-to-export-youtube-comments-with-replies-to-json-or-csv-without-getting-blocked"
author: "Ramazan Akdoğan"
source: "devto_python"
published: "Fri, 20 Nov 2026 15:00:00 +0000"
description: "YouTube comments are a goldmine for audience research, product feedback and sentiment analysis . Getting them out at scale is annoying, though: HTML scrapers..."
keywords: "comments, youtube, video, replies, api, comment, data, actor"
generated: "2026-11-20T15:10:11.460522"
---

# How to export YouTube comments (with replies) to JSON or CSV without getting blocked

## Overview

YouTube comments are a goldmine for audience research, product feedback and sentiment analysis . Getting them out at scale is annoying, though: HTML scrapers break or get rate-limited, and writing your own API pagination for comment threads and replies takes an afternoon. Here's the approach I use: the official YouTube Data API v3 , wrapped in a ready-made actor so there's no code to maintain. Why the official API It doesn't get blocked : no proxies, no CAPTCHAs, and no breakage when YouTube changes its HTML. It's cheap on quota : one commentThreads call returns up to 100 comments for 1 quota unit. In one test, about 28,500 comments used under 400 units of the free 10,000-unit daily quota. The data is clean : author, author channel, likes, reply count, publish and update dates. The tool YouTube Comments Scraper takes: video, Shorts or youtu.be links channels ( @handle ); it collects comments from their latest N videos options: include replies (with a per-comment cap), filter by keywords , minimum likes or date , and sort by top or newest Every row also includes the video title, channel, views and total comment count , so a multi-video export stays easy to analyze in Sheets or pandas. Python example from apify_client import ApifyClient import pandas as pd client = ApifyClient ( "YOUR_APIFY_TOKEN" ) run = client . actor ( "datacraft-tools/youtube-comments" ) . call ( run_input = { "channels" : [ "@mkbhd" ] , "latestVideosPerChannel" : 3 , "maxCommentsPerVideo" : 1000 , "includeReplies" : True , "maxRepliesPerComment" : 20 , "keywords" : [ "battery" , "price" ] , } ) df = pd . DataFrame ( client . dataset ( run [ "defaultDatasetId" ] ) . list_items ( ) . items ) print ( df . groupby ( "videoTitle" ) [ "likes" ] . describe ( ) ) Ideas for what to do with the data Feed comments to an LLM: "Summarize the top 10 complaints about this product." Track how sentiment changes from one video to the next. Mine questions from comments for your next video or FAQ. Pick a fair giveaway winner from comments that contain a keyword. Pricing is pay-as-you-go: $0.70 per 1,000 comments plus $0.01 per run. I built this actor. If you need a feature, tell me in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ramazan_akdoan_fa177aff4/how-to-export-youtube-comments-with-replies-to-json-or-csv-without-getting-blocked-46mg

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
