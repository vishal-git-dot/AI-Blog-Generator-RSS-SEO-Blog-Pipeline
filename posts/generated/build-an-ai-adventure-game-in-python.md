---
title: "Build an AI Adventure Game in Python"
slug: "build-an-ai-adventure-game-in-python"
author: "Sonam"
source: "devto_python"
published: "Wed, 22 Jul 2026 19:14:09 +0000"
description: "Most LLM demos are one prompt and one answer. This one is a little more fun: a text-based choose-your-own-adventure game. The player picks a genre, names a c..."
keywords: "game, telnyx, app, https, com, post, json, adventure"
generated: "2026-07-22T19:34:31.387150"
---

# Build an AI Adventure Game in Python

## Overview

Most LLM demos are one prompt and one answer. This one is a little more fun: a text-based choose-your-own-adventure game. The player picks a genre, names a character, reads a generated scene, and chooses option 1, 2, or 3. The app keeps track of game state while Telnyx AI Inference generates the next scene. Code: https://github.com/team-telnyx/telnyx-code-examples/tree/main/adventure-game-python What the app does The Flask API exposes: POST /game/start POST /game/<id>/choose GET /game/<id> GET /games GET /health Each game tracks: genre player name current scene available choices location health inventory turn count status Statuses can be: ongoing won lost escaped How it uses Telnyx AI Inference The app calls: POST /v2/ai/chat/completions Default model: AI_MODEL=moonshotai/Kimi-K2.6 The system prompt asks the model to act as a game master and return JSON only: { "scene" : "the scene description" , "choices" : [ "choice 1" , "choice 2" , "choice 3" ], "state" : { "location" : "..." , "health" : 100 , "inventory" : [], "turn" : 1 }, "status" : "ongoing" } That structure is what makes the example useful. The model writes the scene, but the app can still parse the result, store state, validate choices, and decide whether the game continues. Run it Clone the repo: git clone https://github.com/team-telnyx/telnyx-code-examples.git cd telnyx-code-examples/adventure-game-python Create your .env : cp .env.example .env Add your Telnyx API key: TELNYX_API_KEY=your_telnyx_api_key AI_MODEL=moonshotai/Kimi-K2.6 HOST=127.0.0.1 PORT=5000 Install and start: pip install -r requirements.txt python app.py Check health: curl http://localhost:5000/health Start a fantasy adventure: curl -X POST http://localhost:5000/game/start \ -H "Content-Type: application/json" \ -d '{ "genre": "fantasy", "player_name": "Aria" }' | python3 -m json.tool Choose your next move: curl -X POST http://localhost:5000/game/game-< id > /choose \ -H "Content-Type: application/json" \ -d '{"choice":1}' | python3 -m json.tool Try other genres: curl -X POST http://localhost:5000/game/start \ -H "Content-Type: application/json" \ -d '{"genre":"cyberpunk","player_name":"Void"}' Valid genres: fantasy sci-fi mystery horror cyberpunk post-apocalyptic Why this is a useful pattern The game is playful, but the app pattern is practical. It shows how to: keep state in your backend pass recent history back to the model ask for structured JSON validate user choices continue or end a session based on model output That same pattern can power training simulations, support flows, onboarding tutorials, guided troubleshooting, or interactive learning tools. The model handles the creative generation. Your app owns the rules. Resources Code: https://github.com/team-telnyx/telnyx-code-examples/tree/main/adventure-game-python Telnyx AI skills and toolkits: https://github.com/team-telnyx/ai Telnyx AI Inference docs: https://developers.telnyx.com/docs/inference Chat Completions API: https://developers.telnyx.com/api/inference/chat-completions Telnyx Portal: https://portal.telnyx.com/

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sonam_50a41a4ced7e6b4f3fa/build-an-ai-adventure-game-in-python-7b6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
