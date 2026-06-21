---
title: "Windows + WSL + Next.js Development Setup: Zero to Professional Environment"
slug: "windows-wsl-nextjs-development-setup-zero-to-professional-environment"
author: "Anik Deb Nath"
source: "devto_webdev"
published: "Sun, 21 Jun 2026 19:50:33 +0000"
description: "আজ আমি আমার Windows মেশিনে একটা স্মুথ ও মডার্ন ওয়েব ডেভেলপমেন্ট সেটআপ তৈরি করেছি ব্যবহার করেছি Windows Subsystem for Linux (WSL) , Node.js , pnpm আর Next.js..."
keywords: "wsl, pnpm, windows, step, linux, node, nvm, code"
generated: "2026-06-21T19:51:26.683240"
---

# Windows + WSL + Next.js Development Setup: Zero to Professional Environment

## Overview

আজ আমি আমার Windows মেশিনে একটা স্মুথ ও মডার্ন ওয়েব ডেভেলপমেন্ট সেটআপ তৈরি করেছি ব্যবহার করেছি Windows Subsystem for Linux (WSL) , Node.js , pnpm আর Next.js । পুরো প্রসেসটা খুবই সহজ এবং প্র্যাকটিক্যাল। যারা Windows এ থেকেও Linux-এর পাওয়ার চান, তাদের জন্য এই গাইডটা অনেক কাজে লাগবে। চলো ধাপে ধাপে দেখি। Step 1: WSL ইনস্টল করা প্রথমেই Windows-এ WSL চালু করলাম। কমান্ড: wsl --install এরপর PowerShell অ্যাডমিন মোডে চালিয়ে Ubuntu ইনস্টল করলাম। WSL ইনস্টল হওয়ার পর Windows এর ভিতরেই একটা পূর্ণাঙ্গ Linux এনভায়রনমেন্ট পেয়ে গেলাম। এখন আমি Linux কমান্ড, টার্মিনাল এবং ডেভেলপমেন্ট টুলস সব স্বাভাবিকভাবে ব্যবহার করতে পারছি। Step 2: Ubuntu সেটআপ WSL ওপেন করে প্রথমে কয়েকটা বেসিক জিনিস সেট করলাম: হোম ডিরেক্টরি চেক করা ( /home/username ) projects ফোল্ডার তৈরি করা সিস্টেম আপডেট করা ( sudo apt update && sudo apt upgrade ) এখানে বুঝলাম, WSL আসলে আলাদা কোনো VM না — এটা Windows এর সাথে খুব ভালোভাবে ইন্টিগ্রেটেড। ফাইল অ্যাক্সেসও দ্রুত। Step 3: Node.js ইনস্টল (nvm দিয়ে) Node.js ইনস্টল করার জন্য nvm (Node Version Manager) ব্যবহার করলাম। এতে যেকোনো সময় ভার্সন চেঞ্জ করা সহজ। curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash nvm install --lts nvm use --lts node -v এবং npm -v চেক করে নিলাম। Step 4: pnpm সেটআপ npm এর বদলে pnpm ব্যবহার করছি কারণ: অনেক দ্রুত প্যাকেজ ইনস্টল হয় ডিস্ক স্পেস অনেক কম লাগে ডিপেন্ডেন্সি ম্যানেজমেন্ট অনেক ভালো Corepack দিয়ে সেট করলাম (Node.js এর সাথেই আসে): corepack enable pnpm pnpm --version Step 5: Next.js প্রজেক্ট তৈরি pnpm create next-app@latest my-project --typescript --tailwind --eslint --app cd my-project pnpm install Step 6: pnpm Build Issue ফিক্স ইনস্টলের সময় একটা সমস্যা হয়েছিল: [ ERR_PNPM_IGNORED_BUILDS] সমাধান: pnpm approve-builds এরপর আবার pnpm install চালালাম। সবকিছু ঠিক হয়ে গেল। Step 7: VS Code + WSL Integration VS Code ইনস্টল করে WSL এক্সটেনশন যোগ করলাম। প্রজেক্ট ফোল্ডারে গিয়ে সিম্পলি টাইপ করলাম: code . অবাক করা ব্যাপার! VS Code Windows এ খুলল, কিন্তু সবকিছু WSL এর Linux এনভায়রনমেন্টে চলতে লাগল। VS Code Server অটোমেটিক্যালি ইনস্টল হয়ে গেল। এটাই সবচেয়ে শক্তিশালী অংশ। Step 8: WSL বন্ধ করা (পরিষ্কার রাখতে) কাজ শেষে র‍্যাম ফ্রি করতে: wsl --shutdown শেষ কথা এই সেটআপের মাধ্যমে আমি এখন Windows এ বসেও প্রায় পুরোপুরি Linux-এর মতো ডেভেলপমেন্ট এক্সপেরিয়েন্স পাচ্ছি। WSL + pnpm + Next.js + VS Code — এই কম্বিনেশনটা সত্যিই শক্তিশালী। সুবিধাগুলো: দ্রুত পারফরম্যান্স আসল Linux টুলস ও কমান্ড সহজ ডিপেন্ডেন্সি ম্যানেজমেন্ট প্রফেশনাল ওয়ার্কফ্লো যারা এখনো WSL ট্রাই করেননি, অবশ্যই চেষ্টা করে দেখবেন। কোনো সমস্যা হলে কমেন্টে জানাবেন — সাহায্য করব। Happy Coding! 🚀

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/anikdebnath/windows-wsl-nextjs-development-setup-zero-to-professional-environment-cl1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
