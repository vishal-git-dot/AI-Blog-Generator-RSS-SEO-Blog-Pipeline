---
title: "Learning Python by Building a Discord Bot"
slug: "learning-python-by-building-a-discord-bot"
author: "Kapil Gaire"
source: "devto_python"
published: "Sun, 19 Jul 2026 17:57:59 +0000"
description: "What I built A expense tracking Discord bot for groups. It lets a server team register members, log shared expenses and repayments, inspect balances, view tr..."
keywords: "bot, server, when, database, made, python, discord, records"
generated: "2026-07-19T19:13:25.016947"
---

# Learning Python by Building a Discord Bot

## Overview

What I built A expense tracking Discord bot for groups. It lets a server team register members, log shared expenses and repayments, inspect balances, view transaction history, and export records to CSV. Why I built The main reason was to get hang of python language. I am someone who learns by doing. So, when I decided to learn backend with python, I wanted to make a project hard enough to challenge me. Also, this bot solves one of the problems that my friends and I often face. Whenever we go out, one person usually pays for everything. We always say we'll settle the expenses later, but it often gets forgotten for months. Eventually, we have to go through months of bank statements just to figure out who owes whom. And, since this is a discord bot, not a webapp, it feels more natural to add the records and view them in the same place where we chat. Tech Stack I wrote this bot in python using the discord.py library. For the database, I used PostgreSQL. This was also my first time using Postgres. I wrote the queries in plain SQL instead of using an ORM. Features This bot uses slash commands to take input from the server members. Some of the main commands are: /initialize_bot - to create the database and tables. /expense - used to record new expense /repay - used to track when repayment is done. /history - shows the expenses and repayments after last cleared timestamp. /balance - shows how much a member owes to others and others owe them. /clear_records - resets the timestamp after all records are settled. /export_transactions - to export all the records as csv. Working It is a simple implementation where discord.py handles the communication with the members. The bot simply takes the expense or repayment info and stores it in table. When showing history, it compares the added date timestamp of expense and repayment to recent cleared timestamp and shows records after that timestamp. Calculating the balance was a bit tricky part. The balance is calculated by summing each participant's share of expenses using sum aggregate function and subtracting sum of repayments they have already made. Challenges The challenging part was writing SQL queries for calculating balance and history but it was also a exciting part seeing the output table come out as intended after using the query. Another issue I realized much later was when running export command, it was throwing an error every time. After a search, I learnt that discord commands expect a response from the server within 3 seconds. So, it was taking more time to query the database when export command was used. This made me to realize how fragile the entire setup was. At this time, I was running the bot server and the databse server locally. But when this gets deployed, this error can happen for all the commands. To prevent this, we need to "defer" when the command is called and this will give us 15 mins of window to respond. So, I made a custom decorator which defers all the commands when they are called. What I learned First, I became more familiar with the syntax of python. I learned the use of with ... as ... and decorators in python. After writing raw SQL, it taught me how ORM works under the hood. I deployed the bot in Railway and database in Supabase. Both were quite easy. Railway directly deployed the bot from github just like Vercel. What I'd improve The current bot can only run in one server at a time. If used in multiple servers it shouldn't work and even if it did, the records will be mixed in database since there is only one database. I made it like this because if made for multiple servers, the bot needs a lot of time (hours) to propagate the changes made in development. So, when developing it is made for a single server. I also made it for single server but now if I want to make it work accross multiple servers, I will need seperate database for each server, means passing server id to all the database operations which I am too lazy to implement now and I think the goal of this project is fulfilled. Source Code The complete source code is available on GitHub

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kapilgaire312/learning-python-by-building-a-discord-bot-1ndj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
