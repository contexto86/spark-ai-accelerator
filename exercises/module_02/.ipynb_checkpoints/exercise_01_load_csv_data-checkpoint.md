# Load CSV Data

## Task

Load all four CSV datasets with header and inferred schema. Print schema and row count for each dataset. Explain what happens lazily and what actions force execution.

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

