from copy import deepcopy
from backend.orchestration.router import route
from backend.orchestration.triggers import detect_triggers, engines_for_triggers
from backend.orchestration.decision import reconcile

def run_scenario(base_state, shocks):
    stressed=deepcopy(base_state)
    for field,delta in shocks.items():
        stressed[field]=stressed.get(field,0)+delta
    triggers=detect_triggers(stressed)
    selected=engines_for_triggers(triggers)
    results=[]
    for engine in selected:
        try: results.append(route(engine,stressed).to_dict())
        except (ValueError,TypeError): continue
    return {"baseline":base_state,"shocks":shocks,"stressed_state":stressed,
            "triggers":triggers,"activated_engines":selected,
            "intelligence":results,"reconciliation":reconcile(results)}
