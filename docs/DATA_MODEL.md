# Canonical Data Model

Raw vendor records are separated from canonical financial entities.

Core entities: Portfolio, Asset, Position, Fund, GP, Company, Investment, Transaction and Valuation Observation.

Identity flow:

Vendor Record -> Entity Resolution -> Canonical Entity -> Relationship Graph -> Features -> Intelligence

Public-market extensions include prices, volumes, corporate actions, fundamentals, benchmarks and factor exposures.

Private-market extensions include commitments, calls, distributions, valuations, ownership, GP relationships, company financials, transaction history and appraisal observations.

Every economically meaningful value is timestamped so the platform can reproduce the state that existed when a decision was made.
