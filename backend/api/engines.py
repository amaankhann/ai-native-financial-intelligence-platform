from flask import Blueprint, jsonify

engines_bp = Blueprint("engines", __name__)

ENGINES = [
    {"name": "Risk", "type": "asset", "status": "working"},
    {"name": "Valuation", "type": "asset", "status": "contract"},
    {"name": "Forecast", "type": "asset", "status": "contract"},
    {"name": "Performance", "type": "asset", "status": "contract"},
    {"name": "Credit", "type": "specialist", "status": "contract"},
    {"name": "Liquidity", "type": "specialist", "status": "contract"},
    {"name": "Anomaly", "type": "specialist", "status": "contract"},
    {"name": "Tax", "type": "specialist", "status": "contract"},
    {"name": "ESG", "type": "specialist", "status": "contract"}
]

@engines_bp.get("/engines")
def engines():
    return jsonify({"engines": ENGINES})
