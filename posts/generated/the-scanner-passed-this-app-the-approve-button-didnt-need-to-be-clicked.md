---
title: "The Scanner Passed This App. The Approve Button Didn't Need to Be Clicked."
slug: "the-scanner-passed-this-app-the-approve-button-didnt-need-to-be-clicked"
author: "Rocky"
source: "devto_webdev"
published: "Sun, 30 Aug 2026 16:20:40 +0000"
description: "The scanner comes back clean. No SQLi, no XSS, auth and session handling look solid, every endpoint requires a valid token. It's an internal expense reimburs..."
keywords: "report, you, approve, every, only, testing, one, what"
generated: "2026-08-30T16:26:18.039651"
---

# The Scanner Passed This App. The Approve Button Didn't Need to Be Clicked.

## Overview

The scanner comes back clean. No SQLi, no XSS, auth and session handling look solid, every endpoint requires a valid token. It's an internal expense reimbursement app: an employee submits a report, a manager approves it, finance pays it out. By every automated check, this thing is fine. Then you stop testing endpoints one at a time and start testing the workflow as a sequence. You submit an expense report as the employee. Instead of waiting for the manager to click approve, you look at what that button actually does: it's a POST to /api/reports/{id}/approve , checked for a valid session token, but the only role check on the endpoint is "is this a logged-in user," not "is this user the assigned approver for this specific report." You replay that request under your own employee session, against your own report ID. It goes through. You just approved your own expense report. No injection. No broken authentication. Every individual endpoint did what it was supposed to do when tested in isolation. The vulnerability only exists in the gap between them: the app has a state machine ( draft -> submitted -> pending_approval -> approved -> paid ) and enforces almost none of the transition rules that make that state machine mean anything. Why this class of bug survives automated scanning A scanner tests endpoints against a fixed model of what a request should look like. It doesn't know that /approve is supposed to only be reachable by a manager for reports they don't own, because nothing in the request itself signals that constraint, it lives entirely in the intended business logic, which usually only exists in a product spec or a developer's head. The same is true for fuzzers hammering one endpoint at a time: they'll never discover that the bug requires calling two endpoints in the wrong order, or skipping one step in a sequence a human designer assumed everyone would follow because the UI only exposes buttons in that order. That's the actual skill gap between clearing the OWASP Top 10 and finding the bugs that get chained into something a client actually cares about: understanding that a web app is often a state machine wearing a UI, and that the interesting failures live in the transitions, not the individual states. A workflow-logic checklist that catches this class Map the intended state machine before you touch a single payload. Every status a resource can be in, every transition between them, and who is supposed to be allowed to trigger each one. For every transition, ask where the role check actually lives. Is "only a manager can approve" enforced server-side against the specific report's assigned approver, or is it just that the approve button is hidden in the UI for non-managers? Hidden buttons are not access control. Test transitions out of order. Can you reach approved without ever passing through pending_approval ? Can you resubmit a report that's already paid ? Test a transition under the wrong identity. Take the exact request the intended role sends and replay it as a different role or a different owner. If it succeeds, the check that should have blocked it doesn't exist. Look for idempotency gaps as a second bug riding the first. If approval isn't checked for "already approved," a self-approval bug can sometimes be chained into a double-payout by replaying it. None of this shows up in a Top 10 checklist, and that's the point. Business logic and chained exploitation are what separate testing that finds the known categories from testing that finds what a specific application actually got wrong, which is usually the finding that changes a client's risk posture instead of just filling a page in the report. That's the exact territory the Advanced Web Application Penetration Testing Book (L2) is built around: past single-bug OWASP coverage, into the business-logic and chained-attack thinking that catches a workflow like this one before someone with less good intentions does.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rockyyy/the-scanner-passed-this-app-the-approve-button-didnt-need-to-be-clicked-1llm

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
