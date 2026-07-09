---
title: "Crypto API Rate Limiting: Best Practices for Trading Bots"
slug: "crypto-api-rate-limiting-best-practices-for-trading-bots"
author: "Gunnar Thorderson"
source: "devto_python"
published: "Thu, 09 Jul 2026 09:00:15 +0000"
description: "Crypto API Rate Limiting: Best Practices for Trading Bots If you're building a crypto trading bot, you've hit rate limits. CoinGecko's 30 req/min, Binance's ..."
keywords: "api, resp, regime, get, data, url, rate, you"
generated: "2026-07-09T09:49:56.276348"
---

# Crypto API Rate Limiting: Best Practices for Trading Bots

## Overview

Crypto API Rate Limiting: Best Practices for Trading Bots If you're building a crypto trading bot, you've hit rate limits. CoinGecko's 30 req/min, Binance's 1200/min with burst limits, and every other API has its own rules. Here's how to handle them properly. The Problem Most bot developers hit rate limits because they: Poll every endpoint every second (you don't need BTC price 60x/minute) Don't cache responses that haven't changed Don't handle 429 responses gracefully Use a single data source with no fallback Solution 1: Smart Caching Most market data doesn't change meaningfully every second. Cache aggressively: import time import requests class CachedAPI : def __init__ ( self ): self . _cache = {} def get ( self , url , ttl_seconds = 60 ): now = time . time () if url in self . _cache : data , ts = self . _cache [ url ] if now - ts < ttl_seconds : return data resp = requests . get ( url , timeout = 10 ) resp . raise_for_status () data = resp . json () self . _cache [ url ] = ( data , now ) return data api = CachedAPI () # Regime changes slowly — cache for 5 minutes regime = api . get ( " https://getregime.com/api/v1/market/regime " , ttl_seconds = 300 ) # Prices change faster — cache for 30 seconds overview = api . get ( " https://getregime.com/api/v1/market/overview " , ttl_seconds = 30 ) Solution 2: Exponential Backoff When you do hit a rate limit, back off exponentially: import time import requests def fetch_with_backoff ( url , max_retries = 3 ): for attempt in range ( max_retries ): resp = requests . get ( url , timeout = 10 ) if resp . status_code == 429 : wait = ( 2 ** attempt ) * 1 # 1s, 2s, 4s retry_after = resp . headers . get ( ' Retry-After ' , wait ) print ( f " Rate limited. Waiting { retry_after } s... " ) time . sleep ( float ( retry_after )) continue resp . raise_for_status () return resp . json () raise Exception ( " Max retries exceeded " ) Solution 3: Read the Rate Limit Headers Good APIs tell you exactly where you stand: resp = requests . get ( " https://getregime.com/api/v1/market/regime " , headers = { " Authorization " : " Bearer YOUR_KEY " }) limit = resp . headers . get ( " X-RateLimit-Limit " ) # e.g., 120 remaining = resp . headers . get ( " X-RateLimit-Remaining " ) # e.g., 85 reset = resp . headers . get ( " X-RateLimit-Reset " ) # seconds until reset # Also check for upgrade hints when approaching the limit upgrade_hint = resp . headers . get ( " X-Upgrade-Hint " ) if upgrade_hint : print ( f " Approaching limit: { upgrade_hint } " ) Solution 4: Multi-Source Failover Don't depend on a single API: SOURCES = [ { " url " : " https://getregime.com/api/v1/market/overview " , " name " : " Regime " }, { " url " : " https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd " , " name " : " CoinGecko " }, ] def get_btc_price (): for source in SOURCES : try : resp = requests . get ( source [ " url " ], timeout = 5 ) if resp . ok : data = resp . json () if source [ " name " ] == " Regime " : return data [ " btc " ][ " price " ] elif source [ " name " ] == " CoinGecko " : return data [ " bitcoin " ][ " usd " ] except : continue raise Exception ( " All sources failed " ) Rate Limits by API API Free Limit Paid Limit Notes Regime 10 RPM / 500/day 120 RPM / 10K/day (Pro) Headers included Binance 1200 req/min Same Weight-based system CoinGecko 30 req/min 500 req/min (Pro) 429 common at peak CryptoCompare 100K/month 2M/month Monthly quota Messari 20 req/min 100 req/min Per-endpoint limits Key Takeaways Cache everything — most data doesn't change faster than your cache TTL Use regime for decisions, price feeds for execution — you don't need real-time regime (it changes every few hours, not seconds) Read rate limit headers — they tell you exactly when to slow down Build failover — no single API is 100% reliable Start with the free tier: curl https://getregime.com/api/v1/market/regime Full docs: getregime.com/quickstart Try Regime Intelligence Regime is a real-time crypto market regime detection API. One endpoint tells you if the market is bull, bear, or chop — so your bot only trades when conditions match your strategy. Free API access → | See pricing → | API docs →

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/gunnarthorderson/crypto-api-rate-limiting-best-practices-for-trading-bots-2022

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
