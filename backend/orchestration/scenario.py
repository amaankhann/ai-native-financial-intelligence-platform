from backend.engines.risk import assess_risk

def run_liquidity_stress(portfolio: dict) -> dict:
    """Reference scenario used to demonstrate conditional orchestration."""
    stressed = dict(portfolio)
    stressed["liquidity_risk"] = min(100, stressed.get("liquidity_risk", 50) + 15)
    stressed["capital_risk"] = min(100, stressed.get("capital_risk", 50) + 8)

    risk = assess_risk(stressed).to_dict()

    return {
        "mode": "illustrative_scenario",
        "scenario": "liquidity-stress",
        "trigger": "Unfunded commitments / liquidity pressure",
        "activated_engines": ["Liquidity", "Risk"],
        "conditional_engines": ["Anomaly", "Forecast", "Credit"],
        "risk_intelligence": risk
    }
