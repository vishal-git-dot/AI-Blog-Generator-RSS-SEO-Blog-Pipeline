---
title: "Python股票实时价格告警系统：WebSocket订阅与REST快照实战"
slug: "pythonwebsocketrest"
author: "San Si wu"
source: "devto_python"
published: "Sun, 13 Sep 2026 10:34:59 +0000"
description: "昨晚美股盘前，我想给自己盯的几只票加个简单的告警：涨跌幅超过3%就推个消息到手机上。需求很简单对吧？但真坐下来写，从"拿数据"到"告警能跑"，前前后后踩了不少坑。这篇就顺着整个过程聊聊，顺便把股票行情接口的接法讲清楚。 先说背景。最近这波行情板块分化得厉害，半导体整体在涨但存储芯片在跌，同一个板块里个股走势都能反..."
keywords: "json, code, get, data, time, chp, headers, stock"
generated: "2026-09-13T11:28:47.306247"
---

# Python股票实时价格告警系统：WebSocket订阅与REST快照实战

## Overview

昨晚美股盘前，我想给自己盯的几只票加个简单的告警：涨跌幅超过3%就推个消息到手机上。需求很简单对吧？但真坐下来写，从"拿数据"到"告警能跑"，前前后后踩了不少坑。这篇就顺着整个过程聊聊，顺便把股票行情接口的接法讲清楚。 先说背景。最近这波行情板块分化得厉害，半导体整体在涨但存储芯片在跌，同一个板块里个股走势都能反着来。光看指数完全没用，必须盯到个股。我盯的就是苹果、英伟达、AMD、英特尔这几只，量不大，但盘中波动的时候手动刷新实在受不了。 REST轮询方案及其局限性 一开始我的思路特别直接：写个脚本，每隔5秒请求一次报价接口，跟3%的阈值比一下，超了就告警。听起来没毛病。 import requests , time API_BASE = " https://api.itick.org " headers = { " accept " : " application/json " , " token " : " your_token " } def get_price ( code ): r = requests . get ( f " { API_BASE } /stock/quote " , headers = headers , params = { " region " : " US " , " code " : code }) return r . json ()[ " data " ] while True : q = get_price ( " AAPL " ) print ( q [ " ld " ], q [ " chp " ]) time . sleep ( 5 ) 跑了一下，能出数。但很快发现两个问题：第一，5秒轮询在盘前或者波动剧烈的时候太慢了，价格可能已经跳了好几个点你才看到；第二，每次都要等网络请求回来才能拿新数据，CPU是不忙但延迟不好控。 这时候才想起来，人家有WebSocket，专门干这个的。 WebSocket实时订阅：鉴权握手与心跳保活 WebSocket的文档我看了一眼，地址是 wss://api.itick.org/stock ，token放Header里。我照着写了个最小连接： import websocket , json ws = websocket . WebSocketApp ( " wss://api.itick.org/stock " , header = [ " token: your_token " ], on_open = lambda ws : ws . send ( json . dumps ({ " ac " : " subscribe " , " params " : " AAPL$US " , " types " : " quote " })), on_message = lambda ws , msg : print ( msg ), ) ws . run_forever () 结果一跑，服务端回了个 cannot be resolved action 。我当时就懵了——格式看着跟文档一样啊。 翻了文档才看到那个容易被忽略的细节：连接建立成功和可以订阅是两回事。服务端先回一句 Connected Successfully ，这时候你什么都不能做；必须等它再推一条 resAc: "auth" 且 code: 1 的消息，才代表鉴权通过，这时候发订阅才有效。 我之前写了太多"连上就能用"的WebSocket接口，差点忘了这个服务端是要做鉴权握手的。改了一下： authenticated = False def on_open ( ws ): print ( " 连接已建立 " ) # 注意：这时候还不能订阅！ def on_message ( ws , message ): global authenticated payload = json . loads ( message ) # 必须等这条鉴权成功消息 if payload . get ( " resAc " ) == " auth " and payload . get ( " code " ) == 1 and not authenticated : authenticated = True ws . send ( json . dumps ({ " ac " : " subscribe " , " params " : " AAPL$US,NVDA$US " , " types " : " quote " })) return 这下终于收到数据了。但没高兴两秒，连接过了一分钟就断了。 又是文档里写了但我没仔细看的：这个服务端要求30秒发一次心跳，超过1分钟不发就踢人。加个线程专门发ping： import threading , time def heartbeat ( ws ): while True : time . sleep ( 30 ) ws . send ( json . dumps ({ " ac " : " ping " , " params " : str ( int ( time . time () * 1000 )) })) # 鉴权成功后启动 threading . Thread ( target = heartbeat , args = ( ws ,), daemon = True ). start () 到这一步，实时报价终于稳定跑起来了。 返回字段解析与交易状态处理 数据能收到了，但解析的时候又踩了坑。返回的JSON长这样： { "code" : 1 , "data" : { "s" : "AAPL" , "ld" : 225.215 , "o" : 226.27 , "p" : 226.27 , "h" : 226.92 , "l" : 224.44 , "ch" : -3.24 , "chp" : -1.17 , "v" : 16742235 , "ts" : 0 , "type" : "quote" } } 全是缩写。我第一反应是 ld 是什么？ chp 又是什么？翻文档才搞清楚： ld = 最新价（last price） p = 前收盘价（previous close） ch = 涨跌额（change） chp = 涨跌幅百分比（change percent） ts = 交易状态，0正常、1停牌、2退市、3熔断 这里有个特别坑的地方：我一开始算涨跌幅的时候，偷懒用了 (ld - o) / o ，也就是拿最新价跟开盘价比。跑出来发现告警触发得特别频繁——因为开盘后前几分钟波动本来就大。后来才反应过来，涨跌幅应该跟前收盘比，服务端已经在 chp 里算好了，直接用就行。 还有一个 ts 字段。有次我挂着告警跑了一晚上，第二天发现某只停牌的票一直在触发告警——因为 ld 停留在昨天的价格，而我的脚本没有检查 ts 。加个判断就好了： if data . get ( " ts " ) == 1 : continue # 停牌，跳过 REST历史K线查询与技术指标计算 告警的事搞完了，又想多做一步：打开脚本的时候先显示一下这几只票近30天的走势，让我对当前位置有个感觉。这就需要拉历史K线。 K线接口跟报价是分开的，路径是 /stock/kline ，注意是单数 stock 不是复数 stocks ——这个我也踩了，一开始写 /stocks/kline 直接404。 def get_kline ( region , code , k_type = 8 , limit = 30 ): """ k_type: 8=日K 其他: 1=1分 2=5分 5=1时 9=周 10=月 """ r = requests . get ( f " { API_BASE } /stock/kline " , headers = headers , params = { " region " : region , " code " : code , " kType " : k_type , " limit " : limit } ) return r . json ()[ " data " ] klines = get_kline ( " US " , " AAPL " , k_type = 8 , limit = 30 ) for bar in klines [ - 5 :]: # 每根K线: t=时间戳 o/h/l/c/v/tu print ( bar [ " t " ], bar [ " o " ], bar [ " c " ]) 返回的是一个数组，每根K线就七个字段，干净利落。用这个算个简单的均线或者波动率，比从行情软件截图方便多了。 完整告警系统：REST初始化与WebSocket增量推送 把REST初始化和WebSocket拼一起，就是最终能跑的告警脚本： import json , threading , time , requests , websocket API_BASE = " https://api.itick.org " WS_URL = " wss://api.itick.org/stock " TOKEN = " your_token_here " headers = { " accept " : " application/json " , " token " : TOKEN } watchlist = [ " AAPL " , " NVDA " , " AMD " , " INTC " ] THRESHOLD = 3.0 # 涨跌幅超过3%告警 # 启动时先拉一遍快照做基线 print ( " === 盘前快照 === " ) for code in watchlist : q = requests . get ( f " { API_BASE } /stock/quote " , headers = headers , params = { " region " : " US " , " code " : code }). json ()[ " data " ] print ( f " { code } : 前收= { q [ ' p ' ] } 最新= { q [ ' ld ' ] } " ) # WebSocket盯盘 authenticated = False def on_message ( ws , message ): global authenticated payload = json . loads ( message ) if payload . get ( " resAc " ) == " auth " and payload . get ( " code " ) == 1 and not authenticated : authenticated = True ws . send ( json . dumps ({ " ac " : " subscribe " , " params " : " , " . join ( f " { c } $US " for c in watchlist ), " types " : " quote " })) threading . Thread ( target = heartbeat , args = ( ws ,), daemon = True ). start () return data = payload . get ( " data " ) or {} if data . get ( " type " ) != " quote " : return if data . get ( " ts " ) != 0 : # 非交易状态不告警 return chp = data . get ( " chp " , 0 ) if abs ( chp ) >= THRESHOLD : print ( f " [告警] { data [ ' s ' ] } : 涨跌幅 { chp } % 超过阈值! " ) def heartbeat ( ws ): while True : time . sleep ( 30 ) ws . send ( json . dumps ({ " ac " : " ping " , " params " : str ( int ( time . time () * 1000 ))})) ws = websocket . WebSocketApp ( WS_URL , header = [ f " token: { TOKEN } " ], on_message = on_message ) ws . run_forever () 跑起来之后，开盘前先看到一组基线，盘中有股票涨跌超过3%就立刻打印告警。整个过程没用到任何框架，依赖就两个。 生产部署注意事项 回头看，整个接入过程的技术点其实不多，但容易踩的坑全在细节里：连接不等于鉴权、必须等auth消息才能订阅、30秒心跳不能忘、字段全是缩写别想当然、交易状态要检查。这些东西文档里都写了，但第一次看的时候很容易扫过去，真跑起来才会一个个撞上。 做监控工具这种东西，稳定性比功能多重要。我现在挂着这个脚本跑了一阵，WebSocket断了会自动重连（websocket-client的run_forever自带），告警逻辑也加了去重，基本上不用管了。 最近这行情波动大，有个自己写的监控脚本比来回切行情软件省心多了。接口文档可以在 这里 看，有其他市场的接入方式也类似。官网地址 https://itick.org

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/san_siwu_f08e7c406830469/pythongu-piao-shi-shi-jie-ge-gao-jing-xi-tong-websocketding-yue-yu-restkuai-zhao-shi-zhan-5gjh

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
