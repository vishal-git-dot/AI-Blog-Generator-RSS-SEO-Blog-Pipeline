---
title: "My autonomous agent caught itself publishing fake statistics on its own public pages"
slug: "my-autonomous-agent-caught-itself-publishing-fake-statistics-on-its-own-public-pages"
author: "Florian Demartini"
source: "devto_python"
published: "Wed, 24 Jun 2026 03:49:50 +0000"
description: "My autonomous agent has been running a small French SaaS (BailleurVérif, a rent-compliance checker for tenants) for ~640 cron-driven wakes. Last week it caug..."
keywords: "agent, pages, csv, latest, canonical, itself, own, data"
generated: "2026-06-24T04:04:51.772810"
---

# My autonomous agent caught itself publishing fake statistics on its own public pages

## Overview

My autonomous agent has been running a small French SaaS (BailleurVérif, a rent-compliance checker for tenants) for ~640 cron-driven wakes. Last week it caught itself doing something embarrassing: serving fabricated statistics on its own public data pages. Here is what happened, why it happened, and the cheap discipline that fixed it. The setup The product's moat is an observatoire — a crawler that scrapes French rental listings, scores each against the legal rent cap (encadrement des loyers), and publishes per-city pages: "In Villeurbanne, 57.9% of listings exceed the legal cap, median overage +44%." Those numbers are the whole value proposition. They are also, it turns out, exactly the kind of thing that rots silently. The crawler appends to a cumulative CSV. The city pages, however, were generated once in early June from a frozen snapshot of that CSV and never re-synced. As the CSV grew (dedup by url_hash , keeping the latest score per listing), the published numbers drifted from reality. Nobody noticed because nobody re-derived them. The defect While refreshing pages from the canonical CSV, the agent found genuinely wrong figures live in production: Lyon displayed max +244% . That data point no longer exists after dedup — real max is +192.5% . Bordeaux displayed 76.2% violations. Recomputed from the canonical source: 71.8% — a 21-point overstatement on the "clear violation" rate. Marseille displayed N=36 . The canonical CSV had 92 rows for Marseille. The first diagnosis ("Marseille is absent from the CSV") was also wrong — the filter searched for a commune_slug that's empty for Marseille (it's outside the encadrement zone, so every row is in_scope_encadrement=false , which is legally correct). Two integrity defects in one page. None of these were malicious or even hard to make. They are the default failure mode of any agent that ships derived numbers: the derivation and the display decouple, and entropy does the rest. The fix that actually matters The interesting part isn't recomputing four pages. It's the two rules that stop this from recurring: 1. Re-derive from a single canonical source, reproducibly, before every ship. Not "trust the last generated value." The recompute is deterministic: import csv , collections rows , latest = [], {} with open ( " observatoire-annonces-loyer-cumulative.csv " ) as f : for r in csv . DictReader ( f ): if r [ " commune_slug " ] != " villeurbanne " : continue if r . get ( " in_scope_encadrement " ) != " true " : continue h = r [ " url_hash " ] # keep latest score per listing (dedup) if h not in latest or r [ " ts_score " ] > latest [ h ][ " ts_score " ]: latest [ h ] = r listings = list ( latest . values ()) n = len ( listings ) clear = sum ( 1 for r in listings if float ( r [ " overage_pct " ]) > 0 ) print ( f " N= { n } , clear= { clear } ( { 100 * clear / n : . 1 f } %) " ) Every figure that ships has to come out of a function like this, run at ship time — not a number copied from a previous render. 2. Never correct an integrity defect silently. The agent's reviewer flagged this hard: a multi-page, multi-week accuracy bug on public assets is a founder-FYI event , not a quiet patch. Silent self-correction trains an agent to hide its own errors. So the fix included a transparency note to the human owner enumerating exactly which numbers were wrong and for how long. Then: making the strategy itself falsifiable The deeper lesson was strategic. The agent had spent five consecutive wakes enriching pages on the thesis that "unique local data → escapes Google's near-duplicate filter → more indexed pages." That thesis had produced zero measured feedback . Five wakes of supply-side work against an unverified belief. So instead of a sixth, it turned the belief into an experiment that already exists in production — no new pages required: 13 city pages carry a unique observatoire data block (enriched cohort). 20 city pages are near-duplicate templates with no local data (thin cohort). The metric is Google's own urlInspection.index.inspect.coverageState via the Search Console API. The decision rule is set in advance , with a deadline: T+30d: enriched − thin ≥ +25pts indexed → thesis holds, keep enriching delta < +10pts → thesis falsified, switch channel A natural A/B that costs nothing to run and can actually kill the strategy. The single blocker is one human click to enable an API — which is itself a useful signal about where the real bottleneck in an "autonomous" system lives. Stack Python stdlib ( csv , urllib.request ), a cumulative CSV as the canonical store, cron every 2h driving the agent loop, the Anthropic API for the agent itself, and the Google Search Console / URL Inspection API for the dedup experiment. No framework — the discipline lives in the prompt and in self-binding rules logged to a ledger, not in code. Takeaways If your agent ships derived numbers, re-derive them from one canonical source at ship time. Cached render values drift; the drift is invisible until someone recomputes. Make self-correction loud. An agent that fixes its own integrity bugs silently is an agent learning to hide them. Turn theses into falsifiable experiments with a pre-committed decision rule and deadline — otherwise "build more" masquerades as progress for weeks. 🔗 Code source MIT github.com/Creariax5/bailleurverif · Site bailleurverif.fr · Wikidata Q139857638

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/bailleurverif/my-autonomous-agent-caught-itself-publishing-fake-statistics-on-its-own-public-pages-4aa6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
