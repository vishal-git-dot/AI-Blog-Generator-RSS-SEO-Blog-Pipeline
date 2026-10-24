---
title: "php -v over SSH doesn’t tell you which PHP your website runs"
slug: "php-v-over-ssh-doesnt-tell-you-which-php-your-website-runs"
author: "Rapls"
source: "devto_webdev"
published: "Sat, 24 Oct 2026 03:55:47 +0000"
description: "After a PHP release, the quickest check is to SSH in and type php -v . I've done that myself. For this post I set up a test machine to see how much that numb..."
keywords: "php, cli, fpm, ini, browser, command, site, you"
generated: "2026-10-24T04:04:22.634498"
---

# php -v over SSH doesn’t tell you which PHP your website runs

## Overview

After a PHP release, the quickest check is to SSH in and type php -v . I've done that myself. For this post I set up a test machine to see how much that number says about the website. Not much. php -v reports the command-line PHP. Your site is served by whatever PHP the web server hands requests to, and on the same box those can be different builds, different versions, with different extensions and different php.ini files. Same machine, two answers I put this together on Ubuntu 24.04: Apache 2.4.58 passing .php requests to PHP-FPM 8.3, and the php command pointing at the PHP 8.4 CLI that was already installed. Then I asked each side who it was. How I checked Result php -v over SSH PHP 8.4.21 (cli) PHP_VERSION from a page in the browser 8.3.6 PHP_SAPI on the command line cli PHP_SAPI in the browser fpm-fcgi php.ini loaded on the command line /etc/php/8.4/cli/php.ini php.ini loaded in the browser /etc/php/8.3/fpm/php.ini WordPress Site Health, opened in the browser 8.3.6, fpm-fcgi The same Site Health data, read from the CLI 8.4.21, cli None of this is new. The PHP manual's chapter on the command line covers the separate SAPI and the separate php.ini. Seeing the two side by side on one machine shows how easy it is to check the wrong one and call it done. Why they drift apart On Ubuntu, each PHP version and each SAPI is its own package: php8.3-cli , php8.3-fpm , php8.4-cli , and so on. The bare php command is a symlink to one of them. $ which -a php php8.3 php8.4 /usr/bin/php /usr/bin/php8.3 /usr/bin/php8.4 $ ls -l /usr/bin/php /usr/bin/php -> /etc/alternatives/php Here it pointed at 8.4. The web server config sent requests to php-fpm8.3 . Those two choices are made in different places, by different people sometimes, and nothing keeps them in sync. It wasn't only the version Halfway through, WordPress refused to load in the browser: Your PHP installation appears to be missing the MySQL extension which is required by WordPress. Please check that the mysqli PHP extension is installed and enabled. From the command line, the same WordPress install worked fine. The 8.4 CLI had mysqli . The 8.3 FPM didn't. php -m happily listed mysqli , because php -m was asking the CLI. Installing php8.3-mysql and restarting FPM fixed the browser side. So the gap covers extensions and ini settings as well as the version number. A check run from the CLI only tells you about the CLI. Checking the PHP your site actually runs The answer has to come from a web request. A tiny file does it. Give it a name nobody will guess, open it in the browser, then delete it: <?php header ( 'Content-Type: text/plain' ); printf ( "PHP_VERSION=%s \n PHP_SAPI=%s \n php.ini=%s \n " , PHP_VERSION , PHP_SAPI , php_ini_loaded_file ()); PHP_VERSION=8.3.6 PHP_SAPI=fpm-fcgi php.ini=/etc/php/8.3/fpm/php.ini phpinfo() tells you the same and much more. I prefer the small file, because forgetting to delete it costs less. On WordPress you don't need a file at all. Tools → Site Health → Info → Server shows the PHP version and SAPI, and since you open it in the browser, it's the web PHP. The catch: WP-CLI runs on the CLI PHP. When I pulled the same Site Health data from the command line, it reported 8.4.21 and cli . If you check from WP-CLI, you're checking the wrong PHP again, just more politely. == Web php_version: 8.3.6 (Supports 64bit values) php_sapi: fpm-fcgi == CLI php_version: 8.4.21 (Supports 64bit values) php_sapi: cli What I check now When I want to know whether a PHP update reached my site, I check from the browser side: the small file, phpinfo() , or Site Health. php -v and WP-CLI tell me about the shell. That's still useful, for cron jobs and CLI scripts, but it isn't the answer to "is my website patched?" One thing I didn't test: what happens when the FPM package updates but the FPM service hasn't restarted yet. I'd expect the old binary to keep serving until a restart, but I haven't measured it, so I won't claim it. What does php -v say on your server, and does it match what your website reports? I build WordPress plugins and write about them at https://raplsworks.com/ . Disclaimer: The tests were run on a test machine I set up for this post. English isn't my first language, so I use an AI assistant to help draft and edit the writing.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rapls/php-v-over-ssh-doesnt-tell-you-which-php-your-website-runs-26b3

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
