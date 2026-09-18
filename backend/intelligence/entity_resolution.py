import re
from typing import Any

def normalize_name(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower().strip())

def resolve_entity(candidate: dict[str, Any], master: list[dict[str, Any]]) -> dict[str, Any]:
    for key in ("isin", "lei", "ticker"):
        value = candidate.get(key)
        if value:
            for item in master:
                if item.get(key) == value:
                    return {"entity_id": item["entity_id"], "match_score": 1.0, "method": "authoritative_identifier"}
    name = normalize_name(str(candidate.get("name", "")))
    best = {"entity_id": None, "match_score": 0.0, "method": "unresolved"}
    for item in master:
        score = 1.0 if name and name == normalize_name(str(item.get("name", ""))) else 0.0
        if score > best["match_score"]:
            best = {"entity_id": item["entity_id"], "match_score": score, "method": "normalized_name"}
    return best
