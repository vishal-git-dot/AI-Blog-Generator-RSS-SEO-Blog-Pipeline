---
title: "44 days of AI signals as a dataset — and 3 silent API traps I hit publishing it"
slug: "44-days-of-ai-signals-as-a-dataset-and-3-silent-api-traps-i-hit-publishing-it"
author: "John"
source: "devto_webdev"
published: "Wed, 14 Oct 2026 21:14:03 +0000"
description: "I've been collecting AI signals from public sources every day for 44 days. This week I published the whole thing as a machine-readable dataset. Along the way..."
keywords: "your, api, you, one, token, daily, request, file"
generated: "2026-10-14T21:28:09.487505"
---

# 44 days of AI signals as a dataset — and 3 silent API traps I hit publishing it

## Overview

I've been collecting AI signals from public sources every day for 44 days. This week I published the whole thing as a machine-readable dataset. Along the way I hit three failure modes that were completely silent — no error, no log line, just "nothing happens". They're worth knowing if you publish a public API or dataset, because they cost me hours and I'd rather you skip them. What the dataset is 17,397 rows , one row per signal, across 44 daily editions (2026-09-01 → 2026-10-14) Fields: source , board , title , url , summary , org , topics , timestamp , edition_date Sources: GitHub trending, Hugging Face models, YouTube talks, arXiv papers, LMSYS Arena boards, AI news JSONL, CC BY 4.0 (commercial use fine, just credit), refreshed daily https://huggingface.co/datasets/leopardyzzj/ai-signals-daily Trap 1 — Your CDN 403s stdlib clients, and your logs show nothing If your JSON endpoints sit behind Cloudflare, a request with the default Python-urllib/3.x User-Agent (or an empty UA) can get a 403 at the edge . The request never reaches your origin, so your access log is empty and your monitoring is green. The trap isn't the 403 — it's the conclusion you draw from it. You look at your logs, see no traffic, and decide "nobody is using my API." Meanwhile people following the standard-library examples in your docs are getting 403s and assuming your API is broken. Fix: send a real User-Agent. Then document it, because the default behaviour of urllib is exactly the thing being blocked: req = urllib . request . Request ( url ) req . add_header ( " User-Agent " , " my-app/1.0 (+https://example.com) " ) requests , httpx , aiohttp , Go's client, node-fetch , axios , okhttp and curl all pass fine — it's specifically the bare stdlib default that gets filtered. Trap 2 — Hugging Face's per-file upload endpoint is gone (410) I built an uploader against POST /api/datasets/{repo}/upload/main/{filename} . It used to work. Now it returns: HTTP 410: This endpoint is deprecated and has been retired, use the commit endpoint instead. The replacement is the commit endpoint, which takes NDJSON: a header line, then one line per file with base64 content. Small files go inline; anything past the 10MB mark needs LFS. lines = [ json . dumps ({ " key " : " header " , " value " : { " summary " : " daily refresh " }})] for f in files : lines . append ( json . dumps ({ " key " : " file " , " value " : { " path " : f . name , " encoding " : " base64 " , " content " : base64 . b64encode ( f . read_bytes ()). decode (), }})) req = urllib . request . Request ( f " https://huggingface.co/api/datasets/ { repo } /commit/main " , data = ( " \n " . join ( lines ) + " \n " ). encode (), method = " POST " , headers = { " Authorization " : f " Bearer { token } " , " Content-Type " : " application/x-ndjson " }) Trap 3 — Don't hardcode the namespace This one is embarrassing and it's the one that would have wasted the most time. My publisher had owner = "my-org-name" written into it, but the API token I was handed belonged to a different account . The result: the repository got created under the token's account, and every file upload was sent to the other namespace. Every single file returned 403 , and it looks exactly like a flaky network problem. Derive the namespace from the token instead, and verify the token actually has write access before you start a 200-file upload: # GET https://huggingface.co/api/whoami-v2 # -> {"name": "<account>", "auth": {"accessToken": {"role": "write"}}} If that role isn't write , a read-only token will get you authenticated, look fine, and then fail at upload time — which is the worst place to discover it. The common thread All three traps share one property: they fail silently, and the misleading signal arrives in a different place than the failure. A CDN block shows up as "no traffic". A dead endpoint shows up as "403 from the namespace". A read-only token shows up as an authentication error. If you're publishing data or an API, here's the cheap insurance: probe your own surface anonymously, from outside , with the same defaults a stranger would use — and do it after every deploy. Most of my worst bugs were invisible from the inside. The dataset: huggingface.co/datasets/leopardyzzj/ai-signals-daily (CC BY 4.0). There's also a free daily digest (4 signals, one per core source), and if you want the whole archive as JSONL in one go, it's a one-time CA$5: buy.stripe.com/00w28r4W08qq8CcecHgw008 .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/signals_api/44-days-of-ai-signals-as-a-dataset-and-3-silent-api-traps-i-hit-publishing-it-4e3l

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
