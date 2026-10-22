---
title: "SlothMode AI: Let Local AI Handle the Busywork"
slug: "slothmode-ai-let-local-ai-handle-the-busywork"
author: "Navya Pachigolla"
source: "devto_ai"
published: "Thu, 22 Oct 2026 16:45:29 +0000"
description: "This is my submission for the Hacktoberfest Open-Source AI Challenge Week 3: Slow and Steady. What I Built SlothMode AI is a local AI-powered file organizer ..."
keywords: "files, file, slothmode, local, project, open, more, model"
generated: "2026-10-22T16:56:20.011338"
---

# SlothMode AI: Let Local AI Handle the Busywork

## Overview

This is my submission for the Hacktoberfest Open-Source AI Challenge Week 3: Slow and Steady. What I Built SlothMode AI is a local AI-powered file organizer designed to make file management less tedious. We all have folders filled with randomly named documents, images, PDFs, and other files. Sorting them manually takes time and effort. SlothMode AI helps automate that busywork by scanning a folder, suggesting suitable categories, and organizing files with less manual effort. 🦥 The goal: Spend less time organizing files and more time doing things that matter. Key features: 🤖 AI-powered file categorization using a locally running model. 📂 Automatic file organization into relevant folders. 👀 Dry-run mode to preview proposed changes before applying them. ↩️ Undo functionality to reverse supported file moves. 📜 History tracking to review previous organization actions. 🛡️ Collision handling to avoid overwriting existing files. 🔌 Heuristic fallback when the local AI model is unavailable. Demo Project: SlothMode AI https://youtu.be/OiBlPZgK5l0 Code GitHub Repository: https://github.com/NavyaPachigolla/SlothMode-AI The project includes the Python source code, setup instructions, tests, and documentation. How I Built It I built SlothMode AI using Python, Ollama, Qwen2.5 3B, and Streamlit. The application uses a locally running language model to suggest file categories. Python handles folder scanning, organization plans, file operations, history, and undo functionality. Streamlit provides a web interface for interacting with the project. I also added safety features to make automation more trustworthy: Preview changes before applying them. Allow selective approval of proposed actions. Track file operations and support undo. Avoid overwriting files when name collisions occur. Fall back to heuristic categorization if the local model is unavailable. The project includes automated tests for important behaviors, including dry-run safety, collision handling, and undo operations. Why Does Open Innovation Matter? Open innovation made it possible to experiment with AI without depending entirely on a paid, closed API. Using an open-weight model through local inference gives users more control over where their files are processed. It can also reduce dependence on external services, avoid per-request API costs, and make experimentation more accessible. For a tool that works with personal files, local processing is especially useful because users can keep their documents on their own machines. This project showed me how open-source AI can turn a repetitive task into a more convenient, user-controlled workflow. My Agent Session I used Antigravity to help develop and test the project. If I publish a DevRelay session for this build, I will add the session link here. The Lazy Payoff 🦥 SlothMode AI aims to reduce the repetitive effort involved in manually sorting files. Instead of moving every file one by one, users can preview a proposed organization plan, approve the changes they want, and review or undo supported operations when necessary. The project includes a demo folder with sample files for testing the workflow. Prize Categories Add the applicable partner prize categories here after checking the challenge rules. Remove this section if you are not entering a partner category. Built with Python and local AI, for everyone who would rather spend less time sorting files. 🦥

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/navya_pachigolla_f45beee0/slothmode-ai-let-local-ai-handle-the-busywork-2kim

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
