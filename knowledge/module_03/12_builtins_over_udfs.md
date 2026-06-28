# Why Built-ins Outperform UDFs


Spark built-in functions usually outperform Python UDFs because Spark understands them. A built-in expression is part of the logical plan. Catalyst can analyze it, simplify it, combine it with other projections, push filters, prune columns, and generate efficient execution code.

Python UDFs often force data to cross from the JVM execution engine into Python worker processes. That adds serialization overhead and can prevent Spark from optimizing inside the function. Spark sees the UDF result type, but not the internal logic. This limits predicate pushdown, constant folding, expression simplification, and code generation opportunities.

For example, categorizing sale prices into bands can be written with `F.when`. Spark can keep that as an expression in the plan. Writing a Python function `def band(price): ...` and registering it as a UDF makes the logic opaque and slower for large datasets.

Built-ins also improve portability and reviewability. Other Spark engineers recognize `to_date`, `year`, `regexp_extract`, `coalesce`, `when`, and aggregate functions. They can inspect the plan and reason about execution. A UDF requires reading custom Python and understanding how Spark invokes it.

There are exceptions. Some domain logic is too complex for built-ins, or the built-in equivalent would be unreadable. In those cases, a UDF can be the pragmatic choice. The engineering standard is to justify the UDF and contain it.

Interview note: built-ins are faster because they stay inside Spark's optimized expression engine. UDFs can add Python serialization and hide logic from Catalyst. Use built-ins first; use UDFs deliberately.
