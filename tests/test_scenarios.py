from backend.orchestration.scenario_engine import run_scenario

def test_liquidity_shock_activates_engines():
    state={"liquidity_risk":60,"concentration_risk":50,"valuation_risk":50,"capital_risk":50,"manager_risk":50,"macro_risk":50,"underlying_asset_risk":50}
    out=run_scenario(state,{"liquidity_risk":20})
    assert "liquidity_stress" in out["triggers"]
    assert "liquidity" in out["activated_engines"]
    assert "risk" in out["activated_engines"]
