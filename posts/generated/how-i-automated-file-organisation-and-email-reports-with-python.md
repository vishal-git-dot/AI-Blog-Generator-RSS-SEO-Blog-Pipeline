---
title: "How I Automated File Organisation and Email Reports with Python"
slug: "how-i-automated-file-organisation-and-email-reports-with-python"
author: "Raaga Priya Madhan"
source: "devto_python"
published: "Wed, 08 Jul 2026 08:17:07 +0000"
description: "By Day 6 of my Python freelancing journey, I was building tools that actually save people time at work. Today: organising messy folders automatically and sen..."
keywords: "filename, path, msg, file, python, folder, import, com"
generated: "2026-07-08T08:37:13.649550"
---

# How I Automated File Organisation and Email Reports with Python

## Overview

By Day 6 of my Python freelancing journey, I was building tools that actually save people time at work. Today: organising messy folders automatically and sending emails from Python. The problem these scripts solve Every small business has the same two problems: A downloads folder with 400 unsorted files Someone manually sending the same weekly report email Both are fixable in under 50 lines of Python. Script 1: Auto-organise any folder by file type import os import shutil def organise_folder ( source_folder ): categories = { ' .pdf ' : ' PDFs ' , ' .docx ' : ' Documents ' , ' .xlsx ' : ' Spreadsheets ' , ' .csv ' : ' Spreadsheets ' , ' .png ' : ' Images ' , ' .jpg ' : ' Images ' , } for filename in os . listdir ( source_folder ): filepath = os . path . join ( source_folder , filename ) if os . path . isdir ( filepath ): continue _ , ext = os . path . splitext ( filename ) folder_name = categories . get ( ext . lower (), ' Others ' ) dest = os . path . join ( source_folder , folder_name ) os . makedirs ( dest , exist_ok = True ) shutil . move ( filepath , os . path . join ( dest , filename )) print ( f " Moved { filename } → { folder_name } / " ) Run this on any messy folder and it sorts itself in seconds. The key functions explained os.listdir() returns every file and folder name in a directory as a list. os.path.splitext() splits a filename into its name and extension — so report.pdf becomes ('report', '.pdf') . shutil.move() moves the file to its new home, creating the folder if needed. Script 2: Send automated emails with Python import smtplib from email.mime.text import MIMEText from email.mime.multipart import MIMEMultipart def send_email ( to , subject , body ): msg = MIMEMultipart () msg [ ' From ' ] = " youremail@gmail.com " msg [ ' To ' ] = to msg [ ' Subject ' ] = subject msg . attach ( MIMEText ( body , ' plain ' )) with smtplib . SMTP_SSL ( ' smtp.gmail.com ' , 465 ) as server : server . login ( " youremail@gmail.com " , " your-app-password " ) server . send_message ( msg ) You need a Gmail App Password (not your regular password) — generate one at myaccount.google.com under Security → App passwords. What this can automate for clients Weekly sales report emailed every Monday at 9am Backup confirmation emails after file operations Invoice reminders sent on a schedule Alert emails when a CSV changes or a threshold is crossed This is exactly the kind of script small businesses pay ₹3,000–₹8,000 for as a one-time delivery. Full code: github.com/raaga102005

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/raagawrites/how-i-automated-file-organisation-and-email-reports-with-python-2m1p

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
