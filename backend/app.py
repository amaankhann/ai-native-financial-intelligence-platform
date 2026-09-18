from flask import Flask, jsonify, request
from flask_cors import CORS

from backend.api.architecture import architecture_bp
from backend.api.engines import engines_bp
from backend.api.risk import risk_bp
from backend.api.scenarios import scenarios_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(architecture_bp, url_prefix="/api")
app.register_blueprint(engines_bp, url_prefix="/api")
app.register_blueprint(risk_bp, url_prefix="/api")
app.register_blueprint(scenarios_bp, url_prefix="/api")

@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "financial-intelligence-platform"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
