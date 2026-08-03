---
title: "Building and Testing PickUp, a Vibe-Coded Platform for Casual Sports Games"
slug: "building-and-testing-pickup-a-vibe-coded-platform-for-casual-sports-games"
author: "Nuh"
source: "devto_webdev"
published: "Mon, 03 Aug 2026 19:27:54 +0000"
description: "Disclaimer: I am an intern at Perfai, however I built this app with a genuine purpose attempting to solve an issue that I face when it comes to sports. Now o..."
keywords: "sports, pickup, can, games, their, application, group, platform"
generated: "2026-08-03T19:44:41.768040"
---

# Building and Testing PickUp, a Vibe-Coded Platform for Casual Sports Games

## Overview

Disclaimer: I am an intern at Perfai, however I built this app with a genuine purpose attempting to solve an issue that I face when it comes to sports. Now obviously, being an intern at Perfai, I used the platform in order to test the security of my app. This is not intended to be an advertisement. Overview Over the weekend, I built PickUp, a web application designed to help people find and organize casual pickup sports games in their local area. Whether someone wants to join a game of basketball after work, find a weekend soccer match, or organize a group for pickleball, the goal of PickUp is to make connecting with other players quick and simple. I used this application as an opportunity to continue exploring how AI-assisted development tools can generate feature-rich full-stack applications while also creating realistic projects for future security testing. Problem As someone who loves staying active by playing sports, there are times where my main group isn’t always free to play pickup games, which is where this idea came from. Oftentimes, there are people who want a group to play basketball, soccer or any other sports with, but don’t know of the right group to get started, either because they are new to the community or even if they are looking for more people to play with. This is the group that PickUp is here to serve. The App Unlike traditional sports apps focusing on organized leagues or tournaments, PickUp is centered around casual community play. Users can browse an interactive map of nearby games, create their own pickup events, RSVP to games, and discover local sports groups based on their interests. Each session includes useful information such as the location, organizer, date and time, skill level, and number of available spots. Players can also create profiles showcasing their favorite sports, playing experience, and recent activity, making it easier to connect with others who enjoy similar activities. Now from a technical perspective, the application is built using Next.js, TypeScript, Tailwind CSS, Prisma, PostgreSQL, Auth.js, and Mapbox. It includes secure authentication with email/password and Google sign-in, role-based authorization, CRUD functionality, search and filtering, file uploads, REST API endpoints, and personalized dashboards for different user roles. Users can upload profile photos, join sports groups, receive notifications, and keep track of their upcoming games, while organizers have additional tools for managing events and communicating with participants. Moderators and administrators have dedicated dashboards for reviewing reports and managing community content. One feature I particularly enjoyed planning was the Sports Groups system. Rather than simply allowing users to create one-time events, groups give players a way to build recurring communities around their favorite sports. Members can organize weekly games, share announcements, chat with teammates, and invite new players into the group. This transforms the platform from an event finder into a social community where people can continue playing together over time. Takeaways Building PickUp has continued to reinforce how much AI can accelerate the early stages of application development. Starting from a detailed prompt, I was able to generate much of the application's overall structure, including authentication, routing, dashboards, and many of the core features that would otherwise require a significant amount of manual setup. Instead of focusing on boilerplate code, I was able to spend more time refining the product concept and thinking about the overall user experience. Security Testing As with my previous projects, the next step was to evaluate the application's security. PerfAI’s system picked up 9 critical issues in the code and 11 medium/low risk issues, none of which I would have picked up on had I not used their platform. PerfAI’s system estimated a total of $14.2k in bug bounty savings.This proved something to me. Vibe-coded applications look picture perfect from the outside, however on the backend there are a number of significant vulnerabilities which can lead to major issues in the future.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nuh_huss/building-and-testing-pickup-a-vibe-coded-platform-for-casual-sports-games-564d

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
