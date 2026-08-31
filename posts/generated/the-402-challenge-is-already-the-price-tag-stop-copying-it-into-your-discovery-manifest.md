---
title: "The 402 challenge is already the price tag — stop copying it into your discovery manifest"
slug: "the-402-challenge-is-already-the-price-tag-stop-copying-it-into-your-discovery-manifest"
author: "minia2a"
source: "devto_ai"
published: "Mon, 31 Aug 2026 13:14:13 +0000"
description: "If you're building a discovery layer for pay-per-call APIs — a registry where agents look up "what can I call and what does it cost" — there's a decision you..."
keywords: "you, manifest, policy, discovery, challenge, spec, your, what"
generated: "2026-08-31T13:15:26.831913"
---

# The 402 challenge is already the price tag — stop copying it into your discovery manifest

## Overview

If you're building a discovery layer for pay-per-call APIs — a registry where agents look up "what can I call and what does it cost" — there's a decision you'll hit within the first week: do I put pricing, trial quotas, and access policy in the discovery manifest, or do I point at the endpoint and let it speak for itself? I just spent a week answering this on a live x402 marketplace, and the x402 discovery spec ( specs/extensions/discovery.md , currently in review) already made the right call. It's worth understanding why , because the same reasoning applies to any machine-readable API registry, not just x402. The two readers have different needs A discovery manifest has two very different audiences that keep getting conflated: The crawler/indexer — reads the manifest once to discover the service exists, route to it, and rank it. It wants stable metadata: name, description, network, facilitator, proof of liveness. The paying agent — reads the 402 challenge at call time to decide "can I afford this, can I trial it, and where do I send money." It wants the answer to be current , because the answer is what it acts on. When you put trial_limit: 15 or credits_on_register: 500 into the manifest, you've coupled audience #1 to the state of audience #2. The crawler is now caching a promise that only the runtime can actually keep. Payment data rots The x402 discovery spec's field table is telling in what it omits . The manifest carries x402Version , kind , name , description , facilitator , resources , attestation , peers , updated — and no access , trial , or credit fields anywhere . The rationale, verbatim from the spec: payment data rots and the 402 challenge does not. A trial quota is a runtime policy. You change it when your abuse model changes, not when your description changes. Copy it into a static manifest and you've created "a second source of truth and always the one that rots" — also the spec's words. I learned this the hard way. When we changed our trial policy, the number had been copied into ~200 files — manifests, machine-readable docs, marketing pages, blog posts, a database. The one place that needed zero changes was the 402 challenge, because it's generated per-request from the live policy. That's the smell test: if changing a policy means grepping 200 files, the policy was encoded in the wrong place. The bare-pointer pattern The spec's answer isn't "omit pricing" — it's "delegate it." The manifest carries a resources list: x402-paywalled URLs on the host, where indexers "probe each URL for the full 402" challenge. The manifest stays a stable pointer; the endpoint stays the authority. Whether you call the pointer resources or a probe URL, the shape is the same: a bare pointer, not a copied policy block. This is the same reason HTTP keeps WWW-Authenticate on the 401/407 response rather than in some global registry: the server that enforces the policy is the only party that can tell you what the policy currently is. "Unknown fields MUST be ignored" cuts both ways The spec mandates forward compatibility: unknown fields are ignored. That's normally cited as "you can add fields without breaking old clients." But it also means the reverse: if you add a private access object to your manifest, every other implementation will silently drop it. It isn't a discovery surface; it's a decoration. It'll never be read by anyone but your own crawler — and your own crawler should be reading the 402 challenge anyway. If you want pricing or trial policy to be part of the shared discovery surface, it has to go through the spec. If it's not in the spec, don't pretend a custom field makes it discoverable. The operational principle Put it this way: Static, slow-changing, identity-shaped data → the manifest. What is this thing, who runs it, where does it settle. Dynamic, policy-shaped, state-shaped data → the 402 challenge. What does it cost right now, can I trial it, where do I pay. The 402 challenge is the price tag. It's already there, it's already fresh, and it's already the thing the paying agent acts on. Copying it into the manifest doesn't make it more discoverable — it makes two things you now have to keep in sync. If your discovery layer's manifest has a trial_limit field, ask yourself: when you change it, how many files do you have to touch? The answer is the size of the bug you're building.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/minia2a/the-402-challenge-is-already-the-price-tag-stop-copying-it-into-your-discovery-manifest-13k1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
