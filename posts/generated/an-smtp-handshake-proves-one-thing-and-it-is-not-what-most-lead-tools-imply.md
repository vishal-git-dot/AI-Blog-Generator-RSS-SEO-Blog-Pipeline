---
title: "An SMTP handshake proves one thing, and it is not what most lead tools imply"
slug: "an-smtp-handshake-proves-one-thing-and-it-is-not-what-most-lead-tools-imply"
author: "Axel Freeman"
source: "devto_webdev"
published: "Fri, 18 Sep 2026 10:45:57 +0000"
description: "Every "email verification" feature I have integrated does the same thing under the hood: it opens a connection to the recipient's mail server and asks about ..."
keywords: "not, verification, what, server, mailbox, you, does, bounce"
generated: "2026-09-18T10:56:11.756237"
---

# An SMTP handshake proves one thing, and it is not what most lead tools imply

## Overview

Every "email verification" feature I have integrated does the same thing under the hood: it opens a connection to the recipient's mail server and asks about a specific mailbox. That is the entire mechanism. The interesting part is not the protocol — it is what the answer does and does not mean, and when you asked. The question you are actually asking The handshake goes roughly: connect, EHLO , MAIL FROM , then RCPT TO:<address> . The server replies to that last line. Four shapes of reply matter: Reply What it means What to do 250 on RCPT TO The server accepts this mailbox right now Safe to send 550 / 551 The mailbox does not exist, or is refused Drop it — it is a hard bounce 450 / 451 Temporary: greylisting, rate limiting, server busy Retry later; it is not invalid Catch-all domain The server accepts anything , so the reply says nothing about the individual address Mark unverified, do not count it as valid That is the whole truth of the category. A tool that reports a clean binary "valid / invalid" and hides which of those four cases it hit is hiding the only part that changes your decision. Two clocks The reason stored lists bounce is not that verification was done badly. It is that verification was done early . Addresses have a half-life: 40% of email addresses go dead within two years ( NeverBounce ) 23% of business contacts change jobs each year ( ZoomInfo, 2025 ) — and the mailbox usually follows the person Freshly sourced data outperforms stale stored records by 42% ( Harvard Business Review, 2024 ) So the useful way to think about a verification result is as a timestamp, not a property . A list verified at import and sent three weeks later is an unverified list with extra steps. Measured bounce, in practice, lands where you would expect: 2–5% for addresses checked at the moment of use, 10–35% for stored lists. Why an agent makes this worse, not better A human running an outbound campaign sees the bounce report and adjusts. An agent calling a tool gets a response object and moves on — it will not notice that 18% of the addresses it was handed are dead, because nothing in the response told it. If verification is a separate step, the agent has to remember to take it, and the gap between the two calls is exactly where decay happens. What I did about it In TAPAC the handshake happens inside the search call. You ask for contacts by industry, job titles, company size, geography and source ( website , telegram , discord ), and every address in the response is SMTP-checked while the response is being assembled. There is no second pass to schedule: curl -X POST https://tapacapi.com/v1/contacts/search \ -H "Authorization: Bearer $TAPAC_API_KEY " \ -H "Content-Type: application/json" \ -d '{"industry":"saas","job_titles":["head of growth"],"limit":10}' Standalone verification exists too ( POST /v1/contacts/verify ) for lists you already own, and it is billed the same way — 100 free searches, then $0.10–0.50 per verified contact, pay-per-use, no seat licence. Agents can call it over MCP with npx -y @tapacapi/mcp . The honest limits A 250 proves the mailbox exists now. It says nothing about whether anyone will answer. Catch-all and greylisting servers refuse to give a clean answer. No method fixes that; it can only be labelled honestly. Some providers rate-limit verification traffic, so a check can return "unknown". Unknown is not "send anyway". Verification is not a quality score for your outreach. It is one fact, with a date attached — and the date is the part most stacks throw away.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/axelfreeman/an-smtp-handshake-proves-one-thing-and-it-is-not-what-most-lead-tools-imply-2lpk

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
