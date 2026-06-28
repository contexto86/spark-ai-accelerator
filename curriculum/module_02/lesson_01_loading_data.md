# Loading Data

## Objectives

- Read CSV data into Spark DataFrames.
- Inspect schema and row counts.
- Explain lazy loading versus action-triggered scans.

## Reading References

- `knowledge/module_02/01_spark_sql_overview.md`
- `knowledge/module_02/02_loading_data.md`

## Exercises

- `exercises/module_02/exercise_01_load_csv_data.md`

## Mentor Guidance

Start by asking the learner what they expect Spark to do physically. Only then run the query. Keep steering the discussion from syntax toward partitions, scans, joins, shuffles, sorting, and action-triggered execution.

## Reflection Questions

- What did Spark know before you called an action?
- Why can schema inference be convenient but risky?

## Interview Questions

- How does reading a CSV in Spark differ from loading rows into PostgreSQL?

## Completion Standard

The learner should answer with both SQL correctness and Spark execution reasoning. A correct query with no explanation of plan shape is not complete for this module.

