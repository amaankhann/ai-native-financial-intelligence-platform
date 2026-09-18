def portfolio_exposures(positions):
    total=sum(float(p.get("market_value",0)) for p in positions)
    if total <= 0: return {"total_value":0,"asset_weights":{},"sector_weights":{},"geography_weights":{}}
    asset_weights={p.get("asset_id"):float(p.get("market_value",0))/total for p in positions}
    sector, geography = {}, {}
    for p in positions:
        w=float(p.get("market_value",0))/total
        s=p.get("sector","Unknown"); g=p.get("geography","Unknown")
        sector[s]=sector.get(s,0)+w; geography[g]=geography.get(g,0)+w
    return {"total_value":total,"asset_weights":asset_weights,"sector_weights":sector,"geography_weights":geography}
