# Selecting Columns


Selecting columns in DataFrames maps to SQL projection. `df.select("municipality_id", "canton")` is the DataFrame equivalent of `SELECT municipality_id, canton FROM ...`. Projection is one of the simplest and most important performance habits in Spark because it controls row width.

Wide rows make expensive operators heavier. If you carry unnecessary columns through joins, exchanges, sorts, and writes, Spark moves and stores more bytes than needed. The optimizer can prune columns in many cases, especially with columnar formats like Parquet, but writing code with explicit projection makes intent clear and helps reviewers see the data shape.

Projection can also compute expressions: `transactions.select("municipality_id", (F.col("sale_price") / 1000).alias("sale_price_k"))`. This maps to a `Project` node in the plan. A `Project` is usually helpful before expensive operators because it narrows or reshapes rows.

Avoid `SELECT *` habits in DataFrame form too. `df.select("*")` or carrying whole joined DataFrames forward is rarely ideal in production code. After a join, select the columns you actually need and disambiguate names. This prevents accidental duplicate columns, ambiguous references, and unnecessary shuffle payload.

A clean pattern is: load with schema, select contract columns, filter rows, then join or aggregate. This keeps the plan easy to inspect. If a downstream consumer needs a wide export, widen late rather than early.

Interview note: projection reduces row width; filtering reduces row count. Both can improve performance, but they solve different problems. A strong Spark engineer tries to project before joins, shuffles, sorts, and writes.
