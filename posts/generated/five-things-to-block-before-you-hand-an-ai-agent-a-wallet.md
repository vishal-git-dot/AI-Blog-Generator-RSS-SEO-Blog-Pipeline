---
title: "Five things to block before you hand an AI agent a wallet"
slug: "five-things-to-block-before-you-hand-an-ai-agent-a-wallet"
author: "agent402dev"
source: "devto_ai"
published: "Wed, 25 Nov 2026 07:48:31 +0000"
description: "An agent that can pay for an API call is useful: it can buy a dataset, a receipt or a conversion the moment it needs one, without you pasting card details an..."
keywords: "can, pay, you, agent, mcp, wallet, without, not"
generated: "2026-11-25T07:53:48.787144"
---

# Five things to block before you hand an AI agent a wallet

## Overview

An agent that can pay for an API call is useful: it can buy a dataset, a receipt or a conversion the moment it needs one, without you pasting card details anywhere. It can also pay the wrong host, pay twice, or keep paying while you sleep. The fix is not to trust the agent more. It is to give the wallet rules that the agent cannot talk its way around. Below are the five rules we put in front of every signature in @agent402-dev/pay-mcp , an MCP server that pays x402 prices in USDC on Solana. The rules are checked on your machine before anything is signed, and with no configuration every payment is refused. The ideas apply to any agent wallet, whatever tool you use. 1. Unknown hosts A paid URL can come from anywhere: a search result, a tool response, a document the agent just read. If the agent can pay any host that answers 402, anyone who can put a URL in front of it can charge it. Block it with an allowlist of hosts. In pay-mcp that is X402_ALLOWED_DOMAINS (https only, http only for localhost). Redirects are followed by hand and every hop must be on the list; a hop that is not on it is never contacted. 2. Unknown recipients An allowed host can still ask you to pay a different address tomorrow, or be compromised today. The domain check alone does not tell you where the money goes. Block it with an allowlist of recipient addresses: X402_TRUSTED_PAY_TO . A 402 response that asks for any other payTo is refused before signing. 3. Unbounded amounts A single price can be wrong, and a loop of correct prices can still add up. Limits need to cover both. pay-mcp has a cap per payment ( X402_MAX_USD , default 0.05 USDC), per UTC day ( X402_MAX_USD_PER_DAY , default 1 USDC), a count per day ( X402_MAX_PAYMENTS_PER_DAY , default 20) and an optional cap per recipient per day. Daily totals count every payment the server signed, whatever happened next, and a warning appears at 80% of a cap so the agent can tell you before it stops. 4. Paying twice, or paying a price that changed Agents retry. A retry after a timeout can mean a second payment for the same thing, and the price you saw a minute ago may not be the price asked now. pay-mcp signs at most once per x402_fetch call; if the server answers 402 again after payment, it does not sign again. x402_quote shows the price without paying and returns a quoteId ; pass it to x402_fetch and the payment is refused if the amount, asset or recipient changed. When a paid request fails after signing, the result says failed and points at payment_history instead of retrying on its own. 5. Large payments without a person Some payments should never be the agent's call alone. Set a threshold and ask a human at or above it: X402_CONFIRM_ABOVE_USD . pay-mcp asks through MCP elicitation, the form your client shows. If the client cannot show that form, or fails while asking, nothing is signed and the result is confirmation_required . For work that takes time instead of a single call, the same idea goes further: an Agent402 Bond job locks a seller bond and a buyer deposit, and the balance is paid only when you accept the result. If you do nothing, each side gets its own money back. Try the rules without a wallet You can see what an agent would pay for, and which rule would refuse it, without a wallet and without paying anything: claude mcp add a402-pay -- npx -y @agent402-dev/pay-mcp Then ask your agent to run wallet_status and x402_quote on a paid URL. The one-minute walkthrough has the steps. Use a small, dedicated wallet for any agent, keep its key on your own machine, and fund it with what you are willing to let it spend in a day. The toolkit is open source (Apache-2.0). Its on-chain programs have had internal review only and are not independently audited.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/agent402dev/five-things-to-block-before-you-hand-an-ai-agent-a-wallet-3hkn

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
