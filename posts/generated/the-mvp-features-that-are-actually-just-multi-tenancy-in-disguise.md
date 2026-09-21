---
title: "The MVP Features That Are Actually Just Multi-Tenancy in Disguise"
slug: "the-mvp-features-that-are-actually-just-multi-tenancy-in-disguise"
author: "MACROGEN"
source: "devto_webdev"
published: "Mon, 21 Sep 2026 21:31:57 +0000"
description: "When people talk about "MVP scope," it's usually framed as a features conversation — what to cut, what to keep, what can wait until v2. But some of the decis..."
keywords: "one, what, customer, mvp, just, decisions, small, you"
generated: "2026-09-21T21:51:47.200314"
---

# The MVP Features That Are Actually Just Multi-Tenancy in Disguise

## Overview

When people talk about "MVP scope," it's usually framed as a features conversation — what to cut, what to keep, what can wait until v2. But some of the decisions hiding inside that conversation aren't really about features at all. They're architecture decisions wearing a feature costume, and they're a lot more expensive to walk back than a UI tweak. Here are a few that show up disguised as "small" scope questions. "Can users belong to more than one workspace?" This sounds like a small toggle. It's actually a foundational question about how you model the relationship between users and tenants. Bolt this on after launch and you're often looking at a schema migration touching every table that references a user, not just adding a join table. If there's any chance of this in year one, it's worth deciding the data model up front even if the UI for it ships later. "Do we need custom roles per customer?" Early on, "admin" and "member" covers almost everyone. Then one enterprise prospect asks for a "billing viewer who can't touch settings" and the two-role system doesn't bend easily. Permissions systems are one of those things that are far cheaper to build with some flexibility from the start (even if you expose only two roles at launch) than to retrofit once real customers depend on the existing behavior not changing. "Should each customer get a subdomain?" This one seems cosmetic — acme.yourapp.com feels like a branding nice-to-have. But once you commit to subdomain-based tenancy, it touches routing, SSL certificate provisioning, session handling, and sometimes your auth flow. Deciding this after a handful of customers are already live on a shared URL structure means a migration, not a config change. "What happens when a customer wants to export everything and leave?" Nobody wants to build this for an MVP, understandably. But designing your data model with clean tenant boundaries from day one makes an eventual export/delete flow straightforward. Design it without that boundary, and "delete this one customer's data" turns into a research project through years of accumulated joins and shared tables. "Do we support one plan or several?" A single flat price is the right call for validating an MVP. The trap is baking that assumption into billing logic in a way that assumes exactly one price forever — no fields for plan tier, no separation between "what a customer is billed" and "what a customer is entitled to." That separation costs almost nothing to add early and saves a rebuild later. Not over-engineering — just noticing the disguise None of this means over-engineering the MVP — the goal is still to ship something small and learn fast. It just means noticing which "small" decisions are actually architecture decisions before they get made by default. Macro-Gen helps SaaS teams work through exactly this kind of scoping before the first migration gets written.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/macrogenltd/the-mvp-features-that-are-actually-just-multi-tenancy-in-disguise-439d

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
