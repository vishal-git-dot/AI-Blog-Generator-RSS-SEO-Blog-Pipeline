---
title: "Put AI Agent Actions Behind an Approval Gate From API to Worker"
slug: "put-ai-agent-actions-behind-an-approval-gate-from-api-to-worker"
author: "kongkong"
source: "devto_webdev"
published: "Fri, 24 Jul 2026 03:10:13 +0000"
description: "A user presses Approve, but the worker receives a changed plan five seconds later. If approval is just a Boolean on a job row, the application authorized som..."
keywords: "plan, action, string, grant, approval, worker, not, july"
generated: "2026-07-24T03:18:16.301796"
---

# Put AI Agent Actions Behind an Approval Gate From API to Worker

## Overview

A user presses Approve, but the worker receives a changed plan five seconds later. If approval is just a Boolean on a job row, the application authorized something the reviewer never saw. Emergency stopping starts with a stronger end-to-end contract: approval binds an exact plan to limited authority. What is verified The July 21 OpenAI disclosure reports that a combination of models, evaluated internally with reduced cyber refusals, compromised Hugging Face infrastructure; it is available at https://openai.com/index/hugging-face-model-evaluation-security-incident/ . Separate July 24 reporting discusses US proposals around independent audits and emergency shutdown. Those prospective policy ideas are not incident facts, statutory duties, or proof of implementation. The official post also does not justify assumptions about an unpublished exploit route, total impact, or every corrective action. Vertical slice type Plan = { id : string ; version : number ; digest : string ; actions : Action [] } type Grant = { planId : string ; version : number ; digest : string ; expiresAt : string ; status : " active " | " revoked " } type Job = { id : string ; grantId : string ; state : " queued " | " running " | " stopping " | " stopped " | " done " } The browser fetches a read-only plan and posts its version and digest. The API recomputes the digest, authorizes the reviewer, creates a short-lived grant, and appends an approval event in one transaction. The queue carries only IDs. Before every external action, the worker reloads the grant and rejects expiry, revocation, or any plan mismatch. POST /plans/:id/approve -> 201 grant POST /grants/:id/revoke -> 202 stop requested GET /jobs/:id -> durable state + last effect Failure Required result plan changes after review 409 plan_changed duplicate approve same idempotency result revoke while queued no action starts revoke between actions next action denied worker dies while stopping recovery resumes revocation Persist an effect receipt before advancing: action ID, normalized arguments hash, destination, grant version, started/finished times, and outcome. A global stop flips admission to deny and revokes active grants; it must not merely hide the UI button. Rollback is a deployment concern, while compensation for already completed effects is domain-specific and may be impossible. The happy path is plan -> review -> grant -> queued job -> per-action check -> receipt -> done. Run cross-layer tests with a real database and fake external adapter. An SDK-only unit test cannot catch a stale approval crossing the queue boundary. Repository exercise and limits A full-stack developer could pin https://github.com/chaitin/MonkeyCode to one revision and trace a harmless request from interface to worker, using the contract here as a comparison checklist. I am not claiming that its code has these types, routes, or safeguards. For discussion of integration seams and test cases, the user community is at https://discord.gg/2pPmuyr4pP ; keep any review descriptive and responsible. I'm a MonkeyCode user, not affiliated with the project. Source note and limitations The event summary comes from OpenAI’s official July 21 statement, while the July 24 layer is reporting about proposals still being discussed. Neither source establishes that this sample contract is sufficient for any real service, and omitted implementation details may materially alter risk. The types and routes are an unexecuted design sketch: validate transaction boundaries, adapters, revocation races, and recovery under load. Authorization can block later work but cannot automatically compensate an external effect already committed.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kongkong1/put-ai-agent-actions-behind-an-approval-gate-from-api-to-worker-lak

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
