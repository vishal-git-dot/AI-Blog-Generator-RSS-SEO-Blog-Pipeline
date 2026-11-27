---
title: "How to Check Every Page on Your Site for Duplicate H1 Tags with Python"
slug: "how-to-check-every-page-on-your-site-for-duplicate-h1-tags-with-python"
author: "Evgenii Kaya"
source: "devto_python"
published: "Fri, 27 Nov 2026 07:27:09 +0000"
description: "When we audited all 199 content URLs on our site, we did not start with Search Console. We started with the HTML the server actually sends, and with a short ..."
keywords: "page, url, text, one, you, template, urls, sitemap"
generated: "2026-11-27T07:44:07.268397"
---

# How to Check Every Page on Your Site for Duplicate H1 Tags with Python

## Overview

When we audited all 199 content URLs on our site, we did not start with Search Console. We started with the HTML the server actually sends, and with a short checklist for each page. One of the simplest checks on that list is also one of the easiest to skip: how many H1 headings does this page have? You want one. A template can add a second without anyone typing it, and once that happens it tends to happen on every page that uses the same template. Here is the small script we used to find that, and to see whether the extras shared a class, which usually means one template fix rather than a page-by-page cleanup. What the script does It reads every URL from your XML sitemap, including sitemap index files, and downloads the raw HTML of each page. It removes scripts, styles, templates and HTML comments, so an <h1> inside a code string or a commented-out block doesn't count. Then it counts the H1s and records their text, their CSS classes and their parent's classes, and writes everything to a CSV. The class columns are the useful part. If the pages with more than one H1 all share the same pair of classes, you have found a template to fix, not a pile of one-off pages. The code You'll need requests , beautifulsoup4 and lxml : pip install requests beautifulsoup4 lxml import csv import sys import time from xml . etree import ElementTree import requests from bs4 import BeautifulSoup , Comment HEADERS = { "User-Agent" : "Mozilla/5.0 (h1-audit)" } NS = { "sm" : "http://www.sitemaps.org/schemas/sitemap/0.9" } def get_urls ( sitemap_url ) : root = ElementTree . fromstring ( requests . get ( sitemap_url , headers = HEADERS , timeout = 20 ) . content ) children = root . findall ( "sm:sitemap/sm:loc" , NS ) if children : return [ url for loc in children for url in get_urls ( loc . text . strip ( ) ) ] return [ loc . text . strip ( ) for loc in root . findall ( "sm:url/sm:loc" , NS ) ] def get_h1s ( url ) : response = requests . get ( url , headers = HEADERS , timeout = 20 , allow_redirects = False ) soup = BeautifulSoup ( response . text , "lxml" ) for tag in soup ( [ "script" , "style" , "noscript" , "template" ] ) : tag . decompose ( ) for comment in soup . find_all ( string = lambda text : isinstance ( text , Comment ) ) : comment . extract ( ) h1s = [ ] for h1 in soup . find_all ( "h1" ) : text = " " . join ( h1 . get_text ( " " ) . split ( ) ) classes = "." . join ( h1 . get ( "class" , [ ] ) ) parent = h1 . parent . get ( "class" , [ ] ) if h1 . parent else [ ] h1s . append ( ( text , classes , "." . join ( parent ) ) ) return response . status_code , h1s def main ( ) : urls = get_urls ( sys . argv [ 1 ] ) limit = int ( sys . argv [ 2 ] ) if len ( sys . argv ) > 2 else None urls = urls [ : limit ] problems = 0 with open ( "h1_audit.csv" , "w" , newline = "" , encoding = "utf-8" ) as file : writer = csv . writer ( file ) writer . writerow ( [ "url" , "status" , "h1_count" , "h1_texts" , "h1_classes" , "parent_classes" ] ) for url in urls : status , h1s = get_h1s ( url ) if len ( h1s ) != 1 : problems += 1 writer . writerow ( [ url , status , len ( h1s ) , " | " . join ( text for text , _ , _ in h1s ) , " | " . join ( cls for _ , cls , _ in h1s ) , " | " . join ( parent for _ , _ , parent in h1s ) , ] ) time . sleep ( 0.5 ) print ( f "Checked {len(urls)} pages, {problems} without exactly one H1. See h1_audit.csv" ) if __name__ == "__main__" : main ( ) Run it with your sitemap and, optionally, a page limit for a quick test: python h1_audit.py https://example.com/sitemap.xml 20 A few details that matter The script reads the HTML the server sends, which is what most crawlers see first. If your site renders content in the browser with JavaScript, you'll need a headless browser instead. Don't follow redirects. With allow_redirects=False , a URL that has already moved shows up with its real status instead of quietly reporting the H1 of a different page. A sitemap shouldn't list URLs that have already moved, so this catches a second problem. Strip comments. Templates often keep old blocks commented out. Without removing comments, a naive count flags those too. Then open the CSV, filter to h1_count not equal to 1, and sort by h1_classes . Group the problems before you edit anything. If they cluster on one or two class pairs, fix the template and run the script again. What to do with the results The usual fix, when a CMS already prints the title as an H1 and a custom hero block adds another, is to change the hero heading to a paragraph or an H2 with the same CSS class. The page looks the same. The title in the CMS stays the only H1. If you have a pre-publish check, make sure it runs on every template, with no section-level exceptions that quietly skip the pages you ship most often. If your site is built from templates, I'd run this after every template change, not just once. It takes a few minutes, and the fix, once you can see the pattern, is usually one or two templates rather than a long page list. I'm Evgenii, founder of NeuroHelper AI, founded in 2024. I write about technical SEO for sites that change fast.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/evgeniikaya/how-to-check-every-page-on-your-site-for-duplicate-h1-tags-with-python-47mm

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
