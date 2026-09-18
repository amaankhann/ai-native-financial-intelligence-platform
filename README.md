# AI-Native Financial Intelligence Platform

> A working demonstrator for an AI-native financial intelligence architecture across public and private markets.

**Live UI:** https://wealthtechmodel.netlify.app  
**Repository:** https://github.com/amaankhann/ai-native-financial-intelligence-platform

## What this project demonstrates

The platform converts heterogeneous financial data into explainable, scenario-aware intelligence.

**Data → Intelligence → Reasoning → Simulation → Decision**

It is deliberately designed as an architecture rather than nine independent dashboards. A common intelligence contract allows specialist engines to contribute evidence to a larger portfolio or asset decision.

## Intelligence engines

| Engine | Domain | Current status |
|---|---|---|
| Risk | Asset | Working |
| Valuation | Asset | Working |
| Forecast | Asset | Working |
| Performance | Asset | Working |
| Liquidity | Specialist | Working |
| Credit | Specialist | Working |
| Anomaly | Specialist | Working |
| Tax | Specialist | Working |
| ESG | Specialist | Working |

The current models are transparent demonstrators. Production implementations can replace the deterministic logic with validated statistical, ML, optimization, graph and vendor-backed models without changing the external intelligence contract.

## Architecture

```
                    DATA UNIVERSE
                         │
        ┌────────────────┴────────────────┐
        │                                 │
   Public Markets                    Private Markets
        │                                 │
        └──────────────┬──────────────────┘
                       ↓
             INGESTION & NORMALIZATION
                       ↓
          DATA QUALITY / ENTITY RESOLUTION
                       ↓
             CANONICAL FINANCIAL MODEL
                       ↓
            RELATIONSHIP / LOOK-THROUGH
                       ↓
               FEATURE INTELLIGENCE
                       ↓
        ┌──────────────┴──────────────┐
        │                             │
   ASSET ENGINES                 SPECIALIST ENGINES
   Risk                         Credit
   Valuation                    Liquidity
   Forecast                     Anomaly
   Performance                  Tax
                                ESG
        │                             │
        └──────────────┬──────────────┘
                       ↓
             ORCHESTRATION / ROUTING
                       ↓
              SCENARIO SIMULATION
                       ↓
       CONFIDENCE / UNCERTAINTY / PROVENANCE
                       ↓
              DECISION INTELLIGENCE
```

## Standard intelligence contract

Every engine returns:

**Result → Drivers → Evidence → Confidence → Uncertainty → Provenance**

This makes engine outputs composable and reviewable.

## Working API

Start the backend:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python backend/app.py
```

Then:

```
GET  /health
GET  /api/architecture
GET  /api/engines
POST /api/intelligence/run
POST /api/risk/assess
POST /api/scenarios/liquidity-stress
```

Example unified request:

```json
{
  "engine": "credit",
  "entity_id": "PRV-001",
  "payload": {
    "leverage_risk": 65,
    "coverage_risk": 58,
    "cash_flow_risk": 63,
    "default_history_risk": 22,
    "covenant_risk": 48
  }
}
```

The same endpoint can route requests to all nine engines.

## Scenario orchestration

A scenario is not simply a dashboard filter. It changes the state supplied to the intelligence pipeline.

Example:

```
Liquidity Stress
      ↓
Liquidity / Capital deterioration
      ↓
Liquidity Engine
      ↓
Risk Engine
      ↓
Conditional Forecast / Credit / Anomaly
      ↓
Evidence reconciliation
      ↓
Decision intelligence
```

The current demonstrator implements a liquidity-stress pathway and a reusable engine router.

## Public vs private markets

The architecture intentionally separates market-specific feature/model layers.

Public-market intelligence can use observable pricing, volume, fundamentals, benchmarks and factor exposures.

Private-market intelligence can use commitments, capital calls, distributions, periodic valuations, ownership relationships, GP/company data, transaction history and appraisal evidence.

The common contract sits above these different data realities.

## Repository structure

```
backend/
  api/                  # HTTP interfaces
  engines/              # intelligence engines
  features/             # feature transformations
  intelligence/         # contracts and scoring primitives
  models/               # canonical entities
  orchestration/        # routing and scenario execution

data/
  sample/                # synthetic demonstrator data

docs/
  MASTER_ARCHITECTURE.md
  ENGINE_SPECIFICATIONS.md
  DATA_MODEL.md
  ORCHESTRATION.md
  PUBLIC_PRIVATE_MARKETS.md
  RISK_INTELLIGENCE_ENGINE.md
  SCENARIO_SIMULATION.md
  EXPLAINABILITY.md

frontend/
tests/
.github/workflows/
Dockerfile
```

## Engineering principles

- Explainability is part of the output contract.
- Confidence and uncertainty are explicit.
- Provenance is retained with every intelligence result.
- Public and private markets use different data/model layers.
- Specialist engines are conditionally invoked.
- Deterministic demo logic is clearly separated from future production ML.
- The architecture is designed for incremental replacement of models and data adapters.

## Testing

Run:

```bash
pytest -q
```

GitHub Actions runs the test suite on pushes and pull requests.

## Docker

```bash
docker build -t financial-intelligence-platform .
docker run -p 5000:5000 financial-intelligence-platform
```

## Roadmap

- [x] Common intelligence contract
- [x] Nine engine contracts/implementations
- [x] Unified engine router
- [x] Scenario pipeline
- [x] Public/private sample data
- [x] CI and Docker baseline
- [ ] ML-backed risk models
- [ ] Real market/private-market data adapters
- [ ] Entity-resolution graph
- [ ] Portfolio look-through graph
- [ ] Feature store
- [ ] Model registry and monitoring
- [ ] Advanced scenario library
- [ ] Production authentication and deployment

## Research disclaimer

This is a research and architecture demonstrator. Sample data and calculations are illustrative and are not investment advice, production risk models or validated institutional models.
