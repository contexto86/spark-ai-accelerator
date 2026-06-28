# Count Municipalities by Canton

## Task

Write Spark SQL that returns canton, municipality_count, and total_population ordered by total_population descending. Identify the aggregation key and whether a shuffle is likely.

## Dataset

Use the CSV files in `datasets/module_02/` and the notebooks in `notebooks/module_02/` as runnable references.

## Required Output

- The Spark SQL or PySpark code used.
- A small result sample.
- A written explanation of the physical execution behavior.
- One sentence comparing the behavior to PostgreSQL where relevant.

## Review Rubric

- SQL correctness: result answers the question and uses the expected keys.
- Spark reasoning: answer mentions partitions, shuffles, joins, scans, sorts, or actions where appropriate.
- Communication: explanation is clear enough for another data engineer to follow.

