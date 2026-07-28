---
title: "Add a Controlled CapSolver Step to a Skyvern Browser Workflow"
slug: "add-a-controlled-capsolver-step-to-a-skyvern-browser-workflow"
author: "luisgustvo"
source: "devto_ai"
published: "Tue, 28 Jul 2026 08:36:10 +0000"
description: "Skyvern can navigate a page and act from natural-language instructions. CapSolver can return a CAPTCHA result through its SDK. The clean integration is a sma..."
keywords: "page, capsolver, skyvern, token, result, await, not, recaptcha"
generated: "2026-07-28T08:43:31.574395"
---

# Add a Controlled CapSolver Step to a Skyvern Browser Workflow

## Overview

Skyvern can navigate a page and act from natural-language instructions. CapSolver can return a CAPTCHA result through its SDK. The clean integration is a small deterministic bridge between them. Use this only for systems you own or are explicitly authorized to automate. 1. Install the SDKs Skyvern’s current pip quickstart supports Python 3.11–3.13: python -m venv .venv source .venv/bin/activate pip install "skyvern[all]" pip install --upgrade capsolver python -m playwright install chromium Load credentials outside source control: export CAPSOLVER_API_KEY = "set-this-in-your-secret-manager" 2. Understand the boundary Skyvern should own: navigation; semantic element interaction; natural-language actions; result validation. Application code should own: target authorization; CapSolver credentials; task parameters; browser-session continuity; token or text handoff; retry limits; final assertions. 3. Call the documented reCAPTCHA v2 task import capsolver solution = capsolver . solve ({ " type " : " ReCaptchaV2TaskProxyLess " , " websiteURL " : " https://www.google.com/recaptcha/api2/demo " , " websiteKey " : " 6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ- " , }) token = solution [ " gRecaptchaResponse " ] Replace the demo values only with parameters from your authorized page. 4. Hand the token to the current page async def inject_token ( page , token : str ) -> None : await page . evaluate ( """ (token) => { const textarea = document.getElementById( ' g-recaptcha-response ' ); if (!textarea) { throw new Error( ' g-recaptcha-response field not found ' ); } textarea.value = token; textarea.dispatchEvent(new Event( ' change ' , { bubbles: true })); } """ , token , ) Not every frontend uses this field. Some owned applications use a configured callback or application request. Implement the method expected by that application rather than asking the model to guess. 5. Continue with Skyvern Skyvern’s current SDK documents AI-assisted page commands such as: await page . act ( " Submit the form " ) passed = await page . validate ( " The authorized test reached the expected successful result " ) if not passed : raise RuntimeError ( " Final validation failed " ) The final validation is mandatory. A returned token is an intermediate result. 6. Add ImageToTextTask image_src = await page . locator ( " #demoCaptcha_CaptchaImage " ). get_attribute ( " src " ) if not image_src or " , " not in image_src : raise RuntimeError ( " A valid Base64 CAPTCHA image was not found " ) base64_image = image_src . split ( " , " , 1 )[ 1 ] solution = capsolver . solve ({ " type " : " ImageToTextTask " , " websiteURL " : TARGET_URL , " module " : " common " , " body " : base64_image , }) captcha_text = solution [ " text " ] Then fill the expected input, submit, and verify: await page . locator ( " #captchaCode " ). fill ( captcha_text ) await page . locator ( " #validateCaptchaButton " ). click () Check the current ImageToTextTask documentation before selecting optional recognition modules. 7. Handle failures deliberately If the page rejects the result: confirm the page URL and site key; check whether navigation changed the page; verify the expected field or callback; preserve the same browser session; inspect the final assertion; stop when the retry budget is exhausted. Never log the API key, cookies, or raw verification result. 8. Put it together Skyvern navigation → authorization check → CapSolver SDK → deterministic page handoff → Skyvern action → application verification This structure lets the AI layer handle changing interfaces without giving it control over secrets or unrestricted challenge handling. Resources: Skyvern GitHub CapSolver CapSolver reCAPTCHA v2

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/luisgustvo/add-a-controlled-capsolver-step-to-a-skyvern-browser-workflow-569e

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
