---
title: "Empower your agents with the new SurrealDB MCP"
slug: "empower-your-agents-with-the-new-surrealdb-mcp"
author: "Matthew McFadden"
source: "devto_ai"
published: "Wed, 05 Aug 2026 14:12:49 +0000"
description: "Exactly a year ago we released SurrealMCP, a server you had to install and run in order to connect agents to your SurrealDB instance. Today, we're excited to..."
keywords: "your, you, surrealdb, mcp, new, can, ask, server"
generated: "2026-08-05T14:21:05.080065"
---

# Empower your agents with the new SurrealDB MCP

## Overview

Exactly a year ago we released SurrealMCP, a server you had to install and run in order to connect agents to your SurrealDB instance. Today, we're excited to announce the next evolution in agent intelligence with the new hosted SurrealDB MCP server. With this new SurrealDB MCP server, all you need is to add one URL to your AI tool of choice, sign in with your SurrealDB account, and your assistant can work on your instances or contexts alongside you. Whether you want to deploy a new instance, spin up a new Spectron context, execute queries against your graph, or ask questions about your data, the new SurrealDB MCP server has you covered. Let's dive into it! 🎉 Getting started Adding the SurrealDB MCP to your agent Previously, you would need to add an MCP configuration for every instance or context that you wanted to connect to, and there was no way to provision instances or contexts with an agent. With the new hosted SurrealDB MCP server, you can do all of this and much more by adding a single URL: https://mcp.surrealdb.com You can authorise the SurrealDB MCP Server either through signing in to your SurrealDB account, or for fine grained control, create a personal access token from the account portal . That is the whole setup. Once connected, your agent now has the ability to interact with your SurrealDB Cloud resources. Looking to setup your agent? We have step-by-step guides for setting up with Claude and Cursor . For other configurations, please see our MCP docs . Deploy and manage resources just by asking Everything you would normally click through in the SurrealDB Studio dashboard is available in your conversations. Deploy a new instance or context, expand your resources as you grow, or upgrade to the latest version of SurrealDB. When deploying resources, the MCP server can put together a configuration, give you a cost estimation, and wait for your confirmation to kick off. The same conversation can also cover the rest of the housekeeping such as inviting users to your organisation, managing their access level, checking your monthly spend, and updating your instances. Ask questions about your data and build with ease Note Instance querying is only available on instances running SurrealDB 3.2.3 and above The usual way to get an AI assistant to look at your database is to copy a schema or a query into a chat window, then paste the results back out again. SurrealDB MCP removes this loop. Simply ask a question in plain language and your assistant finds the right database, writes the query, runs it, and shows you both the query it wrote and what came back. You don't have to describe the shape of your data first, because it can go and look. Ask how many orders you took last week grouped by status, and it will find the table, work out the fields, and write the aggregate itself. Ask what the customer table actually says, and it will describe the fields and indexes back to you. As a bonus, it's often faster than opening SurrealDB Studio to check for yourself. It works the other way round too. While you're building something new, you can ask it to create a single table or an entire schema for an enterprise-level app. Memory that outlasts the conversation Every new chat normally starts from nothing. A decision your team made three weeks ago is gone unless someone remembers to paste it back in. My favorite feature of SurrealDB MCP is that you can interact directly with Spectron , our memory layer for AI agents, in order to keep a persistent brain related to your chats which can be shared with multiple users. Simply ask your agent to save a memory or give it documents to read, and it will search through them by meaning rather than by keyword and store it for you. Then, ask your agent to retrieve something later: Let us know what you think We'd love to hear your thoughts! Join us on Discord to ask questions, share what you're building, or tell us what you'd like your assistant to be able to do next. To learn even more about SurrealDB MCP, please check out our MCP docs .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/surrealdb/empower-your-agents-with-the-new-surrealdb-mcp-m10

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
