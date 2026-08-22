---
title: "Build an Overnight Bug Bounty Recon Pipeline With Python (Step-by-Step)"
slug: "build-an-overnight-bug-bounty-recon-pipeline-with-python-step-by-step"
author: "ULNIT"
source: "devto_python"
published: "Sat, 22 Aug 2026 01:03:26 +0000"
description: "Manual bug bounty recon is a tax on your attention. You open a laptop, run the same five tools against the same scope, stare at output, copy interesting line..."
keywords: "you, scope, kit, stage, pipeline, step, run, program"
generated: "2026-08-22T01:34:35.136934"
---

# Build an Overnight Bug Bounty Recon Pipeline With Python (Step-by-Step)

## Overview

Manual bug bounty recon is a tax on your attention. You open a laptop, run the same five tools against the same scope, stare at output, copy interesting lines into a notes file — and three days later you do it all again, hoping something changed. The hunters who find consistently aren't doing more typing than you. They're running a pipeline that does the typing for them, and they only look at new results. This is a hands-on walkthrough of setting up the Bug Bounty Automation Kit ($15 on LemonSqueezy) — a Python-based recon pipeline I use to sweep program scope overnight and wake up to a short, deduplicated list of things worth investigating. Everything here also runs fine on a Raspberry Pi, which is where mine lives. Step 0: Rules of engagement (don't skip this) Automation makes it easy to touch a lot of infrastructure quickly, so the ethics matter more , not less. Only automate against programs that explicitly permit it (HackerOne, Bugcrowd, Intigriti, and self-hosted programs with written scope). Respect rate limits, exclude out-of-scope assets in your config before the first run, and never point the pipeline at something you don't have written authorization to test. The kit ships with a scope.yaml that forces you to define allow/deny lists before anything runs — that's deliberate. Step 1: Install and layout The kit is plain Python with a requirements.txt — no framework, no database server. State is a directory of JSON files, which means it survives crashes and syncs with git. git clone <kit-repo> && cd bounty-kit python3 -m venv .venv && source .venv/bin/activate pip install -r requirements.txt cp scope.example.yaml scope.yaml # edit this before anything else The directory layout after install: bounty-kit/ ├── scope.yaml # programs, in-scope domains, exclusions ├── stages/ # one script per pipeline stage ├── state/ # seen-before hashes, per-program history ├── reports/ # generated markdown briefs └── run_pipeline.py # orchestrator Step 2: The four stages The pipeline is four scripts, each reading the previous stage's output. You can run them individually, which matters when a program's scope is touchy. Stage 1 — Asset discovery. Passive sources first (crt.sh certificate transparency, Wayback, DNS brute with a small wordlist). The kit merges results and normalizes to a single asset list. Stage 2 — Service scan. A rate-limited port pass over discovered hosts. Defaults are conservative — top 100 ports, 50ms delay — because hammering scope gets you banned. Stage 3 — HTTP probing. This is where it gets interesting. Every live web endpoint gets fingerprinted: status codes, redirects, TLS details, response hashes, and technology signatures. A snippet from the kit's prober: # stages/probe.py (excerpt) async def probe ( url : str , session ) -> dict : async with session . get ( url , timeout = 8 , ssl = False ) as r : body = await r . read () return { " url " : url , " status " : r . status , " hash " : hashlib . sha256 ( body ). hexdigest ()[: 16 ], " server " : r . headers . get ( " Server " , "" ), " title " : extract_title ( body ), " interesting " : score ( body , r . headers ) > THRESHOLD , } The score() function flags the things humans actually care about: debug endpoints, admin panels, verbose error pages, default credentials banners, and misconfigured CORS. Stage 4 — Capture and brief. Headless screenshots for anything new, then a markdown brief per program: what's new since last run, what looks interesting, and direct links. Step 3: Deduplication — the part everyone skips The difference between a pipeline you love and one you abandon in a week is dedup. The kit keeps a hash store per program ( state/<program>.seen.json ). Each run, only new assets, changed response hashes, and new ports make it into your brief. A quiet program produces a two-line report instead of 4,000 lines of déjà vu. Step 4: Schedule it and walk away On the Pi (or any always-on box), a single cron entry does the work: # every night at 02:00 — full pipeline, all configured programs 0 2 * * * cd /home/sean/bounty-kit && .venv/bin/python run_pipeline.py >> state/cron.log 2>&1 The orchestrator checkpoints after every stage, so a crash at stage 3 resumes at stage 3 instead of starting over. That boring reliability is most of what you're paying for in any automation you intend to keep. Step 5: Alerts that don't cry wolf The final piece is a digest hook — mine posts to Telegram. The rule I tuned for: only notify on new + interesting (score above threshold AND not in the seen-store). Everything else waits for the morning brief. My notification rate dropped from dozens per run to one or two per week, and every one was worth reading. What you actually get for $15 The kit includes all four stage scripts, the orchestrator with checkpointing, scope templates for the major platforms, the dedup store, and the Telegram/Slack digest hooks — plus a setup walkthrough. If you want the agent layer on top (LLM triage that reads results and drafts your report skeleton), the $9 AI Agent Toolkit plugs into the same state directory, and everything lives in the agent store . Recon will never write a vulnerability report for you — that part still requires eyes and judgment. But it can absolutely stop eating your evenings. Set the scope, schedule the run, and let the pipeline be bored so you don't have to be.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ulnit/build-an-overnight-bug-bounty-recon-pipeline-with-python-step-by-step-1jk9

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
