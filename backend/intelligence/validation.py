def validate_score(value):
    value=float(value)
    if not 0 <= value <= 100: raise ValueError("score must be between 0 and 100")
    return value

def validate_confidence(value):
    value=float(value)
    if not 0 <= value <= 1: raise ValueError("confidence must be between 0 and 1")
    return value
