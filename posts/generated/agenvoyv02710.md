---
title: "Agenvoy@v0.27.10"
slug: "agenvoyv02710"
author: "邱敬幃 Pardn Chiu"
source: "devto_ai"
published: "Sat, 27 Jun 2026 03:54:37 +0000"
description: "Agenvoy - A personal agent that writes its own tools and repairs itself — Make AI actually work for you. v0.27.5 -> v0.27.10 Summary Unifies tool adapter and..."
keywords: "mcp, tool, add, copilot, agent, adapter, api, tui"
generated: "2026-06-27T03:58:09.836566"
---

# Agenvoy@v0.27.10

## Overview

Agenvoy - A personal agent that writes its own tools and repairs itself — Make AI actually work for you. v0.27.5 -> v0.27.10 Summary Unifies tool adapter and MCP infrastructure while hardening runtime resilience. Consolidates script and API tool guidance under a single ToolGuide layer, adds MCP authentication and automatic reconnection, and introduces provider cooldown with dispatcher retry-and-fallback. New user-facing controls include TUI prompt template selection, LLM-based history compaction, and reasoning-level tuning. Cleans up legacy browser login helpers, bot name sync, and session-scoped MCP configuration. 翻譯 統一 tool adapter 與 MCP 基礎設施，同步強化執行期韌性。將 script 與 API 工具指引合併為單一 ToolGuide 層、新增 MCP 驗證與自動重連、引入 provider 冷卻與 dispatcher fallback 重試機制。使用者面新增 TUI prompt template 選擇、LLM 歷史壓縮、推理等級調整。清理舊版瀏覽器登入 helper、bot 名稱同步與 session 級 MCP 設定。 Changes FEAT Add TUI prompt template picker and upgrade go-browser [ec4d553] Add MCP auth flow and normalize authorization headers [be5b5c0] Add LLM-based history compaction via /compact command [61029c9] Add dispatcher retry with fallback and tool activity display in TUI thinking line [0322248] Add MCP reconnect flow with status display and server info [3636c7a] Add reasoning level control and copilot priority boost [84b3730] 翻譯 新增 TUI prompt template 選擇器並升級 go-browser 新增 MCP 驗證流程並正規化授權標頭 新增基於 LLM 的歷史壓縮功能，透過 /compact 指令觸發 新增 dispatcher 帶 fallback 的重試機制，並於 TUI thinking 行顯示 tool 活動 新增 MCP 重連流程，含狀態顯示與 server 資訊 新增推理等級控制與 copilot 優先提升 FIX Reset tool-call state after agent/model switch [d570701] Always-load RAG tools, switch project instructions to AGENTS.md, and isolate MCP empty schemas [cd690b7] Fix rate-limit handling and add provider cooldown mechanism [adfbb6b] Restore Copilot agent naming with copilot@ prefix and schedule session cleanup via system cron [feb21a8] 翻譯 在 agent/model 切換後重置 tool-call 狀態 強制載入 RAG 工具、將專案指示切換至 AGENTS.md，並隔離 MCP 空 schema 修正 rate-limit 處理並新增 provider 冷卻機制 修復 Copilot agent 命名加回 copilot@ 前綴，並透過系統 cron 排程 session 清理 REFACTOR Replace ScriptToolGuide with unified ToolGuide and rename LoadFS to Builtin in API adapter [9494ed9] Replace Translator with Adapter and consolidate API execution logic [ccdaf6e] Hide tool-cache internals and label plug tools generically [035df0c] Use dedicated download directory path consistently across all callers [a43b0aa] Normalize record log helpers and standardize slog error labels [d34c5dc] Rename resolved skill content helpers and normalize error labels [e087005] 翻譯 以統一 ToolGuide 取代 ScriptToolGuide，並將 API adapter 的 LoadFS 更名為 Builtin 以 Adapter 取代 Translator 並整合 API 執行邏輯 隱藏 tool-cache 內部實作並泛化 plug tools 標籤 統一所有 caller 使用專屬下載目錄路徑 正規化記錄 log helper 與 slog 錯誤標籤 重新命名 skill 內容 helper 並正規化錯誤標籤 REMOVE Remove legacy direct login browser helpers from Copilot and Codex agents [54c7107] Remove legacy bot name sync and history delete helpers [743e020] Remove session-scoped MCP config and unify global MCP settings [21df3a0] 翻譯 移除 Copilot 與 Codex agent 的舊版直接登入瀏覽器 helper 移除舊版 bot 名稱同步與 history 刪除 helper 移除 session 級 MCP 設定，統一為全局 MCP 設定 TEST Add toolAdapter unit tests and update Makefile test target [6144954] 翻譯 新增 toolAdapter 單元測試並更新 Makefile 測試目標

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/pardnchiu/agenvoyv02710-k74

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
