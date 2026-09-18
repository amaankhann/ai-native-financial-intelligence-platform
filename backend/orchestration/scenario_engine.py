from copy import deepcopy
from backend.orchestration.router import route
from backend.orchestration.triggers import detect_triggers, engines_for_triggers
from backend.orchestration.decision import reconcile

def run_scenario(base_state, shocks):
    """Apply illustrative shocks and exercise the orchestration architecture."""
    stressed = deepcopy(base_state)
    for field, delta in shocks.items():
        if isinstance(delta, (int, float)) and not isinstance(delta, bool):
            stressed[field] = stressed.get(field, 0) + delta

    triggers = detect_triggers(stressed)
    selected = engines_for_triggers(triggers)
    results = []
    for engine in selected:
        try:
            results.append(route(engine, stressed).to_dict())
        except (ValueError, TypeError):
            continue

    return {
        "mode": "illustrative_scenario",
        "baseline": base_state,
        "shocks": shocks,
        "stressed_state": stressed,
        "triggers": triggers,
        "activated_engines": selected,
        "intelligence": results,
        "reconciliation": reconcile(results),
    }
