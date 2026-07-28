---
title: "45-Second Production: Testing ChatGPT’s Limits with InterSystems IRIS and PyProd"
slug: "45-second-production-testing-chatgpts-limits-with-intersystems-iris-and-pyprod"
author: "InterSystems Developer"
source: "devto_python"
published: "Tue, 28 Jul 2026 19:12:16 +0000"
description: "It all started on a train ride to visit my parents, while I was chatting with a neighbor in my compartment. As it usually goes, the talk turned to technology..."
keywords: "step, python, pyprod, production, intersystems, chatgpt, https, com"
generated: "2026-07-28T19:39:37.247852"
---

# 45-Second Production: Testing ChatGPT’s Limits with InterSystems IRIS and PyProd

## Overview

It all started on a train ride to visit my parents, while I was chatting with a neighbor in my compartment. As it usually goes, the talk turned to technology, and she threw out a highly specific question: *Could ChatGPT be used to analyze the human genome?* I was highly skeptical that it could pull off something that complex. But the question lingered, burrowing into my mind. By the time I walked through my front door, my skepticism had transformed into a challenge. I didn't have a genome sequencing dataset on hand, but I did want to see if standard ChatGPT could build a functional Interoperability Production from scratch using the PyProd package . Besides, that would give me the chance to participate in the 1st round of the Community Bounty Program "Idea to Application" implementing the third idea . I decided to test it with a multi-step prompt: Using info from the following articles and github repository, write code for a complete InterSystems Production in Python using PyProd package: step 1: come up with the domain for this production step 2: create 4 csv files with 30 records in each in the step 1 domain step 3: write sql create table statement with the structure from csv file step 4: write inbound adapter in Python using PyProd package that reads the file step 5: write a business process in Python that analyzes the structure of the step 2 file and makes 1 calculation that makes sense in the step 1 domain step 6: write business operation in Python to save all the data read in 4 step and the result of calculation from 5 step to the table created in 3 step Here are the articles and github repositories you should use: https://community.intersystems.com/post/pyprod-pure-python-iris-interoperability https://community.intersystems.com/post/pyprod-creating-iris-interoperability-productions-programmatically-python https://community.intersystems.com/post/csvgen-pyprod https://github.com/intersystems/pyprod https://github.com/gabriel-ing/csvgen-pyprod I fed it all to ChatGPT and hit send. Then, I waited. For exactly 45 seconds. The Delivery and the "Gotchas" As a result, I got a smart_grid_pyprod.zip containing the ready-to-use code. Naturally, I was dying to know whether it actually worked or was just a convincing hallucination. Playing the part of a complete novice, I asked it how to set everything up. ChatGPT promptly walked me through all necessary steps. 1. Enabling interoperability in the `USER` namespace via the IRIS Terminal: zn "%SYS" do ##class(%EnsembleMgr).EnableNamespace("USER") 2. Configuring the environment variables for Windows 11 and installing the package: set IRISINSTALLDIR=C:\InterSystems\IRIS set IRISUSERNAME=SuperUser set IRISPASSWORD=SYS set IRISNAMESPACE=USER set PATH=%IRISINSTALLDIR%\mgr\python;%PATH% python -m pip install intersystems_pyprod --target %IRISINSTALLDIR%\mgr\python --upgrade 3. Compile the generated code using intersystems_pyprod smart_grid.py 4. Open the Management Portal, and start the production. Did it work right out of the box? Well, no. Mostly, the problems were about commas where they shouldn’t be and a couple of wrongly written async requests, among other things. It took me about half a day to iron out the creases (granted, I was watching Landman in parallel while waiting for Docker to build, turned out to be quite apropos - pumping oil and electricity 😉). But, thanks to some basic Python knowledge and a crucial reference example from @gabriel .Ing , I got it running. Anatomy of an AI-Generated Production Once the code was fixed, the production (mostly) written by ChatGPT functioned beautifully. It consists of three components: The business service SmartMeterFileService reads the input file The business process SmartMeterAnalysisProcess computes per-file total kWh, average kWh, peak meter id, and peak kWh The business operation SmartMeterDBOperation persists every CSV row with those calculation results ![ ](https://dev-to-uploads.s3.us-east-2.amazonaws.com/uploads/articles/jmn3lraxygfa1sz48m84.png) Looking at the Visual Trace in the Management Portal, you can see messages flowing seamlessly from the service to the process and finally to the operation: And when queried in SQL Explorer SELECT * FROM EnergyOps.SmartMeterReadings the data was there, properly calculated, and perfectly structured: The Verdict: Almost a Success I would call this experiment an almost success . Almost, because it required me to know at least something about how it works, so the complete novice would be stumped (or would need to ask a lot of follow-up questions). However, if you have a bit of foundational knowledge, a willingness to troubleshoot, and good community examples to lean on, you can make it work. It proves that while AI might not be ready to architect complex, enterprise-grade genome sequencing pipelines entirely on its own just yet, it is an incredible tool for taking an example and expanding on it to get a prototype off the ground.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/intersystems/45-second-production-testing-chatgpts-limits-with-intersystems-iris-and-pyprod-5a34

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
