---
title: "Build a Crypto Portfolio Tracker with Python"
slug: "build-a-crypto-portfolio-tracker-with-python"
author: "qing"
source: "devto_python"
published: "Sun, 12 Jul 2026 19:02:30 +0000"
description: "Build a Crypto Portfolio Tracker with Python Unlock the Power of Crypto Investing with Python Are you tired of manual calculations and tedious tracking of yo..."
keywords: "portfolio, tracker, data, value, coins, market, coin, performance"
generated: "2026-07-12T19:12:47.057587"
---

# Build a Crypto Portfolio Tracker with Python

## Overview

Build a Crypto Portfolio Tracker with Python Unlock the Power of Crypto Investing with Python Are you tired of manual calculations and tedious tracking of your cryptocurrency portfolio? Do you want to stay on top of your investments and make data-driven decisions? Look no further! In this article, we'll show you how to build a crypto portfolio tracker using Python. Getting Started Before we dive into the code, let's cover the basics. To build a crypto portfolio tracker, we'll need to: Gather data on our cryptocurrency holdings Calculate the current market value of each coin Track the portfolio's performance over time We'll use Python's requests library to fetch data from the CoinGecko API, which provides real-time cryptocurrency prices and market data. Gathering Data To get started, we'll need to install the requests library. You can do this using pip: pip install requests Next, we'll create a function to fetch data from the CoinGecko API. We'll use the requests.get() method to send a GET request to the API and retrieve the data: import requests def get_coin_data ( coin_id ): """ Fetch coin data from CoinGecko API """ url = f " https://api.coingecko.com/api/v3/coins/ { coin_id } " response = requests . get ( url ) data = response . json () return data This function takes a coin ID as an argument and returns the coin's data as a JSON object. Calculating Market Value Now that we have the coin data, we can calculate the current market value of each coin. We'll use the get_coin_data() function to fetch the coin's current price, and then multiply it by the number of coins we own: def calculate_market_value ( coin_id , num_coins ): """ Calculate market value of a coin """ coin_data = get_coin_data ( coin_id ) current_price = coin_data [ " market_data " ][ " current_price " ][ " usd " ] market_value = current_price * num_coins return market_value This function takes a coin ID and the number of coins we own as arguments and returns the market value of the coin. Tracking Portfolio Performance To track the portfolio's performance over time, we'll need to calculate the percentage change in the portfolio's value. We can do this by comparing the current market value to the previous market value: def calculate_performance ( previous_market_value , current_market_value ): """ Calculate percentage change in portfolio value """ percentage_change = (( current_market_value - previous_market_value ) / previous_market_value ) * 100 return percentage_change This function takes the previous market value and the current market value as arguments and returns the percentage change in the portfolio value. Putting it all Together Now that we have all the individual components, let's put them together to build a complete crypto portfolio tracker. We'll create a PortfolioTracker class that takes a list of coins and their corresponding numbers as arguments: class PortfolioTracker : def __init__ ( self , coins , num_coins ): self . coins = coins self . num_coins = num_coins def get_market_values ( self ): market_values = {} for coin_id , num_coin in self . coins . items (): market_value = calculate_market_value ( coin_id , num_coin ) market_values [ coin_id ] = market_value return market_values def get_performance ( self , previous_market_values ): performance = {} for coin_id , market_value in self . get_market_values (). items (): previous_market_value = previous_market_values [ coin_id ] percentage_change = calculate_performance ( previous_market_value , market_value ) performance [ coin_id ] = percentage_change return performance This class takes a list of coins and their corresponding numbers as arguments and returns a dictionary of market values and a dictionary of percentage changes. Example Use Case Let's say we have a portfolio with the following coins and numbers: coins = { " bitcoin " : 1 , " ethereum " : 2 , " litecoin " : 3 } We can create a PortfolioTracker object and use it to track the portfolio's performance: tracker = PortfolioTracker ( coins , num_coins ) previous_market_values = tracker . get_market_values () current_market_values = tracker . get_market_values () performance = tracker . get_performance ( previous_market_values ) print ( performance ) This will output the percentage change in the portfolio's value for each coin. Conclusion Building a crypto portfolio tracker with Python is a powerful way to stay on top of your investments and make data-driven decisions. With the requests library and a few lines of code, we've created a complete crypto portfolio tracker that can be used to track the portfolio's performance over time. Whether you're a seasoned investor or just starting out, this tracker is a valuable tool that can help you maximize your returns and minimize your risks. So why wait? Start building your crypto portfolio tracker today! 🛠️ Recommended Tool If you found this useful, check out Content Creator Ultimate Bundle (Save 33%) — $29.99 and designed for developers like you. Get instant access to our best-selling AI Dev Boost, HTML Landing Page Templates, AI Prompts for Developers, and Python Automation Scripts Pack, perfect for content creators and marketers looking to elevate their game. This bundle is a must-have for anyone looking to create stunning content, build high-converting landing pages, and drive real results. With these tools, you'll be able to create engaging content, build beautiful landing pages, and boost your online presence.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/qingluan/build-a-crypto-portfolio-tracker-with-python-3fmn

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
