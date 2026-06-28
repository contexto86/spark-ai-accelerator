# Window Functions

Window functions answer ranking and within-group comparison questions while preserving row-level detail. A strong SQL engineer can learn Spark SQL quickly, but only if they keep asking a different question: where will this data live while the query runs? In PostgreSQL, the query usually runs inside one database engine that owns storage, indexes, memory, statistics, and transaction semantics. In Spark, a SQL statement becomes a logical plan that is executed by many tasks across partitions. The syntax can look ordinary while the runtime behavior is distributed.

## Mental Model

Think of Spark SQL as a planning layer over distributed DataFrames. You write a query, Spark parses it, resolves table and column names, optimizes the logical plan, selects a physical plan, and launches tasks only when an action asks for results. A temporary view is not a table copy; it is a name that points to a plan. A CSV read is not automatically a full scan; it creates a DataFrame description and schema. A join is not just a relational operator; it may require repartitioning both sides by the join key unless Spark can broadcast one side.

A useful picture is:

```text
SQL text
  -> parsed logical plan
  -> analyzed logical plan
  -> optimized logical plan
  -> physical plan
  -> jobs, stages, tasks, and shuffles
```

This is the thread that ties the module together. SQL is the expression of intent. The plan is Spark's interpretation of that intent. Jobs and stages are the operational consequence.

## Example

Assume four CSV files: municipalities, accessibility scores, point-of-interest counts, and property value indexes. A query like this feels like ordinary analytics SQL:

```sql
SELECT m.canton,
       COUNT(*) AS municipalities,
       AVG(a.accessibility_score) AS avg_accessibility
FROM municipalities m
JOIN accessibility_scores a USING (municipality_id)
GROUP BY m.canton;
```

The relational meaning is simple: match rows by municipality, then aggregate by canton. Spark has to answer physical questions before work can complete. Are both inputs already partitioned by municipality_id? Is one side small enough to broadcast? Does the aggregation require moving rows with the same canton to the same reducer task? How many shuffle partitions will be created? These are not syntax questions; they are execution questions.

## Engineering Trade-Offs

For this topic, the trade-off is between the productivity of declarative SQL and the operational reality of distributed execution. The practical trade-off is that Spark can scale beyond one machine, but it pays coordination costs. Reading many tiny files can create overhead. A wide aggregation can trigger a shuffle. A join can be cheap when one side is broadcast or expensive when both large sides must move. A window function can be expressive but may require partition-level sorts. Spark SQL rewards the engineer who can separate business logic from data movement.

The goal is not to avoid shuffles at all costs. Shuffles are how distributed systems group related records. The goal is to notice them, predict them, and decide whether they are justified by the analytical question. If the data is small and already fits comfortably in PostgreSQL, PostgreSQL may be the better system. If the data is large, semi-structured, file-based, or part of a batch lakehouse workflow, Spark SQL may be exactly the right tool.

## How To Reason During Development

Start with the narrowest correct query. Load the source with explicit schema when the data matters. Create temporary views for readability. Validate row counts before and after joins. Use GROUP BY carefully and ask which keys force records together. Use window functions when you need row-level output plus within-group ranking. Run EXPLAIN before assuming performance. In the plan, look for scans, filters, joins, aggregates, Sort, Exchange, BroadcastExchange, and AdaptiveSparkPlan.

A good development loop is:

1. State the business question in plain language.
2. Write the simplest correct SQL.
3. Run it on the small module dataset.
4. Inspect the result for row-count and join-shape mistakes.
5. Run EXPLAIN FORMATTED.
6. Identify where Spark scans, moves, joins, sorts, and aggregates data.
7. Explain the plan aloud using Spark architecture vocabulary.

## Interview Notes

Interviewers do not need you to recite every Catalyst optimizer rule. They want evidence that you understand SQL on a distributed execution engine. Strong answers connect SQL operators to Spark mechanics. For example: a GROUP BY often creates partial aggregates per partition, then shuffles by grouping key, then performs final aggregation. A join may become a broadcast hash join if one side is small enough; otherwise Spark often shuffles data by join key. A temp view is session-scoped metadata over a DataFrame, not a durable table. EXPLAIN is how you verify the plan rather than guessing.

A concise practitioner answer sounds like this: "The SQL describes the result, but Spark still has to choose a distributed physical plan. I would check scans, filters, join strategy, exchanges, and aggregations in EXPLAIN. If I see Exchange, I know Spark is moving data across partitions. That may be necessary, but it is the point where cost and failure risk increase."

## Reflection Questions

- Which part of this topic is pure relational logic, and which part is distributed execution?
- Where might Spark create a shuffle?
- What would PostgreSQL do differently because it owns a single-node storage and execution environment?
- What evidence would you use from EXPLAIN before changing the query?

