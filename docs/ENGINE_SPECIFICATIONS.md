# Engine Specifications

All nine engines expose one intelligence contract while using domain-specific features.

## Risk
Current risk state and drivers. Inputs: concentration, liquidity, valuation, capital, manager/GP, macro and underlying-asset signals. Future extensions: factor models, Monte Carlo, graph exposure and calibrated ML.

## Liquidity
Ability to meet obligations under normal and stressed conditions. Inputs: cash buffer, unfunded commitments, market depth and lockups. Future extensions: cash-flow forecasting and liquidation-cost curves.

## Credit
Borrower/issuer resilience. Inputs: leverage, coverage, cash flow, default history and covenants. Future extensions: PD/LGD/EAD, transition models and covenant monitoring.

## Anomaly
Behavior inconsistent with expected state. Future extensions: multivariate detection, graph anomalies and drift detection.

## Forecast
Future states and uncertainty from returns, volatility, macro factors and scenarios. Future extensions: ARIMA, state-space, gradient boosting and neural forecasting.

## Valuation
Model-supported value versus observed value. Future extensions: DCF, multiples, transactions, NAV and private-market appraisal ensembles.

## Performance
Realized performance relative to benchmark or target. Future extensions: Brinson and factor attribution.

## Tax
Tax exposure associated with positions and actions. Future extensions: jurisdiction rules, tax lots and scenario-aware tax impact.

## ESG
Environmental, social and governance risk. Future extensions: materiality mapping, controversy NLP, emissions normalization and regulatory mapping.

## Common output
Result -> Drivers -> Evidence -> Confidence -> Uncertainty -> Provenance -> Timestamp -> Impact.

Engines are contributors to a shared decision fabric, not isolated dashboards.
