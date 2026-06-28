# Filtering


Filtering in DataFrames maps to SQL `WHERE`. Use `.filter(...)` or `.where(...)`; they are aliases. Filters describe predicates Spark can apply to rows, such as `transactions.filter(F.col("sale_price") >= 500000)`.

Filtering is often a narrow transformation. Each partition can drop rows independently without moving data across the cluster. That makes filters valuable before wide operations like joins, aggregations, and sorts. Reducing row count early reduces downstream work.

The best filters are expressed with built-in Spark column functions. Spark can inspect these expressions, push them near scans, and sometimes push them into data sources. With CSV, pushdown is limited compared with Parquet, but Spark can still avoid carrying rows further through the plan. With partitioned Parquet tables, filters on partition columns can avoid reading whole directories.

Be careful with Python-side filtering. Collecting rows to the driver and using Python lists or loops breaks the distributed model. Also be careful with complex UDF predicates; Spark cannot optimize them as well as built-in expressions.

Null semantics matter. `F.col("x") == None` is not the right idiom; use `F.col("x").isNull()` or `.isNotNull()`. SQL-style three-valued logic can surprise people, especially in joins and filters.

Interview note: filters are usually narrow and should be pushed before expensive operations. A practical debugging step is to check whether the filter appears close to the scan in `EXPLAIN FORMATTED` and whether it reduces row count as expected.
