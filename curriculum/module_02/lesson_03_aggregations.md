# Aggregations

## Objectives

- Write GROUP BY queries.
- Connect aggregations to shuffle reasoning.
- Validate aggregate results.

## Reading References

- `knowledge/module_02/04_aggregations.md`

## Exercises

- `exercises/module_02/exercise_03_count_by_canton.md`
- `exercises/module_02/exercise_04_average_accessibility_by_canton.md`

## Mentor Guidance

Start by asking the learner what they expect Spark to do physically. Only then run the query. Keep steering the discussion from syntax toward partitions, scans, joins, shuffles, sorting, and action-triggered execution.

## Reflection Questions

- Which grouping keys might create skew?
- What does partial aggregation buy Spark?

## Interview Questions

- Why can GROUP BY trigger data movement in Spark?

## Completion Standard

The learner should answer with both SQL correctness and Spark execution reasoning. A correct query with no explanation of plan shape is not complete for this module.

