---
title: "Giving Claude live Polymarket data with an MCP server"
slug: "giving-claude-live-polymarket-data-with-an-mcp-server"
author: "ekocam"
source: "devto_python"
published: "Sat, 25 Jul 2026 19:05:56 +0000"
description: "Large language models are good at reasoning about numbers and bad at knowing them. Ask Claude which Polymarket wallets are actually profitable and you will g..."
keywords: "orcalayer, model, mcp, your, server, data, claude, smart"
generated: "2026-07-25T19:16:03.114600"
---

# Giving Claude live Polymarket data with an MCP server

## Overview

Large language models are good at reasoning about numbers and bad at knowing them. Ask Claude which Polymarket wallets are actually profitable and you will get a confident answer assembled from training data that was already stale when the model shipped. The Model Context Protocol fixes that by letting the model call your data directly. This post walks through a working example: a small MCP server that puts live Polymarket whale analytics into Claude Desktop, Cursor, or any other MCP client. The server is open source and MIT licensed, so you can read the whole thing: github.com/orcalayer/orcalayer-mcp . What MCP actually does An MCP server exposes three kinds of capability to a model: Tools the model can call, with typed arguments and structured results Prompts the user can pick from a menu, which orchestrate several tools at once Resources the model can read directly as context, without spending a tool call That third one matters more than people expect. A methodology document loaded as a resource means the model knows how your numbers are defined before it starts interpreting them. Setup The server is a stdio wrapper over the Python SDK, so there is nothing to deploy. Add it to your claude_desktop_config.json : { "mcpServers" : { "orcalayer" : { "command" : "uvx" , "args" : [ "orcalayer-mcp" ] } } } On Windows the file lives at %APPDATA%\Claude\claude_desktop_config.json , on macOS at ~/Library/Application Support/Claude/claude_desktop_config.json . Restart the app after editing. That is the whole install. uvx fetches and runs the package on demand, so there is no virtualenv to manage. The tools Five tools, four of which need no key at all: Tool What it does Key leaderboard Rank smart-money whales by P&L, win rate or volume No wallet_overview A wallet's profile and performance summary No wallet_positions A wallet's largest open positions No markets Search markets where smart whales are clustering No whale_alerts Live feed of recent smart-whale trades Premium For the Premium tool, pass the key through the environment rather than hardcoding it: { "mcpServers" : { "orcalayer" : { "command" : "uvx" , "args" : [ "orcalayer-mcp" ], "env" : { "ORCALAYER_API_KEY" : "your_key_here" } } } } Prompts do the orchestration The part worth stealing for your own server is the prompt layer. Rather than making the user chain tool calls by hand, ship prompts that encode the workflow you actually want: Prompt What it does analyze_wallet Full wallet analysis: smart money or farmer? find_divergence Markets where smart money disagrees with the current price hedge_check Whether a wallet's profit was real alpha or a hedge structure territorial_markets_review Ukraine territorial markets with an ISW frontline overlay hedge_check is the one I would point at if you are building something similar. A wallet that holds both sides of the same market can post a spectacular profit number that means nothing directionally. A naive integration reports that as alpha. Encoding the check as a prompt means the model runs it every time instead of only when the user thinks to ask. That is the general lesson: your domain knowledge belongs in the prompts, not in the user's head. Resources for definitions Three resources load as plain context: orcalayer://methodology covers how smart money is separated from farmers, hedgers and market makers orcalayer://glossary is a prediction-markets glossary orcalayer://api-reference is the REST API reference, including auth and rate limits If your data has any non-obvious definitions, and analytics data always does, put them in a resource. It costs nothing at query time and stops the model from inventing its own interpretation of your columns. One design note on honest nulls The Premium stream now tags every event with a settlement_type of MINT , MERGE , COMPLEMENTARY or null , describing how a match settled rather than what the trader intended. The null is deliberate. It means the pipeline could not determine the settlement type, not that the trade was something else. It is tempting to collapse an unknown into a default, and it is almost always the wrong call: a model reading your data cannot tell a real zero from a missing one, so it will treat your guess as fact. Return the honest null and let the caller decide. Try it Which Polymarket wallets have the best win rate right now, and are any of them just farming near-settled markets? Ask that in Claude Desktop with the server connected and it will call leaderboard , then run the farmer check from the methodology resource, and tell you which of the top names are not what they look like. The server is MIT licensed at github.com/orcalayer/orcalayer-mcp , and the underlying REST API is documented at orcalayer.com/docs/api . Data is for informational purposes only and is not financial advice.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ekocam/giving-claude-live-polymarket-data-with-an-mcp-server-5e5e

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
