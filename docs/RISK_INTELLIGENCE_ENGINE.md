# Risk Intelligence Engine

The Risk Intelligence Engine is the first working engine in this repository.

## Risk dimensions

- Liquidity
- Concentration
- Valuation
- Capital / commitment
- Underlying asset
- Manager / GP
- Market / macro

## Demonstrator calculation

The current implementation uses a transparent weighted aggregation across seven risk components. It is deliberately simple enough to inspect and test.

The architecture is designed so the weighted calculation can later be replaced or augmented with statistical, ML, factor, graph and scenario models without changing the external intelligence contract.

## Explainability

A risk output contains:

- Score
- Classification
- Component states
- Drivers
- Evidence
- Confidence
- Uncertainty
- Provenance

## Private-market look-through

The broader design supports:

`Fund → GP → Company → Investment → Sector → Geography`

This is where private-market risk analysis can extend beyond fund-level observations into underlying economic exposures.
