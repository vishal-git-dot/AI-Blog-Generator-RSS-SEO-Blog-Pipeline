---
title: "How late is Form 4 'real-time' data? Measuring filing delay on 11,241 insider filings"
slug: "how-late-is-form-4-real-time-data-measuring-filing-delay-on-11241-insider-filings"
author: "itsRaxzey"
source: "devto_python"
published: "Mon, 24 Aug 2026 01:13:14 +0000"
description: "If you backtest anything involving insider trades, there's a quiet bug waiting for you: Form 4 data is timestamped twice . Every filing carries a transaction..."
keywords: "days, date, filing, transaction, form, not, delay, insider"
generated: "2026-08-24T01:41:15.128032"
---

# How late is Form 4 'real-time' data? Measuring filing delay on 11,241 insider filings

## Overview

If you backtest anything involving insider trades, there's a quiet bug waiting for you: Form 4 data is timestamped twice . Every filing carries a transaction date (when the insider actually traded) and a filing date (when EDGAR disseminated the form). If your backtest joins on the transaction date, you're trading on information that did not exist yet. How big is that gap in practice? I measured it for every Form 4 filed in July 2026 — 11,241 filings — and the answer is: usually 2 days, sometimes 8 years. (Disclosure up front: I run FilingPulse , the SEC filings API this study is built on. This is a methodology piece, not a pitch — the whole thing reproduces on the free tier, and the raw numbers below are what they are regardless of whose API you use.) Method Window: all Form 4s with a filed date in 2026-07-01 … 2026-07-31 (11,052 originals; 189 Form 4/A amendments excluded — an amendment's delay measures the correction, not the original report). For each filing, delay = filed date − earliest transaction date on the form. Holdings-only forms (70) and forms with no dated transaction (31) are excluded; that leaves 10,951 analyzed . Coverage was verified against EDGAR's own daily indexes for all 22 trading days in the window (22/22 exact match) — so "every Form 4 in July" is a checked claim, not a scrape-and-hope. One framing rule I held throughout: a long delay is an observed reporting lag , not a compliance violation. Section 16 has deemed-execution-date rules (10b5-1 plans, small acquisitions, etc.) that legitimately extend the clock, and you cannot adjudicate those from the filing alone. The headline distribution Calendar days from transaction to dissemination: Percentile Delay p50 2 days p75 4 days p90 5 days p95 7 days p99 91 days max 3,140 days (8.6 years) 92.9% of filings landed within the SEC's 2-business-day deadline. The median is well-behaved. The tail is not: 190 filings arrived 11–30 days after the trade, 131 arrived 31–90 days after, and 110 arrived more than 90 days late. That 8.6-year max is a real filing disseminated in July 2026 for a transaction from 2017. The interesting part: delay depends on what the insider did Breaking the same numbers out by transaction code: Code Meaning Legs Within 2 bus. days S Open-market sale 6,694 98.2% D Disposition to issuer 1,163 98.8% M Option exercise 4,552 95.4% A Grant/award 6,897 92.8% F Tax withholding 1,850 93.8% P Open-market purchase 1,198 80.9% J "Other" 822 79.2% Sales are filed on time almost universally — they're usually broker-assisted and the paperwork pipeline is well-oiled. Open-market purchases — the transaction type most insider-trading research cares about most — are the least punctual common code: 1 in 5 arrives after the deadline window. If your strategy keys on insider buys specifically, your look-ahead bias is concentrated exactly where it hurts. What this means for a backtest Join on filing date, not transaction date. The filing date is when the information became public. Using the transaction date leaks 2+ days of future knowledge on the median filing and months on the tail. The tail is not ignorable. ~4% of filings arrive more than 5 calendar days late. In a monthly-rebalance backtest those stragglers silently teleport information backwards across rebalance boundaries. Point-in-time data matters more for purchases than sales. See the table above. Reproduce it The full write-up with charts is here: How late is Form 4 data? — and the study script is a single Python file that runs against a free API key (the since= / until= parameters give you a fixed, reproducible population): params = { " since " : " 2026-07-01 " , " until " : " 2026-07-31 " , " limit " : 100 } # page through /v1/insider-trades, then for each filing: # delay = filed_date - min(leg["transaction_date"] for leg in legs) Script + methodology notes are linked from the study page. If you rerun it for a different month I'd genuinely like to see whether the purchase-vs-sale punctuality gap holds — it's the one result I didn't expect.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/itsraxzey/how-late-is-form-4-real-time-data-measuring-filing-delay-on-11241-insider-filings-2e9j

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
