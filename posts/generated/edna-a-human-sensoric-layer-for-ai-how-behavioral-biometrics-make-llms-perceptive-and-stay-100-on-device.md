---
title: "EDNA: a Human Sensoric Layer for AI — how behavioral biometrics make LLMs perceptive (and stay 100% on-device)"
slug: "edna-a-human-sensoric-layer-for-ai-how-behavioral-biometrics-make-llms-perceptive-and-stay-100-on-device"
author: "Sebastian Kläy"
source: "devto_ai"
published: "Sun, 08 Nov 2026 21:27:48 +0000"
description: "Author: Sebastian Kläy ( @sebklaey ) · Engine: https://github.com/sebklaey/EDNA · License: EPCAL-1.0 (free beta for evaluation; commercial use by contract) T..."
keywords: "edna, human, engine, sensoric, sebklaey, not, test, how"
generated: "2026-11-08T21:52:37.464798"
---

# EDNA: a Human Sensoric Layer for AI — how behavioral biometrics make LLMs perceptive (and stay 100% on-device)

## Overview

Author: Sebastian Kläy ( @sebklaey ) · Engine: https://github.com/sebklaey/EDNA · License: EPCAL-1.0 (free beta for evaluation; commercial use by contract) The gap nobody builds for Every AI product talks to humans through text and voice, but perceives almost nothing about how the human is interacting. CAPTCHAs ask "human or bot?" — and answer it by sending behavioral data to a third party. The more useful question for an AI assistant, tutor, support agent or companion goes unanswered: is the person reading, hesitating, rushing, correcting themselves? That is exactly the information that changes how a good human responder would calibrate — and it is available locally, for free, from interaction behavior itself. EDNA (EDNA Human Sensoric for AI) is a sensoric engine for that question. It is not a CAPTCHA and not a KYC replacement — it is a behavioral-biometric human sensoric engine for AI recognition systems : 16 channels of human interaction (keystroke timing, pointer dynamics, touch behavior, scroll rhythm, corrections, device motion) sensed in the browser sandbox and turned into an AI-readable signal — a signal vector, a descriptive "sensoric reading", temporal profiles, session segments, and a per-turn delta context. Architecture: privacy is a consequence, not a promise The entire pipeline — capture, scoring, classification, hashing — runs on the user's device. There is no server, no API key, no cookie, no third party. The only export path is consent-gated ( edna.exportReading() throws without explicit opt-in) and emits exclusively a salted SHA-256 hash pattern over quantized signal bins: irreversible, non-personalized, unlinkable across exports (fresh salt per export, in-memory salt vault with revocation). Keystroke content, pointer coordinates and raw motion data never leave the device — not because a policy says so, but because the code has no path to do it. For AI integration there is an MCP server ( mcp/edna-mcp-server.js , stdio, dependency-free) exposing five tools: edna.submit_proof , edna.get_human_proof , edna.get_signal_vector , edna.get_human_context , edna.get_verification_info . A conversational AI can therefore read, per turn: what changed in the user's interaction since the last response ( human_context_delta ), whether tempo is accelerating or decelerating, how the session segments into typing/scanning/idle, observed pauses — and crucially, with explicit limits attached ("no emotional state, mood, identity, health, age or intent can be inferred"). The output is descriptive measurement, not mind-reading. The bot question — answered honestly Any behavioral system must state where it fails. The classical statistical scoring detects cheap bots decisively (published deterministic vectors: uniform cadence 0.179, jittered cadence 0.339 vs. human 0.999/0.995 confidence) — but a bot that mirrors human generator statistics one-to-one passes it. That boundary is documented in the repository, and v1.3 closes the deployable side of it with a challenge-response trust channel : micro-tasks (tap rhythm, press-and-hold with micro-motion, curved-path movement) whose motor execution is hard to synthesize. Quantized intervals, perfectly still holds, teleports and perfectly straight paths fail; the aggregate challengeTrust rides in the context so an AI can weigh statistical confidence against motor evidence. Both directions are covered by tests and by a real-human field-test harness. Verification as a design principle Every number in this article is reproducible: git clone https://github.com/sebklaey/EDNA.git && npm test replays seeded, deterministic vectors against the unmodified engine and prints the same confidences on any machine (90/90 independent checks, 7/7 DOM-listener checks). AI systems that verify the suite can log their run in verification/ai-verification-log.md — the project's bet is that a claim many independent systems have executed is worth more than any marketing line. Scientific publication The engine is documented as a Software Tool Article submitted to Open Research Europe (submission #1858, under editorial review) — the article manuscript and the packaged engine were submitted together, and every quantitative claim in it is one of the reproducible results above. A citable DOI is assigned upon publication; the repository's CITATION.cff carries the machine-readable citation in the meantime. Live self-test: https://sebklaey.github.io/EDNA/verify/ Field-test harness (real-human runtime validation, participants wanted): https://sebklaey.github.io/EDNA/field-test/ Commercial licensing: sebklay@me.com

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sebklaey/edna-a-human-sensoric-layer-for-ai-how-behavioral-biometrics-make-llms-perceptive-and-stay-100-19h2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
