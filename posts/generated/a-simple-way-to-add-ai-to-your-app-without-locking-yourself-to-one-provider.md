---
title: "A Simple Way to Add AI to Your App Without Locking Yourself to One Provider"
slug: "a-simple-way-to-add-ai-to-your-app-without-locking-yourself-to-one-provider"
author: "Aarnav Saboo"
source: "devto_webdev"
published: "Fri, 02 Oct 2026 04:43:21 +0000"
description: "Adding an LLM to an application is easy. The annoying part usually comes six months later. Maybe you started with OpenAI, then another model becomes better f..."
keywords: "provider, model, application, openai, anthropic, your, sdk, const"
generated: "2026-10-02T05:02:05.617192"
---

# A Simple Way to Add AI to Your App Without Locking Yourself to One Provider

## Overview

Adding an LLM to an application is easy. The annoying part usually comes six months later. Maybe you started with OpenAI, then another model becomes better for one particular task. Or you want to use a cheaper model for background jobs and a stronger model for user-facing requests. If model-specific code is scattered throughout the application, changing providers becomes unnecessarily painful. A pattern I like is keeping the AI layer very small. Keep the rest of your app model-agnostic For a TypeScript project, an open-source option for this is the AI SDK. Install the core package and whichever providers you need: npm install ai @ai-sdk/openai @ai-sdk/anthropic Instead of calling provider SDKs directly from controllers, routes, or UI code, create one small AI module. // lib/ai.ts import { generateText } from " ai " ; import { openai } from " @ai-sdk/openai " ; import { anthropic } from " @ai-sdk/anthropic " ; const models = { openai : openai ( process . env . OPENAI_MODEL ! ), anthropic : anthropic ( process . env . ANTHROPIC_MODEL ! ) }; export async function askAI ( prompt : string , provider : keyof typeof models = " openai " ) { const { text } = await generateText ({ model : models [ provider ], prompt }); return text ; } Now the rest of the application doesn't really care which company is serving the model. const summary = await askAI ( " Summarize this customer support conversation " , " anthropic " ); The useful part isn't saving a few lines of code. It's creating a boundary. Why the boundary matters Once AI starts appearing in multiple parts of a product, it's very easy to end up with something like this: /api/chat -> Provider A /api/summarize -> Provider A /jobs/classify -> Provider A /api/search -> Provider A /admin/generate -> Provider A Then configuration, retries, logging and prompts slowly get duplicated everywhere. I'd rather have: Application | v AI Layer | +---- Provider A +---- Provider B +---- Local/Open Model The application talks to your AI layer. The AI layer decides where the request goes. Model selection can then become application logic Once this abstraction exists, routing doesn't need to be static either. For example: export async function generateForTask ( task : " classification " | " reasoning " , prompt : string ) { const provider = task === " classification " ? " openai " : " anthropic " ; return askAI ( prompt , provider ); } In a real application I would probably take this further and route based on things like: task type latency requirements cost context size provider availability required capabilities This also gives you one place to add observability. const started = Date . now (); try { const result = await askAI ( prompt , provider ); console . log ({ provider , duration : Date . now () - started , success : true }); return result ; } catch ( error ) { console . error ({ provider , duration : Date . now () - started , success : false }); throw error ; } Nothing complicated, but suddenly debugging AI requests becomes much easier. Don't expose the AI provider directly to the frontend Another thing I try to avoid is letting the UI know too much about the underlying provider. The frontend should ideally call something like: POST /api/summarize rather than: POST /api/openai/generate Your product feature is summarization . OpenAI, Anthropic, Gemini or a local model is an implementation detail. That distinction becomes useful surprisingly quickly. Open-source tools make this easier There are a few interesting projects solving different parts of this problem. Vercel AI SDK provides a common TypeScript interface for working with multiple AI providers. LiteLLM takes a similar idea further on the infrastructure side, providing a unified interface and an optional self-hosted gateway for many different model providers. For applications that need tools and external integrations, Model Context Protocol (MCP) is also worth looking at. Instead of writing a completely different integration system for every AI client, MCP provides a common protocol for exposing tools and resources. They solve different problems, but they point in roughly the same direction: Keep your application architecture separate from whichever AI model happens to be popular today. The main takeaway I don't think most applications need a huge "AI platform" abstraction from day one. A small module is usually enough. The important part is simply avoiding provider-specific calls everywhere in the codebase. Start with: App -> AI abstraction -> Provider Then add routing, fallbacks, logging, caching and more advanced infrastructure only when the application actually needs them. AI models are changing too quickly to make them the foundation of your application architecture. Your product should depend on a capability. Not a model name.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/aarnavsaboo/a-simple-way-to-add-ai-to-your-app-without-locking-yourself-to-one-provider-5f8h

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
