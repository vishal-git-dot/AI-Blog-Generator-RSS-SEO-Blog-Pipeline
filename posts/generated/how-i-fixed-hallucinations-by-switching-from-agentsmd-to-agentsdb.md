---
title: "How I Fixed Hallucinations by Switching from AGENTS.md to AGENTS.db"
slug: "how-i-fixed-hallucinations-by-switching-from-agentsmd-to-agentsdb"
author: "Mohammed Ibrahim Khan"
source: "devto_ai"
published: "Tue, 21 Jul 2026 14:01:18 +0000"
description: "Before I dive in, a bit of background on how our agentic workflow at Exam Intelligence for deep analysis and notes generation works... Initially, I tried to ..."
keywords: "agent, not, null, text, step, instructions, what, memories"
generated: "2026-07-21T14:05:44.045419"
---

# How I Fixed Hallucinations by Switching from AGENTS.md to AGENTS.db

## Overview

Before I dive in, a bit of background on how our agentic workflow at Exam Intelligence for deep analysis and notes generation works... Initially, I tried to create a complete end-to-end LangGraph workflow. Except, things always ran into unexpected bugs caused by external factors like missing PDFs, being unable to find papers, failing to parse them, or agents returning 503 errors or broken JSONs. At that point, it looked like I needed to build an entire coding agent just to handle the edge cases. The Fix Instead of a master workflow, I switched to creating CLI tools that a coding agent can use. The Setup: Running qwen3.6:35b over Ollama, inside the PI coding agents harness running in a Docker sandbox. The Flow: Basically, each file is a node (a step or an entire workflow to achieve a particular outcome) and the agent executes them one by one. If anything breaks, I decided on 3 levels of fixes: Level 1 (Auto): The agent manually does the job (like finding a missing URL). Level 2 (Auto): The agent identifies a short-term recurring pattern and writes a script for it. Level 3 (Human-in-the-loop): If the agent identifies a bug in my CLI tools, it flags it, suggests a fix, and stops to keep my codebase clean—waiting for my approval before editing the code. The Memory Architecture Unaware of the standard AGENTS.md naming conventions, I initially chose this setup: instructions.md : Informed the agent about the entire workflow, architecture, and how it should execute it. memory.md : A persistent cross-session memory for the agent, mainly storing what bugs/problems it faced and how it fixed them. workflow_checkpoints.db : A SQLite3 database used as temporary storage for the workflow, which is later pushed to PostgreSQL (used by our Django app) after quality checks to ensure production isolation. The Problem The agent started right, but when the time came to migrate the notes data and stuff to the Django database, it completely broke. My workflow had a migrate.py CLI tool which it could call to easily do the job (mentioned in instructions.md ), but it started using inline Python, always made syntax errors, migrated the data with broken formatting, and sometimes entirely skipped migrating certain tables. So after witnessing multiple failures, I made the following changes: Added a plan step . Switched the memory layer entirely to agents.db . Here is the schema layout: sqlite > . schema CREATE TABLE instructions ( id INTEGER PRIMARY KEY , step_order INTEGER NOT NULL , title TEXT NOT NULL , objective TEXT NOT NULL , actions TEXT NOT NULL , tools TEXT NOT NULL , success_criteria TEXT NOT NULL , created_at TEXT NOT NULL ); CREATE TABLE memories ( id INTEGER PRIMARY KEY , title TEXT NOT NULL , step TEXT NOT NULL , tldr TEXT NOT NULL , problem TEXT NOT NULL , fix TEXT NOT NULL , created_at TEXT NOT NULL ); The New Engine Setup The instructions table completely replaced instructions.md . It gave the agent isolated, step-by-step instructions focused on strict objectives, what specific actions it must take, what CLI tools it has access to, and a clearly defined definition of what success looks like. The memories table contained experiences from its past runs on what broke and how it fixed it. I pre-seeded the memories table with everything that went wrong in the previous runs and what the agent should have done in those instances using synthetic memories . The Execution Flow The agent was instructed to go step-by-step over the instructions table. For each step, it queries the memories table (just fetching the tldr ) as a brief on what needs to be done, how to do it, and what can possibly go wrong. If it encounters a new issue, it just adds that to memories. Those changes allowed me to audit what the agent intends to do (the plan) and insert fixes if any. It allowed for hierarchical querying of instructions and bugs, and completely fixed the previous issues. Additional Recommendations While I prompted the agent as a quick fix to just read the database (telling it when to do it), a more reliable way would be to just edit the harness to insert the right instructions and memories—saving more tokens on SQL queries per step. The Flexibility Tax Using the PI coding agents harness as the orchestrator adds flexibility, but it makes things way too unpredictable. Despite the flow being mostly hierarchical, I'm now stuck asking it to do a full run, catching hallucinations, and updating memories...

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/0x1brahim/how-i-fixed-hallucinations-by-switching-from-agentsmd-to-agentsdb-2ch1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
