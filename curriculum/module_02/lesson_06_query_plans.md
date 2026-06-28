# Query Plans

## Objectives

- Read logical and physical plans.
- Identify scans, joins, aggregates, and exchanges.
- Map plans back to Module 01 concepts.

## Reading References

- `knowledge/module_02/07_query_plans.md`
- `knowledge/module_02/08_explain_plans.md`

## Exercises

- `exercises/module_02/exercise_08_explain_query_plan.md`

## Mentor Guidance

Start by asking the learner what they expect Spark to do physically. Only then run the query. Keep steering the discussion from syntax toward partitions, scans, joins, shuffles, sorting, and action-triggered execution.

## Reflection Questions

- Which plan node tells you data moved?
- How do stages relate to Exchange boundaries?

## Interview Questions

- Walk me through a Spark SQL physical plan.

## Completion Standard

The learner should answer with both SQL correctness and Spark execution reasoning. A correct query with no explanation of plan shape is not complete for this module.

