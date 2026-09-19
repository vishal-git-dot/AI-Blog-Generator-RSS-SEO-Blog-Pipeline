---
title: "Automating SQLite Database Backups with Python and Cron on Linux"
slug: "automating-sqlite-database-backups-with-python-and-cron-on-linux"
author: "Python.Coding"
source: "devto_python"
published: "Sat, 19 Sep 2026 15:28:52 +0000"
description: "SQLite databases are lightweight, serverless, and widely used in modern web applications. However, because SQLite stores data in a single file on disk, an ac..."
keywords: "backup, cron, script, database, file, python, your, path"
generated: "2026-09-19T15:42:01.043418"
---

# Automating SQLite Database Backups with Python and Cron on Linux

## Overview

SQLite databases are lightweight, serverless, and widely used in modern web applications. However, because SQLite stores data in a single file on disk, an accidental file deletion or hardware failure can result in total data loss. In this tutorial, you will build an automated backup pipeline for an SQLite database using Python and schedule it to run in the background using Linux cron . Prerequisites To follow along, you will need: A Linux system (Arch, Ubuntu, or Debian). Python 3 installed on your system. Basic familiarity with the Linux command line. Step 1: Create the Python Backup Script Python includes built-in support for SQLite via the sqlite3 module. The sqlite3.Connection.backup() method allows you to create a live copy of your database without interrupting running applications. To ensure the script functions properly when executed by cron (which defaults to running from your home directory), dynamic absolute paths are resolved relative to the script location. Create a script file named backup.py : import sqlite3 import datetime import os # Resolve absolute paths relative to the script location SCRIPT_DIR = os . path . dirname ( os . path . abspath ( __file__ )) DB_PATH = os . path . join ( SCRIPT_DIR , " app.db " ) BACKUP_DIR = os . path . join ( SCRIPT_DIR , " backups " ) def create_backup (): # Ensure backup directory exists if not os . path . exists ( BACKUP_DIR ): os . makedirs ( BACKUP_DIR ) # Generate timestamped filename timestamp = datetime . datetime . now (). strftime ( " %Y%m%d_%H%M%S " ) backup_path = os . path . join ( BACKUP_DIR , f " backup_ { timestamp } .db " ) source_conn = None backup_conn = None # Perform live database backup try : source_conn = sqlite3 . connect ( DB_PATH ) backup_conn = sqlite3 . connect ( backup_path ) with backup_conn : source_conn . backup ( backup_conn ) print ( f " [SUCCESS] Backup created at { backup_path } " ) except sqlite3 . Error as e : print ( f " [ERROR] Backup failed: { e } " ) finally : if source_conn : source_conn . close () if backup_conn : backup_conn . close () if __name__ == " __main__ " : create_backup () Step 2: Verify the Script Manually Initialize a test database and execute the backup script to ensure it creates timestamped files correctly. Run these commands in your terminal: # Create a test database file sqlite3 app.db "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT);" # Run the Python script python3 backup.py Output: [SUCCESS] Backup created at /home/luky/projects/backups/backup_20260917_204500.db Verify that the backup folder contains the new database file: ls -l backups/ Step 3: Automate Execution with Cron To run this backup script automatically every day at midnight, configure a user cron job. Open your cron configuration table: crontab -e Add the following schedule line at the bottom of the file (replace /home/luky/projects with your actual directory path): 0 0 * * * /usr/bin/python3 /home/luky/projects/backup.py >> /home/luky/projects/backup.log 2>&1 0 0 * * * : Runs the command every midnight. >> backup.log 2>&1 : Redirects output and error logs to a log file for debugging. Step 4: Test Cron Execution You can test if the cron environment works immediately by temporarily setting the schedule to run every minute ( * * * * * ). After one minute, check the log file: cat backup.log Output: [SUCCESS] Backup created at /home/luky/projects/backups/backup_20260917_204600.db Once confirmed, change your crontab entry back to 0 0 * * * . Conclusion Combining Python's native sqlite3.backup() API with Linux cron provides an efficient, lightweight backup system that runs automatically in the background without requiring external database servers.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/pythoncoding1/automating-sqlite-database-backups-with-python-and-cron-on-linux-ggk

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
