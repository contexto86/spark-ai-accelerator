# Progress Report

Module: 01 — Spark Architecture

Completion Date: June 24, 2026

Time Invested: Not recorded

## Topics Covered

- Why Spark exists and when distributed computation is justified.
- Spark versus PostgreSQL and pandas.
- Driver and executor responsibilities.
- Partitions, tasks, parallelism, waves, skew, hot keys, and salting.
- Lazy evaluation, transformations, actions, repeated lineage, and caching.
- Jobs, stages, narrow dependencies, wide dependencies, and shuffles.
- Executor failure, lost shuffle blocks, recomputation, and driver failure.
- Small-file overhead and the serial bottleneck caused by `coalesce(1)`.
- Audience-specific explanations for a PostgreSQL developer and an engineering
  manager.
- Exercise 01 completed.
- Exercise 02 completed.
- Exercise 03 completed.
- Exercise 04 completed.
- Exercise 05 completed.
- Exercise 06 completed.
- Formal no-notes checkpoint completed.
- Short mock interview completed.
- Driver OOM from `collect()`, executor skew failures, low partition
  parallelism, and idempotent external side effects were practiced.

## Strengths

- Selects Spark from workload constraints rather than data volume alone.
- Clearly explains driver, executor, partition, task, stage, and shuffle.
- Understands that skew creates a straggler that more executors cannot
  automatically solve.
- Understands action-triggered execution and when caching avoids expensive
  recomputation.
- Correctly rejects Spark for transactional APIs and workloads already meeting
  their SLA on simpler infrastructure.
- Communicates trade-offs clearly and improves answers after targeted
  correction.
- Gave an interview-ready PostgreSQL-developer explanation of Spark that
  accurately covered planning, parallel tasks, partitions, shuffles, and OLTP
  boundaries.

## Weaknesses

- Initially uncertain about stages, shuffles, and executor-loss recovery; these
  improved through guided scenarios.
- Continue refining PostgreSQL comparisons: data residing there does not prove
  it fits on one server, and PostgreSQL also performs query planning.
- Initially underestimated pandas for a 3 GB exploratory workload.
- Driver-side versus executor-side diagnosis improved during Exercise 03;
  continue occasional no-notes recall.
- Small-file overhead, cache placement, and idempotent task side effects should
  be revisited in later performance modules.

## Recommended Reinforcement

- Reinforce why keeping large results distributed is better than simply
  increasing driver memory for `collect()`.
- Review why task retries require idempotent external operations.
- Practice identifying which lineage is repeated by multiple actions.
- Revisit input-file layout versus logical Spark partitioning.
- Practice diagnosing low task counts versus skew: too few partitions is not
  the same as hot-key skew.

## Readiness Score

Formal checkpoint: 8/10.

Short mock interview: average 8/10 — Practitioner.

Module status: complete. Recommended next module: Spark SQL / DataFrame
execution basics, while carrying forward architecture diagnostics.

---

# Module 02 — Spark SQL Fundamentals

Completion Date: June 28, 2026

Time Invested: Not recorded

## Topics Covered

- Reading CSV datasets into Spark DataFrames.
- Explicit schemas versus default string columns and schema inference.
- Temporary views and session-scoped SQL access.
- Spark SQL actions, lazy plans, `show()`, `count()`, and `printSchema()`.
- Aggregations using partial and final `HashAggregate` stages.
- `Exchange` as data movement for grouping, joining, and global ordering.
- Broadcast hash joins versus shuffle/sort-merge joins.
- Join cardinality validation and duplicate-key diagnostics.
- Window functions using `ROW_NUMBER`.
- Logical window `PARTITION BY` versus Spark physical partitions.
- Top-N-per-group plans with `WindowGroupLimit` partial and final stages.
- `EXPLAIN FORMATTED` interpretation for scans, filters, joins, aggregates,
  exchanges, sorts, windows, and adaptive plans.
- Spark SQL versus PostgreSQL execution differences.
- Diagnosing bad query shapes before tuning Spark configuration.

## Strengths

- Correctly explains Spark SQL as SQL intent translated into distributed
  scans, tasks, exchanges, joins, aggregations, sorts, and driver results.
- Understands that temporary views do not copy data into durable tables.
- Explains why `GROUP BY` and window partitioning may require data movement.
- Correctly distinguishes broadcast join and sort-merge join as physical join
  strategies rather than SQL join types.
- Reads physical plans and identifies `BroadcastExchange`,
  `BroadcastHashJoin`, `HashAggregate`, `Window`, `WindowGroupLimit`,
  `Sort`, `Exchange`, and `AdaptiveSparkPlan`.
- Understands why PostgreSQL and Spark can run identical SQL with very
  different execution concerns.
- Diagnoses join row multiplication through expected counts and duplicate-key
  checks.

## Weaknesses

- Needs occasional care with SQL syntax under fatigue, especially window
  `PARTITION BY` keys and complete query clauses.
- Initially conflated logical window partitioning with Spark physical
  partitions; this improved after guided examples.
- Initially described PostgreSQL grouping as repeated scans per group; later
  corrected toward storage, indexes, statistics, and local execution plans.
- Should keep using explicit schemas for numeric CSV fields to avoid implicit
  casts during aggregates.

## Recommended Reinforcement

- Re-run the window exercises and explain why `PARTITION BY canton`, not
  `municipality_id`, answers top-N-per-canton questions.
- Practice writing complete checkpoint SQL without notes before the final mock
  interview.
- Continue reading `EXPLAIN FORMATTED` from top-level shape down to expensive
  operators: scans, projects, exchanges, joins, aggregates, sorts, and windows.
- Keep separating row-width reduction through projection from row-count
  reduction through filters or limits.

## Readiness Score

Checkpoint-style closeout: 7.5/10 — Practitioner with minor syntax gaps.

Final mock interview: deferred by learner preference.

Module status: conceptually complete. Recommended next step: optional short
Module 02 interview, then proceed to the next module while revisiting explicit
schemas and window syntax briefly.

---

# Module 03 — PySpark DataFrames and the SQL ↔ DataFrame Mental Model

Module status: in progress. Estimated coverage: 25-30%.

## Topics Added

- PySpark DataFrames as a composable API for building Spark logical plans.
- SQL ↔ DataFrame translation practice.
- Transformations versus actions in DataFrame code.
- DataFrame immutability and meaningful intermediate names.
- Column expressions, projection, filtering, and calculated columns.
- Aggregations, joins, and window functions using the DataFrame API.
- Conceptual UDF coverage and why built-in functions are preferred.
- Reading `EXPLAIN FORMATTED` from DataFrame pipelines.
- Common PySpark anti-patterns: unnecessary `collect()`, unnecessary UDFs,
  wide rows, repeated actions, weak join validation, and SQL-string overuse.
- Mini-project checkpoint requiring both Spark SQL and PySpark DataFrame
  solutions.

## Assets Added

- `datasets/module_03/transactions.csv`
- `datasets/module_03/population_history.csv`
- `knowledge/module_03/`
- `curriculum/module_03/`
- `exercises/module_03/`
- `notebooks/module_03/`
- `checkpoints/module_03/`
- `prompts/module_03/`
- `career_artifacts/module_03/`

## Current Assessment

- Hours invested by learner: not yet recorded for Module 03.
- Checkpoint score: not yet attempted.
- Interview score: not yet attempted.
- Module status: in progress.

## Topics Covered So Far

- Why DataFrames exist if Spark already supports SQL.
- SQL and DataFrames as two API layers over the same Spark planning and
  execution engine.
- When SQL is clearer versus when DataFrames are clearer.
- Transformations versus actions.
- DataFrame immutability.
- Column expressions as deferred Spark expressions, not immediate Python
  values.
- Built-in Spark functions versus Python UDFs at a conceptual level.
- `select()` as projection / row-width reduction.
- `filter()` as SQL `WHERE` / row-count reduction.
- Column pruning observed in `EXPLAIN FORMATTED`.
- Pushed filters observed in `EXPLAIN FORMATTED`.
- `withColumn()` for derived columns using `F.year`, `F.round`, and `F.when`.
- Catalyst as Spark SQL's optimizer for SQL and DataFrame plans.
- Aggregation with `groupBy().agg()`.
- Partial aggregate, `Exchange hashpartitioning(...)`, and final aggregate in
  a DataFrame physical plan.
- Catalyst pruning unused derived columns from an upstream logical plan.
- Troubleshooting a Py4J `ConnectionRefusedError` caused by a dead Spark JVM /
  stale notebook kernel, not bad aggregation syntax.

## Current Resume Point

Continue in Trainer Mode at Module 03 joins:

- Notebook: `notebooks/module_03/04_joins_windows.ipynb`
- Lesson: `curriculum/module_03/lesson_06_joins.md`
- Exercise: `exercises/module_03/exercise_06_joins.md`

Start with this pipeline:

```python
profile = (
    transactions
    .join(
        municipalities.select("municipality_id", "municipality_name", "canton"),
        "municipality_id",
        "inner",
    )
    .join(property_values, "municipality_id", "left")
    .select(
        "transaction_id",
        "municipality_id",
        "municipality_name",
        "canton",
        "sale_price",
        "sale_date",
        "property_type",
        "property_value_index",
    )
)
```

Ask the learner to reason before running code:

1. What does this return logically?
2. What join cardinality is expected if `municipalities` and
   `property_values` each have one row per `municipality_id`?
3. What physical join strategies might Spark choose?
4. Why is the final `.select(...)` useful?
