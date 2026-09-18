from backend.intelligence.object import IntelligenceObject

def detect_anomaly(entity: dict) -> IntelligenceObject:
    z = float(entity.get("anomaly_score", 0))
    classification = "ANOMALOUS" if z >= 3 else "WATCH" if z >= 2 else "NORMAL"
    return IntelligenceObject(
        engine="anomaly",
        result={"anomaly_score":z,"thresholds":{"watch":2,"anomalous":3}},
        classification=classification,
        drivers=["Observed deviation from expected behavior"] if z >= 2 else [],
        evidence=[{"source":"sample_observations","method":"standardized_deviation"}],
        confidence=.90, uncertainty="low" if z >= 3 else "medium",
        provenance=["sample_observations","rule_based_anomaly_detector"]
    )
