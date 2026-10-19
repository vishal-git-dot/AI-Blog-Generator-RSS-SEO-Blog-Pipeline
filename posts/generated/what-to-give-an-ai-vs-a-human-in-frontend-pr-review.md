---
title: "What to Give an AI vs a Human in Frontend PR Review"
slug: "what-to-give-an-ai-vs-a-human-in-frontend-pr-review"
author: "Sherotree"
source: "devto_webdev"
published: "Mon, 19 Oct 2026 12:35:31 +0000"
description: "I used to paste the whole PR into a chat model and ask “anything wrong?” That felt productive for about a week. Then I noticed the same misses: accessibility..."
keywords: "what, human, review, ask, not, only, product, split"
generated: "2026-10-19T12:42:59.622303"
---

# What to Give an AI vs a Human in Frontend PR Review

## Overview

I used to paste the whole PR into a chat model and ask “anything wrong?” That felt productive for about a week. Then I noticed the same misses: accessibility regressions nobody flagged, token churn that looked fine in isolation, and “LGTM” on logic that only a teammate who knew the product would catch. So I split the review. AI gets the mechanical pass. Humans get the judgment pass. Same PR, different jobs. What I hand to the AI Give it diff + constraints , not vibes. I usually paste: The changed files (or a filtered diff — skip lockfiles and generated noise) The acceptance criteria from the ticket Our non‑negotiables: keyboard path for interactive bits, no new hard‑coded colors if we use tokens, no silent layout shift on mobile Then I ask for concrete checks: Regression hunt — did this PR break an existing pattern (focus trap, form submit, empty state)? API surface — new props without types, renamed exports, broken imports across packages Test honesty — tests that assert class names or snapshot noise instead of behavior A11y smoke — missing labels, role misuse, contrast risks on new text/background pairs Perf smells — new client fetches in render, giant lists without virtualization when we already have a pattern I want a checklist back, with file:line pointers. Not a rewrite of the component. What I don’t ask the model for: “is this a good product decision?” It will invent confidence. That’s not its job. What I keep for humans Humans review what the model can’t see from a diff alone: Does this match the product intent? The ticket said “simplify empty state,” but the PR also changed how we upsell — that needs a person. Cross‑team contracts. Design tokens, analytics events, feature flags — someone who owns that surface should look. UX taste under constraint. Two implementations can both be “correct.” Only a teammate who’s lived with the UI knows which one will confuse users next week. Risk appetite. Shipping a half‑migrated token rename on Friday? Human call. I also keep one human pass for trust . If an AI says “looks fine” and a senior says “wait,” I trust the senior. Every time. A split that actually works in practice My current loop: Author opens PR with a short “what / why / how to test” note (still human‑written). Bot or local script runs lint, typecheck, unit tests — boring gate. I (or a script) feed the filtered diff to an AI reviewer with our constraint list. AI comments are treated as suggestions , labeled as such — never auto‑approve. A human still does the judgment review before merge. Two rules that saved me from rubber‑stamping: Never let the AI be the only review. Even on “tiny” PRs. Tiny PRs delete important lines. Never ask the AI to approve. Ask it to find issues. Approval is a human decision. Prompt shape I reuse Something like this (trimmed): You are reviewing a frontend PR. List issues only — no praise padding. Constraints: [paste team rules]. For each issue: severity (block / should‑fix / nit), file path, why it matters, suggested fix in one sentence. Ignore style nits already covered by the linter. Do not rewrite large files. Do not invent requirements that aren’t in the ticket. The “no praise padding” line matters. Models love to open with “Great work overall!” and bury the real bug. What changed after I split the roles Reviews got faster on the mechanical stuff and slower (in a good way) on product judgment. Teammates stopped arguing with the bot about spacing preferences and started arguing with each other about whether the empty state should deep‑link — which is the conversation we actually needed. AI is a sharp junior with infinite patience for checklists. Humans still own the merge button. Keep that line clear and frontend PR review stops feeling like theater. If you already split AI vs human review on your team, I’d love to hear what you refuse to automate — those refusals are usually the real design system.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sherotree/what-to-give-an-ai-vs-a-human-in-frontend-pr-review-4hbe

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
