---
title: "Build a Natural Language IVR with Telnyx Call Control and AI Inference"
slug: "build-a-natural-language-ivr-with-telnyx-call-control-and-ai-inference"
author: "Sonam"
source: "devto_python"
published: "Fri, 28 Aug 2026 21:12:30 +0000"
description: "Nobody likes phone trees. "Press 1 for billing, press 2 for support." Miss an option? Start over. It is friction at its worst. The voice-ivr-with-agent-backe..."
keywords: "telnyx, call, llm, https, config, ivr, voice, app"
generated: "2026-08-28T22:02:34.845955"
---

# Build a Natural Language IVR with Telnyx Call Control and AI Inference

## Overview

Nobody likes phone trees. "Press 1 for billing, press 2 for support." Miss an option? Start over. It is friction at its worst. The voice-ivr-with-agent-backend example replaces that with a natural language conversation. Callers just say what they need, and the app routes them to the right department. Code: https://github.com/team-telnyx/telnyx-code-examples/tree/main/voice-ivr-with-agent-backend What it builds A Python/Flask app that handles inbound calls with a conversational IVR: Inbound Call -> answer with Call Control -> look up menu config from KV -> LLM generates a dynamic greeting -> gather(speech) — caller says what they need -> LLM routes intent to a department -> transfer call The core primitives The app combines four Telnyx primitives: Call Control : answer() , speak() , gather_using_speech() , transfer() AI Inference : telnyx.ai.openai.chat.completions.create() for greetings and intent routing KV store : menu config per phone number (business name, departments, transfer numbers, keywords) Agent state machine : an IVRAgent class that tracks call state, turn count, and retry logic Dynamic greeting via LLM Instead of a hardcoded "Press 1 for billing," the app generates a conversational greeting from the KV config: def generate_dynamic_menu_prompt ( menu_config : dict ) -> str : departments = menu_config . get ( " departments " , []) dept_list = " \n " . join ( f " - { d [ ' name ' ] } : { d [ ' description ' ] } " for d in departments ) return ( f " You are an IVR assistant for { menu_config [ ' business_name ' ] } . " f " Available departments: \n { dept_list } \n\n " f " Greet the caller briefly and ask how you can help. " f " Keep it conversational and under 2 sentences. " ) The LLM generates the greeting through the OpenAI-compatible Telnyx Inference binding. If it fails, the app falls back to a static greeting from the KV config. Intent routing via LLM When the caller speaks, the transcription is passed to route_intent_with_llm . The LLM is instructed to respond with only the department name for reliable parsing: completion = telnyx . ai . openai . chat . completions . create ( model = " telnyx-llm " , messages = [ { " role " : " system " , " content " : system_prompt }, { " role " : " user " , " content " : user_input }, ], max_tokens = 20 , temperature = 0.1 , ) intent = completion . choices [ 0 ]. message . content . strip (). lower () If the LLM fails or returns "unknown," the app falls back to keyword matching. After max_turns (3 by default), the call transfers to a default operator. Speech gather with Call Control The gather_using_speech primitive plays a prompt and captures the caller's speech in one call: telnyx . Call . gather_using_speech ( call_control_id , payload = prompt , voice = " female-en-US " , language = " en-US " , max_duration = 15 , ) Webhook verification Every webhook request is verified with Ed25519 signature verification: telnyx . Webhook . construct_event ( payload , signature , timestamp , TELNYX_PUBLIC_KEY ) This prevents spoofed requests from triggering call actions. The agent state machine The IVRAgent class manages each call: on_connect() : fetch menu config, generate LLM greeting, speak, gather on_gather_ended(speech) : route intent via LLM, transfer or retry Tracks turn_count and max_turns before falling back to a default transfer Management API PUT /api/menu-config/<phone_number> : update KV menu config dynamically GET /api/menu-config/<phone_number> : retrieve current config GET /api/agents : list active IVR agents (debugging) GET /health : health check Try it git clone https://github.com/team-telnyx/telnyx-code-examples.git cd telnyx-code-examples/voice-ivr-with-agent-backend python3 -m venv venv source venv/bin/activate pip install -r requirements.txt cp .env.example .env Fill in your Telnyx API Key, Public Key, Connection ID, and default transfer number. Then: python app.py ngrok http 5000 Point your Call Control Application webhook to https://<your-ngrok-url>.ngrok-free.app/webhooks/voice . Production notes Before using with real callers, add: persistent KV store (Redis or database instead of in-memory dict) caller ID personalization for greetings call queues for hold instead of blind transfer auth on management endpoints monitoring for LLM latency and fallback rates Resources: Code: https://github.com/team-telnyx/telnyx-code-examples/tree/main/voice-ivr-with-agent-backend Call Control docs: https://developers.telnyx.com/docs/voice/programmable-voice/call-control-overview AI Inference docs: https://developers.telnyx.com/docs/ai/ai-overview Webhooks docs: https://developers.telnyx.com/docs/develop/webhooks Telnyx Python SDK: https://github.com/team-telnyx/telnyx-python Telnyx AI on GitHub: https://github.com/team-telnyx/ai

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sonam_50a41a4ced7e6b4f3fa/build-a-natural-language-ivr-with-telnyx-call-control-and-ai-inference-24l5

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
