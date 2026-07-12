---
title: "Python Async Web Scraping: Scrape 1000 Pages in Seconds"
slug: "python-async-web-scraping-scrape-1000-pages-in-seconds"
author: "qing"
source: "devto_python"
published: "Sun, 12 Jul 2026 13:34:12 +0000"
description: "Python Async Web Scraping: Scrape 1000 Pages in Seconds Synchronous scraping is slow - each request blocks until the server responds. With asyncio and httpx ..."
keywords: "html, url, async, asyncio, httpx, return, semaphore, urls"
generated: "2026-07-12T13:38:55.216513"
---

# Python Async Web Scraping: Scrape 1000 Pages in Seconds

## Overview

Python Async Web Scraping: Scrape 1000 Pages in Seconds Synchronous scraping is slow - each request blocks until the server responds. With asyncio and httpx , you can fire off hundreds of requests concurrently and cut your scraping time from minutes to seconds. Installation pip install httpx beautifulsoup4 lxml The Core Concept Sync: fetch(1) -> wait -> fetch(2) -> wait -> fetch(3) -> wait ... Async: fetch(1), fetch(2), fetch(3) all wait at the same time -> results arrive together This is the difference between 300 seconds and 3 seconds for 1000 pages. Complete Async Scraper with Rate Limiting import asyncio import httpx from bs4 import BeautifulSoup from datetime import datetime import json MAX_CONCURRENT = 20 TIMEOUT = 15 async def fetch_one ( client : httpx . AsyncClient , url : str , semaphore : asyncio . Semaphore , ) -> dict : async with semaphore : try : resp = await client . get ( url ) resp . raise_for_status () return { " url " : url , " status " : resp . status_code , " html " : resp . text } except httpx . HTTPStatusError as e : return { " url " : url , " status " : e . response . status_code , " html " : "" , " error " : str ( e )} except httpx . RequestError as e : return { " url " : url , " status " : 0 , " html " : "" , " error " : str ( e )} async def fetch_all ( urls : list [ str ]) -> list [ dict ]: semaphore = asyncio . Semaphore ( MAX_CONCURRENT ) headers = { " User-Agent " : " Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0 " } async with httpx . AsyncClient ( timeout = TIMEOUT , follow_redirects = True , headers = headers , ) as client : tasks = [ fetch_one ( client , url , semaphore ) for url in urls ] results = await asyncio . gather ( * tasks ) return list ( results ) def parse_title ( html : str ) -> str : if not html : return "" soup = BeautifulSoup ( html , " lxml " ) tag = soup . find ( " title " ) return tag . get_text ( strip = True ) if tag else "" async def scrape_urls ( urls : list [ str ]) -> list [ dict ]: print ( f " Starting async scrape of { len ( urls ) } URLs... " ) start = datetime . now () raw_results = await fetch_all ( urls ) parsed = [] ok_count = 0 for result in raw_results : title = parse_title ( result [ " html " ]) parsed . append ({ " url " : result [ " url " ], " status " : result [ " status " ], " title " : title , " error " : result . get ( " error " , "" ), }) if result [ " status " ] == 200 : ok_count += 1 elapsed = ( datetime . now () - start ). total_seconds () print ( f " Done: { ok_count } / { len ( urls ) } OK in { elapsed : . 1 f } s " ) print ( f " Speed: { len ( urls ) / elapsed : . 1 f } pages/sec " ) return parsed async def main (): base = " https://docs.python.org/3/library/ " modules = [ " asyncio.html " , " pathlib.html " , " dataclasses.html " , " typing.html " , " functools.html " , " itertools.html " , " collections.html " , " contextlib.html " , " logging.html " , " unittest.html " , " json.html " , " csv.html " , " re.html " , " os.html " , " sys.html " , " datetime.html " , " hashlib.html " , " base64.html " , " urllib.request.html " , " http.client.html " , " socket.html " , " ssl.html " , " threading.html " , " multiprocessing.html " , " subprocess.html " , " io.html " , " struct.html " , " array.html " , " queue.html " , " heapq.html " , ] urls = [ base + m for m in modules ] results = await scrape_urls ( urls ) for r in results [: 5 ]: icon = " OK " if r [ " status " ] == 200 else " ERR " print ( f " [ { icon } ] [ { r [ ' status ' ] } ] { r [ ' title ' ][ : 50 ] } " ) with open ( " docs_scrape.json " , " w " ) as f : json . dump ( results , f , indent = 2 ) print ( f " Saved { len ( results ) } results " ) if __name__ == " __main__ " : asyncio . run ( main ()) Retry Logic with Exponential Backoff async def fetch_with_retry ( client : httpx . AsyncClient , url : str , semaphore : asyncio . Semaphore , retries : int = 3 , ) -> dict : async with semaphore : for attempt in range ( retries ): try : resp = await client . get ( url ) resp . raise_for_status () return { " url " : url , " html " : resp . text , " ok " : True } except ( httpx . TimeoutException , httpx . ConnectError ): if attempt < retries - 1 : await asyncio . sleep ( 2 ** attempt ) else : return { " url " : url , " html " : "" , " ok " : False , " error " : " Max retries " } except httpx . HTTPStatusError as e : if e . response . status_code >= 500 : await asyncio . sleep ( 1 ) else : return { " url " : url , " html " : "" , " ok " : False , " error " : f " HTTP { e . response . status_code } " } return { " url " : url , " html " : "" , " ok " : False , " error " : " Unknown " } Practical Tips Start with 5-10 concurrent requests, increase only if the server allows it asyncio.Semaphore is your throttle - never skip it for polite scraping asyncio.gather(*tasks, return_exceptions=True) prevents one failure from cancelling all tasks Stream large responses with client.stream() to avoid memory issues Reuse the AsyncClient - creating one per request is slow and wastes connections Follow me for more Python tips! 🐍

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/qingluan/python-async-web-scraping-scrape-1000-pages-in-seconds-c6p

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
