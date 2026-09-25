---
title: "Your Trading Bot Assumes the Exchange Will Exist Tomorrow. BitMEX and CoinEx Just Proved Otherwise"
slug: "your-trading-bot-assumes-the-exchange-will-exist-tomorrow-bitmex-and-coinex-just-proved-otherwise"
author: "Nefi Swap"
source: "devto_python"
published: "Fri, 25 Sep 2026 20:48:20 +0000"
description: "In September 2026, two exchanges entered wind-down within days of each other. BitMEX stopped trading on September 23. CoinEx announced on September 15 that i..."
keywords: "exchange, only, amount, your, api, network, not, sweep"
generated: "2026-09-25T21:21:27.483905"
---

# Your Trading Bot Assumes the Exchange Will Exist Tomorrow. BitMEX and CoinEx Just Proved Otherwise

## Overview

In September 2026, two exchanges entered wind-down within days of each other. BitMEX stopped trading on September 23. CoinEx announced on September 15 that it will close on December 22. Both closures are orderly: reserves reported as fully backed, withdrawals open. But if you run bots, treasury scripts, or any integration against an exchange API, an orderly closure is still a sequence of breaking changes, and most codebases don't model it. A wind-down is a state machine Looking at both timelines, closures move through predictable phases: Phase What breaks BitMEX CoinEx Reduce-only New orders rejected; only closes allowed From Aug 26 Futures from Sep 15 Product halts Margin, loans, staking, Earn stop — Sep 22 Trading halt All order placement fails; open positions force-closed Sep 23 Spot ends Sep 29 Deposits disabled Funds sent in are not credited After closure Before final close API withdrawals off Scripted exits stop working Sep 28 — Final close Remaining balances charged fees / moved to custody 1%/yr or $50/mo 5%/mo on unclaimed USDT Each phase is a failure mode your code should recognize, not just "the API returned an error." 1. Stop deposit automation first The most expensive bug in a wind-down isn't a failed withdrawal. It's an automated top-up that keeps sending funds to a deposit address that no longer credits them. Any process that pushes funds to an exchange should check a kill switch before every transfer: import os def deposits_allowed ( exchange_id : str ) -> bool : blocked = os . environ . get ( " DEPOSIT_BLOCKLIST " , "" ). split ( " , " ) return exchange_id not in blocked Flipping one environment variable is faster than finding every cron job that sends funds. 2. Don't retry-loop on reduce-only rejections Once an exchange is in reduce-only mode, order placement returns errors your bot has probably never seen. A naive retry loop will hammer the endpoint, hit rate limits, and potentially get the key restricted, right when you need it for withdrawals. Treat unknown rejection codes as a signal to halt strategy logic and alert a human , not to retry. 3. Sweep by policy, not by panic The real fix is architectural: keep only working capital on any venue, and sweep the rest to self-custody continuously. Then a closure announcement is an inconvenience instead of an emergency. A minimal sweep with ccxt: import os import ccxt exchange_class = getattr ( ccxt , os . environ [ " EXCHANGE_ID " ]) exchange = exchange_class ({ " apiKey " : os . environ [ " API_KEY " ], " secret " : os . environ [ " API_SECRET " ], " enableRateLimit " : True , }) # asset -> (network, env var holding the allowlisted address, amount to keep on the venue) SWEEP_RULES = { " USDT " : ( " TRC20 " , " COLD_USDT_TRC20 " , 500 ), " BTC " : ( " BTC " , " COLD_BTC " , 0.01 ), } def sweep (): exchange . load_markets () balances = exchange . fetch_balance () for asset , ( network , address_env , keep ) in SWEEP_RULES . items (): free = ( balances . get ( asset ) or {}). get ( " free " ) or 0 amount = free - keep if amount <= 0 : continue amount = float ( exchange . currency_to_precision ( asset , amount )) tx = exchange . withdraw ( asset , amount , os . environ [ address_env ], params = { " network " : network }, ) print ( f " Swept { amount } { asset } via { network } : { tx . get ( ' id ' ) } " ) if __name__ == " __main__ " : sweep () Notes before running this anywhere real: Allowlist destination addresses on the exchange side and restrict the API key by IP. A sweep key with withdrawal permissions is a high-value target. Check how the venue deducts withdrawal fees. Some take the fee from the amount, others require amount + fee <= free . Adjust keep accordingly. Network names aren't fully standardized across exchanges, even through ccxt. Verify the exact network identifier per venue. For networks that need a memo/tag, pass the tag argument to withdraw() . 4. Never make the API your only exit BitMEX disabled API withdrawals on September 28, after which withdrawals are manual through the website only. If your treasury operations assume API access, have a documented manual procedure: who has the login, where 2FA lives, and which addresses are pre-approved. 5. Watch announcements, not just uptime Your health checks probably ping endpoints. Wind-downs are announced on blogs and status pages weeks before endpoints change behavior. A cheap monitor that diffs each venue's announcement page and alerts on keywords like "wind-down," "reduce-only," or "cessation" buys you weeks of lead time. 6. Handle the long-tail exit After a trading halt, you can only withdraw assets in the form they're held. CoinEx spot trading ends September 29, and from then on, a long-tail token stays a long-tail token. If your integration holds obscure assets, plan to either convert before the halt or withdraw as-is and convert elsewhere. Disclosure: written by the NefiSwap team. We build an instant exchanger with no accounts and no stored balances, so the question of "where does the money sit, and for how long" is one we think about a lot. NefiSwap supports 8,000+ coins if you need to convert long-tail assets after withdrawing them: nefiswap.com

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nefiswap/your-trading-bot-assumes-the-exchange-will-exist-tomorrow-bitmex-and-coinex-just-proved-otherwise-8bh

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
