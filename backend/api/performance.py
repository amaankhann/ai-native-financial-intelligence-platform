from flask import Blueprint, jsonify

performance_bp = Blueprint("performance", __name__)

@performance_bp.get("/performance/status")
def performance_status():
    return jsonify({"engine":"performance","status":"contract","message":"Model contract reserved for attribution, benchmark and contribution analysis."})
