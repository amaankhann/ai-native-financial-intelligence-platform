# Data Quality Gate

The gate sits between canonical data and intelligence execution. It checks completeness, numeric type validity and declared freshness, then returns PASS or DEGRADED with a quality score and explicit missing/invalid fields. Production extensions should include duplicate detection, cross-vendor reconciliation, temporal consistency, source reliability, lineage and drift controls.
