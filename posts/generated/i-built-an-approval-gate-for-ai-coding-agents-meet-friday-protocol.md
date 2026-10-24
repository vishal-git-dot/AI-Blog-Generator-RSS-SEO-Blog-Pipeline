---
title: "I Built an Approval Gate for AI Coding Agents — Meet Friday Protocol"
slug: "i-built-an-approval-gate-for-ai-coding-agents-meet-friday-protocol"
author: "Lucky Hermawan Roza"
source: "devto_ai"
published: "Sat, 24 Oct 2026 20:28:34 +0000"
description: "AI coding agents can be incredibly productive. They can inspect a codebase, propose a solution, modify files, run tests, and keep going with very little supe..."
keywords: "workflow, agent, approval, friday, protocol, what, coding, not"
generated: "2026-10-24T20:31:17.911474"
---

# I Built an Approval Gate for AI Coding Agents — Meet Friday Protocol

## Overview

AI coding agents can be incredibly productive. They can inspect a codebase, propose a solution, modify files, run tests, and keep going with very little supervision. But I kept thinking about one question: What if the agent starts implementing the wrong plan before I have a chance to review it? The problem isn't necessarily that the AI cannot write code. Sometimes, the problem is that it can move from planning to execution too quickly. I wanted a workflow where an agent could still work autonomously, but not skip the moment when a human needs to make a decision. That idea led me to build Friday Protocol . What is Friday Protocol? Friday Protocol is an open-source skill designed to introduce an approval-first workflow for AI coding agents. The idea is straightforward: The agent investigates the task and prepares an implementation plan. The workflow pauses and asks for explicit human approval. The agent proceeds only after approval is given. The implementation goes through the required security checks and testing. The agent provides evidence of what was completed, including any remaining issues. In my workflow, OKE is the explicit approval signal. The goal is not to make an AI agent less capable. It is to make the transition from planning to execution more deliberate and reviewable. Why not just tell the AI to be careful? I could simply add a sentence to a prompt: "Ask me before making changes." But I wanted something more structured than relying on a general instruction. Friday Protocol is built around explicit workflow gates, rather than treating approval as a polite suggestion. The workflow is intended to prevent the agent from treating every request as permission to immediately execute its own interpretation of the task. It also emphasizes verification. An agent should not declare a task complete merely because it has finished editing files. If testing fails, the workflow should return to implementation and verification instead of pretending everything succeeded. Of course, the actual guarantees depend on the agent environment, how the skill is invoked, and how its instructions are followed. This is a workflow-level safeguard, not a claim that every possible unsafe action is technically impossible. What does the workflow look like? Here is the simplified lifecycle: Task Request | v Investigation & Planning | v Present Implementation Plan | v Wait for Explicit Approval | v Implementation | v Security Checks & Testing | v Did Verification Pass? | +---+---+ | | No Yes | | v v Fix and Report Results Retest with Evidence The important part is the approval gate before implementation and the verification loop before completion. What makes it different? Friday Protocol is designed as a reusable skill, rather than a standalone application that must replace an existing coding agent. It can be used as a workflow layer, with optional integration into my other project, MemoriaGraph, which explores contextual memory and decision support. I am also experimenting with these ideas in a broader security operations project. However, Friday Protocol itself focuses on the workflow and approval process, not on replacing a complete security operations platform. My aim is to make the approach reusable across supported AI coding environments. Compatibility and behavior still need to be evaluated for each environment. What I have learned while building it One thing I have learned is that adding more instructions is not automatically the same as creating a reliable workflow. A useful workflow needs observable checkpoints. For example: Did the agent actually stop after presenting its plan? Did it wait for approval before proceeding? What happened when a test failed? Did it retry verification after making a correction? Can the final report distinguish verified results from assumptions? These questions are more useful than simply asking whether an agent claims to follow the rules. I want to keep improving Friday Protocol through practical testing, feedback, and clearer evidence of its behavior. It is still an evolving open-source project, and I don't consider it a complete solution to AI agent safety. Try it and tell me what you think If you work with AI coding agents, I would genuinely appreciate your feedback. Repository: Friday Protocol on GitHub I'm particularly interested in hearing from developers who have experienced problems with agents moving too quickly, making changes before a plan is reviewed, or reporting completion without sufficient verification. A few questions I'd love to discuss: Would an explicit approval gate be useful in your workflow? Which parts of the development lifecycle should require human approval? How would you test whether an agent actually respects the gate? What would make a workflow like this easier to adopt across different coding agents? I'm building this from my own experience working with AI-assisted development, and I'd like to learn how other developers approach the same problem. Thanks for reading. Feedback, criticism, and contributions are welcome.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/lhermawan/i-built-an-approval-gate-for-ai-coding-agents-meet-friday-protocol-4646

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
