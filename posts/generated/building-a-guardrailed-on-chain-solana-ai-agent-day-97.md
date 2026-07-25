---
title: "Building a Guardrailed On-Chain Solana AI Agent (Day 97)"
slug: "building-a-guardrailed-on-chain-solana-ai-agent-day-97"
author: "Hala Kabir"
source: "devto_ai"
published: "Sat, 25 Jul 2026 19:06:58 +0000"
description: "Building a Guardrailed On-Chain Solana AI Agent Autonomous AI agents interacting with blockchain wallets present both immense potential and significant secur..."
keywords: "agent, policy, wallet, run, tool, execution, savings, lamports"
generated: "2026-07-25T19:16:03.118094"
---

# Building a Guardrailed On-Chain Solana AI Agent (Day 97)

## Overview

Building a Guardrailed On-Chain Solana AI Agent Autonomous AI agents interacting with blockchain wallets present both immense potential and significant security risks. Giving an LLM direct access to private keys without strict guardrails can quickly lead to drained wallets or unauthorized execution. For Day 97 of 100 Days of Solana , I built and documented a production-grade on-chain workflow agent that features a deny-by-default policy engine , structured tool-calling loops, and full execution logging. 🛠️ System Architecture & How It Works The architecture separates the agent's decision-making layer (LLM) from actual wallet execution through a strict Policy Middleware Layer : Autonomous Decision Engine : Uses an LLM tool-calling loop (via OpenRouter) to evaluate goal states (e.g., "Ensure savings wallet holds at least 0.2 SOL" ). Policy Enforcement Layer : Intercepts every tool call requested by the model before hitting the blockchain. Deny-by-Default Guardrail : Any transaction request exceeding safety parameters is automatically rejected. Limit Validation : Enforces maximum transfer caps per run. Recipient Verification : Validates destination addresses against known white-listed account sets. Structured Run-Log : Records all system states, model inputs/outputs, tool payloads, policy approvals/denials, and final execution signatures into a clean run-log.json report. 🚀 Quickstart & Setup Guide 1. Prerequisites Node.js (v18+) OpenRouter API Key (for LLM reasoning) 2. Environment Setup Clone the repository and install dependencies: bash npm install @solana/web3.js dotenv export OPENROUTER_API_KEY = "your-openrouter-key" 3. Keypair Configuration Generate or load the operating and savings keypairs: node setup-keys.mjs This populates agent-wallet.json (operating wallet) and savings-wallet.json (savings wallet). 💻 Running the Agent Workflow You can run the agent against Solana Devnet or using the local mock environment: node agent-workflow.mjs Execution Output Sample: GOAL: Ensure the savings wallet holds at least 0.2 SOL. Check balances before moving anything, move only what is needed from the operating wallet, and verify final balances. --- Turn 1 --- [tool] get_balance({"address":"5fzNoe96en7mSc23bcywuDn5kguo8yGTFmSa1evUedEj"}) -> { lamports: 0 } --- Turn 2 --- [tool] get_balance({"address":"B2rbFAthmaTvhWoFHt4Ar1tEnX4hsutavT4Wdv9KD5nM"}) -> { lamports: 1000000000 } --- Turn 3 --- [tool] transfer_sol({"lamports":200000000,"to":"5fzNoe96en7mSc23bcywuDn5kguo8yGTFmSa1evUedEj"}) -> { status: 'confirmed', signature: 'mock_tx_sig_3vx32gid79' } --- Turn 4 --- === FINAL REPORT === The savings wallet balance is now 200,000,000 lamports (0.2 SOL). Task completed successfully. Run log written to run-log.json 🔒 Policy Safety Contract The policy engine implements the following explicit rules: function validatePolicy ( action ) { if ( action . type === ' transfer_sol ' ) { if ( action . lamports > MAX_TRANSFER_LIMIT ) { throw new Error ( `Policy Violation: Transfer amount exceeds max limit of ${ MAX_TRANSFER_LIMIT } lamports.` ); } if ( ! ALLOWED_RECIPIENTS . includes ( action . to )) { throw new Error ( `Policy Violation: Recipient ${ action . to } is not whitelisted.` ); } } return true ; } 📝 Key Takeaways Never trust LLM output directly for web3 writes: Always run transactions through an independent, deterministic policy checker. Deterministic Fallbacks: Including local mock/dry-run capabilities ensures agent pipelines remain resilient even during external RPC rate limits or network issues. Auditability: Complete structured logging ( run-log.json ) allows developers to verify every decision path taken by the AI before and after execution.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/halakabir234hub/building-a-guardrailed-on-chain-solana-ai-agent-day-97-2gim

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
