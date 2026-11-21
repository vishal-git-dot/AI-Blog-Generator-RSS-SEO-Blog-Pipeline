---
title: "PHP's November 2026 Security Release: How to Check, Patch and Restart (and What's New in PHP 8.6)"
slug: "phps-november-2026-security-release-how-to-check-patch-and-restart-and-whats-new-in-php-86"
author: "GeekSpark"
source: "devto_webdev"
published: "Sat, 21 Nov 2026 06:24:59 +0000"
description: "On November 19, 2026, PHP shipped PHP 8.6.0 and, on the same afternoon, security releases for every supported branch: 8.5.13, 8.4.28, 8.3.37 and 8.2.36 . The..."
keywords: "php, cve, security, fpm, can, request, ubuntu, changelog"
generated: "2026-11-21T06:33:10.795982"
---

# PHP's November 2026 Security Release: How to Check, Patch and Restart (and What's New in PHP 8.6)

## Overview

On November 19, 2026, PHP shipped PHP 8.6.0 and, on the same afternoon, security releases for every supported branch: 8.5.13, 8.4.28, 8.3.37 and 8.2.36 . The security releases fix 17 vulnerabilities , seven rated critical. PHP says the critical ones need non-default settings or uncommon setups, but several can lead to running code on the server. The ones most likely to matter: CVE-2026-129289, PHP-FPM request smuggling. If nginx ( fastcgi_keep_conn on ) or Apache ( enablereuse=on ) reuses FastCGI connections, leftover bytes from a request body can be read as a second, forged request that can run code. Standard setups that close the connection aren't affected by the demonstrated attack. Three session bugs (CVE-2026-115560, CVE-2026-126714, CVE-2026-129481), including the upload-progress issue PHP warned about in October. Session upload progress is now off by default . Two PHP 8.5-only bugs in the new fatal-error backtraces. The production setting zend.exception_ignore_args=1 blocks the demonstrated attack. CVE-2026-129291 , which can turn a compromised FPM worker into root when catch_workers_output is on, as it is in the official Docker images. Check properly. Ubuntu and Debian backport fixes without changing the version, so a patched Ubuntu 24.04 still reports PHP 8.3.6. Look for the CVE in the package changelog instead: zcat /usr/share/doc/php*-common/changelog.Debian.gz | grep -m1 CVE-2026-129289 . The fixed Ubuntu 24.04 package is 8.3.6-0ubuntu0.24.04.14 . Then update and restart PHP-FPM (or Apache for mod_php). Docker users should rebuild on the new php: images. If you skipped October's release, this matters even more: the PHP2Shell bugs it fixed have been on CISA's list of exploited vulnerabilities since October 26, and this update covers them too. PHP 8.6 brings partial function application, a \Time\Duration class, clamp() , a SortDirection enum and readonly property defaults. Patch first and test 8.6 later. The exception is PHP 8.2, whose support ends on December 31, 2026. Sources PHP: PHP 8.6.0 released and November 19 security releases PHP 8 ChangeLog (8.5.13, 8.4.28, 8.3.37, 8.2.36) PHP 8.6 release page PHP supported versions GHSA-qc49-hpvq-g2w6: PHP-FPM request smuggling (CVE-2026-129289) GHSA-658j-r8rw-q6mx: Session serializer mismatch (CVE-2026-115560) GHSA-8mjj-2r7p-4hg2: Use-after-free in magic method backtraces (CVE-2026-129474) GHSA-jm4m-qfqx-967m: PHP-FPM epoll use-after-free (CVE-2026-129291) Ubuntu changelog: php8.3 8.3.6-0ubuntu0.24.04.14 Debian security tracker: CVE-2026-129289 CISA Known Exploited Vulnerabilities catalog This is the short version. The full guide, with every step and source, is on GeekSpark .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/_geekspark/phps-november-2026-security-release-how-to-check-patch-and-restart-and-whats-new-in-php-86-32nh

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
