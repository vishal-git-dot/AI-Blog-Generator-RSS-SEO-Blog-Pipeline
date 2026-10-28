---
title: "How to give GitHub Copilot codebase context that persists"
slug: "how-to-give-github-copilot-codebase-context-that-persists"
author: "Syed Fahad"
source: "devto_ai"
published: "Wed, 28 Oct 2026 12:26:29 +0000"
description: "GitHub Copilot codebase context vanishes when the chat ends, because each session starts from zero and Copilot searches the repo again. A graph built once on..."
keywords: "graphify, copilot, graph, you, install, code, how, page"
generated: "2026-10-28T12:28:53.745897"
---

# How to give GitHub Copilot codebase context that persists

## Overview

GitHub Copilot codebase context vanishes when the chat ends, because each session starts from zero and Copilot searches the repo again. A graph built once on your machine is a map Copilot can query the next time. Graphify builds that graph and registers it with Copilot. How do you give GitHub Copilot codebase context? The GitHub Copilot integration page wires this in two commands, then a graph of the repo. The package on PyPI is graphifyy (two y's). uv tool install graphifyy pipx install graphifyy also works. graphify install graphify install registers the /graphify skill and an MCP server, so Copilot can query the graph. Graphify speaks the Model Context Protocol . Any MCP client talks to the same server and the same ten graph tools. The integration page points at the docs for how to point Copilot at that server. Build the graph on the project you have open. In Copilot, run: /graphify . Tree-sitter parses the code locally, so call and import edges come from the syntax tree. Docs and other non-code files are read by the model you already use. The map lands in graphify-out/ as graph.html , GRAPH_REPORT.md , and graph.json . The next session queries those files. The architecture is already on disk. A knowledge graph here means entities and the typed relationships between them. The same shape of setup for Cursor is How to give Cursor a code knowledge graph . What can Copilot ask once the graph exists? The questions on the integration page are the ones that used to mean reading a large slice of the repo. What calls chargeCustomer , and what breaks if the signature changes. The path from a checkout endpoint to the table it writes. Which modules read a config value such as STRIPE_KEY . How the auth subsystem hangs together before you touch it. You can run the same questions from the shell. The page names these commands: graphify query "what calls chargeCustomer" graphify path "checkout" "database" graphify explain "AuthService" graphify prs graphify query returns a scoped piece of the graph. graphify path walks the hops between two nodes. graphify explain lists the edges on one symbol. graphify prs is the pull-request command listed beside them. The docs cover its flags. Every edge Copilot gets back carries a confidence tag. EXTRACTED was parsed from the AST with tree-sitter. INFERRED means a model connected non-code material, such as a doc to the service it describes, and the tag marks that judgment. AMBIGUOUS means there was evidence and it could not be fully resolved, as with dynamic dispatch or an import built from a string. The edge is kept and flagged. When Copilot returns a path, open the file and line on the hop you are about to trust, and read the tag on that edge. An EXTRACTED edge is the parser. An INFERRED edge is the model joining a doc or a schema to code. It can be wrong and still sound plausible. An AMBIGUOUS edge is unresolved evidence, kept so the gap stays visible. The integration page describes the return value as connected structure, a path, which still holds past one or two hops. A pile of matching files, with the links guessed in the chat, is the loop this replaces. What does the graph leave to you? The graph does not update itself. After the code changes, run /graphify . again, or /graphify . --update to re-scan only what changed. From the shell, graphify update . does that pass. graphify hook install adds post-commit and post-checkout git hooks that refresh the changed files. Until you refresh, Copilot is reading the last map you built. Grep still wins when the question is "find this string." The graph is for relationships. A literal string in a comment is still a search. The open-source engine runs on your machine. Code parsing is local. There is no telemetry. Graphify Cloud is the hosted graph. This guide is the on-device setup. Cloud is a different product. How do you confirm it is wired? uv tool install graphifyy graphify install Then, in Copilot: /graphify . The command reference is in the docs . Copilot-specific notes stay on the GitHub Copilot integration page.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/graphify/how-to-give-github-copilot-codebase-context-that-persists-4f0f

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
