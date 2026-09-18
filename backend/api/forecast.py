from flask import Blueprint, jsonify

forecast_bp = Blueprint("forecast", __name__)

@forecast_bp.get("/forecast/status")
def forecast_status():
    return jsonify({"engine":"forecast","status":"contract","message":"Model contract reserved for return, volatility and scenario forecasting."})
