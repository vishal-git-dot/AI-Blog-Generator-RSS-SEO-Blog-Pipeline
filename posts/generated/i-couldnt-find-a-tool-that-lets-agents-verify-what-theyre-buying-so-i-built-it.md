---
title: "I couldn't find a tool that lets agents verify what they're buying. So I built it."
slug: "i-couldnt-find-a-tool-that-lets-agents-verify-what-theyre-buying-so-i-built-it"
author: "FieldmodeLLC"
source: "devto_webdev"
published: "Sat, 15 Aug 2026 01:12:39 +0000"
description: "I built ScrapeCheck because as someone who has been in the crypto industry for over 9 years, I know how important it is for information to be public, like th..."
keywords: "one, what, page, scrapecheck, you, agent, check, agents"
generated: "2026-08-15T01:34:58.729758"
---

# I couldn't find a tool that lets agents verify what they're buying. So I built it.

## Overview

I built ScrapeCheck because as someone who has been in the crypto industry for over 9 years, I know how important it is for information to be public, like the blockchain. With the rise of agentic commerce, I wondered if there was a tool that bots could use to ensure that the item they're looking to purchase could be verified and I could not find it so I decided to build it. Here's what that turned into, and one experiment that shows the whole thing working end to end. The problem, in one sentence Agents increasingly act on web data they didn't fetch themselves: a price from a scraper, a value from a search API, a row from a dataset. When that data is stale or wrong, nothing warns anyone. The agent that fetched it, the pipeline that stored it, and the buyer who acts on it are all trusting a number that may no longer be on the page. What ScrapeCheck does You give it three things: a URL, the value you were given, and what was asked. It independently re-fetches the page from its own infrastructure and returns one of three verdicts: pass, fail, or unverifiable. Never a guess. Two design rules do most of the work. First, a claim is never certified unless our own re-fetch actually contains it. There is a model in the loop, but it has one power only: it can veto a pass. It can never create one. AI may interpret evidence here; it never manufactures it. Second, anything we cannot independently confirm comes back unverifiable instead of being rounded to an answer. Server-rendered pages only; JavaScript-only content returns unverifiable by design. On our benchmark that discipline has held at zero false passes across 67 frozen cases (26 held out, adversarial traps included) and 21 live-web cases. Small sample, and I label it that way on the stats page too. Every verdict is signed with ed25519 and verifies offline against the published key with an open-source verifier. You don't have to trust me, my server, or my database. Check the artifact. Built for agents to buy There's no account and no API key. Payment is the credential: $0.01 per full check, $0.002 for a presence-only check, paid in-band over x402 (USDC on Base). The first 100 checks per client are free, and the 402 challenge itself tells your agent how to use them. It also runs as an MCP server on the official registry, and as the Scrape QA actor on Apify for verifying whole dataset runs. The API speaks x402 v2 and is listed in the CDP Bazaar catalog. The experiment: one agent buys from another, then verifies what it bought I wanted to know if the full loop actually works today, machine to machine, no human in the flow. So we pre-registered a test and ran it. A small buyer agent, deliberately naive, paid Exa (a search API that sells over x402) for a search result. Cost: $0.007, settled on Base. It took a value from the answer it bought, then paid ScrapeCheck $0.01, same rail, to check that value against the live source page. It got back a signed verdict it could verify offline. To be clear about what this was and wasn't: we funded the buyer wallet ourselves and labeled it as our own traffic. This was a demonstration that the loop closes, not evidence of organic demand. The methodology was committed to git before the run, no re-rolls, and the full transcript, settlement hashes included, is in the repo. And credit where it's due: Exa's endpoint worked exactly as advertised, first try. We picked them because they're one of the most real services on the rail. That loop, buy from a machine, verify with a different machine, trust neither, is what I think agentic commerce actually needs before anyone lets an agent spend real money on web claims. The honest state of things The stats page is public and it labels our own test traffic as ours. I publish the misses next to the passes, and there's a permanent line on that page for external paid checks that will read zero until it doesn't. If you want to kick the tires: the repo, the verifier, and one free check in your browser are all one click from the landing page. Service: https://scrapecheck.fly.dev Repo and offline verifier: https://github.com/FieldmodeLLC/scrapecheck-mcp#verify-a-verdict-yourself-offline Live stats, self-traffic labeled: https://scrapecheck.fly.dev/stats If you're building agents that act on web data and this is useful or missing something you need, I want to hear it. Rick C., Fieldmode LLC

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/fieldmodellc/i-couldnt-find-a-tool-that-lets-agents-verify-what-theyre-buying-so-i-built-it-j0b

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
