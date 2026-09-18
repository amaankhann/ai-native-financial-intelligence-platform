# Scenario Simulation

Scenarios modify relevant portfolio states and pass the resulting state through the intelligence pipeline.

Example:

```
Liquidity Stress
 ↓
Liquidity / Capital features deteriorate
 ↓
Liquidity Engine invoked
 ↓
Risk Engine recalculates
 ↓
Forecast / Anomaly / Credit may be conditionally invoked
 ↓
Portfolio impact
 ↓
Decision Intelligence
```

The working demonstrator exposes a liquidity-stress endpoint and returns the engines activated, conditional engines and recalculated risk intelligence.
