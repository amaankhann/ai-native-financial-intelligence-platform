# Intelligence Orchestration

The orchestration layer determines which engines are required for a question or observed state.

Flow:

User/System Request -> Intent and Entity Resolution -> Context and Feature Retrieval -> Trigger Detection -> Engine Selection -> Parallel/Sequential Execution -> Evidence Reconciliation -> Scenario Simulation -> Decision Intelligence

Example: liquidity stress activates Liquidity Intelligence first. Risk then consumes the deteriorated liquidity state. Forecast, Anomaly or Credit can be conditionally activated when their triggers are present.

Production requirements include idempotency, dependency declarations, execution tracing, model versioning, confidence propagation, uncertainty preservation, provenance and failure isolation.

The current implementation provides a lightweight router and scenario pipeline. Production deployment would add a workflow engine, event bus, feature store, model registry and observability.
