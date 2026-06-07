---
title: "Get any Instagram profile data in 10 lines of Python"
slug: "get-any-instagram-profile-data-in-10-lines-of-python"
author: "Pouria Anushiravani"
source: "devto_python"
published: "Sun, 07 Jun 2026 13:44:55 +0000"
description: "Every few months I need to pull Instagram profile data for a side project. And every time, I'd go through the same cycle: spin up instagrapi , get a working ..."
keywords: "you, username, instagram, data, get, requests, headers, profile"
generated: "2026-06-07T14:06:36.535134"
---

# Get any Instagram profile data in 10 lines of Python

## Overview

Every few months I need to pull Instagram profile data for a side project. And every time, I'd go through the same cycle: spin up instagrapi , get a working session, watch it break two days later when Instagram changed something internally, then spend an evening debugging. Last week I found a much simpler approach. Here's the whole thing. What we're building A script that fetches any public Instagram profile — follower count, bio, post count, verification status — with a single HTTP request. No browser automation, no cookie juggling, no proxies. Steps: Install requests (you probably already have it) Get a free API key from hikerapi.com — 100 requests, no credit card Copy the snippet below The code import requests headers = { " x-access-key " : " YOUR_KEY " } r = requests . get ( " https://api.hikerapi.com/v2/user/by/username?username=instagram " , headers = headers ) data = r . json () print ( f " Followers: { data [ ' follower_count ' ] : , } " ) print ( f " Posts: { data [ ' media_count ' ] : , } " ) print ( f " Bio: { data [ ' biography ' ] } " ) Output: Followers: 671,143,291 Posts: 7,842 Bio: Connecting you to what matters... That's it. Swap in any public username and you get back a clean JSON object with everything you'd see on the profile page. Why this beats scraping Scraping Instagram with a headless browser or a library like instagrapi means managing sessions, rotating IPs, and rewriting your code every time Instagram updates their internals. A hosted REST API absorbs all of that — you just call an endpoint and get data. HikerAPI starts at $0.001 per request . Checking 100 profiles costs $0.10. The free tier covers all the experimentation you need. Going further The same pattern works for fetching recent posts, follower lists, hashtag feeds, and more. Once you have the base call working, it's easy to loop over a list of usernames and dump results into a CSV: import requests , csv , time headers = { " x-access-key " : " YOUR_KEY " } usernames = [ " natgeo " , " nasa " , " github " ] with open ( " profiles.csv " , " w " , newline = "" ) as f : w = csv . DictWriter ( f , fieldnames = [ " username " , " followers " , " posts " ]) w . writeheader () for username in usernames : r = requests . get ( f " https://api.hikerapi.com/v2/user/by/username?username= { username } " , headers = headers ) d = r . json () w . writerow ({ " username " : username , " followers " : d [ " follower_count " ], " posts " : d [ " media_count " ] }) time . sleep ( 0.5 ) # be polite print ( " Done — profiles.csv written " ) Run that and you have a clean spreadsheet of profile stats in seconds. Pipe it into pandas for analysis, or wire it up as a cron job for weekly tracking. Wrapping up If you're building anything that needs Instagram data — competitive research, influencer tracking, content analytics — a hosted API is genuinely the right call. The free 100 requests are enough to build something real before you spend anything. Drop a comment if you build something with this — curious what people are tracking.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/pouria_anushiravani_42b89/get-any-instagram-profile-data-in-10-lines-of-python-462g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
