# Window Functions

## Objectives

- Use ROW_NUMBER for ranking.
- Partition windows by canton.
- Explain sort and partition requirements.

## Reading References

- `knowledge/module_02/06_window_functions.md`

## Exercises

- `exercises/module_02/exercise_06_rank_with_row_number.md`
- `exercises/module_02/exercise_07_top_n_municipalities.md`

## Mentor Guidance

Start by asking the learner what they expect Spark to do physically. Only then run the query. Keep steering the discussion from syntax toward partitions, scans, joins, shuffles, sorting, and action-triggered execution.

## Reflection Questions

- Why does a window keep row detail?
- Where might sorting appear in the plan?

## Interview Questions

- How is GROUP BY different from ROW_NUMBER OVER (PARTITION BY ...)?

## Completion Standard

The learner should answer with both SQL correctness and Spark execution reasoning. A correct query with no explanation of plan shape is not complete for this module.

