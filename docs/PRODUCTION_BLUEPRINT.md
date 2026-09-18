# Production Blueprint

The demonstrator is intentionally modular so production components can replace individual layers.

## Data plane

Vendor adapters -> raw landing -> schema validation -> normalization -> entity resolution -> canonical storage -> feature store.

## Intelligence plane

Feature retrieval -> engine execution -> model inference -> confidence calibration -> evidence assembly -> intelligence object.

## Reasoning plane

Trigger detection -> engine routing -> dependency execution -> scenario propagation -> cross-engine reconciliation.

## Governance plane

Data lineage -> model registry -> versioning -> backtesting -> drift monitoring -> access control -> audit trail -> human review.

## Serving plane

API gateway -> portfolio/asset intelligence APIs -> agent interfaces -> UI.

## Production technology candidates

- Relational store for canonical reference data
- Time-series store for market observations
- Object storage for documents/raw data
- Graph store for ownership/look-through
- Feature store for reusable derived features
- Model registry for model lifecycle
- Workflow/event infrastructure for orchestration
- Observability stack for latency, errors and drift

Technology selection should follow workload and governance requirements rather than being hard-coded into the architecture.
