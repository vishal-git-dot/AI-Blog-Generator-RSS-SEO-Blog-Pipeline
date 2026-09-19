---
title: "How I Built an AI Agent That Controls Browsers, Terminals, and Desktop Apps"
slug: "how-i-built-an-ai-agent-that-controls-browsers-terminals-and-desktop-apps"
author: "Safiyev Marat"
source: "devto_ai"
published: "Sat, 19 Sep 2026 10:23:23 +0000"
description: "How I Built an AI Agent That Controls Browsers, Terminals, and Desktop Apps An LLM can tell you what to do. But what happens when you ask it to actually do s..."
keywords: "execution, heyagent, agent, computer, model, can, architecture, verification"
generated: "2026-09-19T10:39:10.077972"
---

# How I Built an AI Agent That Controls Browsers, Terminals, and Desktop Apps

## Overview

How I Built an AI Agent That Controls Browsers, Terminals, and Desktop Apps An LLM can tell you what to do. But what happens when you ask it to actually do something on your computer? Open a browser. Create a document. Execute a terminal command. Manage files. Verify the result. A language model alone cannot reliably handle all of this. That's why I built HeyAgent , an open-source AI agent designed to interact with real desktop environments. Here's how its architecture works. 1. The Core Architecture HeyAgent isn't just an LLM connected to a few tools. It uses a structured execution pipeline: User Request | v Context & Memory | v Router | v Planner | v Mission Queue | v Execution Engine | v Tools | v Verification | +---- Success ---> Response | +---- Retryable Failure ---> Execution Engine Each component has a specific responsibility. The model helps decide what needs to happen. The execution system handles how it happens. 2. Planning Before Execution Imagine giving HeyAgent this request: Open the browser, research a topic, and save the results to a file. This isn't a single action. It requires several steps: Understand the request. Determine which tools are needed. Organize the actions. Execute the workflow. Verify the result. HeyAgent uses routing and planning to prepare tasks before execution. A mission queue coordinates the work, while the execution engine runs the required actions. Depending on the task, execution can use a deterministic harness or an LLM-driven tool loop. 3. Connecting the LLM to a Real Computer The execution engine connects the model to tools that interact with the operating system. HeyAgent supports: Browser: Navigate websites and interact with pages. Desktop: Control the mouse, keyboard, windows, and applications. Terminal: Execute shell commands. Files: Read, create, and manage local files. Integrations: Work with connected services, including Google Workspace. This allows a single workflow to move between different environments. For example, an agent can collect information through a browser, process it using a terminal command, and save the output to a local file. These operations are coordinated through the agent runtime rather than being completely independent scripts. 4. Execution Isn't Completion One important part of the architecture is verification. A successful tool call doesn't necessarily mean the user's task is complete. A browser action might succeed while the website returns an error. A command might execute without producing the expected output. HeyAgent includes a separate verification stage that evaluates execution evidence before the workflow reports completion. If verification detects a retryable failure, execution can continue. Execute | v Verify | +-- Evidence passes --> Complete | +-- Retryable failure --> Continue execution This doesn't guarantee that every task will succeed. It creates an explicit distinction between performing an action and achieving the requested result. I explored this problem in more detail in my previous article about false task completion. 5. Computer Control Needs Permissions Giving an AI agent access to a real computer introduces obvious risks. A tool capable of managing files or running commands can also perform destructive actions. HeyAgent includes a permission system with configurable policies, including approval requirements and capability allowlists. Sensitive operations can require explicit user confirmation before execution. The goal is to make computer automation useful without treating every model-generated action as automatically authorized. 6. No Dependency on a Single LLM Another design decision was to keep the architecture model-agnostic. HeyAgent supports different model providers, including cloud services and local models through Ollama. The system also includes model failover capabilities. The reasoning model can change without requiring an entirely different computer-control architecture. This separation makes it easier to experiment with different models while keeping the surrounding execution system consistent. The Bigger Picture Building an autonomous AI agent isn't just about writing better prompts. It's about connecting several systems: Planning, execution, computer control, permissions, state management, and verification. HeyAgent brings these components together in a local-first architecture accessible through a CLI, desktop application, and Telegram bot. It's still an evolving open-source project, and there's plenty of work ahead. If you're interested in computer-use agents, automation, or agent architecture, feel free to explore the code and contribute. GitHub: https://github.com/SAFIYEV/HeyAgent ⭐ If you find the project interesting, consider giving it a star. I'd also love to hear how you're approaching execution and verification in your own AI agents.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/safiyevmarat/how-i-built-an-ai-agent-that-controls-browsers-terminals-and-desktop-apps-143k

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
