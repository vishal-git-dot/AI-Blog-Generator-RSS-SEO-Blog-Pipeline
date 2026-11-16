---
title: "Show HN: Coral – Open-source gateway where agents write their own tools"
slug: "show-hn-coral-open-source-gateway-where-agents-write-their-own-tools"
author: "jcs"
source: "hackernews"
published: "Mon, 16 Nov 2026 14:14:51 +0000"
description: "Hi HN, I'm James, one of the co-founders of Coral. Coral is an open-source, self-hosted gateway that sits between your agents and the systems they work on. A..."
keywords: "tools, coral, custom, agents, can, agent, https, com"
generated: "2026-11-16T15:22:11.704761"
---

# Show HN: Coral – Open-source gateway where agents write their own tools

## Overview

Hi HN, I'm James, one of the co-founders of Coral. Coral is an open-source, self-hosted gateway that sits between your agents and the systems they work on. Agents call tools by writing short TypeScript programs that they can save as custom tools to reuse. You can publish custom tools for groups of agents, so your team’s library of tools adapts to your unique systems, data and use cases. Custom tools help agent performance and give more precise units of permission control. Here’s a short demo: https://www.youtube.com/watch?v=p0PKOlHLyVI We started on this while building an AI SRE. To investigate an incident, the agent had to connect the dots across an ocean of telemetry data and undocumented relationships across internal and external systems. It took broad permissions, a lot of tokens and it would start from scratch the next time. We built Coral so that the agent remembers the route. Once a task succeeds, the agent writes the steps that worked into a program and saves it as a custom tool. Next time, the agent finds that custom tool in the same search as standard provider tools (e.g. Datadog, Slack), and reuses it. It started with SRE, but we (and our early users) now use Coral for agent work across the org. For our tasks across GitHub, Linear and Slack with Opus 5.5, custom tools help agents work 29% faster, at 31% lower cost (tasks here: https://withcoral.com/docs/examples/custom-tools ). Coral builds on code mode, adding custom tools, policy controls and managed identities. Each program runs in a V8 isolate with no network access or credentials. Coral checks every tool call against workspace policy before attaching credentials and forwarding it to the provider. You can configure each provider to use the caller’s own account, so teammates can share tools without sharing API tokens. (e.g. https://withcoral.com/blog/slackbot-works-better-with-coral ) Coral is written in Rust, and you can run it as a desktop app or as a shared server. The core is Apache 2.0 and has no limits on users, agents or volume. Everything I've described here is in the OSS edition. SAML, SCIM, and org-wide governance features will be available soon under an enterprise licence. We'd love for you to try it and share your feedback. You can download it here https://withcoral.com/download . I'll be in the comments here and on Slack: https://withcoral.com/slack Comments URL: https://news.ycombinator.com/item?id=50517803 Points: 34 # Comments: 9

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://github.com/withcoral/coral

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
