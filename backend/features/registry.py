from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class FeatureDefinition:
    name: str
    description: str
    source_fields: tuple[str, ...]
    domain: str
    freshness: str

FEATURES = {
    "liquidity_pressure": FeatureDefinition("liquidity_pressure","Composite liquidity stress signal",
        ("cash_buffer_risk","unfunded_commitment_risk","market_depth_risk"),"liquidity","near-real-time"),
    "valuation_uncertainty": FeatureDefinition("valuation_uncertainty","Proxy for valuation uncertainty",
        ("valuation_risk","data_freshness_days"),"valuation","daily"),
    "credit_pressure": FeatureDefinition("credit_pressure","Composite balance-sheet and debt-service stress signal",
        ("leverage_risk","coverage_risk","cash_flow_risk"),"credit","daily"),
}

def list_features() -> list[dict[str, Any]]:
    return [{"name":f.name,"description":f.description,"source_fields":list(f.source_fields),
             "domain":f.domain,"freshness":f.freshness} for f in FEATURES.values()]
