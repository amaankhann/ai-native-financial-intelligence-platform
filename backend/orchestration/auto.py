from backend.intelligence.data_quality import validate_input
from backend.orchestration.triggers import detect_triggers, engines_for_triggers
from backend.orchestration.router import run_engine
from backend.orchestration.decision import reconcile

def execute_auto(state: dict) -> dict:
    triggers = detect_triggers(state)
    engines = engines_for_triggers(triggers) or ["risk"]
    quality = {e: validate_input(e, state).to_dict() for e in engines}
    intelligence = []
    for engine in engines:
        if quality[engine]["score"] < 0.5:
            continue
        intelligence.append(run_engine(engine, state).to_dict())
    return {"entity_id":state.get("entity_id","unknown"),"triggers":triggers,
            "activated_engines":engines,"data_quality":quality,
            "intelligence":intelligence,"reconciliation":reconcile(intelligence)}
