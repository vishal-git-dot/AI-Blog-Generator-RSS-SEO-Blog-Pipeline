---
title: "Iam 12 .I Shipped a Buggy Version on Purpose. Here Is Why KODA v0.3.1 Is Better Than Any "Perfect" Release."
slug: "iam-12-i-shipped-a-buggy-version-on-purpose-here-is-why-koda-v031-is-better-than-any-perfect-release"
author: "Harun - solo dev"
source: "devto_ai"
published: "Thu, 01 Oct 2026 12:45:14 +0000"
description: "I am 12 years old. My development machine is a POCO C55 ($150 USD). It is December 1st. Yesterday, I launched v0.1.0. Today morning, I launched v0.2.0. An ho..."
keywords: "history, lightbulb, koda, bugs, would, have, code, fix"
generated: "2026-10-01T12:50:17.626833"
---

# Iam 12 .I Shipped a Buggy Version on Purpose. Here Is Why KODA v0.3.1 Is Better Than Any "Perfect" Release.

## Overview

I am 12 years old. My development machine is a POCO C55 ($150 USD). It is December 1st. Yesterday, I launched v0.1.0. Today morning, I launched v0.2.0. An hour ago, I launched v0.3.0. But here is the truth: v0.3.0 had bugs. Not tiny typos. Real issues. Conversation history didn’t save correctly in some edge cases. The lightbulb menu crashed if no file was open. Some founders would have deleted the release. They would have pretended it never happened. They would have waited three days for QA to sign off before admitting anything. I did none of that. Within two hours, I identified the root causes, wrote the patches, tested them locally, and shipped KODA v0.3.1 . And I marked v0.3.0 as "Bugy / Deprecated." Why? Because trust is built in the repair, not just the reveal. ⚡ WHAT WAS BROKEN IN V0.3.0? Let’s be specific. Transparency builds credibility. History Persistence Race Condition: Symptom: If you closed VS Code too quickly after sending a message, the chat history sometimes failed to write to workspaceState . Cause: Async operation wasn’t awaited properly during the dispose event. Lightbulb Menu Crash on Empty Editor: Symptom: Clicking the lightbulb when no file was open threw a TypeError: Cannot read properties of undefined . Cause: Missing null-check guard in the CodeActionProvider . Context Injection Lag: Symptom: @problems worked, but added ~200ms latency due to unoptimized diagnostic fetching. Cause: Fetching all diagnostics globally instead of filtering by active document first. 🛠️ HOW V0.3.1 FIXED IT (IN 2 HOURS) Fix 1: Awaited Dispose Handler Updated the webview disposal logic to ensure saveConversation() completes before the panel closes. Added a timeout fallback so the UI doesn’t hang if storage is slow. Fix 2: Null-Safe Code Actions Added strict guards in provideCodeActions : if ( ! editor || ! editor . document ) return []; No more crashes. No more errors. Just silence where there should be options. Fix 3: Optimized Diagnostics Query Changed from global getDiagnostics() to targeted getDiagnostics(activeDocument.uri) . Reduced context payload size by ~40% and eliminated the lag. 👑 WHY SHIPPING BUGS IS OKAY (IF YOU FIX THEM FAST) In traditional software, bugs are failures. In solo-founder velocity, bugs are data points . By shipping v0.3.0, I got real-world testing that I couldn’t simulate on my phone. Users found the race condition within minutes. If I had kept it private for "QA," I would have wasted days guessing. Instead, I spent 2 hours fixing what actually broke. The Lesson: Don’t aim for perfect code. Aim for fast recovery. 📊 THE VERSION HISTORY (HONEST EDITION) Version Status Key Feature Known Issue Resolution v0.1.0 ❌ Deprecated Genesis Chat Static Placeholders (XSS Risk) Fixed in v0.2.0 v0.2.0 ⚠️ Untested Streaming + Slash Cmds @problems Collected but Unused Wired in v0.3.0 v0.3.0 🐞 Bugy History + Lightbulb Race Condition + Crash Fixed in v0.3.1 v0.3.1 ✅ STABLE Hotfixes Applied None Known CURRENT LATEST 📥 DOWNLOAD THE CERTIFIED BUILD Do not use v0.3.0. Use v0.3.1. Get it here: github.com/harun-sket/Koda-cursor/releases/tag/v0.3.1 Grab koda-cursor-0.3.1.vsix . Install via Ctrl+Shift+P → "Extensions: Install from VSIX". Restart. Test the history persistence. Close VS Code. Reopen. See your chats still there. Click the lightbulb. See it work smoothly. Age doesn’t matter. Device doesn’t matter. Perfection doesn’t matter. Resilience matters. See you in the logs. And yes, v0.4.0 might drop tomorrow. 😂🐯

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/koda2026/iam-12-i-shipped-a-buggy-version-on-purpose-here-is-why-koda-v031-is-better-than-any-perfect-3acp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
