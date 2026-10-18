# PC-market-skill

一套面向 **PC 市场深度调研** 的 Agent Skill，用来替代「让模型凭常识写一份市场报告」的做法。

它把调研过程编排成固定的工作流：解析 scope → 拆市场维度 → 网络检索 → 筛选来源 → 阅读正文 → 抽取 candidate claims → 聚合成 factors → 评估 importance / confidence → 丢弃弱 claims，最终输出**每条结论都能回溯到来源**的因子清单。

## 目录结构

```text
PC-market-skill/
├── README.md
├── 说明文档.md                                  # 完整设计说明（流程、取舍、反幻觉策略）
├── image002.png / image003.png                  # 说明文档配图
└── skills/deep-pc-market-research/
    ├── SKILL.md                                 # Skill 入口与工作流入
    ├── references/
    │   ├── pc-market-taxonomy.md                # PC 市场维度分类与检索词
    │   ├── source-quality.md                    # 来源 A/B/C/D 分级、置信度与重要性判定
    │   └── output-schema.md                     # 输出的字段 schema
    └── scripts/
        └── validate_factor_json.py              # JSON 输出结构与 URL 校验
```

## 安装

把 `skills/deep-pc-market-research/` 整个目录复制到你所用 Agent 的 skills 目录下即可。不同 Agent 的目录位置不同，按实际路径替换：

```bash
# 通用形式：<AGENT_SKILLS_DIR> 换成你的 Agent 的 skills 目录
cp -r skills/deep-pc-market-research <AGENT_SKILLS_DIR>/

# 例：项目级 workspace
cp -r skills/deep-pc-market-research ./skills/
```

只要目标目录满足 `<skills 目录>/deep-pc-market-research/SKILL.md` 这一结构，Agent 即可通过 SKILL.md 顶部 frontmatter 的 `description` 识别并触发它。

## 使用

直接提出调研问题即可触发，例如：

```text
影响未来 12-24 个月全球 PC 市场与 AI PC 采用率的关键驱动因素是什么？
```

输出默认为 Markdown；需要结构化结果时要求输出 JSON，并用下面的脚本做质量门校验：

```bash
python skills/deep-pc-market-research/scripts/validate_factor_json.py output.json
```

## 核心约束

- 每个最终 factor 必须至少有一个已 fetch 的 URL 作为证据；
- 搜索摘要（snippet）只用于发现来源，不能作为最终证据；
- 来源分 A/B/C/D 四级，D 级不进入最终 evidence；
- 厂商自述与第三方独立证据必须区分；
- 无法核验、来源过弱或与 scope 不匹配的说法进入 `discardedClaims`，而不是包装成结论。

详细设计见 [说明文档.md](./说明文档.md)。
