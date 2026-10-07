---
title: "How I scrape any website in under 5 minutes (Python + Playwright)"
slug: "how-i-scrape-any-website-in-under-5-minutes-python-playwright"
author: "Kabir Hossain"
source: "devto_python"
published: "Wed, 07 Oct 2026 04:48:09 +0000"
description: "python, webdev, tutorial, automation Every scraping tutorial I've read online ends the same way. "Here's how to grab a title with BeautifulSoup." Twenty line..."
keywords: "what, scraping, python, you, audit, tendem, github, how"
generated: "2026-10-07T05:20:33.232828"
---

# How I scrape any website in under 5 minutes (Python + Playwright)

## Overview

python, webdev, tutorial, automation Every scraping tutorial I've read online ends the same way. "Here's how to grab a title with BeautifulSoup." Twenty lines of Python. Works on the demo page. Fails on a real website. That bothered me for a long time. Because real websites are messy. They use JavaScript. They block bots. They hide data behind logins. They paginate. They rename their HTML classes every few months and break every script you've written. So instead of writing another "20-line scraper" tutorial, I want to show you what actual production scraping looks like. Not the theory — the workflow I use for real client jobs. What most tutorials skip When someone asks me to scrape a site, I don't open a fresh Python file and start writing selectors. I follow a process. Step one is an audit. I check the site first. Is it static HTML or JavaScript-rendered? Does it have clear repeating elements like product cards? Does it paginate cleanly? Does robots.txt allow scraping? If I skip this step, I waste hours trying to scrape a site that was never going to work. Five minutes of auditing saves five hours of frustration. Building the audit as a tool Since I audit every site the same way, I automated the audit itself. Here's what my tool does when I run it: bash tendem-audit It asks for a URL. Then it: Fetches the page using the same fetch strategy I use for scraping (static HTTP first, Playwright second) Checks robots.txt Auto-detects the repeating card block using heuristics Fingerprints the CMS (Shopify, WooCommerce, WordPress, Magento) Prints a verdict: green, yellow, orange, or red Green means I can quote the job today. Red means I politely decline. That one step — automating the audit — saved me more time than any scraper I've written. The actual scraping Once I know the site is scrapeable, the scraping itself is boring. That's how it should be. bash tendem-scrape https://shop.example.com/products --preset shopify --max-pages 50 --format csv,json,sqlite That one command: Fetches all 50 pages automatically by following the "Next" link Uses the WooCommerce preset to find the right fields (title, price, image, link) Handles the pagination URL changes Merges items into one dataset Writes CSV, JSON, and SQLite files Total time: two minutes. For a 1,000-product catalog. What production scraping actually means The scraping part is 20% of the job. The other 80% is what makes a client pay. Here's what I deliver for every scraping job — no exceptions: Clean CSV, ready to open in Excel Not a raw dump. Columns with the right names. No hidden characters. UTF-8 BOM so Excel doesn't mangle it. Interactive HTML dashboard A single file the client opens in their browser. Sortable columns. Filterable search box. Works offline. No dependency on my server. Data quality report A file that lists exactly what problems I found: missing titles, empty prices, duplicate rows, broken image links. Clients trust the data because they can see what was checked. Audit trail What was scraped, when, from what URL, by what method. If the client asks "how did you get this?", the answer is one JSON file away. The technical stack For those who want to know how it works under the hood: Python 3.10 or newer Playwright for anything JavaScript-rendered BeautifulSoup with lxml for parsing Pydantic v2 for validated data models SQLite or PostgreSQL for storage GitHub Actions for the CI pipeline Pytest and Allure for tests and reports The framework has over 70 automated tests. There's a public test dashboard on GitHub Pages that shows them passing. What I learned doing this for real clients Three things stand out. First, sessions and logins matter more than anything. Half the sites I scrape require a login. If you don't learn how to save cookies and reuse them, half the job disappears. Second, quality control is what clients actually pay for. A raw CSV is worth ten dollars. A CSV plus a quality report plus a dashboard is worth a hundred. Same data, different packaging. Third, when a site changes, your tests catch it before the client does. That's not a nice-to-have — it's the difference between a one-off job and a monthly subscription. Try it yourself bash git clone https://github.com/pranromumu/tendem-scraper cd tendem-scraper python -m venv .venv source .venv/bin/activate pip install -e ".[dev]" playwright install chromium tendem-scrape https://books.toscrape.com/ --max-pages 3 --open The last command scrapes three pages and opens the dashboard in your browser. What's next I'm building this out as a service for e-commerce sellers and marketing agencies who need competitor pricing, product catalogs, and lead lists on a schedule. If you have a scraping project in mind, or you just want to talk about Python automation, feel free to reach out. The GitHub repo is open source. Fork it, break it, submit a pull request. About me: I'm a web scraping and automation engineer based in Malaysia. I build Python tools that extract data from websites and deliver clean, structured files with quality guarantees. Live demo: https://pranromumu.github.io/tendem-scraper/ GitHub repo: https://github.com/pranromumu/tendem-scraper Fiverr gig: https://www.fiverr.com/s/3AAA3yL If you found this post useful, connect with me. I write about Python, scraping, and automation for real client work.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/prantomomo/how-i-scrape-any-website-in-under-5-minutes-python-playwright-25d3

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
