---
title: "Nothing worked, and nothing said so"
slug: "nothing-worked-and-nothing-said-so"
author: "Lisandro Reinoso"
source: "devto_ai"
published: "Wed, 07 Oct 2026 22:51:54 +0000"
description: "Today the session log of the coordinator project has, for Saturday, October 3, four numbered sessions in the Mac's range and four in Windows's without collid..."
keywords: "nothing, windows, session, mac, repos, machine, both, first"
generated: "2026-10-07T22:56:27.549862"
---

# Nothing worked, and nothing said so

## Overview

Today the session log of the coordinator project has, for Saturday, October 3, four numbered sessions in the Mac's range and four in Windows's without colliding. I built that coexistence that night, after discovering that on Windows nothing worked and nothing said so. An arrow on Windows The repos were there, but the toolkit assumed the Mac: paths with its username, a file-locking module ( fcntl ) that only exists on Unix, python3 and bash within reach. With winget I installed Python 3.12 and Git for Windows, and added a python3.exe copy to cover the Microsoft Store shortcut. Still, the hooks didn't throw errors: they did nothing. A character encoding is the table that translates each letter or symbol into bytes. If the program writes a symbol that the machine's table doesn't have, the write fails, and if nobody looks at that failure, the program simply does nothing. Windows prints with cp1252, which doesn't have the arrow → , and my hooks used it. The fix was an environment variable, PYTHONUTF8=1 , which is still in my global configuration today. 20:37 That night's session closed at 20:37. It left the same folder structure on both machines (15 repos moved), one numbering range per machine, V01-V49 for the Mac and V51-V99 for Windows, stored in a local file on each machine. The session index had 250 rows for 126 files; instead of regenerating it, I let git merge the two versions line by line with merge=union . Syncing ran through git over 17 separate repos. I chose to replicate the structure because it left the Mac untouched. 20:54 At 20:54, seventeen minutes later, another session started to change that. With both machines working at the same time, 17 separate repos meant that session start only pulled the configuration and the open project, that every close needed two commits and two pushes, and that about 30 access tokens were required. The answer was a monorepo: 11 projects inside, 4 products with their own repo because they can be shared or deployed separately, and the configuration on its own. 21:54 and 22:24 At 21:54 the first commit from Windows landed in the monorepo; at 22:24, the first one from the Mac. What lasted seventeen minutes was the sync layer, not the whole decision: the second decision complements the first. The numbering ranges, PYTHONUTF8=1 and paths relative to the user's home directory are all still in force, and with them both machines write the same log without stepping on each other. I'm not saying everything has run perfectly on both ever since. I'm saying that the first failure that night had no message. The next time something "does nothing" on a new machine, will you look for the error, or ask yourself which failure is staying quiet?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/lisandro_reinoso_d12ac7b9/nothing-worked-and-nothing-said-so-1m1k

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
