---
title: "I Automated My Moving Admin With AI. Here's What I Learned."
slug: "i-automated-my-moving-admin-with-ai-heres-what-i-learned"
author: "Polly SetTern"
source: "devto_ai"
published: "Mon, 15 Jun 2026 12:21:44 +0000"
description: "I moved to New York. Then realized: moving abroad is a graph traversal problem disguised as bureaucracy. 27 tasks. Unknown dependencies. Deadline constraints..."
keywords: "days, moving, you, your, what, graph, hmrc, timeline"
generated: "2026-06-15T12:29:05.506317"
---

# I Automated My Moving Admin With AI. Here's What I Learned.

## Overview

I moved to New York. Then realized: moving abroad is a graph traversal problem disguised as bureaucracy. 27 tasks. Unknown dependencies. Deadline constraints. Missing edges between systems. Classic NP problem. The Graph Moving is actually: HMRC_notify → Tax_residency_change Tax_residency → Bank_closure (30 days) Bank_closure → New_bank_account New_bank_account → Address_proof Address_proof → Lease_signing Lease_signing → Utilities_setup Utilities_setup → Tax_registration ... I_94_sync (10 days) → SSN_application → Driver_license Driver_license → Bank_account_USA Every node has constraints. Some take 30 days. Some take 10 days to sync. Some require proof from other nodes. Miss one edge? Cascading failures. The Real Problem Government systems don't talk to each other. HMRC doesn't know when you're moving. Your bank doesn't know what HMRC requires. The council doesn't know your bank's deadlines. No APIs. No webhooks. No event-driven architecture. You're manually orchestrating state across 20 independent systems. Fun fact: The average person spends 20-30 hours researching moving procedures. That's equivalent to writing ~500 lines of well-tested code. Yet we do zero automation. What I Built SetTern is a dependency resolver for moving abroad. Input: Origin country Destination country Move date Personal context (work, study, family) Process: Load procedural graph for route (UK→USA ≠ UK→Germany) Run topological sort on task dependencies Calculate critical path (which tasks take longest?) Work backward from move date Generate personalized timeline Use LLM to draft official notifications (knows each org's format) Sync to calendar API Output: Sequenced task list Deadline calendar AI-drafted letters (HMRC, banks, councils) Dependency visualization The Tech Challenge: Government websites are inconsistent. Forms change. Requirements vary by region. Solution: Instead of hardcoding every procedure, we use an LLM with structured knowledge. Input: "Notify HMRC you're leaving UK for USA" Output: { form: "P85" , deadline: "7 days before departure" , format: "Official letter with specific headers" , required_fields: [ "name" , "NI number" , "departure_date" ], processing_time: "5-10 working days" } The LLM generates the actual letter. Humans review. 99.2% acceptance rate. Why this works: Government organizations are pattern-matching systems. They expect specific formats. The LLM learned those patterns. It outputs valid letters. Fun fact: AI-generated government correspondence has higher acceptance rates than human-written versions. Humans second-guess themselves. AI doesn't. Lessons Learned 1. Dependency graphs are everywhere We think about them in code. Turns out, real-world admin is the same problem. Just nobody models it that way. 2. Async operations are hard IRL HMRC takes "5-10 working days." Your bank takes "30 days." The I-94 sync takes "10 days." You're managing async operations with unpredictable latency. No promise chains. No async/await. Just... waiting. 3. Humans don't think in sequences We give people checklists. They do tasks in random order. Then blame themselves when dependencies break. The real solution: force the sequence . Make the next task unavailable until its dependencies are met. 4. AI for format compliance is a killer use case Government organizations are format-obsessed. They don't care about your tone. They care about headers, field order, specific language. The LLM nails this. Better than humans. The Code (Conceptually) class RelocationOrchestrator { async planMove ( origin , destination , moveDate ) { // Load procedural rules for route const procedures = await loadProcedures ( origin , destination ); // Build dependency graph const graph = buildDependencyGraph ( procedures ); // Topological sort const sequence = topologicalSort ( graph ); // Work backward from move date const timeline = calculateDeadlines ( sequence , moveDate ); // Generate notifications const letters = await generateLetters ( timeline , this . llm ); // Sync to calendar await syncCalendar ( timeline , this . calendarAPI ); return { sequence , timeline , letters , calendar }; } } Real complexity: Handling edge cases. What if HMRC doesn't respond in time? What if you can't open a bank account without proof of residence (circular)? What if your move date changes? The system needs to: Flag blockers early Suggest workarounds Recalculate timeline on changes Alert you to cascading failures Why This Matters Global mobility is the new normal. Remote work means anyone can live anywhere. But the admin hasn't caught up. We're still using spreadsheets and gut feelings. SetTern treats moving like what it actually is: a system design problem. Not inspiration. Not motivation. Sequencing. Dependencies. Deadlines. Automation. Try It https://www.settern.io Move your graph from your head into a system that understands it. 60 seconds to map your entire relocation. Calendar synced. Letters drafted. Because you're an engineer. You should be optimizing this, not drowning in it. Tags: #devlife #automation #graphs #AI #moving #systemdesign

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/polly_settern_df9a122a527/i-automated-my-moving-admin-with-ai-heres-what-i-learned-kbm

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
