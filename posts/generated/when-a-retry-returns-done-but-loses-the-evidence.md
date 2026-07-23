---
title: "When a Retry Returns “Done” but Loses the Evidence"
slug: "when-a-retry-returns-done-but-loses-the-evidence"
author: "Reliable AI Delivery"
source: "devto_ai"
published: "Thu, 23 Jul 2026 19:21:44 +0000"
description: "A retry can recover a response without recovering the context needed to trust it. Consider this fictional sequence: A coding agent receives a task with three..."
keywords: "not, retry, evidence, reviewer, but, completion, output, state"
generated: "2026-07-23T19:26:23.867684"
---

# When a Retry Returns “Done” but Loses the Evidence

## Overview

A retry can recover a response without recovering the context needed to trust it. Consider this fictional sequence: A coding agent receives a task with three acceptance conditions. It edits several files and starts a test. The response stream fails before the handoff reaches the reviewer. The system retries. The reviewer receives a confident completion message, but not the original changed-file list or the complete test output. The retry may have returned a fluent answer. That does not tell us whether the answer belongs to the same task state, the same workspace revision, or the same verification run. This is not proof that the implementation is wrong. It is a provenance gap. What was lost? The useful question is not only “Did the request retry?” It is “Which parts of the delivery record survived the retry?” For a reviewable handoff, preserve at least: the original task and acceptance conditions; the assistant’s exact completion claims; the changed files or diff; the exact command that ran; the complete output and exit state; the revision, branch, or working-tree state; anything unverified, inaccessible, or conflicting. If the retry returns only the final claim, the reviewer cannot safely infer the missing artifacts. Do not turn missing context into a green result Suppose the retry says: “Implemented the change and all tests pass.” But the current record contains no command, no output, and no link between the reported run and the current revision. Three different statements are possible: PROVEN : the supplied material directly supports the specific claim. UNPROVEN : the claim may be true, but the required support is absent. BLOCKED : the reviewer cannot obtain the required artifact or access the environment. In this example, “all tests pass” should not become PROVEN merely because the sentence is confident. If the evidence is missing, keep it UNPROVEN or BLOCKED . Ask for a correction packet, not a longer summary A useful follow-up request is narrow: Restate the exact claim being corrected. List the current changed files or provide diff evidence. Provide the exact verification command and complete result, or state that it was not run. Identify the revision or workspace state that produced the output. List known limitations and unverified areas. The purpose is not to force the agent to repeat the whole conversation. It is to reconstruct the smallest evidence packet another reviewer can inspect. When should a human rerun the check? A supplied log can support a consistency review, but it is not automatically independent proof. The reviewer still has to decide whether the risk justifies a fresh run. For a copy edit, the supplied record may be enough. For a data migration, authentication rule, billing change, security boundary, or production behavior, a human-owned rerun may be necessary. The risk controls the depth of verification. A practical manual workflow The free AI Completion Evidence Auditor Lite is a worksheet for this kind of second pass. It helps compare one completion message with the task, changed-file information, and test or build output you actually have. It does not run code, authenticate logs, or certify production readiness. Free download: https://frankster8205.gumroad.com/l/ai-completion-evidence-auditor-lite?src=devto_us_article2_response_loss_retry_v1&utm_source=devto&utm_medium=organic_content&utm_campaign=reliable_ai_delivery_wave1&utm_content=devto_us_article2_response_loss_retry_v1

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/reliableaiddelivery/when-a-retry-returns-done-but-loses-the-evidence-50ck

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
