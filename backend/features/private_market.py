def private_market_features(asset: dict) -> dict:
    return {
        "unfunded_ratio": float(asset.get("unfunded_ratio", 0)),
        "valuation_staleness": float(asset.get("valuation_staleness", 0)),
        "sector_concentration": float(asset.get("sector_concentration", 0)),
        "gp_concentration": float(asset.get("gp_concentration", 0)),
        "realization_ratio": float(asset.get("realization_ratio", 0)),
        "leverage": float(asset.get("leverage", 0))
    }
