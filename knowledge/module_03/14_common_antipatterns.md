# Common Anti-patterns


The most common PySpark anti-pattern is treating Spark like local pandas. Calling `collect()` to process rows in Python moves distributed data to the driver and can cause driver memory failure. Use distributed transformations and writes instead.

Another anti-pattern is using Python loops to run many small Spark jobs. If each iteration filters and counts a DataFrame, Spark may launch a separate job each time. Prefer grouping, aggregation, or a single distributed transformation that expresses the whole problem.

`SELECT *` and broad DataFrame joins are also common. Wide rows increase scan, shuffle, join, sort, spill, and write cost. Project required columns early and select the final schema explicitly after joins.

Unnecessary UDFs are a major issue. They hide logic from Catalyst and can add serialization overhead. Before writing a UDF, search the built-in functions mentally: conditionals, regex, string, date, array, map, struct, and aggregate functions cover many cases.

Repeated actions on the same expensive lineage can recompute work. In notebooks, repeated `count()` and `show()` calls are easy to miss. Cache only when a materialized DataFrame is reused and the storage cost is justified.

Joining without validating cardinality is a correctness anti-pattern. Duplicate keys can multiply rows and bias aggregates. Always check expected counts and duplicate keys when metrics matter.

Interview note: anti-patterns are not about style purity; they are about distributed execution. The code may be syntactically valid but operationally expensive or incorrect.
