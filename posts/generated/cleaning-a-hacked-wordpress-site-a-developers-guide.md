---
title: "Cleaning a Hacked WordPress Site: A Developer's Guide"
slug: "cleaning-a-hacked-wordpress-site-a-developers-guide"
author: "S M Al Nurise"
source: "devto_webdev"
published: "Sun, 22 Nov 2026 19:12:24 +0000"
description: "* Cleaning a Hacked WordPress Site: A Developer's Guide * A hacked WordPress site is one of the worst calls you can get from a client. Google shows a warning..."
keywords: "wordpress, site, malware, hacked, you, removal, core, check"
generated: "2026-11-22T19:16:57.015734"
---

# Cleaning a Hacked WordPress Site: A Developer's Guide

## Overview

* Cleaning a Hacked WordPress Site: A Developer's Guide * A hacked WordPress site is one of the worst calls you can get from a client. Google shows a warning, the site redirects to spam, and the client is losing sales. Here is the developer workflow I use to clean it in 24 hours. * ## 1. Backup and Scan First * Take a backup first, even if the site is infected. Then scan for malware, backdoors, and changed core files. * ## 2. Verify Core, Plugins, and Themes * Check WordPress core with WP-CLI: wp core verify-checksums Check for suspicious plugins and themes: wp plugin list --status=inactive wp theme list Delete anything unknown. Check wp-content/uploads for .php files. There should be none there. * ## 3. Clean the Database * * Search for common malware patterns: * wp db search "eval(base64_decode" --all-tables Clean those entries from wp_posts and wp_options, and check admin users: wp user list --role=administrator 4. Update, Reset Passwords, and Harden Update everything, change all passwords, enable 2FA, and set up a firewall. Then request a Google review in Search Console if you had a blacklist warning. * ## Why Cleanups Fail * Most cleanups fail because of hidden backdoors. If you miss one backdoor file, the malware comes back in a few days. A full scan and hardening after cleanup is what stops it. ## Don't Want to Do It Yourself? ** **I offer a complete WordPress malware removal service on Fiverr: https://www.fiverr.com/alnurise/do-wordpress-malware-removal-and-recover-your-hacked-wordpress-website It includes complete malware removal, backdoor removal, Google blacklist removal, security hardening, security patches, full backup, and a detailed report. Starting at $20, 1-day delivery, 5.0 rated on Fiverr. Have you ever cleaned a hacked WordPress site? What was the trickiest backdoor you found? Let me know in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/alnurise/cleaning-a-hacked-wordpress-site-a-developers-guide-3dbc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
