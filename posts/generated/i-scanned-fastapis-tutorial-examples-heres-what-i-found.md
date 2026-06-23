---
title: "I scanned FastAPI's tutorial examples. Here's what I found."
slug: "i-scanned-fastapis-tutorial-examples-heres-what-i-found"
author: "Moon sehwan"
source: "devto_python"
published: "Tue, 23 Jun 2026 03:50:41 +0000"
description: "FastAPI's official docs are beautiful. I love them. So I scanned them through AINAScan . Here's what I found. The Setup FastAPI's tutorial examples are desig..."
keywords: "fastapi, user, tutorial, ainascan, app, async, def, result"
generated: "2026-06-23T04:02:13.416792"
---

# I scanned FastAPI's tutorial examples. Here's what I found.

## Overview

FastAPI's official docs are beautiful. I love them. So I scanned them through AINAScan . Here's what I found. The Setup FastAPI's tutorial examples are designed to teach. They're intentionally simplified. That's not a criticism — it's a design choice. But I wanted to know: when someone copies those examples directly into a production app (which happens constantly), what's the actual risk profile? I ran the examples through AINAScan, which tracks taint across variable assignments and detects 48 patterns across 9 languages. Here are the results. Finding 1: The Classic SQL Injection Teaching Example # From FastAPI's SQL tutorial (simplified) from fastapi import FastAPI import sqlite3 app = FastAPI () @app.get ( " /users/{user_id} " ) async def get_user ( user_id : str ): conn = sqlite3 . connect ( " sql_app.db " ) user = conn . execute ( f " SELECT * FROM users WHERE id = ' { user_id } '" ). fetchone () return { " user " : user } AINAScan result: BLOCK: SQL_INJECTION_RISK L5 → f-string in execute() taint: user_id (path param) → SQL query string Score deduction: -28 pts The tutorial goes on to show SQLAlchemy (the right way), but the raw sqlite3 example is what gets copied first. The f-string SQL stays in the codebase. The SQLAlchemy refactor gets marked as "TODO." Fix: user = conn . execute ( " SELECT * FROM users WHERE id = ? " , ( user_id ,) ). fetchone () Finding 2: The async def Trap FastAPI makes async look easy. Which causes this: @app.post ( " /process " ) async def process_file ( file : UploadFile ): content = file . read () # blocks result = heavy_computation ( content ) # blocks db . save ( result ) # blocks return { " status " : " done " } AINAScan result: WARN: FAKE_ASYNC L2 → async def with no await All calls are synchronous — blocks the event loop Score deduction: -6 pts The function is async in name only. Under load, this serializes every request. FastAPI even documents this — use def for blocking operations, async def only when you actually await . But the template makes everything async by default. Fix: @app.post ( " /process " ) def process_file ( file : UploadFile ): # regular def = FastAPI runs in threadpool content = file . read () result = heavy_computation ( content ) db . save ( result ) return { " status " : " done " } Finding 3: The Save That Saves Nothing This one shows up in almost every vibe-coded FastAPI app: @app.post ( " /users/ " ) async def create_user ( user : UserCreate ): # "Save" user new_user = { " id " : generate_id (), " name " : user . name , " email " : user . email } return new_user # returns the dict but never stores it AINAScan result: BLOCK: MISSING_WRITE L8 → create_user() has no DB write Function name implies persistence, no INSERT/save found Score deduction: -10 pts The function looks complete. It takes a UserCreate model, generates an ID, returns a response. But nothing was saved anywhere. The next request has no memory of this user. This is the defining vibe-coding bug: it looks like it works because it returns a 200 with data. It only fails when you try to retrieve the user later. Finding 4: Hardcoded Development Credentials Found across multiple tutorial snippets and community examples: DATABASE_URL = " postgresql://postgres:admin123@localhost/myapp " SECRET_KEY = " 09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7 " ALGORITHM = " HS256 " AINAScan result: BLOCK: HARDCODED_SECRET L1,L2,L3 Variables: DATABASE_URL, SECRET_KEY Score deduction: -22 pts (first), -13.2 pts (second) The tutorial context is clear: these are examples. But SECRET_KEY = "09d25e094..." from the FastAPI JWT tutorial is one of the most Googled strings in Python. It's in production codebases right now. Fix: import os DATABASE_URL = os . environ [ " DATABASE_URL " ] SECRET_KEY = os . environ [ " SECRET_KEY " ] The Score If I assembled these four patterns into a single file and scanned it: HARDCODED_SECRET (2x) → -22 + -13.2 = -35.2 SQL_INJECTION_RISK → -28.0 MISSING_WRITE → -10.0 FAKE_ASYNC → -6.0 Starting score: 100 Final score: 20.8 → Grade D 😱 A D. Built entirely from official tutorial copy-paste. Why This Happens FastAPI tutorials optimize for teaching concepts, not production safety. That's correct — teaching should minimize noise. The problem is the copy-paste gap. Between "this is for illustration" and "this code runs on my server" there's no friction. The tutorial doesn't stop you. Three things that would help: Security comments in examples — # NEVER USE F-STRINGS HERE — use parameterized queries Pre-commit hooks — catch these before they hit main Automated scanning — AINAScan runs in under 3 seconds Try It Paste your FastAPI routes at AINAScan . Free, no signup. Or curl it: curl -X POST https://pleasing-transformation-production-90c2.up.railway.app/v1/scan \ -H 'X-API-Key: vg_free_test' \ -F 'file=@main.py' What's your FastAPI app's score? Drop it in the comments. AINAScan: 48 patterns · 9 languages · github.com/moonsehwan/aina-scan

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/_55c9ae90dd2b13bd715f5/i-scanned-fastapis-tutorial-examples-heres-what-i-found-31mp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
