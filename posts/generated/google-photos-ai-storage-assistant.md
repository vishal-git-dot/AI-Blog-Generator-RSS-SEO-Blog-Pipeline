---
title: "Google Photos + AI Storage Assistant"
slug: "google-photos-ai-storage-assistant"
author: "Naila Akram"
source: "devto_ai"
published: "Sat, 17 Oct 2026 15:15:54 +0000"
description: "This is a submission for the Hacktoberfest Open-Source AI Challenge Week 2: Side Hustle What I Built You know that notification you get on your phone saying ..."
keywords: "photos, storage, assistant, you, photo, like, model, open"
generated: "2026-10-17T15:18:37.849356"
---

# Google Photos + AI Storage Assistant

## Overview

This is a submission for the Hacktoberfest Open-Source AI Challenge Week 2: Side Hustle What I Built You know that notification you get on your phone saying your storage is almost full? I get it every few days, and honestly, it's annoying. Whenever I see it, I open my gallery and start looking for photos I can delete. But then I find so many similar pictures, random screenshots, and photos I don't even remember saving. Sometimes I want to delete a photo, but I stop because I'm not sure if I'll need it later. And the worst part is figuring out which photos are duplicates. Going through hundreds of pictures one by one just to free up some space feels like too much work. That's where I got the idea for Google Photos + AI Storage Assistant . I wanted to build something that could make managing photos easier. The idea is to have a photo gallery where I can browse my pictures, organize them into albums, save my favorites, and eventually get help from AI when I need to clean up my storage. So far, I've built a Google Photos-inspired interface with a photo gallery, categories, favorites, an album suggestion interface, and an AI assistant. Here's what it currently has: A gallery to browse photos. Categories like Travel, Nature, and Screenshots. A favorites feature for important photos. A suggested album interface where users can select photos. An AI chat assistant that runs using a local AI model. A storage management section that I'm working to improve. It's still a prototype, and I know there's a lot more I want to add. Duplicate detection is one of the features I'd really like to build next because it would solve the exact problem that inspired this project. My idea is simple: I want cleaning up a photo gallery to take less time and feel less stressful. Demo 🎥 Demo video: https://youtu.be/8dFOMaO5un4 Code 💻 GitHub: Repository Link - https://github.com/nailaAkr/ai-storage-manager How I Built It I used HTML, CSS, and JavaScript to build the frontend, and Node.js with Express for the backend. For the AI assistant, I used Ollama with the Llama 3.2 (1B) model . I wanted to try using an open-source model locally instead of relying on a paid AI API. Getting everything connected wasn't completely straightforward. I had to work through some issues with the backend and the AI model before I could get responses in my application. This project gave me a chance to learn by actually building something instead of just following tutorials. I also got to understand how a local AI model can be connected to a web application. Why Does Open Innovation Matter? I'm still learning, and I want to be able to experiment with AI without worrying about API costs every time I try something new. Using Ollama made that possible for this project. I could run the model on my own computer and experiment with integrating it into my application. I also like the idea of using open-source tools because they give developers the freedom to learn, experiment, and improve their projects. I'd like to explore more privacy-friendly features as I continue working on this, especially since photos can contain personal memories. What's Next? There are a few things I'd love to add: A way to find duplicate and similar photos. Suggestions for photos that users might want to review or delete. Search that lets users describe the photo they're looking for. Better album suggestions. More control over how personal photo data is handled. I know these features will take more work, but they're the direction I'd like to take the project in. My First User Right now, I'm building this around a problem I face myself, so I'd love to know if other people struggle with the same thing. Do you also get storage-full notifications all the time? How do you decide which photos to delete? And would you use an assistant that helps you find duplicates instead of checking everything manually? I'd love to hear your thoughts! Thanks for checking out my project. ❤️

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nailaakram418/google-photos-ai-storage-assistant-jpm

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
