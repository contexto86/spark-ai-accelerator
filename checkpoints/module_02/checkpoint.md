# Module 02 Checkpoint: Spark SQL Fundamentals

Complete without guidance and without reading the solution material during the attempt.

## Practical Tasks

1. Load all four Module 02 CSV files into Spark DataFrames.
2. Create temporary views for each dataset.
3. Write an aggregation that counts municipalities and sums population by canton.
4. Write a join that combines municipality, accessibility, POI, and property value data.
5. Write a window query that ranks municipalities within each canton.
6. Run EXPLAIN FORMATTED on a join plus aggregation query.
7. Identify scans, joins, aggregations, sorts, and Exchange nodes in the plan.

## Oral Reasoning Questions

- How is Spark SQL different from PostgreSQL?
- What is a temporary view?
- Why can GROUP BY create a shuffle?
- Why might a JOIN become expensive?
- What does an Exchange node usually mean?

## Pass Criteria

Pass requires independent completion of loading, temp views, joins, aggregations, window functions, and EXPLAIN interpretation. A passing answer must include physical execution reasoning, not only working SQL.

## Scoring

- 9-10: Correct code, clear plan interpretation, strong distributed reasoning.
- 7-8: Correct core tasks with minor gaps in plan vocabulary or trade-offs.
- 5-6: Some working SQL but weak understanding of execution behavior.
- 0-4: Cannot complete core SQL tasks or cannot explain Spark-specific behavior.

