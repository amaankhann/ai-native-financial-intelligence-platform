from backend.intelligence.object import IntelligenceObject

def forecast(entity: dict) -> IntelligenceObject:
    base=float(entity.get("base_return",0))
    volatility=float(entity.get("volatility",0))
    stress=float(entity.get("stress_adjustment",0))
    expected=base-stress
    return IntelligenceObject(
        engine="forecast",
        entity_id=str(entity.get("entity_id", "unknown")),
        result={"expected_return":round(expected,4),"volatility":volatility},
        classification="POSITIVE" if expected > 0 else "NEGATIVE",
        drivers=["Base return","Stress adjustment"],
        evidence=[{"source":"sample_market_state","features":["base_return","volatility","stress_adjustment"]}],
        confidence=.74, uncertainty="medium",
        provenance=["sample_market_state","transparent_forecast_baseline"]
    )
