---
title: "Drive a visual site builder with your own Claude/Cursor via MCP"
slug: "drive-a-visual-site-builder-with-your-own-claudecursor-via-mcp"
author: "Mufasa"
source: "devto_webdev"
published: "Mon, 20 Jul 2026 19:40:55 +0000"
description: "I've been building Swebsy , a visual website builder, and last week we shipped something I haven't seen any other builder do. I want to talk about it because..."
keywords: "you, your, agent, already, mcp, their, builder, own"
generated: "2026-07-20T19:49:00.046034"
---

# Drive a visual site builder with your own Claude/Cursor via MCP

## Overview

I've been building Swebsy , a visual website builder, and last week we shipped something I haven't seen any other builder do. I want to talk about it because I think it's a genuinely different way to think about "AI in a builder" — and honestly I'm not sure why nobody else is doing it. The problem with "AI website builders" Look at the current crop. Every one of them bolts an AI chat panel onto their editor and bills you for it. Some markup on top of the raw API tokens, some seat price, some credit system that runs out right when you're in flow. The pitch is always "describe your site and watch it build itself." Two things about that always bugged me: You're paying twice. If you already pay $20/mo for Claude, or you have a Cursor seat, or Copilot through your job — you're already paying for a coding agent. Then the builder charges you again to use their wrapper around a model you're already subscribed to. You don't get to use your agent. You get their agent. Their prompt, their model choice, their context window, their guardrails. If you've spent months tuning how you work with Claude Code or Cursor, none of that comes with you. What we did instead We shipped an MCP server ( @swebsy/mcp ). If you don't know MCP — it's the Model Context Protocol, the open standard for connecting coding agents to tools. Claude Code, Codex, Cursor, Windsurf, Copilot all speak it. So instead of building our own AI panel and metering it, we made Swebsy a tool your existing agent can drive. claude mcp add swebsy -- npx -y @swebsy/mcp That's the whole setup. Now Claude Code (or whatever you use) can read your live canvas, add sections, edit content, take screenshots to check its own work — the same editor you're clicking around in, driven by the agent you already have open. The cost to us of your AI usage: zero. The cost to you: zero extra. You use the plan you're already paying for. Why this feels obviously right (and I don't get why it's rare) No per-token billing. We're not in the loop on model costs at all. Your agent, your subscription, your quota. It runs on your machine. The bridge is a local 127.0.0.1 WebSocket. Your agent talks to your open editor tab. We're not proxying prompts through our servers, secrets stay redacted, nothing gets shipped off to us to bill against. You keep your setup. Your agent, your model, your custom instructions, your muscle memory. We didn't ask you to relearn a new chat box. We dogfooded it. The section on our landing page announcing this feature? An agent built it, live, through the MCP. It's turtles all the way down. The strategic bit, if you're into that: this isn't us claiming to be an "AI website builder." Our core promise is still boring and honest — build visually, export real files, publish where you want. The agent story is a reason to believe , not a new category we're pretending to own. The people it lands with are technical founders who already live in a coding agent all day. We just met them where they already were instead of building a worse version of the tool they already love. The counterintuitive part Every instinct in SaaS says own the AI layer, meter it, that's the margin. And maybe we're leaving money on the table. But metered-AI margin is a rented moat — the second the model gets cheap, the markup evaporates and your users resent every credit. Giving it away feels lazier and it converts better, because the honest pitch writes itself: "use the agent you already pay for." No one else in our space can say that without blowing up their own pricing page. Happy to answer anything about the MCP setup, the local bridge, or how the dogfooding worked. Also genuinely curious — is there a builder out there already doing bring-your-own-agent that I just haven't found? Would love to be wrong about the "nobody" part. — building Swebsy

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mufasawanyama/drive-a-visual-site-builder-with-your-own-claudecursor-via-mcp-19fd

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
