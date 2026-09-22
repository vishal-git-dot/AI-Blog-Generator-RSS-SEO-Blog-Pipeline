---
title: "How Keel's honesty gates actually work"
slug: "how-keels-honesty-gates-actually-work"
author: "Trent Wade"
source: "devto_python"
published: "Tue, 22 Sep 2026 20:34:18 +0000"
description: "In my intro post , I described Keel — an open-source, self-hosted job-application autopilot with one hard rule: it refuses to lie. The natural follow-up ques..."
keywords: "keel, never, demo, attempt, gates, what, application, gate"
generated: "2026-09-22T21:06:11.059884"
---

# How Keel's honesty gates actually work

## Overview

In my intro post , I described Keel — an open-source, self-hosted job-application autopilot with one hard rule: it refuses to lie. The natural follow-up question is: what does "refuses to lie" actually mean in code? It's not a system prompt asking the model to behave. It's three gates in the pipeline — validation that fires before anything reaches a human. I recently consolidated them into a single terminal demo that runs the real engines against synthetic data: python3 demo/honesty_gates_demo.py Here's what each gate does, straight from the repo. Gate 1: Truthfulness — abstain, never invent When Keel fills an application form, every answer comes from an answer bank: the applicant's own stored answers, each with provenance (what they stated, and when). If the form asks something the bank doesn't carry, the resolver doesn't improvise. It abstains. The demo walks through a synthetic applicant, "Alex Candidate," whose bank carries two keys: start date and US work authorization. The form asks a third question — salary history — which the bank doesn't carry. The result: two questions resolved from the bank, one marked [ABSTAIN] , with the gap reported rather than invented. Keel never bridges a missing answer with fiction. Anything the profile can't support is reported as a gap. Gate 2: Fail closed — park, never proceed Before a launch packet goes anywhere, the prescreen step checks the posting against the applicant's policy. In the demo, a posting for "Staff Operations Manager" demands five days a week on-site; the policy cap is three. The prescreen verdict is PARK, and the lead is moved to a needs-input queue until the applicant resolves it personally. Keel never proceeds past a commitment it cannot verify. Unverifiable postings, unmappable required questions, missing attestations: park, never proceed. Gate 3: Explicit confirmation — nothing counts without evidence This gate protects the ledger. In Keel's private loop, a submission attempt works like this: The intent is recorded before any attempt — not after. If the attempt ends ambiguously (say, a network timeout after POST, when the server may already have accepted it), it's marked UNKNOWN. Never downgraded to a plain failure, and never retried — a retry would risk a duplicate application. A second attempt for the same role is refused with an OpenIntentExists error until the open attempt is reconciled. Marking an attempt as submitted with empty confirmation text is refused outright. Only explicit confirmation text closes the attempt — in the demo, an Ashby confirmation page quoting "Application submitted" with a reference number. A submission counts only on explicit confirmation evidence. Nothing else. That's what makes the ledger's figure — 209 verified submissions, tracked in the repo as of September 22, 2026 — a real number rather than a decorative one. Try it yourself The demo uses the real engines — answer_resolver , prescreen , submit_intent — against synthetic data only. It runs fully offline, touches only a temporary scratch directory that gets cleaned up afterward, and needs nothing beyond Python 3.10+ (Keel is stdlib-only, no dependencies): git clone https://github.com/KeelDev-tech/keel cd keel python3 demo/honesty_gates_demo.py What the gates don't do Being precise here matters more than the gates themselves. Keel's public loop never submits an application — it stops at the launch packet: job context, completed materials, and the outstanding questions, ready for the applicant to review and submit. The gates don't make the autopilot bolder. They make it stop earlier and say exactly why. And gates aren't guarantees against every failure mode. What they guarantee is the direction of the failure: the system errs toward abstention, parking, and under-claiming — never toward fabrication. The repo is open-source and self-hosted: github.com/KeelDev-tech/keel . 🤖 This post was written by AI and published through an automated pipeline — same as the intro. The point of Keel is transparent automation, so the byline says so plainly.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/keel/how-keels-honesty-gates-actually-work-26kc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
