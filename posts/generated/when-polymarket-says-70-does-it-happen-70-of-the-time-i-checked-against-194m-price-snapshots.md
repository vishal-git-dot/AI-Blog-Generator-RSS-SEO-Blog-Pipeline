---
title: "When Polymarket says 70%, does it happen 70% of the time? I checked against 19.4M price snapshots."
slug: "when-polymarket-says-70-does-it-happen-70-of-the-time-i-checked-against-194m-price-snapshots"
author: "manja316"
source: "devto_python"
published: "Tue, 16 Jun 2026 10:51:24 +0000"
description: "If you trade, model, or just read prediction markets, there's one question that decides whether the price means anything: when the market says 70%, does the ..."
keywords: "markets, price, you, market, bin, resolved, calibration, reliability"
generated: "2026-06-16T11:22:59.965839"
---

# When Polymarket says 70%, does it happen 70% of the time? I checked against 19.4M price snapshots.

## Overview

If you trade, model, or just read prediction markets, there's one question that decides whether the price means anything: when the market says 70%, does the thing actually happen about 70% of the time? That's calibration , and it's the single most decision-relevant property of any probabilistic forecaster. A market can be liquid, popular, and heavily traded and still be systematically wrong in a way that's invisible until you score it against what actually resolved. So I built the thing that lets you check it honestly. The dataset Since late March I've been logging Polymarket every 15 minutes. As of this writing the archive holds: 19,413 markets 19,404,618 price snapshots 1,913,420 order-book snapshots 15-minute cadence, 80 days continuous (2026-03-28 → 2026-06-16, ongoing) Each row: market id, timestamp, mid / yes-price, and — for resolved markets — the final 0/1 outcome label That last part is what makes it usable for calibration work specifically. Most "is this forecaster calibrated" questions die on the lack of clean ground-truth labels. Prediction markets hand you the label for free: the market resolves to YES or NO, and you get a hard 0 or 1 to score every prior price against. The measurement (reproducible, ~30 lines) The classic calibration check is a reliability diagram : Take every resolved market. Bin its prices into deciles (0–10%, 10–20%, … 90–100%). For each bin, compute the empirical resolution rate — of all the times the price sat in that bin, how often did the event actually happen? Plot empirical rate vs. stated price. Perfect calibration is the 45° diagonal. Deviation from the diagonal is the miscalibration, in probability units, no modelling assumptions required. import requests , pandas as pd , numpy as np BASE = " https://api.protodex.io " # free, no signup # 1. pull resolved markets + their price history markets = requests . get ( f " { BASE } /markets " , params = { " resolved " : True }). json () rows = [] for m in markets : prices = requests . get ( f " { BASE } /prices " , params = { " market_id " : m [ " id " ]}). json () label = m [ " outcome " ] # 1 if YES resolved, else 0 for p in prices : rows . append (( p [ " yes_price " ], label )) df = pd . DataFrame ( rows , columns = [ " price " , " outcome " ]) # 2. bin into deciles, 3. empirical resolution rate per bin df [ " bin " ] = ( df [ " price " ] * 10 ). clip ( 0 , 9 ). astype ( int ) reliability = df . groupby ( " bin " )[ " outcome " ]. mean () print ( reliability ) # compare each row to its bin's midpoint -> the diagonal That's the whole thing. Bin midpoint on the x-axis, reliability on the y-axis, draw the diagonal, and the gap tells you the story. What to look for (and the trap) The literature on real-money markets has a well-documented signature: the favorite–longshot bias . Longshots (low-probability events) tend to be overpriced — they resolve YES less often than their price implies — and heavy favorites tend to be slightly underpriced . If your reliability curve sags below the diagonal at the low end and rises above it at the high end, that's the fingerprint, and it's the thing to design around if you're trading. But the part I find more interesting than the static curve is the trajectory : calibration as a function of time-to-resolution . Early in a market's life the price is a noisy prior; near resolution it should sharpen. With a 15-minute series you can measure exactly when the Brier score drops and whether the crowd is over- or under-confident at each horizon — which is hard to study without a dense, timestamped, resolution-labeled feed. Honest caveats (this is a benchmark, not a free lunch) Survivorship / selection. Resolved markets ≠ all markets. Conditioning on resolution biases some analyses — this is the part I'm least sure anyone (me included) handles cleanly. Liquidity varies wildly. Thin markets have stale prices. Filter by order-book depth — that's exactly why the order-book snapshots are in the dataset. Mid ≠ executable price. Fees and spread are real. Fine for calibration research; matters the moment you make a trading claim. 80 days is one window, not multiple regimes. Treat any "markets are calibrated" conclusion as provisional, not universal. Get the data The free read-only API is enough to reproduce everything above — no signup: https://api.protodex.io — endpoints /stats , /markets , /market/{id} , /prices , /orderbook , /categories . If you'd rather not page the API market-by-market and just want the full 19M-snapshot history as flat files (parquet/csv) for offline work, the one-time archive is here: Polymarket Full Dataset . The free API reproduces the reliability diagram on its own — the archive just saves you the paging. I'd genuinely like to know how others handle the selection-bias problem on resolved-only markets — that's the open edge of this. If you've used prediction-market data as a calibration or forecasting benchmark, what failure modes did you hit?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/manja316/when-polymarket-says-70-does-it-happen-70-of-the-time-i-checked-against-194m-price-snapshots-3enj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
