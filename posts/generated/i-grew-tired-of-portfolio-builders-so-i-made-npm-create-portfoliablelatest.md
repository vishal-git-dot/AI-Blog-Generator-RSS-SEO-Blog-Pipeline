---
title: "I grew tired of portfolio-builders, so I made `npm create portfoliable@latest`"
slug: "i-grew-tired-of-portfolio-builders-so-i-made-npm-create-portfoliablelatest"
author: "Lio Schimanko Bittencourt"
source: "devto_webdev"
published: "Sat, 07 Nov 2026 21:23:26 +0000"
description: "I started my career as a designer, and very early on, I learned how important it was to have a portfolio. When I decided to transition from Product and User ..."
keywords: "you, case, can, portfolio, study, your, video, npm"
generated: "2026-11-07T21:39:06.287281"
---

# I grew tired of portfolio-builders, so I made `npm create portfoliable@latest`

## Overview

I started my career as a designer, and very early on, I learned how important it was to have a portfolio. When I decided to transition from Product and User Experience Design to Software Engineering, I soon realized that a portfolio is important in practically every career path. After being invited to interview with companies like John Deere and Nubank, I decided to share a formula that was working for me. With this in mind, I decoupled my personal portfolio and created Portfoliable.js , an open-source CLI portfolio builder for creatives around the world. It received more than 6,000 npm downloads in the past three months. Here’s what I’ve learned so far. If you’re in a hurry: When you run npm create portfoliable@latest , you get an industry-class portfolio to showcase your work, built in JavaScript as a SPA (single-page application). All case studies and the About page are written in Markdown, with support for the full syntax. You can add optional video presentations in a high-resolution, mockup-ready player. You can add or remove multiple languages via CLI commands. They’re served at runtime, with support for rtl . You can self-host anywhere, with full accessibility features for the web app, including Dark Mode, Forced Colors, High Contrast, Text Increase/Decrease, and more. All content is agent-ready and served in Markdown. Custom design and label edits are possible via tokens. Recruiters have little time It’s difficult to grab a recruiter’s attention, so a portfolio has to be fast, easy to look at, and easy to navigate. That’s why the first page—or, in this case, View —is so important. I tried many iterations of HomeView . Although every portfolio is different and reflects a candidate’s identity, there’s a golden rule for the home page: it needs to show what you’ve built in the real world. As you can see in the screenshot above, HomeView is composed of a gallery that showcases what the candidate has built, as is, with a title, description, and pills indicating whether the case study includes a repository link, a website link, or a video presentation. I call these “Case Decorators.” Except for the title and description—which are important for SEO/GEO—they’re all optional. Their labels can be customized via i18n.labels.js . Choosing the right presentation You also have the option to change the mockup to match the device on which your product was tested or released. When you run npm run portfoliable-thumbnail-options -- --full , you generate thumbnail-options.generated.json , a comprehensive catalog of thumbnails to choose from. They’re grouped by thumbBrand → thumbCategory → thumbModel → thumbColor . Brands include mockups from Apple, Dell, Google, Xiaomi, and others. Within each brand, you can choose a category such as tablet , desktop , mobile , or wearable . When you click on a case study, the recruiter is taken to CaseView , where they can take a closer look at your work. Showing off your work You can customize any case study with several Case Decorators, all of which are optional and independent of one another: A button that takes you to a video presentation inside the app, in PlayerView . Links to repositories or websites. A quick summary of the case study, with summaryProps to highlight real-world impact. An audio player, if you want to record the case study for accessibility. It includes an on/off auto-scroller button. Options to hide a specific case study from crawlers and/or AI agents. The option to password-protect a case study via PHP. A language separator, if your portfolio has more than one language. A fully customizable case study article, written in Markdown with support for its syntax. All of this goes in one Markdown file, so it’s very easy to manage multiple case studies. And, as you might have noticed, it’s very Git-friendly. Video presentations If your case study has a video presentation, you can add it by linking to it in the Case Decorators section of the Markdown file I mentioned earlier. PlayerView uses the mockup device you previously selected, detects the alpha channel in the image, and fits the video into the device screen to create a realistic presentation. The player supports a fully functional drag-to-seek bar, a pause/resume button, and playback speed controls. Support for closed captions is underway. If your portfolio is multilingual, you can add a video for each language. Tell them about yourself There’s also AboutView , which is essentially a copy of CaseView , but reserved for personal presentations. Responsive support Every view is responsive-ready. Free and open-source This project is open-source under the MIT License, which means you can contribute to it. It is not finished! I built it with a lot of love for everyone looking for a job, and I hope it helps you too. ☺️ You can take a look at Portfoliable’s repository and its NPM package .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/schimanko/i-grew-tired-of-portfolio-builders-so-i-made-npm-create-portfoliablelatest-1pfk

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
