---
title: "自動化測試 API 權限漏洞與 OpenAPI 安全性"
slug: "api-openapi"
author: "JH5"
source: "devto_python"
published: "Sat, 13 Jun 2026 04:08:18 +0000"
description: "自動化測試 API 權限漏洞與 OpenAPI 安全性 許多團隊在導入 微服務架構後，往往會因為自動生成了 Swagger/OpenAPI，卻常常卻忘記權限控管，導致 API 變成大家的遊樂園ＸＤ，而AutoSwagger 就是針對這個痛點而生的工具。 UpdatedMarch 24, 2026•2 min re..."
keywords: "api, autoswagger, swagger, json, openapi, get, demo, https"
generated: "2026-06-13T04:19:15.384142"
---

# 自動化測試 API 權限漏洞與 OpenAPI 安全性

## Overview

自動化測試 API 權限漏洞與 OpenAPI 安全性 許多團隊在導入 微服務架構後，往往會因為自動生成了 Swagger/OpenAPI，卻常常卻忘記權限控管，導致 API 變成大家的遊樂園ＸＤ，而AutoSwagger 就是針對這個痛點而生的工具。 UpdatedMarch 24, 2026•2 min read J JhihHao Wu ** 近期研究重點包含 AI Agent 的供應鏈攻擊、PII 偵測模型評估，以及醫療 AI 在臨床流程中的安全落地。 在這裡，我分享深度技術實測報告（如 NVIDIA NeMo, WildGuard）與職場技術成長心得，致力於在 AI 浪潮中打造具備資安韌性的解決方案。 On this page 自動化測試 API 權限漏洞與 OpenAPI 安全性AutoSwagger 是什麼？Deep Dive AutoSwagger1. 自動化流程圖2. 為什麼這很危險？AutoSwagger Demo第一步：安裝環境第二步：基礎掃描第三步：進階模糊測試 (Brute Force Mode) 自動化測試 API 權限漏洞與 OpenAPI 安全性 AutoSwagger 許多團隊在導入 微服務架構後，往往會因為自動生成了 Swagger/OpenAPI，卻常常卻忘記權限控管，導致 API 變成大家的遊樂園ＸＤ，而 AutoSwagger 就是針對這個痛點而生的工具。 AutoSwagger 是什麼？ AutoSwagger 是一款由 Intruder 開發的開源 CLI 工具（基於 Python），專門用於自動化發現、解析並測試 Swagger/OpenAPI 定義的 API 端點，主要用來解決 「Broken Authorization」（權限失效） 的問題。 很多開發者會在 API 上加上驗證（Authentication），但卻漏掉了授權（Authorization），或者某些隱藏的端點（Shadow APIs）根本沒有保護。 自動偵測 (Discovery) ：它會掃描目標 URL，嘗試尋找 swagger.json , openapi.yaml 等常見路徑，或是解析 swagger-ui.html 頁面來抓取定義檔。 智慧解析 (Parsing) ：讀取 API 規格，理解每個端點需要的參數類型（String, Int, UUID 等），另外還有 Fuzzing Mode， 可以使用 --brute 參數時，它會嘗試用各種邊界值來繞過簡單的驗證邏輯。 併發測試 (Concurrent Testing) ：模擬請求去打這些 API，檢查是否在「未登入」的情況下回傳了 200 OK，或者洩露了 PII（個人識別資訊），而且內建 Microsoft Presidio， 利用 NLP 技術自動識別回傳內容中的敏感個資（Email、電話、信用卡號）。 Deep Dive AutoSwagger 讓我們用工程師都懂的語言來拆解它： 1. 自動化流程圖 你可以把它想像成一個「自動化的 API 測試機器人」，流程如下： graph LR A [ 目標 URL ] --> B { 規格偵測 } B -->| 找到 swagger . json | C [ 解析器 Parser ] B -->| 找不到 | D [ 暴力枚舉路徑 ] D --> B C --> E [ 攻擊面生成 Attack Surface ] E --> F { 並發測試 Runner } F -->| 發送 Payload | G [ 目標 API ] G -->| 回傳 Response | H [ 結果分析器 Analyzer ] H -->| PII 偵測 / 敏感關鍵字 | I [ 報告輸出 JSON / Table ] 2. 為什麼這很危險？ 在 K8s 環境中，我們常使用 Ingress 或 API Gateway。 開發者思維 ：「我的 API 都在內網，或者我有加 JWT 驗證，Swagger 開出去給前端看沒關係。」 AutoSwagger 思維 ：「真的每一個端點都有加 verifyToken middleware 嗎？有沒有漏掉的 GET /users/export 或是 GET /admin/config 」 這工具就是用來 驗證「你以為你有鎖，但其實沒鎖」的端點。 AutoSwagger Demo 假設我們有一個網站的 API 跑在 https://api.shop-demo.com ，開發者不小心把 Swagger UI 暴露在公開網路。 第一步：安裝環境 AutoSwagger 是 Python 寫的，這對我們全端工程師來說非常友善。 # Clone 專案 git clone https://github.com/intruder-io/autoswagger.git cd autoswagger # 建議使用 virtualenv 隔離環境 python3 -m venv venv source venv/bin/activate # 安裝依賴 (包含 Presidio NLP 引擎) pip install -r requirements.txt 第二步：基礎掃描 我們讓 AutoSwagger 自動去尋找規格書並掃描所有 GET 請求，看看是否有未授權的資料流出。 # -v: 詳細模式, -json: 輸出成 JSON 格式以便後續串接 CI/CD python3 autoswagger.py https://api.shop-demo.com -v -json > report.json 接著會自動嘗試存取 https://api.shop-demo.com/swagger/v1/swagger.json 。如果找到，它會解析出 50 個 API 端點，然後會開始並行發送請求。 [+] Parsing schema from: https://api.shop-demo.com/swagger/v1/swagger.json [+] Found 50 endpoints. [+] Starting scan... [ VULNERABLE ] GET /api/v1/users/recent Status : 200 OK Size : 4 . 5 KB Secrets Found : [ "AWS_ACCESS_KEY_ID" ] PII Detected : [ "Email" , "Phone Number" ] 發現 GET /api/v1/users/recent 這個端點竟然在沒有 Token 的情況下回傳了 200，而且內容包含了 AWS Key 和 Email，而這種案例通常是因為開發者在寫 Controller 時忘記掛上 Auth Middleware ～ 第三步：進階模糊測試 (Brute Force Mode) 如果 API 有參數驗證（例如需要 UserID），我們可以開啟暴力模式。 # -b: 開啟 Brute force，嘗試繞過參數檢查 python3 autoswagger.py https://api.shop-demo.com -b 假設有一個端點 GET /api/orders/{id}， AutoSwagger 會自動分析 {id} 是 UUID 還是 Integer，然後自動填入測試值，例如 GET /api/orders/1 或 GET /api/orders/00000000-0000-0000-0000-000000000000 ，試圖誘騙後端回傳資料XD 以前最常聽到的名言就是，資安最大的弱點是人ＸＤ 無論ＡＩ再怎麼輔助我們開發，有滿多日常開發的Practice還是得扎實的面對，例如在 Production 環境的 K8s Ingress 中，直接 Block 掉 /swagger-ui.html , /v2/api-docs , /openapi.json 等路徑，讓Swagger 只能在 Dev/Staging 環境存取。 此外，不要在每個 Controller 上單獨加 Auth，應該在 API Gateway 層或是框架的最外層 Middleware 強制要求 Auth，只有特定的 Public Endpoint (如 Login) 設為例外 (Allowlist)。 如果可以的話，把 AutoSwagger 加入你的 CI Pipeline，在每次部署 Staging 後，自動跑一次掃描，確保沒有新的端點意外暴露。 # ai # python # security

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jh5_pulse/zi-dong-hua-ce-shi-api-quan-xian-lou-dong-yu-openapi-an-quan-xing-396f

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
