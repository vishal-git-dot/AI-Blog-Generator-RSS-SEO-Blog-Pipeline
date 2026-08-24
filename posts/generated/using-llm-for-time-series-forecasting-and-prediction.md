---
title: "Using LLM for Time Series Forecasting and Prediction"
slug: "using-llm-for-time-series-forecasting-and-prediction"
author: "shashank ms"
source: "devto_ai"
published: "Mon, 24 Aug 2026 01:33:50 +0000"
description: "We are building a minimal LLM-powered forecasting agent that fetches the last two weeks of a stock ticker, feeds the closing prices to a model, and returns a..."
keywords: "date, forecast, price, recent, plt, oxlo, you, model"
generated: "2026-08-24T01:41:15.131781"
---

# Using LLM for Time Series Forecasting and Prediction

## Overview

We are building a minimal LLM-powered forecasting agent that fetches the last two weeks of a stock ticker, feeds the closing prices to a model, and returns a structured prediction for the next five business days. This is useful for analysts and developers who want to prototype directional forecasts without training a dedicated statistical model. Because the prompt length grows with the history you provide, Oxlo.ai's flat per-request pricing keeps the cost predictable even when you send dozens of rows. What you'll need An Oxlo.ai API key . The Free plan gives you 60 requests per day, which is plenty for testing. Python 3.10 or newer. The openai , yfinance , pandas , and matplotlib packages. Install them with pip install openai yfinance pandas matplotlib . Step 1: Fetch historical price data We will use yfinance to pull the last 30 days of daily closes for Apple (AAPL) and keep the most recent 10 trading days. This gives the model enough context without overflowing the context window. import yfinance as yf import pandas as pd ticker = "AAPL" df = yf.download(ticker, period="30d", interval="1d") df = df.reset_index() # Flatten multi-level columns if present df.columns = [c[0] if isinstance(c, tuple) else c for c in df.columns] df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d") recent = df[["Date", "Close"]].tail(10) print(recent.to_string(index=False)) Step 2: Format the time series for the LLM LLMs reason best over plain text, so we convert the DataFrame to a simple CSV string. We also build a user message that tells the model exactly what we want. history_csv = recent.to_csv(index=False) user_message = f"""Here are the recent daily closing prices for {ticker}: {history_csv} Predict the closing price for the next 5 business days. Respond only with the requested JSON format.""" Step 3: Define the forecasting system prompt The system prompt constrains the model to emit valid JSON and nothing else. This makes downstream parsing trivial. SYSTEM_PROMPT = """You are a financial forecasting assistant. Given a CSV of recent daily closing stock prices, predict the next 5 business days. Respond ONLY with a JSON object in this exact format: {"forecast": [{"date": "YYYY-MM-DD", "price": }, ...]} Do not include markdown, explanations, or extra text.""" Step 4: Request the forecast from Oxlo.ai Now we send the prompt to Oxlo.ai. I am using llama-3.3-70b because it follows structured instructions well, but qwen-3-32b and deepseek-v3.2 are also solid choices for this task. from openai import OpenAI client = OpenAI(base_url="https://api.oxlo.ai/v1", api_key="YOUR_OXLO_API_KEY") response = client.chat.completions.create( model="llama-3.3-70b", messages=[ {"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": user_message}, ], ) raw_output = response.choices[0].message.content print(raw_output) Step 5: Parse and plot the results We parse the JSON, combine it with the historical data, and write a quick chart to disk so we can see the trend at a glance. import json import matplotlib.pyplot as plt forecast = json.loads(raw_output) forecast_df = pd.DataFrame(forecast["forecast"]) forecast_df["date"] = pd.to_datetime(forecast_df["date"]) forecast_df["price"] = forecast_df["price"].astype(float) recent["Date"] = pd.to_datetime(recent["Date"]) recent["Close"] = recent["Close"].astype(float) plt.figure(figsize=(10, 5)) plt.plot(recent["Date"], recent["Close"], label="Historical", marker="o") plt.plot(forecast_df["date"], forecast_df["price"], label="Forecast", marker="o", linestyle="--") plt.title(f"{ticker} Price Forecast") plt.xlabel("Date") plt.ylabel("Price (USD)") plt.legend() plt.grid(True) plt.tight_layout() plt.savefig("forecast.png") print("Saved forecast.png") Run it Save the complete script as forecast.py , replace YOUR_OXLO_API_KEY with your key from https://portal.oxlo.ai , then execute: python forecast.py Typical output looks like this: Date Close 2025-01-06 226.50 2025-01-07 228.00 2025-01-08 229.50 2025-01-09 230.00 2025-01-10 229.00 2025-01-13 231.00 2025-01-14 232.50 2025-01-15 233.00 2025-01-16 234.00 2025-01-17 233.50 {"forecast": [{"date":"2025-01-21","price":234.20},{"date":"2025-01-22","price":235.50},{"date":"2025-01-23","price":234.80},{"date":"2025-01-24","price":236.00},{"date":"2025-01-27","price":237.10}]} Saved forecast.png Next steps Swap llama-3.3-70b for deepseek-r1-671b or kimi-k2.6 on Oxlo.ai if you want the model to show its reasoning chain before emitting the final JSON. You can also expand the script to backtest the agent by withholding the last 5 known days, requesting a forecast, and computing mean absolute error. Because Oxlo.ai charges a flat rate per request, you can pass 50 rows of history for the same cost as 5 rows, which makes long-context experiments affordable. See https://oxlo.ai/pricing for plan details.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/shashank_ms_6a35baa4be138/using-llm-for-time-series-forecasting-and-prediction-4km9

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
