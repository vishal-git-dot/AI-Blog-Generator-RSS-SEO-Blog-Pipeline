---
title: "git worktree でコーディングエージェントを並列実行する開発環境の作り方"
slug: "git-worktree"
author: "orca_forge"
source: "devto_ai"
published: "Fri, 17 Jul 2026 19:03:09 +0000"
description: "📝 Originally published at forge.workstyle.tech . 複数のコーディングエージェント（Claude Code や Codex など）を試していると、こんな悩みに突き当たります。「同じリポジトリで別々のタスクを同時に進めたいが、作業が互いに干渉してしまう」「エージェントA..."
keywords: "git, worktree, cli, ade, diff, claude, node, path"
generated: "2026-07-17T19:18:11.650784"
---

# git worktree でコーディングエージェントを並列実行する開発環境の作り方

## Overview

📝 Originally published at forge.workstyle.tech . 複数のコーディングエージェント（Claude Code や Codex など）を試していると、こんな悩みに突き当たります。「同じリポジトリで別々のタスクを同時に進めたいが、作業が互いに干渉してしまう」「エージェントAとエージェントBの結果を並べて比較したい」。 これを解決するのが git worktree を使った並列実行環境 です。この記事では、専用のデスクトップ型 ADE（Agent Development Environment）を例に、セットアップから並列比較、デプロイ承認までの流れを整理します。特定ツールに依存しない考え方が中心なので、自分の環境に読み替えて活用できます。 なぜ git worktree なのか git worktree は、1つのリポジトリから 複数の作業ディレクトリ を切り出せる仕組みです。ブランチごとに独立したフォルダが用意されるため、次のような使い方が可能になります。 タスクAはエージェントに任せつつ、タスクBは別のエージェントに任せる それぞれの変更が別ディレクトリに閉じるので、ファイルの衝突が起きない 同じ課題を複数のエージェントに解かせ、diff を並べて品質を比較する ブランチ切り替え（ git checkout ）だと作業ツリーは1つきりですが、worktree なら物理的に別の場所で並行作業できる、というのがポイントです。 事前に揃えておくもの 環境を作る前に、以下が入っているか確認します。 コーディングエージェントの CLI（例: Claude Code）と、その ログイン認証済みの状態 git と node （プロジェクトの CI で使うランタイム） エージェントを束ねる ADE アプリ本体 エージェントの認証はホームディレクトリの設定（例: ~/.claude ）に保存され、ADE 側がそれを自動参照する方式が一般的です。すでに CLI でログイン済みなら、 追加のログイン設定は不要 なことが多く、GUI から繋ぐだけで使い始められます。 セットアップの流れ 1. アプリを起動して初期許可を与える 初回起動時にホームディレクトリへのアクセス許可を求められたら許可します。既存設定のインポートを促されたら、必要なければスキップして構いません。 2. リポジトリを追加する 作業対象のリポジトリを登録します。いきなり本番リポジトリではなく、 練習用の小さなサンプルリポジトリ から始めるのがおすすめです。追加すると git の状態が読み取られ、デフォルトブランチ（多くは main ）が基準（base ref）に設定されます。 3. ワークツリー（タスク）を作成する タスク名を付けて新しいワークツリーを作ります。これが main から独立した git worktree となり、他タスクと干渉しない作業場所になります。タスク名は add-readme-section のように内容が分かるものにしておくと後で追いやすくなります。 4. エージェントを割り当てる ワークツリーごとに使うエージェントを選びます。認証は前述の設定を自動参照するため、ログイン済みなら即実行できます。 5. プロンプトを与えて実行する 「README に使い方セクションを追加して」のような具体的な指示を出して走らせます。 6. 並列で比較する ここが並列環境の真価です。同じ課題に対して、手順3〜4を繰り返し -2 , -3 のように複数のワークツリーを作り、別々のエージェントを割り当てます。ペインを分割すれば、それぞれの進行を同時に監視し、結果を横並びで比較できます。 レビューからデプロイまで 各ワークツリーの diff ビュー で変更内容を確認します。AI による差分評価（アノテーション）機能があれば、レビューの一次スクリーニングに使えます。 良い結果が得られたら commit & push 。ここから先は自動化されたパイプラインに乗せるのが定石です。 PR 作成 — push をトリガーにプルリクエストが作られる CI 実行 — テスト（例: node --test ）が自動で走る デプロイ — 本番反映は手動トリガー（Run workflow）にして、 人間の承認ゲート を挟む エージェントが書いたコードであっても、CI と人間の承認を通す流れは変えない、というのが安全に運用するコツです。自動生成だからこそ、機械的なテストと人の目という二段構えを崩さないようにします。 つまずきやすいポイント PATH の問題 最もよくあるトラブルが「エージェントの CLI が見つからない」です。バージョン管理ツール（fnm や nvm など）経由で node や CLI を入れている場合、それらはシェルプロファイル（ .zshrc など）で初期化されて初めて PATH に載ります。 ADE が起動するシェルがこのプロファイルを読み込んでいないと、コマンドが見つかりません。もし「コマンドが見つからない」と出たら、 シェルプロファイルの初期化行 を確認しましょう。 認証の重複 複数アカウントを切り替える場合、認証リフレッシュが重複しないようガードされている実装が多いです。基本はホームディレクトリの設定に任せておけば問題ありません。 まとめ git worktree を使うと、複数のコーディングエージェントを 干渉なく並列実行 できる 同じ課題を複数エージェントに解かせ、diff を並べて品質を比較できる レビューは diff ビューで、本番反映は CI + 人間の承認ゲート で守る 最大の落とし穴は PATH。バージョン管理ツールの初期化がシェルプロファイルに入っているか確認する 多くの環境では新しく入れるものは少なく、既存の CLI 認証を繋ぐだけで並列エージェント開発を始められます。まずは練習用リポジトリで、同じ指示を2〜3のエージェントに投げて比較するところから試してみてください。

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/orca_forge/git-worktree-dekodeinguezientowobing-lie-shi-xing-surukai-fa-huan-jing-nozuo-rifang-3g1g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
