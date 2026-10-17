---
title: "Rules: no AI clichés (listed banned words). Senior engineer style like Dan Luu / P..."
slug: "rules-no-ai-clichs-listed-banned-words-senior-engineer-style-like-dan-luu-p"
author: "Sandi"
source: "devto_python"
published: "Sat, 17 Oct 2026 10:12:57 +0000"
description: "The user wants a technical article draft in Indonesian (mostly) for Dev.to/Paragraph.com, ~600 words, about zero-gas autonomous agents and account abstractio..."
keywords: "paymaster, gas, base, indonesian, account, entrypoint, zero, let"
generated: "2026-10-17T10:24:53.456107"
---

# Rules: no AI clichés (listed banned words). Senior engineer style like Dan Luu / P...

## Overview

The user wants a technical article draft in Indonesian (mostly) for Dev.to/Paragraph.com, ~600 words, about zero-gas autonomous agents and account abstraction on Base L2. Target audience: AI engineers, Web3 developers, crypto builders. Rules: no AI clichés (listed banned words). Senior engineer style like Dan Luu / Paul Graham: direct, varied rhythm, honest, empirically grounded. Include real Python/Web3 code. Reference Base L2 (Chain ID 8453) and autonomous cash wallet: 0x92Aff59709b03b9373b8fA887D24953D60fAd919. The article should be in Indonesian (the instructions are in Indonesian, and the banned phrases include Indonesian ones). I'll write mostly in Indonesian with English technical terms — that's typical for Dev.to Indonesian devs. Actually let me consider — could be either. The prompt is in Indonesian, so I'll write in Indonesian. Keep code in Python. Let me design a real technical argument: Key technical content: ERC-4337 (EntryPoint v0.7 on Base), Paymaster (verifying paymaster / ERC-20 paymaster), bundlers (Pimlico, Alchemy, Stackup). Base L2 specifics: Chain ID 8453, low gas (EIP-1559, base fee ~0.001-0.01 gwei), ~2s block time. Post-EIP-4844 blob fees. Zero-gas for the agent: the agent's UserOperation is sponsored by a paymaster. But "zero gas" doesn't mean free — someone pays. Options: Sponsorship by the operator (subsidy) — normal for a bounded task budget. ERC-20 paymaster — agent pays in USDC, but then needs USDC first (chicken-and-egg). Pre-funded paymaster deposit at EntryPoint, with signed off-chain policy. The honest part: the hard problem isn't gas sponsorship, it's the policy engine — rate limits, allowlists, spend caps. Because an LLM with a key is a liability. Paymaster plus session keys. Code: Python with web3.py + eth-account, build a UserOperation, sign it, submit to bundler via eth_sendUserOperation RPC (Pimlico/Alchemy). Include paymaster fields. Also mention simulation: eth_call with EntryPoint.simulateValidation, or bundler's eth_estimateUserOperationGas . Nonce management: 2D nonce (key + sequence) in EntryPoint v0.7. Failure modes: paymaster deposit drained, bundler rejects on paymasterAndData timestamp expiry, agents replaying failed ops, HA — retry idempotency. Empirical numbers: a swap on Base costs ~$0.0001–0.001. So gas isn't the cost center, the bundler markup is. That's a good Dan Luu-style point: measure. Actually a really good honest point: on Base, gas is so cheap that paymasters are often over-engineering. If your UserOp costs 120k gas at 0.005 gwei base fee + 0.001 gwei priority, that's 120000 * 0.006e-9 ETH = 7.2e-7 ETH ≈ $0.002 at $3000/ETH. So sponsorship budget for 10k ops/day is $20/day. The real reason for AA isn't gas, it's atomicity (batching), session keys, and recovery. Wait — but the article title says "Zero-Gas Autonomous Agents". So we should define what "zero-gas" means precisely: the agent holds zero ETH. It can still transact. The sponsoring paymaster holds the ETH. Let me write the code: # agent_paymaster.py — Base mainnet import os , time import requests from eth_account import Account from eth_abi import encode from web3 import Web3 BASE_CHAIN_ID = 8453 BUNDLER = " https://api.pimlico.io/v2/8453/rpc " # or your own bundler ENTRYPOINT = " 0x0000000071727De22E5E9d8BAf0edAc6f37da032 " # v0.7 AGENT_EOA = " 0x92Aff59709b03b9373b8fA887D24953D60fAd919 " EntryPoint v0.7 address is 0x0000000071727De22E5E9d8BAf0edAc6f37da032. Correct. EntryPoint v0.6 is 0x5FF137D4b0FDCD49DcA30c7CF57E578a026d2789. Correct. Actually, the "AGENT_EOA" — the wallet 0x92Aff... — I'll treat it as the smart account address (the deployed account, counterfactual or deployed). Since it starts with 0x92 not 0x being a typical counterfactual, but fine. I'll call it "the account" (smart account address), not EOA, since AA accounts are contracts. But the article says "dompet kas otonom" = autonomous cash wallet. I'll say it's the smart account address. Code should show building the UserOperation with paymasterAndData including a validity window and sponsor signature. Let me write the paymasterAndData encoding: v0.7 paymasterAndData: paymaster (20) || paymasterVerificationGasLimit (16) || paymasterPostOpGasLimit (16) || paymasterData (variable) v0.6: paymaster (20) || paymasterVerificationGasLimit (16) || paymasterPostOpGasLimit(16) || validUntil(6) || validAfter(6) || signature(65) I'll use v0.7 style since that's current (Base supports both). Let's write: def pack_paymaster_data ( paymaster : str , valid_until : int , sig : bytes ) -> bytes : return ( bytes . fromhex ( paymaster [ 2 :]) + ( 150_000 ). to_bytes ( 16 , " big " ) # verification gas + ( 60_000 ). to_bytes ( 16 , " big " ) # postOp gas + valid_until . to_bytes ( 6 , " big " ) # sponsor deadline + sig ) Hmm, in v0.7 the paymasterData is arbitrary and the paymaster's own validatePaymasterUserOp decodes it. So a custom paymaster can define its own layout. That's a fair representation if we say "our paymaster's layout". Let me define it as the operator's own paymaster with a simple ABI encoding: abi.encode(uint48 validUntil, bytes signature) . Better: use encode(["uint48","bytes"], [valid_until, sig]) . Then: python user_op = { "sender": AGENT_WALLET, "nonce": ..., # key <<

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sandi13/rules-no-ai-cliches-listed-banned-words-senior-engineer-style-like-dan-luu-p-3m2c

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
