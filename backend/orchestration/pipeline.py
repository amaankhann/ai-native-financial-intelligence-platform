from backend.orchestration.router import route

def execute(request: dict) -> dict:
    engine=request["engine"].lower()
    return {"request":{"engine":engine,"entity_id":request.get("entity_id")},
            "intelligence":route(engine,request.get("payload",{})).to_dict()}
