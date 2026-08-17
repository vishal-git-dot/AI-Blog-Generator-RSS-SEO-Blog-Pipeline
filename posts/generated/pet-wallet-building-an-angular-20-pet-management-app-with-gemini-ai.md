---
title: "Pet-Wallet: Building an Angular 20 Pet Management App with Gemini AI"
slug: "pet-wallet-building-an-angular-20-pet-management-app-with-gemini-ai"
author: "Scott Thompson"
source: "devto_ai"
published: "Mon, 17 Aug 2026 01:23:31 +0000"
description: "This is a submission for Weekend Challenge: Dog Days Edition What I Built Pet-Wallet is a lightweight pet management application that allows users to add, ed..."
keywords: "pet, gemini, wallet, application, information, api, use, experiment"
generated: "2026-08-17T01:39:21.440548"
---

# Pet-Wallet: Building an Angular 20 Pet Management App with Gemini AI

## Overview

This is a submission for Weekend Challenge: Dog Days Edition What I Built Pet-Wallet is a lightweight pet management application that allows users to add, edit, and remove their pets. The application stores pet information such as name, breed, weight, and other personal details, while also allowing users to track daily care tasks and medications for each pet. I also integrated AI to help users collect pet information. The application can read a document containing pet data and use that information to assist with creating a new pet profile. This project was an opportunity for me to experiment with my recent development skills, participate in one of my first coding challenges, and now make my first post in the DEV.to Community. Demo 🐾 Try Pet-Wallet Live Code Griffonknox / Pet-Wallet Pet Wallet Pet Wallet is a pet care dashboard built with Angular that helps owners manage their pets, medication schedules, and daily care tasks in one place. Overview This application lets users: create and manage multiple pets edit pet profile details such as name, breed, age, weight, and avatar view a pet dashboard with summary stats add and complete care tasks for the day add and manage medications with active/inactive status store pet data locally in the browser optionally import pet details from a document using the Gemini API Features Pet selection screen with add, edit, and delete actions Pet dashboard with dynamic derived stats Care task tracking and completion workflow Medication management with status indicators Local persistence via browser storage Rounded, modern UI with a soft dark theme AI-powered document extraction for pet profile setup Tech Stack Angular 20 TypeScript SCSS RxJS Google Gemini API Getting Started Install dependencies: … View on GitHub How I Built It With the goal of keeping this experiment lightweight, Pet-Wallet is a front-end-only application built with Angular 20. I enjoy working with Angular because of its use of TypeScript, reusable components, and the ability to use a centralized Pet Service to manage our pet data and state. The application is deployed using GitHub Pages, with GitHub Actions handling the deployment process automatically whenever changes are pushed to the main branch. The final technology I wanted to experiment with was Google Gemini. I integrated Gemini to read PDF documents containing pet information and use that information to assist with creating a new pet profile. This is where things get a little more interesting. Because I wanted to keep Pet-Wallet as a lightweight, front-end-only experiment, the Gemini API request has to happen from the browser. That means I couldn't safely include my own API key in the application or public repository. Instead, I added a workflow where the user provides their own Gemini API key when they want to use the AI import feature. This isn't an architecture I would recommend for a production application(in a real application), I would move the Gemini request behind a backend service so the API key could remain server-side. But for this challenge, it allowed me to experiment with the Gemini API without exposing my own credentials. I'm definitely interested in hearing how others would approach this differently, so if you have suggestions for alternative solutions, I'd love to hear them in the comments! Prize Categories Best Use of Google AI Pet-Wallet uses Google Gemini to assist with creating new pet profiles. Users can provide a pet-information document, and Gemini reads the document and extracts relevant information that can then be used to populate the new pet form. I chose this feature as a way to experiment with Google AI while making the process of creating a new pet profile easier for the user.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/griffonknox/pet-wallet-building-an-angular-20-pet-management-app-with-gemini-ai-14j8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
