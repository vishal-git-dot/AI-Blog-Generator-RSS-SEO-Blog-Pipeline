---
title: "Python印度股票API接入：NSE/BSE行情数据与实时订阅实战"
slug: "pythonapinsebse"
author: "San Si wu"
source: "devto_python"
published: "Sat, 10 Oct 2026 11:37:20 +0000"
description: "最近不少朋友在做新兴市场的量化策略，印度股市是绕不开的一个。NSE（印度国家证券交易所）和BSE（孟买证券交易所）的市值加起来排全球前列，而且增长速度快，很多策略在印度市场的表现跟美股完全不一样。 但接印度股票数据的时候，有几个跟美股、港股都不一样的地方——尤其是订阅格式和交易所指定。这篇记录一下接入印度股票行情..."
keywords: "nse, data, code, exchange, get, json, reliance, payload"
generated: "2026-10-10T12:13:29.602947"
---

# Python印度股票API接入：NSE/BSE行情数据与实时订阅实战

## Overview

最近不少朋友在做新兴市场的量化策略，印度股市是绕不开的一个。NSE（印度国家证券交易所）和BSE（孟买证券交易所）的市值加起来排全球前列，而且增长速度快，很多策略在印度市场的表现跟美股完全不一样。 但接印度股票数据的时候，有几个跟美股、港股都不一样的地方——尤其是订阅格式和交易所指定。这篇记录一下接入印度股票行情的全过程。 印度市场跟其他市场有什么不一样 刚开始接的时候我以为跟美股一样，直接传个代码和region就行，结果发现根本不是那么回事。 第一，印度有两个主要交易所：NSE和BSE。 同一只股票在两个交易所都可能上市，代码一样但交易所不同。所以接印度股票的时候，必须指定交易所，不然返回的数据可能不是你想要的那个。 第二，WebSocket订阅格式不一样。 美股是两个参数： AAPL$US （代码$市场）。印度是三个参数： RELIANCE$NSE$IN （代码$交易所$市场）。一开始我按美股的格式传，结果订阅一直失败。 第三，region代码是 IN 。 不是 US 、 HK 那种，印度市场传 IN 。 REST拉取印度股票报价 先从REST开始，确认数据格式对不对。 import requests API_BASE = " https://api.itick.org " TOKEN = " your_token_here " headers = { " accept " : " application/json " , " token " : TOKEN } # 拉印度股票的实时报价 def get_india_stock_quote ( code , exchange = " NSE " ): resp = requests . get ( f " { API_BASE } /stock/quote " , headers = headers , params = { " region " : " IN " , " code " : code , " exchange " : exchange } ) return resp . json ()[ " data " ] # 拉几只印度大盘股 stocks = [ ( " RELIANCE " , " NSE " ), # 信实工业 ( " TCS " , " NSE " ), # 塔塔咨询 ( " INFY " , " NSE " ), # 印孚瑟斯 ] for code , exchange in stocks : q = get_india_stock_quote ( code , exchange ) sign = " + " if q [ " chp " ] >= 0 else "" print ( f " { code } ( { exchange } ): { q [ ' ld ' ] } ( { sign }{ q [ ' chp ' ] } %) " ) 返回字段跟其他市场基本一致： ld 最新价、 chp 涨跌幅、 o/h/l 开高低、 v 成交量。做行情看板这些字段够用了。 注意 ：印度股票的代码是字母形式（RELIANCE、TCS），不是数字。跟港股的数字代码（700）不一样。 WebSocket订阅印度股票（重点） 这是印度市场最容易踩坑的地方——订阅格式跟其他市场不一样。 其他市场（美股、港股、外汇）都是两个参数： 代码$市场 ，比如 AAPL$US 。 印度市场是三个参数： 代码$交易所$市场 ，比如 RELIANCE$NSE$IN 。 import json import threading import time import websocket WS_URL = " wss://api.itick.org/stock " TOKEN = " your_token_here " authenticated = False def on_message ( ws , message ): global authenticated payload = json . loads ( message ) # 先等鉴权成功 if payload . get ( " resAc " ) == " auth " and payload . get ( " code " ) == 1 and not authenticated : authenticated = True # 印度股票订阅格式：代码$交易所$市场 ws . send ( json . dumps ({ " ac " : " subscribe " , " params " : " RELIANCE$NSE$IN,TCS$NSE$IN " , " types " : " quote " })) return if payload . get ( " resAc " ) == " pong " : return data = payload . get ( " data " ) or {} if data . get ( " type " ) == " quote " : sign = " + " if data [ " chp " ] >= 0 else "" print ( f " { data [ ' s ' ] } : { data [ ' ld ' ] } ( { sign }{ data [ ' chp ' ] } %) " ) 为什么印度要多一个交易所参数？ 因为同一只股票在NSE和BSE都可能上市，价格可能不一样。指定交易所才能确保你拿到的是你想要的那个交易所的数据。 K线数据获取 K线接口跟其他市场一样，只是多了个exchange参数。 def get_india_kline ( code , exchange = " NSE " , k_type = 8 , limit = 100 ): """ k_type: 1=1分钟 2=5分钟 5=1小时 8=日K 9=周K 10=月K """ resp = requests . get ( f " { API_BASE } /stock/kline " , headers = headers , params = { " region " : " IN " , " code " : code , " exchange " : exchange , " kType " : k_type , " limit " : limit } ) return resp . json ()[ " data " ] # 拉RELIANCE最近100根日K daily = get_india_kline ( " RELIANCE " , " NSE " , k_type = 8 , limit = 100 ) closes = [ bar [ " c " ] for bar in daily ] # 算20日均线 ma20 = sum ( closes [ - 20 :]) / 20 print ( f " RELIANCE最新收盘: { closes [ - 1 ] } , 20日均线: { ma20 : . 2 f } " ) K线返回标准OHLCV： t 时间戳、 o/h/l/c 开高低收、 v 成交量。做技术分析直接用这些字段。 印度市场接入的特殊注意事项 订阅格式别搞错。 这是最容易踩的坑。印度是三个参数： RELIANCE$NSE$IN ，不是两个参数。一开始我按美股格式传 RELIANCE$IN ，结果订阅一直失败。 交易所要指定。 印度有NSE和BSE两个交易所，同一只股票在两个交易所都可能上市。REST接口要传 exchange=NSE 或 exchange=BSE ，WebSocket订阅要在params里带上交易所代码。 交易时间跟国内不一样。 印度股市的交易时间是印度标准时间（IST），比北京时间晚2.5小时。做实时监控的时候要注意时区转换。 股票代码是字母。 印度股票代码是字母形式（RELIANCE、TCS、INFY），不是数字。跟港股的数字代码（700）不一样。 时间戳是毫秒。 所有返回的时间戳都是毫秒，直接当秒数处理会得到一个很远的未来时间，记得除以1000。 完整脚本：印度股票行情监控 把前面几块拼起来，最终的完整脚本： import json , time , threading , requests , websocket API_BASE = " https://api.itick.org " WS_URL = " wss://api.itick.org/stock " TOKEN = " your_token_here " headers = { " accept " : " application/json " , " token " : TOKEN } # 印度股票监控列表 watchlist = [ ( " RELIANCE " , " NSE " ), ( " TCS " , " NSE " ), ( " INFY " , " NSE " ), ] # 启动时拉快照 print ( " === 印度股票快照 === " ) for code , exchange in watchlist : r = requests . get ( f " { API_BASE } /stock/quote " , headers = headers , params = { " region " : " IN " , " code " : code , " exchange " : exchange }). json ()[ " data " ] sign = " + " if r [ " chp " ] >= 0 else "" print ( f " { code } ( { exchange } ): { r [ ' ld ' ] } ( { sign }{ r [ ' chp ' ] } %) " ) # WebSocket实时推送 authenticated = False def on_message ( ws , message ): global authenticated payload = json . loads ( message ) if payload . get ( " resAc " ) == " auth " and payload . get ( " code " ) == 1 and not authenticated : authenticated = True # 印度股票订阅格式：代码$交易所$市场 params = " , " . join ( f " { c } $ { e } $IN " for c , e in watchlist ) ws . send ( json . dumps ({ " ac " : " subscribe " , " params " : params , " types " : " quote " })) threading . Thread ( target = heartbeat , args = ( ws ,), daemon = True ). start () return if payload . get ( " resAc " ) == " pong " : return data = payload . get ( " data " ) or {} if data . get ( " type " ) == " quote " : sign = " + " if data [ " chp " ] >= 0 else "" print ( f " [实时] { data [ ' s ' ] } : { data [ ' ld ' ] } ( { sign }{ data [ ' chp ' ] } %) " ) def heartbeat ( ws ): while True : time . sleep ( 30 ) ws . send ( json . dumps ({ " ac " : " ping " , " params " : str ( int ( time . time () * 1000 ))})) ws = websocket . WebSocketApp ( WS_URL , header = [ f " token: { TOKEN } " ], on_message = on_message ) ws . run_forever () 这个脚本跑起来之后，开盘前先看到一组印度股票的快照，盘中实时更新价格和涨跌幅。 小结 接印度股票数据的技术框架跟美股、港股差不多——REST做快照和历史数据，WebSocket做实时推送。但有几个特殊点：订阅格式是三个参数（代码$交易所$市场）、必须指定NSE或BSE交易所、交易时间跟国内有时差。这些细节不踩一遍坑很容易忽略。 参考文档： https://docs.itick.org/websocket/stocks GitHub： https://github.com/itick-org/

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/san_siwu_f08e7c406830469/pythonyin-du-gu-piao-apijie-ru-nsebsexing-qing-shu-ju-yu-shi-shi-ding-yue-shi-zhan-4pol

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
