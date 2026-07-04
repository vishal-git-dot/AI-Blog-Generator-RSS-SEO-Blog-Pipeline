---
title: "Practical Applications of LLMs in Supply Chain Management"
slug: "practical-applications-of-llms-in-supply-chain-management"
author: "shashank ms"
source: "devto_ai"
published: "Sat, 04 Jul 2026 13:34:03 +0000"
description: "We are going to build a supply chain risk analyzer that ingests inventory levels, supplier lead times, and daily demand, then flags potential stockouts and s..."
keywords: "oxlo, sku, supply, risk, supplier, openai, chain, inventory"
generated: "2026-07-04T13:45:59.773170"
---

# Practical Applications of LLMs in Supply Chain Management

## Overview

We are going to build a supply chain risk analyzer that ingests inventory levels, supplier lead times, and daily demand, then flags potential stockouts and suggests reorders. This kind of agent helps operations teams move from spreadsheet firefighting to automated early warnings. We will run the whole thing on Oxlo.ai using its OpenAI-compatible API so you can plug it into existing pipelines without vendor lock-in. What you'll need Python 3.10 or newer The OpenAI SDK: pip install openai An Oxlo.ai API key from https://portal.oxlo.ai Step 1: Set up the Oxlo.ai client Create a new file called supply_agent.py and initialize the client. Oxlo.ai exposes a fully OpenAI-compatible endpoint, so the only difference is the base URL and your Oxlo.ai API key. from openai import OpenAI import json import os client = OpenAI( base_url="https://api.oxlo.ai/v1", api_key=os.environ.get("OXLO_API_KEY", "YOUR_OXLO_API_KEY") ) Step 2: Define the inventory schema Before we call the model, we need clean data. I represent each SKU as a dictionary with fields that map to real ERP exports: current stock, reorder point, average daily demand, and supplier lead time. inventory = [ { "sku": "ELEC-8821", "description": "22uF Ceramic Capacitor", "current_stock": 900, "reorder_point": 500, "daily_demand": 30, "supplier_lead_time_days": 14, "supplier": "Shenzhen Components Ltd" }, { "sku": "MECH-3304", "description": "Aluminum Bracket 40mm", "current_stock": 450, "reorder_point": 200, "daily_demand": 30, "supplier_lead_time_days": 7, "supplier": "Midwest Metals Inc" }, { "sku": "PCB-9912", "description": "Main Control Board Rev 4", "current_stock": 80, "reorder_point": 100, "daily_demand": 20, "supplier_lead_time_days": 30, "supplier": "Pacific PCBs" } ] Step 3: Write the system prompt The system prompt is the core logic of the agent. It tells the model how to evaluate risk and what format to return. I keep it strict and structured so the output is predictable. SYSTEM_PROMPT = """You are a supply chain risk analyst. Your job is to evaluate inventory data and return a JSON object with no markdown formatting. For each SKU, calculate: - days_of_supply: current_stock / daily_demand - stockout_date: today's date + days_of_supply - risk_level: "low" if days_of_supply > lead_time + 7, "medium" if days_of_supply > lead_time, else "high" - recommended_action: either "no_action", "reorder_now", or "expedite_order" Return a JSON object with this exact structure: { "analyses": [ { "sku": "string", "days_of_supply": number, "stockout_date": "YYYY-MM-DD", "risk_level": "low|medium|high", "recommended_action": "no_action|reorder_now|expedite_order", "reasoning": "string" } ] } Be concise. Use ISO dates. Do not include markdown code fences in your response.""" Step 4: Build the analysis function Now we wire the prompt and the data together. This function takes a single SKU record, formats it as a user message, and sends it to Oxlo.ai. I use llama-3.3-70b because it handles structured JSON reliably and is cost-effective on Oxlo.ai's flat per-request pricing, which means long supplier descriptions do not inflate the cost. from datetime import datetime def analyze_sku(sku_data: dict) -> dict: user_message = f"""Analyze this SKU as of {datetime.now().strftime('%Y-%m-%d')}: {json.dumps(sku_data, indent=2)}""" response = client.chat.completions.create( model="llama-3.3-70b", messages=[ {"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": user_message}, ], response_format={"type": "json_object"}, temperature=0.1, ) raw = response.choices[0].message.content return json.loads(raw) Step 5: Batch process the catalog A real warehouse has hundreds of SKUs. We loop over the inventory list, call the analyzer for each item, and collect the results. Oxlo.ai has no cold starts on popular models, so this loop runs without latency spikes. def run_inventory_audit(inventory_list: list) -> list: results = [] for item in inventory_list: try: analysis = analyze_sku(item) results.extend(analysis.get("analyses", [])) except Exception as e: results.append({ "sku": item.get("sku"), "error": str(e) }) return results Run it Here is the entry point. I run the audit on our sample data and print a summary table focused on high-risk items. if __name__ == "__main__": print("Running supply chain audit via Oxlo.ai...\n") all_results = run_inventory_audit(inventory) for r in all_results: if "error" in r: print(f"FAIL {r['sku']}: {r['error']}") continue flag = "🚨" if r["risk_level"] == "high" else "⚠️" if r["risk_level"] == "medium" else "✅" print(f"{flag} {r['sku']} | Risk: {r['risk_level'].upper()} | Action: {r['recommended_action']} | {r['reasoning']}") Example output: Running supply chain audit via Oxlo.ai... ✅ ELEC-8821 | Risk: LOW | Action: no_action | 30 days of supply exceeds lead time plus safety buffer. ⚠️ MECH-3304 | Risk: MEDIUM | Action: reorder_now | 15 days of supply covers lead time but leaves no safety margin. 🚨 PCB-9912 | Risk: HIGH | Action: expedite_order | Only 4 days of supply remaining against a 30-day lead time. Wrap-up That is a working supply chain risk agent. Two concrete directions to take it next: connect the recommended_action output to your procurement system's API to trigger purchase orders automatically, or switch to kimi-k2.6 on Oxlo.ai if you want to add multi-tier supplier reasoning and vision capabilities for analyzing scanned packing lists or shipment photos.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/shashank_ms_6a35baa4be138/practical-applications-of-llms-in-supply-chain-management-nh0

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
