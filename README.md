# PC-market-skill

**English** | [简体中文](README.zh-CN.md)

An Agent Skill for **deep PC market research**. Instead of generating a market report from model intuition, it follows a traceable evidence workflow and produces a **sourced list of market factors ranked by importance and confidence**.

## Research scope and workflow

Covers laptops, desktops, workstations, commercial PCs, consumer PCs, and AI PCs. Research lanes include demand, supply, cost, technology, competition, macro, channel, policy, and product lifecycle.

```text
Parse scope → Decompose research lanes → Search the web → Screen sources → Read source pages
→ Extract candidate claims → Merge into factors → Rank importance and confidence → Discard weak claims
```

## Repository structure

```text
PC-market-skill/
├── .gitignore
├── README.md
├── README.zh-CN.md
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

## Requirements and installation

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

## Usage and output

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

## Evidence rules

- Every final factor needs at least one source URL whose page content has been fetched and read. Search snippets are for discovery, not final evidence.
- Sources are graded A/B/C/D; D-grade sources are excluded from final evidence.
- High-importance factors should have two independent sources, or one highly authoritative source with appropriate caveats.
- Separate vendor statements from independent evidence. Label forecasts as forecasts and preserve conflicts as counter-evidence or caveats.
- Record unknown dates as `unknown`; do not invent dates or missing information.
- Move unverifiable, weakly supported, or out-of-scope claims to `discardedClaims` or a low-confidence section rather than presenting them as established conclusions.

## References

- [Skill entry point and full workflow](skills/deep-pc-market-research/SKILL.md)
- [PC market taxonomy and search vocabulary](skills/deep-pc-market-research/references/pc-market-taxonomy.md)
- [Source quality, importance, and confidence rules](skills/deep-pc-market-research/references/source-quality.md)
- [Markdown / JSON output specification](skills/deep-pc-market-research/references/output-schema.md)
- [JSON validator](skills/deep-pc-market-research/scripts/validate_factor_json.py)
