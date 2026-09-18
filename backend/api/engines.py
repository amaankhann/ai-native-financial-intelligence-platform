from flask import Blueprint, jsonify
engines_bp=Blueprint("engines",__name__)
ENGINES=[
{"name":"Risk","slug":"risk","type":"asset","status":"working"},
{"name":"Valuation","slug":"valuation","type":"asset","status":"working"},
{"name":"Forecast","slug":"forecast","type":"asset","status":"working"},
{"name":"Performance","slug":"performance","type":"asset","status":"working"},
{"name":"Credit","slug":"credit","type":"specialist","status":"working"},
{"name":"Liquidity","slug":"liquidity","type":"specialist","status":"working"},
{"name":"Anomaly","slug":"anomaly","type":"specialist","status":"working"},
{"name":"Tax","slug":"tax","type":"specialist","status":"working"},
{"name":"ESG","slug":"esg","type":"specialist","status":"working"}]
@engines_bp.get("/engines")
def engines(): return jsonify({"count":len(ENGINES),"engines":ENGINES})
