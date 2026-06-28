# EXPLAIN and PostgreSQL Comparison

## Objectives

- Use EXPLAIN FORMATTED.
- Compare Spark SQL and PostgreSQL execution.
- Diagnose bad query shapes.

## Reading References

- `knowledge/module_02/08_explain_plans.md`
- `knowledge/module_02/09_spark_vs_postgresql.md`
- `knowledge/module_02/10_common_mistakes.md`

## Exercises

- `exercises/module_02/exercise_09_compare_spark_sql_postgresql.md`
- `exercises/module_02/exercise_10_diagnose_bad_query.md`

## Mentor Guidance

Start by asking the learner what they expect Spark to do physically. Only then run the query. Keep steering the discussion from syntax toward partitions, scans, joins, shuffles, sorting, and action-triggered execution.

## Reflection Questions

- What would PostgreSQL likely do differently?
- Which problem is syntax, and which is physical execution?

## Interview Questions

- Why would Spark SQL execute the same SQL statement differently from PostgreSQL?

## Completion Standard

The learner should answer with both SQL correctness and Spark execution reasoning. A correct query with no explanation of plan shape is not complete for this module.

