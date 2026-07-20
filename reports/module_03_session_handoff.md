# Module 03 Session Handoff

**Updated:** July 20, 2026  
**Mode:** Trainer Mode  
**Module:** 03 — PySpark DataFrames and the SQL ↔ DataFrame Mental Model  
**Status:** In progress  
**Estimated coverage:** 25-30%

## Resume instruction

Continue as a senior PySpark mentor. Ask one question at a time and let the
learner reason before explaining. Do not start by teaching syntax. Keep tying
DataFrame API code back to Spark logical plans, Catalyst, physical plans, and
the SQL mental model from Module 02.

## Current position

Resume at **DataFrame joins**.

Use:

- `notebooks/module_03/04_joins_windows.ipynb`
- `curriculum/module_03/lesson_06_joins.md`
- `exercises/module_03/exercise_06_joins.md`

Start from this pipeline:

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

Ask:

1. What does this return logically?
2. What join cardinality is expected if `municipalities` and
   `property_values` each have one row per `municipality_id`?
3. What physical join strategies might Spark choose?
4. Why is the final `.select(...)` useful?

## Topics already covered

- Why DataFrames exist if Spark already supports SQL.
- SQL and DataFrames as two API layers over the same Spark planning and
  execution engine.
- When SQL is clearer versus when DataFrames are clearer.
- Transformations versus actions.
- DataFrame immutability.
- Column expressions as deferred Spark expressions.
- Built-in Spark functions versus Python UDFs conceptually.
- `select()` as projection / row-width reduction.
- `filter()` as SQL `WHERE` / row-count reduction.
- Column pruning observed in `EXPLAIN FORMATTED`.
- Pushed filters observed in `EXPLAIN FORMATTED`.
- `withColumn()` derived columns using `F.year`, `F.round`, and `F.when`.
- Catalyst as Spark SQL's optimizer for both SQL and DataFrame plans.
- Aggregation with `groupBy().agg()`.
- Partial aggregate, `Exchange hashpartitioning(...)`, and final aggregate in
  DataFrame physical plans.
- Catalyst pruning unused derived columns from an upstream logical plan.
- Troubleshooting Py4J `ConnectionRefusedError` as a dead Spark JVM / stale
  notebook session.

## Learner strengths

- Understands that DataFrame transformations build logical plans lazily.
- Understands SQL and DataFrames can produce similar plans when semantics
  match.
- Correctly distinguishes projection from filtering:
  - projection reduces row width
  - filtering reduces row count
- Reads plan evidence concretely:
  - `ReadSchema`
  - `PushedFilters`
  - `Project`
  - partial/final `HashAggregate`
  - `Exchange` keys
- Understands why built-ins are usually preferred over Python UDFs.

## Reinforcement needed

- Be precise that `select()` maps to projection, not reading.
- Be precise that derived columns exist in the logical plan even if they have
  not been physically materialized.
- DataFrame joins are next and not yet assessed.
- DataFrame windows, SQL ↔ DataFrame translation workbook, code review, and
  mini-project checkpoint remain.

## Last assessed answers

- DataFrame versus SQL front doors into Spark: 9/10.
- SQL clarity versus DataFrame clarity: 9/10.
- Transformations and lazy filtering: 8/10.
- Immutability: 8.5/10.
- Column expression: 8/10.
- Built-ins versus UDFs: 7.5/10.
- `withColumn` / derived column plan: 9/10.
- Aggregation prediction: 10/10.
- Aggregation plan read: 8/10.

## Environment note

The learner had a Py4J `ConnectionRefusedError` during aggregation because the
Spark JVM/backend connection died. Restarting the notebook kernel and rerunning
setup/load cells fixed it.

Health check:

```python
spark.range(5).show()
```

## Remaining Module 03 work

- DataFrame joins and join validation.
- DataFrame windows and top-N-per-group.
- Reading more complex DataFrame physical plans.
- SQL ↔ DataFrame translation workbook.
- UDF anti-pattern and code review practice.
- Mini-project checkpoint.
- Final interview/checkpoint.
