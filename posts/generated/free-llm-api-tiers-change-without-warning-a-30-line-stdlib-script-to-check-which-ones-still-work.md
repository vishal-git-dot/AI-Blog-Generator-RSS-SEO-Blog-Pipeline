---
title: "Free LLM API tiers change without warning — a 30-line stdlib script to check which ones still work"
slug: "free-llm-api-tiers-change-without-warning-a-30-line-stdlib-script-to-check-which-ones-still-work"
author: "rene"
source: "devto_python"
published: "Mon, 28 Sep 2026 13:08:36 +0000"
description: "Free tiers on LLM APIs are a moving target. A provider that worked last week silently drops to a paid-only plan, rate-limits harder, or deprecates the model ..."
keywords: "content, free, model, time, name, llm, check, status"
generated: "2026-09-28T13:27:07.928889"
---

# Free LLM API tiers change without warning — a 30-line stdlib script to check which ones still work

## Overview

Free tiers on LLM APIs are a moving target. A provider that worked last week silently drops to a paid-only plan, rate-limits harder, or deprecates the model you pinned — and the first sign is usually a production failure, not a changelog entry. Instead of finding out from a stack trace, ping every configured endpoint on a schedule and check three things: HTTP status, latency, and whether the response actually contains content. import json , time , urllib . request def check_endpoint ( name , base_url , api_key , model ): t0 = time . time () req = urllib . request . Request ( f " { base_url } /chat/completions " , data = json . dumps ({ " model " : model , " messages " : [{ " role " : " user " , " content " : " ping " }], " max_tokens " : 5 , }). encode (), headers = { " Authorization " : f " Bearer { api_key } " , " Content-Type " : " application/json " }, ) try : with urllib . request . urlopen ( req , timeout = 15 ) as r : data = json . loads ( r . read ()) latency = round ( time . time () - t0 , 2 ) choice = ( data . get ( " choices " ) or [{}])[ 0 ] content = choice . get ( " message " , {}). get ( " content " , "" ) finish = choice . get ( " finish_reason " ) ok = bool ( content . strip ()) return { " name " : name , " ok " : ok , " status " : r . status , " latency_s " : latency , " finish_reason " : finish } except Exception as e : return { " name " : name , " ok " : False , " error " : str ( e )} The trap worth calling out explicitly: a 200 OK with an empty content and finish_reason: "length" . That's not a failure by HTTP status — it's a reasoning model that burned its whole token budget on hidden reasoning tokens and never emitted an answer. If you only check status_code == 200 , this one passes your health check and then fails in production. Run this against every provider in your pool once a day (or before each deploy) and log the result — ok , latency_s , finish_reason . Three runs of silent failure is your signal to fail over, not the 2am page. This stdlib script is the minimum viable version. If you want a maintained, curated list of free-tier LLM providers — which ones are currently genuinely free with no card, their rate limits, and known gotchas like this one — I packaged that research as the Free-LLM Provider Pack .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/renev3408/free-llm-api-tiers-change-without-warning-a-30-line-stdlib-script-to-check-which-ones-still-work-120b

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
