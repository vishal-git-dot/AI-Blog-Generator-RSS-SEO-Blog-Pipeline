---
title: "The tool name lies, so I tier the action inside: how my desktop AI companion gates MCP calls"
slug: "the-tool-name-lies-so-i-tier-the-action-inside-how-my-desktop-ai-companion-gates-mcp-calls"
author: "Krish Verma"
source: "devto_ai"
published: "Sat, 24 Oct 2026 10:25:22 +0000"
description: "The tool name lies, so I tier the action inside: how my desktop AI companion gates MCP calls The scariest bug I have fixed in Ankita was not a crash. It was ..."
keywords: "tier, action, ask, not, tool, mcp, one, default"
generated: "2026-10-24T10:39:36.555409"
---

# The tool name lies, so I tier the action inside: how my desktop AI companion gates MCP calls

## Overview

The tool name lies, so I tier the action inside: how my desktop AI companion gates MCP calls The scariest bug I have fixed in Ankita was not a crash. It was a permission that was never asked for. Ankita, my open-source desktop AI companion, can connect external apps through MCP — Gmail, calendars, and the rest — via Composio. The old approval rule was binary: a tool with readOnlyHint: true skipped the gate, everything else asked, and a trusted server skipped it entirely. Composio was trusted. So a connected Gmail could send mail with no prompt at all. Sending is the one action you cannot undo, and the recipient sees it. That is the worst possible action to get wrong. So I replaced the binary rule with explicit tiers, in src/integrations/mcp-tiers.mjs . The decision is inspectable, and the user sees the real action, not the wrapper's name. The four tiers Tier 0 — auto-allow: read-only tools. Tier 1 — ask once: the default for an unclassified tool. Tier 2 — always ask: destructive verbs. Tier 3 — deny: only ever from an explicit blocklist entry. The resolution order is fixed: blocklist, then an explicit per-tool rule, then a per-app rule, then an app default, then the heuristic. Tier 3 is only reachable through the blocklist, so a heuristic can never silently deny something. That is deliberate: a heuristic guessing wrong should cost a prompt, never a blocked workflow the user cannot explain. The tool name is the least trustworthy part The hard case is Composio's meta-tools. COMPOSIO_MULTI_EXECUTE_TOOL takes a list of real tools in its arguments, so the name on the call tells the user nothing. Showing "approve COMPOSIO_MULTI_EXECUTE_TOOL?" would be asking them to sign a blank cheque. enclosedActions() unwraps it instead. Each entry's slug is split by splitSlug() — GMAIL_SEND_EMAIL becomes app gmail , action send email — and the tier that matters is the worst one enclosed. One destructive action in a batch of ten reads lifts the whole call to always-ask. The user is then shown describeCall() output — "gmail: send email" — never the meta-tool name. Discovery tools ( COMPOSIO_SEARCH_TOOLS , COMPOSIO_GET_TOOL_SCHEMAS ) stay auto-allow: they read metadata and perform no app action, so there is nothing meaningful to approve. Connection management gets the same treatment. Adding a connection is ask-once, because the user is already watching the OAuth flow. Removing one is always-ask, because it destroys working setup. Why substring matching, and why Gmail starts locked down Destructive verbs — send , delete , publish , pay , transfer , remove , destroy , revoke — are matched as substrings, so payment and resend count. A false positive only costs an extra prompt, and asking is already the default, so there is no reason to risk a false negative by insisting on word boundaries. I would rather over-ask than under-ask on the irreversible actions. Mail gets its own default on top of that. New Composio connections start with Gmail at always-ask instead of inheriting the generic default. Reads stay harmless; the send path never does. That one default is the direct fix for the original bug: the trusted-server shortcut is gone, and the highest-regret app starts at the strictest tier a heuristic can assign. The policy lives outside the server list, on purpose Explicit overrides live in mcp-tiers.json , deliberately not in the MCP server record. Composio is a synthetic connection that never appears in mcp.json , and adding a command-less record there would make the reconciler try to spawn a process that does not exist. A separate file keeps the policy generic across every server. Two details matter here. First, the policy is re-read before every write, because the CLI and a running daemon each hold their own copy — otherwise the last writer silently wins. Second, a missing or malformed policy file falls back to heuristics rather than failing: the tiers degrade to ask-by-default, not to allow-by-default. Lowering a tier is itself approval-worthy ( lowersProtection() treats an unset tier as ask-once, so auto-allowing anything previously unclassified counts as a downgrade), and every decision bumps an audit counter — allowed, asked, denied — so "why did it send that mail?" has an answer on disk. What this does not solve This is classification, not a sandbox. A tier-0 tool is only as read-only as its readOnlyHint annotation claims, and that annotation comes from the server itself. A lying annotation is a gap this design does not close. And the heuristic's ceiling is ask-once for anything unknown: a novel destructive verb that is not in the list gets one prompt and then runs, not a permanent always-ask. Those are the two places I would most like to be proven wrong. So here is the design question, written before the rest of this article: one destructive action lifts a whole multi-execute batch to always-ask — is that the right granularity, or should each enclosed action get its own prompt, even at the cost of prompt fatigue? The worst-action rule is simple and safe, but it treats a batch of nine reads and one send as if it were ten sends. Per-action approval would be more precise and much noisier. Which failure would you rather ship? Ankita is open-source (MIT) and local-first: github.com/akyourowngames/A.N.K.I.T.A — a little companion, a lot more possible. If you have connected MCP servers to your own assistant, I would genuinely like to hear how you gate them: what does your tier system do with a tool whose name hides the action?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/krish_verma_77e28d3fd63ca/the-tool-name-lies-so-i-tier-the-action-inside-how-my-desktop-ai-companion-gates-mcp-calls-3do9

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
