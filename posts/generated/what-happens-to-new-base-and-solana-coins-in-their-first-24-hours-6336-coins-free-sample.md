---
title: "What happens to new Base and Solana coins in their first 24 hours (6,336 coins, free sample)"
slug: "what-happens-to-new-base-and-solana-coins-in-their-first-24-hours-6336-coins-free-sample"
author: "CyberWareX"
source: "devto_python"
published: "Fri, 13 Nov 2026 14:07:02 +0000"
description: "We record every new Base and Solana coin our scanner sees, then go back and read its price 1 hour, 6 hours, 24 hours and 7 days later. After five weeks the t..."
keywords: "coins, base, first, you, sample, table, not, chain"
generated: "2026-11-13T14:27:37.206041"
---

# What happens to new Base and Solana coins in their first 24 hours (6,336 coins, free sample)

## Overview

We record every new Base and Solana coin our scanner sees, then go back and read its price 1 hour, 6 hours, 24 hours and 7 days later. After five weeks the table has 6,336 coins, first seen between 2026-10-04 and 2026-11-10. This post shows what the first day looks like, and how to get the rows yourself. A free sample needs no key and no payment. What the first 24 hours look like All numbers below are counted from the rows on 2026-11-10. Returns are measured from the price when our recorder first saw the coin, not from the first block. Base: 2,051 coins, 1,965 with a 24 hour reading 1,866 of 1,965 were down 90% or more after 24 hours 83 were up at all 30 had doubled or better Solana: 4,285 coins, 4,089 with a 24 hour reading 1,538 of 4,089 were down 90% or more after 24 hours 444 were up at all 161 had doubled or better the median coin was down 81% One caution on Base: the table holds the coins our scanner picks up, which may lean toward fast, cheap launches. Treat the Base share as "coins like the ones we see", not "every Base coin". Why keep the dead ones A list built from coins that are still trading leaves out the ones that went to zero, so any average you take over it looks better than reality. Our table keeps every coin, with an empty cell when a reading was not taken, never a zero in its place. That is what makes it usable for questions like "what share of launches with over 50k liquidity survive a day". Get the free sample curl -s https://chain.cyberwarex.com/launch-dataset/sample | python3 -m json.tool | head -40 Each row has: chain, token address, symbol, first seen time (UTC), liquidity and FDV at first sight, return at 1h, 6h, 24h and 7d, the highest of those readings, and a rugged flag. The sample holds the newest coins whose 24 hour reading is already in, plus the whole-table counts. The full table GET https://chain.cyberwarex.com/launch-dataset?days=30 returns up to 60 days of rows as JSON or CSV for 15 USDC on Base, paid with any x402 client. Without payment it answers 402 with the price, so you can see the terms before you pay. A bad request or an empty answer is not charged. No x402 client? https://chain.cyberwarex.com/buy shows an exact USDC amount to send on Base from any wallet; paste the transaction hash and the file downloads. The column notes are here: https://cyberwarex.com/answers/token-launch-outcomes-dataset-base-solana A second table: who keeps buying them We also rank the wallets that trade these coins. In the latest build, the biggest group of Base wallets that buy 5 or more of the same coins within 10 minutes of each other has 113 members, and 111 of them got their first funds from the same address. They bought 15 coins together in the 4.9 days our trade tape covers, and 7 of those coins were later drained. A "smart money" list that does not check funders would show you this farm as 7 separate winners. The free sample of that report is at https://chain.cyberwarex.com/wallet-report/sample Use something else when You need Ethereum mainnet, BNB or another chain. This covers Base and Solana only. You need every coin on a chain. This is what our scanner sees, not a full index. You need tick data or the intraday high. We store readings at fixed times; the highest reading is not the peak. You need history before 2026-10-04. The table starts there.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/cyberwarex/what-happens-to-new-base-and-solana-coins-in-their-first-24-hours-6336-coins-free-sample-21ie

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
