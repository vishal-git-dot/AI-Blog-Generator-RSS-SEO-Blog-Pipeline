---
title: "🚂 MINDTRACE AI: Echoes of the Last Train 🔎"
slug: "mindtrace-ai-echoes-of-the-last-train"
author: "Shantanu Shete"
source: "devto_webdev"
published: "Sat, 24 Oct 2026 19:55:48 +0000"
description: "This is a submission for the Hacktoberfest Open-Source AI Challenge Week 3: Slow and Steady 🚂 MINDTRACE AI: Echoes of the Last Train 🔎 Every lie leaves a tra..."
keywords: "mindtrace, game, dialogue, open, model, can, mystery, evidence"
generated: "2026-10-24T20:31:17.911088"
---

# 🚂 MINDTRACE AI: Echoes of the Last Train 🔎

## Overview

This is a submission for the Hacktoberfest Open-Source AI Challenge Week 3: Slow and Steady 🚂 MINDTRACE AI: Echoes of the Last Train 🔎 Every lie leaves a trace. Every choice changes the truth. What if you could solve a murder mystery by questioning suspects, connecting evidence, and catching contradictions—with the help of a locally running AI model? That's the idea behind MINDTRACE AI , an AI-powered detective mystery game I built for Hacktoberfest Week 3. What I Built MINDTRACE AI is a browser-based detective game where players investigate a mysterious incident aboard a train. Instead of simply reading a fixed story, players explore different train locations, discover clues, interview suspects, and use evidence to uncover inconsistencies before making their final accusation. ✨ Key Features 🔎 Interactive Investigation: Explore five train locations and discover clues. 🕵️ Suspect Interrogations: Interview three suspects with different secrets and motives. 🤖 AI-Powered Dialogue: Use Gemma 4 through Ollama to generate suspect responses. 🧩 Truth Tracker: Identify contradictions and verify them with supporting evidence. 📌 Evidence Board: Connect clues and evaluate possible explanations. 🏆 Multiple Endings: Your final accusation determines the outcome. 🔄 Fallback Dialogue: Continue playing with scripted responses if the local AI is unavailable. The goal was to combine detective gameplay with AI-generated conversations while keeping the mystery's actual solution consistent. Demo 🎬 Watch the gameplay demonstration: https://youtu.be/V_P0PZ-KfWg The video demonstrates my MINDTRACE AI project. Code 💻 GitHub Repository: https://github.com/Shantanuu1/MINDTRACE-AI The repository contains the project's source code and instructions for running it locally. Feel free to explore the implementation and contribute ideas for improving the game! How I Built It I built MINDTRACE AI using Python, Flask, HTML, CSS, and JavaScript. For the AI component, I used Gemma 4 ( gemma4:e2b ) through Ollama , allowing the model to run locally rather than relying entirely on a hosted AI API. Technology Stack Python: Backend logic and game mechanics. Flask: Web application and server-side routes. HTML, CSS, and JavaScript: User interface and interactive gameplay. Gemma 4 + Ollama: AI-generated suspect dialogue. SQLite or JSON: Game data storage, depending on the implemented storage layer. Pytest: Automated testing. One important design decision was to separate AI-generated dialogue from the core game logic. The model generates suspect responses, but the canonical culprit, timeline, evidence, and final accusation logic remain controlled by the game itself. This helps prevent unexpected AI responses from changing the mystery's underlying solution. I also included scripted fallback dialogue so players can continue investigating if the local model is unavailable. Why Does Open Innovation Matter? Open innovation makes it possible for developers to experiment, build, and share technology without depending entirely on closed platforms. For MINDTRACE AI, using an open-weight model locally through Ollama gave me the opportunity to experiment with AI-generated dialogue and integrate it directly into a game running on my own computer. This approach offers several benefits: More control: Developers can choose and configure the model they run. Local inference: The game can generate dialogue locally when the model is installed and running. Reduced API dependency: The project doesn't need a paid hosted AI API for its core dialogue generation. Learning by building: Developers can explore the practical challenges of integrating language models with real application logic. Open innovation isn't just about making technology available. It's about giving more people the ability to experiment, learn, and create something of their own. My Agent Session I used an AI-assisted coding workflow to help develop the project. The workflow helped me organize the application, implement the frontend and backend, and prepare tests. I haven't included a DevRelay session link because I don't currently have a shareable session to provide. The Lazy Payoff The idea behind MINDTRACE AI is to make solving a mystery feel interactive without requiring players to read a long, predetermined story. Players can investigate at their own pace, ask questions, gather evidence, and decide when they have enough information to make an accusation. For developers, running the AI locally also provides a way to experiment with conversational gameplay without building the project around a paid hosted AI API. Prize Categories I am submitting MINDTRACE AI to the Hacktoberfest Open-Source AI Challenge Week 3: Slow and Steady. Primary focus: Open-weight AI and local inference using Gemma 4 and Ollama. Building MINDTRACE AI helped me explore how local AI can be combined with web development, interactive storytelling, and deterministic game mechanics. The mystery isn't solved by AI alone. The player has to investigate, question, connect the clues, and decide what the truth really is. Every lie leaves a trace. Can you find it? 🔎 devchallenge #hf26challenge

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/shantanu_shete_1e614e6e52/mindtrace-ai-echoes-of-the-last-train-3fkp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
