---
title: "Psychopath: An All-in-One Threat Emulation & Social Engineering Framework"
slug: "psychopath-an-all-in-one-threat-emulation-social-engineering-framework"
author: "Chadi"
source: "devto_python"
published: "Wed, 18 Nov 2026 23:16:25 +0000"
description: "In the ever-evolving landscape of cybersecurity, red teams and security researchers constantly seek advanced tools to simulate realistic threat scenarios. Tr..."
keywords: "psychopath, security, social, engineering, framework, osint, phishing, testing"
generated: "2026-11-19T00:06:06.932026"
---

# Psychopath: An All-in-One Threat Emulation & Social Engineering Framework

## Overview

In the ever-evolving landscape of cybersecurity, red teams and security researchers constantly seek advanced tools to simulate realistic threat scenarios. Traditional penetration testing often compartmentalizes reconnaissance, OSINT, spear-phishing, and credential harvesting into disparate tools. Enter Psychopath ( chadi0x/Psychopath ) — an open-source, all-in-one threat emulation and social-engineering framework designed to streamline and centralize authorized security assessments. Whether you're conducting an adversary simulation, performing comprehensive OSINT reconnaissance, or testing organizational resilience against social engineering, Psychopath provides a powerful unified suite. 🔍 What Makes Psychopath Different? Developed by security researcher chadi0x , Psychopath moves away from fragmented toolchains. Built primarily using Python (Flask, SQLAlchemy, Selenium) paired with a responsive HTML/CSS/JavaScript interface and full Docker support, it offers a modular, web-driven console where every phase of a social-engineering campaign can be managed from a single dashboard. Let's take a deep dive into the core modules that power the framework. 🧰 Key Features & Tool Directory 1. Target Database & Dossier Vault At the heart of any sophisticated engagement is profiling. Psychopath provides a centralized database for storing target details, communication histories, contact points, origin data, IP addresses, and an encrypted credential vault to securely manage captured assets. 2. Elite Connections Mind Map Visualizing attack surfaces and relationships between targets, associated infrastructure, and organizational hierarchies is crucial. Psychopath includes a Vis.js-powered interactive mind-mapping tool with persistent layout storage, allowing operators to graphically chart asset links in real time. 3. Intelligence Hub (OSINT Engine) Reconnaissance is automated via an integrated OSINT engine featuring: A built-in automated Google Dork generator A headless Chromium/Selenium-driven image scraper This automates candidate and infrastructure footprinting before a single lure is cast. 4. Real-Time IP & Geolocation Tracker Operators can generate specialized lure links that discreetly log visitor metadata — including IP addresses, user agents, device fingerprints, ISPs, and precise geographic coordinates leveraging IP-API integration. 5. Evil Package Factory To simulate multi-platform dropper scenarios, the Evil Package Factory generates bespoke lures and payloads tailored for Windows, Linux, and Android environments — ranging from simulated trading platforms and captive portals to security verification popups. 6. Email Factory & SMTP Knife Crafting compelling pretexts is made simple with the Email Factory, which supports dynamic variable tagging (such as {name} , {company} , and {link} ) alongside live HTML previewing. Paired with the SMTP Knife , operators can execute direct SMTP relay delivery with TLS/SSL testing, custom headers, and spoofed display names. 7. Flash Phishing Engine The framework features over 30 turnkey cloned enterprise login portals (covering major services like Google, Microsoft 365, Facebook, and GitHub). Key highlights include: Multi-Language Support — English, French, and Arabic RTL pretexts Cloudflare Tunnel Integration — Automated generation of secure public tunnels ( trycloudflare.com ) out of the box Global Kill Switch — An emergency safety control to instantly shut down active phishing instances 8. Psychopath AI Assistant Integrating local LLM capabilities (via Ollama running on port 11434 with models like Mistral or Llama), the built-in AI assistant helps operators: Brainstorm realistic pretexts Draft compelling phishing copy Design tailored social-engineering scenarios 🚀 Quick Start Deployment Deploying Psychopath can be accomplished in minutes via Docker or a manual local setup. Method 1: Docker Compose (Recommended) git clone https://github.com/chadi0x/psychopath.git cd psychopath chmod +x run.sh ./run.sh ⚠️ Important Legal & Ethical Disclaimer Strict Legal Notice Psychopath is an advanced security testing framework built strictly for authorized security assessments, academic research, and defensive posture hardening. Deploying these modules against targets, networks, or individuals without explicit, documented prior written consent is strictly illegal under international cybersecurity laws. Always ensure you have a formal Rules of Engagement (RoE) document signed before conducting any simulated engagements. 🎯 Conclusion Psychopath represents a significant leap forward in consolidating red-teaming toolsets into an accessible, web-based platform. By combining robust OSINT mapping, advanced phishing mechanics, and local AI assistance, it equips security professionals with the comprehensive visibility needed to test and harden modern defense perimeters effectively. Have you tested Psychopath in your home lab or red-team engagements? Drop your thoughts and setup tips in the comments below. 👇

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/chadi0x/psychopath-an-all-in-one-threat-emulation-social-engineering-framework-489m

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
