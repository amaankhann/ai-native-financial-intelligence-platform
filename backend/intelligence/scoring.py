def clamp(value: float, low: float = 0, high: float = 100) -> float:
    return max(low, min(high, value))

def classify(score: float) -> str:
    if score >= 70:
        return "HIGH"
    if score >= 45:
        return "MEDIUM"
    return "LOW"

def weighted_score(values: dict[str, float], weights: dict[str, float]) -> float:
    total_weight = sum(weights.values())
    if not total_weight:
        return 0.0
    return round(sum(values.get(k, 0.0) * w for k, w in weights.items()) / total_weight)
