# Output Schema

The skill can produce Markdown for readers or JSON for downstream programs. Use Markdown by default. Use JSON when the user asks for machine-readable output, validation, or pipeline input.

## Markdown Template

```markdown
# PC Market Factor List

## Scope And Assumptions

- Query:
- Region:
- Time window:
- Segments:
- Assumptions:

## Executive Summary

[Summarize the most important 3-5 drivers and the overall direction.]

## Ranked Factors

### F001. [Factor name]

- Category:
- Impact direction:
- Affected segments:
- Affected regions:
- Time horizon:
- Importance:
- Confidence:
- Rationale:
- Evidence:
  - [Source title](https://example.com), publisher, date: supported claim.
- Counter-evidence:
  - [Source title](https://example.com), publisher, date: conflicting claim.
- Caveats:
  - [Limitations, uncertainty, or scope mismatch.]

## Discarded Or Low-Confidence Claims

- Claim:
  - Reason:
  - Source:

## Method Notes

- Search lanes used:
- Evidence policy:
- Known limitations:
```

## JSON Schema By Convention

The JSON output should be one object:

```json
{
  "query": "string",
  "scope": {
    "region": "global | China | US | EMEA | APAC | other",
    "timeWindow": "string",
    "segments": ["consumer laptop", "commercial laptop", "desktop", "workstation", "AI PC"]
  },
  "assumptions": ["string"],
  "method": {
    "searchLanes": ["demand", "supply", "cost"],
    "sourcePolicy": "string",
    "lastVerified": "YYYY-MM-DD"
  },
  "factors": [
    {
      "id": "F001",
      "factor": "string",
      "category": "demand | supply | cost | technology | competition | macro | channel | policy | lifecycle",
      "impactDirection": "positive | negative | mixed | uncertain",
      "affectedSegments": ["string"],
      "affectedRegions": ["string"],
      "timeHorizon": "near-term | medium-term | long-term",
      "importance": "high | medium | low",
      "confidence": "high | medium | low",
      "rationale": "string",
      "evidence": [
        {
          "title": "string",
          "url": "https://example.com",
          "publisher": "string",
          "publishedDate": "YYYY-MM-DD or unknown",
          "sourceQuality": "A | B | C",
          "evidenceType": "data | quote | forecast | company statement | official statistic | news report | analysis",
          "supportedClaim": "string"
        }
      ],
      "counterEvidence": [
        {
          "title": "string",
          "url": "https://example.com",
          "publisher": "string",
          "publishedDate": "YYYY-MM-DD or unknown",
          "claim": "string"
        }
      ],
      "caveats": ["string"]
    }
  ],
  "discardedClaims": [
    {
      "claim": "string",
      "reason": "no source | weak source | contradicted | outdated | irrelevant | inaccessible | too generic",
      "sourceUrl": "https://example.com or unknown"
    }
  ]
}
```

## Allowed Values

Allowed categories:

- `demand`
- `supply`
- `cost`
- `technology`
- `competition`
- `macro`
- `channel`
- `policy`
- `lifecycle`

Allowed impact directions:

- `positive`
- `negative`
- `mixed`
- `uncertain`

Allowed importance and confidence values:

- `high`
- `medium`
- `low`

Allowed source quality values:

- `A`
- `B`
- `C`

D-grade sources should be excluded from final evidence.

## Validation Expectations

The validator checks structure and evidence coverage. It does not prove that claims are true. Human review is still required for:

- whether a source actually supports the claim
- whether the importance ranking is reasonable
- whether caveats are complete
- whether there are missing research lanes
- whether the demo answers the user's real business question
