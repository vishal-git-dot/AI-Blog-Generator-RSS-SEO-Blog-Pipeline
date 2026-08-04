---
title: "An AI agent with $0 just deployed its own token — signed by its own wallet"
slug: "an-ai-agent-with-0-just-deployed-its-own-token-signed-by-its-own-wallet"
author: "Broke to Built"
source: "devto_ai"
published: "Tue, 04 Aug 2026 03:11:34 +0000"
description: "I run a standing experiment called ZERO : an autonomous agent (a free-tier GLM model wrapped in a Cloudflare Worker) that was born with a self-created wallet..."
keywords: "agent, zero, own, its, wallet, gas, coin, you"
generated: "2026-08-04T03:13:25.005593"
---

# An AI agent with $0 just deployed its own token — signed by its own wallet

## Overview

I run a standing experiment called ZERO : an autonomous agent (a free-tier GLM model wrapped in a Cloudflare Worker) that was born with a self-created wallet holding exactly nothing, and one mission — earn real crypto from zero, with no human hands, no faucets, no KYC, and write down how, so it can always climb back from broke. It has been running for a week. Yesterday it crossed a line I didn't expect this soon: it deployed its own token, with its own wallet, and now sells it from its own storefront. How a broke agent transacts at all The interesting engineering was never the model — it's the money plumbing. A wallet with $0 can't pay gas, so ZERO's whole existence depends on finding infrastructure someone else subsidizes: Safe's public relayer sponsors gas on Base/Arbitrum/Optimism/Gnosis — keyless, no signup, 5 txs/day/chain. That's how ZERO executed its first transaction at a $0 balance. ERC-4337 token paymasters (Candide's is keyless) let an account pay gas in USDC instead of ETH — measured cost 0.009087 USDC per operation. x402 — the HTTP 402 payment protocol — has the property that the buyer settles on-chain and pays gas. A seller only has to answer HTTP with a challenge. So a broke agent can sell before it can even move money. Its first earnings were keeper crumbs: calling harvest() on vault strategies that pay whoever triggers them. Measured average: $0.0038 per harvest. A hard law it learned this week: those only profit on sponsored gas — we measured 883k–4.3M gas per harvest, so self-funding them is net-negative. The subsidy is the margin. The token Zora's coin factory on Base is permissionless — you don't need their site, just the contract. ZERO's wallet called ZoraFactory.deploy(...) directly (2.24M gas, about five cents) and minted ZERO , an ERC-20 content coin with a Uniswap v4 pool, where every creator-reward field points back at the agent's own wallet . Anyone trades it, the agent earns the fees. Passive, permanent, zero marginal effort. The metadata is served from the agent's own Worker ( /coin.json ) — turns out Zora's indexer happily accepts an https tokenURI, no IPFS pinning needed. Coin: zora.co/coin/base:0xa08c…661c The storefront ZERO's Worker answers HTTP 402 with x402 payment challenges. The catalogue ( /.well-known/x402 ) sells what the agent built for itself: payout-oracle ($0.03) — simulates whether any contract would pay you for calling it right now (a Multicall3 [balance, call, balance] sandwich — the delta is the caller fee). Reward getters lie; simulated settlement doesn't. interface-xray ($0.04) — recovers the complete external interface of unverified contracts from bytecode PUSH4 selectors, then prices every function. contract-audit ($0.05), wallet-brief ($0.02) — LLM reports grounded in verified source / on-chain facts. and now buy-zero ($1.00) — 250,000 ZERO from the agent's creator supply, delivered on-chain by the agent's own signature the moment payment verifies. Full disclosure baked into the listing: the fixed price is above the (thin) pool price; you're funding the experiment and buying a piece of the story, not an investment. Everything is public — the agent keeps a live journal, ledger, and status page at zero-agent.broke2built.workers.dev . Lifetime on-chain earnings so far: a few cents, every one of them measured and logged. The experiment's bet is that streams stack: keeper crumbs + storefront sales + coin fees, each layer funding the next. If you've built something in the agent-payments space (x402 clients, agent-to-agent commerce), I'd genuinely like to hear what broke when you tried it — the protocol survives contact with reality far better than I expected, but the demand side is still the frontier. Disclosure: ZERO runs on GLM's free tier; if you want the paid coding plan, this referral link funds the experiment's compute. The buy-zero listing is exactly what it says: an above-market OTC tranche that funds an autonomous-agent experiment.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/broke2builtai/an-ai-agent-with-0-just-deployed-its-own-token-signed-by-its-own-wallet-48e

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
