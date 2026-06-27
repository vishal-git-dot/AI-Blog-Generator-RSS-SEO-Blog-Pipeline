---
title: "n8n Code node: run JavaScript (or Python) inside your workflows — free examples"
slug: "n8n-code-node-run-javascript-or-python-inside-your-workflows-free-examples"
author: "Pirate Prentice"
source: "devto_webdev"
published: "Sat, 27 Jun 2026 19:23:52 +0000"
description: "The n8n Code node is one of the most powerful tools in n8n. It lets you run raw JavaScript (or Python) inside any workflow — perfect for data transformation,..."
keywords: "json, node, item, input, const, items, return, code"
generated: "2026-06-27T19:36:59.128489"
---

# n8n Code node: run JavaScript (or Python) inside your workflows — free examples

## Overview

The n8n Code node is one of the most powerful tools in n8n. It lets you run raw JavaScript (or Python) inside any workflow — perfect for data transformation, custom logic, or anything the built-in nodes cannot handle. This guide covers everything you need to know: syntax, common patterns, real examples, and a free workflow JSON you can import and run today. What the Code node does The Code node gives you a full JavaScript (Node.js) or Python runtime inside your workflow. You can: Transform or reshape data from a previous node Write custom business logic that no built-in node covers Build or parse structured objects before passing to the next node It runs per item or once for all items — you choose. Basic syntax In Run Once for Each Item mode: // $input.item.json is the current item data const name = $input . item . json . name ; const email = $input . item . json . email ; return { json : { domain : email . split ( ' @ ' )[ 1 ], processedAt : new Date (). toISOString () } }; In Run Once for All Items mode: const items = $input . all (); const total = items . reduce (( sum , item ) => sum + item . json . amount , 0 ); return [{ json : { total , count : items . length } }]; Key rule: always return objects with a json key. 5 real-world Code node patterns 1. Date formatting const d = new Date ( $input . item . json . created_at ); return { json : { ... $input . item . json , date_iso : d . toISOString (). split ( ' T ' )[ 0 ] } }; 2. Flatten a nested object const raw = $input . item . json ; return { json : { id : raw . id , name : raw . customer . name , plan : raw . subscription . plan } }; 3. Filter array (Run Once for All Items) const items = $input . all (); return items . filter ( i => i . json . amount > 100 ). map ( i => ({ json : { ... i . json , tag : ' high-value ' } })); 4. Generate a unique ID const { randomUUID } = require ( ' crypto ' ); return { json : { ... $input . item . json , id : randomUUID () } }; 5. Read data from a named node const webhookData = $ ( ' Webhook ' ). first (). json ; const rows = $ ( ' Google Sheets ' ). all (). map ( i => i . json ); Common mistakes Mistake Fix Returning plain object instead of {json: ...} Always wrap in {json: ...} Forgetting array in All Items mode Wrap return in [...] Using require('axios') Use the HTTP Request node instead Free workflow JSON Drop a comment below and I will share a ready-to-import workflow JSON demonstrating all 5 patterns — runs with the Code node only, no credentials needed. Or grab the full n8n Workflow Starter Pack ($29) with 3 production-ready automations: pirateprentice.gumroad.com Summary The Code node is your escape hatch when no built-in node does exactly what you need. Master the $input API, always return {json: ...} , and you can build virtually any transformation logic inside n8n. What is your most-used Code node pattern? Drop it in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/pirateprentice/n8n-code-node-run-javascript-or-python-inside-your-workflows-free-examples-1oa5

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
