---
title: "Check every incoming USDT (TRC-20) deposit for freeze risk in 20 lines of Python"
slug: "check-every-incoming-usdt-trc-20-deposit-for-freeze-risk-in-20-lines-of-python"
author: "FreezeCheck"
source: "devto_python"
published: "Wed, 18 Nov 2026 15:11:59 +0000"
description: "Disclosure: I work on FreezeCheck, the service used in the examples. The trial key is free; the code works with any HTTP client. If your business receives US..."
keywords: "check, api, key, address, res, your, code, you"
generated: "2026-11-18T15:25:47.038654"
---

# Check every incoming USDT (TRC-20) deposit for freeze risk in 20 lines of Python

## Overview

Disclosure: I work on FreezeCheck, the service used in the examples. The trial key is free; the code works with any HTTP client. If your business receives USDT on TRON — an exchanger, an OTC desk, a payment gateway, a P2P merchant — there is one failure mode that costs real money: you accept a deposit, and a few days later Tether freezes the wallet that paid you, or the wallet you passed the funds to. Tether's blacklist only tells you about addresses that are already frozen. The useful question is earlier: where did this money come from, and how likely is this wallet to be frozen? This post shows how to put that check in front of every deposit with a small HTTP API, in about 20 lines of Python, and how to try it on your own recent deposits first without writing any code. The decision your code needs A risk API is only useful if your code can act on it without a human reading a report. Each answer carries one field for that, action : action verdict what to do accept 🟢 credit automatically review 🟡 or ⚪ show to a manager with the reasons hold 🔴 don't credit, hold the funds Everything else in the answer (score 0–100, reasons with stable codes, a link to the full report with the graph of links) is there for the human who reviews. Step 0: try it on a list, no code Before integrating anything, it is worth seeing how the verdicts look on your traffic. The API console gives a trial key at once (100 checks a day for 20 days). Paste a column of addresses from Excel or upload a CSV of your last deposits — up to 500 — and you get a table of accept / review / hold with the main reasons, exportable back to Excel. Step 1: one address import requests KEY = "fc_YOUR_KEY" API = "https://freezecheck.org/api/v1" def check ( address : str ) -> dict : r = requests . get ( f "{API}/check" , params = { "address" : address , "lang" : "en" } , headers = { "Authorization" : f "Bearer {KEY}" } , timeout = 180 , # a new, very large wallet can take up to two minutes ) r . raise_for_status ( ) return r . json ( ) res = check ( "TP36EX4Ht88mjvTKeRvt3FS9n7Auri5Xym" ) print ( res [ "action" ] , res [ "score" ] , res [ "title" ] ) for s in res [ "signals" ] [ : 3 ] : print ( " -" , s [ "text" ] ) The address above was frozen by Tether on 17 November, so the answer is hold . A typical new check takes 5–15 seconds; a repeat check of the same address comes from cache at once. Step 2: check the sender of a transaction Often you have a transaction hash, not an address. Pass tx= instead and the API checks the sender of the largest USDT transfer in it, and returns the transfer details next to the verdict: r = requests . get ( f "{API}/check" , params = { "tx" : tx_hash } , headers = { "Authorization" : f "Bearer {KEY}" } , timeout = 180 , ) res = r . json ( ) print ( res [ "tx" ] [ "from" ] , res [ "tx" ] [ "amount" ] , res [ "action" ] ) Step 3: a batch of payouts For payouts, split a batch into "pay now" and "hold for review" in one call (up to 50 addresses): r = requests . post ( f "{API}/batch" , json = { "addresses" : payout_addresses , "lang" : "en" } , headers = { "Authorization" : f "Bearer {KEY}" } , timeout = 600 , ) pay_now = [ x [ "address" ] for x in r . json ( ) [ "results" ] if x . get ( "action" ) == "accept" ] Each item has the same fields as a single check, or an error for that address. Errors worth handling 401 no_key / bad_key — header missing or key revoked. 429 quota — daily limit used up; resets_at says when. 429 busy — too many new checks at once for this key; retry in a few seconds. 503 slow / source_down — the blockchain source didn't answer; retry in a minute. A safe default: on any error, route the deposit to review rather than accept . How good is the verdict? We publish the test sets. On a blind test of Tether's October freezes, 82% of the wallets that had any history were flagged 🟡 or 🔴 in advance (101 of 123). On ordinary exchange customers, 91% get 🟢 and 1% get 🔴. The method and the CSVs are in the methodology . The verdict is a heuristic risk estimate, not a legal AML opinion. Links API console (trial key, list check, code): https://freezecheck.org/api-pult.html?lang=en&ref=devto Full API docs: https://freezecheck.org/developers.html The same check as a Telegram bot for your team's chat: https://t.me/freezecheck_bot?start=devto_api Questions: hello@freezecheck.org or Telegram @freezecheck_support.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/freezecheck/check-every-incoming-usdt-trc-20-deposit-for-freeze-risk-in-20-lines-of-python-308b

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
