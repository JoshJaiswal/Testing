"""
map_to_canonical.py
────────────────────
Translates raw analyzer output (from CU or LLM) into the
canonical schema structure defined in contract-package.schema.json.

Uses mapping-matrix.yaml as the translation ruleset.

The mapping matrix format (mapping-matrix.yaml) should look like:
    mappings:
      deal_intake:
        clientName:      parties.client.name
        vendorName:      parties.vendor.name
        startDate:       dates.effectiveDate
        endDate:         dates.expirationDate
        dealValue:       commercials.totalValue
      nda:
        confidentialityTerm:  confidentiality.term
        governingLaw:         legal.governingLaw
        obligations:          confidentiality.obligations
        exceptions:           confidentiality.exceptions
      sow:
        scopeOfWork:     scope.description
        deliverables:    scope.deliverables
        milestones:      scope.milestones
        paymentTerms:    commercials.paymentTerms
"""

import yaml
import logging
from pathlib import Path
from typing import Any

log = logging.getLogger(__name__)

# Path to mapping-matrix.yaml (relative to project root)
MAPPING_MATRIX_PATH = Path(__file__).parent.parent.parent / "canonical" / "mapping-matrix.yaml"


def load_mapping_matrix() -> dict:
    """Load and parse the mapping-matrix.yaml file."""
    # TODO: Add caching so this isn't re-read on every call
    with open(MAPPING_MATRIX_PATH, "r") as f:
        matrix = yaml.safe_load(f)

    mappings = matrix.get("mappings", {})
    # Support two matrix formats:
    # 1) dictionary-based mapping sections (legacy)
    # 2) list of mapping rules with sourceAnalyzer/sourceField/canonicalPath
    if isinstance(mappings, list):
        parsed = {}
        for rule in mappings:
            source = rule.get("sourceAnalyzer") or rule.get("source")
            source_field = rule.get("sourceField")
            canonical_path = rule.get("canonicalPath")
            if not source or not source_field or not canonical_path:
                continue
            parsed.setdefault(source, {})[source_field] = canonical_path
        return {"mappings": parsed}

    return matrix


def set_nested(target: dict, dotted_key: str, value: Any) -> None:
    """
    Write a value into a nested dict using a dot-notation key.
    e.g. set_nested(d, "parties.client.name", "Acme Corp")
         → d["parties"]["client"]["name"] = "Acme Corp"
    """
    keys = dotted_key.split(".")
    cursor = target
    for key in keys[:-1]:
        cursor = cursor.setdefault(key, {})
    cursor[keys[-1]] = value


def get_nested(source: dict, dotted_key: str, default=None) -> Any:
    """
    Read a value from a nested dict using dot-notation key.
    Returns default if any key in the chain is missing.
    """
    keys = dotted_key.split(".")
    cursor = source
    for key in keys:
        if not isinstance(cursor, dict) or key not in cursor:
            return default
        cursor = cursor[key]
    return cursor


def map_to_canonical(raw_result: dict) -> dict:
    """
    Apply the mapping matrix to translate raw analyzer output
    into a canonical schema-conformant dict.

    Args:
        raw_result: Raw extraction dict. Must contain a "_source" key
                    indicating which analyzer produced it.

    Returns:
        A partial canonical package dict with only the fields
        this analyzer is responsible for populated.
    """
    matrix = load_mapping_matrix()
    source = raw_result.get("_source", "unknown")
    analyzer_used = raw_result.get("_analyzerUsed")
    mappings = matrix.get("mappings", {})

    if not isinstance(mappings, dict):
        log.warning("[Mapper] Unexpected mapping format. Expected dict, got %s", type(mappings))
        return {"_raw": raw_result, "_source": source, "_mapped": False}

    # Prefer exact analyzer ID if available (for CU analyzer names)
    analyzer_mappings = {}
    if analyzer_used and analyzer_used in mappings:
        analyzer_mappings = mappings.get(analyzer_used, {})
    elif source in mappings:
        analyzer_mappings = mappings.get(source, {})
    elif source.replace("llm_", "") in mappings:
        analyzer_mappings = mappings.get(source.replace("llm_", ""), {})
    else:
        # If no mapping for source, try fallback by analyzerUsed suffix
        if analyzer_used:
            for key in mappings:
                if key in analyzer_used:
                    analyzer_mappings = mappings.get(key, {})
                    break

    if not analyzer_mappings:
        log.warning(f"[Mapper] No mapping found for source '{source}' analyzer '{analyzer_used}' — passing through raw")
        return {"_raw": raw_result, "_source": source, "_mapped": False}

    canonical = {
        "_source": source,
        "_mapped": True,
        "_confidence": raw_result.get("_confidence", 0.0),
    }

    for raw_field, canonical_path in analyzer_mappings.items():
        value = raw_result.get(raw_field)
        if value is not None:
            set_nested(canonical, canonical_path, value)
            log.debug(f"[Mapper] {raw_field} → {canonical_path} = {value!r}")
        else:
            log.debug(f"[Mapper] {raw_field} missing in raw result — skipping")

    # TODO: Apply any transformation rules from mapping-matrix.yaml
    # e.g. date normalization, currency formatting, name casing

    # TODO: Handle list fields (deliverables, obligations) — these need
    # special treatment if the analyzer returns them as a string

    return canonical


def build_empty_canonical() -> dict:
    """
    Return a fully-structured empty canonical package.
    Matches contract-package.schema.json structure.
    Used as the base dict that merge_engine populates.
    """
    return {
        "parties": {
            "client": {"name": "", "signatories": []},
            "vendor": {"name": "", "signatories": []},
        },
        "dates": {
            "effectiveDate": "",
            "expirationDate": "",
            "executionDate": "",
        },
        "scope": {
            "description": "",
            "deliverables": [],
            "milestones": [],
        },
        "confidentiality": {
            "term": "",
            "obligations": [],
            "exceptions": [],
        },
        "commercials": {
            "totalValue": "",
            "paymentTerms": "",
            "currency": "",
        },
        "legal": {
            "governingLaw": "",
            "jurisdiction": "",
            "disputeResolution": "",
        },
        "risks": [],
        "missingFields": [],
        "conflicts": [],
        "provenance": [],
        "review": {
            "status": "needs_review",
            "reviewReason": [],
            "reviewedBy": "",
            "reviewedAt": "",
        },
    }
