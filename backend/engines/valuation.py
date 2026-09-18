from backend.intelligence.object import IntelligenceObject

def value_asset(entity: dict) -> IntelligenceObject:
    intrinsic=float(entity.get("intrinsic_value",0))
    market=float(entity.get("market_value",0))
    gap=0 if market == 0 else (intrinsic-market)/market
    return IntelligenceObject(
        engine="valuation",
        result={"intrinsic_value":intrinsic,"market_value":market,"valuation_gap":round(gap,4)},
        classification="DISCOUNT" if gap > .10 else "PREMIUM" if gap < -.10 else "ALIGNED",
        drivers=["Intrinsic vs market value"],
        evidence=[{"source":"sample_valuation_inputs","fields":["intrinsic_value","market_value"]}],
        confidence=.70, uncertainty="high" if entity.get("market")=="private" else "medium",
        provenance=["sample_valuation_inputs","transparent_valuation_baseline"]
    )
