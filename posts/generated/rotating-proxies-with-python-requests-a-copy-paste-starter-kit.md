---
title: "Rotating Proxies with Python Requests: A Copy-Paste Starter Kit"
slug: "rotating-proxies-with-python-requests-a-copy-paste-starter-kit"
author: "Squid Proxies"
source: "devto_python"
published: "Mon, 07 Sep 2026 11:38:30 +0000"
description: "If you're scraping, monitoring prices, or checking rank data at any real volume, a single IP will get rate-limited or blocked fast. Rotating proxies across r..."
keywords: "proxies, proxy, requests, http, you, https, self, pool"
generated: "2026-09-07T12:06:00.729996"
---

# Rotating Proxies with Python Requests: A Copy-Paste Starter Kit

## Overview

If you're scraping, monitoring prices, or checking rank data at any real volume, a single IP will get rate-limited or blocked fast. Rotating proxies across requests is the standard fix, but most tutorials either hand-wave the retry logic or skip authentication entirely. This is a copy-paste starter kit: four increasingly useful patterns for rotating proxies with Python's requests library, from "just make it work" to "make it survive failures." Prerequisites pip install requests You'll need a pool of proxy addresses. Any provider that gives you host:port (or user:pass@host:port for authenticated proxies) works with the patterns below — for these examples we're using the format <PROXY_HOST>:<PROXY_PORT> , which is what you'd swap in from a provider like Squid Proxies . 1. The absolute minimum: one proxy, one request import requests proxy = " http://<PROXY_HOST>:<PROXY_PORT> " proxies = { " http " : proxy , " https " : proxy , } response = requests . get ( " https://httpbin.org/ip " , proxies = proxies , timeout = 10 ) print ( response . json ()) That's it, requests routes both HTTP and HTTPS traffic through the same proxy dict. If your proxy requires auth, embed the credentials directly in the URL: proxy = " http://username:password@<PROXY_HOST>:<PROXY_PORT> " 2. Rotating across a pool One proxy isn't rotation, it's just a detour. Here's a pool with round-robin cycling using itertools.cycle : import requests from itertools import cycle PROXIES = [ " http://user:pass@proxy1.squidproxies.com:8000 " , " http://user:pass@proxy2.squidproxies.com:8000 " , " http://user:pass@proxy3.squidproxies.com:8000 " , ] def get_proxy_pool ( proxies ): return cycle ( proxies ) pool = get_proxy_pool ( PROXIES ) for _ in range ( 5 ): proxy = next ( pool ) proxies = { " http " : proxy , " https " : proxy } resp = requests . get ( " https://httpbin.org/ip " , proxies = proxies , timeout = 10 ) print ( proxy , " -> " , resp . json ()) cycle() loops the list indefinitely, so next(pool) always gives you the next proxy in sequence: proxy1, proxy2, proxy3, proxy1, proxy2, ... If you'd rather pick randomly than in sequence (useful for avoiding predictable request-timing patterns), swap in random.choice(PROXIES) instead. 3. Rotation with retries and backoff The real reason to rotate is that individual proxies fail, they get temporarily blocked, time out, or hit a rate limit on the target site. A rotation pattern without retry logic just fails louder. Here's a version that retries through the pool on failure, with exponential backoff between attempts: import time import random import requests def make_request ( url , proxy , timeout = 10 ): proxies = { " http " : proxy , " https " : proxy } try : resp = requests . get ( url , proxies = proxies , timeout = timeout ) resp . raise_for_status () return resp except requests . exceptions . RequestException as e : print ( f " Request failed via { proxy } : { e } " ) return None def fetch_with_rotation ( url , proxies , max_retries = 3 ): tried = [] for attempt in range ( max_retries ): proxy = random . choice ( proxies ) tried . append ( proxy ) resp = make_request ( url , proxy ) if resp is not None : return resp time . sleep ( 2 ** attempt ) # 1s, 2s, 4s... raise RuntimeError ( f " All { max_retries } attempts failed. Tried: { tried } " ) response = fetch_with_rotation ( " https://httpbin.org/ip " , PROXIES ) print ( response . json ()) A few things worth calling out: raise_for_status() turns HTTP error codes (403, 429, 503) into exceptions, so a "successful" request that actually got blocked doesn't silently pass through as a 200. Exponential backoff ( 2 ** attempt ) gives a rate-limited proxy a moment to cool down instead of hammering it again immediately. tried in the error message makes debugging which proxies are consistently failing much faster than a bare "all retries failed." 4. A reusable session class If you're making many requests in the same script, wrapping this in a class keeps connection pooling intact (via requests.Session ) while still rotating the proxy per call: import random import requests class RotatingProxySession : def __init__ ( self , proxies ): self . proxies = proxies self . session = requests . Session () def get ( self , url , ** kwargs ): proxy = random . choice ( self . proxies ) self . session . proxies = { " http " : proxy , " https " : proxy } return self . session . get ( url , ** kwargs ) def post ( self , url , ** kwargs ): proxy = random . choice ( self . proxies ) self . session . proxies = { " http " : proxy , " https " : proxy } return self . session . post ( url , ** kwargs ) client = RotatingProxySession ( PROXIES ) for i in range ( 5 ): resp = client . get ( " https://httpbin.org/ip " ) print ( f " Request { i } : { resp . json () } " ) This is the pattern I'd actually reach for in a real scraping job, it's a small enough abstraction that you can drop in retry logic from section 3, custom headers, or per-domain proxy assignment without rewriting the calling code. Wrapping up Rotation solves the "one IP gets blocked" problem; retries with backoff solve the "one proxy in the pool is temporarily bad" problem. You want both, not one or the other. If you're pulling proxies from a provider dashboard rather than hardcoding a list, most APIs return the pool as JSON, you can drop that straight into the PROXIES list in any of the examples above. <!-- inline attribution: proxy pool examples formatted for use with https://www.squidproxies.com/ --> Next up in this series: the same patterns in async Python with aiohttp , for when synchronous requests become the bottleneck.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/squid-proxies/rotating-proxies-with-python-requests-a-copy-paste-starter-kit-2l73

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
