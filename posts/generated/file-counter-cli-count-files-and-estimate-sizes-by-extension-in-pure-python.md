---
title: "File Counter CLI: Count Files and Estimate Sizes by Extension in Pure Python"
slug: "file-counter-cli-count-files-and-estimate-sizes-by-extension-in-pure-python"
author: "poolion"
source: "devto_python"
published: "Thu, 20 Aug 2026 01:13:09 +0000"
description: "File Counter CLI: Quick File Counts and Size Estimates by Extension Before committing to Git, auditing your downloads folder, or preparing for disk cleanup, ..."
keywords: "file, files, size, counter, extension, count, python, before"
generated: "2026-08-20T01:35:46.537806"
---

# File Counter CLI: Count Files and Estimate Sizes by Extension in Pure Python

## Overview

File Counter CLI: Quick File Counts and Size Estimates by Extension Before committing to Git, auditing your downloads folder, or preparing for disk cleanup, you often need simple answers: "How many files?" and "What size are they, by type?" This CLI tool provides instant file counts and size estimates broken down by extension—using only Python's standard library. What It Does Count all files : Total number with breakdown by extension Estimate sizes : Storage used per extension group (KB/MB/GB) Control depth : Scan shallow directories or the entire tree Handle errors gracefully : Permission issues skip silently Perfect for quickly auditing folder contents before Git commits, cleanup operations, or understanding storage distribution in your projects. Installation No pip install needed. Drop file-counter.py anywhere and run: chmod +x file-counter.py # Unix/macOS python file-counter.py count -s ./your-folding [ -d depth] On Linux, copy to /usr/local/bin/file-counter to use from anywhere in PATH. Usage Examples Basic File Count python file-counter.py count -s ~/Downloads Shows total files and breakdown by extension: Python scripts *.py Text documents *.txt Images, logs, archives, etc. Size Estimation per Extension python file-counter.py size -s ~/projects -d 0 Scans the entire ~/projects tree (depth=0) and shows how much space each extension type uses. Great for spotting if you've forgotten to clean up old build artifacts or cache files. Quick Summary python file-counter.py summary -s /home/user/work Shows top extensions by count and size—ideal for a quick snapshot of folder contents before running larger scripts or uploads. Command Reference All commands use -s (or --src-dir ) with the starting directory: Command Description count Total file count with breakdown by extension size Counts files and shows size totals per extension summary Quick overview of top extensions Common Options -s , --src-dir Directory to scan ( required ) -d , --depth Maximum directory depth ( 0 = unlimited ) Examples in Action # Count files in current directory one level deep python file-counter.py count -d 1 . # Deep scan of entire /var/log with size breakdown python file-counter.py size -s /var/log -d 3 # Check ~/Downloads before deleting files python file-counter.py summary -s ~/Downloads Code Walkthrough The core function uses os.walk() to traverse directories and accumulate stats: def count_files ( source_dir , max_depth = 0 ): total_count = 0 breakdown = {} for root , dirs , files in os . walk ( source_dir ): current_depth = len ( root . replace ( source_dir , '' ). split ( os . sep )) if max_depth > 0 and current_depth >= max_depth : dirs [:] = [] # Don't descend further for f in files : fp = os . path . join ( root , f ) try : if not os . path . isfile ( fp ): continue ext = os . path . splitext ( f )[ 1 ]. lower () or '' key = ' * ' + ext if ext else ' _no_extension ' total_count += 1 breakdown [ key ] = breakdown . get ( key , 0 ) + 1 except ( OSError , IOError ): continue return total_count , breakdown The size calculator walks the same tree but accumulates file sizes per extension group. Results are sorted by frequency or size depending on the command used. Permission errors are caught and skipped—impossible to access doesn't crash the tool. For extensions without a suffix (common with config files in some systems), the tool groups them as _no_extension for unified counting. The summary command limits output to top 10 largest entries by count and size, keeping results readable even in folders with thousands of files. Why Build This? Before writing complex scripts or using heavy tools, sometimes you just need "how many files" and "what's the size distribution?" Git pre-commit hooks can blow up finding thousands of Python scripts. Downloads folder audits reveal which extension hogs space. Storage quotas looming in cloud environments need quick answers. This tool demonstrates minimal viable thinking: solve one practical problem cleanly without extra features, UIs, or dependencies. A 60-line script that does exactly what you need. Use Cases Git prep : Count commits before pushing to avoid bloating repos with thousands of files Downloads cleanup : See which file type dominates before deletion scripts Storage audits : Identify which extension family (logs, images, builds) needs attention Quick checks : Instant verification before running find or other heavier tools Source Code All code is in the public repository with a permissive license. Readable, dependency-free, and suitable as a starting point for extending into file discovery utilities, duplicate finders, and more. 🔗 Repo : https://github.com/Poolion/file-counter-cli If you find this useful, you can support development: https://www.buymeacoffee.com/poolion

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/poolion/file-counter-cli-count-files-and-estimate-sizes-by-extension-in-pure-python-56gf

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
