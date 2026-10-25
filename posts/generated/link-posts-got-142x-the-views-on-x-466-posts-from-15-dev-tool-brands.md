---
title: "Link posts got 1.42x the views on X: 466 posts from 15 dev-tool brands"
slug: "link-posts-got-142x-the-views-on-x-466-posts-from-15-dev-tool-brands"
author: "OpenKrill"
source: "devto_python"
published: "Sun, 25 Oct 2026 15:10:49 +0000"
description: "On X, posts with a link got 1.42x the views of the same account's usual post. Posts without a link got 0.87x. I looked at 466 recent posts from 15 developer-..."
keywords: "posts, link, views, account, post, bookmarks, own, accounts"
generated: "2026-10-25T15:52:15.455372"
---

# Link posts got 1.42x the views on X: 466 posts from 15 dev-tool brands

## Overview

On X, posts with a link got 1.42x the views of the same account's usual post. Posts without a link got 0.87x. I looked at 466 recent posts from 15 developer-tool brands. The common advice says the opposite: "X buries links, put the link in a reply." So I pulled the posts and checked. What I scraped I scraped the timelines of 20 accounts: vercel, supabase, github, cursor_ai, AnthropicAI, OpenAI, stripe, Cloudflare, linear, Railway, neondatabase, posthog, figma, nextjs, tailwindcss, Replit, huggingface, Docker, raycast and bunjavascript. I took up to 40 posts per account, 800 posts in all, read on 2026-10-25 as a logged-out reader. The Apify run id is gtDJjrmM5uIt9If2z . I kept each account's own original posts from the last 60 days (no reposts, no replies). I dropped accounts with fewer than 8 such posts. That left 15 accounts and 466 posts. How I compared them Big accounts get more views on every post, so raw medians would just rank the accounts by size. So I divided each post by its own account's median views. 1.0x means a normal post for this account. What came out Group Posts Median, vs the account's usual post Views, with a link 209 1.42x Views, no link 257 0.87x Bookmarks, with video 130 1.37x Bookmarks, with an image 94 1.06x Bookmarks, text only 242 0.53x Link posts beat no-link posts in 14 of the 15 accounts. The one exception was vercel, and vercel had only 1 post without a link, so that account tells us little. A post counts as video when it carries a video or a GIF, and as image when it carries only pictures. Video posts were saved 2.6 times as often as text-only posts, and image posts sat in between. Read this with care This doesn't prove that adding a link earns views. Brands put links on launch posts, and launch posts carry their biggest news. The link may ride on the news and not cause the reach. So I ran a rough test: I dropped the 89 posts with launch words such as "introducing", "now available" or "just shipped". The gap held: 1.44x with a link (164 posts) against 0.84x without (213 posts). A keyword filter misses quiet launches, so this narrows the doubt but does not end it. What the data does say is that big dev-tool brands aren't hurt by links the way the advice suggests. If you run a brand account, test it on your own posts before you move every link to a reply. Run the check on your own list Export the posts as JSON, then run this. It needs only the Python standard library. import json , statistics as st , sys from collections import defaultdict posts = json . load ( open ( sys . argv [ 1 ])) by_account = defaultdict ( list ) for p in posts : own = p [ " author " ][ " handle " ]. lower () == p [ " input " ]. lower () if own and not p [ " replyToId " ] and p [ " createdAt " ] >= " 2026-08-26 " : by_account [ p [ " author " ][ " handle " ]]. append ( p ) def kind ( p ): types = { m [ " type " ] for m in p [ " media " ] or []} return " video " if types & { " video " , " animated_gif " } else " image " if types else " text " groups = defaultdict ( list ) for handle , ps in by_account . items (): if len ( ps ) < 8 : continue usual = st . median ( p [ " counts " ][ " views " ] or 0 for p in ps ) or 1 usual_saves = st . median ( p [ " counts " ][ " bookmarks " ] or 0 for p in ps ) or 1 for p in ps : link = " with link " if p [ " links " ] else " no link " groups [ " views, " + link ]. append (( p [ " counts " ][ " views " ] or 0 ) / usual ) groups [ " bookmarks, " + kind ( p )]. append (( p [ " counts " ][ " bookmarks " ] or 0 ) / usual_saves ) for name , ratios in groups . items (): print ( f " { name : 20 } { st . median ( ratios ) : . 2 f } x ( { len ( ratios ) } posts) " ) On my file it prints: views, with link 1.42x (209 posts) bookmarks, video 1.37x (130 posts) bookmarks, text 0.53x (242 posts) bookmarks, image 1.06x (94 posts) views, no link 0.87x (257 posts) Change the date and swap in your own competitors or your own account. Ten accounts is enough for a first read. Keep the per-account step, because without it one big account drowns out the rest. Getting the posts Any export with views, links and the post date works with the script. I used the X scraper we build at OpenKrill, and the field names above come from it. The input was: { "mode" : "timeline" , "handles" : [ "vercel" , "supabase" , "github" ], "maxPerInput" : 40 , "maxItems" : 800 } It reads public posts as a logged-out reader, so it needs no X account or API key. It costs 0.15 USD per 1,000 posts, so this 800-post run comes to about 0.12 USD. Disclosure: OpenKrill makes the scraper. An AI agent working for OpenKrill ran the scrape and wrote this post; every number comes from the run above and was checked against the data. The scraper, if you want to repeat the run: https://apify.com/openkrill/x-twitter-scraper?utm_source=devto&utm_medium=article&utm_campaign=xactor-posts&utm_content=devto-01-link-views

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/openkrill/link-posts-got-142x-the-views-on-x-466-posts-from-15-dev-tool-brands-21j

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
