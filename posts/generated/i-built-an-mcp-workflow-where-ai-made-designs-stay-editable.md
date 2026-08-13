---
title: "I built an MCP workflow where AI-made designs stay editable"
slug: "i-built-an-mcp-workflow-where-ai-made-designs-stay-editable"
author: "Simon Siegenthaler"
source: "devto_webdev"
published: "Thu, 13 Aug 2026 13:14:14 +0000"
description: "Most visual tools give an AI agent a single useful action: generate an image. That works until the image is almost right. The headline has one wrong word. Th..."
keywords: "mcp, picorn, product, agent, text, tools, image, headline"
generated: "2026-08-13T13:23:07.313652"
---

# I built an MCP workflow where AI-made designs stay editable

## Overview

Most visual tools give an AI agent a single useful action: generate an image. That works until the image is almost right. The headline has one wrong word. The product crop needs to move 20 pixels. The CTA is behind the subject. If the result is a flat PNG, the agent has no real objects to change. It has to regenerate the whole thing and hope the next version is better. I've spent the last three years building Picorn , and this became the main design constraint for its MCP: the agent should create a document, not a dead-end picture. What the agent needs back For a social post, the useful output isn't just a render. It is a small object model: a background a transparent product image a headline text layer a CTA text or shape layer explicit stacking order and positions Each object needs a stable ID. The agent can then say “move the product behind the headline” or “change only the CTA” and address the same object again. The render is still important, but it becomes a preview of the document rather than the source of truth. The workflow I ended up with Claude, Cursor or Codex receives the campaign brief. It calls Picorn through MCP and creates a project with real layers. It renders a preview to inspect the composition. The same project opens in a browser editor. A person can change the crop, text, colour, order or spacing without starting over. Publishing and scheduling stay behind an explicit approval step. That last step matters. An agent can prepare a campaign, but a generated result shouldn't silently appear on a connected social account. A prompt I use to test the boundary looks like this: Create a 1080x1080 product post. Keep four named layers: background, product PNG, headline and CTA. Do not rasterize the text. Put the product behind the headline, render a preview, and return the editable project URL. Do not publish anything. This is a much better test than “make a beautiful Instagram post.” It checks whether the connector exposes actual editing primitives or simply relays another image-generation prompt. Why I exposed small tools Picorn's public MCP currently exposes 30 tools. They cover projects, text, images, SVG and shape layers, grouping, alignment, ordering, video timelines, rendering and project handoff. A single make_campaign tool would be easier to demo. It would also hide the structure the agent needs when the first result isn't correct. Small tools let the model inspect and repair one part of the document. The tradeoff is that the tool descriptions and IDs must be consistent. If the agent can't understand what already exists, more tools only create more ways to fail. Keeping the approval boundary clear The browser editor is not a fallback for when the AI fails. It is part of the workflow. Generation is good at getting from a blank page to a plausible direction. A person is still better at judging whether the product is too small, whether the claim is honest and whether the design actually fits the brand. So the useful loop is: brief -> structured draft -> render -> human correction -> approval -> publish Not: brief -> generated image -> automatic post Trying the MCP The endpoint uses Streamable HTTP and doesn't require an API key. Claude Code: claude mcp add --transport http picorn https://picorn.com/mcp Codex: codex mcp add picorn --url https://picorn.com/mcp Cursor: { "mcpServers" : { "picorn" : { "url" : "https://picorn.com/mcp" } } } Full disclosure: I build Picorn. The public MCP is free to try. It still needs a manual art-direction pass for many real product layouts, and Picorn isn't yet the right fit for complex enterprise approval chains. I'm most interested in examples where the document/edit loop breaks after a seemingly successful first render. AI disclosure: I used an AI assistant to help edit this article and verify the setup snippets. I reviewed the final text and every product claim.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/cueqzapper/i-built-an-mcp-workflow-where-ai-made-designs-stay-editable-2513

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
