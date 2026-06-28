# DataFrames vs SQL


Spark SQL and the PySpark DataFrame API are two ways to build Spark logical plans. SQL starts from a text statement. DataFrames start from Python objects and method calls. The important idea is that Spark does not treat them as two different engines. Both routes end up as Catalyst logical plans, optimized plans, and physical plans with scans, joins, aggregates, exchanges, sorts, and tasks.

A SQL query says `SELECT canton, COUNT(*) FROM municipalities GROUP BY canton`. The DataFrame version says `municipalities.groupBy("canton").count()`. The surface syntax is different, but Spark sees both as a projection, grouping key, aggregate expression, and input relation. This is why `explain("formatted")` is so useful: it lets you compare the plan Spark actually intends to run instead of arguing from syntax.

SQL is often clearer for declarative analytics. It is compact, familiar to analysts, and close to business questions. DataFrames are often stronger when code needs composition, reusable functions, conditional logic, testing, package structure, or integration with Python application code. A production job often uses both: SQL for readable transformations and DataFrames for orchestration, validation, reusable helper functions, and writing outputs.

The trade-off is not SQL versus Python taste. It is maintainability versus control in a specific codebase. SQL can become hard to refactor when queries grow into huge strings with repeated subqueries. DataFrame chains can become unreadable when every expression is nested and no intermediate names explain intent. Good Spark engineers can translate both ways and choose the representation that makes the plan and business logic easiest to review.

A useful translation pattern is: `SELECT` maps to `.select`, `WHERE` maps to `.filter`, `GROUP BY` maps to `.groupBy`, aggregate functions map to `pyspark.sql.functions`, `JOIN` maps to `.join`, `ORDER BY` maps to `.orderBy`, and window functions use `Window.partitionBy(...).orderBy(...)` with functions like `row_number()`.

Interview note: a strong answer says that SQL and DataFrames are APIs over the same Spark optimizer. The API choice affects readability and software engineering ergonomics, but performance should be verified from the physical plan. If SQL and DataFrame code express the same logical operation, Spark can often optimize them similarly.
