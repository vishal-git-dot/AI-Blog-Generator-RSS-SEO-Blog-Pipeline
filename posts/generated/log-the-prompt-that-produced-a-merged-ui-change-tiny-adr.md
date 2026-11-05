---
title: "Log the prompt that produced a merged UI change (tiny ADR)"
slug: "log-the-prompt-that-produced-a-merged-ui-change-tiny-adr"
author: "Sherotree"
source: "devto_ai"
published: "Thu, 05 Nov 2026 14:28:19 +0000"
description: "We merge a lot of agent UI now. Six months later someone asks “why does this form validate zip before city?” and the PR description just says “agent polish.”..."
keywords: "prompt, agent, you, adr, before, not, next, city"
generated: "2026-11-05T14:31:30.070178"
---

# Log the prompt that produced a merged UI change (tiny ADR)

## Overview

We merge a lot of agent UI now. Six months later someone asks “why does this form validate zip before city?” and the PR description just says “agent polish.” The diff is gone from working memory. The prompt that made the decision is gone too. I started treating the prompt that shipped like a tiny ADR. Not a ceremony. One short file (or PR note) next to the change so the next human — or the next agent — can see what we asked for , not only what landed . What goes in the tiny ADR Keep it under ~15 lines. I use this shape: ## Prompt ADR — ShippingForm zip-before-city (2026-11-05) **Goal:** Require zip before city on blur for US addresses. **Prompt (verbatim):** … **Files touched:** `ShippingForm.tsx` , `shippingValidation.ts` **Rejected alternatives:** city-first (matches old mock); shared schema with Checkout (too wide for this PR) **Follow-ups:** none / link issue Verbatim matters. Paraphrase loses the constraints the agent actually obeyed (or ignored). Why not “just read the commit”? Commits show outcome . Prompts show intent and guardrails : “Only touch ShippingForm.tsx ” explains why Checkout stayed dirty “No new deps” explains why we didn’t pull in zod “Match existing error copy keys” explains the awkward i18n string you were about to “clean up” Without that, the next agent “simplifies” the awkward bits and reopens bugs you already paid for. Where I put it Pick one place and stick to it. Mine: Preferred: docs/prompt-adrs/YYYY-MM-DD-short-slug.md in the same PR Fine: a ## Prompt used section in the PR body (copy into docs when merging) Avoid: only in chat history / only in the agent transcript Chat is not a durable design record. Repo is. Prompt I paste when starting the work You’re editing `ShippingForm` US address validation only. Before you change code, write `docs/prompt-adrs/YYYY-MM-DD-shipping-zip-before-city.md` with: - Goal (one sentence) - This prompt pasted verbatim - Files you expect to touch - Alternatives you will NOT do in this PR Then implement. Do not expand scope. If you need Checkout changes, stop and say so. Yes, I ask the agent to write the ADR first. If it skips the file, I bounce the PR before reviewing the UI. What I reject in review Reject / ask to add Agent UI PR with no prompt record and a vague “assisted by AI” checkbox ADR that says “improved UX” with no verbatim prompt Prompt buried in a screenshot of the chat Accept Short markdown in-repo Verbatim prompt + goal + files + explicit non-goals Link from PR description to the ADR path Tiny habit On the next agent UI merge, spend two minutes: paste the prompt into docs/prompt-adrs/… , list files, name one thing you didn’t do. Future you (and the next model) will treat that as source of truth instead of inventing a nicer story from the diff alone.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sherotree/log-the-prompt-that-produced-a-merged-ui-change-tiny-adr-1bbp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
