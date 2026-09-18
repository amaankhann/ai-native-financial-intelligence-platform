from flask import Blueprint, jsonify

architecture_bp = Blueprint("architecture", __name__)

@architecture_bp.get("/architecture")
def architecture():
    return jsonify({
        "layers": [
            "Data Universe",
            "Data Foundation",
            "Canonical Financial Model",
            "Feature Intelligence",
            "Asset Intelligence Engines",
            "Specialist Intelligence Engines",
            "Scenario & Governance",
            "Decision Intelligence"
        ],
        "flow": "Data → Intelligence → Reasoning → Simulation → Decision"
    })
