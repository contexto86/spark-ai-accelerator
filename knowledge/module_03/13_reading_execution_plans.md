# Reading Execution Plans from DataFrame Code


DataFrame code can and should be inspected with `explain("formatted")`. The syntax may be Python, but the plan still reveals scans, filters, projections, joins, exchanges, aggregates, windows, sorts, and adaptive execution.

Start from the top-level shape, then inspect expensive boundaries. Look for `Scan` nodes and confirm schemas, pushed filters, and selected columns. Look for `Project` nodes and check whether row width is reduced before joins or shuffles. Look for join nodes and identify whether Spark chose `BroadcastHashJoin` or `SortMergeJoin`. Look for `Exchange` nodes because they indicate data movement.

Aggregations often show partial and final `HashAggregate` nodes. Windows often show `Sort`, `Window`, and sometimes `WindowGroupLimit`. Global ordering often shows range partitioning followed by sort. Adaptive plans may show `AdaptiveSparkPlan`, meaning Spark can revise some decisions during runtime.

Do not read plans as trivia. Read them as operational evidence. If a query is slow, ask where data is scanned, where rows get wider or narrower, where data moves, where sorting happens, and whether the join strategy matches the data sizes.

Comparing SQL and DataFrame plans is a powerful learning exercise. If both versions express the same logic, their optimized plans may be very similar. If they differ, the difference often reveals a semantic mismatch or a missed projection/filter.

Interview note: a strong plan-reading answer names operators and explains why they matter. `Exchange` means data movement. `BroadcastExchange` means a relation is copied to executors. `Sort` means ordering cost. `Project` is row shaping. `HashAggregate partial/final` is local combine plus global merge.
