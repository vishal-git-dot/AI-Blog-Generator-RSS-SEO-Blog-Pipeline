---
title: "Building phi-guard-mcp: Catching PHI Leaks in AI-Generated Code"
slug: "building-phi-guard-mcp-catching-phi-leaks-in-ai-generated-code"
author: "Abidit Shrestha"
source: "devto_ai"
published: "Sun, 30 Aug 2026 16:15:28 +0000"
description: "The Problem Nobody's Watching Your AI coding agent just shipped a patient's diagnosis to OpenAI. The code worked. The tests passed. The PR got approved. Nobo..."
keywords: "phi, mcp, guard, code, patient, mrn, your, not"
generated: "2026-08-30T16:26:18.041784"
---

# Building phi-guard-mcp: Catching PHI Leaks in AI-Generated Code

## Overview

The Problem Nobody's Watching Your AI coding agent just shipped a patient's diagnosis to OpenAI. The code worked. The tests passed. The PR got approved. Nobody noticed — because nothing was watching for it. This is a new class of mistake. Infrastructure scanners like Prowler check S3 bucket encryption, not whether your code interpolates patient.name into a prompt. The FHIR MCPs help agents read clinical data — they don't check whether other code is leaking PHI into logs or analytics. The code is doing exactly what it was written to do. That's the problem. What PHI Guard MCP Does phi-guard-mcp is a local-first MCP server that catches PHI (protected health information) before it hits LLM calls, logs, or analytics events. It runs entirely on your machine over stdio. No network calls. No telemetry. No data ever leaves your environment. Two tools: scan_code — Walks your repo and flags lines where a sensitive identifier (patient, diagnosis, mrn, ssn, dob) appears on the same line as a risky sink (openai, anthropic, console.log, logger, .track()) redact_suggest — Takes any raw text and returns a redacted version with PHI replaced by placeholders Example: { "text" : "Patient John Doe (MRN-12345), DOB: 01/01/1980" } { "redacted" : "Patient [NAME] ([MRN]), [DOB]" , "detected" : [ { "type" : "mrn" , "value" : "MRN-12345" , "confidence" : 0.9 }, { "type" : "dob" , "value" : "01/01/1980" , "confidence" : 0.85 }, { "type" : "name" , "value" : "John Doe" , "confidence" : 0.8 } ] } What It Catches PHI Type Confidence Example Matches SSN 0.95 123-45-6789 MRN 0.90 MRN-12345, MRN: 12345 DOB 0.85 01/01/1980, born 3/14/75 Name 0.80 Patient John Doe Phone 0.75 555-867-5309 Email 0.70 jane.roe@example.com The patterns are deliberately narrow. A false positive that trains someone to ignore the tool is worse than a missed match. Tested Against Real Leak Patterns 6/6 planted leaks detected across 5 different sinks (OpenAI, Anthropic, Sentry, Winston, PostHog/analytics) 0 false positives across 5 clean-code fixtures Scans .ts, .js, .tsx, .jsx, .py, .go Skips node_modules, dist, build, .next, .turbo, and dotfiles What This Is Not Not a HIPAA certification or legal compliance guarantee — it's a linter-grade signal, not an audit Not a competitor to Prowler or AWS Config — those scan infrastructure, this reads source code Not a hosted service — it runs entirely on your machine, no BAA required How to Use It Installation: npm install -g phi-guard-mcp With Claude Code: Add .mcp.json to your project root: { "mcpServers" : { "phi-guard" : { "command" : "node" , "args" : [ "/absolute/path/to/phi-guard-mcp/dist/index.js" ] } } } Command Line: phi-guard-mcp Then ask your AI agent: "Scan this repo for PHI leaks in prompts and logs" or "Redact this text: 'Patient John Doe (MRN-12345) was admitted on 1980-01-01'" Why I Built This This came from watching AI agents write code that ships patient data into prompts, logs, and analytics — with total confidence, because nothing was watching for it. The gap I saw was real: no existing tool catches this. The code works. Tests pass. PRs get approved. But patient.diagnosis just went to OpenAI. So I built the thing I wished existed. Links GitHub: github.com/Abidit/phi-guard-mcp npm: npmjs.com/package/phi-guard-mcp MCP Registry: mcpservers.org/servers/abidit/phi-guard-mcp MIT licensed. Open source. Free to use, forever. Feedback welcome, especially if you're building in healthtech or working on AI safety.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/abidit_shrestha_fefae4cee/building-phi-guard-mcp-catching-phi-leaks-in-ai-generated-code-17m8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
