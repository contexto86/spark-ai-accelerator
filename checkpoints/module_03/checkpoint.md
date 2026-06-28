# Module 03 Checkpoint: PySpark DataFrames

Complete without guidance and without reading solution material.

## Mini Project

Create a municipality performance report using Module 02 and Module 03 datasets.

Requirements:

1. Load all required datasets with explicit schemas.
2. Create both SQL temp views and DataFrame variables.
3. Join municipalities, transactions, accessibility scores, POI counts, property values, and 2025 population history where useful.
4. Create calculated columns such as sale year, sale price in millions, and price band.
5. Aggregate by canton and property type.
6. Rank municipalities within each canton by average sale price or performance score.
7. Filter to a meaningful top-N output.
8. Produce both a Spark SQL solution and a PySpark DataFrame solution.
9. Run `EXPLAIN FORMATTED` on both and compare the physical plans.
10. Review the DataFrame code for unnecessary `collect()`, UDFs, wide rows, unclear joins, and unnecessary shuffles.

## Oral Questions

- Why do SQL and DataFrame code often produce similar Spark plans?
- What is a Column expression?
- Why are DataFrames immutable?
- What is the difference between transformation and action?
- Why can built-in functions outperform Python UDFs?
- How do you validate a DataFrame join did not multiply rows?
- When would SQL be clearer than DataFrames?
- When would DataFrames be clearer than SQL?

## Pass Criteria

Pass requires correct SQL and DataFrame implementations, clear plan interpretation, and practical code review reasoning. A passing answer must discuss execution behavior, not just syntax.

## Scoring

- 9-10: Correct implementation, strong translation fluency, clear plan and code-review reasoning.
- 7-8: Correct core implementation with minor syntax or explanation gaps.
- 5-6: Partial implementation, weak translation or plan reasoning.
- 0-4: Cannot express core transformations or explain execution.
