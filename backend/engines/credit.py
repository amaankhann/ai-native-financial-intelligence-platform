from backend.intelligence.scoring import classify, clamp, weighted_score
from backend.intelligence.object import IntelligenceObject

def assess_credit(entity: dict) -> IntelligenceObject:
    values = {
        "leverage": float(entity.get("leverage_risk", 50)),
        "coverage": float(entity.get("coverage_risk", 50)),
        "cash_flow": float(entity.get("cash_flow_risk", 50)),
        "default_history": float(entity.get("default_history_risk", 50)),
        "covenant": float(entity.get("covenant_risk", 50))
    }
    score = clamp(weighted_score(values, {"leverage":.25,"coverage":.20,"cash_flow":.25,"default_history":.15,"covenant":.15}))
    return IntelligenceObject(
        engine="credit", result={"score":score,"components":values},
        classification=classify(score),
        drivers=sorted(values,key=values.get,reverse=True)[:3],
        evidence=[{"source":"sample_credit_profile","fields":list(values)}],
        confidence=.82, uncertainty="medium",
        provenance=["sample_credit_profile","transparent_credit_model"]
    )
