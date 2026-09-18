def detect_triggers(state):
    triggers=[]
    if float(state.get("liquidity_risk",0)) >= 70: triggers.append("liquidity_stress")
    if float(state.get("anomaly_score",0)) >= 2: triggers.append("anomaly_signal")
    if float(state.get("leverage_risk",0)) >= 70: triggers.append("credit_stress")
    if float(state.get("valuation_staleness",0)) >= .70: triggers.append("valuation_uncertainty")
    return triggers

def engines_for_triggers(triggers):
    mapping={"liquidity_stress":["liquidity","risk"],"anomaly_signal":["anomaly","risk"],"credit_stress":["credit","risk"],"valuation_uncertainty":["valuation","risk"]}
    return list(dict.fromkeys(e for t in triggers for e in mapping.get(t,[])))
