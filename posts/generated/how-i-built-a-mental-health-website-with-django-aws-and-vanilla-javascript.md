---
title: "How I Built a Mental Health Website with Django, AWS and Vanilla JavaScript"
slug: "how-i-built-a-mental-health-website-with-django-aws-and-vanilla-javascript"
author: "Asier Larruscain"
source: "devto_python"
published: "Wed, 02 Sep 2026 15:54:47 +0000"
description: "I'm a psychologist, not a software engineer. A few years ago, if I wanted to change something on my website, automate a process, or build a new feature, I wo..."
keywords: "website, django, project, you, aws, javascript, build, has"
generated: "2026-09-02T16:20:36.990317"
---

# How I Built a Mental Health Website with Django, AWS and Vanilla JavaScript

## Overview

I'm a psychologist, not a software engineer. A few years ago, if I wanted to change something on my website, automate a process, or build a new feature, I would have needed to ask a developer. I decided to take a different approach: learn enough web development to build and maintain the project myself. The result is Supera tu Ansiedad , a Spanish mental health website focused on anxiety, where I publish evidence-based educational content, practical resources and offer access to online psychological therapy. Today, the website runs on a stack built around Python, Django, AWS, HTML, CSS and vanilla JavaScript . This is what I learned building it. Why Django? My first major decision was choosing the backend. I wanted something that: could grow with the website had a mature ecosystem handled content dynamically allowed me to automate repetitive tasks didn't force me to reinvent basic web functionality Django ended up being a great fit. One of the things I appreciate most about Django is how much functionality is already structured for you. Instead of assembling many independent tools, I could progressively learn how models, views, templates, URLs and other parts of the application worked together. For someone coming from psychology rather than computer science, that structure helped enormously. Keeping the frontend simple For the frontend I decided not to use React, Vue or another JavaScript framework. The website mainly uses: HTML CSS vanilla JavaScript Django templates For this particular project, that has been enough. Most pages are content-heavy psychology resources, so I don't need a large client-side application. JavaScript is added when interaction is actually useful rather than being the foundation of the website. This keeps the architecture relatively simple and gives me direct control over what is happening in the browser. It has also taught me an important lesson: You don't necessarily need a JavaScript framework to build a useful production website. The right stack depends on the problem you're trying to solve. Going serverless with AWS and Zappa The application is deployed using AWS and Zappa. Zappa makes it possible to run Django using AWS Lambda, which was an interesting architecture for a relatively small independent project. My infrastructure also uses AWS services for things such as static files, distribution and automation. This was probably the steepest part of the learning curve. Building something locally is one thing. Understanding deployments, cloud infrastructure, permissions, caching and production errors is another. But learning those pieces gradually gave me much more control over the project. Python beyond the website itself One of the biggest advantages of choosing Python is that I can use it for much more than Django. As the website grew, I started creating small automations around it. For example, I use automation to help with: website maintenance SEO analysis detecting potential problems processing data repetitive administrative tasks This is where programming became particularly valuable to me. Instead of only asking: "How do I build this page?" I started asking: "Why am I doing this manually every week?" If something follows predictable rules, there is often an opportunity to automate at least part of it. Building software as a non-developer The most interesting part of this project has probably been learning software development without trying to become a software engineer. My goal is still psychology. Programming is a tool that allows me to build things around my professional work. That changes the way I approach development. I don't need to know everything about Python, JavaScript or AWS. I need to understand them well enough to solve the problems my project actually has. That project-based approach has worked extremely well for me. Every real problem gives me a reason to learn the next concept. What I would recommend to other non-developers If you're learning programming from another profession, my biggest recommendation would be: Build something you genuinely need. Don't wait until you feel like you know enough. Start with a small real project and allow the problems you encounter to determine what you learn next. My own progression has essentially been: HTML/CSS → JavaScript → Python → Django → AWS → automation And I'm still learning. What started as simply wanting more control over my psychology website has gradually turned into the ability to build, deploy and maintain my own web project. For me, that's one of the most powerful things about learning to code.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/asier_larruscain_509eef99/how-i-built-a-mental-health-website-with-django-aws-and-vanilla-javascript-4m6e

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
