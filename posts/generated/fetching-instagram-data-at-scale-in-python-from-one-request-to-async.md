---
title: "Fetching Instagram Data at Scale in Python: From One Request to Async"
slug: "fetching-instagram-data-at-scale-in-python-from-one-request-to-async"
author: "SHINO"
source: "devto_python"
published: "Thu, 23 Jul 2026 08:20:45 +0000"
description: "I collect Instagram data for <私が収集しているもの・用途 例: hashtag research for my content projects>, and at some point "just call the API in a loop" stopped being fast ..."
keywords: "name, headers, asyncio, api, requests, async, session, data"
generated: "2026-07-23T08:38:07.282116"
---

# Fetching Instagram Data at Scale in Python: From One Request to Async

## Overview

I collect Instagram data for <私が収集しているもの・用途 例: hashtag research for my content projects>, and at some point "just call the API in a loop" stopped being fast enough. Here's how I went from a single request to concurrent fetching in Python, using HikerAPI — a REST API for Instagram data (auth is one header, from $0.001/request, 100 free requests to start). The starting point: one request Everything begins with a plain synchronous call: import requests headers = { " x-access-key " : " YOUR_KEY " } r = requests . get ( " https://api.hikerapi.com/v2/hashtag/medias/top " , params = { " name " : " photography " }, headers = headers , ) print ( r . json ()) This returns the top posts for a hashtag as JSON. Simple. But if you have <私のボリューム 例: a few hundred hashtags or usernames> to go through, a sequential loop means each request waits for the previous one to finish. At ~0.5–1s per round trip, hundreds of items turn into many minutes of waiting for what is mostly network idle time. Option 1: threads (smallest change to your code) Since this is I/O-bound work, ThreadPoolExecutor gets you most of the win with almost no rewrite: from concurrent.futures import ThreadPoolExecutor import requests headers = { " x-access-key " : " YOUR_KEY " } HASHTAGS = [ " photography " , " travel " , " food " ] # your list here def fetch_hashtag ( name ): r = requests . get ( " https://api.hikerapi.com/v2/hashtag/medias/top " , params = { " name " : name }, headers = headers , timeout = 30 , ) r . raise_for_status () return name , r . json () with ThreadPoolExecutor ( max_workers = 10 ) as pool : for name , data in pool . map ( fetch_hashtag , HASHTAGS ): print ( name , len ( data )) Ten workers roughly means ten requests in flight at once — a 10x wall-clock speedup on a big list. Option 2: asyncio + aiohttp (better for large volumes) For bigger batches I switched to asyncio , mainly because a semaphore makes concurrency control explicit: import asyncio import aiohttp HEADERS = { " x-access-key " : " YOUR_KEY " } CONCURRENCY = 10 async def fetch_hashtag ( session , sem , name ): async with sem : async with session . get ( " https://api.hikerapi.com/v2/hashtag/medias/top " , params = { " name " : name }, ) as r : r . raise_for_status () return name , await r . json () async def main ( hashtags ): sem = asyncio . Semaphore ( CONCURRENCY ) async with aiohttp . ClientSession ( headers = HEADERS ) as session : tasks = [ fetch_hashtag ( session , sem , h ) for h in hashtags ] return await asyncio . gather ( * tasks ) results = asyncio . run ( main ([ " photography " , " travel " , " food " ])) The semaphore is the important part: without it, gather fires everything at once, which brings us to… Rate limits: don't hammer the API A few things I do to stay polite and keep runs stable: Cap concurrency. I stay around 10 in-flight requests. More than that mostly increases error rates, not throughput. Back off on 429/5xx. Retry with exponential backoff instead of failing the whole batch: async def fetch_with_retry ( session , sem , name , retries = 3 ): for attempt in range ( retries ): try : return await fetch_hashtag ( session , sem , name ) except aiohttp . ClientResponseError as e : if e . status in ( 429 , 500 , 502 , 503 ) and attempt < retries - 1 : await asyncio . sleep ( 2 ** attempt ) # 1s, 2s, 4s continue raise Save as you go. At $0.001/request the cost of a batch is small, but re-running a half-failed batch is still wasted money. I write each result to disk (JSONL) as it arrives, so a crash only re-fetches what's missing. Takeaway One-off calls: plain requests is fine. Hundreds of items: ThreadPoolExecutor , 10 workers, done in minutes. Ongoing/large collection: asyncio + semaphore + retry, writing results incrementally. The nice thing about having Instagram data behind a plain REST API is that all the usual Python concurrency patterns just work — no session juggling or scraper babysitting. How do you handle batch collection in your projects — threads or asyncio? And what concurrency do you find APIs generally tolerate? Disclosure: this post is part of HikerAPI's reward program (rewarded in API credits). The code and workflow are my own.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/shino_17251665a6a8538491b/fetching-instagram-data-at-scale-in-python-from-one-request-to-async-4peg

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
