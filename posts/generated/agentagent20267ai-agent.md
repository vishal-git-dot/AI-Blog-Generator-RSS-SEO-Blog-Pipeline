---
title: "从"造Agent"到"管Agent"：2026年7月，AI Agent行业正在经历什么？"
slug: "agentagent20267ai-agent"
author: "llimage"
source: "devto_ai"
published: "Fri, 31 Jul 2026 03:26:16 +0000"
description: "从"造Agent"到"管Agent"：2026年7月，AI Agent行业正在经历什么？ 作者 ：神通说 日期 ：2026-07-31 主题 ：行业趋势 | 周五轮换 项目 ：FROST + FROST-SOP 阅读时间 ：12分钟 2026年上半年，我们都在讨论"怎么造一个Agent"。 2026年下半年，行业..."
keywords: "frost, sop, tier, gitee, governance, agent, https, com"
generated: "2026-07-31T03:29:44.279971"
---

# 从"造Agent"到"管Agent"：2026年7月，AI Agent行业正在经历什么？

## Overview

从"造Agent"到"管Agent"：2026年7月，AI Agent行业正在经历什么？ 作者 ：神通说 日期 ：2026-07-31 主题 ：行业趋势 | 周五轮换 项目 ：FROST + FROST-SOP 阅读时间 ：12分钟 2026年上半年，我们都在讨论"怎么造一个Agent"。 2026年下半年，行业开始追问："怎么管住一群Agent？" 这个转变，在7月加速到令人窒息。 一、三件事，同一个信号 过去两周，三件看似不相关的事情同时发生： 7月15日 ，中国正式实施全球首个国家级AI Agent监管框架——《智能Agent创新应用标准化实施意见》。所有在中国部署的Agent，必须按三级决策权限分类才能"上岗"。 7月28日 ，Snowflake在Black Hat 2026发布Cortex AI Gateway——一个专门解决"Agent身份管理"的基础设施层产品。1Password、Okta、SailPoint等六大安全厂商同步宣布集成。 7月28日 ，Bain发布报告，标题开门见山： "Agentic AI has crossed a threshold that existing governance cannot handle" （Agentic AI已突破现有治理能力边界）。 三件事的共同指向： Agent治理不再是学术话题，而是产业基础设施 。 二、数字说话：Agent的"燃料消耗"已经到了什么量级？ 要理解治理为什么突然紧迫，先看一组数字。 OpenAI 2025年企业报告披露：其企业客户平均每家机构的API推理Token消耗， 一年内增长约320倍 。到2026年4月，OpenAI的API处理规模已超过 每分钟150亿Token 。 36氪在7月29日的分析更直接： "在部分长链、复杂任务中，Agent的Token消耗可能比传统聊天场景高出百倍、千倍。" 这意味着什么？ Agent不再是"偶尔问一下AI"，而是"持续不断地执行任务"。 当Agent从对话式走向执行式，它带来的风险维度也彻底改变了——不再是"说错话"，而是"做错事"。 一个读取数据库的Agent，一次提示词注入攻击，可能导致不可逆的数据泄露。 一个拥有文件写入权限的Agent，一个错误的决策链，可能覆盖关键业务文件。 一个能发送邮件的Agent，被恶意利用后，可以冒充企业身份发起钓鱼攻击。 能力边界突破的瞬间，治理就变成了刚需。 三、中国的解法：三级决策权限分类 中国7月15日生效的监管框架，核心设计非常清晰： 级别 定义 典型场景 Tier 1 仅人类可执行，不可代理 签署合同、转移资金 Tier 2 Agent提议，人类批准后执行 发送外部邮件、修改配置 Tier 3 在授权范围内自主执行，人类可随时干预 文档摘要、自动监控响应 这个分类的精髓不在于"分了几级"，而在于 它要求每个Agent在设计阶段就必须明确自己的决策边界 。 正如国际分析机构的判断： "Operators who designed their agents without formal decision-authorisation structures now face retrofit compliance costs. The practical lesson is not to comply with China's rules specifically, but to adopt tiered autonomy architecture as the default design pattern for any agent deployment, anywhere." （没有在正式决策授权结构下设计Agent的运营者，现在面临改造合规成本。实际教训不是要遵守中国的具体规则，而是将分层自治架构作为任何地方Agent部署的默认设计模式。） 换句话说： 分层自治不是中国特色，而是全球Agent工程的下一个标配 。 四、基础设施层的响应：Agent身份与治理工具链 监管只是"外驱力"。真正的产业变革，来自基础设施层的自我进化。 4.1 Agent身份管理成为刚需 Snowflake的Cortex AI Gateway做了一件事： 给每个Agent一个独立的系统身份 。 这不是一个锦上添花的功能。当企业运营数百个Agent时，审计日志里如果只记录"人类A的操作"，你根本无法追溯是哪个Agent、基于什么模型、在什么权限下执行了某个动作。 Cortex AI Gateway的核心控制维度： - 模型访问治理：哪些团队可以用哪些模型，成本上限是多少 - 工具/MCP访问：100+ MCP服务器统一接入，单端点管控 - Agent身份：独立于部署者，审计日志精确到Agent级别 - 成本控制：AI支出归属到具体团队、Agent、工作负载 六大身份管理厂商（1Password、Aembit、Cyera、Linx Security、Okta、SailPoint、Saviynt）同步宣布集成—— 这说明身份管理行业已经形成共识：Agent身份是下一个核心战场 。 4.2 微软的确定性治理路线 微软在4月开源的Agent Governance Toolkit（AGT）走了另一条路： "与其让模型'不太可能'做坏事，不如让它在结构上'不可能'做坏事。" 这个区别是范式级的。当前大多数AI Agent安全方案本质上是System Prompt + RLHF对齐——在"劝说"模型遵守规矩。但ICLR 2025的论文数据已经证明： 对GPT-4o、Claude 3、Llama-3使用自适应攻击，越狱成功率可达100% 。 AGT的选择是：在模型表达"意图"之后、动作真正执行之前，用 确定性的应用层代码 拦截每一次工具调用、每一条消息发送。被拦截的操作不是"不大可能发生"，而是 物理上不会发生 。 4.3 FROST的治理视角 这正是FROST框架从第一天就在思考的问题。 FROST的五维元模型（Weapon/任务/事件/平台/规则）中， "规则"维度 从设计之初就承担了这个职责——不是事后补救，而是在Agent的基因里嵌入治理逻辑： # FROST的治理思路：在SOP定义阶段就绑定决策权限 class GovernedSOP ( SOP ): """ 带治理属性的SOP：每个步骤都有明确的决策权限 """ steps = [ Step ( skill = analyze_data , decision_tier = Tier . AUTONOMOUS , # 数据分析：自主执行 ), Step ( skill = generate_report , decision_tier = Tier . AUTONOMOUS , # 生成报告：自主执行 ), Step ( skill = send_email , decision_tier = Tier . HUMAN_APPROVE , # 发送邮件：需人类批准 ), ] 这不是对监管的被动响应，而是 Agent工程的本征需求 。当你的Agent家族从1个增长到10个、100个，没有内建的治理机制，混乱只是时间问题。 五、行业图谱：2026年7月的Agent生态全景 让我们拉远视角，看看整个Agent开源生态正在发生什么。 根据7月27日更新的《2026年AI开发者必备：Agent开源生态图谱》，几个关键变化： Agent Skills生态爆发 obra/superpowers 单项目258k Stars 三大Skills仓库单日合计涨星近50万 "谁做出App Store for AI Skills，谁就可能定义下一个分发入口" MCP生态规模 GitHub上MCP仓库超15,900个 官方Registry登记Server近10,000个 SDK月下载9,700万次 巨头整合加速 Microsoft Agent Framework 1.0发布（Semantic Kernel + AutoGen正式合并） xAI的Grok Build正式开源（7月14日） GLM-5.2首次在agentic coding上击败GPT-5和Claude 这些数据的潜台词是：Agent的"造"已经高度成熟，行业的重心正在向"管"迁移。 六、从"造"到"管"的迁移路径 结合以上趋势，2026年下半年Agent工程的关键命题正在清晰化： 6.1 治理前置（Governance by Design） 不是先建Agent再补治理，而是 在架构设计阶段就把治理编入DNA 。 这意味着： 每个Skill定义时就要声明权限边界 每个SOP编排时就要标注决策层级 每个Agent实例化时就要绑定身份和审计策略 6.2 标准化治理协议 就像HTTP之于Web、SQL之于数据库，Agent治理也需要标准协议。 中国的三级分类是一个起点。新加坡在达沃斯发布的《智能体AI治理示范框架》提供了另一个参考。微软AGT的OPA/Cedar策略引擎走了技术实现路线。 最终的方向是：治理策略可声明、可移植、可审计、可执行。 6.3 从单体治理到家族治理 当Agent以"家族"形态运行时（一个主Agent协调多个子Agent），治理的粒度从"单个Agent的行为约束"上升到"Agent家族的协作规则"。 这正是FROST的核心定位——不是一个Agent框架，而是 Agent家族的治理框架 。 FROST 家族治理模型 ├── 祖辈（主Agent）：全局编排，战略决策 │ ├── 父辈（中层Agent）：领域专家，承上启下 │ │ ├── 子辈（执行Agent）：具体任务执行 │ │ └── 子辈（执行Agent）：具体任务执行 │ └── 父辈（中层Agent）：领域专家 │ └── ... └── 治理规则：贯穿全族的记忆、权限、审计体系 七、FROST + FROST-SOP：治理理念的工程化落地 理念的领先不等于工程的落地。FROST的治理理念，正在通过FROST-SOP工程平台转化为可执行的代码。 当前进展 FROST（教学框架） 五维元模型V5.0稳定版 197个测试用例全覆盖 家族治理模型V1.0已确认 Gitee： https://gitee.com/liao_liang_7514/frost FROST-SOP（工程平台） 执行引擎防盲飞机制 Skill系统标准化设计 初始化流水线V6.1.0 Gitee： https://gitee.com/liao_liang_7514/frost-sop 下一步 8月1日， 破局·动态能力生长实战营 正式开营。FROST将作为第一个实战案例，在15位学员的真实场景中验证"治理前置"的理念是否真的能降低Agent工程的复杂度。 这不是一次营销行为，而是一次 公开造物 ——培训系统设计的过程本身，就是FROST最好的Demo。 结语：治理不是刹车，是油门 Bain报告里有一句话，我觉得可以当作2026年下半年Agent行业的注脚： "The organizations moving fastest treat governance as the enabler of scale, not the brake." （走得最快的组织，把治理视为规模化的推动力，而不是刹车片。） 当你只有一个Agent时，治理是多余的。 当你有十个Agent时，治理是必要的。 当你有上百个Agent组成的家族时，治理是生死线。 2026年7月，行业集体走到了这个拐点。 FROST选择在这个时间点，把"治理"写进每一行代码。不是因为我们预见到了监管的到来，而是因为我们相信： 好的架构，天然就是可治理的 。 📌 FROST项目地址： https://gitee.com/liao_liang_7514/frost 📌 FROST-SOP项目地址： https://gitee.com/liao_liang_7514/frost-sop 📌 如果觉得有启发，欢迎Star支持一下，你的每一个Star都是我们持续开源的动力。 参考资料 ： 中国《智能Agent创新应用标准化实施意见》（2026年7月15日生效） Bain: Agentic AI Governance, Risk, and Controls for Business Leaders （2026-07-28） Snowflake Cortex AI Gateway @ Black Hat 2026（2026-07-28） 36氪：《下半年，垂直Agent先下牌桌？》（2026-07-29） 2026年AI开发者必备：Agent开源生态图谱（2026-07-27）

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/llimage/cong-zao-agentdao-guan-agent2026nian-7yue-ai-agentxing-ye-zheng-zai-jing-li-shi-yao--38m1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
