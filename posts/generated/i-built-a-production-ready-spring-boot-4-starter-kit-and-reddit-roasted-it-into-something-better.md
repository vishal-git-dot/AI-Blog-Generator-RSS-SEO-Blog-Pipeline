---
title: "I built a production-ready Spring Boot 4 Starter Kit (and Reddit roasted it into something better)"
slug: "i-built-a-production-ready-spring-boot-4-starter-kit-and-reddit-roasted-it-into-something-better"
author: "Rahul Kushwaha"
source: "devto_webdev"
published: "Sat, 27 Jun 2026 03:33:12 +0000"
description: "Why I built this Every new Spring Boot project starts the same way. JWT setup. Security config. CORS. Rate limiting. Docker. CI/CD. Exception handling. I was..."
keywords: "jwt, spring, boot, every, docker, token, http, cookie"
generated: "2026-06-27T03:58:09.835808"
---

# I built a production-ready Spring Boot 4 Starter Kit (and Reddit roasted it into something better)

## Overview

Why I built this Every new Spring Boot project starts the same way. JWT setup. Security config. CORS. Rate limiting. Docker. CI/CD. Exception handling. I was copy-pasting the same boilerplate across projects, so I decided to build it once, do it properly, and open source it. What's inside 🔐 JWT Auth — access token (15 min) + refresh token (7 days) with rotation 👮 Role-based access — ROLE_USER, ROLE_ADMIN via @PreAuthorize 🚦 Rate limiting — per IP using Bucket4j 📄 Swagger UI — auto-generated at /swagger-ui.html 🛡️ Global exception handling — consistent ApiResponse on every endpoint 🗃️ Flyway migrations — version-controlled schema 🐳 Docker + Nginx + MySQL — one command deploy ⚙️ GitHub Actions CI/CD — test → build → EC2 deploy 🍪 HTTP-only cookie support — XSS protection Java 21 + Spring Boot 4 Reddit made it better I posted on r/SpringBoot and r/java. The feedback was brutal. And valuable. Criticism 1: "Why are you making a DB call on every request? That defeats the purpose of JWT." They were right. My JWT filter was loading the user from DB on every request to get roles. Completely stateless JWT was the whole point. Fix: Embedded roles directly into JWT claims at login time. Filter now extracts roles from token — zero DB calls per request. Criticism 2: "Why not store tokens in HTTP-only cookies? Bearer headers are XSS vulnerable in browsers." Also valid. Added HTTP-only cookie support. Both Bearer header and cookie work simultaneously — browser apps use cookie, mobile/API clients use header. Criticism 3: "Spring Security already handles this with AbstractAuthenticationProcessingFilter. You don't need a custom JWT filter." This one was more nuanced. They suggested Spring Session + JDBC instead of JWT entirely. So I added both approaches: main branch → JWT (stateless, mobile-friendly) feature/spring-session → Spring Session JDBC (simpler, instant revocation, survives restarts) Devs can pick what fits their use case. How to use it git clone https://github.com/raahulllkushwaha/springboot-starter-kit cd springboot-starter-kit # runs on H2 in-memory — zero setup mvn spring-boot:run Open http://localhost:8080/swagger-ui.html Register → Login → copy token → hit protected endpoints. For production: cp .env.example .env # fill your secrets docker compose up -d Rename for your project Find & replace com.starterkit → com.yourcompany.app Then add your entities on top. Auth, Docker, CI/CD already done. What I learned Open source feedback > any code review README quality matters more than code quality for adoption JWT stateless = NO DB calls in filter. Period. Spring Security's built-in flow exists for a reason GitHub: If this saves you time, a ⭐ means a lot.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/raahulllkushwaha/i-built-a-production-ready-spring-boot-4-starter-kit-and-reddit-roasted-it-into-something-better-4co4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
