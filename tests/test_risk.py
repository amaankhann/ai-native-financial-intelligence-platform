from backend.engines.risk import assess_risk

def test_risk_engine_returns_valid_intelligence():
    result = assess_risk({
        "concentration_risk": 76,
        "liquidity_risk": 82,
        "valuation_risk": 71,
        "capital_risk": 61,
        "manager_risk": 58,
        "macro_risk": 63,
        "underlying_asset_risk": 67
    }).to_dict()

    assert result["engine"] == "risk"
    assert result["result"]["score"] == 70
    assert result["classification"] == "HIGH"
    assert 0 <= result["confidence"] <= 1
