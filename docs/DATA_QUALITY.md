# Data Quality and Sufficiency

Intelligence quality is bounded by input quality.

## Quality dimensions

- Completeness
- Validity
- Consistency
- Timeliness
- Uniqueness
- Referential integrity
- Source reliability
- Temporal alignment

## Sufficiency gate

Before model execution, the platform should determine whether required fields exist and whether their quality is sufficient for the intended engine.

A failed sufficiency gate should not silently produce a normal score. It should return an explicit data-quality state and preserve the missing-field evidence.

## Temporal alignment

Observations from different sources must be aligned to the decision timestamp. This is especially important in private markets where valuation, financial statements and transactions may have different reporting dates.

## Uncertainty propagation

Low-quality or stale inputs should increase uncertainty and may reduce confidence. The exact calibration is model-specific and must be validated.
