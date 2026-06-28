# Joins


DataFrame joins map to SQL joins, but the physical strategy matters. `left.join(right, "municipality_id", "inner")` expresses the logical relationship. Spark may execute it as a broadcast hash join, sort-merge join, shuffle hash join, or another strategy depending on size, stats, hints, and configuration.

Broadcast joins are efficient when one side is small enough to copy to each executor. Tasks scanning the larger side can probe the local broadcast relation without shuffling the large side. Sort-merge joins are common for large-to-large joins: Spark repartitions both sides by join key, sorts them, and streams matching keys together.

Join cardinality is the first correctness check. If both sides have one row per `municipality_id`, an inner join should preserve the base count for matched keys. If the right side has duplicate keys, rows multiply. This can silently corrupt counts and averages.

Before joining, project required columns and validate keys. After joining, select the output schema explicitly. This avoids carrying duplicate columns and wide payloads through later stages. For multiple joins, consider building small, validated dimension-like DataFrames first.

Null keys do not match in normal equality joins. Inner joins may show `isnotnull` filters in the physical plan because null join keys cannot produce matches. Left joins preserve left rows but fill right columns with nulls when no match exists.

Interview note: distinguish logical join type from physical join strategy. `inner` and `left` describe semantics. `BroadcastHashJoin` and `SortMergeJoin` describe execution. Good engineers validate cardinality before trusting joined metrics.
