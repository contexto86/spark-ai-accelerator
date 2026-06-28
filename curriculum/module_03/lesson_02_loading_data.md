# Loading Data

## Learning Objectives

- Explain the concept behind this lesson in Spark execution terms.
- Translate the related SQL idea into PySpark DataFrame operations.
- Identify whether the work is narrow, wide, lazy, or action-triggered.
- Review the resulting code for correctness, readability, and Spark idioms.

## Reading References

- `knowledge/module_03/02_transformations_vs_actions.md`
- `knowledge/module_03/05_selecting_columns.md`

## Guided Exercises

- `exercises/module_03/exercise_02_load_module_03_data.md`

## Mentor Guidance

Start by asking: "What would you write first?" Require the learner to state the SQL meaning, the expected DataFrame operations, and the likely physical plan shape before implementation.

## Reflection Questions

- What DataFrame operation maps to the SQL concept here?
- Which step is lazy, and which step triggers execution?
- Where might Spark need an `Exchange`?
- Would SQL or DataFrames be clearer for this case, and why?

## Interview Questions

- Explain this operation to a SQL-first data engineer.
- What would you inspect in `EXPLAIN FORMATTED`?
- What code review concern would you raise for a weak implementation?
