---
title: "Using the Gemini API with Python (Free Tier)"
slug: "using-the-gemini-api-with-python-free-tier"
author: "Phil IPS"
source: "devto_python"
published: "Mon, 12 Oct 2026 05:17:46 +0000"
description: "Using the Gemini API with Python (Free Tier) Build AI-powered applications using Google's Gemini model via the free tier. Prerequisites Python 3.8+ OpenRoute..."
keywords: "free, response, gemini, api, print, prompt, str, content"
generated: "2026-10-12T05:22:20.390062"
---

# Using the Gemini API with Python (Free Tier)

## Overview

Using the Gemini API with Python (Free Tier) Build AI-powered applications using Google's Gemini model via the free tier. Prerequisites Python 3.8+ OpenRouter API key (free at https://openrouter.ai ) requests library: pip install requests Quick Start import requests import os # Configuration OPENROUTER_URL = " https://openrouter.ai/api/v1/chat/completions " MODEL = " google/gemini-2.0-flash-exp:free " # Free tier model def call_gemini ( prompt : str , api_key : str , max_tokens : int = 200 ) -> str : """ Call the free Gemini API via OpenRouter. """ headers = { " Authorization " : f " Bearer { api_key } " , " Content-Type " : " application/json " } data = { " model " : MODEL , " messages " : [{ " role " : " user " , " content " : prompt }], " temperature " : 0.7 , " max_tokens " : max_tokens } response = requests . post ( OPENROUTER_URL , headers = headers , json = data ) if response . status_code == 200 : return response . json ()[ " choices " ][ 0 ][ " message " ][ " content " ] else : raise Exception ( f " API Error: { response . status_code } - { response . text } " ) # Usage if __name__ == " __main__ " : api_key = os . getenv ( " OPENROUTER_API_KEY " ) if not api_key : print ( " Set OPENROUTER_API_KEY environment variable " ) exit ( 1 ) prompt = " Write a haiku about Python programming " try : result = call_gemini ( prompt , api_key ) print ( f " Prompt: { prompt } " ) print ( f " Response: { result } " ) except Exception as e : print ( f " Error: { e } " ) Advanced Example: Chat Loop import requests import os def chat_with_gemini ( api_key : str ): """ Interactive chat with Gemini. """ conversation = [] url = " https://openrouter.ai/api/v1/chat/completions " headers = { " Authorization " : f " Bearer { api_key } " , " Content-Type " : " application/json " } print ( " Gemini Chat (type ' quit ' to exit) " ) print ( " - " * 40 ) while True : user_input = input ( " You: " ) if user_input . lower () in ( ' quit ' , ' exit ' , ' q ' ): break conversation . append ({ " role " : " user " , " content " : user_input }) data = { " model " : " google/gemini-2.0-flash-exp:free " , " messages " : conversation , " temperature " : 0.7 , " max_tokens " : 300 } response = requests . post ( url , headers = headers , json = data ) if response . status_code == 200 : assistant_msg = response . json ()[ " choices " ][ 0 ][ " message " ][ " content " ] conversation . append ({ " role " : " assistant " , " content " : assistant_msg }) print ( f " Gemini: { assistant_msg } " ) else : print ( f " Error: { response . status_code } " ) print ( " - " * 40 ) if __name__ == " __main__ " : api_key = os . getenv ( " OPENROUTER_API_KEY " ) chat_with_gemini ( api_key ) Key Parameters Parameter Range Purpose temperature 0.0-1.0 Randomness (low=factual, high=creative) max_tokens 1-4096 Response length limit model various Choose free models with :free suffix Error Handling import time def robust_call ( prompt : str , api_key : str , retries : int = 3 ) -> str : """ Call API with exponential backoff retry. """ for attempt in range ( retries ): try : return call_gemini ( prompt , api_key ) except Exception as e : if " 429 " in str ( e ): # Rate limited wait = 2 ** attempt print ( f " Rate limited. Waiting { wait } s... " ) time . sleep ( wait ) else : raise raise Exception ( " Max retries exceeded " ) Best Practices Secure API keys - Use environment variables Handle rate limits - Implement exponential backoff Limit token usage - Set max_tokens to control costs Validate inputs - Sanitize user prompts Log usage - Track API calls for debugging Conclusion The free Gemini tier via OpenRouter provides an excellent way to integrate AI into Python applications at zero cost. Start with the simple function above, then expand into chatbots, content generators, or analysis tools.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ipsphil_digital/using-the-gemini-api-with-python-free-tier-26cm

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
