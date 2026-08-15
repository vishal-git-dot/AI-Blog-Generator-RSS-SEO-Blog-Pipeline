---
title: "Building Samar: My 10-Day Voice AI Agent Journey with Murf Falcon"
slug: "building-samar-my-10-day-voice-ai-agent-journey-with-murf-falcon"
author: "RAGHUL P"
source: "devto_webdev"
published: "Sat, 15 Aug 2026 06:22:37 +0000"
description: "Building Samar: My 10-Day Voice AI Agent Journey with Murf Falcon Over the past 10 days, I built Samar , a multilingual AI voice agent for a Bharat Digital B..."
keywords: "voice, agent, samar, can, information, multilingual, banking, user"
generated: "2026-08-15T06:47:15.231874"
---

# Building Samar: My 10-Day Voice AI Agent Journey with Murf Falcon

## Overview

Building Samar: My 10-Day Voice AI Agent Journey with Murf Falcon Over the past 10 days, I built Samar , a multilingual AI voice agent for a Bharat Digital Bank use case as part of the 10 Days of Voice Agents – VoiceForBharat Edition challenge. The project started as a simple voice assistant and gradually evolved into a more complete Voice AI system capable of remembering users, using real-time tools, making outbound calls, escalating sensitive situations to humans, analyzing calls, and handing specialized conversations to another AI agent. 🎯 The Problem Banking can sometimes be difficult to navigate, especially when users need quick information or assistance without going through multiple screens and menus. I wanted to build a voice-first banking assistant that could provide natural conversations while also maintaining security and knowing when it should involve a human. That's where Samar comes in. 🤖 What is Samar? Samar is a multilingual banking voice agent designed to help users with general banking-related queries. It can: Answer general banking questions Provide financial information Remember returning users with consent Fetch real-time information using tools Find nearby branches Provide exchange-rate information Make outbound reminder calls Escalate sensitive issues to human support Track call analytics Hand specialized conversations to a specialist agent The voice experience is powered by Murf Falcon , the fastest TTS API used in this challenge. 🏗️ How the System Works At a high level, the voice interaction follows this flow: User Speech ↓ Speech-to-Text ↓ LLM / Agent Logic ↓ Memory or Tool Calling ↓ Text-to-Speech ↓ User hears the response The system uses real-time voice communication through LiveKit, an LLM for reasoning and conversation, speech recognition for understanding the user, and Murf Falcon for natural voice generation. 🚀 Important Features 1. Voice AI with Guardrails Samar has a clear banking role and follows safety rules. It does not ask users for sensitive information such as: PIN OTP CVV Passwords Full account credentials For sensitive requests, it knows its limits instead of pretending it can access protected information. 2. Multilingual Conversations Samar supports multilingual conversations and follows native-script requirements. For example: Hindi → Devanagari English → Latin script This helped improve the naturalness and correctness of multilingual responses. 3. Persistent Memory Samar can remember returning users after receiving explicit permission. The system stores useful profile information and retrieves it during future conversations. This allows the experience to become more personalized instead of starting from zero every time. 4. Real-Time Tools I added tools that allow Samar to access useful information instead of relying only on the LLM. For example: Exchange-rate lookup Nearby branch lookup Banking-related information The agent decides when a tool is needed and presents the result naturally to the user. 5. Outbound Calls Samar can initiate outbound calls instead of only waiting for users to contact the agent. One use case is a banking reminder where Samar proactively contacts the user with an important update. 6. Human Escalation A good AI agent should know when it cannot safely handle something. For example, if a user reports potential fraud, Samar can ask for permission to create a support request and escalate the issue to human assistance. 7. Call Analytics I built a Call Analytics Dashboard to understand how the voice agent is performing. The dashboard can provide insights such as: Total calls Completed calls Human escalations Average call duration Tool usage Call trends Language distribution Recent escalations This makes it easier to understand user interactions and improve the agent. 8. Specialist Agent Handoff Finally, Samar does not have to be an expert in everything. For specialized questions, the main agent can hand the conversation to a specialist agent. For example: User → Samar → Loan Specialist The specialist can then continue the conversation with more focused knowledge. 🧩 A Major Challenge I Faced One of the challenges I faced was multilingual voice handling. The agent could understand Hindi, but the generated voice could sound like an English-accented response when the language configuration was not handled correctly. I addressed this by configuring multilingual speech recognition and dynamic voice/locale handling, while also enforcing the correct native script for each language. This taught me that multilingual Voice AI is not just about understanding different languages. Speech recognition, language detection, script generation, and voice synthesis all need to work together. 🛠️ How to Run the Project Clone the repository: bash git clone YOUR_GITHUB_REPOSITORY_URL Backend cd backend uv sync uv run python src/agent.py dev Frontend Open another terminal: cd frontend pnpm install pnpm dev Then open: http://localhost:3000 Connect to Samar and start a conversation. 🔐 Environment Variables Never publish API keys directly in your source code or GitHub repository. Store credentials in environment variables such as: MURF_API_KEY=your_key DEEPGRAM_API_KEY=your_key GOOGLE_API_KEY=your_key LIVEKIT_API_KEY=your_key LIVEKIT_API_SECRET=your_secret LIVEKIT_URL=your_url

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/raghul_p23itr122_8708ad5/building-samar-my-10-day-voice-ai-agent-journey-with-murf-falcon-41no

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
