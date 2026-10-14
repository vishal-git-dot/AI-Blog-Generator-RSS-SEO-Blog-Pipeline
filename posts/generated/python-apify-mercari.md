---
title: "Python Apifyで日本の中古市場データをスクレイピング 。 Mercari・ヤフオク・ラクマの実装例"
slug: "python-apify-mercari"
author: "atu ino"
source: "devto_python"
published: "Wed, 14 Oct 2026 21:03:57 +0000"
description: "日本の中古市場（Mercari、Yahoo!オークション、ラクマなど）から構造化データを取得するためのApify Actor群を公開しています。 なぜApify Actorなのか 日本のマーケットプレイスはAPIが限られており、構造化された情報を得るのが困難です。これらのActorはスクレイピングの複雑さを隠蔽し..."
keywords: "japan, scraper, mcp, market, mercari, prices, search, yahoo"
generated: "2026-10-14T21:28:09.486812"
---

# Python Apifyで日本の中古市場データをスクレイピング 。 Mercari・ヤフオク・ラクマの実装例

## Overview

日本の中古市場（Mercari、Yahoo!オークション、ラクマなど）から構造化データを取得するためのApify Actor群を公開しています。 なぜApify Actorなのか 日本のマーケットプレイスはAPIが限られており、構造化された情報を得るのが困難です。これらのActorはスクレイピングの複雑さを隠蔽し、リアルタイムの価格・出品データを提供します。 主なActor一覧 Actor ターゲット 抽出データ mercari-japan-search-scraper Mercari Japan 検索結果、価格、出品詳細 yahoo-auctions-japan-scraper Yahoo Auctions 出品・落札データ、入札履歴 japan-kakaku-price-search Kakaku.com 家電・雑貨の価格比較 suumo-japan-real-estate-scraper SUUMO 賃貸・物件情報 japan-market-mcp 複数プラットフォーム 統一MCPインターフェース rakuten-japan-mcp 楽天市場 商品カタログ（MCP対応） mandarake-auction-scraper まんだらけ オークション出品データ japan-used-camera-market-scraper カメラ市場 中古カメラ価格データ Why this matters 日本の市場データはAPIが限られており、構造化された情報を得るのが困難です。これらのActorはスクレイピングの複雑さを隠蔽し、リアルタイムの価格・出品データを提供します。 Getting started 各ActorにはExample run input、Dataset output（JSON/CSV）、Scheduled runs機能が付きます。 from apify import ApifyClient client = ApifyClient ( token = " YOUR_APIFY_TOKEN " ) # Mercari検索例 run = client . actor ( " fruitful_quintessence/mercari-japan-search-scraper " ). call ( input_override = { " searchTerms " : " Nintendo Switch " , " maxItems " : 100 } ) # データ取得 data = run . data_items ソース: github.com/atushi1841/kensho さらに多くのActorへ 上記のActorに加えて、 Apify Store では以下のActorも公開中です。 Actor 用途 japan-hobby-market-scanner 日本ホビーマーケットスキャン japan-offmall-market-scraper オフモール市場データ tackleberry-japan-fishing-tackle-scraper 釣具市場データ 全Actorは Apify Store で公開中（85本以上）。 Smithery MCP Server さらに、これらのデータをMCP経由で直接アクセスできます： # japan-ec-mcp をインストール npx @smithery/cli install atushi1841/japan-ec-mcp --client claude # japan-market-mcp をインストール npx @smithery/cli install atushi1841/japan-market-mcp --client claude 実用的な利用例 価格監視パイプライン mercari-japan-search-scraper で毎日キーワード監視 japan-market-mcp で価格比較API経由で一括取得 mlit-japan-property-prices で不動産価格と組み合わせる データ分析例 import json # データロード with open ( " mercari_data.json " ) as f : items = json . load ( f ) # 価格分布分析 prices = [ item [ " price " ] for item in items if " price " in item ] print ( f " 平均価格: { sum ( prices ) / len ( prices ) : . 0 f } 円 " ) print ( f " 中央値: { sorted ( prices )[ len ( prices ) // 2 ] } 円 " ) このように、PythonとApifyを組み合わせることで、日本市場のデータを自在に活用できます。 この投稿で使用したデータソース mercari-japan-search-scraper yahoo-auctions-japan-scraper japan-market-mcp rakuten-japan-mcp mandarake-auction-scraper japan-used-camera-market-scraper

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/atu_ino_ed473db24d76d234a/pythonxapifyderi-ben-nozhong-gu-shi-chang-detawosukureipingu-mercariyahuokurakumanoshi-zhuang-li-n5o

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
