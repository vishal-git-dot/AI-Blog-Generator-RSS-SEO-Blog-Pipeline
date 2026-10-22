---
title: "How to Export Steam Game Reviews (with Playtime) for Player Sentiment Analysis"
slug: "how-to-export-steam-game-reviews-with-playtime-for-player-sentiment-analysis"
author: "Scrape-Smith"
source: "devto_python"
published: "Thu, 22 Oct 2026 16:38:40 +0000"
description: "How to Export Steam Game Reviews for Player Sentiment Analysis Steam reviews are unusually rich feedback. Every review is a thumbs up or down, it comes with ..."
keywords: "reviews, steam, game, review, players, sentiment, hours, you"
generated: "2026-10-22T16:56:20.007896"
---

# How to Export Steam Game Reviews (with Playtime) for Player Sentiment Analysis

## Overview

How to Export Steam Game Reviews for Player Sentiment Analysis Steam reviews are unusually rich feedback. Every review is a thumbs up or down, it comes with how many hours the reviewer had played, and other players vote on whether it was helpful. For game developers, publishers and analysts, that's a sentiment dataset most industries would envy. Steam shows reviews nicely on the store page, but not in a form you can analyse. This tutorial uses Valve's public reviews endpoint through the Steam Reviews Scraper to export them, then looks at a couple of analyses worth doing. The endpoint Valve documents a public endpoint: https://store.steampowered.com/appreviews/440?json=1&filter=recent&language=all&num_per_page=100 It returns reviews in pages with a cursor for the next page, plus a summary like "Very Positive". The actor handles cursor pagination, throttles to roughly one request per second, and flattens each review into a row. Step 1: Run the example Open the actor and click Try for free . It's prefilled with app 440 (Team Fortress 2) and 20 reviews: gameName recommended playtimeAtReviewMinutes votesUp language Team Fortress 2 true 1236 0 spanish Each row includes review text, recommended , votesUp , votesFunny , weightedVoteScore , playtimeForeverMinutes , playtimeAtReviewMinutes , playtimeLastTwoWeeksMinutes , steamPurchase , receivedForFree , writtenDuringEarlyAccess , primarilySteamDeck , author stats and any developerResponse . Step 2: Pick your game and filters appIds : the number in the store URL ( store.steampowered.com/app/1091500/... ) or the whole URL. filter : recent (newest first; the way to page through full history), updated , or all (most helpful first, optionally with dayRange ). language : english , german , schinese ... or all . reviewType : positive or negative only. purchaseType : Steam purchases vs. keys bought elsewhere. Step 3: Two analyses worth doing from apify_client import ApifyClient import pandas as pd client = ApifyClient ( " YOUR_APIFY_TOKEN " ) run = client . actor ( " scrape-smith/steam-reviews-scraper " ). call ( run_input = { " appIds " : [ " 1091500 " ], " maxReviewsPerApp " : 5000 , " filter " : " recent " , " language " : " english " , }) df = pd . DataFrame ( client . dataset ( run [ " defaultDatasetId " ]). iterate_items ()) df [ " created " ] = pd . to_datetime ( df [ " createdAt " ]) df [ " hours " ] = df [ " playtimeAtReviewMinutes " ] / 60 # 1) Sentiment over time: did the last patch help? print ( df . set_index ( " created " ). resample ( " W " )[ " recommended " ]. mean (). tail ( 8 )) # 2) Do experienced players feel differently? df [ " bucket " ] = pd . cut ( df [ " hours " ], [ 0 , 2 , 10 , 50 , 200 , 10000 ]) print ( df . groupby ( " bucket " , observed = True )[ " recommended " ]. agg ([ " mean " , " count " ])) The first table shows the weekly share of positive reviews, the fastest way to see a patch landing well or badly. The second often reveals a pattern: players under two hours (refund window) and players over 200 hours can feel very differently about the same game. Both are useful, for different reasons. From there, feed negative reviews from heavy players into an LLM or topic model to find the issues your most committed players care about. Use cases Live-ops and patch monitoring for studios. Competitor and genre research before greenlighting a project. Publisher due diligence on games they might sign. Sentiment and NLP datasets with a built-in label (recommended or not). Daily alerts for new negative reviews. Honest limitations Some orderings (like all ) don't go back through the full history. Use recent to page through everything. Huge games have hundreds of thousands of reviews; at one request per second, exporting all of them takes a while. Set maxReviewsPerApp . Review text is user content. If you publish it, attribute and respect Steam's terms. Not affiliated with or endorsed by Valve. Cost $0.0003 per review. The 20-review test is well under a cent; 10,000 reviews is $3. Error rows are free and you can cap spend per run. Wrap-up Steam gives you labelled, playtime-weighted feedback for every game on the platform. The Steam Reviews Scraper gets it into a DataFrame in a minute. Try the prefilled example, then point it at your game or the competitor you keep comparing yourself to. Scrape-Smith builds small, cheap data tools on public and official APIs.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/scrape-smith/how-to-export-steam-game-reviews-with-playtime-for-player-sentiment-analysis-4fej

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
