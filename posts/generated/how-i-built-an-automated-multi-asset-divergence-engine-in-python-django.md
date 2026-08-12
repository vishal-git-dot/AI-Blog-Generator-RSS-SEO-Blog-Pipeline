---
title: "How I Built an Automated Multi-Asset Divergence Engine in Python & Django"
slug: "how-i-built-an-automated-multi-asset-divergence-engine-in-python-django"
author: "Artem"
source: "devto_python"
published: "Wed, 12 Aug 2026 18:42:51 +0000"
description: "Screening 100+ financial assets across multiple timeframes for technical chart anomalies is an impossible task for a human eye. If you want to detect momentu..."
keywords: "divergence, res, indicator, timeframe, trend, atr, price, order"
generated: "2026-08-12T19:08:00.188316"
---

# How I Built an Automated Multi-Asset Divergence Engine in Python & Django

## Overview

Screening 100+ financial assets across multiple timeframes for technical chart anomalies is an impossible task for a human eye. If you want to detect momentum divergence across Forex, Crypto, Metals, and Commodities in real time, you need an automated data pipeline. In this post, I will break down the engineering architecture behind the AEMMtrader automated divergence engine: how we calculate real-time extrema, filter out false signals using Higher-Timeframe (MTF) trend confirmation, and dynamically plot ATR execution levels. System Architecture Overview The system runs on a modern Python/Django backend with Celery background workers managing scheduled websocket/REST market data streams. [ Market Feeds: Crypto / FX / Metals ] │ ▼ [ Celery Worker Queue ] │ ▼ [ Technical Engine: Pandas / NumPy ] ├─ 1. Calculate Oscillators (RSI, Stoch, CCI, MACD, UO) ├─ 2. Peak & Trough Extrema Detection ├─ 3. Multi-Timeframe (MTF) Trend Verification └─ 4. Dynamic Volatility (ATR) Sizing │ ▼ [ PostgreSQL & Redis Cache ] │ ▼ [ Client UI: Django Templates + DataTables + Plotly.js ] 1. The Core Algorithm: Detecting Mathematical Divergence To identify a divergence, the algorithm must find consecutive local peaks (or troughs) in both the price series and the oscillator series, then evaluate their relative slopes. Here is a simplified Python representation using pandas and scipy.signal.argrelextrema: import numpy as np import pandas as pd from scipy.signal import argrelextrema def detect_regular_bearish_divergence ( df , order = 5 ): """ df requires: ' high ' , ' close ' , ' indicator ' (e.g. RSI, Stochastic) order: number of points on each side to use for peak comparison """ # Find local price maxima price_peaks_idx = argrelextrema ( df [ ' high ' ]. values , np . greater , order = order )[ 0 ] # Find local indicator maxima ind_peaks_idx = argrelextrema ( df [ ' indicator ' ]. values , np . greater , order = order )[ 0 ] if len ( price_peaks_idx ) < 2 or len ( ind_peaks_idx ) < 2 : return None # Get the last two structural peaks p_last , p_prev = price_peaks_idx [ - 1 ], price_peaks_idx [ - 2 ] i_last , i_prev = ind_peaks_idx [ - 1 ], ind_peaks_idx [ - 2 ] # Temporal alignment check (ensure peaks correspond to similar candles) if abs ( p_last - i_last ) <= 2 and abs ( p_prev - i_prev ) <= 2 : price_hh = df [ ' high ' ]. iloc [ p_last ] > df [ ' high ' ]. iloc [ p_prev ] ind_lh = df [ ' indicator ' ]. iloc [ i_last ] < df [ ' indicator ' ]. iloc [ i_prev ] if price_hh and ind_lh : return { " type " : " Bearish Divergence " , " price_points " : ( p_prev , p_last ), " ind_points " : ( i_prev , i_last ), " bars_ago " : len ( df ) - 1 - p_last } return None 2. Solving the False-Positive Problem: Multi-Timeframe (MTF) Filtering A common failure mode in quantitative divergence detection is picking tops in strong trending markets. To solve this, our pipeline enforces an MTF Filter: For an M5 / M15 signal, we query the H1 trend direction via an EMA 50/200 structural slope filter. For an H1 signal, we query the D1 trend direction. If a Bearish Divergence occurs while the higher timeframe is in a confirmed downtrend, the state is tagged as Confirmed (Trend Down) and prioritized in the database. You can explore the live implementation of this table directly on the AEMMtrader Divergence Dashboard . 3. Dynamic ATR Execution Engine Instead of outputting raw alerts, the system computes actionable entry, stop-loss, and take-profit targets based on volatility: Stop Loss = Entry Price + ( 1.5 × ATR 14 ​ ) Take Profit = Entry Price − ( 3.0 × ATR 14 ​ ) This enforces a mandatory 1:2 Risk-to-Reward ratio tailored to the current market environment. 4. Client-Side Rendering with Plotly.js When a user clicks "View" in the dashboard, an asynchronous AJAX endpoint returns the OHLC payload, indicator arrays, and calculated divergence coordinates. The client renders an interactive dual-axis chart without page reloading: // Sample snippet rendering the indicator trace with Plotly let traceCandles = { x : res . datetime , open : res . open , high : res . high , low : res . low , close : res . close , type : ' candlestick ' , name : ' Price ' , yaxis : ' y ' }; let traceOscillator = { x : res . datetime , y : res . indicator , type : ' scatter ' , mode : ' lines ' , name : res . oscillator_name , line : { color : ' #8e44ad ' , width : 2 }, yaxis : ' y2 ' }; let layout = { grid : { rows : 2 , columns : 1 , pattern : ' independent ' }, yaxis : { domain : [ 0.3 , 1 ], title : ' Price ' }, yaxis2 : { domain : [ 0 , 0.25 ], title : res . oscillator_name }, xaxis : { rangeslider : { visible : false } } }; Plotly . newPlot ( ' plotlyContainer ' , [ traceCandles , traceOscillator ], layout ); Conclusion & What’s Next By combining mathematical peak detection, higher-timeframe trend verification, and dynamic ATR volatility sizing, we transformed a discretionary charting concept into an automated quant engine. Check out the live platform at AEMMtrader.com or explore the screener directly at AEMMtrader Live Divergences . Have thoughts on refining peak detection algorithms or optimizing multi-timeframe caching in Django? Drop your ideas in the comments below!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/_3f894c66c75105a0ef8/how-i-built-an-automated-multi-asset-divergence-engine-in-python-django-2n8h

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
