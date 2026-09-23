---
title: "Two standards are reviving HTTP 402, and it changes who owns the customer"
slug: "two-standards-are-reviving-http-402-and-it-changes-who-owns-the-customer"
author: "Michael Hairetis"
source: "devto_ai"
published: "Wed, 23 Sep 2026 11:06:41 +0000"
description: "HTTP 402 has sat unused in the spec since the early web. Two competing standards are now bringing it back, and the reason matters more than the trivia. x402 ..."
keywords: "payments, agent, card, two, than, stablecoin, stripe, not"
generated: "2026-09-23T11:11:45.089044"
---

# Two standards are reviving HTTP 402, and it changes who owns the customer

## Overview

HTTP 402 has sat unused in the spec since the early web. Two competing standards are now bringing it back, and the reason matters more than the trivia. x402 , from Coinbase. An agent requests a resource, the server answers 402 with payment instructions, the agent signs a stablecoin transaction and retries with proof attached. No account, no login, no stored card. Most traffic settles in USDC on Base or Solana. Coinbase and Cloudflare moved it under a foundation with Circle, Stripe and AWS involved, and it is one of the first extensions to Google's Agent Payments Protocol. It currently carries the most volume of the two. MPP , the Machine Payments Protocol, from Stripe and Tempo. Spec at mpp.dev, launched March 2026. Two things make it notable. It is not stablecoin-only: Stripe offramps agent stablecoin payments into an ordinary Stripe balance, and fiat and card payments run through it via Shared Payment Tokens, with Visa publishing card specs and an SDK. And it adds a sessions primitive, where an agent authorises a spending limit once and then streams many small payments without settling each one separately. So the framing is not "stablecoins replace cards." Machine payments need three properties card rails were never designed for: small amounts, high frequency, and authority scoped and revocable per purchase rather than per account. Stablecoin rails got there first because they could. The card networks are arriving through the same protocols rather than being displaced. The honest state: in March 2026 x402 was processing on the order of tens of thousands of dollars a day, much of it testing, against an ecosystem valued in the billions. The protocol works and the facilitators are live. Widespread use is years away, not a question of whether. I wrote up what this does to the businesses in the middle. Short version: a delivery app's moat was the interface, not the logistics, and a driver fleet is a hard operational job rather than a defensible asset. https://openred.space/blog/the-interface-was-the-moat.html

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/michaelhairetis/two-standards-are-reviving-http-402-and-it-changes-who-owns-the-customer-3njn

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
