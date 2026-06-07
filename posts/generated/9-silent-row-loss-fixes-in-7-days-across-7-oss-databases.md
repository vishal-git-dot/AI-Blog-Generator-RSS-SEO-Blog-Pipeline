---
title: "9 silent-row-loss fixes in 7 days across 7 OSS databases"
slug: "9-silent-row-loss-fixes-in-7-days-across-7-oss-databases"
author: "sravan27"
source: "devto_webdev"
published: "Sun, 07 Jun 2026 09:00:43 +0000"
description: "A pattern: a JavaScript database re-implements four common SQL operators - upper / lower , length / substr , case-insensitive match, range comparison. The im..."
keywords: "powersync, same, database, length, upper, case, data, open"
generated: "2026-06-07T09:24:56.819776"
---

# 9 silent-row-loss fixes in 7 days across 7 OSS databases

## Overview

A pattern: a JavaScript database re-implements four common SQL operators - upper / lower , length / substr , case-insensitive match, range comparison. The implementation looks right. The tests pass. The CI is green. And then the moment a user's data contains the German ß , a fi ligature, an emoji, a Turkish dotted-i, or a CJK Extension B character, the operator silently returns the wrong rows. No error. No log. Just less data than the user expected, or the wrong data. I've now shipped this exact bug class to seven open-source JavaScript database query layers in seven days. Nine PRs. None of them throw. All of them silently return wrong rows. Here's the streak: PowerSync ( #644 ) - LIKE/range semantics. Merged. Funded a paid 48-hour follow-on sprint. PowerSync ( #645 ) - CAST semantics. Merged. PowerSync ( #646 ) - division by zero. Merged. PowerSync ( #647 ) - json_each over scalar. Merged. PowerSync ( #662 ) - JOIN parsing silently syncs zero rows. Open. PowerSync ( #663 ) - upper/lower ASCII vs Unicode case-fold divergence. Open. PowerSync ( #664 ) - length() UTF-16 code units vs SQLite code points. Open. PowerSync ( #665 ) - substring() splitting surrogate pairs. Open. TanStack DB ( #1574 ) - ASCII case fold in upper/lower/ilike. Open today. Plus earlier same-class fixes in Rocicorp's Zero , InstantDB , ElectricSQL , Dexie , and RxDB . The pattern is always the same shape A JS database re-implements a SQL operator in JavaScript: // PowerSync sync-rules - before const upper = { call ( value ) { return value ?. toUpperCase () ?? null } } // TanStack DB - before case `upper` : return ( data ) => { const value = arg ( data ) return typeof value === `string` ? value . toUpperCase () : value } String.prototype.toUpperCase() is locale-aware and length-changing : input .toUpperCase() SQLite's upper() 'straße' 'STRASSE' (6 -> 7) 'STRAßE' 'ﬁle' 'FILE' (3 -> 4) 'ﬁLE' 'İ'.toLowerCase() 'i̇' (1 -> 2, combining dot above) 'i' 'I'.toLowerCase() (tr-TR) 'ı' 'i' When the JS re-implementation and the source database disagree, the bucket key the client looks up and the bucket key the server wrote silently mismatch. The row doesn't appear on the client. No error fires. Same pattern for length() - JavaScript's String.prototype.length counts UTF-16 code units, SQLite's length() counts code points. They disagree by 2x on every emoji, CJK Extension B-G character, and ancient script glyph. Same for substring() - JS slices on code units and can return unpaired surrogates. Same for case-insensitive LIKE / ilike - same toLowerCase() length-change problem. The fix is always the same shape too Stop calling locale-aware JS string methods on data the database is supposed to be authoritative about. Use ASCII-only case fold loops, iterate by code points ( for...of or [...text] ), and walk surrogate pairs deliberately. It's about 30 lines of JS to catch the four common cases. I packaged it: npm i silentdrop silentdrop is a zero-dependency MIT correctness checker. You wire your query layer's operators ( like , ilike , gt , etc.) and it runs the four divergence classes against them, naming each silent-row-loss it finds. Same lens applied to LLM outputs (missing required fields, enum drift, hallucinated IDs that look syntactically valid, claim-vs-list mismatches): npm i silentdrop-llm What makes this worth the hour to run Every single time I have run silentdrop or its sibling discipline on a new database, I have found a real bug. PowerSync (8), TanStack DB (1 just today), Zero, InstantDB, Electric, Dexie, RxDB. The bug class has 100% hit rate on JS query layers that claim SQL parity. The fix is small. The user impact is real - some user's row, somewhere, has a ß in it, and the row is currently silently missing. If your database/sync layer is correctness-critical and you'd rather have the whole operator surface hardened by hand - same pass as the nine PRs above - I take that on as a fixed 48-hour sprint, no-find-no-charge. $1,000 flat: https://buy.polar.sh/polar_cl_z0eLsPUJeMwrcNs4MQPAQbKIM3Rbdb8fLDgVj2RZcmr . Or smaller scope - one specific operator I find a divergence on, repro + fix + PR delivered - $500: https://buy.polar.sh/polar_cl_G0fuUHHZ1tg9E0oe7gluje9gs44l8FAqVnfwS2AJkbw . Otherwise, npm i silentdrop is free and the first bug it finds will pay you back in the prevented hours of debugging.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sravan27/9-silent-row-loss-fixes-in-7-days-across-7-oss-databases-2nd-draft-56da

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
