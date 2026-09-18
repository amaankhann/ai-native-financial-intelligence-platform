from dataclasses import dataclass, field
from typing import Literal

AssetType = Literal["equity","bond","fund","etf","private_company","real_asset","cash"]

@dataclass
class Asset:
    asset_id: str
    name: str
    asset_type: AssetType
    market: Literal["public","private"]
    currency: str = "USD"
    sector: str | None = None
    geography: str | None = None

@dataclass
class Position:
    asset_id: str
    quantity: float
    market_value: float
    cost_basis: float
    unrealized_pnl: float = 0.0
    weight: float = 0.0

@dataclass
class Portfolio:
    portfolio_id: str
    owner_type: str
    positions: list[Position] = field(default_factory=list)
    cash: float = 0.0
    unfunded_commitment: float = 0.0
