---
title: "I Built a SEC Disclosure-Risk Audit Tool — Here's What It Found on a Real Ticker (SNBR)"
slug: "i-built-a-sec-disclosure-risk-audit-tool-heres-what-it-found-on-a-real-ticker-snbr"
author: "Jared Ablon"
source: "devto_python"
published: "Sun, 28 Jun 2026 03:53:30 +0000"
description: "I Built a SEC Disclosure-Risk Audit Tool — Here's What It Found on a Real Ticker (SNBR) I've been building FilingFirehose for the past few months — a tool th..."
keywords: "audit, item, risk, what, snbr, you, disclosure, every"
generated: "2026-06-28T04:20:44.691465"
---

# I Built a SEC Disclosure-Risk Audit Tool — Here's What It Found on a Real Ticker (SNBR)

## Overview

I Built a SEC Disclosure-Risk Audit Tool — Here's What It Found on a Real Ticker (SNBR) I've been building FilingFirehose for the past few months — a tool that ingests every SEC 8-K, 10-K, 10-Q, S-3, and 13D filing in real time and scores each issuer for disclosure risk. This week I shipped the first end-to-end "audit" deliverable: a 12-page forensic write-up on a single ticker, with every red flag traced back to a specific EDGAR accession number. I want to walk through the actual audit it generated on Sleep Number Corp (SNBR) — a real, mid-cap, publicly traded company — because the patterns it surfaced are a useful illustration of what's hiding in plain sight in routine 8-K cadence. The full sample is public: https://filingfirehose.com/audit/sample/SNBR The TL;DR The system pulled SNBR's last four quarters of SEC filings, ran them through a red-flag taxonomy I built (bankruptcy proximity, delisting notices, dilution proximity, restatement risk, officer departure clustering, cyber-incident disclosure, going-concern language, activist 13D filings), and produced this: SNBR — ELEVATED risk band. 7 distinct signals across an 8-K cluster filed late May through mid-June 2026. Trajectory: worsening. The interesting part isn't the score. It's the pattern it caught — one that any short-side analyst would also catch within 10 minutes of looking, but that most retail traders and even some IROs miss. The Pattern Three things happened in a 21-day window: May 27, June 2, June 10 — three consecutive 8-K filings each carrying Item 5.02 (officer/director events). Short-side desks treat clustered 5.02s as a "departure cluster" regardless of the stated reason. June 12 — a single 8-K carrying Items 1.01, 1.03, 2.04, 7.01, and 9.01. The presence of Item 1.03 (bankruptcy / receivership) alongside Item 2.04 (triggering events accelerating a financial obligation) is one of the highest-signal item-mixes in the 8-K vocabulary. It rarely shows up benignly. June 17 — a standalone Item 3.01 filing. Item 3.01 is the notice category used for "notification of delisting or failure to satisfy a continued listing rule." Standalone 3.01s are uncommon and are the first item outside readers scan for. Taken individually, none of these necessarily means anything bad. Taken as a sequence — 5.02 cluster → embedded 1.03 with 2.04 → standalone 3.01 — they form a single narrative that an experienced short-side reader will instantly assemble. That's what the audit does: it does the assembly for you, names the narrative, cites each filing, and tells you what an outside reader is seeing. How the System Works (high level) This is the open-source-ish stack I'm running on Fly.io: EDGAR full-text feed (polled every 60s) ↓ Parquet store of every filing back to 2023 ↓ Taxonomy classifier (8-K item parsing + buried_json extraction) ↓ Per-ticker risk-signal aggregator ↓ Claude Opus prompt with the signal list + full context ↓ Structured JSON → HTML PDF + Loom-style narration script A few decisions I made that worked out: Pre-compute risk scores nightly instead of computing on request. Stripping parquet scans out of the request handler took the p99 response time from 3s to 8ms. Lesson: never do heavy compute in a web request, even if you "wrap it in a thread with a timeout." I tried that and it took the production app down for 45 minutes one afternoon. Cite every claim to an EDGAR accession number. An audit that says "we found dilution risk" is useless. An audit that says "see accession 0000950103-26-008891, Item 7.01, where the company filed an Item 1.03 reference embedded in a Regulation FD disclosure" is forensically defensible. Every red flag in the deliverable links to the source filing. Trust the LLM for synthesis, not for fact-extraction. The accession numbers, item codes, and dates come from a deterministic parser. The LLM is only used to assemble the narrative. This avoids the "the AI made up a filing" failure mode that kills credibility instantly. What the Free Tool Does If you want to try the underlying scoring engine on any US ticker — no signup, no email — it's at filingfirehose.com/forensic . Type a ticker, hit go, get a score band + breakdown in about 800ms. The full audit deliverable (12-page PDF + every accession cited + executive summary + outside-reader interpretation) is a one-time $497 product for IROs, CFOs, and audit committees who want to know what an outside analyst is seeing in their filings before the outside analyst writes the article. It's at filingfirehose.com/audit if you want to see the landing — or just read the SNBR sample to see what one looks like in the real world. What I'd Build Next Two things on the roadmap: Sector-comparative scoring — instead of an absolute score, show "you're in the 87th percentile of disclosure risk among small-cap consumer goods companies." Context beats absolutes. Earnings-call language drift detection — pair the 8-K signal stream with transcript embeddings, surface when management's framing diverges from the filing language. This is where short-sellers actually find alpha. If you build forensic analysis tools or run a small-cap research desk, would genuinely love to hear what signals you key on that I should add to the taxonomy. Reply here or hit me at jared@filingfirehose.com . The SNBR audit is real and public. Nothing in this post is investment advice. The "ELEVATED risk band" is a disclosure-language read on routine SEC filings, not a financial conclusion or a recommendation to short the stock.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jared_ablon_f27e6e2896913/i-built-a-sec-disclosure-risk-audit-tool-heres-what-it-found-on-a-real-ticker-snbr-24c7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
