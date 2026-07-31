---
title: "I Built a "Fastest Pizza Near Me" Tool with the UberEats API and Python"
slug: "i-built-a-fastest-pizza-near-me-tool-with-the-ubereats-api-and-python"
author: "Benjamin Flores Vega"
source: "devto_python"
published: "Fri, 31 Jul 2026 02:57:45 +0000"
description: ""Which pizza place near me is actually good and fast tonight?" UberEats doesn't really answer that. It sorts by relevance, promotions, and whatever the algor..."
keywords: "store, rating, keyword, address, run, ubereats, delivery, client"
generated: "2026-07-31T03:29:44.278203"
---

# I Built a "Fastest Pizza Near Me" Tool with the UberEats API and Python

## Overview

"Which pizza place near me is actually good and fast tonight?" UberEats doesn't really answer that. It sorts by relevance, promotions, and whatever the algorithm feels like — not by "best combination of rating and delivery speed," which is what I actually want at 8pm on a Tuesday. So I built a tiny tool that answers it properly, using the UberEats Stores Search by Location and Keyword actor on Apify and about 40 lines of Python. The idea Pull every store matching a keyword at a given address — name, rating, estimated delivery time — then rank them myself instead of trusting the app's default order. A place with a 4.8 rating and 45-minute delivery isn't necessarily better than a 4.5-rated spot that shows up in 20. Walkthrough Install the client: pip install apify-client Fetch the data: from apify_client import ApifyClient client = ApifyClient("YOUR_APIFY_TOKEN") run_input = { "locations": ["85 Marsh St, Newark, NJ 07114, USA"], "search_keyword": "pizza", "max_search_results": 30, } run = client.actor("datacach/ubereats-stores-search-by-location-and-keyword").call(run_input=run_input) items = list(client.dataset(run["defaultDatasetId"]).iterate_items()) Each store comes back with estimated_time_to_delivery as a string like "20 min" . Parse it and score each place — rating matters, but delivery time should pull the score down the longer it takes: import re def parse_minutes(text): match = re.search(r"\d+", text or "") return int(match.group()) if match else 60 # unknown time = penalize heavily def score(store): rating = store.get("rating") or 0 minutes = parse_minutes(store.get("estimated_time_to_delivery")) return rating - 0.03 * minutes # tune this weight to taste ranked = sorted(items, key=score, reverse=True) for store in ranked[:5]: print(f"{store['name']:<30} ★{store.get('rating', '?'):<5} {store.get('estimated_time_to_delivery', '?')}") That's it — a ranked top 5 that actually balances "good" against "fast," instead of whatever order the app decided to show you. Make it a CLI Wrap it so you can run it for any address/keyword combo: import sys if __name__ == "__main__": address, keyword = sys.argv[1], sys.argv[2] # ...call the actor with {"locations": [address], "search_keyword": keyword}... python fastest_near_me.py "123 Main St, Newark, NJ, USA" "sushi" Ideas to extend it Compare cuisines : run it for "pizza", "sushi", and "burgers" at the same address and see what's actually fastest tonight across the board. Compare neighborhoods : run the same keyword across a few addresses to find which part of town has the best delivery options. Tune the score : weight rating_count in too — a 4.8 from 3 reviews is less trustworthy than a 4.5 from 500. Try it There's a free plan (1 location, 10 results per run) if you want to try this on your own address before scaling it up. UberEats Stores Search by Location and Keyword — the actor used above If you tweak the scoring formula into something better, I'd love to see it — drop it in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/bflores/i-built-a-fastest-pizza-near-me-tool-with-the-ubereats-api-and-python-loc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
