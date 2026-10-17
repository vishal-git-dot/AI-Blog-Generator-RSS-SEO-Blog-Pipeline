---
title: "Your retry logic has never seen a real 429. Here is how to test it with a local fault-injecting mock"
slug: "your-retry-logic-has-never-seen-a-real-429-here-is-how-to-test-it-with-a-local-fault-injecting-mock"
author: "rene"
source: "devto_python"
published: "Sat, 17 Oct 2026 03:16:59 +0000"
description: "Most LLM client code has a retry branch that has never actually run. The provider returns 200 in every test, so the 429 , 500 and timeout paths sit untested ..."
keywords: "your, retry, schedule, status, after, self, has, client"
generated: "2026-10-17T03:51:06.689605"
---

# Your retry logic has never seen a real 429. Here is how to test it with a local fault-injecting mock

## Overview

Most LLM client code has a retry branch that has never actually run. The provider returns 200 in every test, so the 429 , 500 and timeout paths sit untested until production hits them at 3am. The fix is cheap: point your client at a local server that fails on a schedule you control. The idea Run a tiny HTTP server on localhost that mimics a chat-completions endpoint. Give it a failure schedule, for example: [ { "status" : 429 , "retry_after" : 2 }, { "status" : 500 }, { "status" : "timeout" }, { "status" : 200 } ] Each incoming request consumes the next step. Your client sees a 429 with a Retry-After header, then a 500, then a hang, then a good response. What to assert Retry-After is honored. The second attempt should not fire before the header says it can. There is a time budget. The loop gives up after N seconds, not after infinity. Timeouts are set. A hung request raises instead of blocking forever. Non-retryable errors fail fast. A 400 should not be retried. Backoff has jitter. Two clients should not retry in lockstep. A minimal version import json , sys , time from http.server import BaseHTTPRequestHandler , HTTPServer SCHEDULE = json . load ( open ( sys . argv [ 1 ])) step = { " i " : 0 } class H ( BaseHTTPRequestHandler ): def do_POST ( self ): s = SCHEDULE [ min ( step [ " i " ], len ( SCHEDULE ) - 1 )] step [ " i " ] += 1 if s [ " status " ] == " timeout " : time . sleep ( 60 ) return self . send_response ( s [ " status " ]) if " retry_after " in s : self . send_header ( " Retry-After " , str ( s [ " retry_after " ])) self . end_headers () self . wfile . write ( b ' { " choices " :[{ " message " :{ " content " : " ok " }}]} ' ) HTTPServer (( " 127.0.0.1 " , 9797 ), H ). serve_forever () Point your client's base URL at http://127.0.0.1:9797 and run your normal code path. If you want it packaged I bundled a slightly more complete version (schedule file, README, examples) as a pay-what-you-want download, minimum $1: https://renevibe76.gumroad.com/l/sargxm The snippet above is enough to get started on your own, though. The point is to see your retry code run at least once before production does it for you.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/renev3408/your-retry-logic-has-never-seen-a-real-429-here-is-how-to-test-it-with-a-local-fault-injecting-mock-2pi2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
