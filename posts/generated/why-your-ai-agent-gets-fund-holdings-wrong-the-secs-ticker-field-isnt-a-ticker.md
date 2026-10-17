---
title: "Why your AI agent gets fund holdings wrong: the SEC's "Ticker" field isn't a ticker"
slug: "why-your-ai-agent-gets-fund-holdings-wrong-the-secs-ticker-field-isnt-a-ticker"
author: "Alex B"
source: "devto_python"
published: "Sat, 17 Oct 2026 14:58:25 +0000"
description: "If you are building an agent or a model on SEC fund-holdings data, it will read a field called IDENTIFIER_TICKER and trust it. Here is what that field actual..."
keywords: "ticker, field, sec, data, port, you, what, rows"
generated: "2026-10-17T15:18:37.847156"
---

# Why your AI agent gets fund holdings wrong: the SEC's "Ticker" field isn't a ticker

## Overview

If you are building an agent or a model on SEC fund-holdings data, it will read a field called IDENTIFIER_TICKER and trust it. Here is what that field actually contains. If you build fund-ownership data from SEC Form N-PORT, you will read a field called IDENTIFIER_TICKER and treat it as a stock symbol. The SEC's data-set documentation describes it in one word: "Ticker". The form itself says more. Form N-PORT, Item C.1.e, asks for "at least one" other identifier: an ISIN, or a "Ticker (if ISIN is not available)", or some other identifier. Nothing requires the ticker to be an exchange symbol. It is a fallback. So we measured what funds actually put there - every quarter the SEC has published, 2019 Q4 to 2026 Q2: 17,361,050 rows carry a ticker. 72% are on common-stock lines, and they look like real tickers: MSFT, AMZN, AAPL. On mortgage-backed lines (676,336 rows) the "tickers" are agency pool-type prefixes: FN 161,550 rows, GN 109,156, FNMA 55,140, FHLMC 45,223. On bond lines (2,312,102 rows) the ticker is the ISSUER's stock symbol, not the bond's: AT&T bonds carry "T" on 86,298 rows. On derivative lines you find futures contract codes (TYZ2, ESZ2) and currency codes (USD, EUR). Why it matters: FG is a Freddie Mac pool prefix. It is also the NYSE ticker of F&G Annuities & Life. Join N-PORT's ticker field to a ticker list and Freddie Mac mortgage pools turn into holdings of an insurance company. Bond holdings turn into stock holdings. Ownership counts, "smart money" signals and flow features all inherit it - silently. Two more traps in the same files: Placeholders that look like data: ISSUER_CUSIP is "N/A" on 47.5 million rows, "000000000" on 15.2 million and "999999999" on 210 thousand. ISSUER_LEI is "N/A" on 67.6 million. Count those as filled and your coverage numbers are wrong. The SEC's machine-readable field list ships unchanged with every historical quarter, so a field "defined" there may not exist in older files (the VaR table is listed back to 2019 but only appears from 2022 Q1). What to do: before trusting any identifier on an N-PORT line, check what kind of holding the line is (the ASSET_CAT field), and treat placeholder values as blank. What I don't know yet: Whether anyone publishes an open mapping from N-PORT pool prefixes (FN, GN, FG...) to the agency programs they stand for. I could not find one. How much of the bond-line "issuer ticker" habit comes from filers themselves and how much from the software vendors that prepare their filings. We published the full N-PORT field dictionary - the SEC's definitions with citations, the official code lists, and what is actually in each field - free, under CC BY 4.0: https://alexbocio.github.io/us-gov-data-dictionary/sec_nport.html Source data: SEC Form N-PORT data sets, 2019 Q4 - 2026 Q2. If you build fund-ownership data from N-PORT: how do you handle the non-stock lines today - map them, or drop them? And if someone has already solved this better, link it in the comments and I'll credit it in the dictionary.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/alexbsolodev/why-your-ai-agent-gets-fund-holdings-wrong-the-secs-ticker-field-isnt-a-ticker-7a4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
