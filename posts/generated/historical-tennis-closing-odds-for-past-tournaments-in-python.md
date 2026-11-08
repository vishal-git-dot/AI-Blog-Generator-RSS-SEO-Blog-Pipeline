---
title: "Historical tennis closing odds for past tournaments, in Python"
slug: "historical-tennis-closing-odds-for-past-tournaments-in-python"
author: "Aurelix Solutions"
source: "devto_python"
published: "Sun, 08 Nov 2026 05:13:53 +0000"
description: "A tennis model or a betting system is only as good as the backtest behind it, and a backtest needs the market's closing prices for the matches you test on. D..."
keywords: "closing, odds, tennis, matches, betexplorer, results, match, you"
generated: "2026-11-08T05:28:47.822175"
---

# Historical tennis closing odds for past tournaments, in Python

## Overview

A tennis model or a betting system is only as good as the backtest behind it, and a backtest needs the market's closing prices for the matches you test on. Daily feeds give you that from now on; for last year's Wimbledon or the 2023 Paris Masters you need the archive. BetExplorer keeps one public results page per tournament season with the closing odds of every match, and each match page lists the closing price of every bookmaker it tracked. This post turns those pages into rows in Python, checks how often the closing favourite won, and notes what the archive does and doesn't contain. Disclosure: I'm Aurelix, and I built the Tennis Odds Scraper , which reads these pages in its History mode. It's a paid tool (prices below). Check the Store page before you buy: prices change. Finding a season On betexplorer.com, go to Tennis, pick the tour (ATP Singles, WTA Singles, Challenger...), the tournament and Results, then choose the year. Past seasons have their own path: /tennis/atp-singles/paris-2023/results/ /tennis/wta-singles/wimbledon-2023/results/ Use the path, not a ?year= link: BetExplorer's robots.txt asks bots not to fetch those query URLs, so the tool reads seasons by path only (a ?year=2023 link you paste is rewritten to the -2023 path). Every match of a season with closing odds pip install apify-client import os from apify_client import ApifyClient client = ApifyClient ( os . environ [ " APIFY_TOKEN " ]) run = client . actor ( " aurelix/tennis-odds-scraper " ). call ( run_input = { " mode " : " history " , " seasons " : [ " /tennis/atp-singles/paris-2023/results/ " , " /tennis/wta-singles/wimbledon-2023/results/ " , ], " bookmakerOdds " : True , " maxResults " : 500 , } ) rows = list ( client . dataset ( run [ " defaultDatasetId " ]). iterate_items ()) print ( len ( rows ), " matches " ) Each row is one match: tournament ("Paris 2023"), round ("Final", "Semi-finals", "1/8-finals"...), date , category , match_type . player1 / player2 as BetExplorer lists them ("Djokovic N."), and with match pages on player1_full_name , player1_url , score ( 6-4 6-3 ) and set_scores . status : finished, retired, walkover or canceled; winner , winner_name , sets_p1 / sets_p2 . odds_p1 / odds_p2 : BetExplorer's average closing odds; implied_prob_p1 / p2 with the margin removed and the overround . bookmaker_odds : each listed bookmaker's closing price and the time it was set; closing_avg_* and closing_best_* across them. In the 2023 Paris final, for example, BetExplorer's average closing odds were 1.33 for Djokovic and 3.34 for Dimitrov, with 12 bookmakers listed; Djokovic won 6-4 6-3. How often did the closing favourite win? done = [ r for r in rows if r [ " status " ] in ( " finished " , " retired " ) and r [ " odds_p1 " ] and r [ " odds_p2 " ]] fav = sum (( r [ " odds_p1 " ] < r [ " odds_p2 " ]) == ( r [ " winner " ] == " player1 " ) for r in done ) print ( f " { fav } of { len ( done ) } matches ( { fav / len ( done ) : . 0 % } ) went to the closing favourite " ) On those two seasons it was 72% each: 38 of 53 priced matches in Paris 2023 and 88 of 123 at Wimbledon 2023 (women's singles). That is the base rate any model has to beat, and the implied probabilities tell you how much the market already knew. For a calibration check, bucket implied_prob_p1 and compare it with how often player 1 actually won in each bucket; with a few seasons of Grand Slams and Masters you have thousands of matches. Several seasons into one table import csv with open ( " closing_odds.csv " , " w " , newline = "" , encoding = " utf-8 " ) as f : w = csv . writer ( f ) w . writerow ([ " tournament " , " round " , " date " , " player1 " , " player2 " , " winner " , " odds_p1 " , " odds_p2 " , " best_p1 " , " best_p2 " , " bookmakers " ]) for r in rows : w . writerow ([ r [ " tournament " ], r [ " round " ], r [ " date " ], r [ " player1 " ], r [ " player2 " ], r [ " winner_name " ], r [ " odds_p1 " ], r [ " odds_p2 " ], r [ " closing_best_p1 " ], r [ " closing_best_p2 " ], r [ " bookmakers_count " ]]) match_id ( bx-l81rCxw4 ) is BetExplorer's own match code, so a second run of the same season returns the same IDs; with incremental on it returns nothing new and charges nothing for matches. What the archive does not have Opening odds. The match pages show each bookmaker's closing price; the opening price and the moves in between are not in the archive pages this mode reads. For matches from now on, the tool's Results mode reads TennisExplorer, which has opening and closing per bookmaker. Surface and rankings. Not on these pages; join them from the tournament's surface and a ranking history if your model needs them. Names as listed. List names are "Surname I."; full names come from match pages (on by default). Times. The time each closing price was set is read as the site's Prague time and converted to UTC. Cost $3.00 per 1,000 matches ($2.50 on paid plans), per-bookmaker closing odds included, plus a $0.005 start fee per run. A Grand Slam draw is about 127 matches, so a season costs about $0.39 on the free plan; Apify's free plan includes $5 of credit a month. Matches outside your filters, beyond maxResults or already returned in only-new mode are not charged. That is less than the dedicated BetExplorer tools on the Apify Store charge, and bookmaker odds cost nothing extra. Links Tennis Odds Scraper on the Apify Store Example repo The daily side of the same tool: tennis results with opening and closing odds from every bookmaker

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/aurelix_solutions/historical-tennis-closing-odds-for-past-tournaments-in-python-2l46

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
