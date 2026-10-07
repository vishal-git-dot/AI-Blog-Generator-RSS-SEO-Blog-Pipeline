---
title: "Measure Cost per Handled Enquiry: A Small Logging Pattern for LLM Workflows"
slug: "measure-cost-per-handled-enquiry-a-small-logging-pattern-for-llm-workflows"
author: "Ujjwal Dubey"
source: "devto_python"
published: "Wed, 07 Oct 2026 05:03:01 +0000"
description: "Pre-build cost estimates are guesses. After launch you can measure. The most useful number I know for a small-business workflow is cost per handled enquiry i..."
keywords: "per, none, cost, your, eid, enquiry, model, qty"
generated: "2026-10-07T05:20:33.231434"
---

# Measure Cost per Handled Enquiry: A Small Logging Pattern for LLM Workflows

## Overview

Pre-build cost estimates are guesses. After launch you can measure. The most useful number I know for a small-business workflow is cost per handled enquiry in AI automation : everything it cost to take one customer message from arrival to a resolved state. Disclosure: I run NxFlowAI, an automation agency. The pattern below is generic. What to count For each enquiry, record: model tokens in and out (per call) messaging events (per message sent, by category, using your provider's billing categories) automation-platform runs or tasks human minutes (time spent approving or rewriting a draft) A minimal event log import json , time , uuid LOG = " cost_events.jsonl " def log_event ( enquiry_id , kind , qty , meta = None ): with open ( LOG , " a " ) as f : f . write ( json . dumps ({ " ts " : time . time (), " enquiry_id " : enquiry_id , " kind " : kind , " qty " : qty , " meta " : meta or {}}) + " \n " ) # inside your workflow eid = str ( uuid . uuid4 ()) log_event ( eid , " tokens_in " , 812 , { " model " : " your-model " }) log_event ( eid , " tokens_out " , 164 , { " model " : " your-model " }) log_event ( eid , " wa_message " , 1 , { " category " : " service " }) log_event ( eid , " platform_run " , 3 ) log_event ( eid , " human_minutes " , 2 , { " step " : " approve_quote_reply " }) Roll it up with your own rates from collections import defaultdict RATES = { # fill in from your own invoices; units must match qty " tokens_in " : None , " tokens_out " : None , " wa_message " : None , " platform_run " : None , " human_minutes " : None , } def cost_per_enquiry ( path = LOG ): per = defaultdict ( float ) for line in open ( path ): e = json . loads ( line ) rate = RATES . get ( e [ " kind " ]) if rate is not None : per [ e [ " enquiry_id " ]] += e [ " qty " ] * rate return per What the numbers tell you Human minutes dominate more often than tokens. If approvals take most of the cost, look at which drafts are rejected and why. Long prompts show up fast. If token cost per enquiry is creeping up, check what context you are stuffing into every call. Retries hide in platform runs. A spike in runs per enquiry usually means a failing step. Keep it boring Append-only JSONL, one roll-up script, a weekly look. That is enough for most small businesses. Ship a dashboard later if anyone actually opens it. We set this up as part of monitoring after the 72-hour audit and build. If you are still deciding whether to go custom at all, our custom AI vs off-the-shelf chatbot comparison covers the trade-offs.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ujjwal_dubey_9/measure-cost-per-handled-enquiry-a-small-logging-pattern-for-llm-workflows-51ni

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
