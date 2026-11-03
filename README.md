# PC-market-skill

[中文](#中文) | [English](#english)

## 中文

面向 **PC 市场深度调研** 的 Agent Skill。它将调研编排为可追溯的证据工作流，而不是让模型凭常识生成市场报告，最终输出**带来源、按重要性和置信度排序的市场因子清单**。

### 调研范围与工作流

覆盖笔记本、台式机、工作站、商用 PC、消费 PC 和 AI PC；可分析需求、供给、成本、技术、竞争、宏观、渠道、政策和产品生命周期等维度。

```text
解析调研范围 → 拆分市场维度 → 网络检索 → 筛选来源 → 阅读来源正文
→ 抽取候选说法 → 合并为市场因子 → 评估重要性与置信度 → 剔除弱证据说法
```

### 目录结构

```text
PC-market-skill/
├── .gitignore
├── README.md
└── skills/
    └── deep-pc-market-research/
        ├── SKILL.md
        ├── references/
        │   ├── pc-market-taxonomy.md
        │   ├── source-quality.md
        │   └── output-schema.md
        └── scripts/
            └── validate_factor_json.py
```

### 运行要求与安装

- 使用能够加载 `SKILL.md` 的 Agent 环境；技能识别方式和目录位置以该环境的配置为准。
- 当前技能按 nanobot 的 `web_search` / `web_fetch` 接口编写。其他 Agent 需提供兼容接口，或适配技能中的工具调用说明；仅复制目录不保证工具兼容。
- 运行 JSON 校验脚本建议使用 Python 3.10+，无需第三方 Python 包。

先克隆仓库并进入仓库根目录：

```bash
git clone git@github.com:CarlYuHQ/PC-market-skill.git
cd PC-market-skill
```

将整个技能目录复制到 Agent 配置的 skills 目录。请把下面的路径替换为实际目录：

```bash
AGENT_SKILLS_DIR="/path/to/your/agent/skills"
mkdir -p "$AGENT_SKILLS_DIR"
cp -r skills/deep-pc-market-research "$AGENT_SKILLS_DIR/"
```

安装后的结构应为 `<skills 目录>/deep-pc-market-research/SKILL.md`。确认 Agent 已加载该技能，并且搜索、网页读取工具可用。

### 使用与输出

向已加载技能的 Agent 提出调研问题，例如：

```text
影响未来 12-24 个月全球 PC 市场与 AI PC 采用率的关键驱动因素是什么？
```

默认输出 Markdown，包含调研范围与假设、执行摘要、排序后的因子、逐因子证据、反证与限制、被剔除或低置信度的说法，以及方法说明。

需要结构化结果时，可要求：

```text
请按技能的 output-schema 输出 JSON，并保留逐因子的证据和 discardedClaims。
```

在仓库根目录校验生成的 JSON：

```bash
python3 skills/deep-pc-market-research/scripts/validate_factor_json.py output.json
```

校验脚本检查字段结构、枚举值、证据覆盖和 HTTP(S) URL 格式；它**不检查网页是否可访问，也不验证来源是否真正支持结论**。结构错误须修复，警告须审阅并在结果中说明。

### 证据规则

- 每个最终因子必须至少有一个已读取正文的来源 URL；搜索摘要仅用于发现来源，不能作为最终证据。
- 来源按 A/B/C/D 分级，D 级来源不进入最终证据。
- 高重要性因子应有两个独立来源，或一个高度权威来源并附必要限制说明。
- 区分厂商自述与独立证据；预测须标明为预测，冲突须保留为反证或限制。
- 未知日期写为 `unknown`，不编造时间或缺失信息。
- 无法核验、证据过弱或不符合调研范围的说法进入 `discardedClaims` 或低置信度部分，不包装成确定结论。

### 详细参考

- [技能入口与完整工作流](skills/deep-pc-market-research/SKILL.md)
- [PC 市场分类与检索词](skills/deep-pc-market-research/references/pc-market-taxonomy.md)
- [来源质量、重要性与置信度规则](skills/deep-pc-market-research/references/source-quality.md)
- [Markdown / JSON 输出规范](skills/deep-pc-market-research/references/output-schema.md)
- [JSON 校验脚本](skills/deep-pc-market-research/scripts/validate_factor_json.py)

---

## English

An Agent Skill for **deep PC market research**. Instead of generating a market report from model intuition, it follows a traceable evidence workflow and produces a **sourced list of market factors ranked by importance and confidence**.

### Research scope and workflow

Covers laptops, desktops, workstations, commercial PCs, consumer PCs, and AI PCs. Research lanes include demand, supply, cost, technology, competition, macro, channel, policy, and product lifecycle.

```text
Parse scope → Decompose research lanes → Search the web → Screen sources → Read source pages
→ Extract candidate claims → Merge into factors → Rank importance and confidence → Discard weak claims
```

### Repository structure

```text
PC-market-skill/
├── .gitignore
├── README.md
└── skills/
    └── deep-pc-market-research/
        ├── SKILL.md
        ├── references/
        │   ├── pc-market-taxonomy.md
        │   ├── source-quality.md
        │   └── output-schema.md
        └── scripts/
            └── validate_factor_json.py
```

### Requirements and installation

- An agent environment that can load `SKILL.md`. Skill discovery and directory locations depend on the agent's configuration.
- The current skill targets nanobot's `web_search` / `web_fetch` interfaces. Other agents need compatible interfaces or adaptations to the skill's tool-call instructions; copying the directory alone does not guarantee compatibility.
- Python 3.10+ is recommended for the JSON validator. No third-party Python packages are required.

Clone the repository and enter its root directory:

```bash
git clone git@github.com:CarlYuHQ/PC-market-skill.git
cd PC-market-skill
```

Copy the complete skill directory into your agent's configured skills directory. Replace the path below with the actual location:

```bash
AGENT_SKILLS_DIR="/path/to/your/agent/skills"
mkdir -p "$AGENT_SKILLS_DIR"
cp -r skills/deep-pc-market-research "$AGENT_SKILLS_DIR/"
```

The installed layout should be `<skills directory>/deep-pc-market-research/SKILL.md`. Confirm that the agent has loaded the skill and that its search and page-fetch tools are available.

### Usage and output

Ask an agent with the skill loaded a research question, for example:

```text
What are the key drivers of the global PC market and AI PC adoption over the next 12-24 months?
```

The default output is Markdown: scope and assumptions, an executive summary, ranked factors, evidence per factor, counter-evidence and caveats, discarded or low-confidence claims, and method notes.

For structured output, request:

```text
Return JSON following the skill's output-schema, retaining evidence per factor and discardedClaims.
```

Validate the generated JSON from the repository root:

```bash
python3 skills/deep-pc-market-research/scripts/validate_factor_json.py output.json
```

The validator checks field structure, enum values, evidence coverage, and HTTP(S) URL formatting. It **does not check page accessibility or verify that a source actually supports a claim**. Fix structural errors, review warnings, and explain any remaining warnings in the result notes.

### Evidence rules

- Every final factor needs at least one source URL whose page content has been fetched and read. Search snippets are for discovery, not final evidence.
- Sources are graded A/B/C/D; D-grade sources are excluded from final evidence.
- High-importance factors should have two independent sources, or one highly authoritative source with appropriate caveats.
- Separate vendor statements from independent evidence. Label forecasts as forecasts and preserve conflicts as counter-evidence or caveats.
- Record unknown dates as `unknown`; do not invent dates or missing information.
- Move unverifiable, weakly supported, or out-of-scope claims to `discardedClaims` or a low-confidence section rather than presenting them as established conclusions.

### References

- [Skill entry point and full workflow](skills/deep-pc-market-research/SKILL.md)
- [PC market taxonomy and search vocabulary](skills/deep-pc-market-research/references/pc-market-taxonomy.md)
- [Source quality, importance, and confidence rules](skills/deep-pc-market-research/references/source-quality.md)
- [Markdown / JSON output specification](skills/deep-pc-market-research/references/output-schema.md)
- [JSON validator](skills/deep-pc-market-research/scripts/validate_factor_json.py)
