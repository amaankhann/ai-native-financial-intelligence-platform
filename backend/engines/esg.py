from backend.intelligence.object import IntelligenceObject

def assess_esg(entity: dict) -> IntelligenceObject:
    environmental=float(entity.get("environmental_risk",50))
    social=float(entity.get("social_risk",50))
    governance=float(entity.get("governance_risk",50))
    score=round(.4*environmental+.3*social+.3*governance)
    return IntelligenceObject(
        engine="esg",
        entity_id=str(entity.get("entity_id", "unknown")),
        result={"score":score,"environmental":environmental,"social":social,"governance":governance},
        classification="HIGH" if score>=70 else "MEDIUM" if score>=45 else "LOW",
        drivers=["environmental","social","governance"],
        evidence=[{"source":"sample_esg_profile","fields":["environmental_risk","social_risk","governance_risk"]}],
        confidence=.76, uncertainty="medium",
        provenance=["sample_esg_profile","illustrative_esg_aggregation"]
    )
