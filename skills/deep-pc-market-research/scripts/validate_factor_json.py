#!/usr/bin/env python3
"""Validate Deep PC Market Research JSON output.

This validator checks schema shape and evidence hygiene. It does not verify
that a source actually supports a claim; that remains a human review step.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


ALLOWED_CATEGORIES = {
    "demand",
    "supply",
    "cost",
    "technology",
    "competition",
    "macro",
    "channel",
    "policy",
    "lifecycle",
}
ALLOWED_DIRECTIONS = {"positive", "negative", "mixed", "uncertain"}
ALLOWED_LEVELS = {"high", "medium", "low"}
ALLOWED_TIME_HORIZONS = {"near-term", "medium-term", "long-term"}
ALLOWED_SOURCE_QUALITY = {"A", "B", "C"}
ALLOWED_DISCARD_REASONS = {
    "no source",
    "weak source",
    "contradicted",
    "outdated",
    "irrelevant",
    "inaccessible",
    "too generic",
}


class ValidationReport:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warning(self, message: str) -> None:
        self.warnings.append(message)


def is_http_url(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def require_string(obj: dict[str, Any], key: str, path: str, report: ValidationReport) -> None:
    value = obj.get(key)
    if not isinstance(value, str) or not value.strip():
        report.error(f"{path}.{key} must be a non-empty string")


def require_list(obj: dict[str, Any], key: str, path: str, report: ValidationReport) -> list[Any]:
    value = obj.get(key)
    if not isinstance(value, list):
        report.error(f"{path}.{key} must be a list")
        return []
    return value


def require_enum(
    obj: dict[str, Any],
    key: str,
    allowed: set[str],
    path: str,
    report: ValidationReport,
) -> None:
    value = obj.get(key)
    if value not in allowed:
        report.error(f"{path}.{key} must be one of {sorted(allowed)}, got {value!r}")


def validate_evidence_item(item: Any, path: str, report: ValidationReport) -> None:
    if not isinstance(item, dict):
        report.error(f"{path} must be an object")
        return

    for key in ("title", "url", "publisher", "publishedDate", "supportedClaim"):
        require_string(item, key, path, report)

    if not is_http_url(item.get("url")):
        report.error(f"{path}.url must be an http(s) URL")

    source_quality = item.get("sourceQuality")
    if source_quality is not None and source_quality not in ALLOWED_SOURCE_QUALITY:
        report.error(f"{path}.sourceQuality must be one of {sorted(ALLOWED_SOURCE_QUALITY)}")


def validate_counter_evidence(item: Any, path: str, report: ValidationReport) -> None:
    if not isinstance(item, dict):
        report.error(f"{path} must be an object")
        return

    for key in ("title", "url", "claim"):
        require_string(item, key, path, report)

    if not is_http_url(item.get("url")):
        report.error(f"{path}.url must be an http(s) URL")


def validate_factor(factor: Any, index: int, report: ValidationReport) -> None:
    path = f"factors[{index}]"
    if not isinstance(factor, dict):
        report.error(f"{path} must be an object")
        return

    for key in ("id", "factor", "rationale"):
        require_string(factor, key, path, report)

    require_enum(factor, "category", ALLOWED_CATEGORIES, path, report)
    require_enum(factor, "impactDirection", ALLOWED_DIRECTIONS, path, report)
    require_enum(factor, "importance", ALLOWED_LEVELS, path, report)
    require_enum(factor, "confidence", ALLOWED_LEVELS, path, report)
    require_enum(factor, "timeHorizon", ALLOWED_TIME_HORIZONS, path, report)

    evidence = require_list(factor, "evidence", path, report)
    if not evidence:
        report.error(f"{path}.evidence must contain at least one source")
    for evidence_index, item in enumerate(evidence):
        validate_evidence_item(item, f"{path}.evidence[{evidence_index}]", report)

    if factor.get("importance") == "high" and len(evidence) < 2:
        report.warning(
            f"{path} is high importance but has fewer than two evidence items; "
            "this requires an A-grade source or an explicit caveat"
        )

    for list_key in ("affectedSegments", "affectedRegions", "caveats"):
        values = require_list(factor, list_key, path, report)
        if not values:
            report.warning(f"{path}.{list_key} is empty")

    counter_evidence = factor.get("counterEvidence", [])
    if counter_evidence is None:
        counter_evidence = []
    if not isinstance(counter_evidence, list):
        report.error(f"{path}.counterEvidence must be a list when present")
    else:
        for counter_index, item in enumerate(counter_evidence):
            validate_counter_evidence(item, f"{path}.counterEvidence[{counter_index}]", report)


def validate_discarded_claim(item: Any, index: int, report: ValidationReport) -> None:
    path = f"discardedClaims[{index}]"
    if not isinstance(item, dict):
        report.error(f"{path} must be an object")
        return

    require_string(item, "claim", path, report)
    require_enum(item, "reason", ALLOWED_DISCARD_REASONS, path, report)

    source_url = item.get("sourceUrl")
    if source_url not in (None, "", "unknown") and not is_http_url(source_url):
        report.error(f"{path}.sourceUrl must be an http(s) URL or unknown")


def validate_document(data: Any) -> ValidationReport:
    report = ValidationReport()
    if not isinstance(data, dict):
        report.error("root must be a JSON object")
        return report

    require_string(data, "query", "root", report)

    scope = data.get("scope")
    if not isinstance(scope, dict):
        report.error("root.scope must be an object")
    else:
        require_string(scope, "region", "root.scope", report)
        require_string(scope, "timeWindow", "root.scope", report)
        require_list(scope, "segments", "root.scope", report)

    require_list(data, "assumptions", "root", report)

    factors = require_list(data, "factors", "root", report)
    if not factors:
        report.error("root.factors must contain at least one factor")
    for index, factor in enumerate(factors):
        validate_factor(factor, index, report)

    discarded = data.get("discardedClaims", [])
    if discarded is None:
        discarded = []
    if not isinstance(discarded, list):
        report.error("root.discardedClaims must be a list when present")
    else:
        for index, item in enumerate(discarded):
            validate_discarded_claim(item, index, report)

    return report


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python validate_factor_json.py <factor-list.json>", file=sys.stderr)
        return 2

    path = Path(argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON: {exc}", file=sys.stderr)
        return 1

    report = validate_document(data)

    for warning in report.warnings:
        print(f"WARNING: {warning}")
    for error in report.errors:
        print(f"ERROR: {error}")

    if report.errors:
        print(f"Validation failed: {len(report.errors)} error(s), {len(report.warnings)} warning(s)")
        return 1

    print(f"Validation passed: 0 error(s), {len(report.warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
