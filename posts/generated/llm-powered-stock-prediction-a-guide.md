---
title: "LLM-Powered Stock Prediction: A Guide"
slug: "llm-powered-stock-prediction-a-guide"
author: "shashank ms"
source: "devto_ai"
published: "Mon, 27 Jul 2026 19:39:18 +0000"
description: "We are going to build a lightweight stock analysis agent that pulls 30 days of OHLCV data and generates a structured trading signal via an LLM. This is usefu..."
keywords: "ticker, oxlo, signal, close, json, you, row, content"
generated: "2026-07-27T19:42:31.393927"
---

# LLM-Powered Stock Prediction: A Guide

## Overview

We are going to build a lightweight stock analysis agent that pulls 30 days of OHLCV data and generates a structured trading signal via an LLM. This is useful for developers who want to prototype quantitative strategies without managing model infrastructure or unpredictable token costs. I run this on Oxlo.ai because the flat per-request pricing lets me include the full price history in every prompt without input costs scaling. Details are at https://oxlo.ai/pricing . What you'll need Python 3.10 or newer An Oxlo.ai API key from https://portal.oxlo.ai The OpenAI SDK: pip install openai yfinance and pandas: pip install yfinance pandas Step 1: Fetch market data I use yfinance to download the last 30 trading days for any ticker. This gives the model enough recent history to identify momentum and volatility patterns. import yfinance as yf import pandas as pd def fetch_stock_data(ticker: str, days: int = 30) -> pd.DataFrame: stock = yf.Ticker(ticker) df = stock.history(period=f"{days}d") df = df.reset_index() df["Date"] = df["Date"].dt.strftime("%Y-%m-%d") return df[["Date", "Open", "High", "Low", "Close", "Volume"]] if __name__ == "__main__": df = fetch_stock_data("AAPL") print(df.tail()) Step 2: Format the prompt LLMs parse compact markdown tables reliably, so I format the DataFrame as a pipe-delimited table and prepend a one-line momentum summary. Because Oxlo.ai bills per request rather than per token, adding more rows to the context does not increase the cost. def build_user_message(df: pd.DataFrame, ticker: str) -> str: lines = [ "| Date | Open | High | Low | Close | Volume |", "|---|---|---|---|---|---|" ] for _, row in df.iterrows(): lines.append( f"| {row['Date']} | {row['Open']:.2f} | {row['High']:.2f} " f"| {row['Low']:.2f} | {row['Close']:.2f} | {row['Volume']:.0f} |" ) table = "\n".join(lines) latest = df.iloc[-1] prev = df.iloc[-2] change = (latest["Close"] - prev["Close"]) / prev["Close"] * 100 return f"""Ticker: {ticker} Recent close: ${latest['Close']:.2f} ({change:+.2f}% vs prior day) 30-day OHLCV: {table} Analyze this data and return a JSON object with keys: signal (BUY, HOLD, or SELL), confidence (0-100), and reasoning (one concise paragraph).""" Step 3: Define the system prompt The system prompt forces the model into the role of a disciplined quantitative analyst and locks the output format to JSON. Keeping this separate from the data makes the prompt reusable across tickers. SYSTEM_PROMPT = """You are a senior quantitative analyst. You evaluate short-term equity price data and emit structured trading signals. Rules: - Base your analysis only on the OHLCV data provided. - Output strictly valid JSON with keys: signal, confidence, reasoning. - Signal must be one of: BUY, HOLD, SELL. - Confidence is an integer 0-100. - Reasoning must be one concise paragraph, no bullet points.""" Step 4: Query Oxlo.ai Now we send the formatted message to Oxlo.ai. I use Llama 3.3 70B here because it follows structured instructions accurately and returns clean JSON. Replace YOUR_OXLO_API_KEY with the key from your Oxlo.ai dashboard. from openai import OpenAI import json client = OpenAI(base_url="https://api.oxlo.ai/v1", api_key="YOUR_OXLO_API_KEY") def get_signal(ticker: str) -> dict: df = fetch_stock_data(ticker) user_message = build_user_message(df, ticker) response = client.chat.completions.create( model="llama-3.3-70b", messages=[ {"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": user_message}, ], temperature=0.2, max_tokens=512, ) content = response.choices[0].message.content content = content.replace(" ```json", "").replace("``` ", "").strip() return json.loads(content) Step 5: Parse the output The analyze helper fetches the signal and prints a readable summary. Wrapping the JSON parse in a small function makes it easy to drop into a scheduler or API later. def analyze(ticker: str): result = get_signal(ticker) print(f"Ticker: {ticker}") print(f"Signal: {result['signal']}") print(f"Confidence: {result['confidence']}/100") print(f"Reasoning: {result['reasoning']}") analyze("AAPL") Run it You can run the script against any ticker. Below is the complete entry point and an example of the output you can expect. if __name__ == "__main__": analyze("NVDA") Example output: Ticker: NVDA Signal: HOLD Confidence: 62/100 Reasoning: The stock has shown consolidation over the last week with declining volume after a sharp prior run-up, suggesting indecision between buyers and sellers at current levels. Next steps Feed recent news headlines into the same prompt to add sentiment context. On Oxlo.ai, the extra text does not change what you pay, so you can iterate on richer prompts without surprise token bills. Another concrete move is to wrap the analyze function in a FastAPI endpoint and trigger it via cron each morning.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/shashank_ms_6a35baa4be138/llm-powered-stock-prediction-a-guide-1n7k

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
