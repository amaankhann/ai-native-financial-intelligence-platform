from backend.intelligence.scoring import classify, clamp, weighted_score
from backend.intelligence.object import IntelligenceObject

def assess_liquidity(portfolio: dict) -> IntelligenceObject:
    values = {
        "cash_buffer": 100 - float(portfolio.get("cash_buffer_risk", 50)),
        "unfunded": float(portfolio.get("unfunded_commitment_risk", 50)),
        "market_depth": float(portfolio.get("market_depth_risk", 50)),
        "lockup": float(portfolio.get("lockup_risk", 50)),
    }
    weights = {"cash_buffer": .30, "unfunded": .30, "market_depth": .20, "lockup": .20}
    score = weighted_score(values, weights)
    score = clamp(score)
    return IntelligenceObject(
        engine="liquidity",
        result={"score": score, "components": values},
        classification=classify(score),
        drivers=[max(values, key=values.get)],
        evidence=[{"source":"sample_portfolio","fields":list(values)}],
        confidence=.86,
        uncertainty="medium",
        provenance=["sample_portfolio","transparent_liquidity_model"]
    )
