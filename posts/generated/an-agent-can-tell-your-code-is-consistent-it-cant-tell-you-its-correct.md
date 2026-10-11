---
title: "An agent can tell your code is consistent. It can't tell you it's correct."
slug: "an-agent-can-tell-your-code-is-consistent-it-cant-tell-you-its-correct"
author: "Jeff"
source: "devto_ai"
published: "Sun, 11 Oct 2026 21:25:56 +0000"
description: "Give an agent a ticket that says "add a refund endpoint for cancelled orders." It will write a route, a service method, a migration, and three tests. The tes..."
keywords: "agent, not, code, what, actually, ticket, have, can"
generated: "2026-10-11T21:42:13.764537"
---

# An agent can tell your code is consistent. It can't tell you it's correct.

## Overview

Give an agent a ticket that says "add a refund endpoint for cancelled orders." It will write a route, a service method, a migration, and three tests. The tests pass. The diff is clean. The PR description summarizes what the code does. Ship it, and two weeks later finance notices that refunds are being issued to orders that were never paid for. The agent followed the ticket literally: refund on cancel, no payment-state check. The code is consistent with what was written. It is not correct for what the business actually needed. This gap shows up in every agentic workflow I have run, and it is not a prompt-engineering problem. What an agent actually verifies When an agent says "done," it means a narrow set of things: the file it edited parses, the imports resolve, the tests it chose to run pass, the type checker is quiet. Those are all internal consistency checks. They prove the code does not contradict itself. They do not prove the code matches the real world: the real payment ledger, the real state machine, the real boundary condition the product owner actually cares about. The agent has never seen those. It has only seen the ticket text and the existing code. Worse, the tests the agent writes are part of the same hallucination loop. It generates the feature, then generates a test that confirms the feature behaves the way it said it would behave. If the original interpretation of the ticket was wrong, the test will happily lock the wrong behavior in as "expected." Where the gap actually bites The failures I have had to clean up all share a shape: the agent picked one plausible reading of an ambiguous requirement and built the whole thing to that reading. There was no moment where it stopped and said, "wait, which one of these three did you mean?" The cancel endpoint that also refunds, on a system where some orders were never charged. The pagination query that sorts by created_at when the spec said updated_at , because created_at is what every other endpoint uses. The webhook handler that returns 200 for unknown event types, because "we don't want to break the sender," instead of logging them for inspection. The retry wrapper that catches network errors but not validation errors, because the ticket said "make it retry on failures." In each case the code was clean, the tests passed, the PR was reviewable. The bug was in the interpretation, and no amount of reading the diff would have caught it without context the agent does not have. What closes the gap cheaply I stopped trying to make the agent ask better clarifying questions. It will not, not reliably, and a ten-round clarification chat is slower than just writing the code myself. What works better is pushing the ambiguity into a form the agent can actually check against. Write the contract before the implementation. For API work, that means an OpenAPI file with explicit status codes, required fields, and documented error responses for each failure mode. The agent cannot then quietly decide that an unknown event should return 200 , because the contract says it returns 422 and logs. We do this locally in Powerduck now: the OpenAPI file is the spec, the implementation has to match it, and re-running the contract against the live endpoint catches drift instead of waiting for a user to report it. Name the edge case in the ticket. "Refund on cancel" becomes "Refund on cancel, but skip refunds for orders that were never captured." One sentence, written by a human, removes the branch the agent would have guessed wrong. Ask for the failure test, not the happy-path test. When reviewing an agent-written PR, skip the happy path. Read the test that should have failed. If it does not exist, the agent has not actually thought about the wrong input. The line I now draw An agent is great at taking a precise, bounded spec and producing code that matches it. It is bad at taking a vague sentence and inferring the spec correctly. The fix is not a better model; it is moving the ambiguity upstream, into a place a machine can actually read. Consistency checks you can automate. Correctness still has to come from a human who knows what the system is for . The agent's job is to make that human review cheap, not to replace it.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jeff_pdc/an-agent-can-tell-your-code-is-consistent-it-cant-tell-you-its-correct-1can

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
