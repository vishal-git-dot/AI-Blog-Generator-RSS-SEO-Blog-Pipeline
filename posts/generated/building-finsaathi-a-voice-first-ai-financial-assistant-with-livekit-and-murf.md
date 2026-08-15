---
title: "Building FinSaathi: A Voice-First AI Financial Assistant with LiveKit and Murf"
slug: "building-finsaathi-a-voice-first-ai-financial-assistant-with-livekit-and-murf"
author: "Astha Bansal"
source: "devto_python"
published: "Sat, 15 Aug 2026 18:29:43 +0000"
description: "Building FinSaathi: A Voice-First AI Financial Assistant Financial information can be difficult to understand. Banking terms, loans, credit scores, payments,..."
keywords: "voice, livekit, finsaathi, production, agent, first, next, application"
generated: "2026-08-15T18:36:33.510608"
---

# Building FinSaathi: A Voice-First AI Financial Assistant with LiveKit and Murf

## Overview

Building FinSaathi: A Voice-First AI Financial Assistant Financial information can be difficult to understand. Banking terms, loans, credit scores, payments, and other financial decisions can quickly become overwhelming when users have to navigate everything through forms and complicated interfaces. So I wanted to explore a simpler interaction: What if financial guidance could start with a conversation? That idea became FinSaathi , a voice-first AI financial assistant. What I Built The first goal was simple: get a real-time voice assistant working end-to-end and deploy it. The current architecture is: Next.js Frontend → LiveKit → Python AI Agent → Voice/AI Services The frontend is deployed on Vercel, while the LiveKit agent is deployed on Railway. Users can open the application, start a conversation, and interact with the FinSaathi agent through voice. The Tech Stack Frontend Next.js React TypeScript LiveKit Components Tailwind CSS Vercel Backend Python LiveKit Agents UV Docker Railway Voice / AI LiveKit Murf AI/LLM services Data SQLite for application memory and call-related data The Part That Took More Time Than Expected Getting the agent to work locally was relatively straightforward. Getting the same system to actually run in production was a different problem. The Railway deployment initially failed with: python: can't open file '//src/agent.py': [Errno 2] No such file or directory The problem turned out to be related to how the application path and startup command were being handled inside the Docker deployment. After fixing the container and Railway startup configuration, the deployment moved further — and exposed another issue. Because the container runs the application as a non-root user, UV initially could not create its cache directory: Permission denied: '/app/.cache/uv' Fixing the permissions allowed the actual LiveKit AgentServer to start successfully. The production logs then showed the agent listening for connections and registering its worker with LiveKit. That was the first real milestone: the backend was no longer just "working on my machine" — it was actually running in production. Testing the Voice Pipeline After the backend was live, I tested the frontend against the production LiveKit setup. The voice interaction worked end-to-end. The user can speak to FinSaathi, the session connects through LiveKit, and the deployed agent processes the conversation and responds through the voice pipeline. This was the main goal of the first phase. Memory and Analytics FinSaathi also has a SQLite-based memory and call analytics layer. The local application works with this storage layer, but deployment exposed a file-permission issue when the application attempted to write to the SQLite database during session completion. So this part is not being treated as completely solved yet . The next step is to move this production storage layer to a more appropriate persistent database/storage setup instead of relying on a writable SQLite file inside the application container. What's Next? The current interface is intentionally focused on the core voice experience. The next phase will be about turning the working prototype into a more complete product. Planned improvements include: A dedicated FinSaathi landing page Improved voice interaction UI Authentication Human-support / escalation dashboard Call analytics dashboard Persistent production database Better observability Expanded language support The escalation and analytics pieces are being designed around the idea that an AI assistant should know when a conversation needs human support rather than trying to handle every situation itself. Current Status The core voice system is now deployed. Currently working: Next.js frontend LiveKit real-time connection Python LiveKit agent Murf voice integration Production deployment on Railway Production frontend deployment on Vercel End-to-end voice interaction Still being improved: Production database persistence Analytics storage Escalation dashboard Landing page Authentication Live Demo https://finsaathi-alpha.vercel.app GitHub https://github.com/true-brace05/murf-livekit-starter This is only the first phase of FinSaathi, but getting the complete voice pipeline from a local prototype to a deployed system was a valuable engineering milestone. The next phase is about building the product around that core.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/truebrace05/building-finsaathi-a-voice-first-ai-financial-assistant-with-livekit-and-murf-4pfe

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
