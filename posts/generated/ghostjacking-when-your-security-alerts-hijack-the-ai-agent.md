---
title: "GhostJacking: when your security alerts hijack the AI agent"
slug: "ghostjacking-when-your-security-alerts-hijack-the-ai-agent"
author: "Beatriz Albernaz"
source: "devto_webdev"
published: "Tue, 15 Sep 2026 11:19:11 +0000"
description: "Tenet Security showed at DEF CON 34 how an attacker can poison the logs and alerts your AI agent already trusts, then wait for the agent to act on them with ..."
keywords: "agent, your, can, tenet, already, those, also, attacker"
generated: "2026-09-15T11:28:03.175654"
---

# GhostJacking: when your security alerts hijack the AI agent

## Overview

Tenet Security showed at DEF CON 34 how an attacker can poison the logs and alerts your AI agent already trusts, then wait for the agent to act on them with its own credentials. Dark Reading's Jai Vijayan covered the research on August 10. Tenet calls the pattern GhostJacking. The agent never bypasses authentication. It uses the access you already gave it. What Tenet actually demonstrated The attack starts in systems your team treats as internal: Cloudflare firewall logs, Datadog alerts, Sentry error reports. An attacker plants instructions in content those systems store verbatim. A blocked HTTP request is enough. The firewall did its job. The log kept the payload word for word. Barak Sternberg, Tenet's CEO, described the Cloudflare case to Dark Reading: an analyst asks an agent to review blocked events, and the block becomes the delivery path. In Tenet's testing, Claude Code followed the planted instructions nine times out of ten on Cloudflare's recommended configuration. In one demo, that path was enough to change DNS settings and take over a domain. They showed the same pattern in Datadog with a fake diagnostic alert that got an agent to run attacker-controlled commands and pull environment secrets. They also showed agent-to-agent spread: a malicious Sentry report that made Sentry's own AI recommend a fix, which a second coding agent then trusted and ran. Tenet's write-up puts the condition in one sentence. An AI reads outside data it trusts, and the same AI can act on it. Where those two meet, the door is open. Why identity controls do not catch this Traditional access control answers two questions: who is this, and are they allowed to touch that system. GhostJacking never fails those checks. The agent authenticates. It stays inside its permission set. The decision to act came from attacker-controlled text sitting in a log your team already considers trusted. That is why SIEM rules built for stolen passwords miss it. There is no unauthorized session to flag. It is also a different problem from the prompt injection most SaaS teams already test for. Those tests usually cover the chat box, the ticket form, the uploaded document. They rarely cover the firewall log, the Datadog title, or the Sentry stack trace that an on-call agent reads every night. What to map before you add another agent Sternberg's inventory question is the useful one: which of your agents reads outside data and can also write or execute? That list is the risk register. For each agent on it, treat any field an outsider can influence as hostile input. User-Agent strings, Referer headers, error messages, log bodies, ticket text, alert titles. Tenet's Nevo Poran is blunt about execution: human approval on writes, no autoruns, no silent shell access. Least privilege still matters. It does not detect the hijack, but it shrinks what a hijacked agent can reach. Short-lived credentials, task-scoped tokens, and a hard split between "read the alert" and "change production DNS" are the practical cuts. If you already run AI features that watch monitoring tools, this is in scope for AI red teaming. The test is whether planted text in an operational source can make the agent call a tool it should only use on a human's say-so. At Faultline Security we test AI agents for European B2B SaaS companies, including the data sources those agents treat as trusted. If an on-call agent can read your logs and also change config, get in touch before someone else writes the alert. The question that matters for your team: which of your AI agents can read outside data and also write or execute? That list is your risk register.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/albernaz_/ghostjacking-when-your-security-alerts-hijack-the-ai-agent-2d8m

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
