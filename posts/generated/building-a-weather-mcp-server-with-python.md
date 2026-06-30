---
title: "Building a Weather MCP Server with Python"
slug: "building-a-weather-mcp-server-with-python"
author: "Mary Luz Chura Ticona"
source: "devto_python"
published: "Tue, 30 Jun 2026 03:34:00 +0000"
description: "Building a Weather MCP Server with Python Introduction The Model Context Protocol (MCP) is an open standard that allows AI models like Claude to connect with..."
keywords: "mcp, server, weather, current, city, client, python, httpx"
generated: "2026-06-30T04:06:54.983230"
---

# Building a Weather MCP Server with Python

## Overview

Building a Weather MCP Server with Python Introduction The Model Context Protocol (MCP) is an open standard that allows AI models like Claude to connect with external tools and data sources. In this article, I'll show you how to build a Weather MCP Server using Python that any MCP client can use. What We'll Build A simple MCP Server with one tool: get_weather — it receives a city name and returns current temperature, wind speed, and humidity using the Open-Meteo API (free, no API key required). Requirements Python 3.12+ mcp[cli] httpx Installation pip install "mcp[cli]" httpx The Code from mcp.server.fastmcp import FastMCP import httpx mcp = FastMCP ( " Weather MCP Server " ) @mcp.tool () async def get_weather ( city : str ) -> str : """ Get current weather for a city. """ geo_url = f " https://geocoding-api.open-meteo.com/v1/search?name= { city } &count=1 " async with httpx . AsyncClient () as client : geo_data = ( await client . get ( geo_url )). json () if not geo_data . get ( " results " ): return f " City ' { city } ' not found. " r = geo_data [ " results " ][ 0 ] lat , lon = r [ " latitude " ], r [ " longitude " ] weather_url = ( f " https://api.open-meteo.com/v1/forecast " f " ?latitude= { lat } &longitude= { lon } " f " &current=temperature_2m,wind_speed_10m,relative_humidity_2m " f " &timezone=auto " ) async with httpx . AsyncClient () as client : current = ( await client . get ( weather_url )). json ()[ " current " ] return ( f " Weather in { r [ ' name ' ] } , { r [ ' country ' ] } : \n " f " Temperature: { current [ ' temperature_2m ' ] } °C \n " f " Wind Speed: { current [ ' wind_speed_10m ' ] } km/h \n " f " Humidity: { current [ ' relative_humidity_2m ' ] } % " ) if __name__ == " __main__ " : mcp . run () Testing with MCP Inspector Run the development server: mcp dev server.py This opens the MCP Inspector in your browser where you can test the get_weather tool with any city name. Result When tested with "Lima", the server returned: Temperature: 19.0°C Wind Speed: 12.2 km/h Humidity: 81% Repository The full source code is available on GitHub: weather-mcp-server Conclusion MCP makes it easy to extend AI capabilities with real-world data. With just a few lines of Python, we built a working weather tool that any MCP client like Claude or VSCode can use.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/marychuraticona/building-a-weather-mcp-server-with-python-11g4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
