---
title: "The bug that made my Terraform drift detector cry wolf (and the one-line fix)"
slug: "the-bug-that-made-my-terraform-drift-detector-cry-wolf-and-the-one-line-fix"
author: "ひとし 田畑"
source: "devto_python"
published: "Mon, 15 Jun 2026 12:15:46 +0000"
description: "terraform plan tells you what Terraform changed. It says nothing about the RDS parameter someone tweaked in the console at 2am, or the security group rule ad..."
keywords: "key, new, keys, resource, old, you, drift, diff"
generated: "2026-06-15T12:29:05.501576"
---

# The bug that made my Terraform drift detector cry wolf (and the one-line fix)

## Overview

terraform plan tells you what Terraform changed. It says nothing about the RDS parameter someone tweaked in the console at 2am, or the security group rule added by hand during an incident. To catch that kind of drift, you have to compare your tfstate against what AWS actually returns from the API — yourself. I built exactly that, and the first version was useless. Not because the diff was wrong, but because it screamed about drift on every single resource, every single time. Here's the bug, and why the fix is one line. The naive approach The idea is simple. For each resource you have two dicts: old — the attributes from your tfstate import new — the attributes from a live AWS scan (boto3) Diff them, report the fields that changed: def compute_diff ( old : dict , new : dict ) -> list : changes = [] for key in old . keys () | new . keys (): # union of all keys if old . get ( key ) != new . get ( key ): changes . append ({ " field " : key , " old " : old . get ( key ), " new " : new . get ( key )}) return changes Looks correct. Ship it. Why it cried wolf Every resource came back as massively "drifted" — even ones nobody had touched. The cause is a schema asymmetry between the two sources: A tfstate import stores everything Terraform knows about a resource — 50+ attributes per instance, including provider-internal fields, computed values, timeouts, tags-all, and so on. A live scan only emits the handful of attributes you can reliably and comparably fetch from the AWS API — in my case ~11 carefully chosen keys. So old has 50+ keys, new has ~11. Take the union of keys and every tfstate-only field has new.get(key) == None, which never equals the stored value. Result: ~40 phantom "deletions" on every resource. The signal drowns in noise, and people stop trusting the tool on day one. The fix: compare the intersection, not the union Real drift can only happen on a key that both sides actually report. A field that the live scanner never emits isn't "deleted" — it's simply out of scope for the comparison. So you intersect: def compute_diff ( old : dict , new : dict ) -> list : changes = [] keys = ( set ( old . keys ()) & set ( new . keys ())) - EXCLUDE # intersection for key in sorted ( keys ): ov , nv = old . get ( key ), new . get ( key ) if ov != nv : changes . append ({ " field " : key , " old " : str ( ov ) if ov is not None else "" , " new " : str ( nv ) if nv is not None else "" , }) return changes & instead of |. That's the whole fix. False positives went to zero, and the fields that do differ are now real, every time. "But then you miss added and removed resources" Right — and that's the point. Intersecting keys is the correct tool for attribute-level drift on a resource that exists in both worlds. Detecting whole resources that were added or removed is a different question, and it deserves a different layer. I keep a raw_data_prev snapshot per asset. New resource → no previous snapshot. Removed resource → present before, absent now. That detection lives separately from compute_diff, so each layer stays simple and honest about what it's actually measuring. Trying to make one function answer both questions is exactly how you end up with the cry-wolf bug. One more consistency trap: the dashboard badge that counts "N changed" must use the same diff function, not a raw !=. The first version used raw_data != raw_data_prev for the badge — which is true on every resource thanks to the same schema asymmetry — so the badge counts ballooned while the detail view said "no drift." Use one source of truth for "did this drift?". Don't store secrets in your diffs tfstate is full of plaintext secrets — DB passwords, access keys, tokens. The moment you persist a diff or render it in a UI, you can leak them. Before storing anything, scrub by key name: SECRET_PATTERNS = ( " password " , " secret " , " token " , " private_key " , " access_key " , " credential " , " auth " ) def scrub ( attrs : dict ) -> dict : return { k : " *** " if any ( p in k . lower () for p in SECRET_PATTERNS ) else v for k , v in attrs . items () } Partial match on the lowercased key, applied on both the tfstate and the boto3 side, before the data ever hits the database. Self-hosted or not, your own diff history shouldn't become a secrets store. Takeaways Comparing two data sources? Check whether they share a schema. If not, intersect the keys — a union diff turns missing-by-design into false drift. Keep "attribute changed" and "resource added/removed" as separate layers. Any aggregate count (badges, summaries) must reuse the same diff logic, or it will disagree with the detail view. Scrub secrets before persistence, by key name, on every source. I packaged all of this into a small self-hosted web app — an AWS asset ledger with tfstate-vs-live drift detection and middleware EOL tracking. It's open source (MIT) and runs with one docker compose up: syncvey.com. I'd genuinely like to hear how others handle the added/removed-resource layer — do you snapshot, or diff against a fresh terraform plan?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hitoshi1964/the-bug-that-made-my-terraform-drift-detector-cry-wolf-and-the-one-line-fix-49ai

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
