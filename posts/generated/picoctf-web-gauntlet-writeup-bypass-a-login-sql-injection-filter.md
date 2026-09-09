---
title: "PicoCTF Web Gauntlet Writeup — Bypass a Login SQL Injection Filter"
slug: "picoctf-web-gauntlet-writeup-bypass-a-login-sql-injection-filter"
author: "CTFDojo"
source: "devto_webdev"
published: "Wed, 09 Sep 2026 20:31:56 +0000"
description: "The login form filters classic SQL keywords (spaces, OR , -- ) in an overly simplistic way. By varying the case and using syntactic equivalents, we bypass th..."
keywords: "username, sql, filter, case, password, test, injection, bypass"
generated: "2026-09-09T20:46:26.462195"
---

# PicoCTF Web Gauntlet Writeup — Bypass a Login SQL Injection Filter

## Overview

The login form filters classic SQL keywords (spaces, OR , -- ) in an overly simplistic way. By varying the case and using syntactic equivalents, we bypass the filter and authenticate without a valid password. Platform: picoGym Category: Web Exploitation Points: 200 pts Difficulty: Intermediate Technique: SQL injection, filter bypass Challenge description The challenge presents a classic login form, with a username field and a password field. Nothing else is provided in the prompt, aside from a link to the application: "Log in as admin! http://saturn.picoctf.net:PORT/ " When we enter an invalid credential, the application returns an error message that hints at what's happening server-side: something like Login failed for user: ... , strongly suggesting a SQL query of the form SELECT * FROM users WHERE username='...' AND password='...' . Step 1 — Basic injection test Classic reflex when facing a login form suspected of being vulnerable: attempt a basic SQL injection in the username field, leaving the password empty or arbitrary. Username : ' OR 1=1 -- - Password : anything On a naive form, this payload turns the query into SELECT * FROM users WHERE username='' OR 1=1 -- -' AND password='...' , which authenticates anyone. But here, the server's response is different: 403 Forbidden — malicious keyword detected The site is therefore actively filtering certain keywords before executing the query. We need to understand precisely what's being blocked. Step 2 — Identify the filter word by word We isolate each component of the previous payload and test it separately to see which one triggers the block: Test 1: Username = OR → blocked Test 2: Username = -- → blocked Test 3: Username = ' '(space) → allowed through Test 4: Username = 1=1 → allowed through Test 5: Username = oR → allowed through! Two important observations emerge from these tests: The filter blocks the keyword OR and the SQL comment -- when written exactly as-is The filter is case-sensitive — it looks for the exact uppercase string OR , not a case-insensitive variant This is a classic design flaw: a hardcoded keyword blacklist, applied with a case-sensitive comparison, without normalizing the string to upper or lower case before comparing it. Step 3 — Bypass the filter With this case-sensitivity flaw identified, we can rebuild a working payload simply by avoiding the exact spelling of the blocked words: ' oR 1=1 -- - → "oR" passes the filter, remains a valid OR in SQL ' oR 1 = 1 # → MySQL comment alternative ( # ) instead of -- Some filters also block spaces around keywords. In that case, a classic trick is to replace spaces with inline SQL comments, which are ignored by the SQL engine but don't contain the forbidden string: '/**/oR/**/1=1/**/--/**/- On this particular challenge, the case variation is already enough to pass the filter — no need to complicate things further. Step 4 — Authentication bypass We send the payload that passes the filter in the username field, with an arbitrary password: Username : admin ' oR ' 1 '=' 1 ' -- - Password : x The query generated server-side becomes (schematically): SELECT * FROM users WHERE username = 'admin' oR '1' = '1' -- -' AND password='x' The condition '1'='1' is always true, and everything after -- is commented out — the password is never checked. We get a success page showing admin access, with the flag: Welcome back, admin! picoCTF{***************************} 🚩 picoCTF{ flag intentionally hidden } The flag is deliberately hidden — follow the method, you've earned it. 💪 Key takeaways This challenge illustrates why blacklist filtering is a fundamentally fragile defense against SQL injection: there's always a case variation, encoding, or equivalent syntax that the blacklist didn't anticipate. Keyword blacklist filtering is fundamentally breakable — case variation, alternative spacing, and equivalent SQL syntax almost always find a way around it The real protection against SQL injection is prepared statements or an ORM, never hand-filtered string concatenation Testing each component of a payload separately lets you precisely map out what a filter blocks and what it lets through Originally published on CTFdojo — join the CTFdojo Discord to discuss writeups and get notified about new ones.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ctfdojo/picoctf-web-gauntlet-writeup-bypass-a-login-sql-injection-filter-1ih4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
