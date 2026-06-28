# Interview Notes


PySpark DataFrame interviews usually test whether you understand distributed execution behind the API. Syntax matters, but not as much as explaining why an operation is lazy, why a join shuffles or broadcasts, why a UDF can be costly, and why `collect()` is dangerous.

A good answer often starts with semantics, then execution. For example: `groupBy("canton").agg(avg("sale_price"))` computes one row per canton. Physically, Spark can partially aggregate per partition, exchange by canton, then finalize the average from sum and count states.

When asked SQL versus DataFrames, avoid choosing a universal winner. Say both build Spark logical plans. SQL is concise for declarative analytics and easy for SQL-heavy teams. DataFrames are better for composable application code, reusable functions, tests, and conditional transformation pipelines.

When asked about performance, do not jump straight to configuration. Inspect the query shape first: scans, filters, projections, join cardinality, join strategy, exchanges, sorts, skew, row width, and actions. Then consider settings such as shuffle partitions or broadcast thresholds.

When asked about UDFs, say they are useful but should not be the default. Built-ins are usually faster because Spark can optimize them. UDFs can hide logic and add serialization overhead.

When asked to review code, focus on correctness, readability, Spark idioms, unnecessary shuffles, unnecessary collects, unnecessary UDFs, and whether the code validates assumptions.

A concise closing line for this module: DataFrames are not local Python data structures; they are a typed, composable way to build Spark plans.
