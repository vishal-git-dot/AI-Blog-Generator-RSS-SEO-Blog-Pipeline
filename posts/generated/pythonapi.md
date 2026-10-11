---
title: "Python日本股票API接入：东证行情数据与实时订阅实战"
slug: "pythonapi"
author: "San Si wu"
source: "devto_python"
published: "Sun, 11 Oct 2026 12:01:56 +0000"
description: "最近做亚洲市场量化的朋友越来越多，日本股市是绕不开的一个——东证一部（TSE Prime）有2000多家上市公司，日均成交额排全球前三。跟美股、港股比起来，日本市场的代码体系和交易规则都不太一样，接数据的时候容易踩坑。 这篇记录一下接入日本股票行情的全过程，重点讲日本市场的代码体系和跟其他市场的差异。 日本市场的..."
keywords: "data, code, get, json, payload, token, chp, headers"
generated: "2026-10-11T12:27:52.113671"
---

# Python日本股票API接入：东证行情数据与实时订阅实战

## Overview

最近做亚洲市场量化的朋友越来越多，日本股市是绕不开的一个——东证一部（TSE Prime）有2000多家上市公司，日均成交额排全球前三。跟美股、港股比起来，日本市场的代码体系和交易规则都不太一样，接数据的时候容易踩坑。 这篇记录一下接入日本股票行情的全过程，重点讲日本市场的代码体系和跟其他市场的差异。 日本市场的基本情况 日本主要的交易所是东京证券交易所（TSE），现在分三个板块：Prime（主板）、Standard（标准）、Growth（成长）。我们平时说的日经225指数和东证股价指数（TOPIX）都是从Prime板块里选的。 跟其他市场比起来，日本市场有几个特点： 第一，代码是4位数字。 跟美股的字母代码（AAPL）、港股的5位数字代码（00700）都不一样，日本股票代码是4位数字，比如7203是丰田、9984是软银、6758是索尼。 第二，交易时间是日本标准时间（JST）。 比北京时间早1小时，开盘时间是东京时间9:00-11:30（午盘前）和12:30-15:00（午盘后）。做实时监控的时候要注意时区转换。 第三，region代码是 JP 。 不是US、HK那种，日本市场传 JP 。 日本股票代码速查 先整理一下日本常见大盘股的代码，接数据的时候直接用： 代码 公司名 行业 7203 丰田汽车 汽车 9984 软银集团 综合商社 6758 索尼集团 电子 8306 三菱UFJ金融集团 银行 6861 基恩士 工业自动化 6098 Recruit Holdings 人力资源 7974 任天堂 游戏 4063 信越化学 化工 这些都是日经225指数的成分股，流动性好，数据也稳定。 REST拉取日本股票报价 先从REST开始，确认数据格式。 import requests API_BASE = " https://api.itick.org " TOKEN = " your_token_here " headers = { " accept " : " application/json " , " token " : TOKEN } # 拉日本股票的实时报价 def get_jp_stock_quote ( code ): resp = requests . get ( f " { API_BASE } /stock/quote " , headers = headers , params = { " region " : " JP " , " code " : code } ) return resp . json ()[ " data " ] # 拉几只日本大盘股 stocks = [ " 7203 " , " 9984 " , " 6758 " ] for code in stocks : q = get_jp_stock_quote ( code ) sign = " + " if q [ " chp " ] >= 0 else "" print ( f " { code } : { q [ ' ld ' ] } ( { sign }{ q [ ' chp ' ] } %) " ) 返回字段跟其他市场基本一致： ld 最新价、 chp 涨跌幅、 o/h/l 开高低、 v 成交量。做行情看板这些字段够用了。 注意 ：日本股票代码是4位数字，传参数的时候要传字符串形式（"7203"），不要传数字。 WebSocket订阅日本股票 WebSocket订阅格式跟美股一样，是两个参数： 代码$市场 。 import json import threading import time import websocket WS_URL = " wss://api.itick.org/stock " TOKEN = " your_token_here " authenticated = False def on_message ( ws , message ): global authenticated payload = json . loads ( message ) # 先等鉴权成功 if payload . get ( " resAc " ) == " auth " and payload . get ( " code " ) == 1 and not authenticated : authenticated = True # 日本股票订阅格式：代码$市场 ws . send ( json . dumps ({ " ac " : " subscribe " , " params " : " 7203$JP,9984$JP " , " types " : " quote " })) return if payload . get ( " resAc " ) == " pong " : return data = payload . get ( " data " ) or {} if data . get ( " type " ) == " quote " : sign = " + " if data [ " chp " ] >= 0 else "" print ( f " { data [ ' s ' ] } : { data [ ' ld ' ] } ( { sign }{ data [ ' chp ' ] } %) " ) 跟印度市场不一样——日本是两个参数（ 7203$JP ），不是三个参数。因为日本主要就是东证一个交易所，不需要像印度那样指定NSE/BSE。 K线数据获取 K线接口跟其他市场一样，只是region传 JP 。 def get_jp_kline ( code , k_type = 8 , limit = 100 ): """ k_type: 1=1分钟 2=5分钟 5=1小时 8=日K 9=周K 10=月K """ resp = requests . get ( f " { API_BASE } /stock/kline " , headers = headers , params = { " region " : " JP " , " code " : code , " kType " : k_type , " limit " : limit } ) return resp . json ()[ " data " ] # 拉丰田汽车近100根日K daily = get_jp_kline ( " 7203 " , k_type = 8 , limit = 100 ) closes = [ bar [ " c " ] for bar in daily ] # 算20日均线 ma20 = sum ( closes [ - 20 :]) / 20 print ( f " 7203最新收盘: { closes [ - 1 ] } , 20日均线: { ma20 : . 2 f } " ) K线返回标准OHLCV： t 时间戳、 o/h/l/c 开高低收、 v 成交量。做技术分析直接用这些字段。 日本市场接入的注意事项 代码是4位数字。 日本股票代码是4位数字（7203、9984），跟港股的5位数字（00700）、美股的字母代码（AAPL）都不一样。一开始我传了"07203"（带前导零），结果返回空数据。 交易时间跟国内差1小时。 日本标准时间（JST）比北京时间早1小时。东证开盘时间是东京时间9:00-11:30和12:30-15:00，对应北京时间8:00-10:30和11:30-14:00。做实时监控的时候要注意时区。 午间休市。 日本股市中午有1小时休市（东京时间11:30-12:30），这个时间段没有成交数据。做策略回测的时候要注意，别把午休时间当成流动性枯竭。 订阅格式是两个参数。 日本跟美股一样是两个参数（ 7203$JP ），不是印度那种三个参数。因为日本主要就是东证一个交易所。 时间戳是毫秒。 所有返回的时间戳都是毫秒，直接当秒数处理会得到一个很远的未来时间，记得除以1000。 完整脚本：日本股票行情监控 把前面几块拼起来，最终的完整脚本： import json , time , threading , requests , websocket API_BASE = " https://api.itick.org " WS_URL = " wss://api.itick.org/stock " TOKEN = " your_token_here " headers = { " accept " : " application/json " , " token " : TOKEN } # 日本股票监控列表 watchlist = [ " 7203 " , " 9984 " , " 6758 " ] # 启动时拉快照 print ( " === 日本股票快照 === " ) for code in watchlist : r = requests . get ( f " { API_BASE } /stock/quote " , headers = headers , params = { " region " : " JP " , " code " : code }). json ()[ " data " ] sign = " + " if r [ " chp " ] >= 0 else "" print ( f " { code } : { r [ ' ld ' ] } ( { sign }{ r [ ' chp ' ] } %) " ) # WebSocket实时推送 authenticated = False def on_message ( ws , message ): global authenticated payload = json . loads ( message ) if payload . get ( " resAc " ) == " auth " and payload . get ( " code " ) == 1 and not authenticated : authenticated = True params = " , " . join ( f " { c } $JP " for c in watchlist ) ws . send ( json . dumps ({ " ac " : " subscribe " , " params " : params , " types " : " quote " })) threading . Thread ( target = heartbeat , args = ( ws ,), daemon = True ). start () return if payload . get ( " resAc " ) == " pong " : return data = payload . get ( " data " ) or {} if data . get ( " type " ) == " quote " : sign = " + " if data [ " chp " ] >= 0 else "" print ( f " [实时] { data [ ' s ' ] } : { data [ ' ld ' ] } ( { sign }{ data [ ' chp ' ] } %) " ) def heartbeat ( ws ): while True : time . sleep ( 30 ) ws . send ( json . dumps ({ " ac " : " ping " , " params " : str ( int ( time . time () * 1000 ))})) ws = websocket . WebSocketApp ( WS_URL , header = [ f " token: { TOKEN } " ], on_message = on_message ) ws . run_forever () 这个脚本跑起来之后，开盘前先看到一组日本股票的快照，盘中实时更新价格和涨跌幅。 小结 接日本股票数据的技术框架跟美股差不多——REST做快照和历史数据，WebSocket做实时推送。主要区别在代码体系（4位数字）、交易时间（比国内早1小时）和午间休市。这些细节不踩一遍坑很容易忽略。 参考文档： https://docs.itick.org/websocket/stocks GitHub： https://github.com/itick-org/

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/san_siwu_f08e7c406830469/pythonri-ben-gu-piao-apijie-ru-dong-zheng-xing-qing-shu-ju-yu-shi-shi-ding-yue-shi-zhan-3ml8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
