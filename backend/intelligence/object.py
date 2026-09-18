from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone
from typing import Any

@dataclass
class IntelligenceObject:
    engine: str
    entity_id: str
    result: Any
    classification: str | None
    drivers: list[str]
    evidence: list[dict] = field(default_factory=list)
    confidence: float = 0.0
    uncertainty: str = "unknown"
    provenance: list[str] = field(default_factory=list)
    impact: dict[str, Any] = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    model_version: str = "demo-0.2"

    def to_dict(self):
        return asdict(self)
