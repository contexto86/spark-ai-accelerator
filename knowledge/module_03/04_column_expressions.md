# Column Expressions


A PySpark `Column` is not a local Python value. It is an expression in a Spark logical plan. `F.col("sale_price") * 1.05` does not multiply a Python number immediately; it describes an expression Spark executors will evaluate for each row when an action runs.

This is the source of many beginner mistakes. You cannot usually use normal Python `if` statements to branch per Spark row. Use Spark expressions such as `F.when(...).otherwise(...)`. You cannot call arbitrary Python string methods on a Spark column and expect distributed execution. Use built-in functions like `F.upper`, `F.trim`, `F.to_date`, `F.year`, and `F.round`.

Column expressions are composable. You can build a calculated field with `withColumn("price_band", F.when(F.col("sale_price") >= 1000000, "premium").otherwise("standard"))`. Spark sees this as part of the plan and can optimize it with surrounding projections and filters.

The trade-off is readability. Deeply nested column expressions become hard to review. Prefer small named expressions when logic grows. For example, define `is_premium = F.col("sale_price") >= F.lit(1000000)` and use it inside `withColumn`. This keeps the DataFrame API expressive without turning code into a knot.

Column expressions are also safer than string SQL snippets when refactoring Python code. `F.col("municipality_id")` is explicit and works naturally with Python composition. SQL strings are compact but easier to break during dynamic construction. Both are valid; choose based on clarity.

Interview note: a Column is a deferred expression, not data on the driver. Built-in column functions are optimized and executed by Spark. Python control flow controls plan construction, not row-by-row distributed logic.
