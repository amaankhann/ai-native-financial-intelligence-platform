from backend.orchestration.pipeline import execute

def test_unified_router_runs_credit():
    out=execute({"engine":"credit","entity_id":"PRV-001","payload":{"leverage_risk":65,"coverage_risk":58,"cash_flow_risk":63,"default_history_risk":22,"covenant_risk":48}})
    assert out["intelligence"]["engine"]=="credit"
    assert "result" in out["intelligence"]

def test_unified_router_runs_valuation():
    out=execute({"engine":"valuation","entity_id":"PUB-001","payload":{"intrinsic_value":112,"market_value":100,"market":"public"}})
    assert out["intelligence"]["classification"]=="DISCOUNT"
