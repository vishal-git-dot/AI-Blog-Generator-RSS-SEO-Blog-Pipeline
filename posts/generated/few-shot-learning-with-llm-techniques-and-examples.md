---
title: "Few-Shot Learning with LLM: Techniques and Examples"
slug: "few-shot-learning-with-llm-techniques-and-examples"
author: "shashank ms"
source: "devto_ai"
published: "Wed, 24 Jun 2026 19:35:12 +0000"
description: "We are going to build a support ticket triage classifier that uses few-shot prompting to label incoming tickets as Critical, High, or Low priority. By embedd..."
keywords: "ticket, oxlo, examples, tickets, api, priority, prompt, openai"
generated: "2026-06-24T19:54:11.168922"
---

# Few-Shot Learning with LLM: Techniques and Examples

## Overview

We are going to build a support ticket triage classifier that uses few-shot prompting to label incoming tickets as Critical, High, or Low priority. By embedding labeled examples directly into the prompt, we get reliable classification without fine-tuning or maintaining a vector database. This is ideal for small support teams that need to route tickets immediately and keep infrastructure minimal. You will need Python 3.10 or newer, the OpenAI SDK installed with pip install openai , and an API key from your Oxlo.ai dashboard at https://portal.oxlo.ai . Step 1: Configure the Oxlo.ai client. Start by importing the SDK and pointing it at Oxlo.ai. The client is a drop-in replacement for the standard OpenAI client, so the only change is the base URL and your Oxlo.ai API key. from openai import OpenAI client = OpenAI(base_url="https://api.oxlo.ai/v1", api_key="YOUR_OXLO_API_KEY") Step 2: Write the system prompt with few-shot examples. The system prompt carries the task description and the labeled examples. Because Oxlo.ai charges per request rather than per token, adding these few-shot examples does not inflate our cost. We can include enough context to make the model accurate without trimming examples to save on prompt length. SYSTEM_PROMPT = """You are a support ticket triage assistant. Read the ticket description and classify its priority as exactly one of: Critical, High, or Low. Respond with only the priority label and a one-sentence justification. Examples: Ticket: "Our production database is down and customers cannot check out." Priority: Critical Reason: Complete service outage affecting all users. Ticket: "Feature request: dark mode for the dashboard." Priority: Low Reason: Nice-to-have UI improvement with no functional impact. Ticket: "Intermittent 500 errors on the invoice export endpoint since the last deploy." Priority: High Reason: Degraded functionality for a core workflow impacting paid accounts. """ Step 3: Define the classification function. This helper formats the incoming ticket, sends the conversation to Oxlo.ai, and returns the text response. I am using Llama 3.3 70B here because it follows structured instructions reliably, though Qwen 3 32B or DeepSeek V3.2 would work just as well for this task. def classify_ticket(ticket_body: str) -> str: user_message = f'Ticket: "{ticket_body}"\nPriority:' response = client.chat.completions.create( model="llama-3.3-70b", messages=[ {"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": user_message}, ], temperature=0.2, max_tokens=100, ) return response.choices[0].message.content.strip() Step 4: Run a batch of tickets. To see the few-shot pattern generalize, we will process a list of new tickets and print the results. This is the same loop I run in staging before wiring the classifier into our CRM webhook. tickets = [ "The entire API returns 503 errors. This started 10 minutes ago.", "Can we get a CSV download option for the analytics page?", "Some users report missing 2FA codes after the iOS app update.", ] for t in tickets: result = classify_ticket(t) print(f"Ticket: {t}\nResult: {result}\n") Run it. Save the full script as triage.py , set your API key, and run it. The model should generalize from the three examples to label the new tickets correctly. $ export OXLO_API_KEY="sk-oxlo.ai-..." $ python triage.py Ticket: The entire API returns 503 errors. This started 10 minutes ago. Result: Critical Reason: Complete service outage affecting all API consumers. Ticket: Can we get a CSV download option for the analytics page? Result: Low Reason: Nice-to-have feature request with no immediate functional impact. Ticket: Some users report missing 2FA codes after the iOS app update. Result: High Reason: Security workflow degradation affecting a subset of users. This classifier is already useful, but two moves make it production-ready. First, add a confidence threshold by asking the model to output a score from 1 to 10 and escalate anything below 7 to a human reviewer. Second, because Oxlo.ai uses request-based pricing, you can expand the system prompt with ten or twenty more examples to cover edge cases without watching your bill grow with prompt length. If you need deeper reasoning for ambiguous tickets, swap the model to DeepSeek R1 671B or Kimi K2.6 and keep the same code.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/shashank_ms_6a35baa4be138/few-shot-learning-with-llm-techniques-and-examples-5c74

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
