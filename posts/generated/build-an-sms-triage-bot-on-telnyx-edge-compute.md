---
title: "Build an SMS Triage Bot on Telnyx Edge Compute"
slug: "build-an-sms-triage-bot-on-telnyx-edge-compute"
author: "Sonam"
source: "devto_ai"
published: "Thu, 13 Aug 2026 18:58:07 +0000"
description: "Support SMS inboxes are usually a routing problem before they are an AI problem. Someone asks about billing. Someone else needs technical support. A third pe..."
keywords: "telnyx, sms, triage, agent, https, com, route, history"
generated: "2026-08-13T19:08:38.061926"
---

# Build an SMS Triage Bot on Telnyx Edge Compute

## Overview

Support SMS inboxes are usually a routing problem before they are an AI problem. Someone asks about billing. Someone else needs technical support. A third person wants to talk to sales. The app has to understand the message, pick the right destination, reply to the customer, and remember what happened. This TypeScript example does that on Telnyx Edge Compute with the Agent SDK. Code: https://github.com/team-telnyx/telnyx-code-examples/tree/main/agent-sms-triage-bot What it builds agent-sms-triage-bot receives inbound SMS webhooks, classifies each message into one of four topics, looks up the route for that topic, replies by SMS, and stores triage history in durable actor state. The topics are: billing support sales general The default route table maps those topics to queue names: billing -> billing-queue support -> support-queue sales -> sales-queue general -> general-queue The request flow Inbound SMS -> POST /webhooks/sms -> TriageAgent.triage(from, text) -> Telnyx AI Inference classifies topic -> durable route table lookup -> SMS reply -> triage history update The app uses one TriageAgent actor per inbound number. That actor stores route rules, recent history, total messages, and topic counts. The main routes POST /webhooks/sms receives Telnyx message.received events POST /debug/triage simulates inbound SMS POST /routes updates the route table GET /routes lists route rules GET /history returns recent triage history GET /debug/state inspects actor state GET /health/liveness and GET /health/readiness provide health checks The Agent SDK piece The core class is TriageAgent . It extends the Agent SDK Agent class and uses durable state for: route table triage history total message count topic counts The AI classification call uses the Telnyx binding: const completion = await this . env . TELNYX . ai . openai . chat . createCompletion ({ model : this . env . AI_MODEL || " moonshotai/Kimi-K2.6 " , messages : [ { role : " system " , content : CLASSIFY_SYSTEM_PROMPT }, { role : " user " , content : `Customer message: " ${ text } "` }, ], max_tokens : 2000 , temperature : 0.2 , }); The SMS reply uses the same binding pattern: await this . env . TELNYX . messages . send ({ from : state . fromNumber || state . phoneNumber , to : from , text : replyText , }); That means the example does not hardcode an API key in application code. Messaging and inference both go through this.env.TELNYX . Try the debug endpoint After deploying with telnyx-edge ship , you can test without sending a real SMS: curl -X POST https://agent-sms-triage-bot-< id > .telnyxcompute.com/debug/triage \ -H "Content-Type: application/json" \ -d '{"from":"<customer-number>","to":"<triage-number>","text":"Why was I charged twice this month?"}' Example response: { "action" : "triaged" , "from" : "<customer-number>" , "to" : "<triage-number>" , "text" : "Why was I charged twice this month?" , "topic" : "billing" , "route" : "billing-queue" , "confidence" : 0.95 } Then inspect the actor history: curl "https://agent-sms-triage-bot-<id>.telnyxcompute.com/history?number=<triage-number>" Why this pattern is useful For a small support workflow, this keeps the first version compact: Telnyx Messaging receives and sends SMS Telnyx AI Inference classifies intent Edge Compute hosts the webhook Agent SDK durable state stores routing memory You can later replace queue names with real integrations: Slack, Zendesk, Salesforce, email, or an internal queue. Production notes Before using this with real customer traffic, I would add: webhook signature verification SMS opt-out and consent handling duplicate webhook idempotency PII redaction and retention controls role-based route updates human review for low-confidence classifications alerting when outbound SMS fails Resources: Code: https://github.com/team-telnyx/telnyx-code-examples/tree/main/agent-sms-triage-bot Agent SDK docs: https://developers.telnyx.com/docs/agent-sdk Edge Compute docs: https://developers.telnyx.com/docs/edge-compute Messaging docs: https://developers.telnyx.com/docs/messaging Telnyx AI Inference docs: https://developers.telnyx.com/docs/inference Telnyx AI skills and toolkits: https://github.com/team-telnyx/ai

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sonam_50a41a4ced7e6b4f3fa/build-an-sms-triage-bot-on-telnyx-edge-compute-4gin

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
