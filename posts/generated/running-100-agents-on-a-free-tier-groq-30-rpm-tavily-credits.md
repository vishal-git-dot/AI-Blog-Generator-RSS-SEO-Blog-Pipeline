---
title: "Running 100 agents on a free tier (Groq 30 RPM, Tavily credits)"
slug: "running-100-agents-on-a-free-tier-groq-30-rpm-tavily-credits"
author: "Dev Jhawar"
source: "devto_python"
published: "Tue, 20 Oct 2026 16:27:27 +0000"
description: "GridMind is a spreadsheet where every cell is its own research agent. You type "Stripe" in a row, "who is the CEO?" in a column, hit Run, and an agent goes o..."
keywords: "self, you, one, cell, none, run, per, not"
generated: "2026-10-20T16:39:11.044872"
---

# Running 100 agents on a free tier (Groq 30 RPM, Tavily credits)

## Overview

GridMind is a spreadsheet where every cell is its own research agent. You type "Stripe" in a row, "who is the CEO?" in a column, hit Run, and an agent goes off, searches the web, and fills the cell with an answer and sources. You can try it live at grid-mind-tan.vercel.app , and the code is on GitHub . Cute idea. Then you do the maths. A 10 x 10 sheet is 100 cells. Each cell needs an LLM call to plan, one or two searches, and an LLM call to answer. Groq's free tier gives me around 30 requests a minute. Tavily gives 1000 search credits a month. So one enthusiastic click on "Run all" can eat a decent chunk of the month, and the 429s start before the first row is even done. I didn't want to pay for anything yet. So the job became: make the free tier last. It turned out to be four small things, none of them clever. 1. A limiter that sits under the limit The first fix is the obvious one: don't send more than the provider allows. It's a sliding window, about 20 lines ( resilience.py ): class RateLimiter : def __init__ ( self , rate : int , per : float = 60.0 ) -> None : self . rate , self . per = max ( 1 , rate ), per self . _hits : deque [ float ] = deque () self . _lock = asyncio . Lock () async def acquire ( self ) -> None : while True : async with self . _lock : now = time . monotonic () while self . _hits and now - self . _hits [ 0 ] >= self . per : self . _hits . popleft () if len ( self . _hits ) < self . rate : self . _hits . append ( now ) return wait = self . per - ( now - self . _hits [ 0 ]) await asyncio . sleep ( wait + random . random () * 0.1 ) Two details I care about. The limit is set to 25 for Groq, not 30. If you aim exactly at the line, clock skew and a retry or two will push you over it. And the little random sleep at the end is there so a hundred waiting workers don't all wake up on the same tick and stampede. 2. When it still fails, retry like an adult Limiter or not, you will get a 429 or a 503 sometimes. The retry is exponential backoff with jitter, and it respects Retry-After when the server sends one. If the server tells you how long to wait, believe it: retry_after = getattr ( getattr ( exc , " response " , None ), " headers " , {}). get ( " retry-after " ) delay = float ( retry_after ) if retry_after and str ( retry_after ). replace ( " . " , "" ). isdigit () else None await asyncio . sleep ( min ( cap , delay if delay is not None else random . uniform ( 0 , base * 2 ** i ))) Only transient errors (408, 429, 5xx, timeouts) are retried. Hitting my own daily call budget for the LLM is not transient either, retrying it just burns time, so that one raises a separate non-retryable error. 3. Stop asking the same question twice This one saved the most. In a sheet about companies, the cells in one row ask near-identical things about the same entity. Searching "Stripe CEO" and "Stripe chief executive" is wasted money when the results are basically the same. So searches and page reads go through a small cache with a TTL (an hour by default). The part that matters is the in-flight de-dup: if ten cells ask for the same thing at the same moment, only the first one actually goes out, and the rest wait on its result. if key in self . _inflight : return await asyncio . shield ( self . _inflight [ key ]) A plain cache doesn't help here. When you hit Run all, all the identical requests start before any of them has finished , so there's nothing in the cache yet. Sharing the pending call is what fixes that. If the shared call fails, the failure is shared too, and nothing bad gets cached. 4. Spend the paid credit once, and have a floor to fall to Tavily is good, so it gets the first query of each cell. The second query goes to DuckDuckGo, which is free. A cell costs one credit instead of two. On top of that there's a counter that stops me at 900 credits a month, so I never hit the 1000 wall mid-run. And if Tavily errors out or the budget is gone, the search quietly falls back to DuckDuckGo. Results get a bit worse, but the sheet still fills. DuckDuckGo gets rate-limited a lot too. For the secondary query that's fine, a miss just returns an empty list and the agent works with what it has. For the primary query, a miss is a real error. What this doesn't solve Being honest here: Every limiter and counter lives in memory, per instance . Run two API instances and you've doubled your limits without meaning to. Going global means Redis counters, which I haven't done yet. The fallback means answer quality is not constant. A cell answered from DuckDuckGo snippets can be thinner than one answered from Tavily. I picked 25, 40 and 900 by feel and the providers' published limits, not by load testing. None of it is fancy. A limiter, a retry, a cache that shares in-flight work, and a budget with a fallback. But together they're why a sheet of 100 agents can run on a setup that costs me nothing. If you want to see the limiter at work, open any cell in the live demo and check its trace. Every search the agent made is listed there. Code is here if you want to poke at it: github.com/DEVJHAWAR11/GridMind

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev_jhawar/running-100-agents-on-a-free-tier-groq-30-rpm-tavily-credits-pgi

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
