---
title: "FROST 的治理哲学：为什么每个 Agent 系统都需要一部宪法"
slug: "frost-agent"
author: "llimage"
source: "devto_python"
published: "Mon, 06 Jul 2026 03:23:52 +0000"
description: "FROST 的治理哲学：为什么每个 Agent 系统都需要一部宪法 "细胞会死，但谱系会存续。Agent 会消亡，但宪法会传承。资产会永存。" 在 AI Agent 框架百花齐放的 2026 年，我们见证了一个有趣的现象：框架越来越多，治理却越来越缺失。LangChain 给了你工具链，CrewAI 给了你角色扮..."
keywords: "agent, frost, self, sop, store, key, generation, def"
generated: "2026-07-06T04:05:09.365530"
---

# FROST 的治理哲学：为什么每个 Agent 系统都需要一部宪法

## Overview

FROST 的治理哲学：为什么每个 Agent 系统都需要一部宪法 "细胞会死，但谱系会存续。Agent 会消亡，但宪法会传承。资产会永存。" 在 AI Agent 框架百花齐放的 2026 年，我们见证了一个有趣的现象：框架越来越多，治理却越来越缺失。LangChain 给了你工具链，CrewAI 给了你角色扮演，AutoGen 给了你对话——但没有人回答一个关键问题： 当你的 Agent 家族有十代、百代，谁来保证它们的行为不越界？ 这就是 FROST 要解决的问题。 一、一个被忽视的问题：Agent 治理真空 想象这样一个场景：你构建了一个 Agent 系统，它帮你处理客户咨询、自动写报告、管理财务。一开始只有 3 个 Agent，你都能监控。三个月后，Agent 数量变成了 30 个——有些是你创建的，有些是 Agent 自己创建的。 问题来了： 某个 Agent 开始访问不该访问的数据 某个 Agent 创建的子 Agent 继承了一份不该继承的权限 某个 SOP 工作流在运行中被人悄悄修改了 这不是科幻场景，这是今天 Agent 系统正在发生的事。 根本原因 ：现有框架的"治理"要么是提示词级别的软约束（"请你不要访问这些数据"），要么是事后的日志审计。没有一个是代码级别、架构级别的硬约束。 FROST 的设计哲学是： 治理必须是架构的一部分，而不是补丁。 二、FROST 的宪法模型：四层治理 FROST 把治理拆解为四个层次，每一层都有对应的代码实现： 第一层：只读继承——权限的代码级强制 在大多数框架中，Agent 之间的数据共享靠的是"约定"。FROST 用的是 HierarchicalStore ——一种层级化记忆容器： class HierarchicalStore : """ 层级化记忆存储。 祖先 Store 对后代只读——后代可以继承，但不能篡改。 """ def __init__ ( self , data = None , parent = None , readonly = False ): self . _data = data or {} self . _parent = parent self . _readonly = readonly # 关键：只读标记 def save ( self , key , value ): if self . _readonly : raise PermissionError ( " 只读 Store 禁止写入 " ) self . _data [ key ] = value def load ( self , key , default = None ): if key in self . _data : return self . _data [ key ] if self . _parent : return self . _parent . load ( key , default ) return default 注意 readonly 参数。当一个 Agent 创建子 Agent 时，子 Agent 对父 Agent 的 Store 是 只读的 。这不是提示词告诉 Agent "请你不要修改"，而是代码直接抛出异常。 这意味着 ：即使 LLM 产生了幻觉，试图越权写入，代码层面也会拒绝执行。 第二层：SOP 宪法校验——工作流的可审计性 在 FROST 中，SOP 不是随便定义的步骤列表，而是经过祖辈审核的"宪法文本"： def validate_sop ( ancestor_sop , descendant_sop ): """ 祖辈验证后代的 SOP 是否合规。 检查点： 1. 后代 SOP 的步骤不能超出祖辈定义的边界 2. 后代 SOP 不能调用未授权的 Skill 3. 后代 SOP 的数据访问不能超出权限范围 """ # 检查 1：步骤边界 for step in descendant_sop . steps : if step not in ancestor_sop . allowed_steps : raise SOPValidationError ( f " 步骤 { step } 超出祖辈定义的边界 " ) # 检查 2：Skill 授权 for skill in descendant_sop . required_skills : if skill not in ancestor_sop . authorized_skills : raise SOPValidationError ( f " Skill { skill } 未获授权 " ) return True 这意味着 ：任何后代 Agent 想要执行的工作流，都必须通过祖辈的审核。这不是事后审计，而是事前拦截。 第三层：代数限制——防止越级生成 FROST 的家族模型定义了三层角色：祖辈（治理）、父辈（协调）、孙辈（执行）。关键的是，代数不能越级： class Agent : def __init__ ( self , name , store , skills , generation = 0 , max_spawn_generation = 3 ): self . name = name self . generation = generation self . max_spawn_generation = max_spawn_generation # 最大代数限制 def spawn_child ( self , child_name , child_skills ): if self . generation >= self . max_spawn_generation : raise GenerationError ( f " Agent { self . name } (第 { self . generation } 代) " f " 已达到最大生成代数限制( { self . max_spawn_generation } ) " ) # 创建子 Agent，代数 +1 return Agent ( name = child_name , store = HierarchicalStore ( parent = self . store , readonly = True ), skills = child_skills , generation = self . generation + 1 , max_spawn_generation = self . max_spawn_generation ) 这意味着 ：Agent 不能无限递归生成子 Agent。每一代的权限都会收窄，数据访问都会受限。 第四层：选择性持久化——只有经过审核的输出才能传承 在 FROST 中，Agent 的执行结果是 瞬态的 ——Agent 执行完毕即消亡，但经过父辈审核的输出会被保留： def merge_from ( parent_store , child_output ): """ 父辈从子 Agent 的输出中选择性地保留有价值的内容。 这是一个显式的、可审计的决策过程。 """ for key , value in child_output . items (): if parent_store . approves ( key , value ): # 显式审核 parent_store . save ( key , value ) else : log_discard ( key , value ) # 记录丢弃决策 这意味着 ：不是所有 Agent 产出都会自动成为系统记忆。每一次数据的保留都是经过审核的、有记录的。 三、与主流框架的治理对比 治理能力 LangChain CrewAI FROST 数据权限边界 无限制 提示词建议 代码强制只读 工作流审核 无 无 祖辈宪法校验 代数控制 无限递归 固定角色 显式代数限制 输出继承 全部保留 对话日志 选择性持久化 审计追溯 链式日志 对话历史 结构化决策记录 这张表不是要贬低其他框架——它们在各自的场景下做得很好。但如果你要构建一个 需要长期运行、需要合规审计、需要权限控制 的 Agent 系统，FROST 的治理模型是目前唯一在架构层面提供解决方案的框架。 四、一个真实的治理场景 让我们看一个完整的例子——如何用 FROST 构建一个有治理结构的客服 Agent 家族： from core import Store , Agent , SOP from core.governance import HierarchicalStore , validate_sop # 第一步：定义祖辈宪法 constitution = { " data_boundary " : [ " customer_info " , " product_catalog " ], " authorized_skills " : [ " search_product " , " generate_reply " , " escalate " ], " max_generation " : 3 } # 第二步：创建祖辈 Agent ancestor_store = Store ( data = { " constitution " : constitution }) ancestor = Agent ( " grandparent " , ancestor_store , skills = {}, generation = 0 ) # 第三步：创建父辈 Agent（继承祖辈 Store，只读） parent_store = HierarchicalStore ( parent = ancestor_store , readonly = True ) parent = Agent ( " coordinator " , parent_store , skills = { " search_product " : search_product }, generation = 1 ) # 第四步：创建孙辈 Agent（继承父辈 Store，只读） child_store = HierarchicalStore ( parent = parent_store , readonly = True ) child = Agent ( " executor " , child_store , skills = { " generate_reply " : generate_reply }, generation = 2 ) # 第五步：定义并验证 SOP customer_sop = SOP ( name = " handle_customer_inquiry " , steps = [ " search_product " , " generate_reply " ], required_skills = [ " search_product " , " generate_reply " ] ) # 宪法校验 try : validate_sop ( ancestor_sop = ancestor . define_sop ( constitution ), descendant_sop = customer_sop ) print ( " ✅ SOP 合规，可以执行 " ) except SOPValidationError as e : print ( f " ❌ SOP 不合规: { e } " ) 在这个例子中： 祖辈定义了数据边界和授权技能 父辈和孙辈只能只读继承祖辈的宪法 每一个 SOP 都需要通过宪法校验 每一代的权限都收窄 五、为什么这很重要？ Agent 治理不是一个"以后再说"的问题。当你开始把 Agent 部署到生产环境，你会发现： 没有治理 = 没有可控性 ：你无法回答"这个 Agent 为什么做了这个决策" 没有治理 = 没有合规性 ：在 GDPR 等法规下，你必须能解释 AI 的每一个行为 没有治理 = 没有可扩展性 ：Agent 数量增长后，你无法手动监控每一个 FROST 的治理哲学是： 把约束写在代码里，而不是写在提示词里。 结语：Agent 需要宪法，正如社会需要法律 FROST 不是一个"更好的"Agent 框架。它是一个 不同维度的 Agent 框架。 当其他框架在思考"如何让 Agent 更聪明"时，FROST 在思考"如何让 Agent 更可控"。 当其他框架在追求"更多的功能"时，FROST 在追求"更深的治理"。 这不是非此即彼的选择——最好的 Agent 系统既聪明又可控。FROST 要填补的，正是那个被忽视的"可控"维度。 如果你正在构建一个需要治理的 Agent 系统，不妨来看看 FROST。 FROST：让智能体拥有谱系、记忆和荣誉感。 相关链接 ： 📦 FROST（教学框架）： https://gitee.com/liao_liang_7514/frost 🔧 FROST-SOP（工程平台）： https://gitee.com/liao_liang_7514/frost-sop 📄 FROST 白皮书： https://gitee.com/liao_liang_7514/frost/blob/main/WHITEPAPER.md 标签 ：#Python #Agent #AI #开源 #FROST #Agent治理

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/llimage/frost-de-zhi-li-zhe-xue-wei-shi-yao-mei-ge-agent-xi-tong-du-xu-yao-bu-xian-fa-1dcg

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
