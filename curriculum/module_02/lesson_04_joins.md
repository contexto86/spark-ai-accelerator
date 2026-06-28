# Joins

## Objectives

- Join multiple module datasets.
- Check row counts and join keys.
- Reason about broadcast and shuffle joins.

## Reading References

- `knowledge/module_02/05_joins.md`

## Exercises

- `exercises/module_02/exercise_05_join_accessibility_population.md`

## Mentor Guidance

Start by asking the learner what they expect Spark to do physically. Only then run the query. Keep steering the discussion from syntax toward partitions, scans, joins, shuffles, sorting, and action-triggered execution.

## Reflection Questions

- What makes a join expensive?
- How would duplicate join keys change results?

## Interview Questions

- Why might two correct join queries have different physical plans?

## Completion Standard

The learner should answer with both SQL correctness and Spark execution reasoning. A correct query with no explanation of plan shape is not complete for this module.

