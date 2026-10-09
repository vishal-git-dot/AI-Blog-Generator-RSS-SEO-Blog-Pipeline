---
title: "【完全無料・サーバーレス】AWS Lambda FastAPI で作る「お出かけホテル検索マップ」の手順"
slug: "aws-lambda-fastapi"
author: "minaduki"
source: "devto_python"
published: "Fri, 09 Oct 2026 04:59:31 +0000"
description: "こんにちは！今回は、自宅の重いサーバーや有料のホスティング環境を使わず、AWS Lambdaの永年無料枠を活用して、ほぼ完全無料（サーバー代0円）で動くホテル検索マップアプリを個人開発したので、その仕組みと作り方をシェアしたいと思います。 hotel map フロントエンドの地図操作から、バックエンドのPytho..."
keywords: "fastapi, request, import, aws, google, mangum, requests, item"
generated: "2026-10-09T05:33:37.106461"
---

# 【完全無料・サーバーレス】AWS Lambda FastAPI で作る「お出かけホテル検索マップ」の手順

## Overview

こんにちは！今回は、自宅の重いサーバーや有料のホスティング環境を使わず、AWS Lambdaの永年無料枠を活用して、ほぼ完全無料（サーバー代0円）で動くホテル検索マップアプリを個人開発したので、その仕組みと作り方をシェアしたいと思います。 hotel map フロントエンドの地図操作から、バックエンドのPython（FastAPI）、そして安全に公開するためのセキュリティ対策までギュッとまとめました。 このアプリで実現したこと・アーキテクチャ 地図上で中心地を選ぶと、その周辺にあるホテルを自動で検索して一覧・マップ表示してくれるアプリです。 フロントエンド: HTML / JavaScript （Google Mapsをインタラクティブに操作） バックエンド: Python 3.11 ＋ FastAPI インフラ（ホスティング）: AWS Lambda（関数URL）＋ Mangum 外部API: SerpAPI（Google Hotels） 「サーバーレス」構成にすることで、アクセスがないときの維持費は完全0円。個人開発のサービス公開やポートフォリオにぴったりの構成です。 実装のポイントとハマりどころ 今回の開発でこだわったポイントや、実際に躓きやすいポイントをいくつか紹介します。 ① 重いSDKを排除し、requests 直叩きで軽量化 AWS Lambdaで動かす際、パッケージサイズが大きすぎるとデプロイやコールドスタート（初回起動）のパフォーマンスに影響します。今回は余計な重いSDKを使わず、標準的な requests ライブラリだけでSerpAPIのエンドポイントを直接叩くシンプルな設計にしました。 ② Windows環境でのZIP地獄をPowerShellでスマートに解決 Lambdaに外部ライブラリ（fastapi, requests など）を同梱してアップロードするためには、依存関係を含めたZIPファイルを作る必要があります。Windows環境ではPowerShellを使って以下のように一撃でビルド・圧縮する仕組みを整えました。 PowerShell 依存関係のインストールとZIP圧縮のスクリプト例 Remove-Item -ErrorAction SilentlyContinue deployment.zip Remove-Item -Recurse -Force -ErrorAction SilentlyContinue package pip install --platform manylinux2014_x86_64 --target package --implementation cp --python-version 3.11 --only-binary=:all: fastapi uvicorn mangum pydantic requests New-Item -ItemType Directory -Force package | Out-Null Copy-Item main.py package/ if (Test-Path templates) { Copy-Item -Recurse -Force templates package/ } Add-Type -AssemblyName System.IO.Compression.FileSystem 安全に公開するための「4つのセキュリティ対策」 個人でWebアプリを公開する場合、APIキーの流出や不正利用（予期せぬコスト発生）を防ぐ対策が不可欠です。今回は以下の万全な備えを行っています。 APIキーの完全隠蔽 Google MapsやSerpAPIのキーはソースコードに直書きせず、すべてAWS Lambdaの環境変数として安全に管理しています。 Google Maps APIの「HTTPリファラー制限」 万が一キーが露出しても他のサイトで勝手に使われないよう、Google Cloud Console側で「自分のLambda関数URL」からしかマップが読み込めないよう制限をかけています。 アプリ側の簡易レートリミット（回数制限） 不正なボット等による無限スクレイピングを防ぐため、IPアドレスごとに「1人あたり3回まで」の検索制限をコード内に実装しています。 エラーメッセージのマスク処理 バックエンドで万が一エラーが起きた際、内部のシステム詳細やパスが画面に露出しないよう、クライアント側には一律で Internal Server Error を返し、詳細な原因はAWSのCloudWatch Logsにだけ記録するようにしています。 さらに、AWS Budgets（予算アラート）を設定して、万が一のコスト発生時にも即座に気づける体制にしています。 サンプルコード（バックエンド: main.py） 実際にAWS Lambda（Mangum経由）で動かしているFastAPIのメインコードはこちらです。 Python import os import math from collections import defaultdict import requests from fastapi import FastAPI, HTTPException, Query, Request from fastapi.responses import HTMLResponse from mangum import Mangum 環境変数からAPIキーを取得 GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY", "") SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY", "") IPごとの簡易検索回数管理（3回まで） search_counts = defaultdict(int) MAX_SEARCH_LIMIT = 3 def check_search_limit(request: Request): client_ip = request.client.host if request.client else "unknown" if search_counts[client_ip] >= MAX_SEARCH_LIMIT: raise HTTPException( status_code=429, detail="無料体験の検索回数（3回）に達しました。ページを再読み込みしてください。" ) search_counts[client_ip] += 1 app = FastAPI() @app.get("/api/search-vacant-hotels") def search_vacant_hotels(request: Request, ...): check_search_limit(request) try: # ホテル検索ロジック... return {"hotels": []} except HTTPException: raise except Exception as e: print(f"[Backend Exception]: {e}") raise HTTPException(status_code=500, detail="Internal Server Error") @app.get("/", response_class=HTMLResponse) def read_root(): # HTMLテンプレートを読み込んでAPIキーを埋め込む処理 ... handler = Mangum(app) おわりに サーバーレスと聞くと難しそうに感じるかもしれませんが、AWS Lambdaの関数URLとFastAPIを組み合わせれば、驚くほど手軽にモダンなWebアプリを公開できます。

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/_ad122393ca44f5a698b1/wan-quan-wu-liao-sabaresu-aws-lambda-fastapi-dezuo-ruochu-kakehoterujian-suo-matupu-noshou-shun-bj3

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
