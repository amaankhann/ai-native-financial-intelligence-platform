from backend.intelligence.object import IntelligenceObject

def assess_performance(entity: dict) -> IntelligenceObject:
    ret=float(entity.get("return_1y",0))
    benchmark=float(entity.get("benchmark_return",0))
    excess=ret-benchmark
    return IntelligenceObject(
        engine="performance",
        result={"return_1y":ret,"benchmark_return":benchmark,"excess_return":round(excess,4)},
        classification="OUTPERFORMING" if excess>0 else "UNDERPERFORMING" if excess<0 else "IN_LINE",
        drivers=["Excess return versus benchmark"],
        evidence=[{"source":"sample_performance","fields":["return_1y","benchmark_return"]}],
        confidence=.88, uncertainty="low",
        provenance=["sample_performance","benchmark_attribution_baseline"]
    )
