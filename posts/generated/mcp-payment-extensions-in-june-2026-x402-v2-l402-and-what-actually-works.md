---
title: "MCP Payment Extensions in June 2026 — x402 v2, L402, and What Actually Works"
slug: "mcp-payment-extensions-in-june-2026-x402-v2-l402-and-what-actually-works"
author: "Rumblingb"
source: "devto_ai"
published: "Fri, 12 Jun 2026 15:23:15 +0000"
description: "Last week, x402 shipped v2. This week, Stripe and Adyen integrated Mastercard's AP4M. Two weeks ago, Base shipped Agent Skills with payment hooks. The MCP pa..."
keywords: "payment, lightning, agent, base, facilitator, you, use, boltz"
generated: "2026-06-12T15:28:32.971613"
---

# MCP Payment Extensions in June 2026 — x402 v2, L402, and What Actually Works

## Overview

Last week, x402 shipped v2. This week, Stripe and Adyen integrated Mastercard's AP4M. Two weeks ago, Base shipped Agent Skills with payment hooks. The MCP payment layer is getting real infrastructure faster than anyone expected. If you're building an agent that needs to pay for APIs, data, or compute, you now have three viable protocols. Here's what each one actually is, what changed in June 2026, and which one to use. x402 v2 — The Coinbase/Base Standard x402 is the payment protocol that uses HTTP 402 "Payment Required" — a status code that sat dormant for 29 years. The idea: an agent hits an API, gets a 402 with machine-readable payment instructions, pays in USDC on Base, and gets access. No human in the loop. What changed in v2 (June 2026): The migration is not a version bump — it's a different npm scope. v1 packages ( x402-express , x402-fetch ) stop at 1.2.0. v2 lives under @x402 : npm rm x402-express x402-fetch npm i @x402/express @x402/fetch @x402/evm @x402/core Three breaking changes that matter: Network identifiers are CAIP-2 now. base-sepolia becomes eip155:84532 . If your env files say base-sepolia , they'll silently break. Payment challenges moved into headers. v1 put them in the JSON body. v2 402 responses have an empty body — the challenge is base64 JSON in the PAYMENT-REQUIRED header. If you parse 402 bodies, your code breaks. Middleware sync required at startup. v2 needs paymentMiddleware to sync supported payment kinds before issuing challenges. Without it, even challenge issuance fails with "Facilitator does not support exact on eip155:84532." Your offline tests now need network access. Trap to avoid: @x402/express has an optional peer dep on @x402/paywall . Don't install it unless you want the browser UI — it pulls wagmi/walletconnect/solana, which adds the exact dependency bloat v2 was designed to eliminate. Who should use x402: Builders deploying on Base, Coinbase Developer Platform users, anyone who wants USDC settlement and doesn't want to run their own payment node. The facilitator at https://x402.org/facilitator handles verification and settlement for you. L402 — The Lightning/Bitcoin Standard L402 came from Lightning Labs in 2020. It's the OG machine-payment protocol, built on Bitcoin's Lightning Network. How it works: Agent pings an API endpoint Server responds 402 + a macaroon (bearer token) + a Lightning invoice Agent pays the invoice via Lightning, gets back a preimage (receipt) Agent pairs macaroon + preimage into an L402 token Agent returns with the L402 → gets access No intermediaries. No facilitator. No USDC. Just Bitcoin Lightning and macaroons. Key difference from x402: L402 uses proof-of-payment baked into the auth token itself. The macaroon + preimage combination is self-verifying — the server doesn't need to call a third-party facilitator to check if payment happened. This is architecturally cleaner but requires you to run Lightning infrastructure. Who should use L402: Bitcoin-native projects, anyone already running Lightning nodes, builders who want fully self-sovereign payment verification with no external facilitator dependency. BoltzPay — The Bridge Boltz isn't a payment protocol per se — it's a non-custodial swap exchange. But in the agent payment stack, it fills a specific gap: converting between chains. An agent that earns in Lightning BTC but needs to pay an x402 endpoint in USDC on Base can route through Boltz. It's the interoperability layer that neither x402 nor L402 solves natively. Who should use Boltz: Agents that operate across chains. Not a primary payment protocol, but essential infrastructure for multi-chain agents. What to Actually Use in June 2026 If you... Use Deploy on Base/CDP x402 v2 ( @x402/express ) Run Bitcoin/Lightning infra L402 (Lightning Labs) Operate multi-chain x402 + Boltz bridge Want zero facilitator dependency L402 Want fastest integration x402 v2 + facilitator The Bigger Picture Three weeks ago, none of this was consolidated. Now x402 has a v2 with clean npm scoping, L402 has years of production use on Lightning, and Boltz bridges them. Combined with Mastercard's AP4M for enterprise settlement and Stripe's agent tokens for traditional rails, the agent payment stack is forming faster than the identity and audit layers. The payment rails are here. The guardrails — audit trails, expense reports, dispute resolution for 400K agents spending $43M — are still missing. That's the next frontier. Sources: FiatDock x402 v2 migration (June 2026), Lightning Labs L402 docs, Coinbase CDP x402 facilitator, Base Agent Skills repo, Boltz exchange docs. AgentPay Labs — Building the payment control plane for autonomous agents.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rumblingb/mcp-payment-extensions-in-june-2026-x402-v2-l402-and-what-actually-works-14jp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
