---
title: "Grafana MCP: Query Your Dashboards and Metrics Directly from Claude"
slug: "grafana-mcp-query-your-dashboards-and-metrics-directly-from-claude"
author: "curatedmcp"
source: "devto_ai"
published: "Fri, 28 Aug 2026 10:39:32 +0000"
description: "Install guide and config at curatedmcp.com Grafana MCP: Query Your Dashboards and Metrics Directly from Claude Monitoring shouldn't require context-switching..."
keywords: "grafana, your, claude, mcp, data, metrics, dashboards, api"
generated: "2026-08-28T10:48:56.459595"
---

# Grafana MCP: Query Your Dashboards and Metrics Directly from Claude

## Overview

Install guide and config at curatedmcp.com Grafana MCP: Query Your Dashboards and Metrics Directly from Claude Monitoring shouldn't require context-switching. Grafana MCP is the official integration that lets Claude, Cursor, and other AI agents query your Grafana instance directly—dashboards, metrics, alerts, logs, and all—using natural language. Instead of copy-pasting metrics or manually hunting through dashboards while debugging, you ask Claude: "What's happening with API latency right now?" It pulls real data from your Grafana, correlates it with deployment annotations, digs into your Loki logs, and surfaces the root cause in the same conversation. What It Does Grafana MCP connects your AI agent to any Grafana instance (Cloud or self-hosted) with read and write capabilities across your entire observability stack: Query live dashboard panels and retrieve their data Explore metrics from Prometheus, Loki, InflexDB, and other data sources Search and manage alert rules — view states, histories, and configurations Access annotations for incident correlation (deployments, incidents, notes) Run raw queries in PromQL, LogQL, Flux, or your data source's native language Export dashboards as JSON for backup or migration The result: your monitoring becomes conversational. Troubleshooting becomes faster because the AI has direct access to the same observability data you do. How to Install Install via npm: npx -y @grafana/mcp-server Add to your Claude Desktop config: { "mcpServers" : { "grafana-mcp" : { "command" : "npx -y @grafana/mcp-server" , "env" : { "GRAFANA_URL" : "https://your-grafana-instance.com" , "GRAFANA_API_TOKEN" : "your-grafana-api-token" } } } } Generate an API token in Grafana under Admin > API Tokens, then set it as an environment variable. Real-World Use Cases Incident triage in seconds : "The checkout service is slow." Claude queries dashboard latency panels, finds a spike correlating with a recent deploy, checks Loki logs for errors, and suggests rolling back. Data source health checks : Monitor which metrics are stale or missing. Ask Claude to validate data source connectivity and flag gaps before they impact alerting. On-call context building : "Summarize the last 24 hours of API errors and deployments." Claude pulls annotations, alert history, and error logs, giving you a full incident timeline without manual digging. Full install guides for Claude Desktop, Cursor, Windsurf, and more at CuratedMCP .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/curatedmcp/grafana-mcp-query-your-dashboards-and-metrics-directly-from-claude-34gm

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
