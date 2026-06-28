# Temporary Views

## Objectives

- Create temporary views from DataFrames.
- Use Spark SQL against views.
- Explain session scope and non-persistence.

## Reading References

- `knowledge/module_02/03_temp_views.md`

## Exercises

- `exercises/module_02/exercise_02_create_temp_view.md`

## Mentor Guidance

Start by asking the learner what they expect Spark to do physically. Only then run the query. Keep steering the discussion from syntax toward partitions, scans, joins, shuffles, sorting, and action-triggered execution.

## Reflection Questions

- What does a temp view store?
- When would a managed table be more appropriate?

## Interview Questions

- Is a temporary view a copy of data? Defend your answer.

## Completion Standard

The learner should answer with both SQL correctness and Spark execution reasoning. A correct query with no explanation of plan shape is not complete for this module.

