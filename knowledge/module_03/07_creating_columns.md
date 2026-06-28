# Creating Columns


`withColumn` adds or replaces a column using a Spark expression. It maps to SQL expressions in the `SELECT` list. For example, `withColumn("sale_year", F.year("sale_date"))` is equivalent to selecting `year(sale_date) AS sale_year`.

Creating columns is powerful because it keeps business logic inside the distributed plan. Use built-in functions for dates, strings, math, conditionals, arrays, and structs. For example, price bands can be expressed with `F.when(F.col("sale_price") >= 1000000, "premium").otherwise("standard")`.

A common anti-pattern is chaining many `withColumn` calls without thinking. Spark can often collapse projections, but the code becomes hard to read. For multiple derived columns, `.select` with original and new expressions can be clearer because the output schema is visible in one place.

Another anti-pattern is replacing columns accidentally. `withColumn("population", ...)` overwrites the existing `population` column in the new DataFrame. That can be correct, but for auditability prefer new names when transforming raw values, such as `population_clean`.

Date handling deserves care. CSV reads dates as strings unless the schema or parsing is explicit. Use `F.to_date("sale_date")` before extracting year or doing date comparisons. Otherwise lexical string behavior can leak into business logic.

Interview note: creating columns should use Spark built-ins whenever possible. The goal is not just syntax; it is keeping the transformation visible to Catalyst so Spark can optimize and execute it across partitions.
