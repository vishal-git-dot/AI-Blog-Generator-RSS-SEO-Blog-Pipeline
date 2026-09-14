---
title: "When Someone Else's System Rejects You Without a Reason — Fixing a Diagnostic Order in Advance"
slug: "when-someone-elses-system-rejects-you-without-a-reason-fixing-a-diagnostic-order-in-advance"
author: "Sungsoo Youn"
source: "devto_ai"
published: "Mon, 14 Sep 2026 04:10:06 +0000"
description: "This is chapter 11 of my book **Building Autonomous AI Agents with Claude Code * — a field guide to turning Claude Code from a coding assistant into an agent..."
keywords: "test, you, two, cause, format, order, claude, not"
generated: "2026-09-14T04:21:00.975707"
---

# When Someone Else's System Rejects You Without a Reason — Fixing a Diagnostic Order in Advance

## Overview

This is chapter 11 of my book **Building Autonomous AI Agents with Claude Code * — a field guide to turning Claude Code from a coding assistant into an agent that remembers, verifies its own work, and knows when to stop. Everything below is from a system I actually run every day on one Windows PC.* 1. The Story of Losing Two Days I built an automation that uploads a submission file to an external service. The upload succeeded, but the next step returned 403 Forbidden . The response contained not a single character of explanation. The agent (and I) moved like this. "It looks like account authentication is missing" → asked the user to complete phone verification Verification was already done → "Then the permission scheme must have changed" → asked for a different key to be issued That wasn't it either → "ID-based identity verification is required" → asked the user yet again All three times we suspected the other side's system, and all three times we were wrong. The real cause was this. The archive was built as .zip , but that service accepts only .tar.gz . After changing the format, it passed on the first try . Two days had passed in between, and during that time the user went hunting for settings screens that didn't even exist. Something that could have been checked in 5 minutes was pushed onto a person. 2. Why This Happens Two biases overlap. ① We suspect the side we can't control first. The assumption that my code is wrong is uncomfortable, and blaming the other system is comfortable. On top of that, "an authentication problem" is a common story, so it sounds plausible. ② We call something a "cause" without verifying it. Once you say "authentication is the cause," that sentence stays in the record, and the next judgment is built on top of it. Two days of work get stacked on a false premise. AI agents suffer from these two biases more than humans do. Producing plausible explanations confidently is exactly what language models are good at. 3. The Rule: Decide the Suspicion Order in Advance When you encounter an external error with no stated reason, always check in this order . Order What Why first ① My output Do the format, structure, size, and encoding match the other side's spec? I control it 100%. Checking is cheapest ② My call method Endpoint, arguments, extension, headers Also on my side. Just compare against the docs ③ Account, permissions, authentication Their territory starts here Checking is expensive and requires a human And the way of speaking becomes a rule too. Before verification, don't say "cause." Say "candidate." This one word keeps the record uncontaminated. A candidate can be erased, but a cause gets read as fact by the next person. 4. Design the Discriminating Test First If there are multiple candidates, first build a test that separates the candidates . Picking one without a test is exactly what guessing is. Candidate Discriminating test Interpreting the result Rules not agreed to Can the data list be queried? If yes, agreement is done Service configuration problem Does the metadata show a "submissions paused" flag? If not, the configuration is fine My file format Send it once in a different format If it passes, the format is the cause Account permissions Same call with a different account or different key Only at this point do you ask a person The reason we lost two days is that we never carried the third test through to the end . We postponed the cheapest test until last. 5. The Sentences to Put in CLAUDE.md To make the agent follow this order every time, nail it into the rules file. If you have the memory structure built in Chapter 3, incidents like this also get recorded in mistakes.md . The sole purpose of the record is to keep the same mistake from happening twice. 6. Locking It In with a Regression Test Once you've found the cause, don't stop there. Leave a test so that that format can never be produced again . def test_submission_is_targz_not_zip (): path = build_submission () assert path . suffix == " .gz " and path . name . endswith ( " .tar.gz " ), \ def test_required_files_are_at_archive_root (): with tarfile . open ( build_submission ()) as tar : names = tar . getnames () The key is writing why the test exists in the test's message. Without the reason, six months later someone (or an AI) deletes it as "a constraint that looks unnecessary." 7. How to Phrase a Request to a Human If you've come all the way to the end and truly need a human hand, say it like this. ❌ "You just need to verify your identity" — an unverified assertion. If it's wrong, it wastes the other person's time. ⭕ "Two candidates remain. A takes 30 seconds to check, so please start with A." Requests also get an order and a rationale attached. A person is not an unlimited testing tool. Want the whole system? The book has 10 chapters plus 4 ready-to-use templates (CLAUDE.md starter, memory files, auditor checklist, measurement guide) and a hands-on section for every chapter. It's $19 as a PDF: https://dbsoul.gumroad.com/l/autonomous-ai-agents-claude-code Not sure yet? The first three chapters are free, same PDF format: https://dbsoul.gumroad.com/l/autonomous-ai-agents-claude-code-free-sample Questions about the setup are welcome in the comments — I'll answer with what actually happened, not theory.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dbsoul/when-someone-elses-system-rejects-you-without-a-reason-fixing-a-diagnostic-order-in-advance-4n5b

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
