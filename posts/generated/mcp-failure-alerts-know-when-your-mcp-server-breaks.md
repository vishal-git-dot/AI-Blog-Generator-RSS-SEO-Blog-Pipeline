---
title: "MCP Failure Alerts: Know When Your MCP Server Breaks"
slug: "mcp-failure-alerts-know-when-your-mcp-server-breaks"
author: "Docstar"
source: "devto_ai"
published: "Thu, 26 Nov 2026 07:40:07 +0000"
description: "When an AI assistant calls your MCP server and something on your side breaks, nobody tells you. The assistant gets an error, maybe retries, and then tells yo..."
keywords: "your, mcp, api, alerts, docstar, alert, server, you"
generated: "2026-11-26T07:44:38.397671"
---

# MCP Failure Alerts: Know When Your MCP Server Breaks

## Overview

When an AI assistant calls your MCP server and something on your side breaks, nobody tells you. The assistant gets an error, maybe retries, and then tells your user "that didn't work". Your user gives up, and you find out days later, if at all. DocStar's MCP failure alerts fix that: the moment a tool, your token check or your sign-in fails for one of your users, you get an alert on your own webhooks, in a Slack channel or by email, with the request that failed and the response your API gave. This post explains why MCP failures are so easy to miss, what a useful alert should contain, and how to turn alerts on for your DocStar MCP server in a couple of minutes. Why MCP failures go unnoticed A normal API has a dashboard, error logs and users who email support. An MCP server sits between an AI assistant and your API, and that changes who sees the error: The user never sees your error message. The AI assistant reads it and rephrases it, often as a vague apology. The assistant hides the pattern. It may retry, try a different tool, or give up quietly. One broken endpoint can look like the AI "being bad at your product". Sign-in failures look like the user's fault. If your token check refuses every token after a deploy, every user is asked to sign in again, and most simply stop using the connector. So the people who could fix the problem, you and your team, are the last to know. What a useful MCP alert contains An alert that just says "tool failed" sends you digging through logs. A useful one answers five questions straight away: Question Example What happened? "create_order" failed: your API answered 422 What did my users see? The AI got the error back and told the user the action failed. What should I do? A 4xx often means the AI called the tool with wrong inputs: check the tool's description and input examples. Which call failed, exactly? The request sent ( POST https://api.acme.com/v1/orders with its body) and the response (422 in 312 ms, with its body). How often? First time in the last 10 minutes, or "7 more since the last alert". It also has to be safe to send to a chat channel. Passwords, tokens, API keys, cookies and login codes must never end up in Slack. How failure alerts work in DocStar Every DocStar docs and API collection gets its own hosted MCP server. With failure alerts on, that server watches three things on your side: Tools. Your API answers 4xx or 5xx, can't be reached, or a tool's viaSocket flow fails. Your token check. If your MCP server checks users' tokens against your own validation URL, you're told when that URL fails, times out or refuses tokens. Sign-in. Your token URL refuses a login code or refresh, your session exchange fails, or your login page sends users back with an error. Each alert includes what happened, what your users saw, what to do, the API that failed, the request sent and the response received. Secret-looking values show as [hidden] , query strings are removed from URLs, and request headers are never included. To keep the noise down, the same problem is sent at most once every 10 minutes, and the next alert says how many times it happened in between. Problems on DocStar's side, and users who simply haven't signed in yet, never trigger an alert. Where alerts go Pick any mix of three places: Your webhooks. Add up to 9 https URLs. Each gets a POST with the alert as JSON, ready for your incident tool, your own Slack bot or a workflow. The JSON includes a ready-to-read message plus separate fields such as kind , api , request and response . Slack. Connect your workspace and pick a channel. Alerts arrive as a message in that channel. Email. Add up to 20 addresses, with nothing to connect. Alerts arrive from DocStar ( docstar-report@viasocket.com ), and each address gets its own copy, so no one sees the others. Turn it on Open your collection's settings and open the MCP tab. Under Server settings , click Set up next to Failure alerts . Add a webhook, connect Slack or add email addresses. Click Send test alert to check every destination. You see the result for each one. That's it. The next time something on your side breaks for an AI assistant user, you hear about it first. Full details, including the complete webhook payload, are in the Help page: MCP Failure Alerts: Webhooks, Slack and Email . Frequently asked questions Will I get flooded if my API goes down? No. Each problem is sent at most once every 10 minutes, with a count of repeats. Can I send alerts to more than one place? Yes. Add several webhooks, a Slack channel and several email addresses together. Every alert goes to all of them, and one failing destination doesn't stop the others. Are my users' tokens or passwords ever included? No. Values whose name looks like a password, token, API key, cookie or code are hidden, query strings are removed and request headers are never sent. Building an MCP server for your API? Start with DocStar and turn your API docs into an MCP server any AI assistant can use, with failure alerts built in. Originally published on the DocStar blog . Try DocStar free: https://docstar.io

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/docstar_io/mcp-failure-alerts-know-when-your-mcp-server-breaks-48c7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
