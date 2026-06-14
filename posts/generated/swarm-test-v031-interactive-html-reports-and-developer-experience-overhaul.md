---
title: "swarm-test v0.3.1 — Interactive HTML Reports and Developer Experience Overhaul"
slug: "swarm-test-v031-interactive-html-reports-and-developer-experience-overhaul"
author: "suraj kumar"
source: "devto_python"
published: "Sun, 14 Jun 2026 19:15:30 +0000"
description: "Major update to swarm-test — the open-source multi-agent reliability testing tool. The problem with CLI output: tools dump everything. You run the test, get ..."
keywords: "swarm, critical, test, findings, agent, agents, everything, you"
generated: "2026-06-14T19:44:48.275771"
---

# swarm-test v0.3.1 — Interactive HTML Reports and Developer Experience Overhaul

## Overview

Major update to swarm-test — the open-source multi-agent reliability testing tool. The problem with CLI output: tools dump everything. You run the test, get 200 lines, and scroll back trying to find what matters. For CI scripts, you need one line. For debugging, you need everything. For daily use, you need something in between. Most tools pick one mode. That's wrong. swarm-test v0.3.1 adds three output modes: Default — first line is the verdict: "Swarm Score: 0/100 — CRITICAL (5 critical, 1 high findings)" followed by only CRITICAL and HIGH findings with actionable fixes. Lower-severity findings hidden with a note. Quiet (--quiet) — one line only. "Swarm Score: 10/100 — CRITICAL (2 critical findings)". Exit code does the rest. 0 = pass. 1 = threshold exceeded. Perfect for CI scripts. Verbose (--verbose) — everything. All findings including LOW and INFO. Full graph metrics. All agent health details. Complete redundancy table. Every finding now ends with a specific fix, not just a problem statement: CRITICAL | cascade_failure Catastrophic cascade potential: Hub failure cascades to 5 agents → Add a fallback agent for 'Hub' or distribute its responsibilities across multiple agents. The big addition is the interactive HTML report. Run: swarm-test run crew.py --output-format html --output-path report.html --open Your browser opens with a full dashboard: Swarm Score Gauge — large circular gauge showing 0-100 with certification level (EXCELLENT, GOOD, NEEDS IMPROVEMENT, AT RISK, CRITICAL). One look tells you the state of your system. Agent Interaction Graph — D3 force-directed graph. Nodes are agents, sized by connections, colored by health (green/yellow/red). SPOF agents get a pulsing red border. Drag to reposition, scroll to zoom, click to highlight edges. Interaction Heatmap — NxN grid showing which agent pairs communicate most. Darker = more interactions. Red overlay = findings on that edge. Instantly see where the risky connections are. Health Scores Table — sortable with colored progress bars. Each agent shows its score, status, and specific risk details like "100% blast radius, SPOF, high cascade depth." Redundancy Table — replaceability scores from IRREPLACEABLE (0-20) to FULLY REDUNDANT (81-100). SPOFs highlighted in red with green progress bars for safe agents. Findings Section — filter buttons (ALL / CRITICAL / HIGH / MEDIUM / LOW). Each finding is collapsible — click to expand for full description, affected agents, and remediation steps. Everything else still works. Same 8 reliability tests (cascade failure, context leakage, intent drift, collusion detection, blast radius, timeout resilience, sensitive data detection, contract violation). Same 3 framework adapters (CrewAI, LangGraph, AutoGen). Same YAML config with auto-discovery. Same GitHub Action for CI/CD gating. Same JSON and Markdown exports. Nothing removed, everything improved. Install: pip install swarm-test --upgrade What's next: plugin system — write your own custom reliability tests with a simple BasePlugin interface. GitHub: github.com/surajkumar811/swarm-test

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/suraj_kumar_96bb8767435e2/swarm-test-v031-interactive-html-reports-and-developer-experience-overhaul-45d4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
