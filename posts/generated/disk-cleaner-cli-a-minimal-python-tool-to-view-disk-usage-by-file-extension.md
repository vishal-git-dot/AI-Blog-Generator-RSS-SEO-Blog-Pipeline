---
title: "Disk Cleaner CLI: A Minimal Python Tool to View Disk Usage by File Extension"
slug: "disk-cleaner-cli-a-minimal-python-tool-to-view-disk-usage-by-file-extension"
author: "poolion"
source: "devto_python"
published: "Thu, 20 Aug 2026 01:16:59 +0000"
description: "Disk Cleaner CLI: Instant Report on Which Extensions Fill Your Storage Before cleanup scripts, Git commits, or cloud quota reviews, you often need simple ans..."
keywords: "disk, cleaner, python, size, extension, space, before, you"
generated: "2026-08-20T01:35:46.537400"
---

# Disk Cleaner CLI: A Minimal Python Tool to View Disk Usage by File Extension

## Overview

Disk Cleaner CLI: Instant Report on Which Extensions Fill Your Storage Before cleanup scripts, Git commits, or cloud quota reviews, you often need simple answers: "How much space" and "What's taking up storage?" This CLI tool does both—showing total size and per-extension breakdowns using only Python standard library. What It Does Total space : Sum of all files in directory Extension report : Top 10 extensions by size (KB/MB/GB) Depth control : Scan shallow folders or entire tree JSON output : Machine-readable for automation Perfect for downloads folder audits where tarballs/zip archives dominate, or understanding which file type hogs storage in cloud environments. Installation No pip install needed. Drop disk-cleaner.py anywhere: python disk-cleaner.py -s /path/to/dir [ -d depth] [ -j ] Copy to /usr/local/bin/disk-cleaner for PATH access on Unix systems. Usage Examples Basic Space Report python disk-cleaner.py -s ~/Downloads Shows total space used and top extensions by size, with percentages of the total: Total size: 125.4 MB Top 10 extensions by size: *.tar.gz 98.2 MB (78%) *.zip 24.1 MB (19%) *._no_extension 3.1 MB (<1%) Useful when you download packages, logs tarballs accumulate over time, or want to verify before deleting "temporary" files. Deep Scan of Projects Directory python disk-cleaner.py -s ~/work-projects -d 2 Scans up to 2 directory levels deep—avoiding filesystem traversal but capturing what's truly in your working projects folder. Good when you want to audit /home contents from root and see which subfolder hogs space most. JSON Output for Automation python disk-cleaner.py -s /var/log -j Machine-readable output suitable for piping into dashboards, logging systems, or cleanup automation: { "total" : "8540 MB" , "by_extension" : [ { "*.log" : "7200 MB (84.3%)" }, { "*.conf" : "1140 MB (13.3%)" }, { "*.temp" : "200 MB (2.4%)" } ] } Command Reference All commands use -s (or --src-dir ) with the starting directory: Flag Description -s Source directory to scan (required) -d Maximum depth (0=entire tree, default 2) -j JSON output instead of text Common Workflows # Audit ~/Downloads before cleanup scripts python disk-cleaner.py -s ~/Downloads # Check /var/log before rotation or cleanup python disk-cleaner.py -s /var/log -d 1 # Report in JSON for dashboards python disk-cleaner.py -s ~/work/ -j # Deep scan without depth limits python disk-cleaner.py -s /home/user -d 0 Code Breakdown The tool uses os.walk() to traverse and accumulate per-extension sizes: def scan_directory ( source_dir , max_depth = 0 ): stats = { ' total ' : 0 , ' by_extension ' : {}, ' directories ' : {}} for root , dirs , files in os . walk ( source_dir ): current_depth = len ( root . replace ( source_dir , '' ). split ( os . sep )) # Prune deep folders if limit set if max_depth > 0 and current_depth >= max_depth : dirs [:] = [] continue for f in files : fp = os . path . join ( root , f ) try : size = os . path . getsize ( fp ) ext = os . path . splitext ( f )[ 1 ]. lower () or '' key = ' * ' + ext if ext else ' _no_extension ' stats [ ' by_extension ' ][ key ] = ( stats [ ' by_extension ' ]. get ( key , 0 ) + size ) stats [ ' total ' ] += size except ( OSError , IOError ): continue return stats Permission errors are caught and skipped—unreachable files don't crash the tool. Results sorted by descending size give immediate insight into which file types dominate storage. The "No Extension" group captures config files, binaries, and other paths without extensions—often significant in projects directories with many source code files. Why Build This? Before running massive cleanup scripts or before committing to Git repositories, you often need quick answers: "How much space" and "what's filling it?" Tools like du show totals but not per-extension breakdowns. This tool fills that gap with minimal overhead—just standard library calls giving immediate answers without pip dependencies on storage analysis packages. For downloads folders with many tarballs/zip archives, or projects directories where you need to audit before repository creation, this 60-line script provides exactly what you need: quick space reports by file type. Use Cases Downloads cleanup : Identify which archive types (tarball vs zip) hogs space Git preparation : Know storage footprint before committing large files Quota management : Find which extension family needs attention in cloud environments Logging audits : See if log rotation is working or if old entries dominate Alternative Approaches Compared Other tools like du -h --apparent-size -d 1 show totals per directory but don't break down by file extension. Tools like ncdu provide interactivity but require external dependencies. This script combines both: space totals and extension breakdowns with only Python standard library. Source Code All code is in the public repository with a permissive license. Readable, dependency-free, suitable as starting point for storage analysis automation scripts. 🔗 Repo : https://github.com/Poolion/disk-cleaner-cli If you find this useful, you can support development: https://www.buymeacoffee.com/poolion

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/poolion/disk-cleaner-cli-a-minimal-python-tool-to-view-disk-usage-by-file-extension-136o

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
