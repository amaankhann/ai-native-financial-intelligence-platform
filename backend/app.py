from flask import Flask, jsonify
from flask_cors import CORS
from backend.api.architecture import architecture_bp
from backend.api.engines import engines_bp
from backend.api.risk import risk_bp
from backend.api.scenarios import scenarios_bp
from backend.api.intelligence import intelligence_bp

app = Flask(__name__)
CORS(app)

for blueprint in (architecture_bp, engines_bp, risk_bp, scenarios_bp, intelligence_bp):
    app.register_blueprint(blueprint, url_prefix="/api")

@app.get("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "financial-intelligence-architecture",
        "mode": "architecture_prototype",
        "data": "illustrative_inputs_only",
        "version": "0.3.0",
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
