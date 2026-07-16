---
title: "Launch HN: Traceforce (YC S26) – Company-wide security monitoring for AI apps"
slug: "launch-hn-traceforce-yc-s26-company-wide-security-monitoring-for-ai-apps"
author: "XiaHua"
source: "hackernews"
published: "Thu, 16 Jul 2026 16:52:16 +0000"
description: "Hey HN, we’re Xia and Varun, the founders of Traceforce ( https://www.traceforce.ai/ ). Traceforce provides visibility and control over AI apps such as ChatG..."
keywords: "traceforce, security, company, device, mcps, apps, https, all"
generated: "2026-07-16T19:20:26.280992"
---

# Launch HN: Traceforce (YC S26) – Company-wide security monitoring for AI apps

## Overview

Hey HN, we’re Xia and Varun, the founders of Traceforce ( https://www.traceforce.ai/ ). Traceforce provides visibility and control over AI apps such as ChatGPT, Claude etc directly on all devices (laptops, sandboxes, virtual machines) by discovering not just which apps are being used but also how they are connected to other data sources via MCPs. We also have an open-source dynamic MCP pentesting tool https://github.com/traceforce/mcp-xray to detect vulnerable MCPs. The purpose of Traceforce is to: - Give a company’s employees a standardized way to ensure that AI software running on their device is operating safely - Give the company’s security team visibility of the activities of AI software on the company’s devices, and to detect and prevent unsafe actions and security breaches as early as possible. How Traceforce works 1. Traceforce is installed on each device as a lightweight binary and browser extension. 2. Within 30 minutes, the device is uploading live data to the company profile, displaying all the AI agents/apps running across all company devices on a dashboard. 3. Company security staff can monitor the activity of all the agents in real time, implement controls, and be alerted to any security risks as soon as they arise. Here’s the video demo: https://youtu.be/IdK2WKg7kaM The inspiration for Traceforce came via Xia’s experience as Director of Engineering at a startup called Clumio (which was acquired by Commvault in Oct 2024). Being able to monitor how team members are using AI without slowing them down was a top priority at Clumio. After speaking with 50+ CISOs and CIOs, it became clear that this is a much-needed solution right now across industries. We keep hearing that new AI features are being adopted so quickly and so broadly that visibility and control just can't keep up. Traceforce is transparent about what we monitor and collect. By default, Traceforce collects only metadata and telemetry about the AI applications, MCPs, and tools running on a device. Security teams can enable options to inspect tool calls for the purpose of detecting, warning on, or blocking predefined high-risk or potentially destructive actions. All content inspection happens locally on the device. User prompts are never stored unless explicitly configured by the organization's security administrators. We work closely with end-users of the product, and once they understand what is being monitored/shared, they actually have great comfort that they have a powerful layer of protection on their device to prevent security incidents. It enables them to just focus on their work without worrying about what leaks and breaches may be happening under the hood without their awareness. The Traceforce binary is built using Go and the browser extension is written in Node JS. The hardest part is building a complete connectivity graph between AI applications, MCPs, and tools, then identifying the vulnerabilities and attack paths introduced by those connections. Traditional security tools fall short: EDRs see processes, CASBs see network traffic, but neither has visibility into the application-level activity happening inside AI apps. The way we got it to work was by understanding the configurations and logs of each and every app. It’s a labor intensive process because every app is different and AI features change frequently. Traceforce is currently deployed across more than 1,000 devices at 10 organizations. On average, we discover over 15 AI applications per device with each application connected to 5-10 MCPs. We've helped customers identify exposed plaintext secrets in MCP configurations, prevent API keys from leaking through AI-generated code, and warn developers before executing potentially destructive commands such as “DROP TABLE”. Our "warn and acknowledge" approach has been especially well received, giving developers the freedom to work while helping them avoid costly mistakes. We're looking to work with security, IT, and AI platform teams at small to medium enterprises (200+ employees) that are rapidly adopting AI coding assistants, ChatGPT, Claude, and MCPs. If you're struggling to understand what AI tools people use to boost their productivity or need a practical way to reduce AI-related security risk without slowing folks down, we'd love to talk. You can get started with a free trial at https://www.traceforce.ai or reach out directly to schedule a demo and discuss your environment. Comments URL: https://news.ycombinator.com/item?id=48937020 Points: 15 # Comments: 6

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://news.ycombinator.com/item?id=48937020

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
