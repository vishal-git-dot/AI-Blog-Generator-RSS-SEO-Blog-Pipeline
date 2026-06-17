---
title: "不搭百度云、不绑手机号，5 分钟用 Baidu OCR + GoldBean 识别中文文档"
slug: "5-baidu-ocr-goldbean"
author: "goldbean"
source: "devto_python"
published: "Wed, 17 Jun 2026 04:12:53 +0000"
description: "不搭百度云、不绑手机号，5 分钟用 Baidu OCR 识别中文文档 TL;DR ： GoldBean 封装了百度 OCR API，一个接口搞定身份证、银行卡、营业执照、发票识别。无需中国手机号，按次付费 $0.01 起。支持 Python、cURL、Node.js。 痛点：为什么海外开发者用不了百度 OCR？ ..."
keywords: "api, ocr, goldbean, baidu, curl, key, https, json"
generated: "2026-06-17T04:47:02.509484"
---

# 不搭百度云、不绑手机号，5 分钟用 Baidu OCR + GoldBean 识别中文文档

## Overview

不搭百度云、不绑手机号，5 分钟用 Baidu OCR 识别中文文档 TL;DR ： GoldBean 封装了百度 OCR API，一个接口搞定身份证、银行卡、营业执照、发票识别。无需中国手机号，按次付费 $0.01 起。支持 Python、cURL、Node.js。 痛点：为什么海外开发者用不了百度 OCR？ 你需要识别中文文档。你搜到百度 OCR 是业界最好的中文 OCR 引擎之一（中文识别准确率 96%+）。 但注册百度云需要： 中国手机号 ❌ 你没有 实名认证 ❌ 麻烦 预存几百块 ❌ 不想 解决方案：GoldBean × Baidu OCR GoldBean 是一个按次付费 API 市场，封装了百度 AI 的 13 个核心 API。 一个 API Key 搞定，无需预存款，最低 $0.01/次，全球可用。 为什么选 GoldBean？ 对比项 GoldBean 直接百度云 手机号验证 不需要 必须 (中国手机) 预存款 $0 100+ 起付金额 $0.01/次 按套餐 全球访问 任何国家 部分地区限制 支付方式 支付宝/PayPal/USDC 仅国内支付 5 分钟教程 第 1 步：获取 API Key 打开 GoldBean 官网 充值 $1（支持支付宝 / PayPal / USDC on Base） 获取你的 API Key 第 2 步：cURL 调用 curl -X POST https://goldbean-api.xyz/api/baidu/ocr/general-basic \ -H "Authorization: Bearer YOUR_API_KEY" \ -H "Content-Type: application/json" \ -d '{"image": "https://example.com/chinese-doc.jpg"}' 第 3 步：Python 示例 import requests import base64 API_KEY = " your_goldbean_api_key " BASE_URL = " https://goldbean-api.xyz/api/baidu/ocr " with open ( " invoice.jpg " , " rb " ) as f : img_b64 = base64 . b64encode ( f . read ()). decode () resp = requests . post ( f " { BASE_URL } /general-basic " , headers = { " Authorization " : f " Bearer { API_KEY } " }, json = { " image " : img_b64 } ) print ( resp . json ()) 支持的 OCR 类型 API 用途 价格 通用文字识别 印刷体文档 $0.01 高精度版 复杂场景文本 $0.02 身份证识别 姓名/身份证号/地址 $0.01 银行卡识别 卡号/银行/有效期 $0.01 营业执照识别 统一信用代码/公司名 $0.01 增值税发票识别 发票代码/金额/日期 $0.02 适用场景 跨境电商 - 识别中文发票、营业执照 出海产品 - 集成中文 OCR 功能 学术研究 - 批量中文文档数字化 RAG 系统 - 中文文档预处理 更多 Baidu AI API GoldBean 不止有 OCR，还集成了百度其他 12 个 AI API。查看 Baidu AI 完整指南 。 GoldBean API | GitHub GoldBean (GB) - Wishing You Good Fortune & Prosperity

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/goldbean/bu-da-bai-du-yun-bu-bang-shou-ji-hao-5-fen-zhong-yong-baidu-ocr-goldbean-shi-bie-zhong-wen-4cc9

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
