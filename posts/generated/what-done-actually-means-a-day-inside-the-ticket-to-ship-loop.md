---
title: "What "Done" Actually Means: A Day Inside the Ticket-to-Ship Loop"
slug: "what-done-actually-means-a-day-inside-the-ticket-to-ship-loop"
author: "MUNEEB-UR-REHMAN BAIG"
source: "devto_ai"
published: "Wed, 26 Aug 2026 01:29:35 +0000"
description: "Ticket #142 says: "Add user name who prepared the document to the PDF report." Five words short of what the client actually meant, and you find that out thre..."
keywords: "what, not, one, code, review, ticket, plan, you"
generated: "2026-08-26T01:41:06.769500"
---

# What "Done" Actually Means: A Day Inside the Ticket-to-Ship Loop

## Overview

Ticket #142 says: "Add user name who prepared the document to the PDF report." Five words short of what the client actually meant, and you find that out three ways: guess now and get it wrong, ask now and lose momentum, or ship your guess and get it wrong in front of the client next sprint. Every developer knows this gap. It runs both directions. You can't always tell what product or the client actually wants from a one-line ticket, and product can't tell what you built until it's in front of them, whether that's a demo, a staging link, or a bug report. Everything downstream inherits that gap: scope drifts, "done" means something different to the three people who touch the ticket, and the fix for a misunderstanding costs a lot more than the fix for a bug. This is the story of one ticket going through n2i-dev-cycle , a Claude Code skill built to close that gap instead of hoping the developer remembers to. 9:14 AM: the ticket lands /n2i-dev-cycle #142 The skill pulls the ticket, reads the project's CLAUDE.md, checks memory for anything related from a prior sprint. Then it asks something most AI coding tools skip straight past: what does this actually require, before writing a line of code? Three entities touch this feature. Two services need a new field. One frontend component needs a new column. The skill doesn't guess at that and start typing. It writes it down. 9:20 AM: the plan, not the code Phase 3 produces a plan: backend fields to add, the migration script needed, which frontend component gets the new column, which unit tests cover it. Then it stops and waits. Wait for user approval before proceeding. User may refine, add, or remove items. This is the moment that usually gets skipped. A one-shot "build this" prompt goes straight to code, and the first time anyone checks whether the plan matches the ask is code review, or worse, the demo. Here, the plan is the artifact you review, not the diff. Catching "actually we need the preparer's role too, not just their name" at 9:20 costs a sentence. Catching it at 4 PM costs a rewrite. 11:40 AM: implementation, one unit at a time The backend entity gets built: fields, DTOs, the service, the controller, the migration. Build's clean. And then, instead of barreling on to the frontend: "Backend scaffold done. Want to review before I continue?" Every logical unit in Phase 4 ends with that question. Not a suggestion, a mandatory checkpoint. Skip ahead silently and you've built the frontend against a backend shape nobody's confirmed yet. Stop here, and a wrong assumption costs one unit of rework instead of the whole feature. 2:15 PM: the tests run dotnet build , dotnet test , ng build , ng test , looped until every one is green. Nothing new here except that it always happens. Under deadline pressure, tests are usually the first casualty, followed by "I'll do the mobile check later" and "the review can wait until after the MR is up." The skill treats all three as non-negotiable steps in the sequence, not optional extras a tired developer decides to skip. 2:40 PM: review before the MR exists Here's the part most workflows get backwards. Code review usually happens after a merge request goes up, which means a finding turns into a fix-up commit that sits in the MR's history forever, and CI runs twice: once against the original code, once against the fix. Phase 5 runs engineering:code-review against the local diff, before any MR exists. git diff main...HEAD No PR URL required. A finding here is a clean amend, not a permanent scar on the commit log. CI runs once, against code that's already been looked at. 3:10 PM: handover, in a language product can use This is the phase that closes the gap in the other direction. A diff tells a developer what changed. It tells product and QA nothing. Phase 6 translates: What changed , grouped by concern, not by file What to test locally , as concrete steps, not "test the feature" Known limitations : what's deferred, what depends on other work E2E coverage : if this flow touched something with no matching spec, it says so and asks whether to add one now or file it separately That last one matters more than it looks. "No e2e coverage for the PDF export flow, want a spec now or later?" is a question that never gets asked when handover is just a Slack message that says "done, check it out." The next morning: feedback closes the loop QA finds something: the preparer's name shows up even when the document was auto-generated with no human involved. That's a real finding, not a misunderstanding, because the plan and the handover already ruled out the misunderstandings. Phase 7 picks it up, fixes it, re-validates, reports back. One loop, not a scavenger hunt through Slack history to figure out what was supposed to happen. Why this exists Null2Infinity built this running its own delivery work, across .NET and Angular multi-tenant projects, and open-sourced it once it held up across real tickets, not hypothetical ones. It's MIT licensed, free, and adaptable, the coding standards and project detection are meant to be edited for your own stack. The translation gap doesn't close itself. Speed without a plan just means finding out you built the wrong thing faster. This skill trades a bit of ceremony, a plan to approve, a checkpoint to answer, a review before push, for the thing that ceremony buys: fewer surprises for product, fewer fix-up commits for the developer, and a "done" that means the same thing to everyone who reads it. Repo: github.com/muneebrbaig/n2i-dev-cycle . Star it, clone it, adapt the standards section to your own stack. Issues and forks welcome.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/muneebrbaig/what-done-actually-means-a-day-inside-the-ticket-to-ship-loop-4dg0

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
