---
title: "The confirmation your app shows isn't the confirmation that matters"
slug: "the-confirmation-your-app-shows-isnt-the-confirmation-that-matters"
author: "StareBrain"
source: "devto_ai"
published: "Fri, 11 Sep 2026 03:56:36 +0000"
description: "If you're building anything that lets an AI agent act on a user's behalf — send a message, book something, control a device — there's a failure mode that's e..."
keywords: "you, action, not, permission, system, blocked, confirmation, agent"
generated: "2026-09-11T04:00:57.645626"
---

# The confirmation your app shows isn't the confirmation that matters

## Overview

If you're building anything that lets an AI agent act on a user's behalf — send a message, book something, control a device — there's a failure mode that's easy to miss until it bites you: the gap between "permission was granted" and "permission is still valid right now." The scenario Imagine this timeline: T+0:00 — An agent has permission to perform an action, and that authority is valid. T+0:04 — The authority is revoked, or the world changes underneath it (a contact's number updates, a calendar slot fills, a setting reverts). T+0:05 — The agent still has the technical capability to execute. T+0:06 — A downstream system records the action as complete. The agent had permission. Was it still authorized at the moment it actually mattered? Those are different questions, and most systems don't distinguish them. Why "blocked" often lies Say you catch the problem and try to stop the action after authority changes. If the request has already been dispatched to an external system — an SMS provider, a calendar API — simply flipping your own app's state to "blocked" doesn't prove anything happened, or didn't. You're guessing, dressed up as a system that checked. This showed up for me building a confirm-before-execute layer for phone commands. A stale result from an earlier attempt rendered as "executed" right after a new attempt correctly denied the same action. The denial was truthful about the decision. It was silent about the actual state of the world. Three states, not two Most systems track two outcomes: executed, or blocked. That's not enough. The honest model needs three: EXECUTED — observed evidence the intended side effect actually occurred. DENIED_CONFIRMED — denied, and verified the action never crossed the execution boundary. DENIED_UNRESOLVED — denial was intended, but available evidence can't independently establish whether a downstream side effect occurred anyway. That third state is the one most systems don't have a slot for at all. Without it, uncertainty silently gets rounded up to a confident "blocked" — which is worse than an honest "I don't know," because it actively points you away from checking. The fix that keeps showing up Talking this through with people building completely different systems — WordPress admin tools, AI ops platforms, agent authorization layers — the same pattern kept surfacing independently: Never trust an earlier authorization check. Re-verify right before execution, not when the action was first requested. Bind confirmation to exact parameters. A dry run returns a short-lived token tied to the specific values (recipient, time, amount). Confirm has to present that token, byte-identical, or it's treated as a new plan requiring fresh approval — not a rubber-stamp of the old one. Once dispatched externally, "blocked" isn't a real status anymore. Only a provider receipt or webhook can close the loop. Until then, the honest label is "submitted, unresolved" — not "blocked," and definitely not "executed." What this changes practically For a phone-command interface, the gap between showing someone a plan and firing it is usually seconds — but "short" isn't "zero." A dry run now returns a hash of everything the action depends on. Confirm has to match that hash exactly, or it's rejected as stale and requires a fresh confirmation. Cheap to build, and it closes a real gap that used to be invisible. The broader lesson: if your system can't tell "we decided not to do this" apart from "we don't know what happened," you don't have a permission system — you have a permission system's confident-sounding guess. Building StareBrain — natural language commands for Android, with exactly this confirmation model at its core. Currently pre-launch: starebrain.vercel.app

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/starebrain/the-confirmation-your-app-shows-isnt-the-confirmation-that-matters-57mo

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
