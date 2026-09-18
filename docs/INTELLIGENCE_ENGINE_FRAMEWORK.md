# Intelligence Engine Framework

Every engine follows a common contract:

```
Input
 ↓
Validation
 ↓
Normalization
 ↓
Feature Engineering
 ↓
Model / Rules
 ↓
Intelligence Object
 ↓
Confidence + Uncertainty
 ↓
Evidence + Provenance
 ↓
Decision Contribution
```

## Engine families

### Asset engines
Risk, Valuation, Forecast, Performance.

### Specialist engines
Credit, Liquidity, Anomaly, Tax, ESG.

## Conditional orchestration

Specialist engines can be activated when upstream signals indicate that deeper analysis is required. For example, a liquidity shock can activate Liquidity and Risk immediately, while Forecast, Anomaly or Credit can be conditionally invoked depending on the observed state.

## Output standard

Every engine should expose a consistent intelligence object so the orchestration layer can compare, aggregate and trace outputs without coupling itself to a specific model implementation.
