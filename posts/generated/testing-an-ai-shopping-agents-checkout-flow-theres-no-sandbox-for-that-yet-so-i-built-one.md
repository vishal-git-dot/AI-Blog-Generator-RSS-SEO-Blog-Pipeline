---
title: "Testing an AI shopping agent's checkout flow? There's no sandbox for that yet — so I built one"
slug: "testing-an-ai-shopping-agents-checkout-flow-theres-no-sandbox-for-that-yet-so-i-built-one"
author: "sms-florin"
source: "devto_webdev"
published: "Wed, 26 Aug 2026 06:46:59 +0000"
description: "If you're building or evaluating an AI agent that can shop and check out on its own, you've probably run into the new "agentic commerce" protocols: ACP (Open..."
keywords: "acp, agent, you, sandbox, merchant, com, real, https"
generated: "2026-08-26T06:57:10.997141"
---

# Testing an AI shopping agent's checkout flow? There's no sandbox for that yet — so I built one

## Overview

If you're building or evaluating an AI agent that can shop and check out on its own, you've probably run into the new "agentic commerce" protocols: ACP (OpenAI + Stripe + Meta), AP2 (Google), and UCP. They define how an agent talks to a merchant to create a checkout session, apply a payment token, and get an order back. Stripe's own test mode covers the payment half fine — test cards, test API keys. But there's no hosted "fake merchant" you can point your agent at to verify the protocol half: does your agent correctly create a session, handle a 422 idempotency conflict, parse the order response, retry politely? You either mock it yourself from the spec, or risk finding out against a real merchant. So I built acp-sandbox — a small hosted mock merchant implementing the ACP checkout API, live at https://acp-sandbox.flo-voice1.com . What it does It implements the real checkout_sessions lifecycle from ACP's 2026-04-17 spec : create, retrieve, update, complete, cancel. Responses match the actual CheckoutSession / Order / Error schemas for the fields it supports — I pulled the OpenAPI spec directly rather than guessing field names. # get a test key, no signup curl -X POST https://acp-sandbox.flo-voice1.com/keys \ -H "Content-Type: application/json" -d '{"email":"you@example.com"}' # create a session against the demo catalog curl -X POST https://acp-sandbox.flo-voice1.com/checkout_sessions \ -H "Authorization: Bearer acps_test_..." \ -H "Content-Type: application/json" \ -d '{"line_items":[{"id":"item_demo_headphones","quantity":1}],"currency":"usd"}' Every request/response is logged per API key ( GET /logs ), so you can see exactly what your agent sent when something doesn't work. What it deliberately doesn't do (yet) No real payment processing — complete always succeeds once you send any payment_data . No OAuth delegate_authentication flow. No fulfillment options (shipping/pickup) — every session goes straight to ready_for_payment . Fixed demo catalog (4 items), not a real product feed — feed ingestion is a merchant-onboarding concern, not something your checkout-testing agent needs to exercise. ACP is still beta (5 spec revisions in about 7 months), so this will need upkeep as the protocol moves. Scoped tightly on purpose rather than trying to cover AP2/UCP too — happy to extend it if there's real interest. If you're also building agent-identity-mcp or similar (disposable email/phone for AI agents to use as a buyer identity), it pairs directly with this — identity on one side, a merchant to check out with on the other. Repo: https://github.com/flovoice53-tech/acp-sandbox Live: https://acp-sandbox.flo-voice1.com

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/flovoice53tech/testing-an-ai-shopping-agents-checkout-flow-theres-no-sandbox-for-that-yet-so-i-built-one-dgo

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
