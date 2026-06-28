# Module 03 Interview Cheatsheet

- DataFrames and SQL both build Spark logical plans.
- Transformations are lazy; actions trigger jobs.
- DataFrames are immutable; each transformation returns a new plan.
- Column expressions are distributed expressions, not local Python values.
- Projection reduces row width; filtering reduces row count.
- Built-in functions are preferred over UDFs because Catalyst can optimize them.
- `groupBy().agg()` often becomes partial aggregate, exchange, final aggregate.
- Joins require cardinality validation and may broadcast or shuffle.
- Window functions preserve rows; `GROUP BY` collapses rows.
- `EXPLAIN FORMATTED` is the evidence for scans, exchanges, joins, aggregates, sorts, and windows.
