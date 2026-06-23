---
title: "When your agent does something bad, can you tell which agent did it?"
slug: "when-your-agent-does-something-bad-can-you-tell-which-agent-did-it"
author: "Brenn Hill"
source: "devto_ai"
published: "Tue, 23 Jun 2026 15:02:22 +0000"
description: "An agent does something it shouldn't: deletes a record it had no business touching, sends a message to the wrong tenant, calls an API in a tight loop until t..."
keywords: "agent, you, can, which, one, action, not, build"
generated: "2026-06-23T15:13:55.045711"
---

# When your agent does something bad, can you tell which agent did it?

## Overview

An agent does something it shouldn't: deletes a record it had no business touching, sends a message to the wrong tenant, calls an API in a tight loop until the bill spikes. Someone asks the only question that matters in the first ten minutes of an incident: which agent did this? If the honest answer is "we're not sure," everything downstream is harder. You can't contain what you can't name. You can't kill a build you can't identify. You can't audit, and you can't learn enough to stop it happening again. The frustrating part is that this is usually an identity problem, not a logging problem. The logs exist. They just don't say enough to point at one agent. Why the action is unattributable Two patterns make most agent actions impossible to pin down. The first is shared service accounts . Ten agents share one set of credentials, so every action shows up as the same actor. The IdP records "service-account-prod did X" ten thousand times a day, and there is no way to separate the agent that misbehaved from the nine that didn't. The second is agents running under a human's credentials . The agent inherits the launching user's full access, and in the logs the action is indistinguishable from something the human did by hand. Now you have an attribution problem and a blast-radius problem: the agent can do anything the human can. There's a subtler version too. Say two different builds of an agent both authenticate as the same account. Same name in the IdP, same token. In the logs they are identical — but one has a changed system prompt, a newer model, a different tool config. When one of them goes wrong, you cannot tell from the logs which build was running. Give the agent its own identity Step one: the agent gets its own identity, separate from the launching user. Not a human's credentials. Not a shared service account. Its own. This is the foundation everything else sits on. Once the agent authenticates as itself, every action it takes is at least its own action in the record — not borrowed from a person, not blended with nine siblings. Stamp six fields on every action Identity at the IdP is necessary but not sufficient. The action itself needs to carry enough context to be reconstructed later. Stamp six fields on every action: Accountable party — who is responsible for this agent existing. Operational owner — who actually runs and maintains it day to day. Tenant — which customer this action was on behalf of. Agent-type-id — which build of the agent this is. Agent-instance-id — which specific run . Trace context — where this sits in the call graph. Together they answer: who's responsible, who operates it, for which customer, which build, which run, and where in the chain of calls. Most systems capture one or two of these — usually a tenant and maybe a trace id. The gap between "one or two" and "all six" is exactly the gap that makes an incident unattributable. Make agent-type-id a content hash, not a name The field that quietly breaks is agent-type-id , because the obvious implementation is a name someone assigns. Call it support-agent-v2 and ship it. Three weeks later someone swaps the model, tweaks the system prompt, and ships again — still support-agent-v2 . The name didn't change; the behavior did. Silent drift, invisible in the logs. Make agent-type-id a content hash instead. Hash over everything that determines how the agent behaves: the container image, the harness, the system prompt, the model identifier, the config. Like a container digest, but extended past the image to everything that shapes behavior. The property you want is that the id changes when any input changes. Swap the model, the hash changes. Edit one line of the system prompt, the hash changes. A changed build can no longer masquerade as the old one, because it gets a new id automatically. Drift stops being silent and shows up as a new agent-type-id in your logs. Track parent-child lineage Agents spawn sub-agents, and the sub-agent is where a lot of trouble actually happens. So record lineage: which sub-agent ran, under which parent, and — this is the part people miss — the prompt the parent handed it . That parent-passed prompt is often the only place an injected instruction is visible. A poisoned tool result or a manipulated upstream response turns into an instruction the parent passes down. If you didn't capture the handoff, the injection leaves no trace and the sub-agent looks like it just decided to misbehave on its own. Identity is the recovery surface The thing to internalize: identity isn't paperwork you do for compliance. It's the recovery surface . Containment, the kill switch, the audit trail, and the learning afterward all depend on being able to attribute an action to a specific agent build and run. And it has to be there before the incident. Identity added afterward is too late for the incident you're currently in — you can instrument for next time, but the one in front of you stays unattributable. The BRACE agent guide goes deeper on the field definitions and how they fit the broader framework. One honest question to leave you with: pull up your logs from an action an agent took an hour ago. Can you name the specific build that took it? If not, that's the gap — and it's worth closing before you need it.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/brennhill/when-your-agent-does-something-bad-can-you-tell-which-agent-did-it-37a2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
