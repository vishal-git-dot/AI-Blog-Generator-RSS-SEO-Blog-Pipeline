---
title: "Setting up a React Environment"
slug: "setting-up-a-react-environment"
author: "vidhya murali"
source: "devto_webdev"
published: "Tue, 14 Jul 2026 08:04:43 +0000"
description: "To use React in production, you need npm which is included with Node.js. Also, you need to set up a React Environment, and choose a build tool. First, make s..."
keywords: "svg, classname, vite, use, div, app, icon, href"
generated: "2026-07-14T08:17:51.110180"
---

# Setting up a React Environment

## Overview

To use React in production, you need npm which is included with Node.js. Also, you need to set up a React Environment, and choose a build tool. First, make sure you have Node.js installed. You can check by running this in your terminal: node -v Install a Build Tool (Vite) When you have Node.js installed, you can start creating a React application by choosing a build tool. We will use the Vite build tool npm install -g create-vite npm create vite@latest my-react-app -- --template react Need to install the following packages: create-vite@9.0.7 Ok to proceed? (y) or npm create vite@latest A new browser window will pop up with your newly created React App! If not, open your browser and type localhost:5173 in the address bar. Now that your development environment is set up, let's try to modify the default app to display "Hello, World!" * Example * : This is the default content of the App.jsx file in the src folder: import { useState } from ' react ' import reactLogo from ' ./assets/react.svg ' import viteLogo from ' ./assets/vite.svg ' import heroImg from ' ./assets/hero.png ' import ' ./App.css ' function App () { const [ count , setCount ] = useState ( 0 ) return ( <> < section id = "center" > < div className = "hero" > < img src = { heroImg } className = "base" width = "170" height = "179" alt = "" /> < img src = { reactLogo } className = "framework" alt = "React logo" /> < img src = { viteLogo } className = "vite" alt = "Vite logo" /> </ div > < div > < h1 > Get started </ h1 > < p > Edit < code > src/App.jsx </ code > and save to test < code > HMR </ code > </ p > </ div > < button type = "button" className = "counter" onClick = { () => setCount (( count ) => count + 1 ) } > Count is { count } </ button > </ section > < div className = "ticks" ></ div > < section id = "next-steps" > < div id = "docs" > < svg className = "icon" role = "presentation" aria-hidden = "true" > < use href = "/icons.svg#documentation-icon" ></ use > </ svg > < h2 > Documentation </ h2 > < p > Your questions, answered </ p > < ul > < li > < a href = "https://vite.dev/" target = "_blank" > < img className = "logo" src = { viteLogo } alt = "" /> Explore Vite </ a > </ li > < li > < a href = "https://react.dev/" target = "_blank" > < img className = "button-icon" src = { reactLogo } alt = "" /> Learn more </ a > </ li > </ ul > </ div > < div id = "social" > < svg className = "icon" role = "presentation" aria-hidden = "true" > < use href = "/icons.svg#social-icon" ></ use > </ svg > < h2 > Connect with us </ h2 > < p > Join the Vite community </ p > < ul > < li > < a href = "https://github.com/vitejs/vite" target = "_blank" > < svg className = "button-icon" role = "presentation" aria-hidden = "true" > < use href = "/icons.svg#github-icon" ></ use > </ svg > GitHub </ a > </ li > < li > < a href = "https://chat.vite.dev/" target = "_blank" > < svg className = "button-icon" role = "presentation" aria-hidden = "true" > < use href = "/icons.svg#discord-icon" ></ use > </ svg > Discord </ a > </ li > < li > < a href = "https://x.com/vite_js" target = "_blank" > < svg className = "button-icon" role = "presentation" aria-hidden = "true" > < use href = "/icons.svg#x-icon" ></ use > </ svg > X.com </ a > </ li > < li > < a href = "https://bsky.app/profile/vite.dev" target = "_blank" > < svg className = "button-icon" role = "presentation" aria-hidden = "true" > < use href = "/icons.svg#bluesky-icon" ></ use > </ svg > Bluesky </ a > </ li > </ ul > </ div > </ section > < div className = "ticks" ></ div > < section id = "spacer" ></ section > </> ) } export default App Example Replace all the content of the App.jsx file with the code below: function App () { return ( < div className = "App" > < h1 > Hello World! </ h1 > </ div > ); } export default App ; Notice that the changes are visible immediately after you save the file, you do not have to reload the browser!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/vidhya_murali_5aabe7784bd/setting-up-a-react-environment-9ga

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
