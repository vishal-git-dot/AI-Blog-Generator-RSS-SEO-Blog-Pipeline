---
title: "How do I make a Premier League xG shot map in Python?"
slug: "how-do-i-make-a-premier-league-xg-shot-map-in-python"
author: "noah"
source: "devto_python"
published: "Sat, 24 Oct 2026 14:55:49 +0000"
description: "Every located shot a club took in a season, with player, outcome, body part, expected goals and pitch coordinates, plus totals by zone. Code verified October..."
keywords: "shots, goals, zone, data, season, player, outcome, team"
generated: "2026-10-24T15:41:31.908182"
---

# How do I make a Premier League xG shot map in Python?

## Overview

Every located shot a club took in a season, with player, outcome, body part, expected goals and pitch coordinates, plus totals by zone. Code verified October 10, 2026. It takes one call to get_shot_map, 10 credits. The call team takes an abbreviation, a name or an id from list_teams. Season 2025 is 2025-26. Pass against: true to see the shots a club conceded. import requests import pandas as pd API_KEY = " YOUR_API_KEY " resp = requests . post ( " https://mcp.strikerapi.com/v1/get_shot_map " , headers = { " x-api-key " : API_KEY }, json = { " team " : " ARS " , " season " : 2025 , }, timeout = 60 , ) resp . raise_for_status () data = resp . json ()[ " data " ] shots = pd . DataFrame ( data [ " shots " ]) print ( data [ " totals " ]) print ( pd . DataFrame ( data [ " zones " ])[[ " zone " , " shots " , " goals " , " xg " , " conversion " ]]) by_player = shots . groupby ( " player " ). agg ( shots = ( " xg " , " count " ), xg = ( " xg " , " sum " ), goals = ( " outcome " , lambda s : ( s == " goal " ). sum ())) print ( by_player . sort_values ( " xg " , ascending = False ). head ( 8 ). round ( 2 )) # x is distance from the goal line as a share of half the pitch, y runs across it. print ( shots [[ " x " , " y " ]]. describe (). round ( 2 )) You need requests and pandas ( pip install requests pandas ) and a free API key from StrikerAPI . What comes back The data object, trimmed to the first rows. Every value is real output from the run above. { "season" : 2025 , "zones" : [ { "zone" : "six_yard_box" , "shots" : 83 , "goals" : 19 , "on_target" : 28 , "headers" : 53 , "xg" : 26.8 , "conversion" : 0.229 , "share" : 0.16 }, { "zone" : "penalty_area" , "shots" : 298 , "goals" : 34 , "on_target" : 97 , "headers" : 59 , "xg" : 35.57 , "conversion" : 0.114 , "share" : 0.573 }, "...2 more" ], "shots_total" : 538 , "totals" : { "shots" : 538 , "located" : 520 , "goals" : 67 , "on_target" : 169 , "xg" : 72.14 , "xg_per_shot" : 0.139 }, "shots" : [ { "game_id" : "740968" , "date" : "2026-05-24" , "minute" : 4 , "team" : "ARS" , "player" : "Gabriel Jesus" , "outcome" : "woodwork" , "body_part" : "right_foot" , "zone" : "penalty_area" , "xg" : 0.069 , "x" : 0.296 , "y" : 0.362 }, { "game_id" : "740968" , "date" : "2026-05-24" , "minute" : 4 , "team" : "ARS" , "player" : "Noni Madueke" , "outcome" : "saved" , "body_part" : "left_foot" , "zone" : "penalty_area" , "xg" : 0.04 , "x" : 0.282 , "y" : 0.681 }, "...518 more" ], "unlocated_shots" : 18 } What to do next get_events (10 credits). The shots, goals and cards of a single match, with the same xG. get_team_stats (5 credits). Per-match xG for and against, so you do not have to sum shots yourself. Originally published at strikerapi.com .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/noahowsh/how-do-i-make-a-premier-league-xg-shot-map-in-python-pen

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
