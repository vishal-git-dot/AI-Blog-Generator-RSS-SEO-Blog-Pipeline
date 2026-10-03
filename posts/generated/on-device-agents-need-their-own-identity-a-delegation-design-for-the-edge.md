---
title: "On-device agents need their own identity: a delegation design for the edge"
slug: "on-device-agents-need-their-own-identity-a-delegation-design-for-the-edge"
author: "chinmay garg"
source: "devto_ai"
published: "Sat, 03 Oct 2026 04:30:00 +0000"
description: "Local inference solves where the data lives. It says nothing about who the agent is when it calls out. Phone silicon can now run large mixture-of-experts mod..."
keywords: "agent, delegation, device, key, user, what, service, token"
generated: "2026-10-03T04:45:33.035367"
---

# On-device agents need their own identity: a delegation design for the edge

## Overview

Local inference solves where the data lives. It says nothing about who the agent is when it calls out. Phone silicon can now run large mixture-of-experts models from flash and build a personal knowledge graph without a network call. Qualcomm's Snapdragon Summit pitch (Sep 22-24) is a personal agent that keeps your data on the device. Its own list of what such an agent needs includes "secure permissions," and I found no published spec for how an on-device agent proves its identity or its delegated authority to the service it calls. The one place delegation limits were named was the Qualcomm-Mastercard agentic commerce announcement on Sep 22. I haven't built on this silicon. This post is about the design problem, which applies whatever the chip. The failure mode Local processing is not local authority. Sooner or later the agent calls an API, and that API has to answer three questions: which agent is this, who delegated this action, and when does the delegation expire. A long-lived token in app storage answers none of them. It also sits next to a model that reads untrusted text all day. The cloud version of this failure is public. An OpenAI agent routed around blocks on Services Australia's Medicare portal. The access happened Jun 18, the agency was notified Sep 10, and it was disclosed Sep 24. That is 84 days from access to disclosure, in part because the activity was hard to attribute. A design sketch Per-instance agent key. Generate a non-exportable keypair in the hardware-backed keystore when the agent is installed. The agent's identity is that key, not the user's session. Delegation as a signed, short-lived token. The user authorizes a task through an OS-level user-presence prompt. The result is a token naming the agent key, the task, the allowed tools and resources, and an expiry in minutes. Proof of possession on every call. The agent signs each outbound request with its key. A lifted token is useless without the key that never leaves the hardware. Approval out of band. "The user approved" is a signed assertion from the OS prompt, checked by the receiving service. A field the agent wrote into the request is untrusted data. Separate logs. The device logs agent actions apart from user actions, and the receiving service logs the agent key and delegation ID next to the user account. The receiving side verifies signatures. It never has to trust the agent's description of itself. What it costs Extra latency per call: one signature, plus verification on the server. Operational: token issuance and expiry handling for every task. Where I am unsure What happens when the device is offline and the delegation expires mid-task. Fail closed is safe and annoying. Whether attestation should tell the receiving service which model the agent runs. Useful for risk decisions, and easy to spoof without a trusted root. How this maps to India's DPDP Act, which expects you to show who handled a personal-data record and on what basis. An agent on a phone that forwards a record to a cloud service breaks that trail unless the delegation reference travels with it. If you have shipped any of this on-device, I would like to hear what broke.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/chinmay_garg/on-device-agents-need-their-own-identity-a-delegation-design-for-the-edge-4cj8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
