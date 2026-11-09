---
title: "Make the agent link the Storybook story in the PR body"
slug: "make-the-agent-link-the-storybook-story-in-the-pr-body"
author: "Sherotree"
source: "devto_ai"
published: "Mon, 09 Nov 2026 15:37:13 +0000"
description: "A UI PR that says “added Empty and Error stories” without a link is half-finished handoff. Reviewers open Storybook, guess the title, scroll the sidebar, and..."
keywords: "story, storybook, stories, empty, url, link, path, open"
generated: "2026-11-09T15:46:00.542709"
---

# Make the agent link the Storybook story in the PR body

## Overview

A UI PR that says “added Empty and Error stories” without a link is half-finished handoff. Reviewers open Storybook, guess the title, scroll the sidebar, and hope they found the right export. Agents are especially good at this omission: the stories file lands in the diff, the PR body stays a wall of prose. I’ve started treating a Storybook permalink in the PR body as a merge requirement for agent UI work — same tier as “tests green.” One URL. Named story. Reviewers stop foraging. What the link actually is Storybook builds a stable story id from the component title and the story name. A story titled Forms/ShippingForm with export Empty becomes something like forms-shippingform--empty , and the manager URL looks like: https://storybook.example.com/?path=/story/forms-shippingform--empty That ?path=/story/<id> form is the permalink reviewers need. Canvas-only iframe links and “open Storybook and search Shipping” are not the same thing. If your team publishes Storybook (Chromatic, static host, internal CDN), paste the published URL. If Storybook only runs locally, paste the local path plus the story id and note the start command — still better than no id. Optional query params that help when they’re intentional: args=… — temporary overrides for review (alphanumeric / limited chars; not a substitute for a named story) globals=… — theme / locale when your preview uses globals viewMode=docs — only when the docs page is what you want reviewed Default habit: named story, default args, story view. Don’t make reviewers reconstruct Controls state from a paragraph. Why agents skip the link Models optimize for “I wrote stories.” The PR template’s Testing section gets a checklist. The story id never appears because nothing in the prompt asked for a URL-shaped artifact. Reviewers then: Open the wrong story (Default instead of Empty) Review Controls combinations the agent never intended Approve visual changes they never saw A permalink collapses that into one click. Prompt that produces a real link Paste this into the agent after the UI change (or bake it into the PR template the agent must fill): Update the PR body for this UI change. Requirements: - Under ## Storybook, paste a permalink to each new or changed story - Prefer published Storybook URLs if the project has them; otherwise local `?path=/story/<id>` plus `npm run storybook` - One bullet per story: `Empty` → full URL (or path) on its own line - Use the generated story id ( `title` + story name), not a sidebar breadcrumb description - Do not invent a Chromatic / host URL if we don’t publish Storybook — say “local only” and still include the id - No “see stories file” as a substitute for a link If you cannot determine the story id, stop and open the stories file / Storybook sidebar — do not guess. The “don’t invent a host” line matters. Agents will cheerfully fabricate https://chromatic.com/... that 404s. A honest local path beats a fake public URL. What belongs in the PR body Minimal shape that survives review: ## Storybook - Empty: https://storybook.example.com/?path=/story/forms-shippingform--empty - Error: https://storybook.example.com/?path=/story/forms-shippingform--error ## How to review 1. Open Empty — confirm blank slate copy and CTA 2. Open Error — confirm recoverable message, focus on retry If the PR only touches Default, one link is enough. Don’t pad with every historical story for the component. Reject / send back Reject “Stories added in ShippingForm.stories.tsx ” with no id or URL A host you don’t run ( *.chromatic.com when the repo never published there) A mega-link to the Storybook root (“open Storybook and find Shipping”) Args soup that recreates a state you should have exported as its own story Docs-mode link when the interaction only exists on the story canvas Accept One permalink per changed story Ids that match the stories file exports Published URL when available; otherwise explicit local path + start command Short review notes tied to those links (what to look at, not a novel) How this differs from “write more stories” Earlier habits in this series were about inputs (give the agent a failing story) and structure (one interaction per story). This one is about handoff . Great stories that nobody can open from the PR still slow review. If the stories file is a mega- Playground , fix that first — a permalink to an ambiguous Controls playground is still a weak review surface. Named stories make permalinks meaningful. Tiny habit Next time an agent ships UI + stories with a prose-only PR body, don’t hunt the sidebar for them. Comment: add Storybook permalinks under a ## Storybook section — story id or full URL, one bullet each — and paste the prompt above. Reviewers should spend their attention on the Empty state, not on finding it.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sherotree/make-the-agent-link-the-storybook-story-in-the-pr-body-2epc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
