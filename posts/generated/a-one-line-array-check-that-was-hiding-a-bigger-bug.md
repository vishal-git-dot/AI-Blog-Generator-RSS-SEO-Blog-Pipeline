---
title: "A one line array check that was hiding a bigger bug"
slug: "a-one-line-array-check-that-was-hiding-a-bigger-bug"
author: "sirmos"
source: "devto_webdev"
published: "Wed, 12 Aug 2026 07:15:19 +0000"
description: "This is a submission for DEV's Summer Bug Smash: Clear the Lineup powered by Sentry . Project Overview Brickwarden pairs two agents around one tokenized asse..."
keywords: "one, transactions, prepared, array, const, mint, transaction, call"
generated: "2026-08-12T07:40:00.503479"
---

# A one line array check that was hiding a bigger bug

## Overview

This is a submission for DEV's Summer Bug Smash: Clear the Lineup powered by Sentry . Project Overview Brickwarden pairs two agents around one tokenized asset on Ethereum Sepolia, built on Brickken's sandbox API. An Issuer Agent creates the asset, runs the offering, whitelists investors, mints tokens, and pays out dividends. A Warden Agent watches the same asset for compliance triggers and can revoke access or burn tokens on its own the moment something goes wrong, no approval needed from the Issuer. Every write action either agent takes, mint, whitelist, burn, approve, goes through one shared helper function that prepares a transaction, signs it locally, and sends it to the chain. Bug Fix or Performance Improvement That shared helper assumed the API always returns an array of transactions to sign. That held up for months, until one specific call broke it. I needed to mint tokens to an investor who was already whitelisted, so I passed needWhitelist: true anyway, expecting it to just get skipped. Instead the API responded with transactions as a single object instead of an array, and the loop that signs each transaction crashed with: Re-mint failed: prepared.transactions is not iterable ![Terminal showing the crash after two earlier failed attempts, ending in "prepared.transactions is not iterable"] Nothing in the error pointed at the real cause. I compared the raw response against a normal, working mint call side by side, and the only difference was that one field's shape, an object where an array should have been, and only when that one flag combination fired. Code Before: console . log ( `Signing ${ prepared . transactions . length } transaction(s)...` ); const signedTransactions = []; for ( const tx of prepared . transactions ) { signedTransactions . push ( await wallet . signTransaction ( tx )); } After: const txList = Array . isArray ( prepared . transactions ) ? prepared . transactions : [ prepared . transactions ]; console . log ( `Signing ${ txList . length } transaction(s)...` ); const signedTransactions = []; for ( const tx of txList ) { signedTransactions . push ( await wallet . signTransaction ( tx )); } Full source: https://github.com/sirmos/Brickwarden/blob/main/src/brickkenRest.js My Improvements I could have special cased this one call and moved on, but the helper is shared across every write action in the project, so a narrow fix would only have delayed the next time this shape showed up somewhere else. The Array.isArray check normalizes the response once, at the one place all of them pass through, so every call benefits from the same guard instead of needing its own workaround. I also logged the raw prepared response before touching it, rather than guessing from the error text alone. The error said "not iterable," which explains what broke but not why. Seeing the actual shape next to a working response made the real cause obvious in one comparison instead of several rounds of trial and error. Thank you for reading!!!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sirmos/a-one-line-array-check-that-was-hiding-a-bigger-bug-5bp2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
