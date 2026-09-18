def market_features(asset: dict) -> dict:
    price = float(asset.get("price", 0))
    benchmark = float(asset.get("benchmark_return", 0))
    return {
        "return_1y": float(asset.get("return_1y", 0)),
        "volatility": float(asset.get("volatility", 0)),
        "drawdown": float(asset.get("drawdown", 0)),
        "benchmark_return": benchmark,
        "excess_return": float(asset.get("return_1y", 0)) - benchmark,
        "price": price
    }
