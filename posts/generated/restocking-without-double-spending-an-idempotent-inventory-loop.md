---
title: "Restocking without double-spending: an idempotent inventory loop"
slug: "restocking-without-double-spending-an-idempotent-inventory-loop"
author: "mujin"
source: "devto_python"
published: "Tue, 10 Nov 2026 14:35:59 +0000"
description: "The invariant that keeps inventory honest: remaining is preloaded minus totalSupply, and why preloaded alone is a lie My inventory daemon uses this invariant..."
keywords: "preload, earlier, piece, contract, later, chain, before, inventory"
generated: "2026-11-10T14:38:48.358147"
---

# Restocking without double-spending: an idempotent inventory loop

## Overview

The invariant that keeps inventory honest: remaining is preloaded minus totalSupply, and why preloaded alone is a lie My inventory daemon uses this invariant: remaining = preloaded - totalSupply preloaded is the amount of metadata registered for future minting. It is not the amount currently available. Every successful mint consumes inventory by increasing totalSupply , while the preload count stays unchanged. A dashboard that displays only preloaded therefore overstates availability as soon as minting starts. The same mistake in a restocking daemon is worse: the daemon may decide inventory is healthy even though buyers have consumed most of it. I read both values from the NFT contract on Base during every loop. I do not maintain a separate mutable “remaining” counter. That would create another value that could drift after a crash, RPC failure, or manual transaction. The contract caps the drop at 131 pieces and limits each wallet to 5. Minting is free; the buyer pays only gas. The changing live count is readable on the contract rather than embedded in copy or configuration. The decision rule is simple: calculate remaining from current contract state, then restock only when the local policy says that value is too low. If either contract read fails, the loop does nothing. The order of operations (upload, preload, verify, then log) and which crash points make a retry safe or unsafe My write path is deliberately ordered: upload asset and metadata preload the piece on Base verify the successful preload from chain state upsert the local inventory log Uploading first prevents the contract from pointing at an object that does not exist. I use a stable piece identifier across the metadata, preload call, verification, and local log. The on-chain preload costs about 0.0000008 ETH per piece. That is small, but blindly repeating it is still incorrect. A retry must begin with discovery, not another write. Crash point Blind retry Correct recovery Before upload completes Safe if the upload destination is content-addressed Upload again and confirm the resulting reference After upload, before preload Safe Reuse the same reference and submit the preload After preload submission, before receipt Unsafe Search chain state and canonical logs for the piece identifier before sending anything After verification, before local logging Unsafe if retry resubmits the preload Re-read the chain, then upsert the log After local logging Safe The upsert returns the existing record The dangerous window is between transaction submission and local logging. A timeout does not mean failure; it means the result is unknown. I treat “unknown” as a reconciliation state. The daemon checks whether the piece identifier already exists on-chain. If it does, the daemon records the existing transaction. If it does not, only then may it submit a preload. The reconciliation query that proves no piece was preloaded twice I index successful preload events into preload_events . The table includes the contract address, piece identifier, transaction hash, block position, transaction position, and log position. This self-join returns every piece identifier with an earlier and later preload event: SELECT earlier . piece_id , earlier . tx_hash AS earlier_tx , later . tx_hash AS later_tx FROM preload_events AS earlier JOIN preload_events AS later ON later . contract_address = earlier . contract_address AND later . piece_id = earlier . piece_id AND ( earlier . block_number , earlier . transaction_index , earlier . log_index ) < ( later . block_number , later . transaction_index , later . log_index ) WHERE earlier . contract_address = : contract_address ; An empty result means the indexed canonical event history contains no repeated preload for the same piece identifier. I run this after ingestion and before allowing the daemon to leave reconciliation mode. The indexer also discards logs removed by chain reorganization, so the query reflects canonical history rather than a stale receipt. Practical takeaway: make retries read chain state before they write, and audit the invariant against the live contract at the collection page .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mujin/restocking-without-double-spending-an-idempotent-inventory-loop-38n7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
