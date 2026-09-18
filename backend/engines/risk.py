from backend.intelligence.object import IntelligenceObject

def assess_risk(portfolio: dict) -> IntelligenceObject:
    concentration = float(portfolio.get("concentration_risk", 0))
    liquidity = float(portfolio.get("liquidity_risk", 0))
    valuation = float(portfolio.get("valuation_risk", 0))
    capital = float(portfolio.get("capital_risk", 0))
    gp = float(portfolio.get("manager_risk", 0))
    macro = float(portfolio.get("macro_risk", 0))
    underlying = float(portfolio.get("underlying_asset_risk", 0))

    components = {
        "concentration": concentration,
        "liquidity": liquidity,
        "valuation": valuation,
        "capital": capital,
        "manager_gp": gp,
        "macro": macro,
        "underlying_asset": underlying
    }

    weights = {
        "concentration": .16, "liquidity": .20, "valuation": .16,
        "capital": .12, "manager_gp": .10, "macro": .12,
        "underlying_asset": .14
    }

    score = round(sum(components[k] * weights[k] for k in components))
    classification = "HIGH" if score >= 70 else "MEDIUM" if score >= 45 else "LOW"

    drivers = [
        f"Liquidity risk ({liquidity:.0f})",
        f"Concentration risk ({concentration:.0f})",
        f"Valuation risk ({valuation:.0f})"
    ]
    drivers = sorted(drivers, key=lambda x: float(x.split("(")[1][:-1]), reverse=True)

    return IntelligenceObject(
        engine="risk",
        result={"score": score, "components": components},
        classification=classification,
        drivers=drivers,
        evidence=[
            {"source": "sample_portfolio", "fields": list(components.keys())},
            {"source": "sample_market_state", "status": "illustrative"}
        ],
        confidence=0.89,
        uncertainty="medium",
        provenance=["sample_portfolio", "transparent_weighted_risk_model"]
    )
