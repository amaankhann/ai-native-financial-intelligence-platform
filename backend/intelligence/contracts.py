from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class EngineRequest:
    engine: str
    entity_id: str
    market: str
    features: dict[str, Any]
    context: dict[str, Any]

@dataclass
class EngineResult:
    engine: str
    result: dict[str, Any]
    drivers: list[str]
    evidence: list[dict[str, Any]]
    confidence: float
    uncertainty: str
    provenance: list[str]
    timestamp: str | None = None

    def to_dict(self):
        return self.__dict__.copy()
