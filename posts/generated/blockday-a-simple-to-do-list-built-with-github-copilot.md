---
title: "Blockday - A Simple To-Do List Built with GitHub Copilot"
slug: "blockday-a-simple-to-do-list-built-with-github-copilot"
author: "Pankaj Maity"
source: "devto_webdev"
published: "Fri, 16 Oct 2026 03:36:59 +0000"
description: "Blockday - A Simple To-Do List Built with GitHub Copilot I built Blockday , a responsive To-Do List application with a block-style, Minecraft-inspired design..."
keywords: "tasks, github, copilot, application, browser, due, task, reminders"
generated: "2026-10-16T04:00:24.052860"
---

# Blockday - A Simple To-Do List Built with GitHub Copilot

## Overview

Blockday - A Simple To-Do List Built with GitHub Copilot I built Blockday , a responsive To-Do List application with a block-style, Minecraft-inspired design. The idea was simple: create a lightweight task manager that makes everyday task planning a little more engaging while keeping the interface clean and easy to use. Features Add tasks with Normal, High, or Low priority Assign a due date to tasks Automatically identify overdue tasks Optional reminders for tasks due today Browser notifications when permission is granted In-app reminders when browser notifications are unavailable Mark tasks as completed Search tasks by title Filter tasks by All, Active, or Done Delete tasks Track completion progress Daily streak and best streak tracking Automatically save tasks using browser localStorage Responsive design for desktop and mobile Works without a backend or database Technologies Used HTML CSS Vanilla JavaScript Browser localStorage Browser Notifications API GitHub Codespaces GitHub Copilot Render No React, Node.js, database, or external backend is required. Built with GitHub Copilot One of the main reasons I built this project was to explore how GitHub Copilot can assist throughout the development process . I used GitHub Copilot inside GitHub Codespaces to help build and improve the application, including: Structuring the application Implementing task management functionality Adding due dates Implementing reminders Fixing UI layout issues Improving responsive behavior Creating project documentation The process wasn't simply about asking Copilot to build an application. I provided requirements, reviewed the generated code, tested the application, identified issues, and then used specific prompts to improve the implementation. Due Dates and Reminders Users can assign a due date when creating a task or add/change it later. Tasks are organized into: Overdue Due Today Upcoming No Due Date Completed The application also provides optional reminders for incomplete tasks that are due today. When reminders are enabled, the application can use browser notifications if permission is granted. If notifications are unavailable or blocked, an in-app reminder is used instead. The current implementation checks reminders while the application is open, so it does not guarantee notifications when the website is completely closed. Data Storage Tasks are stored locally in the browser using localStorage . This means: Tasks remain after refreshing the page. Tasks normally remain after restarting the browser. Tasks are not uploaded to a server. Tasks are not synchronized between different devices or browsers. Live Demo Try it yourself: https://blockday-todo.onrender.com/ Create your own tasks and explore the different features. GitHub Repository https://github.com/pnkj006/ToDoList-Using_Copilot What I Learned This project helped me understand how AI coding tools can fit into a real development workflow. The important part wasn't simply generating code with Copilot. I had to: Define the requirements clearly. Review the generated code. Test the application. Identify UI and functionality issues. Give Copilot specific prompts to fix them. Document the project. Deploy the final version. It was a useful hands-on experience with AI-assisted development, GitHub Codespaces, Git, browser APIs, and deployment . What's Next? Some improvements I would like to explore in the future: User authentication Cloud-based task synchronization Database storage More advanced reminder scheduling Reliable background push notifications Task categories and tags Drag-and-drop task organization For now, Blockday is a simple and lightweight project that helps you plan your day, one block at a time. GitHub #GitHubCopilot #Codespaces #JavaScript #WebDevelopment #HTML #CSS #OpenSource

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/pnkj_mty_4ec833d844e216ec/blockday-a-simple-to-do-list-built-with-github-copilot-4i61

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
