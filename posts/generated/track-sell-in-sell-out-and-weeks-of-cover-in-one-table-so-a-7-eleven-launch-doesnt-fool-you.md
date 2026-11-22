---
title: "Track Sell-In, Sell-Out and Weeks of Cover in One Table So a 7-Eleven Launch Doesn't Fool You"
slug: "track-sell-in-sell-out-and-weeks-of-cover-in-one-table-so-a-7-eleven-launch-doesnt-fool-you"
author: "Flowup Insights Team"
source: "devto_python"
published: "Sun, 22 Nov 2026 19:04:23 +0000"
description: "Shipments are the number brands see first, and in the weeks after a 7-Eleven (7-11) listing they usually look great. Distribution is being filled and stores ..."
keywords: "sell, week, out, stock, weeks, distributor, cover, only"
generated: "2026-11-22T19:16:57.013404"
---

# Track Sell-In, Sell-Out and Weeks of Cover in One Table So a 7-Eleven Launch Doesn't Fool You

## Overview

Shipments are the number brands see first, and in the weeks after a 7-Eleven (7-11) listing they usually look great. Distribution is being filled and stores are taking their opening stock. If you read only that number, you can spend a month believing a product is selling when shoppers have barely started. The fix is simple to describe: put what was shipped in (sell-in) next to what shoppers bought (sell-out), and derive how many weeks of stock are sitting in the system. The concepts are explained here: https://www.flowupth.com/en/insights/sell-in-vs-sell-out?utm_source=devto&utm_campaign=P500 This post is the table and a few lines of code to keep it honest. The grain One row per SKU per week. Weekly is a compromise: daily is noisy and hard to get, monthly hides turning points. If your distributor can only give monthly store sales, keep the same structure with months and accept that flags will be slower. The columns Column Meaning Source week ISO week start – sku your unit code master sheet sell_in units shipped into the retailer's network distributor shipment report sell_out units sold to shoppers whatever store sales data the distributor receives stores_in_stock stores with stock that week distributor, if available stock_end estimated units in the network at week end derived woc weeks of cover derived Record the source and frequency of sell_out next to the table. Store data that arrives late or is partial changes how much weight the flags deserve. Deriving stock and weeks of cover If you don't receive a stock figure directly, estimate it from a known opening point: stock_end[t] = stock_end[t-1] + sell_in[t] - sell_out[t] - returns[t] Then weeks of cover uses a trailing average of sell-out, not one week, to avoid overreacting: woc[t] = stock_end[t] / mean(sell_out[t-3 .. t]) The derived stock will drift if returns or write-offs are missing, so reset it whenever the distributor gives you an actual stock count. The script import pandas as pd df = pd . read_csv ( "weekly.csv" , parse_dates = [ "week" ] ) . sort_values ( [ "sku" , "week" ] ) df [ "returns" ] = df . get ( "returns" , 0 ) def add_cover ( g , opening_stock = 0 ) : g = g . copy ( ) g [ "stock_end" ] = opening_stock + ( g . sell_in - g . sell_out - g . returns ) . cumsum ( ) g [ "avg_out_4w" ] = g . sell_out . rolling ( 4 , min_periods = 2 ) . mean ( ) g [ "woc" ] = g . stock_end / g . avg_out_4w return g df = df . groupby ( "sku" , group_keys = False ) . apply ( add_cover ) The flags Thresholds are yours to set; there is no published standard for convenience retail, and the right level depends on shelf life and delivery rhythm. Pick values with your distributor and write them down so the flags mean the same thing every month. WOC_HIGH = 8 # example threshold only WOC_LOW = 1.5 # example threshold only df [ "flag_piling" ] = ( df . woc > WOC_HIGH ) & ( df . sell_in . rolling ( 4 ) . sum ( ) > df . sell_out . rolling ( 4 ) . sum ( ) ) df [ "flag_tight" ] = df . woc < WOC_LOW df [ "flag_launch_fill" ] = df . groupby ( "sku" ) . cumcount ( ) < 4 # early weeks: read with care How to read them: flag_launch_fill – early weeks after listing. High sell-in and modest sell-out is expected; don't celebrate or panic yet. flag_piling – shipments keep outrunning shopper purchases and cover is high. Stock is building somewhere. Find out why before cutting price. flag_tight – cover is low. If stores_in_stock is also falling, sell-out is probably being capped by empty shelves, not by demand. A worked pattern (example only) Made-up numbers for one SKU, to show the shape rather than a benchmark: week sell_in sell_out stock_end woc 1 4,000 600 3,400 – 2 1,500 700 4,200 6.5 3 800 650 4,350 6.7 4 900 500 4,750 7.8 5 1,000 450 5,300 9.2 Shipments look healthy every week. Sell-out has turned down since week 2, and cover is rising past the example threshold. On a shipments-only dashboard this SKU looks fine until the distributor stops ordering. Where it fits Run the table weekly and bring only the flagged rows to the monthly distributor review. It turns "sales are good" into a shared view of what shoppers actually took. In our work at Flowup Thailand (flowupth.com) it is also how we decide where TikTok content should run: areas with stock and falling sell-out need demand, areas with tight cover need supply first. Limits What sell-out data a distributor receives differs by contract and category, so some columns may stay empty. The table is a reading aid, not a rule; real weeks often mix situations, and returns or clearance discounts should be logged so the derived stock stays credible.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/flowupth/track-sell-in-sell-out-and-weeks-of-cover-in-one-table-so-a-7-eleven-launch-doesnt-fool-you-4j6g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
