---
title: "Bulk Google + Amazon keyword search volume for about $3 per 1,000 keywords (API, n8n, Claude)"
slug: "bulk-google-amazon-keyword-search-volume-for-about-3-per-1000-keywords-api-n8n-claude"
author: "Pravinraj Vincent"
source: "devto_python"
published: "Sat, 17 Oct 2026 20:08:34 +0000"
description: "If you've ever pasted 300 keywords into an SEO suite and hit a daily cap, or you just want search volume inside a script or an AI agent without paying for a ..."
keywords: "keyword, google, volume, keywords, amazon, search, apify, you"
generated: "2026-10-17T20:22:56.708348"
---

# Bulk Google + Amazon keyword search volume for about $3 per 1,000 keywords (API, n8n, Claude)

## Overview

If you've ever pasted 300 keywords into an SEO suite and hit a daily cap, or you just want search volume inside a script or an AI agent without paying for a seat, this is the setup I use: one API call in, one row per keyword out. What you get per keyword Google monthly search volume, with up to 4 years of monthly history CPC, competition, keyword difficulty and search intent Month-over-month, quarter-over-quarter and year-over-year trend Amazon monthly search volume (a modeled estimate, because Amazon doesn't publish volumes) An optional USPTO trademark-risk flag, useful if you sell on Etsy, Merch by Amazon or KDP The data comes from DataForSEO. Google figures come from its Google Ads-based keyword database (refreshed about monthly), so no Google Ads account is needed. A real run: 12 keywords, United States I mixed SEO-tool keywords with product keywords to show the range: Keyword Google / month Amazon / month CPC KD YoY Trademark flag google keyword planner 49,500 5,759 $18.10 47 -18% high ("google") keyword research tool 4,400 299 $15.75 81 -81% none etsy seo 2,900 224 $7.69 22 -47% high ("etsy") long tail keywords 1,000 149 $46.37 61 -70% none keyword search volume 880 74 $12.61 79 -55% none amazon keyword tool 260 74 $12.83 17 -77% none coloring book for adults 60,500 1,907 $0.61 1 -18% none teacher gift 18,100 1,645 $0.88 0 0% none pickleball paddle 301,000 11,594 $1.50 25 -45% medium Three things stood out: Generic "keyword tool" searches are falling fast. "keyword research tool" is down 81% year over year and "free keyword tool" is down 80%. My guess is that people now ask an AI assistant instead. That's also the best argument for piping keyword data into those assistants (see below). CPC and difficulty don't move together. "long tail keywords" has a $46 CPC but KD 61. "amazon keyword tool" has a $12.83 CPC at KD 17, a much easier target. The trademark flag isn't noise for sellers. "etsy seo" and "google keyword planner" come back high-risk because of live marks. That's irrelevant for a blog post, but it matters if the phrase goes on a T-shirt. "pickleball paddle" is medium because live marks contain "pickleball". That doesn't mean you can't use it. It means you should check the record before printing it. Option 1: Python from apify_client import ApifyClient client = ApifyClient ( " <YOUR_APIFY_TOKEN> " ) run = client . actor ( " vncntlabs/keyword-search-volume " ). call ( run_input = { " keywords " : [ " teacher gift " , " coloring book for adults " , " pickleball paddle " ], " sources " : [ " google " , " amazon " ], " location " : " United States " , " trademarkCheck " : True , }) for row in client . dataset ( run . default_dataset_id ). iterate_items (): print ( row [ " keyword " ], row [ " googleSearchVolume " ], row [ " amazonSearchVolume " ], row [ " cpcUsd " ]) Option 2: plain HTTP (n8n, Make, Zapier, curl) curl -X POST "https://api.apify.com/v2/acts/vncntlabs~keyword-search-volume/run-sync-get-dataset-items" \ -H "Authorization: Bearer $APIFY_TOKEN " -H "Content-Type: application/json" \ -d '{"keywords":["teacher gift","pickleball paddle"],"sources":["google"],"location":"United States"}' In n8n, that's one HTTP Request node, or the Apify node with "Run actor and get dataset". Option 3: from Claude, ChatGPT or Cursor (MCP) Apify runs a hosted MCP server. Add it to your client: { "mcpServers" : { "apify" : { "url" : "https://mcp.apify.com" } } } Then ask something like "Get US Google and Amazon search volume for these 40 keywords and sort by volume per KD point." The assistant finds the Actor, runs it, and reads the dataset. You pay only for the rows returned. What it costs Event Price Keyword with Google volume $0.003 Keyword with Amazon volume $0.004 Batch fee (per up to 700 Google / 1,000 Amazon keywords that returned data) $0.05 Trademark check $0.001 So 1,000 Google-only keywords cost $3.10 , and keywords with no data aren't charged. The 12-keyword run above with Google, Amazon and trademark checks came to about $0.20 at list price. You can set a maximum charge per run, and the Actor stops before exceeding it. A new Apify account's free monthly credit covers a few hundred keywords. To be fair to the competition: if you only need Google numbers for very large lists, some Store Actors charge less per row (I keep a dated comparison on our site). Where this one is different is Amazon volume and the trademark flag in the same row. Caveats Volumes are rounded monthly averages, so use them to compare keywords, not as exact traffic. Amazon volume is modeled, so treat it as relative. Trademark flags are automated screening against live U.S. federal marks only. They're not legal advice, and no flag doesn't mean safe. Code: https://github.com/PravinrajV/vncntlabs-apify-examples/tree/main/01-keyword-search-volume Try it: https://apify.com/vncntlabs/keyword-search-volume . Questions or missing features? Leave a comment. I read them all. Disclosure: I build and sell the Apify Actor used in this post (VNCNT Labs). Every number in this post comes from a real run on October 17, 2026, and prices are the Apify Store list prices on that date.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/vncntlabs/bulk-google-amazon-keyword-search-volume-for-about-3-per-1000-keywords-api-n8n-claude-f87

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
