---
title: "There is no 'fastest free RPC'. We measured 15 providers from 3 regions and the winner changes every time you move."
slug: "there-is-no-fastest-free-rpc-we-measured-15-providers-from-3-regions-and-the-winner-changes-every-time-you-move"
author: "boba bobo"
source: "devto_webdev"
published: "Thu, 02 Jul 2026 14:06:49 +0000"
description: "few months ago we started measuring every free, no-key RPC endpoint we could find: PublicNode, dRPC, 1RPC, Tenderly, Cloudflare, Nodies, Lava, Merkle, MeowRP..."
keywords: "you, chain, provider, your, per, rpc, providers, every"
generated: "2026-07-02T14:15:25.137860"
---

# There is no 'fastest free RPC'. We measured 15 providers from 3 regions and the winner changes every time you move.

## Overview

few months ago we started measuring every free, no-key RPC endpoint we could find: PublicNode, dRPC, 1RPC, Tenderly, Cloudflare, Nodies, Lava, Merkle, MeowRPC, Flashbots, plus the chain-foundation endpoints. One eth_blockNumber POST every 15 seconds, per provider, per chain, from three regions (us-east, eu-west, Singapore), everything recorded into a public Prometheus. The plan was to publish a simple leaderboard: "here is the fastest free RPC, you're welcome." That leaderboard turned out to be impossible to write honestly. Here is why, and what we found instead. Finding 1: the winner changes when you move Same request, same second, three regions. Current p50 over 24h as I write this: Region #1 #2 #3 us-east Binance dataseed (4 ms) Merkle (9.5 ms) PublicNode (11.5 ms) eu-west Tenderly (17.7 ms) PublicNode (18 ms) Binance dataseed (22 ms) Singapore Cloudflare (10 ms) dRPC (13.2 ms) Binance dataseed (72 ms) Three regions, three different winners. A provider that is #1 from Virginia can be 7x slower from Singapore. If your users are global and you hardcode one RPC because a blog post said it was "the fastest", you are shipping someone else's latency profile. The practical takeaway: pick per region, or use a provider that anycasts properly. The full per-chain × per-region matrix is public, so you can look up your own deployment region instead of trusting an aggregate. Finding 2: aggregate rankings quietly lie Notice the Binance dataseed number above. 4 ms p50 from us-east looks incredible — until you know it only serves BNB Chain. Providers that cover one chain well will look faster than providers that answer for ten chains, because their average isn't diluted by the slow chains. We got this wrong in our own first version. The fix was to publish the per-cell matrix (chain × region) and to only rank like-for-like. Any benchmark that shows you a single global number for a multi-chain provider is averaging away exactly the information you need. Finding 3: p50 is marketing, p99 is production Several providers sit in a comfortable 10–30 ms band at p50 and then blow past hundreds of ms at p99. If you build anything latency-sensitive (a bot, a wallet with optimistic UI, an indexer with tight loops), the p99 is what your users feel during the bad minutes. We publish p50/p90/p99 and success rate for every provider, and we never headline means. A provider that fails 30% of requests but is fast on the other 70% does not deserve to look fast. Finding 4: the bot-filter trap The weirdest failure mode we hit: one provider's Ethereum endpoint sits behind an aggressive bot filter that locks you out for ~20 minutes after a single programmatic request. Fine for a human with a browser, catastrophic for anything automated — and invisible on their status page, which stays green the whole time. We now exclude that endpoint from the Ethereum leaderboard and documented why. Status pages tell you what the vendor wants you to see; continuous external measurement tells you what your code will actually experience. Finding 5: "free" tiers are wildly unequal Keyless coverage differs a lot more than the marketing suggests: Some providers serve 10 EVM chains without a key One big-name provider only answers keyless on 2 chains (everything else requires signup) Foundation endpoints (Arbitrum, Base, Optimism, Avalanche) are documented "best-effort" and behave like it — fine for dev, risky for prod If your fallback chain assumes "keyless provider X covers chain Y", verify it. We probe exactly this and publish the support matrix. How the measurement works (and how to attack it) Every number above is a literal PromQL query against a public Prometheus instance. The harnesses are open source (MIT), the specs are YAML, and reproducing a result is docker compose up — your /metrics endpoint emits the same numbers ours does within 30 seconds. Funding disclosure: the project is funded by Mobula, which is itself measured on several benchmarks (and does not always win). The methodology is public precisely so you can check that we are not tipping the scales. If you find a bias, open an issue and we will fix it in the open. Live data, methodology and the full matrix: openchainbench.com/benchmarks/rpc-capabilities If you run infrastructure that talks to a chain and want your provider added (or think our numbers are wrong), the repo is github.com/ChainBench/OpenChainBench . Wrong-but-loud feedback beats polite silence.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/boba_bobo_c54aa2b42146177/there-is-no-fastest-free-rpc-we-measured-15-providers-from-3-regions-and-the-winner-changes-k78

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
