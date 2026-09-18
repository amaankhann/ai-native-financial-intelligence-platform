# AI-Native Financial Intelligence Platform

> An interactive working demonstrator for an AI-native financial intelligence architecture across public and private markets.

**Live UI:** https://wealthtechmodel.netlify.app

## Overview

This repository demonstrates a modular financial intelligence platform that moves from raw financial data through data quality, entity resolution, feature intelligence, specialist engines, scenario analysis and explainable decision intelligence.

The architecture covers nine intelligence engines:

- Risk
- Valuation
- Forecast
- Performance
- Credit
- Liquidity
- Anomaly
- Tax
- ESG

The current working implementation focuses on the **Risk Intelligence Engine**, a standardized **Intelligence Object**, scenario orchestration and a lightweight API/frontend demonstrator. Other engines are represented through the same extensible contract and can be implemented incrementally.

## Architecture

```
Data Sources
    ↓
Ingestion & Normalization
    ↓
Data Quality + Entity Resolution + Lineage
    ↓
Canonical Financial Model
    ↓
Exposure & Feature Intelligence
    ↓
┌─────────────────────────────────────────────┐
│ Asset Intelligence                          │
│ Risk | Valuation | Forecast | Performance   │
├─────────────────────────────────────────────┤
│ Specialist Intelligence                     │
│ Credit | Liquidity | Anomaly | Tax | ESG    │
└─────────────────────────────────────────────┘
    ↓
Orchestration + Scenario Simulation
    ↓
Confidence + Uncertainty + Provenance
    ↓
Decision Intelligence
```

## Working Demonstration

The API exposes a deterministic sample Risk Intelligence calculation:

```
POST /api/risk/assess
POST /api/scenarios/liquidity-stress
GET  /api/architecture
GET  /api/engines
```

The sample model is intentionally transparent: it demonstrates architecture, feature flow, aggregation and explainability without pretending to reproduce an institutional production model.

## Example Intelligence Object

```json
{
  "engine": "risk",
  "score": 73,
  "classification": "HIGH",
  "drivers": ["Unfunded commitments", "Sector concentration", "Valuation uncertainty"],
  "confidence": 0.89,
  "uncertainty": "medium",
  "provenance": ["sample_portfolio", "sample_market_state"]
}
```

## Repository Structure

```
backend/
  api/
  engines/
  intelligence/
  orchestration/
  models/
data/
  sample/
  schemas/
docs/
frontend/
tests/
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python backend/app.py
```

Open `http://localhost:5000`.

## Design Principles

1. **Explainability over opaque scoring**
2. **Common intelligence contract across engines**
3. **Scenario-aware orchestration**
4. **Public and private market extensibility**
5. **Evidence, confidence, uncertainty and provenance as first-class outputs**
6. **Clear separation between demonstrator logic and production ML/data integrations**

## Status

**Working demonstrator:** Risk Engine, Intelligence Object, orchestration flow, scenario simulation and API.

**Architecture-ready:** Valuation, Forecast, Performance, Credit, Liquidity, Anomaly, Tax and ESG engine contracts.

## Disclaimer

This is a research and architecture demonstrator. Sample outputs use synthetic/illustrative inputs and transparent calculations. It is not investment advice, a production risk model, or a substitute for institutional model validation.

## Roadmap

- [ ] Add ML-backed risk models
- [ ] Implement remaining eight engines
- [ ] Add real data adapters
- [ ] Add portfolio look-through graph
- [ ] Add scenario library
- [ ] Add model monitoring and validation
- [ ] Add authentication and production deployment
