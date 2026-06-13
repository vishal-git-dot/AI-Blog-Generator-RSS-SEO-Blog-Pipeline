---
title: "工程師眼中的 “Don’t Make Me Think”"
slug: "dont-make-me-think"
author: "JH5"
source: "devto_ai"
published: "Sat, 13 Jun 2026 04:08:30 +0000"
description: "工程師眼中的 “Don’t Make Me Think” Steve Krug有一本跟使用者經驗有關的經典著作《Don’t Make Me Think》，很多工程師誤以為這本書只屬於 UI/UX 設計師，尤其是現在在Agent AI輔助我們日常的開發下，更需要把工程思維中的「Don’t Make Me… Upda..."
keywords: "don, make, think, message, web, bff, api, sending"
generated: "2026-06-13T04:19:15.388724"
---

# 工程師眼中的 “Don’t Make Me Think”

## Overview

工程師眼中的 “Don’t Make Me Think” Steve Krug有一本跟使用者經驗有關的經典著作《Don’t Make Me Think》，很多工程師誤以為這本書只屬於 UI/UX 設計師，尤其是現在在Agent AI輔助我們日常的開發下，更需要把工程思維中的「Don’t Make Me… UpdatedMarch 24, 2026•2 min read J JhihHao Wu ** 近期研究重點包含 AI Agent 的供應鏈攻擊、PII 偵測模型評估，以及醫療 AI 在臨床流程中的安全落地。 在這裡，我分享深度技術實測報告（如 NVIDIA NeMo, WildGuard）與職場技術成長心得，致力於在 AI 浪潮中打造具備資安韌性的解決方案。 On this page 工程師眼中的 “Don’t Make Me Think”工程師眼中的 “Don’t Make Me Think”1. 從 UX 到 Core Web Vitals (INP)2. Optimistic UI3. BFF (Backend for Frontend)4. K8s 與 韌性設計 (Resilience) 工程師眼中的 “Don’t Make Me Think” Steve Krug — Don’t Make Me Think Steve Krug有一本跟使用者經驗有關的經典著作《Don’t Make Me Think》，很多工程師誤以為這本書只屬於 UI/UX 設計師，尤其是現在在Agent AI輔助我們日常的開發下，更需要把工程思維中的「Don’t Make Me Think」的精神，轉換成使用者想要的 「Don’t Make Me Wait」 與 「Don’t Make Me Guess」相關需求。 工程師眼中的 “Don’t Make Me Think” 這本書的核心原則是「減少用戶的認知負荷」，對應到全端開發的工作中，我們更應該著重在 Latency（延遲） 、 Feedback（反饋） 與 Resilience（韌性） 。 1. 從 UX 到 Core Web Vitals (INP) 現在 Google 的核心指標已經進化，要讓用戶「不思考」，網頁必須像原生 App 一樣流暢。 INP (Interaction to Next Paint): 這是 2024 年取代 FID 的新指標，主要測量的是「用戶點擊後，畫面 真正 給出視覺反饋」的時間。 如果用戶點了按鈕，畫面卡頓 500ms 沒反應，用戶就會開始 思考 ：「我是不是沒點到？還是當機了？」。 工程解法： Main Thread Blocking: 避免巨大的 Hydration 阻塞主執行緒。 Web Workers: 將繁重的運算移出主執行緒。 2. Optimistic UI 不需要等 Server 回應才告訴用戶「成功了」，以用戶按「讚」這樣常見的功能來看， 傳統做法： 點擊 -> Loading Spinner -> Server 回傳 200 OK -> UI 變更為已按讚。(用戶等待 200ms-1s)，而Optimistic UI 的想法則為， 點擊 -> UI 立刻變更為已按讚 -> 背景發送 API。(用戶感覺 0ms 延遲)，例如 React 中已經可以 使用新的 useOptimistic hook。 import { useOptimistic , useState , useRef } from ' react ' ; // 模擬後端 API async function deliverMessage ( message ) { await new Promise (( res ) => setTimeout ( res , 1000 )); // 模擬 1秒 延遲 return message ; } export default function Thread ({ messages , sendMessage }) { // 1. 設定樂觀狀態 const [ optimisticMessages , addOptimisticMessage ] = useOptimistic ( messages , ( state , newMessage ) => [ ... state , { text : newMessage , sending : true } // 立即顯示，並標記為發送中 ] ); async function formAction ( formData ) { const message = formData . get ( " message " ); // 2. 在 API 請求前，直接更新 UI (Optimistic Update) addOptimisticMessage ( message ); // 3. 背景執行真實請求 await sendMessage ( message ); } return ( < div > { optimisticMessages . map (( m , i ) => ( < div key = { i } style = {{ opacity : m . sending ? 0.5 : 1 }} > { m . text } { m . sending && < small > ( Sending ...) < /small>} < /div> ))} < form action = { formAction } > < input type = " text " name = " message " /> < button type = " submit " > Send < /button> < /form> < /div> ); } 這段程式碼的精髓在於，即便網路很慢，用戶也會覺得你的 App 是「瞬間」完成動作的，這便是經典的利用工程手段降低認知負荷。 3. BFF (Backend for Frontend) 要讓前端「無腦」渲染，後端就不能丟一堆垃圾資料給前端處理。 如果一個畫面需要 User Profile + Order History + Recommendations，傳統 REST API 可能要前端發 3 個 Requests，然後自己在前端組裝。這增加了前端邏輯複雜度與延遲。 在BFF 模式下，可以 為 Web 端建立一個專屬 Backend Service，再為 iOS/Android 建立另一個，而前幾年流行的 GraphQL 則是實踐 BFF 的絕佳工具，雖然偶爾會看到濫用ＸＤ，帶來的效益便是 Over-fetching 歸零， 前端只拿需要的欄位，頻寬變小，速度變快。 4. K8s 與 韌性設計 (Resilience) 當系統出錯時，「Don’t Make Me Think」意味著不要給用戶看 500 Internal Server Error 這種工程師才懂的訊息，或是當某個 Microservice (例如：推薦系統) 掛掉時，不要讓整個首頁轉圈圈，應該直接切斷對該服務的請求，並回傳「預設/快取」的資料。 透過 Graceful Degradation 的設計，正常狀況下可以 顯示個人化推薦商品，而當 服務掛掉時，則： 顯示「本週熱門商品」(從 Redis Cache 拿)。對用戶來說，他根本不知道你後端掛了，體驗依然流暢，這就是最高級的 UX 這本書不只是設計師的讀物，更是每個開發使用者面向產品的「效能與架構指南」。 前端： 騙過用戶的眼睛，讓他們覺得網站飛快。 後端： 用 BFF 幫前端把資料切好，不要讓瀏覽器做重工。 維運： 用 K8s + Redis 做好降級策略，永遠不要讓用戶看到錯誤代碼。 # ai

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jh5_pulse/gong-cheng-shi-yan-zhong-de-dont-make-me-think-1ne4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
