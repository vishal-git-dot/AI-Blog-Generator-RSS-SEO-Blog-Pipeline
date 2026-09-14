---
title: "Selenium Architecture & Setup"
slug: "selenium-architecture-setup"
author: "Madhesh"
source: "devto_python"
published: "Mon, 14 Sep 2026 11:59:56 +0000"
description: "Inside Selenium: Understanding its Architecture and the Importance of Virtual Environments in Python There was a time when I had been using Selenium without ..."
keywords: "selenium, python, browser, one, install, driver, project, architecture"
generated: "2026-09-14T12:21:57.412703"
---

# Selenium Architecture & Setup

## Overview

Inside Selenium: Understanding its Architecture and the Importance of Virtual Environments in Python There was a time when I had been using Selenium without understanding at all how Python lines would result in movement of the actual Chrome window. Once the trainer explained the architecture to us, a lot of the peculiar errors which I kept facing became clear to me. This is what I understood along with another lesson that took me an entire afternoon to learn. Selenium architecture, level by level WebDriver is a Selenium module consisting of four components that act in sequence. The client library is the module I install via pip. This is the language binding provided for Python, Java, C#, JavaScript, and Ruby. When I call driver.find_element(By.ID, "user") , the language binding does not interact with the browser in any way. It converts my method call into a regular HTTP request, consisting of URL and JSON payload. This is what the protocol transports. Here lies the difference between Selenium 3 and Selenium 4. Selenium 3 uses the JSON Wire Protocol, which means that the request needs to be translated from the client side and then decoded by the driver because each browser speaks its own dialect. Selenium 4 supports the W3C WebDriver standard, implemented natively by all major browser vendors. There is no longer a need for any kind of translation layer, and this is one of the reasons why Selenium 4 tests are more robust. The browser driver is the executable like ChromeDriver, GeckoDriver, or EdgeDriver. Not only is this something we install and ignore. Every driver has its own little HTTP server listening on a local port, receiving my request and translating it into commands for the browser engine. This is also the reason why I cannot use Chrome 130 and ChromeDriver from long ago. The driver speaks only to one browser version. The browser executes the action and the result gets translated back through HTTP just like in any other case, to become a Python object like WebElement or boolean. Selenium Grid extends the same idea to other machines. Selenium 4 splits the Grid into a router, a distributor, a session map and nodes, making it possible for my laptop to control a Firefox session in a totally different machine with the exact same code. The importance of virtual environments My very first error in Python was to install all packages globally. For example, the first project required an older version of Selenium, and the second one requires the most recent, but just one command pip install silently destroyed the first project. Virtual environments help avoid such problems since they create an isolated folder with an isolated Python interpreter and site-packages . None of the installed packages will leak out. For instance, my practice project works with Selenium 4.21 and pytest 8, and an older course project requires Selenium 3.141, since it uses find_element_by_id . Two different environments, two folders, no conflicts. Another example would be reporting. One project needs pytest-html, and another one needs Allure. The process is simple: python -m venv venv , activate it, pip install selenium pytest , and finally pip freeze > requirements.txt . With that file, a colleague or a CI pipeline can recreate the environment with just one command. This is how test results become reproducible, instead of saying “it works on my machine”. Getting an insight into both concepts influenced my debugging approach because I understood at which level the failure occurred and that my dependencies were not to blame.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/madhesh_321950d350b0ecec7/selenium-architecture-setup-6m4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
