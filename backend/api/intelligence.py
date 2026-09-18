from flask import Blueprint, jsonify, request
from backend.orchestration.pipeline import execute
intelligence_bp=Blueprint("intelligence",__name__)

@intelligence_bp.post("/intelligence/run")
def run_intelligence():
    payload=request.get_json(silent=True) or {}
    if "engine" not in payload: return jsonify({"error":"engine is required"}),400
    try: return jsonify(execute(payload))
    except ValueError as exc: return jsonify({"error":str(exc)}),400
