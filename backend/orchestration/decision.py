def reconcile(results):
    if not results: return {"status":"NO_INTELLIGENCE","engines":[]}
    c=[float(r.get("confidence",0)) for r in results]
    return {"status":"INTELLIGENCE_READY","engines":[r.get("engine") for r in results],"average_confidence":round(sum(c)/len(c),4),"high_priority_drivers":[d for r in results for d in r.get("drivers",[])][:10],"evidence_count":sum(len(r.get("evidence",[])) for r in results)}
