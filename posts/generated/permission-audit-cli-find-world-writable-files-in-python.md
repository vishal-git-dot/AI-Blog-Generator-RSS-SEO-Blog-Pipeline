---
title: "Permission Audit CLI: Find World-Writable Files in Python"
slug: "permission-audit-cli-find-world-writable-files-in-python"
author: "poolion"
source: "devto_python"
published: "Thu, 20 Aug 2026 01:20:30 +0000"
description: "Permission Audit CLI: A Minimal Tool for Security Reviews and Compliance Checks Security audits, compliance reviews, or permission normalization—how do you e..."
keywords: "files, audit, writable, group, perm, world, permission, security"
generated: "2026-08-20T01:35:46.536999"
---

# Permission Audit CLI: Find World-Writable Files in Python

## Overview

Permission Audit CLI: A Minimal Tool for Security Reviews and Compliance Checks Security audits, compliance reviews, or permission normalization—how do you efficiently check which files need attention? This CLI tool reports file permissions (octal modes) and flags world-writable files that violate principle-of-least-access policies. Uses only Python standard library. What It Does Permission listing : Show octal codes like 644 , 755 , 0600 Danger check : Report world-writable or group-writable files (security risks) Ownership flags : Highlight when file UID differs from real user Summary/report modes : Choose compact counts or detailed listings Perfect for: Security audits before deployments or migrations CI/CD checks that fail on 0777 files in production Team directory reviews where shared folders need proper group access Regulatory compliance (documenting state per policy) Installation No pip install needed. Drop perm-audit.py anywhere: python perm-audit.py -d /path/to/dir [ -l depth] [ -v ] [ -w ] Copy to /usr/local/bin/perm-audit for PATH access: cp perm-audit.py /usr/local/bin/perm-audit chmod +x /usr/local/bin/perm-audit Usage Examples Full Audit (Summary Mode) python perm-audit.py -d /home/developer Shows top 20 permission modes sorted by count: Mode counts (octal): 644 1,532 files 0755 482 files 0600 97 files 0644 24 files 0755 18 files Each code means: 0644 : owner rw+group/others r (standard data file) 0755 : owner rwx+group/r-others rx (executable scripts) 0600 : owner-only rw (secrets, keys—safe where restricted) Verbose Listing python perm-audit.py -d /home/projects -v Detailed view with flags: / path / to / file1 . py [ 644 ] executable = False writable = False / path / to / public / index . html [ 644 ] executable = False writable = False [ path !] / etc / passwd [ 0600 ] owner_writable ( uid != real - user ) Truncated paths show first folder—useful for spotting unusual permissions across a tree. Security Check: World-Writable Only Before deploying, find files that allow others to modify: python perm-audit.py -d /var/www/html -w World-writable (mode 06xx ) means anyone with group access can write—common vulnerability when uploads directory isn't cleaned. Use for: Shared team directories : Verify sticky bit on /tmp or correct group perms elsewhere Web roots : Flag writable scripts/CGI in world-writable directories Migrations : Detect files copied from external sources with loose permissions Command Reference All commands use -d with directory to audit: Option Description -d Source directory (required) -l,--depth Max depth (default=2, 0=all paths) `-v Verbose listing (all files) `-w World-writable/security check only Common Workflows Full Security Scan python perm-audit.py -d /home/developer -v -l 2 Reports: Octal permissions sorted by count Writable flags if group/others can write Owner-writable flag for UID mismatches CI/CD Fail Gate Find 0777 files in build: python perm-audit.py -d /tmp/build-artifact -v 2>&1 | grep "0777" Typically indicates scripts copied with full permissions before packaging. For sensitive environments, world-writable files should be rejected by security gates since any user in group can modify file contents. Quick Summary on Production System python perm-audit.py -d /var/www/html -v 2>/dev/null Shows unique permission set. Common for: Data files 644 or 600 (read-only by group/others) Executables/sidecars 755 or 664 (when group owns binaries) Configs 600 in restricted folders, 644 when shared config group exists Code Example The scanner walks directories and builds a permission table: def iterate ( path , depth = 0 ): if depth == 0 or current < depth : try : stat_info = os . stat ( path ) mode = stat . S_IMODE ( stat_info . st_mode ) & 0o777 # Security flags is_world_writable = bool ( mode & stat . S_IWOTH ) is_owner_writable = ( fi . st_uid != os . getuid ()) except OSError : dirs . append ({ ' path ' : path , ' mode ' : ' (error) ' }) Octal representation uses stat() to extract permission bits. Special bits like setuid/setgid are stripped—only user/group/others bits reported. World-writable check uses mode & stat.S_IWOTH (octal 02 bit). Owner-writable flag triggers when file's UID differs from real user—indicates leftover write access after cleanup or elevated process creation. Use Cases Compared Scenario Manual Check This Tool Find world-writable files find -perm o+w (slow) -w flag, instant report Permission summary ls -la page-heavy Compact table/count mode Compliance audit Multiple runs Single pass, sorted output Tools like find . ! -type d -perm /o+w exist but produce verbose listings and require parsing. This tool normalizes to permission code with count summaries—easier for humans scanning results. Web servers show many 644 HTML files while 0600 config files dominate backend directories. When group permissions expand, files may shift to 0775 (executable with group write)—unusual in production environments where binaries should be read-only except for the owner. Code Audit Checklist Use this tool to verify: [ ] Secrets/keys in 0600 , not shared-access modes [ ] Web roots have no world-writable subdirectories [ ] Executables are 755 or group-read only ( 754 ) [ ] No scripts with 0777 in production paths [ ] Logs rotate before accumulation and permissions reset to 0644 Source Code Public repo with examples. Readable, dependency-free, suitable as starting point for security automation or policy enforcement tools. 🔗 Repo : https://github.com/Poolion/perm-audit-cli If you find this useful, you can support development: https://www.buymeacoffee.com/poolion

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/poolion/permission-audit-cli-find-world-writable-files-in-python-2poh

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
