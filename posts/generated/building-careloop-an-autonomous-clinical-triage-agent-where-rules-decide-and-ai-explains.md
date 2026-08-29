---
title: "Building CareLoop: an autonomous clinical-triage agent where rules decide and AI explains"
slug: "building-careloop-an-autonomous-clinical-triage-agent-where-rules-decide-and-ai-explains"
author: "prakhar gupta"
source: "devto_python"
published: "Sat, 29 Aug 2026 06:03:57 +0000"
description: "I created this content for the purposes of entering the All Things Agentic Hackathon. The problem that started it A doctor gets about eight minutes with a pa..."
keywords: "cloud, agent, patient, one, clinician, every, decision, triage"
generated: "2026-08-29T06:36:04.046443"
---

# Building CareLoop: an autonomous clinical-triage agent where rules decide and AI explains

## Overview

I created this content for the purposes of entering the All Things Agentic Hackathon. The problem that started it A doctor gets about eight minutes with a patient and, for anyone with a real history, forty pages of scattered records — lab reports, discharge notes, and pharmacy bills from three different clinics. So the history is effectively invisible at the exact moment it matters most. And when the visit ends, nothing follows up: the six-month course lapses at week five, the recheck never gets booked. I wanted to build an agent that closes that loop — one that reads the mess, decides urgency in a way a clinician can actually trust, and handles the follow-up on its own. That became CareLoop , my entry for the All Things Agentic Hackathon (Taskmaster track), built on Gemini, the Google Agent Development Kit (ADK), Cloud Run, and Firestore. The one principle I wouldn't compromise on Rules decide, AI explains. The temptation with an LLM is to let it do everything — including deciding whether a chest-pain patient is urgent. I refused to do that. In CareLoop, a deterministic engine owns every clinical decision: a weighted symptom score plus a red-flag override sets the triage level and routing. It is fully auditable, and it returns byte-identical output on the same input every single time. The LLM's job is strictly language: Reading unstructured documents into a fixed schema — I call it "Gemini extracts, rules merge." Writing the structured result into a plain-language brief a clinician can skim in ten seconds. No language model is ever in the decision path. When a judge asks "why was this Critical?", the answer is a score breakdown they can inspect — not a model's say-so. That single decision shaped the whole architecture. What it actually does CareLoop runs the full loop end to end: Ingest & compact — it reads a patient's documents and merges them into one structured ledger: allergies, chronic conditions, active medications, and lab trends over time. Instead of pushing forty pages into context on every visit, later steps read the compacted ledger. The satisfying part: three separate lab reports become a single trend line — HbA1c 6.8 → 7.2 → 7.5 — automatically. Triage — a patient describes symptoms; the deterministic engine scores probable conditions, assigns urgency, routes to a specialty, and escalates red flags (chest pain radiating to the arm, meningitis signs) instantly, bypassing the score. Brief the clinician — Gemini writes a summary that pulls in history, surfacing (for example) a penicillin allergy before anything is prescribed. Write back & bill — the clinician states their decision in the chat, the agent records it into the ledger, and the hospital pharmacy itemises the prescription plus the consultation fee (mock payment, clearly labeled). Follow up autonomously — a background sweep decides who is due for a refill and who needs a check-in, then sends the reminder. Because the doctor's prescription wrote into the ledger, the medicine prescribed today drives the reminder a month from now. That's the loop closing. How it's built Gemini 3.5 Flash via Google ADK powers the agent, its tools, and the dev UI. Cloud Run hosts the deployed agent with the web UI on the same origin. Firestore persists the patient ledger in the cloud; the Cloud Run service account reads and writes it. A deterministic Python core handles triage scoring, the compaction merge, and follow-up scheduling — no model involved — backed by 34 tests, including one that runs the same input twenty times and asserts identical output. Pluggable backends mean local vs. cloud storage and mock vs. real email are each one environment flip apart, so the whole system runs offline for testing and on Google Cloud for the demo. What I ran into Auth and CORS. Getting the agent talking to Gemini through the right path, and getting the dev UI past Cloud Shell's proxy (every JavaScript file 403'd until I passed the right allow-origins flag), took real iteration. The lesson that stuck: isolate the front end from the engine so you can debug each one cleanly instead of guessing. Cloud Build permissions. My first Cloud Run deploy failed because the default build service account was missing IAM roles — a genuinely common gotcha. Granting the build roles explicitly fixed it. Discipline over cleverness. Keeping the LLM out of every clinical decision was a constant design pressure. It would have been easier to let the model "just handle it." Not doing that is the whole point. What I learned Determinism is a feature, not a limitation. The single most valuable thing I built is a triage engine that gives the same answer on the same input, every time — because that is the difference between a tool a clinician can sign off on and a chatbot that guesses. A note on safety All patient data in the project is synthetic. The symptom/condition dataset is demo-grade, not a medical reference. Output is decision support for a licensed clinician, never a diagnosis. Payment and email are mocked and labeled as such. Built for the All Things Agentic Hackathon. #AllThingsAgenticHackathon

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/prakhar_gupta_b11e41958ac/building-careloop-an-autonomous-clinical-triage-agent-where-rules-decide-and-ai-explains-4eja

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
