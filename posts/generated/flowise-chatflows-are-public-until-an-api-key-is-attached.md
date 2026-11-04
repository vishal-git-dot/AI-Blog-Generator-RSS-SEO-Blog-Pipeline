---
title: "Flowise chatflows are public until an API key is attached"
slug: "flowise-chatflows-are-public-until-an-api-key-is-attached"
author: "johnettagaweraks"
source: "devto_ai"
published: "Wed, 04 Nov 2026 23:22:09 +0000"
description: "Flowise chatflows are public until an API key is attached Flowise is used to build and run chatflows and agentflows. Its chatflow-level authorization documen..."
keywords: "key, flowise, api, flow, level, app, public, can"
generated: "2026-11-04T23:27:35.558175"
---

# Flowise chatflows are public until an API key is attached

## Overview

Flowise chatflows are public until an API key is attached Flowise is used to build and run chatflows and agentflows. Its chatflow-level authorization documentation states the important default plainly: by default, a flow is available to the public, and anyone with the chatflow ID can run a prediction through the embed or API. Assigning an API key to that chatflow changes the API path so the caller must send the correct Authorization header. On 2026-11-05, a count-only ZoomEye query with sub_type=all , page 1 and page size 1 returned 40,843 matches for app="Flowise" . The title query returned 42,376. These counts do not show whether a given flow has an API key, what tools it can invoke or whether the instance has app-level authentication. App-level authorization and flow-level authorization answer different questions. Flowise documents app-level login and JWT settings, including token and session secrets. The documentation warns that default secrets can increase the chance of forged tokens and impersonation. A production deployment should set unique secrets and review the cookie and session configuration. That does not automatically protect a flow that is intended to be callable by ID. Inventory flows as executable integrations A chatflow can connect to models, vector stores, HTTP tools, credentials and document stores. An exposed prediction endpoint is therefore more than a chat UI. It can consume paid tokens, query private data or trigger tools. Inventory each flow's owner, public state, attached API key, credential references and downstream systems. Test an unauthenticated prediction request and record the exact response. Assign a separate API key to each externally exposed flow where possible. Rotate the key when a widget is removed or a customer relationship ends. Treat the chatflow ID as discoverable metadata, not as a secret. If the ID appears in a public embed or support page, confirm that the flow's API key is still required. Use network restrictions and rate limits around the Flowise instance. An app-level login protects the management UI, but the prediction route may be intentionally public. Restrict the server from reaching internal metadata, administrative networks and unapproved HTTP destinations. A flow that can fetch arbitrary URLs needs an egress policy independent of its chat prompt. Store the Flowise encryption key separately from the deployment repository and back it up with the database. The documentation explains that it protects third-party credentials. If the key is regenerated or lost, existing credentials may fail to decrypt. A stolen key plus database access can expose the credentials attached to many flows. Monitor for new public flows, API-key changes, bulk predictions and unusual tool calls. The ZoomEye result is a prioritization aid, not evidence of an exposed workflow. Use the exact application count to locate candidate instances, then verify the app authentication, flow settings and outbound tool access. The security boundary is the flow's executable authority, not just its chat input box. References Flowise chatflow-level authorization Flowise app-level authorization Flowise environment variables and credential encryption ZoomEye app="Flowise" observation

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/johnettagaweraks/flowise-chatflows-are-public-until-an-api-key-is-attached-223n

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
