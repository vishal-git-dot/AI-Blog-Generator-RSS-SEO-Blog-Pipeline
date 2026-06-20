---
title: "How to Download Historical Exchange Rates as CSV with a Free API"
slug: "how-to-download-historical-exchange-rates-as-csv-with-a-free-api"
author: "Jenpo Zhan"
source: "devto_python"
published: "Sat, 20 Jun 2026 09:01:49 +0000"
description: "Developers and spreadsheet users often need historical exchange rates for reporting, bookkeeping, ecommerce reconciliation, or dashboards. The usual workflow..."
keywords: "cny, try, api, fxpeek, url, rates, csv, https"
generated: "2026-06-20T09:27:21.554236"
---

# How to Download Historical Exchange Rates as CSV with a Free API

## Overview

Developers and spreadsheet users often need historical exchange rates for reporting, bookkeeping, ecommerce reconciliation, or dashboards. The usual workflow is awkward: Search a currency converter. Copy a single number. Repeat for many dates. Paste everything into a spreadsheet. This tutorial shows a simpler workflow using FXpeek's free JSON and CSV endpoints. 1. Get The Latest Reference Rate curl 'https://fxpeek.com/api/rates?from=CNY&to=TRY' Example response: { "from" : "CNY" , "to" : "TRY" , "rate" : 6.789 , "timestamp" : 1780576363130 } 2. Get A Historical Series curl 'https://fxpeek.com/api/history?from=CNY&to=TRY&days=365' Use this when you want to build: A chart A dashboard A report A validation script A lightweight finance tool 3. Download CSV For Excel Or Google Sheets curl -L 'https://fxpeek.com/api/csv?from=CNY&to=TRY&days=365' \ -o cny-try-history.csv CSV output: date,base,target,rate 2026-05-28,CNY,TRY,6.7699 2026-05-29,CNY,TRY,6.7811 2026-06-01,CNY,TRY,6.7839 4. Use It In JavaScript async function getHistory ( from , to , days = 365 ) { const url = new URL ( ' https://fxpeek.com/api/history ' ); url . searchParams . set ( ' from ' , from ); url . searchParams . set ( ' to ' , to ); url . searchParams . set ( ' days ' , String ( days )); const res = await fetch ( url ); if ( ! res . ok ) { throw new Error ( `FX API error: ${ res . status } ` ); } return res . json (); } const history = await getHistory ( ' CNY ' , ' TRY ' , 30 ); console . log ( history . rates ); 5. Use It In Python import requests import pandas as pd url = " https://fxpeek.com/api/history " params = { " from " : " CNY " , " to " : " TRY " , " days " : 365 } data = requests . get ( url , params = params , timeout = 20 ). json () df = pd . DataFrame ( data [ " rates " ]) df . to_csv ( " cny-try-history.csv " , index = False ) Notes FXpeek provides reference rates for historical lookup, spreadsheets, reports, and lightweight apps. These are not transaction quotes. API docs: https://fxpeek.com/en/api?utm_source=devto&utm_medium=article&utm_campaign=fxpeek_wave1_api_csv&utm_content=csv_tutorial Example pair page: https://fxpeek.com/en/cny-to-try?utm_source=devto&utm_medium=article&utm_campaign=fxpeek_wave1_api_csv&utm_content=pair_page Good Next Steps Add a date picker. Cache the API result. Build a chart with Recharts or Chart.js. Export monthly averages. Combine rates with ecommerce order data.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jenpo_zhan_aca905ad2a8a5b/how-to-download-historical-exchange-rates-as-csv-with-a-free-api-48gc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
