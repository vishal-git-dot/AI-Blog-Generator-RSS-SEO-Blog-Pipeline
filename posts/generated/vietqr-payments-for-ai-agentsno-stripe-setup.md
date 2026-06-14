---
title: "VietQR Payments for AI Agents—No Stripe Setup"
slug: "vietqr-payments-for-ai-agentsno-stripe-setup"
author: "ServicesAI VN"
source: "devto_python"
published: "Sun, 14 Jun 2026 04:26:00 +0000"
description: "VietQR Payments for AI Agents—No Stripe Setup The Problem Building AI agents in Vietnam that need to collect payments? Stripe doesn't support VietQR, and int..."
keywords: "your, agentpay, payment, bank, payments, settlement, vietqr, agents"
generated: "2026-06-14T04:46:39.565318"
---

# VietQR Payments for AI Agents—No Stripe Setup

## Overview

VietQR Payments for AI Agents—No Stripe Setup The Problem Building AI agents in Vietnam that need to collect payments? Stripe doesn't support VietQR, and integrating traditional payment gateways means managing API keys, webhooks, and fund settlement delays. Most solutions require your agent to hold or route money through intermediaries. What if your AI could generate a QR code that points directly to your business bank account? Introducing AgentPay VN AgentPay is an open-source (MIT) Python SDK + MCP server that lets Claude, local LLMs, and custom agents collect VietQR payments in three lines of logic: Create a payment request Send the checkout URL to your customer Await settlement confirmation from the bank feed No middleman. No fund holding. The QR points straight to your merchant account. How It Works AgentPay reads your bank's SePay feed to confirm when a payment settles. It doesn't touch the money—it just watches for it. Your AI agent can then trigger downstream workflows (send invoice, unlock feature, etc.) once settlement is confirmed. Installation pip install agentpay-vn Or run the MCP server for Claude Desktop / Code: pip install agentpay-mcp Quick Example from agentpay import AgentPayClient client = AgentPayClient ( api_key = " your_api_key " , merchant_id = " your_merchant_id " ) # Step 1: Create payment request payment = client . create_payment_request ( amount = 100000 , # 100K VND description = " AI consulting session " , order_id = " order_12345 " ) print ( f " Checkout URL: { payment . checkout_url } " ) # Share with customer → they scan QR → money hits your bank # Step 2: Poll for settlement import time while True : status = client . get_payment_status ( payment . id ) if status . settled : print ( " ✓ Payment confirmed! Triggering downstream workflow... " ) break time . sleep ( 5 ) MCP Integration Add to your Claude Desktop config ( claude_desktop_config.json ): { "mcpServers" : { "agentpay" : { "command" : "python" , "args" : [ "-m" , "agentpay_mcp.server" ], "env" : { "AGENTPAY_API_KEY" : "your_api_key" , "AGENTPAY_MERCHANT_ID" : "your_merchant_id" } } } } Now Claude can: Generate payment QR codes on demand Check settlement status mid-conversation Chain payments into multi-step workflows Real Use Cases AI Consulting Chatbots : "That analysis will cost ₫500K. [Scan QR]. Thanks! Here's your report." Autonomous Trading Bots : Collect fees when trades execute; settle directly to ops account. AI Content Marketplace : Agent lists content, collects micro-payments, splits revenue—all via QR. Honest Limitations Vietnam-only : Requires a VietQR-compatible bank account. SePay dependency : Settlement confirmation relies on your bank's SePay feed API (not all banks fully supported yet—check docs). Polling model : No real-time webhooks; you'll poll for status updates. Early-stage : Open-source project; production use should include your own monitoring. Get Started GitHub : https://github.com/phuocdu/agentpay-vn Docs + Swagger : https://agentpay.servicesai.vn API Reference : https://agentpay.servicesai.vn/v1/docs AgentPay strips away payment infrastructure complexity so you can focus on what your AI agent does best. No Stripe. No holding accounts. Just QR → Bank → Done. Try it. Open an issue. Build something interesting.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ai_services_f9c382bdb33b9/vietqr-payments-for-ai-agents-no-stripe-setup-3d9f

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
