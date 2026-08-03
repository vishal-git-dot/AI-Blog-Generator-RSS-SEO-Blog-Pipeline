---
title: "Do Not Trust the Green Checkmark"
slug: "do-not-trust-the-green-checkmark"
author: "Onur Kesim"
source: "devto_python"
published: "Mon, 03 Aug 2026 19:33:05 +0000"
description: "Most people trust a green checkmark in a CI pipeline. If every job is marked as successful, we usually believe that everything worked correctly. I was doing ..."
keywords: "test, error, green, results, tests, data, pipeline, continue"
generated: "2026-08-03T19:44:41.764737"
---

# Do Not Trust the Green Checkmark

## Overview

Most people trust a green checkmark in a CI pipeline. If every job is marked as successful, we usually believe that everything worked correctly. I was doing the same. Then I found a case where a completely green workflow was hiding an important problem. While testing hafiza-kur across different platforms, my main goal wasn't just to see green checkmarks. I wanted to build a full list of what broke on which platform. I needed to see every single error, without stopping the pipeline at the first failure. To do this, I added continue-on-error: true to the test steps. It was a conscious choice: let the tests run to the end on every platform, collect the raw logs, and check the results later. Then came Windows with Python 3.11 and 3.13. The test t_y42 ran 58 test scenarios. It took 91 seconds on Py3.11 and 110 seconds on Py3.13 to finish. The heavy lifting was completely done and the assertions ran. Then came the final step: printing the summary of the results to the console. Right on the first line of the summary loop, Python hit a character that the default Windows console couldn't encode. UnicodeEncodeError . The process crashed instantly. All 58 test results vanished before reaching the log file. And because continue-on-error: true was active, CI quietly ignored the crash, cleaned up, and moved forward. The situation got worse when I checked the workflow data using the GitHub Actions API. I expected the step to show a failure, even if the main job continued. It didn't. The API returned: conclusion: success In GitHub Actions, if a step has continue-on-error: true , its conclusion field is recorded as success . The actual failure was hidden in a different, rarely checked field called outcome . That meant one-third of our cross-platform data was completely invisible — but CI was showing it as a green, successful run. I created a separate verification step right after test execution: hukum_kapisi.py (The Gate of Verdicts). This gate runs without continue-on-error . Instead of running the tests again, it reads the raw output logs printed to the screen. It explicitly looks for the lines that print the final test summary. If the log ends before those lines appear, hukum_kapisi.py stops the build immediately with an error. There is a very important limit to how this gate works: this gate never tells you that the test results were green. It only tells you that they were not lost. Confusing "the tests passed" with "the test results were successfully recorded" leads to hidden bugs. hukum_kapisi.py makes sure the log data actually exists; the next tool decides if the tests passed or failed. This problem is not unique to my project, or to Windows encoding bugs. Any CI pipeline that relies on reading screen output, summary loops, or permissive error settings can suffer from silent data loss. If your pipeline depends on log output to collect data, ask yourself this question: Are you sure your tests actually passed — or are you just assuming your reporting script didn't crash before showing the results?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/onurkesim/do-not-trust-the-green-checkmark-48i5

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
