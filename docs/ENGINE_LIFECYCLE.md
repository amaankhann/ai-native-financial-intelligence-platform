# Intelligence Engine Lifecycle

Every engine follows one common lifecycle: request contract → data quality gate → feature preparation → calculation/model inference → validation → canonical Intelligence Object → trigger evaluation → cross-engine reconciliation → decision intelligence.

The repository implementations are transparent reference baselines. Production hardening should add calibrated models, historical backtesting, model monitoring, access controls, lineage, drift detection and independent validation.
