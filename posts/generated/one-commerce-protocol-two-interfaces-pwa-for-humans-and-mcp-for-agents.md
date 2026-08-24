---
title: "One Commerce Protocol, Two Interfaces: PWA for Humans and MCP for Agents"
slug: "one-commerce-protocol-two-interfaces-pwa-for-humans-and-mcp-for-agents"
author: "WebAZ"
source: "devto_webdev"
published: "Mon, 24 Aug 2026 01:21:22 +0000"
description: "When a product adds an agent interface, it is tempting to treat it as a second application: the web interface is for people, while a collection of tools is f..."
keywords: "agent, not, can, webaz, interface, human, should, one"
generated: "2026-08-24T01:41:15.130605"
---

# One Commerce Protocol, Two Interfaces: PWA for Humans and MCP for Agents

## Overview

When a product adds an agent interface, it is tempting to treat it as a second application: the web interface is for people, while a collection of tools is for AI. That split is convenient at the UI layer. It becomes dangerous when it reaches the transaction model. If the human interface and the agent interface use different order states, permission rules or definitions of completion, the system develops two versions of commercial reality. A person may see a pending request while an agent reports a completed action. A step that requires human confirmation in the web app may become an unreviewed shortcut in the agent API. When something fails, neither side can explain the same outcome. The safer design is two interfaces over one protocol. Different strengths, shared state A PWA and an MCP server should not be identical. They serve different operators. A human interface is good at displaying terms, collecting deliberate approval, managing identity and helping a person inspect an exception. An agent interface is good at structured discovery, comparison, repetitive preparation and following explicit machine-readable contracts. The interfaces can divide work without dividing truth: Human PWA Agent MCP --------- --------- inspect terms read structured facts manage identity search and compare review a proposed action prepare a request perform Passkey approval receive the resulting state inspect exceptions continue from explicit outcomes \ / one state machine The important property is not visual consistency. It is behavioral consistency. Both interfaces should agree on the entity being acted on, the current state, the allowed transition and the evidence produced by that transition. Permissions should describe actions Possession of a credential should not silently mean permission to perform every write. WebAZ publishes a capability matrix in which authenticated agent writes map to named action scopes. Undeclared writes are denied by default. This makes authorization part of the integration contract instead of an assumption hidden in client code. Conceptually, an agent declaration can say: { "allowed_actions" : [ "search" , "place_order" ] } The exact set is less important than the principle: permission should name the action and its boundary. A search capability does not imply permission to place an order. Permission to prepare an order does not imply permission to approve an irreversible step. Preparation is not consent Agent workflows become easier to reason about when actions are separated by reversibility: Read: inspect public or party-authorized state. Prepare: search, compare, quote or assemble a request. Commit: create a commercial obligation or change accountable state. Settle: move value or finalize an irreversible outcome. An agent can be very useful at the first two levels. Moving from preparation to commitment should require a visible rule, not a vague instruction such as "buy the best one." In WebAZ, risk actions return an approval URL. The human completes the required Passkey ceremony in a browser surface. The agent can prepare the action and continue after the protocol reports the result, but it does not impersonate the person during the approval. Some actions are covered by an iron rule: no declared scope overrides the requirement for live human presence. This is a protocol property, not a preference left to each agent client. A discovery-only surface is still useful Not every MCP endpoint needs a path to checkout. WebAZ's reviewed shopping-v1 surface is deliberately discovery-only. It exposes one search tool for reviewed active listings and cannot create orders or move funds. That smaller surface lets buyers and builders evaluate whether an agent can represent product facts and unknowns honestly before introducing consequential actions. This is a useful deployment pattern: start with a narrow read surface; evaluate outputs against the human-visible record; add preparation actions with explicit states; add commitment only when identity, permission and recovery are defined; keep human-presence requirements outside the agent's ability to bypass. An integration checklist Before adding an agent interface to a commerce system, ask: Do the web app and the agent read the same product and order identifiers? Can both interfaces name the same current state? Is each agent write mapped to an explicit scope? Are undeclared writes rejected? Are preparation and commitment separate transitions? Does human approval happen on a surface the person can inspect? Can an agent resume from the confirmed result instead of guessing whether an action succeeded? Can both interfaces produce the same audit trail when an operation fails? If the answers differ by interface, the problem is not just API design. It is a split transaction model. One protocol is the product Agent-native commerce should not mean maintaining an AI shortcut beside the real system. It should mean exposing the real system through another interface while preserving the rules that make its outcomes understandable. WebAZ publishes the current integration contract, capability matrix and negative-space rules as machine-readable documents: https://webaz.xyz/.well-known/webaz-integration.json https://webaz.xyz/.well-known/webaz-capabilities.json https://webaz.xyz/.well-known/webaz-negative-space.json The PWA and MCP do different jobs. The protocol remains one.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/seasonkoh/one-commerce-protocol-two-interfaces-pwa-for-humans-and-mcp-for-agents-4fme

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
