---
title: "Turn Newsletter Replies Into a Feedback Log With 40 Lines of Python"
slug: "turn-newsletter-replies-into-a-feedback-log-with-40-lines-of-python"
author: "AI Automation Enterenpeur"
source: "devto_python"
published: "Fri, 20 Nov 2026 23:37:43 +0000"
description: "Ending a newsletter with one question ("What should we build next?") is one of the cheapest ways to get customer feedback. The hard part isn't getting replie..."
keywords: "msg, text, your, csv, subject, box, newsletter, body"
generated: "2026-11-20T23:51:31.226782"
---

# Turn Newsletter Replies Into a Feedback Log With 40 Lines of Python

## Overview

Ending a newsletter with one question ("What should we build next?") is one of the cheapest ways to get customer feedback. The hard part isn't getting replies. It's not losing them. Here's a small Python script that checks an inbox for new replies to your newsletter, tags each one by keyword, and appends it to a CSV you can open in any spreadsheet. What it does Connects to your inbox over IMAP. Finds unread messages whose subject matches your newsletter's reply subject. Pulls the plain-text body. Tags it as pricing, bug, feature_request, praise or other. Appends date, sender, tag and the first line to newsletter_replies.csv. No third-party packages. Just the standard library. The code import csv import email import imaplib import os from email . utils import parseaddr SUBJECT = "Re: The Weekly Build" # your newsletter's subject TAGS = { "pricing" : [ "price" , "pricing" , "cost" , "plan" ] , "feature_request" : [ "wish" , "would love" , "feature" , "could you add" ] , "bug" : [ "bug" , "broken" , "error" , "doesn't work" ] , "praise" : [ "love" , "great" , "thanks" , "helpful" ] , } def tag_reply ( text ) : text = text . lower ( ) found = [ tag for tag , words in TAGS . items ( ) if any ( w in text for w in words ) ] return ", " . join ( found ) or "other" def get_body ( msg ) : parts = msg . walk ( ) if msg . is_multipart ( ) else [ msg ] for part in parts : if part . get_content_type ( ) == "text/plain" : payload = part . get_payload ( decode = True ) or b "" return payload . decode ( errors = "ignore" ) return "" def main ( ) : box = imaplib . IMAP4_SSL ( os . environ [ "IMAP_HOST" ] ) box . login ( os . environ [ "IMAP_USER" ] , os . environ [ "IMAP_PASS" ] ) box . select ( "INBOX" ) _ , ids = box . search ( None , f '(UNSEEN SUBJECT "{SUBJECT}")' ) with open ( "newsletter_replies.csv" , "a" , newline = "" ) as f : writer = csv . writer ( f ) for num in ids [ 0 ] . split ( ) : _ , data = box . fetch ( num , "(RFC822)" ) msg = email . message_from_bytes ( data [ 0 ] [ 1 ] ) _ , sender = parseaddr ( msg [ "From" ] ) body = get_body ( msg ) . strip ( ) first_line = body . splitlines ( ) [ 0 ] [ : 200 ] if body else "" writer . writerow ( [ msg [ "Date" ] , sender , tag_reply ( body ) , first_line ] ) box . logout ( ) if __name__ == "__main__" : main ( ) How to run it Set IMAP_HOST, IMAP_USER and IMAP_PASS as environment variables (for Gmail, use imap.gmail.com and an app password), then run: python3 log_replies.py Fetching a message marks it as read, so each reply is logged only once. Schedule it with cron to run every morning: 0 8 * * * cd /path/to/script && python3 log_replies.py Ideas to extend it Strip quoted text (lines starting with ">") so you only keep the new reply. Swap the keyword tagger for an LLM call that returns a tag and a one-sentence summary. Write rows to Google Sheets or your CRM instead of a CSV. Post a Slack or Discord message when a reply is tagged bug. Why bother Keyword tagging won't be perfect, but it turns a pile of unread replies into a sortable list. Once a month, filter by feature_request and you have a ranked, real-words wishlist from your own customers. I build automations like this for businesses and SaaS teams: https://ai-automation-entrepreneur.vercel.app/

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/greatest7/turn-newsletter-replies-into-a-feedback-log-with-40-lines-of-python-3pdm

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
