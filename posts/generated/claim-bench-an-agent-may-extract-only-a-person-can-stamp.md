---
title: "Claim Bench — an agent may extract, only a person can stamp"
slug: "claim-bench-an-agent-may-extract-only-a-person-can-stamp"
author: "Nakabiri Knolz"
source: "devto_webdev"
published: "Mon, 21 Sep 2026 04:18:31 +0000"
description: "This is a submission for the Sanity Challenge , Path Two: Vibe-Code Something Strange What I Built Claim Bench is the editor side of CabinClaim. It is not an..."
keywords: "agent, bench, claim, app, two, state, path, not"
generated: "2026-09-21T04:21:01.281458"
---

# Claim Bench — an agent may extract, only a person can stamp

## Overview

This is a submission for the Sanity Challenge , Path Two: Vibe-Code Something Strange What I Built Claim Bench is the editor side of CabinClaim. It is not another read-only frontend of the desk. The desk in Path One answers cabin questions from dated ruleClaim documents. Path Two is the process that gets a claim to a state the desk is allowed to trust. Left pane: the official excerpt, still linked to the live TSA or United page. Right pane: the structured claim plus a claimWorkflow document that lives next to it in the same dataset. The states are data, not a UI enum: ingested → extracted → disputed | approved → superseded Two seats share those transitions. An agent may ingest and extract. An agent may mark a pair of quotes disputed. The approve button is visible from the agent seat. Pressing it returns 403: The agent's hand cannot hold the stamp. decidedBy stays empty. agentAttemptCount goes up. Sit as human, press the same button, and the document becomes approved . That is the product. The agent can move work forward. A person has to hold the stamp. Demo Claim Bench (no login): https://cabinclaim.vercel.app/bench Desk (Path One): https://cabinclaim.vercel.app Studio, grouped by workflow state: https://cabinclaim.vercel.app/studio Public workflow documents: current claimWorkflow rows No login is required on the bench. Judge test — do this in order: Open /bench . You are seated as agent . Find the extracted lithium 100Wh claim. Press Try stamp (should fail) . The card stays extracted . decidedBy stays empty. The attempt count goes up. Switch the seat to human . Press Stamp approve . State becomes approved . decidedBy is human . The disputed spare-count pair is the same United vs TSA conflict the desk already shows. An agent can keep them disputed. A person has to approve one or both. The Studio lists the same documents under Ingested, Extracted, Disputed, Approved, Superseded. The bench and the Studio are two interfaces on one process. Code GitHub: https://github.com/python07070/cabinclaim src/sanity/schemaTypes/workflow.ts — claimWorkflow next to the claim src/lib/workflowRules.ts — allowed moves, and the human-only stamp app/bench/page.tsx — two seats, official excerpt vs structured claim app/api/bench/transition/route.ts — writes state; 403 on agent approve src/sanity/structure.ts — Studio grouped by workflow state The rule the API will not bend: if ( to === " approved " && actor === " agent " ) { return " The agent's hand cannot hold the stamp. Only a person can approve. " ; } How I Used Sanity Same project as Path One ( x9n6hu5i / production ). Path Two adds a first-class process document instead of hiding status on the claim. A ruleClaim is still one official sentence: operator, value, dates, source URL, quote. A claimWorkflow points at that claim and stores state , lastActor , decidedBy , decidedAt , and agentAttemptCount . The process is queryable. GROQ can ask for every extracted claim waiting on a human, or every disputed pair, without scraping a UI. Studio is customized around that process. The default document list is replaced with panes by state, plus a badge that the stamp is human-only. Opening /studio is opening the queue, not a generic CMS. I prompted this in Cursor. The first Path Two schema I accepted was a portable-text body plus a status string on the claim itself. The agent then wanted to “approve” by rewriting the quote. That is how a blog template gets built. I deleted the body field and made workflow its own type so an agent can change state without being allowed to change the official sentence. Workflows, on purpose This is the Path Two bonus I actually shipped. Content review is modeled as data next to the content. The agent and the person call the same transition route. The difference is one guard: approve is human-only. After a human stamps, decidedBy is no longer empty. A later agent run can read that field and know which claims the desk may treat as trusted. The spare-count pair starts disputed because the two official pages do not say the same thing. The agent is not allowed to pick a winner. That is the same refusal as Path One, turned into a workflow state. App SDK, and why the bench is Next.js I read the App SDK docs and started a @sanity/sdk-react shell. Real-time useDocuments is the feature the brief asks for. The SDK’s live bindings assume Sanity Dashboard auth. This contest is judged without a login. A Dashboard-only bench would have been a polished demo I could not hand a judge. So the shipped bench is a custom Next.js app on top of the same workflow documents: two seats, your own interface, polling /api/bench/queue every four seconds. It is not a read-only frontend of the desk. It writes claimWorkflow state. It is also not a Dashboard App SDK app. If I had pretended otherwise, the writeup would be the lie. The honest version: I used the Workflows bonus as specified, and I used the App SDK idea (custom app, live queue, own UI) without the Dashboard login the current SDK requires. Sanity Project Details Project ID: x9n6hu5i Dataset: production Organization: opm3ppvty

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nakabiri_knolz_c215da66a1/claim-bench-an-agent-may-extract-only-a-person-can-stamp-2049

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
