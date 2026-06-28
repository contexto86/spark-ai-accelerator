# Window Functions


Window functions compute values across related rows while preserving row-level output. This is the key difference from `GROUP BY`, which collapses rows. In PySpark, windows are built with `Window.partitionBy(...).orderBy(...)` and functions such as `row_number`, `rank`, `dense_rank`, `sum`, and `avg`.

`partitionBy` in a window is logical grouping for the analytic calculation. It is not the same as Spark physical partitions, although Spark may repartition data by that key to execute the window. `orderBy` inside the window defines the order within each logical group.

A top-N-per-group query is a classic example. Define a window partitioned by canton and ordered by population descending, add `row_number`, then filter rank <= N. The output still contains municipality rows, not one row per canton.

Determinism matters. If two rows tie on the ordering column, `row_number` can assign arbitrary order unless you include a stable tie-breaker. Add `municipality_id` or another deterministic key after the business sort key.

Window functions often require sorting and sometimes exchange. Spark must bring rows from the same logical group together and order them before assigning row numbers or cumulative metrics. For top-N windows, Spark may use `WindowGroupLimit` partial and final stages to reduce candidate rows before a full window calculation.

Interview note: explain windows as row-preserving analytics. `GROUP BY canton` produces one row per canton; `ROW_NUMBER() OVER (PARTITION BY canton ORDER BY population DESC)` keeps municipality rows and adds a rank within each canton.
