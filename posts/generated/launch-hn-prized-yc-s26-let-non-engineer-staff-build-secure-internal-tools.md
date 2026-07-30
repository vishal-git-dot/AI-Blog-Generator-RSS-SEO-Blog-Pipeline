---
title: "Launch HN: Prized (YC S26) – Let non-engineer staff build secure internal tools"
slug: "launch-hn-prized-yc-s26-let-non-engineer-staff-build-secure-internal-tools"
author: "marinoseliades"
source: "hackernews"
published: "Thu, 30 Jul 2026 13:29:03 +0000"
description: "Hi HN, we're Marinos and Hudson, founders of Prized ( https://prized.dev )! Prized lets non-engineer employees describe the internal tool they need and get a..."
keywords: "prized, data, company, internal, tools, tool, built, https"
generated: "2026-07-30T14:15:57.942950"
---

# Launch HN: Prized (YC S26) – Let non-engineer staff build secure internal tools

## Overview

Hi HN, we're Marinos and Hudson, founders of Prized ( https://prized.dev )! Prized lets non-engineer employees describe the internal tool they need and get a full-stack app, wired to their company’s data and deployed behind the company’s sign-in, without them ever juggling API keys or connectors. Here's a demo: https://www.youtube.com/watch?v=730MuYOfZTY The way Prized provides security is by limiting what the agent can reach at the network layer and by keeping credentials out of the sandbox entirely. The sandbox never holds any keys or connector secrets, it only uses scoped session tokens that are stored as opaque placeholders. The real values are swapped into the request headers on our egress proxy. When production data is connected, the sandbox's network policy is set to deny by default so the only path out is via the proxy. Any call the agent makes to an external connector is reviewed by an LLM judge to prevent dangerous operations. Prized is meant for the internal workflows that start as notebooks or spreadsheets but never become real tools because engineering has more important things to work on. One customer’s data scientist pasted in his personal fraud-detection notebook with hardcoded thresholds and all. After a few prompts, it became a published risk console connected to the company’s data with those thresholds turned into UI controls. Earlier today, we got off a call with them and most of their company is using it. To do this, you need to give people the freedom to build without having unaudited access to company systems. We allow admins to scope data to specific users or teams and data access is recorded in an audit log. Each tool is built with its own Postgres schema and role, with queries running via an authenticated SQL gateway as that role. We think Prized sits between products like Lovable and Retool. Lovable makes it easy to generate and host software, but it isn’t designed around distribution with permissions. Retool generally assumes that a technical builder is creating an app for an end user. Prized treats internal tools as shared objects. Anyone in the workspace can see what others have built, fork, and connect different data. For example, one customer’s marketing lead built a promotional analytics tool. A data scientist at the same company then forked it and added confidence intervals with the existing tool as a starting base. This way workspaces become libraries of tools that people can reuse. We’re live and self-serve. Our free tier includes 2 tool builds/month and our Teams tier is $100/month. The Enterprise tier is custom and supports personalized features like on-prem deployment. We're still working out the right boundary between control and freedom. If you've built internal tools before we'd appreciate your feedback! Comments URL: https://news.ycombinator.com/item?id=49109721 Points: 9 # Comments: 0

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://prized.dev

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
