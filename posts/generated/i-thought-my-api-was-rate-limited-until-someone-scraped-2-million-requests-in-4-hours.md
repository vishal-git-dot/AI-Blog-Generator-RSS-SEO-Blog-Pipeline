---
title: "I Thought My API Was Rate-Limited — Until Someone Scraped 2 Million Requests in 4 Hours"
slug: "i-thought-my-api-was-rate-limited-until-someone-scraped-2-million-requests-in-4-hours"
author: "kol kol"
source: "devto_ai"
published: "Sun, 07 Jun 2026 14:04:53 +0000"
description: "I had express-rate-limit installed. I had it configured. I had tests that proved it worked. And yet, someone still scraped 2 million API requests from my pro..."
keywords: "rate, api, redis, requests, const, limiting, per, limit"
generated: "2026-06-07T14:06:36.537926"
---

# I Thought My API Was Rate-Limited — Until Someone Scraped 2 Million Requests in 4 Hours

## Overview

I had express-rate-limit installed. I had it configured. I had tests that proved it worked. And yet, someone still scraped 2 million API requests from my production server in under 4 hours. Costing me $4,200 in upstream API calls. Here's exactly what went wrong, how I found out, and the architecture I use now. The Setup That Lied to Me My API was a simple Express app. I added rate limiting like any reasonable developer would: import rateLimit from ' express-rate-limit ' ; const limiter = rateLimit ({ windowMs : 15 * 60 * 1000 , // 15 minutes max : 100 , // 100 requests per window standardHeaders : true , legacyHeaders : false , }); app . use ( ' /api/ ' , limiter ); Tests passed. I saw X-RateLimit-Limit: 100 in curl responses. I slept well. The problem? I was running 4 instances behind a load balancer. Each instance had its own in-memory counter. So the real limit was 400 requests per 15 minutes — not 100. And the attacker wasn't hitting one IP with 100 requests. They were rotating through a proxy pool of 2,000+ IPs. How It Happened At 2:47 AM, our monitoring dashboard showed something odd: API request volume spiked 800%. I dismissed it as a newsletter push going out. By 4:00 AM, the database connection pool was saturated. Queries that normally took 12ms were timing out at 30 seconds. By 6:30 AM, I checked our upstream LLM provider bill. We'd made 2.1 million API calls since midnight. At $0.002 per call, that's roughly $4,200 . The attacker was: Hitting our search endpoint with systematic keyword variations Rotating IPs from a residential proxy network Staying under per-instance rate limits by spreading requests across IPs Extracting structured data from our responses Why My Defenses Failed Defense Why It Failed express-rate-limit (in-memory) Not shared across instances IP-based limiting Proxy rotation defeated it No request logging depth Couldn't trace the attack pattern No anomaly alerts 800% spike looked like "normal traffic" The fundamental mistake: I treated rate limiting as a configuration problem instead of an architecture problem . The Fix: Distributed Rate Limiting I rebuilt the system with three layers: Layer 1: Redis Sliding Window (The Real Rate Limiter) import Redis from ' ioredis ' ; import { createClient } from ' redis-rate-limiter ' ; const redis = new Redis ( process . env . REDIS_URL ); async function checkRateLimit ( key , max , windowSec ) { const now = Date . now (); const windowStart = now - windowSec * 1000 ; // Use Redis sorted set for true sliding window await redis . zremrangebyscore ( key , 0 , windowStart ); const count = await redis . zcard ( key ); if ( count >= max ) { return { allowed : false , remaining : 0 }; } await redis . zadd ( key , now , ` ${ now } - ${ Math . random ()} ` ); await redis . expire ( key , windowSec ); return { allowed : true , remaining : max - count - 1 }; } This gives you a true 100-request limit across all instances, not 100 per instance. Layer 2: Behavioral Fingerprinting IP addresses are useless against proxy pools. Instead, I track: Request pattern entropy — Are endpoints being hit in alphabetical order? That's a scraper. Timing regularity — Requests every exactly 1.0 seconds? Bot. Header consistency — Same User-Agent, same Accept-Encoding, same everything? Bot. function calculateRequestEntropy ( requests ) { const endpoints = requests . map ( r => r . path ); const uniqueEndpoints = new Set ( endpoints ). size ; // Low entropy = sequential/scraping pattern return uniqueEndpoints / endpoints . length ; } // Entropy < 0.3 → likely scraping // Entropy > 0.7 → likely human Layer 3: Cost-Based Circuit Breakers This is the one that actually saves money: // Track estimated cost per endpoint const endpointCosts = { ' /api/search ' : 0.002 , // LLM call ' /api/analyze ' : 0.015 , // Expensive LLM call ' /api/health ' : 0 , // Cheap }; let hourlyCost = 0 ; const COST_THRESHOLD = 50 ; // Alert at $50/hr function trackCost ( endpoint ) { hourlyCost += endpointCosts [ endpoint ] || 0 ; if ( hourlyCost > COST_THRESHOLD ) { // Auto-throttle expensive endpoints expensiveEndpoints . enabled = false ; slack . alert ( `API cost spike: $ ${ hourlyCost . toFixed ( 2 )} /hr` ); } } When costs spike, expensive endpoints automatically throttle. You don't need to be awake at 3 AM to stop a bleeding wallet. The Results After 30 Days Metric Before After Successful scrapes 2 incidents 0 Peak API cost/hr $4,200 $12 False positive blocks 0 2 (tuned rules) Legitimate user impact N/A None detected The Real Lesson Rate limiting isn't about setting a number. It's about understanding: Your threat model — Who would want to scrape your API and why? Your architecture — In-memory doesn't work in a distributed system. Period. Your cost exposure — Know the dollar cost per endpoint, and set automatic circuit breakers. The $4,200 mistake taught me that security theater — rate limiting that looks right but isn't — is worse than no rate limiting at all. It gives you confidence to deploy things that aren't actually protected. Have you ever been bitten by a "working" defense that wasn't? What's your rate limiting setup? Drop it in the comments — I'm always looking for ways to improve mine.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kollittle/i-thought-my-api-was-rate-limited-until-someone-scraped-2-million-requests-in-4-hours-509d

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
