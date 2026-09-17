---
title: "Clean JSON Extraction with Ollama and Python"
slug: "clean-json-extraction-with-ollama-and-python"
author: "flow nears"
source: "devto_python"
published: "Thu, 17 Sep 2026 15:55:56 +0000"
description: "When building autonomous agents or production workflows with local LLMs via Ollama , one of the most persistent engineering challenges is output parsing. Eve..."
keywords: "json, ollama, python, content, text, import, tags, output"
generated: "2026-09-17T16:39:14.788942"
---

# Clean JSON Extraction with Ollama and Python

## Overview

When building autonomous agents or production workflows with local LLMs via Ollama , one of the most persistent engineering challenges is output parsing. Even when instructed to produce pure JSON, smaller models like llama3:8b , mistral:7b , or phi3 often output markdown code fences ( json ... ), conversational text preambles, or incomplete payloads. In this article, we will explore a robust, zero-dependency Python pattern using Anchor Tag Framing and dynamic boundary isolation to extract 100% valid JSON from Ollama text streams. The Problem: Fine-Tuning Artifacts in Small LLMs Open-source LLMs are heavily fine-tuned on chat datasets and markdown documentation. When you prompt a model to return JSON: import ollama response = ollama . chat ( model = " llama3 " , messages = [ { " role " : " user " , " content " : " Extract user info from text: ' John Doe, 29, Software Engineer ' . Return JSON. " , } ], ) print ( response [ " message " ][ " content " ]) You frequently receive output like this: Here is the extracted information in JSON format: json { "name": "John Doe", "age": 29, "occupation": "Software Engineer" } Hope this helps! python If you feed response['message']['content'] directly into json.loads() , your application raises a json.decoder.JSONDecodeError . Relying on regex fallbacks or generic string replaces ( replace(" ` json", "") ) is fragile—especially when model responses contain nested code blocks or escaped quotes. The Solution: Anchor Tag Framing Instead of negative constraints (" Do not include markdown "), we use Anchor Tag Framing . By instructing the model to place its JSON payload strictly inside unique, non-colliding XML-style execution tags, we establish a deterministic structural boundary. 1. The Prompt Template Define a clear system contract containing explicit <payload> boundary tags: ` python SYSTEM_PROMPT = """ You are a specialized data extraction API that ONLY outputs valid JSON. STRICT EXECUTION RULES: Do not include any introductory text, preambles, explanations, or postscript text. Do not use markdown code fences (e.g., json or ). Output the raw JSON payload exclusively within the execution boundary and . Example format: { "key": "value" } """ ` 2. Robust Python Extractor Function Next, build a lightweight parser in Python that extracts content strictly within the target tags, falling back gracefully if needed: ` python import json import re from typing import Any, Dict import ollama def extract_json_payload(raw_text: str) -> Dict[str, Any]: """Extracts and parses JSON located inside tags. Falls back to regex searching for raw JSON objects if tags are missing. """ # 1. Primary Extraction: Boundary Tags tag_pattern = r"<payload>\s*(\{.*\}|\[.*\])\s*</payload>" match = re.search(tag_pattern, raw_text, re.DOTALL) if match: json_str = match.group(1) else: # 2. Fallback: Search for first opening brace/bracket to last closing brace/bracket fallback_pattern = r"(\{.*\}|\[.*\])" fallback_match = re.search(fallback_pattern, raw_text, re.DOTALL) if fallback_match: json_str = fallback_match.group(1) else: raise ValueError("No JSON payload detected in response.") # 3. Parse JSON return json.loads(json_str.strip()) ` End-to-End Implementation Example Here is a complete, runnable script demonstrating the extraction pipeline: ` python import json import re import ollama def query_ollama_json(user_text: str) -> dict: system_instruction = """ You are a structural parser API. Transform input text into structured JSON. Output ONLY within the and tags. """ user_prompt = f""" Extract key attributes from the following text into JSON format (keys: 'name', 'role', 'skills'): "{user_text}" """ response = ollama.chat( model="llama3", messages=[ {"role": "system", "content": system_instruction}, {"role": "user", "content": user_prompt}, ], ) content = response["message"]["content"] return extract_json_payload(content) --- Execution --- if name == " main ": raw_input = "Alice Smith is a Senior DevOps Engineer skilled in Docker, Kubernetes, and Python." try: structured_data = query_ollama_json(raw_input) print("Successfully extracted JSON:") print(json.dumps(structured_data, indent=2)) except Exception as e: print(f"Extraction failed: {e}") ` Why This Technique Works Under the Hood Attention Focusing: Small LLMs pay higher attention to token sequences with distinct boundary delimiters ( <tag> vs </tag> ). Deterministic Context Window: By shifting the target output pattern to standard tag structures, you minimize the activation of conversational completion tokens learned during post-training fine-tuning. Regex Isolation: Extracting via fixed string boundaries eliminates false positives from nested quotes or markdown formatting in text fields. References & Further Reading Ollama Official Documentation EdgeJSON Prompt & Modelfile Pack — A collection of 40+ production-ready prompts, Ollama Modelfiles, and validation schemas for deterministic JSON generation.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nearshi/-clean-json-extraction-with-ollama-and-python-21f3

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
