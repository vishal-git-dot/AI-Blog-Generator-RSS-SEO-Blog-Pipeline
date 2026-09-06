---
title: "I replaced a paid pomodoro app with a 300-line Python script"
slug: "i-replaced-a-paid-pomodoro-app-with-a-300-line-python-script"
author: "Reza Ghorbanmeyabadi"
source: "devto_python"
published: "Sun, 06 Sep 2026 10:26:11 +0000"
description: "Most pomodoro apps gate your own history behind a paywall. Marinara and Focus To-Do (among others) only keep a month of data on the free tier. I wanted to ac..."
keywords: "end, pomo, time, jalali, calendar, start, csv, row"
generated: "2026-09-06T10:39:35.962380"
---

# I replaced a paid pomodoro app with a 300-line Python script

## Overview

Most pomodoro apps gate your own history behind a paywall. Marinara and Focus To-Do (among others) only keep a month of data on the free tier. I wanted to actually analyze months of tracked time, not lose it after four weeks. On top of that, I track dates on the Persian (Jalali) calendar, which none of the existing tools support at all. So I wrote my own. First pass was a function in a Jupyter notebook logging start/end events to a CSV. It worked, but running a notebook cell every time I wanted to log a task wasn't exactly frictionless for something meant to fire dozens of times a day. v2 turned it into a real CLI: pomo start coding pomo status pomo end pomo agg Each session is one row in a CSV: uuid, date, weekday, task, start_hour, start_minute, end_hour, end_minute, mins start appends a row with the end fields blank; end fills them in on that same row. No state kept in memory between commands, since a CLI invocation is a fresh process every time, so the CSV itself is the source of truth for "is anything currently running." v3 added a calendar toggle, since the Jalali dependency was the whole reason I built this but also the thing that made it useless to most people: export POMODORO_CALENDAR=gregorian # defaults to jalali Everything else (data model, commands, aggregation) stays identical regardless of which calendar is active. Repo's here: GitHub

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rezaghm/i-replaced-a-paid-pomodoro-app-with-a-300-line-python-script-42n6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
