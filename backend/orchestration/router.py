from backend.engines.risk import assess_risk
from backend.engines.liquidity import assess_liquidity
from backend.engines.credit import assess_credit
from backend.engines.anomaly import detect_anomaly
from backend.engines.forecast import forecast
from backend.engines.valuation import value_asset
from backend.engines.performance import assess_performance
from backend.engines.tax import assess_tax
from backend.engines.esg import assess_esg

def route(engine: str, payload: dict):
    handlers = {"risk":assess_risk,"liquidity":assess_liquidity,"credit":assess_credit,
                "anomaly":detect_anomaly,"forecast":forecast,"valuation":value_asset,
                "performance":assess_performance,"tax":assess_tax,"esg":assess_esg}
    if engine not in handlers:
        raise ValueError(f"Unknown engine: {engine}")
    return handlers[engine](payload)
