---
title: "My backtest re-runs when I save the strategy file, and shows which trades changed"
slug: "my-backtest-re-runs-when-i-save-the-strategy-file-and-shows-which-trades-changed"
author: "Tomozo / HAWK Backtester"
source: "devto_python"
published: "Sun, 11 Oct 2026 04:03:41 +0000"
description: "I'm building a backtesting web app called Hawk Backtester on the side. This post is about one feature, a watch mode for local Python strategies. The loop tha..."
keywords: "run, strategy, close, trades, browser, slow, hawk, side"
generated: "2026-10-11T05:08:30.392863"
---

# My backtest re-runs when I save the strategy file, and shows which trades changed

## Overview

I'm building a backtesting web app called Hawk Backtester on the side. This post is about one feature, a watch mode for local Python strategies. The loop that annoyed me most was edit the strategy, run it in a terminal, open the results, then try to remember what the previous run looked like. The last step was the worst. If PnL went up a little, I couldn't tell whether my change did it or a couple of trades just happened to land differently. So now the backtest runs again the moment I save, and it tells me which trades changed. Using it On your machine: pip install -U hawk-bt hawk-bt run my_strategy.py A strategy looks like this. Anything declared with Param shows up in the browser as a slider. from hawk_bt import Strategy , Context , Param class MaCross ( Strategy ): fast = Param ( 10 , min = 3 , max = 50 , step = 1 ) slow = Param ( 50 , min = 10 , max = 200 , step = 5 ) async def step ( self , ctx : Context ) -> None : snap = ctx . state . snapshot close = ctx . state . candles . close [: int ( snap . step )] # last element is the current bar if len ( close ) < self . slow + 1 : return fast , slow = close [ - self . fast :]. mean (), close [ - self . slow :]. mean () prev_fast , prev_slow = close [ - self . fast - 1 : - 1 ]. mean (), close [ - self . slow - 1 : - 1 ]. mean () if prev_fast <= prev_slow and fast > slow : side = " buy " elif prev_fast >= prev_slow and fast < slow : side = " sell " else : return price = float ( close [ - 1 ]) await ctx . engine . place_ticket ( side = side , units = int ( snap . equity / price ), take_profit = price * 0.01 , stop_loss = price * 0.005 ) In the browser you pick a dataset and press "Connect to Local Strategy" once. After that you just go back to your editor and save. Moving a slider also re-runs your local Python with the new value. The diff sits above the results. When I changed the take profit from 1% to 2% and saved, it said: trades 60→60, added 0, removed 0, changed 20, PnL +406.55. Same number of trades, but 20 of them ended differently, and about half of those 20 actually got worse. If I'd only looked at the total I would have called it "a bit better" and moved on. How it's put together The execution engine is C++ compiled to WebAssembly and runs in the browser. Your strategy runs in your own Python process and talks to the browser over a localhost websocket, so the strategy code is never uploaded. I decided that early, because I wouldn't want to upload my own strategies to somebody's server either. The watch part is simple. hawk-bt run polls the file's mtime, reloads the module when it changes, and asks the browser to start a new run. On each run, Python sends the strategy name and its Param definitions, and the browser answers with the current slider values. For the diff, trades from the previous run and the new run are matched on entry time and side. One bug took me a while. The browser sometimes received the trade log for the same run twice, treated the second copy as "the next run", and every diff came out as zero. Tagging each run with an ID and ignoring repeats fixed it. Two other things in the same screen You can pick two parameters, sweep the grid, and look at it as a heatmap. The single best cell is easy to overfit, so the average of its neighbours is shown next to it. In this example the best cell is +17.01%, but its neighbours average +9.31%. The left column (10-bar lookback) is around +15% for every take profit, so the lookback matters much more than the TP here. There's also a button that sends the aggregated numbers to an LLM and gets back what to look at and what to try next. Only the aggregates go out, not your code or raw data, and it's told not to give trading advice. In the run above it picked up the diff too, and its first suggested experiment was to work out why 20 trades changed before comparing the two versions. Limits One instrument per backtest. Bar data only, no ticks. When TP and SL are both touched inside one bar it assumes the stop came first. Portfolio support is what I'm working on next. Trying it Honestly almost nobody uses this yet, so even a short "I tried it and X was confusing" helps a lot. There's a demo that needs no account (synthetic data). Demo: https://app.hawk-backtester.com/en/demo/?utm_source=devto&utm_medium=article&utm_campaign=watch_mode App: https://app.hawk-backtester.com/en/?utm_source=devto&utm_medium=article&utm_campaign=watch_mode (free plan) What would you want the diff to show that it doesn't yet?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hawkbtcommander/my-backtest-re-runs-when-i-save-the-strategy-file-and-shows-which-trades-changed-13cd

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
