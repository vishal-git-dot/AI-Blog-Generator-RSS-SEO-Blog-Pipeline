---
title: "Stop Doing Bug Bounty Recon by Hand: A Practical Tutorial With the Automation Kit"
slug: "stop-doing-bug-bounty-recon-by-hand-a-practical-tutorial-with-the-automation-kit"
author: "ULNIT"
source: "devto_python"
published: "Tue, 25 Aug 2026 01:05:03 +0000"
description: "If you hunt bug bounty targets for more than a week, you'll notice a depressing pattern: the actual hunting is maybe 20% of your time. The other 80% is recon..."
keywords: "you, example, your, step, com, kit, pipeline, list"
generated: "2026-08-25T01:36:16.221107"
---

# Stop Doing Bug Bounty Recon by Hand: A Practical Tutorial With the Automation Kit

## Overview

If you hunt bug bounty targets for more than a week, you'll notice a depressing pattern: the actual hunting is maybe 20% of your time. The other 80% is recon — enumerating subdomains, resolving DNS, probing HTTP, diffing what changed since yesterday. It's tedious, mechanical work, and it's exactly the kind of work a machine should do while you sleep. This is a step-by-step tutorial on turning your recon into an automated pipeline using the Bug Bounty Automation Kit ($15 on LemonSqueezy) . I run it on a Raspberry Pi 5 so it costs nothing but electricity, but everything here works identically on any Linux box or a $5 VPS. The kit is plain Python — you can read every line, modify every stage, and own the whole thing. What you're building A pipeline with four stages that runs on a schedule, every night, without you touching it: Enumerate — collect subdomains from passive sources Resolve — DNS-resolve the full list and dedupe Probe — check which hosts are actually alive over HTTP(S) Diff & report — compare against yesterday's snapshot and flag what's new The golden rule this pipeline encodes: new assets are where the bugs are. Everyone else is testing the same stale endpoints; the subdomain that appeared last Tuesday at 3am has had zero eyeballs on it. Step 1: Install and configure pip install -r requirements.txt cp config.example.yaml config.yaml Edit config.yaml and set your targets. Everything is scoped to your program's allowed scope — the kit refuses to touch anything outside the domains you list, which is a guardrail you'll be grateful for when you're tired: targets : - " *.example.com" # from your program's scope out_of_scope : - " *.staging.example.com" dns_resolvers : [ " 1.1.1.1" , " 8.8.8.8" ] probe_concurrency : 25 notify : telegram Keep concurrency modest. Twenty-five parallel probes is fast enough and won't get your IP reputation toasted or hammer the target into noticing you. Step 2: Enumeration The kit's enumerator pulls from multiple passive sources — certificate transparency logs, archived DNS datasets, wayback-style archives — and merges them into one candidate list. Passive is deliberate: no packets hit the target yet, so there's no noise and nothing to get you flagged. python -m bountikit.enumerate --target example.com --out data/raw_subs.txt On a typical program I see anywhere from a few hundred to a few thousand candidates per target. Don't judge quality at this stage — that's what resolution is for. Step 3: Resolve and dedupe python -m bountikit.resolve --in data/raw_subs.txt --out data/resolved.json The resolver is async and fast, but the interesting part is the state. It keeps a persistent database of every subdomain it has ever seen, with the date first seen and last-seen status. That database is the backbone of the whole system — the diff step reads from it. Anything that fails to resolve gets kept in the DB with a dead flag; subdomains come back to life, and you want history. Step 4: Probe the living python -m bountikit.probe --in data/resolved.json --out data/live.json This hits each resolved host with a plain HTTP(S) HEAD/GET and records status code, title, server header, and content length. The output is the real gold: it's the list of actual attack surface , not DNS trivia. The probe normalizes redirects so a chain of 301s gets recorded as its final destination, which kills a whole class of duplicates. Step 5: Diff and notify This is the stage that makes the pipeline worth owning: python -m bountikit.diff --in data/live.json --notify The diff compares today's live set against the stored snapshot and emits three buckets: new hosts , newly dead hosts , and changed hosts (different status code or title since yesterday). The report goes to Telegram — or wherever you've pointed it — looking something like this: NEW (3): api-v2.internal.example.com 200 "API Gateway" dev-portal.example.com 401 status.example.com 302 -> statuspage.io DEAD (1): promo.example.com (was 200) CHANGED (2): admin.example.com 200->500, ... That api-v2.internal.example.com that showed up overnight? That's your morning. Step 6: Schedule it The whole thing collapses into one cron entry on the Pi: 0 2 * * * cd /home/pi/bountikit && ./run_nightly.sh >> logs/$(date +\%F).log 2>&1 run_nightly.sh just chains the four commands and exits non-zero if any stage fails, so a broken pipeline shows up as a missing morning report instead of silent failure. Rules that keep you out of trouble A pipeline that runs unattended needs discipline baked in: Stay inside program scope. The config's scope list is enforced, not decorative. Respect it. Throttle. Rate limits on enumeration sources and probe concurrency are set conservatively in the defaults; leave them. Passive first, active second. The kit enumerates passively; only probing touches the target, and politely. Log everything. When you submit a report, being able to show exactly when you found the asset is useful. The takeaway Recon automation isn't about doing more work — it's about relocating the boring 80% to a $35 computer that never gets bored. You wake up to a short list of things that changed, and you spend your actual attention on the part that requires a human: figuring out what's exploitable. The full Bug Bounty Automation Kit is $15 on LemonSqueezy and it's the same pipeline described here, fully commented, with the notifier and state database included. If you'd rather build your own, this tutorial gives you the architecture — but at that price, reading the kit's source is a faster education. Either way, stop doing recon by hand.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ulnit/stop-doing-bug-bounty-recon-by-hand-a-practical-tutorial-with-the-automation-kit-1aj8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
