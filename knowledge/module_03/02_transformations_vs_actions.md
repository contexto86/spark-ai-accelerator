# Transformations vs Actions


DataFrame code is lazy. Most methods return a new DataFrame that describes an additional transformation; they do not immediately scan data. Examples include `select`, `filter`, `withColumn`, `join`, `groupBy`, and `orderBy`. Actions ask Spark to materialize a result: `show`, `count`, `collect`, `take`, `write`, and many display operations in notebooks.

This distinction matters because a long DataFrame chain is usually plan construction, not immediate execution. Spark waits until an action, then optimizes the entire lineage. That is why it can push filters near scans, remove unused columns, combine projections, and choose join strategies. If every transformation executed immediately, Spark would lose many optimization opportunities.

For example, `df.select("id", "price").filter("price > 0")` builds a plan. `df.count()` launches a job. `df.show(10)` launches a job. `df.write.parquet(path)` launches a job. `df.printSchema()` mostly inspects metadata. Some operations can trigger work indirectly, such as schema inference while reading CSV, but the mental model remains: transformations define; actions execute.

A common bug is running multiple actions on the same expensive lineage and accidentally recomputing it. If a joined and aggregated DataFrame feeds three downstream actions, Spark may recompute the upstream work for each action unless the result is cached or written. Caching is useful only when the materialized result is reused and fits the memory/storage budget. It is not a magic performance button.

The DataFrame API makes laziness visible through immutability. `df.filter(...)` returns a new DataFrame. If you do not assign it or chain it, the original `df` is unchanged. This catches people coming from mutable data-frame libraries where operations may modify an object in place.

Interview note: explain transformations and actions through execution. Transformations build lineage and let Catalyst optimize. Actions trigger jobs, stages, and tasks. A practical engineer checks actions in notebooks because repeated `show()` and `count()` calls can be expensive on real data.
