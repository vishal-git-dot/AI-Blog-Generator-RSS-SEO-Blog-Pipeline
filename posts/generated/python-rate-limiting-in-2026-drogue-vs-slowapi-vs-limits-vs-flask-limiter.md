---
title: "Python rate limiting in 2026: drogue vs slowapi vs limits vs flask-limiter"
slug: "python-rate-limiting-in-2026-drogue-vs-slowapi-vs-limits-vs-flask-limiter"
author: "zlynv"
source: "devto_webdev"
published: "Sun, 25 Oct 2026 03:54:31 +0000"
description: "You're adding rate limiting to a Python web app. The usual suspects are slowapi, flask-limiter, django-ratelimit, and the limits library. There's also drogue..."
keywords: "limiter, drogue, slowapi, request, yes, you, rate, flask"
generated: "2026-10-25T04:06:12.673426"
---

# Python rate limiting in 2026: drogue vs slowapi vs limits vs flask-limiter

## Overview

You're adding rate limiting to a Python web app. The usual suspects are slowapi, flask-limiter, django-ratelimit, and the limits library. There's also drogue. Here's how they compare. The short version drogue slowapi flask-limiter limits request: Request in signatures No Yes Yes N/A (standalone) FastAPI Yes Yes No Via adapter Django Yes No No Via adapter Flask Yes No Yes Via adapter Algorithms 5 (Token Bucket, Sliding, Fixed, GCRA, Leaky) 1 (Fixed Window) 1 (Fixed Window) 3 WebSocket Yes No No No DDoS detection Yes No No No Auto-ban Yes No No No CAPTCHA challenges Yes No No No Shadow mode Yes No No No Custom 429 body error_renderer Custom handler Custom handler N/A Zero runtime deps Yes No (starlette) No (flask) No The request: Request problem This is the biggest difference and the reason drogue exists. slowapi requires you to add request: Request to every decorated endpoint: # slowapi from slowapi import Limiter from slowapi.util import get_remote_address from starlette.requests import Request limiter = Limiter ( key_func = get_remote_address ) @app.get ( " /api/data " ) @limiter.limit ( " 10/minute " ) async def get_data ( request : Request ): # rate limiter leaked into your signature return { " data " : " value " } Now your business logic is coupled to the rate limiter. Change the limiter, rewrite every endpoint. Test the endpoint without HTTP, mock the request. drogue extracts identity from the ASGI context without touching your signature: # drogue from drogue.adapters.fastapi import DrogueLimiter limiter = DrogueLimiter ( app ) @app.get ( " /api/data " ) @limiter.limit ( " 10/minute " ) async def get_data (): # clean return { " data " : " value " } Algorithm choice matters slowapi uses Fixed Window only. "30/minute" means exactly 30 requests, then hard stop. That's fine for strict quotas but harsh on bursty traffic. drogue defaults to Token Bucket, which allows short bursts above the average rate. A "30/minute" limit with Token Bucket might briefly allow 35 requests, then smooth out. For strict quotas, use algorithm=AlgorithmType.FIXED_WINDOW . The choice between burst-friendly and strict-per-window is a design decision, not a bug. slowapi just doesn't offer the option. WebSocket rate limiting Neither slowapi nor flask-limiter supports WebSocket rate limiting. If you have real-time features (chat, notifications, games), you need drogue or roll your own. Built-in defense layers drogue goes beyond rate limiting: DDoS detection - Z-score anomaly detection across client rate distributions Auto-ban - progressive ban with doubling duration (5m to 160m) Trust scoring - 9x throughput for verified users (state machine: Unknown/Normal/Trusted/Distrusted/Banned) CAPTCHA challenges - Turnstile integration with signed pass cookies and replay-proof tokens Circuit breaker - Closed/Open/HalfOpen states for failing backends Shadow mode - test rules without enforcing, collect metrics first All off by default. Enable what you need. Custom 429 responses slowapi makes you replace the exception handler entirely. drogue gives you a callback: from starlette.responses import JSONResponse def my_renderer ( request , exc , headers ): return JSONResponse ( { " error " : " rate_limited " , " retry_after " : exc . retry_after }, status_code = 429 , headers = headers , ) limiter = DrogueLimiter ( app , error_renderer = my_renderer ) Rate limit headers ( X-RateLimit-Limit , X-RateLimit-Remaining , Retry-After ) are injected automatically. When to use which Use drogue if you want clean signatures, multiple algorithms, WebSocket support, defense layers, or you're migrating from slowapi and want less code. Use slowapi if you're on FastAPI only, already have it integrated, and don't mind request: Request in your signatures. Use flask-limiter if you're on Flask and want something battle-tested. Use limits if you need a standalone rate limiter (CLI tools, scripts, etc.) without a web framework. Install pip install drogue[fastapi] # or [django], [flask], [drf] GitHub | Full docs | Migration guide

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/zlynv/python-rate-limiting-in-2026-drogue-vs-slowapi-vs-limits-vs-flask-limiter-3fe7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
