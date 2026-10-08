---
title: "Give your AI agent a fact-checker for text: AI detection, grammar and plagiarism over MCP"
slug: "give-your-ai-agent-a-fact-checker-for-text-ai-detection-grammar-and-plagiarism-over-mcp"
author: "João Reis"
source: "devto_webdev"
published: "Thu, 08 Oct 2026 12:59:16 +0000"
description: "More and more of the text that flows through our apps is written, edited or summarised by a language model. Content platforms want to know before they publis..."
keywords: "text, your, agent, probator, you, credits, detection, mcp"
generated: "2026-10-08T13:09:09.869985"
---

# Give your AI agent a fact-checker for text: AI detection, grammar and plagiarism over MCP

## Overview

More and more of the text that flows through our apps is written, edited or summarised by a language model. Content platforms want to know before they publish it. Schools want to know before they grade it. And under Article 50 of the EU AI Act, anyone publishing AI-generated text to inform the public will need to label it. Probator.ai checks a text for three things in one call: AI generation : a likelihood and a verdict, sentence by sentence, with the evidence behind it; Grammar and style : corrections with explanations, never applied for you; Plagiarism : matching sources from the web, academic databases and Wikipedia in every language. It also reports hidden characters, look-alike letters and AI provenance marks (C2PA, IPTC labels, invisible Unicode tags used for hidden prompts). It works in 100+ languages, and you can call it from your code or let your AI agent call it directly. For agents: one line of MCP config Probator runs a remote MCP server. Add it to any client that speaks MCP over HTTP (Claude, Cursor, VS Code, your own agent): { "mcpServers" : { "probator" : { "type" : "http" , "url" : "https://probator.ai/mcp" } } } The first call returns a 401 that points the client to OAuth 2.1. The client registers itself, you sign in and approve, and that's it: no keys to copy around. If your agent prefers a key, add "headers": { "Authorization": "Bearer pb_live_…" } instead. Your agent gets five tools: Tool What it does check_ai AI-text detection with evidence and provenance marks check_grammar corrections, with explanations in 6 languages check_plagiarism originality score and matching sources check_all all three in one call get_credits plan and remaining credits (free) Agents that can't run an OAuth client can still register: they send the person's email, the person signs in, and types a 6-digit code the agent shows them. The details are in auth.md . For your code: a plain REST API curl https://probator.ai/v1/detect \ -H "Authorization: Bearer $PROBATOR_KEY " \ -H "Content-Type: application/json" \ -d '{"text": "Paste the text you want to check here..."}' { "verdict" : { "key" : "likely_ai" , "p_ai" : 0.94 , "confidence" : "high" , "guards" : [] }, "sentences" : [ … ], "evidence" : [ … ], "provenance" : { "declared" : null , "marks" : [] }, "credits" : { "used" : 142 , "remaining" : 499858 } } Endpoints: /v1/analyze runs any combination of checks, and also accepts PDF, Word, Markdown, HTML and text files. /v1/detect , /v1/grammar and /v1/plagiarism run a single check each, and /v1/usage returns your plan and credits. Errors: every error has a stable code ( insufficient_credits , too_many_words , rate_limited ), and every response carries x-credits-used and x-credits-remaining headers. Specs: the OpenAPI file is public, and so are llms.txt and llms-full.txt , so your coding assistant can read the docs itself. How the detection works (and why you can trust a "no") Most AI detectors give you one opaque number. Probator combines four independent signals: Its own detection model: a classifier over multilingual sentence embeddings, trained on human and AI-written text in six languages, including AI-polished and "humanized" text. An expert reading by a language model that quotes the passages it finds suspicious. A rewrite test: machine text changes little when a model polishes it again. Forensic evidence: chatbot leftovers, invisible characters, look-alike letters, file metadata. A false positive costs much more than a miss, so the engine is built to avoid them: Short texts: no "AI-generated" verdict under 80 words without hard evidence. Strongest verdict: two detectors must agree. Per-language thresholds: calibrated to keep false positives on human text at 1% or less. When a guard changes a result, the report tells you which one, in verdict.guards . On held-out test documents the model scores 98.4% accuracy and an AUROC of 0.998 . Results by language are published on the accuracy page . Results are probabilities with reasons, not proof. Use them to decide what a person should review, not to decide about a person. What people build with it Publishing pipelines: check articles before they go live and add the AI disclosure where it's needed. Learning platforms: run submissions through detection and plagiarism, then show teachers the evidence, not just a score. Editorial and review agents: an agent that triages incoming text, flags what needs a human, and fixes the grammar on the rest. Moderation queues: catch generated spam and copied content across languages. Signed certificates: turn a check into a PDF certificate with an Ed25519 signature that anyone can verify . Privacy, briefly Saved documents and the account database stay in the EU. Texts are never used to train models, and the language models it uses are called with no retention and no training. Probator reports hidden marks and AI labels but never removes them. Try it Free: 5,000 credits a month in the web editor , no card needed. AI detection costs 1 credit per word. API and MCP: included in Pro (€12.99 a month, 500,000 credits) and Team (€39 a month for 3 seats, 2,000,000 shared credits). Docs: probator.ai/docs/api I'd love to hear what you'd plug it into, and what your agent would need from a tool like this. Drop it in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mrjootta/give-your-ai-agent-a-fact-checker-for-text-ai-detection-grammar-and-plagiarism-over-mcp-54mm

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
