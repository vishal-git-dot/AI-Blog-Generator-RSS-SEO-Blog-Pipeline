---
title: "Retry-Safe API Calls in Node.js: Idempotency Keys, Backoff and 429s"
slug: "retry-safe-api-calls-in-nodejs-idempotency-keys-backoff-and-429s"
author: "APIHiver"
source: "devto_webdev"
published: "Thu, 15 Oct 2026 20:17:51 +0000"
description: "A user taps "Pay" twice. Or your request times out after the server already processed it. Retry blindly and you may charge someone twice. Never retry and you..."
keywords: "key, retry, server, attempt, after, res, you, const"
generated: "2026-10-15T21:09:19.878735"
---

# Retry-Safe API Calls in Node.js: Idempotency Keys, Backoff and 429s

## Overview

A user taps "Pay" twice. Or your request times out after the server already processed it. Retry blindly and you may charge someone twice. Never retry and you lose real requests. This post shows a small Node.js client that retries the right things, waits the right amount, and keeps POST requests safe. The three rules Retry only what is safe to retry. Network errors, timeouts, 408 , 429 , 502 , 503 and 504 . Never retry 400 , 401 , 403 , 404 or 422 : the same request will fail the same way. Make POST requests safe with an idempotency key. Generate one key per intended operation and reuse it on every retry of that operation. The server remembers the result for that key and returns it again instead of doing the work twice. Wait intelligently. Use exponential backoff with jitter, and obey the Retry-After header when the server sends one. The code import { randomUUID } from " node:crypto " ; const RETRYABLE = new Set ([ 408 , 429 , 502 , 503 , 504 ]); const sleep = ( ms ) => new Promise (( resolve ) => setTimeout ( resolve , ms )); function waitMs ( attempt , retryAfter ) { // 1. The server told us exactly how long to wait. if ( retryAfter ) { const seconds = Number ( retryAfter ); if ( ! Number . isNaN ( seconds )) return seconds * 1000 ; const date = Date . parse ( retryAfter ); if ( ! Number . isNaN ( date )) return Math . max ( 0 , date - Date . now ()); } // 2. Otherwise: exponential backoff (0.5s, 1s, 2s...) with full jitter. const ceiling = Math . min ( 30 _000 , 500 * 2 ** attempt ); return Math . random () * ceiling ; } export async function apiCall ( url , { method = " GET " , body , headers = {}, retries = 4 } = {}) { // One key per intended operation, reused on every retry below. const key = method === " POST " ? randomUUID () : undefined ; for ( let attempt = 0 ; ; attempt ++ ) { let res ; try { res = await fetch ( url , { method , headers : { " Content-Type " : " application/json " , ...( key && { " Idempotency-Key " : key }), ... headers , }, body : body ? JSON . stringify ( body ) : undefined , signal : AbortSignal . timeout ( 10 _000 ), }); } catch ( err ) { // Network error or timeout: the server may or may not have seen it. if ( attempt >= retries ) throw err ; await sleep ( waitMs ( attempt )); continue ; } if ( res . ok ) return res . status === 204 ? null : res . json (); if ( ! RETRYABLE . has ( res . status ) || attempt >= retries ) { throw new Error ( `HTTP ${ res . status } : ${ await res . text ()} ` ); } await sleep ( waitMs ( attempt , res . headers . get ( " retry-after " ))); } } Usage: const payment = await apiCall ( " https://api.example.com/v1/payments " , { method : " POST " , body : { amount : 4900 , currency : " usd " }, }); Why each part is there The key is created outside the loop. That is the whole trick. If you generate a new key per attempt, the server sees three different payments. Timeouts count as retryable. A timeout does not mean the request failed, only that you did not hear back. The idempotency key is what makes retrying safe. Retry-After wins over our own guess. When a server says "wait 20 seconds", waiting 1 second just earns another 429 . Jitter matters. If 1,000 clients all retry after exactly 2 seconds, they hit the server together again. Random waiting spreads them out. Client errors are not retried. A 422 means your data is wrong. Retrying will not fix it. What the server must do A key only helps if the API honours it. On the server side: Store the result of the first request under the key, scoped to the authenticated user. If the same key arrives again with the same body, return the stored response instead of repeating the work. If the same key arrives with a different body, reject it with an error. That is a bug in the client. Expire old keys after a documented period. Many providers keep them for around a day, so check the docs of the API you use. Important: only send Idempotency-Key to an API that documents support for it. If it does not, retrying a POST after a timeout can still create duplicates. In that case, retry only after checking whether the first request went through. Note that the Idempotency-Key header is still an IETF draft rather than a finished standard, but it is widely used in practice. Things I would add next A total time budget , so retries stop after, say, 30 seconds no matter how many attempts remain. Logging the attempt number, status and key, so a support ticket can be traced. A circuit breaker for when a provider is down and every call is going to fail anyway. Over to you How do you handle retries in your own API clients: a library, a hand-rolled helper like this one, or "we just hope for the best"? And has a duplicate request ever bitten you in production? I would like to hear the stories, and I will answer every comment.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/api_hiver/retry-safe-api-calls-in-nodejs-idempotency-keys-backoff-and-429s-50pc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
