from dataclasses import dataclass, field
from typing import Any

@dataclass
class QualityReport:
    status: str
    score: float
    missing: list[str] = field(default_factory=list)
    invalid: list[str] = field(default_factory=list)
    stale: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {"status": self.status, "score": round(self.score, 3), "missing": self.missing,
                "invalid": self.invalid, "stale": self.stale, "warnings": self.warnings}

ENGINE_REQUIREMENTS = {
    "risk": ["concentration_risk", "liquidity_risk", "valuation_risk"],
    "liquidity": ["cash_buffer_risk", "unfunded_commitment_risk", "market_depth_risk"],
    "credit": ["leverage_risk", "coverage_risk", "cash_flow_risk"],
    "anomaly": ["anomaly_score"], "forecast": ["base_return", "volatility"],
    "valuation": ["intrinsic_value", "market_value"], "performance": ["return_1y", "benchmark_return"],
    "tax": ["realized_gain", "effective_tax_rate"],
    "esg": ["environmental_risk", "social_risk", "governance_risk"],
}

def validate_input(engine: str, payload: dict[str, Any]) -> QualityReport:
    required = ENGINE_REQUIREMENTS.get(engine, [])
    missing = [k for k in required if k not in payload]
    invalid = [k for k in required if k in payload and
               (not isinstance(payload[k], (int, float)) or isinstance(payload[k], bool))]
    score = max(0.0, 1.0 - (len(missing) + len(invalid)) / max(len(required), 1))
    warnings = []
    if payload.get("data_freshness_days", 0) > payload.get("max_freshness_days", 30):
        warnings.append("Input data exceeds declared freshness window.")
    return QualityReport("PASS" if not missing and not invalid else "DEGRADED",
                          score, missing, invalid, [], warnings)
