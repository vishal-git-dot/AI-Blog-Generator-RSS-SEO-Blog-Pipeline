---
title: "The limit you configured is not the limit it applies"
slug: "the-limit-you-configured-is-not-the-limit-it-applies"
author: "Cleiton Augusto Correa Bezerra"
source: "devto_ai"
published: "Tue, 10 Nov 2026 22:45:46 +0000"
description: "An agent that pays for things needs a limit: a maximum price per call, a payee you expect, sometimes a list of networks and tokens you trust. The question he..."
keywords: "not, limit, agent, quote, what, you, payee, one"
generated: "2026-11-10T23:03:02.012079"
---

# The limit you configured is not the limit it applies

## Overview

An agent that pays for things needs a limit: a maximum price per call, a payee you expect, sometimes a list of networks and tokens you trust. The question here is narrower and more important than whether the limit exists: does it apply to the payment the client signs, or to a quote the agent saw a moment earlier? Those can be different payments. Two requests, two prices x402 turns HTTP 402 into a payment step. The server answers 402 Payment Required with what it wants — amount, payee, asset, network — the client signs a matching authorization, and retries. A common agent flow splits this in two. First the agent makes the request and reads the 402: "0.10 USDC to 0x1111". It decides that is acceptable. Then it calls the paying action, passing the option it chose. If that action sends a new request and signs whatever the new 402 asks for, the check and the payment are about different things. The server can quote 0.10 and then ask for 0.90, or change the payee, or switch the network. This is the oldest problem in signing: what you see is not what you sign. Hardware wallets fixed it for transactions with clear signing. Card payments in Europe fixed it with PSD2's dynamic linking, which ties the authentication to the amount and payee shown to the payer. Agent payments are rediscovering it. A test anyone can run I wrote a small harness ( github.com/cleitonaugusto/x402-conformance ) that plays a dishonest x402 seller on 127.0.0.1 . It quotes one thing on the first 402 and asks for something else on every later one, then decodes what the client actually signed. There is no chain, no facilitator and no money; outbound connections other than loopback are blocked and logged. Each SDK gets an adapter that drives it the way an agent would, with a configured limit of 0.50 USDC. Seven scenarios: an honest quote; the price raised to 0.90; the payee swapped; both; the asset swapped; the network swapped; and a quote already above the limit. Results Run against the current public code of three agent payment SDKs: SDK Signed something other than the quote vAPI Network core 0.12.0 0 of 14 runs BlockRun ClawRouter 0.12.312 0 of 14 runs Coinbase AgentKit ( main , unreleased, f2f3e8c ) 6 of 14 runs The two that pass do it in different ways, and both are worth copying: vAPI parses the 402 it is about to pay, applies the price limit and the expected payee to that quote, reserves the amount against a cumulative cap, and signs that same quote. If the server returns a changed quote after authorization, it stops and does not retry on its own. It also refuses to pay a non-HTTPS endpoint. ClawRouter turns off the library's default cap and enforces its own policy in the x402 client's onBeforePaymentCreation hook, on the exact requirement about to be signed, with allowlists for payee, network and asset. Every refusal names the rule that stopped it. On AgentKit's development branch, the two-step flow checks the limit against the option the model passed in, while the payment is created from a fresh 402. Quoted 0.10, it signed 0.90; quoted one payee, it paid another; quoted Base Sepolia, it signed for Base mainnet. The automatic action does not apply the limit at all. And the action's result reports the amount that was checked, not the one that was signed, so the agent's own log said 0.10 when it signed 0.90. (The released 0.10.4 has no limit option at all — it does not enforce spend caps and documents that it leaves this to the developer, so it is a different case: no promise, nothing broken.) I'm naming names only because it is public, reproducible code and the point is the pattern, not the vendor. Any of these can change tomorrow; the test is in the repo, so check for yourself rather than trust this table. The rule All of it reduces to one sentence: apply the spend policy to the requirement you sign, and bind it to the quote that was approved. Same amount or less, same payee, same asset, same network — or no signature. It is not in the x402 specification today, and there is no client conformance test that would catch a kit that gets it wrong — which is why I built this one, and why I plan to raise both with the x402 Foundation. The same gap exists one layer up. In the Agentic Commerce Protocol, the call that completes a checkout carries the payment credential but nothing that identifies the order the buyer approved. I opened SEP #325 to carry an approved_purchase digest and refuse completion when it does not match — the same "what you approved is what settles" rule, after two contributors there sharpened it (one with data showing agents pay store-inflated totals without asking). Where this stops The harness tests what a client signs , not what a person saw . If the agent showed the human something different from the quote it checked, a correct client still signs the wrong thing faithfully. Binding the display is a separate, harder problem. A seller that quotes honestly and then fails to deliver is a different issue. Three SDKs is a sample, not a survey. Adding one is a single file; please send the ones I missed. If you build agent payments Run the harness against your client. If a changed 402 gets signed, move your check to the payment you sign, and make your result report what was signed, not what was quoted. — Cleiton Augusto Correa Bezerra GitHub: github.com/cleitonaugusto X: @cleitonaugustob Email: augusto.cleiton@gmail.com

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/cleiton_augusto_/the-limit-you-configured-is-not-the-limit-it-applies-53mp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
