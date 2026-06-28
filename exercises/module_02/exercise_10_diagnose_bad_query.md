# Diagnose a Bad Query

## Task

A learner joins all datasets, groups by municipality_name, orders globally, and calls collect on the full result. Diagnose correctness, data movement, and driver risk. Propose a better query workflow.

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

