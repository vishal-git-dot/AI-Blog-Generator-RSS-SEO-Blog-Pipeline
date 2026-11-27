---
title: "Gate a Solana bot swap with a pre-trade token risk check"
slug: "gate-a-solana-bot-swap-with-a-pre-trade-token-risk-check"
author: "Erik Hill"
source: "devto_python"
published: "Fri, 27 Nov 2026 20:41:04 +0000"
description: "Most Solana bots send the swap first and look at risk later. A better default is a hard gate: call a token check, apply a few thresholds, and skip the trade ..."
keywords: "mint, check, not, key, com, python, mindthemint, api"
generated: "2026-11-27T20:56:45.959130"
---

# Gate a Solana bot swap with a pre-trade token risk check

## Overview

Most Solana bots send the swap first and look at risk later. A better default is a hard gate: call a token check, apply a few thresholds, and skip the trade when the mint fails. I published a small open-source starter that does exactly that, in zero-dependency Python (stdlib urllib ) and TypeScript (Node 18+ fetch ): egnaro9/mind-the-mint-starter . It uses the same HTTP check as the free website at mindthemint.com . This is a heuristic risk screen, not financial advice, and not an audit. Scores are risk signals, not buy or sell calls. Get a free 100-check key Website checks stay free and unlimited, with no signup. The HTTP API is for bots and needs a key. You can issue a free 100-check trial key (one per network every 30 days) in one click on mindthemint.com or mindthemint.com/docs , or with: curl -X POST https://mindthemint.com/v1/trial-key export MINDTHEMINT_API_KEY = "your_trial_key" Do not commit the key. Call the check The live contract is a single GET, with the key in the X-API-Key header: curl -H "X-API-Key: $MINDTHEMINT_API_KEY" \ https://mindthemint.com/v1/check/JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN A successful body includes risk_score (0 to 100), risk_level , flags , and a heuristics object with mint_authority_active , freeze_authority_active , and top10_holder_pct . Full examples live in the API docs and in the repo fixture. Default guardrails and exit codes The starter blocks a mint when any of these are true: risk_score is at or above 25 mint authority is active freeze authority is active top10_holder_pct is above 80 Override them with flags or env vars ( --max-risk-score , --max-top10-pct , --allow-mint-authority , --allow-freeze-authority ). Exit codes are simple to wire into a bot: Code Meaning 0 Token passed your thresholds 2 Token was blocked 1 Error (missing key, HTTP 401/402/429, or a network failure) Drop it in before the swap Python: python python/check_token.py JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN Or import the same functions your CLI uses: import os from check_token import fetch_check , evaluate mint = "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN" payload = fetch_check ( mint , os . environ [ "MINDTHEMINT_API_KEY" ] ) decision = evaluate ( payload ) if not decision [ "passed" ] : print ( "skip trade:" , "; " . join ( decision [ "reasons" ] ) ) raise SystemExit ( 2 ) # continue with your swap The TypeScript filter is a drop-in match ( typescript/checkToken.ts in the repo). A real dry-run on the JUP fixture The repo ships tests/fixtures/jup_pass.json , shaped like a live Mind the Mint check of JUP captured on 27 November 2026. This dry run used that fixture only. It did not call the API or spend a credit: $ python python/check_token.py --fixture tests/fixtures/jup_pass.json PASS JUP (JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN) risk_score 23 low (block at 25+) mint_authority inactive freeze_authority inactive top10_holder_pct 64.61 (max 80) credits_remaining 99 summary: Top holders look like one entity split across wallets accounting for 64.61% of supply, and top 10 holders control 64.61%. Mint and freeze authorities are inactive, liquidity is 3.54 million USD, and pair age is 24744.19 hours. This is not a buy signal. The score does not cover the team, social channels, off-chain custody, or later changes to the mint. JUP passes these defaults because the score is 23, both authorities are inactive, and top-10 concentration is 64.61%, under the 80 cap. A high score, an active mint or freeze authority, or a more concentrated holder set exits 2 and should skip the swap. Clone it here: github.com/egnaro9/mind-the-mint-starter . Run a free website check at mindthemint.com , or read the API docs . Built by Erik Hill. MIT licensed. Not financial advice.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/agentdev9/gate-a-solana-bot-swap-with-a-pre-trade-token-risk-check-2b4i

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
