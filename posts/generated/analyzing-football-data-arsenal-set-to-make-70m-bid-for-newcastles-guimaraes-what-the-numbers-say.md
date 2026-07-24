---
title: "Analyzing Football Data: Arsenal set to make £70m bid for Newcastles Guimaraes — What the Numbers Say"
slug: "analyzing-football-data-arsenal-set-to-make-70m-bid-for-newcastles-guimaraes-what-the-numbers-say"
author: "Muhammad Bin Nazeer"
source: "devto_webdev"
published: "Fri, 24 Jul 2026 03:07:15 +0000"
description: "Analyzing Football Data: Arsenal set to make £70m bid for Newcastles Guimaraes — What the Numbers Say TL;DR : Arsenal are preparing a £70m bid for Bruno Guim..."
keywords: "data, football, guimaraes, live, arsenal, bid, matches, make"
generated: "2026-07-24T03:18:16.302567"
---

# Analyzing Football Data: Arsenal set to make £70m bid for Newcastles Guimaraes — What the Numbers Say

## Overview

Analyzing Football Data: Arsenal set to make £70m bid for Newcastles Guimaraes — What the Numbers Say TL;DR : Arsenal are preparing a £70m bid for Bruno Guimaraes as Mikel Arteta moves to solve the one problem that has quietly dogged his side for two seasons: what happens when Continue reading: Arsenal set to make £70m bid for Newcastles Guimaraes The Data Behind the Story Every major football event generates thousands of data points in real time — xG (expected goals), shots on target, possession pct, and passes completed. Most fans see the headline; data engineers see the underlying stream. Here is a minimal Python snippet to pull live football data: import requests def get_live_football_data ( api_key : str ): resp = requests . get ( " https://api.football-data.org/v4/matches " , headers = { " X-Auth-Token " : api_key } ) matches = resp . json (). get ( " matches " , []) for m in [ x for x in matches if x [ " status " ] == " IN_PLAY " ]: home = m [ " homeTeam " ][ " name " ] away = m [ " awayTeam " ][ " name " ] score = m [ " score " ][ " fullTime " ] print ( f " { home } { score [ ' home ' ] } - { score [ ' away ' ] } { away } " ) return matches live = get_live_football_data ( " YOUR_API_KEY " ) print ( f " Live matches: { len ( live ) } " ) Key Coverage & Analysis Arsenal are preparing a £70m bid for Bruno Guimaraes as Mikel Arteta moves to solve the one problem that has quietly dogged his side for two seasons: what happens when the engine room runs empty. The Brazil international, who captained Newcastle for large stretches of last season and signed a new long-term deal on Tyneside in 2024, has emerged as the clubs priority target in a midfield rebuild that could reshape the balance of power at the top of the Premier League. The proposed fee would make Guimaraes one of the most expensive midfield signings in Arsenals history and represents a decisive shift from the incremental squad-building of recent windows. It is also a direct test of Newcastles r What This Means for Analysts When building a football analytics pipeline, three metrics matter most: Shots on Target per Game — teams averaging below 3.5 have a 78% relegation rate in the final 5 gameweeks Possession Percentage — correlates with press resistance; teams below 44% avg possession are 2.1x more likely to drop Passes Completed in Final Third — the single strongest predictor of chance creation (r2 = 0.71 in EPL data 2020-2026) These are the signals worth instrumenting first in any real-time football event stream. Live Coverage & Full Analysis For complete live scores, match stats, and real-time updates: Arsenal set to make £70m bid for Newcastles Guimaraes — Full Coverage on SportsPortal.net SportsPortal.net aggregates live football data across all major tournaments — built for fans who want more than a scoreline.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/muhammad_binnazeer_6a810/analyzing-football-data-arsenal-set-to-make-ps70m-bid-for-newcastles-guimaraes-what-the-numbers-7ap

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
