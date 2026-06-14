---
title: "The billing state most APIs get wrong: "unknown" is not "no""
slug: "the-billing-state-most-apis-get-wrong-unknown-is-not-no"
author: "Larry Johnson"
source: "devto_python"
published: "Sun, 14 Jun 2026 13:55:12 +0000"
description: "If you bill per result, there is one design decision that quietly decides whether customers trust you: what you do when you could not get an answer. Most usa..."
keywords: "you, not, your, unknown, answer, bill, could, per"
generated: "2026-06-14T14:17:29.350318"
---

# The billing state most APIs get wrong: "unknown" is not "no"

## Overview

If you bill per result, there is one design decision that quietly decides whether customers trust you: what you do when you could not get an answer. Most usage-billed APIs collapse the world into two states. The call worked, or it failed. Valid or invalid. Found or not found. That binary is where the trust leaks out, because it hides a third state that happens constantly in the real world: you asked, and the system genuinely could not tell you right now. A concrete example Say you run an email verification endpoint. A customer sends an address, you check it, you bill for the answer. Easy. Then a DNS lookup times out. Or the domain returns SERVFAIL. Or the mail server greylists your probe and hangs. What do you return? The lazy answer is invalid , because it is not valid , and now the row is "done" and billable. That single shortcut does two bad things at once. It deletes a real lead from your customer's list, because a timeout is not proof the address is dead. And it charges them for the deletion. They paid you to damage their own data. The honest version keeps three states: valid -> we confirmed it. billable. invalid -> we confirmed it is not deliverable (no MX, etc). billable. unknown -> we could not determine it right now. NOT billable. unknown is the whole game. It says "you asked, we tried, we could not be sure, so we are not going to charge you or pretend." It is the difference between a tool that cleans a list and a tool that silently corrupts it. This generalizes past email The same gap shows up anywhere you bill per result: A scraper hits a page that 404s. Is that "no contact found" (a real answer) or "we could not load the page" (an unknown)? Bill the first, never the second. A profile lookup gets rate-limited. The lazy path returns an empty profile that looks exactly like a real "this person has no data." Now your customer cannot tell a true empty from a failure, and you billed for both. A price checker can not reach a vendor. Returning "no price" reads as "free or unavailable." Returning unknown reads as "try again." Very different downstream. The rule I have settled on across a handful of pay-per-event tools: bill for delivered answers, never for attempts, and make "we could not tell" a first-class, free, clearly-labeled output. Why this is worth the lost revenue It costs you money on paper. Every unknown and every no-result is a row you did not charge for. Your per-run number looks worse than a competitor who bills for everything including the garbage. It is also the only version of the number that survives the customer opening their own logs. The competitor who billed for failures looks cheaper for exactly one cycle, until someone notices their bounce rate went up after a "cleaning" or their lead count dropped for no reason. Trust is the actual product. The billing model is just where you prove you have it. How to implement it without overthinking Every record carries its own status. Do not infer success from "the batch finished." Use at least three buckets: answer, no-result, unknown. Add more if your domain needs them (fetch-error, rate-limited, etc), but never fewer. Only "answer" (and a definitive negative answer, if that is what was asked for) is billable. Everything else is free and labeled. Say it out loud in your docs. "We do not bill for failed fetches or unknowns" converts better than any feature list, because it tells buyers you understand the failure modes they have already been burned by. If you are building anything usage-billed, the binary will tempt you because it is simpler and it makes more money this week. Resist it. The third state is cheap insurance against the one outcome you can not recover from, which is a customer deciding your numbers can not be trusted. I build a few data tools on this rule (the public ones are at apify.com/mrlarryjohnson ). Happy to compare notes if you are designing a pay-per-result model. What is your third state?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/larry_johnson_e014cef9ad9/the-billing-state-most-apis-get-wrong-unknown-is-not-no-o9c

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
