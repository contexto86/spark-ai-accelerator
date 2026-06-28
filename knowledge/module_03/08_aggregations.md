# Aggregations


DataFrame aggregations map directly to SQL `GROUP BY`. `df.groupBy("canton").agg(F.count("*").alias("municipalities"))` describes grouped aggregation by canton. Spark typically performs partial aggregation per partition, shuffles partial states by grouping key, then performs final aggregation.

Partial aggregation is a distributed optimization. Instead of moving every raw row across the network, Spark first reduces rows locally. For counts and sums, this can dramatically reduce shuffle volume. For averages, Spark carries sum and count states, then computes the final average after merging.

Not every aggregation has the same cost. Grouping by a low-cardinality key like canton may create a small final result. Grouping by a high-cardinality key like transaction_id may produce almost as many groups as input rows and reduce less data. Grouping by skewed keys can create stragglers when one group is much larger than others.

Use `.agg` with explicit aliases. This makes downstream code cleaner and avoids awkward generated names like `avg(sale_price)`. Example: `transactions.groupBy("municipality_id").agg(F.count("*").alias("transactions"), F.avg("sale_price").alias("avg_sale_price"))`.

Always validate aggregation semantics. `COUNT(*)` counts rows. `COUNT(column)` counts non-null values. `AVG(column)` ignores nulls. In left joins, this distinction often determines whether a metric means all entities or only matched entities.

Interview note: a strong explanation says that aggregation is logical grouping plus physical partial/final work. The expensive boundary is usually the `Exchange` that brings same-key partials together.
