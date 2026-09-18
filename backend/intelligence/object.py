from dataclasses import dataclass, asdict
from typing import Any

@dataclass
class IntelligenceObject:
    engine: str
    result: Any
    classification: str | None
    drivers: list[str]
    evidence: list[dict]
    confidence: float
    uncertainty: str
    provenance: list[str]

    def to_dict(self):
        return asdict(self)
