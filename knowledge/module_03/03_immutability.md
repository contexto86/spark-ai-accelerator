# Immutability


PySpark DataFrames are immutable. A transformation does not edit an existing DataFrame; it returns a new DataFrame with a new logical plan. This is different from many local Python workflows where an object can be modified in place. In Spark, immutability supports reproducible planning, lineage tracking, retries, and optimizer reasoning.

If you write `df.filter(F.col("population") > 100000)`, Spark returns a filtered DataFrame. If you do not store it, the result is discarded. The original `df` still represents the original input. This can feel verbose at first, but it encourages clear naming: `large_municipalities = municipalities.filter(...)` communicates intent and gives later reviewers a stable point in the transformation pipeline.

Immutability also helps failure recovery. Spark can recompute a lost partition from lineage because each step is a deterministic description of how to derive the next DataFrame. That does not mean every transformation is free; it means the plan is declarative and replayable until an action materializes it.

The trade-off is that a careless notebook can create many similarly named DataFrames and confuse the reader. Prefer names that describe business state, not implementation trivia. `ranked_municipalities` is clearer than `df2`. For reusable code, wrap transformations in functions that accept a DataFrame and return a DataFrame.

A good code review question is: does each intermediate DataFrame represent a meaningful state? If yes, name it. If not, chain the transformation. Also check that no one expects `withColumn` or `drop` to mutate an existing object. They never do.

Interview note: say that immutability means transformations return new logical plans. It supports lazy execution, optimizer reasoning, lineage, and retries. The practical habit is to assign meaningful intermediate names or compose transformations cleanly.
