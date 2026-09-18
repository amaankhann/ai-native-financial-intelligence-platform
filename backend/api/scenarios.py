from flask import Blueprint, jsonify, request
from backend.orchestration.scenario import run_liquidity_stress

scenarios_bp = Blueprint("scenarios", __name__)

@scenarios_bp.post("/scenarios/liquidity-stress")
def liquidity_stress():
    payload = request.get_json(silent=True) or {
        "concentration_risk": 76,
        "liquidity_risk": 82,
        "valuation_risk": 71,
        "capital_risk": 61,
        "manager_risk": 58,
        "macro_risk": 63,
        "underlying_asset_risk": 67
    }
    return jsonify(run_liquidity_stress(payload))
