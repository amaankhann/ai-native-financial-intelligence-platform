from flask import Blueprint, jsonify, request
from backend.engines.risk import assess_risk

risk_bp = Blueprint("risk", __name__)

DEFAULT_PORTFOLIO = {
    "concentration_risk": 76,
    "liquidity_risk": 82,
    "valuation_risk": 71,
    "capital_risk": 61,
    "manager_risk": 58,
    "macro_risk": 63,
    "underlying_asset_risk": 67
}

@risk_bp.post("/risk/assess")
def risk_assess():
    payload = request.get_json(silent=True) or DEFAULT_PORTFOLIO
    return jsonify(assess_risk(payload).to_dict())
