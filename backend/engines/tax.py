from backend.intelligence.object import IntelligenceObject

def assess_tax(entity: dict) -> IntelligenceObject:
    gain=float(entity.get("realized_gain",0))
    rate=float(entity.get("effective_tax_rate",0))
    liability=max(0,gain*rate)
    return IntelligenceObject(
        engine="tax",
        entity_id=str(entity.get("entity_id", "unknown")),
        result={"estimated_tax_liability":round(liability,2),"realized_gain":gain,"effective_rate":rate},
        classification="MATERIAL" if liability > float(entity.get("tax_materiality_threshold",10000)) else "NORMAL",
        drivers=["Realized gain","Effective tax rate"],
        evidence=[{"source":"sample_tax_lot","fields":["realized_gain","effective_tax_rate"]}],
        confidence=.68, uncertainty="high",
        provenance=["sample_tax_lot","illustrative_tax_calculation"]
    )
