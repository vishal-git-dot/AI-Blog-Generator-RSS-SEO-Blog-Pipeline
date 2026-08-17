---
title: "Nose ID: I Taught an AI to Recognize Dogs by Their Nose-Print"
slug: "nose-id-i-taught-an-ai-to-recognize-dogs-by-their-nose-print"
author: "Rimsha Shehzadi"
source: "devto_webdev"
published: "Mon, 17 Aug 2026 06:54:15 +0000"
description: "What I Built Nose ID — a biometric dog identification system. Instead of a collar tag, chip scanner, or manual lookup, it identifies a dog the way security s..."
keywords: "nose, dog, react, elevenlabs, their, print, new, embedding"
generated: "2026-08-17T07:04:47.154263"
---

# Nose ID: I Taught an AI to Recognize Dogs by Their Nose-Print

## Overview

What I Built Nose ID — a biometric dog identification system. Instead of a collar tag, chip scanner, or manual lookup, it identifies a dog the way security systems identify people: from a unique physical trait. In this case, the dog's nose-print — the ridge and texture pattern on a dog's nose, which is as individual to each dog as a fingerprint is to a human. Scan a dog's nose → the system tells you who it is (with a spoken voice response) or offers to enroll it if it's new. Demo How It Works 1. Embedding extraction (the core ML piece) Rather than training a nose-print classifier from scratch, I used a pretrained MobileNetV2 (ImageNet weights) as a feature extractor, stripping its classification head and using the penultimate layer's pooled output as a 1280-dimensional embedding vector. This is a standard transfer-learning technique — mid-level CNN filters trained on general images still respond well to texture, edges, and ridge patterns, which is exactly what distinguishes one nose-print from another. 2. Matching Each enrolled dog's embedding is L2-normalized and stored. A new scan's embedding is compared against all stored ones using cosine similarity . A similarity above a tuned threshold (0.90) counts as a match. 3. AI-generated personality On enrollment, Google Gemini generates a short, fun bio for each dog from its name and breed. 4. Voice confirmation On identification, ElevenLabs turns the result into a spoken response — "Welcome back, Bella. Access granted." or "I don't recognize this nose. Would you like to enroll?" Tech Stack Frontend: React (Vite) Backend: FastAPI (Python) ML: PyTorch, pretrained MobileNetV2, cosine similarity matching Google Gemini — dog bio generation ElevenLabs — text-to-speech voice confirmation Challenges I Ran Into Both Gemini and ElevenLabs changed parts of their APIs the same week I built this: Google's new API key format required switching from the legacy generateContent endpoint to their new Interactions API . ElevenLabs' free tier restricts which voices are callable via the API, even though the full library shows in their dashboard — had to query /v1/voices to find one my account could actually use. Try It rimsha-shehzadi98 / Nose_Print React + Vite This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules. Currently, two official plugins are available: @vitejs/plugin-react uses Oxc @vitejs/plugin-react-swc uses SWC React Compiler The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see this documentation . Expanding the ESLint configuration If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the TS template for information on how to integrate TypeScript and typescript-eslint in your project. View on GitHub Prize Categories Best use of Google AI Best use of ElevenLabs weekendchallenge

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rimshashehzadi98/nose-id-i-taught-an-ai-to-recognize-dogs-by-their-nose-print-l44

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
