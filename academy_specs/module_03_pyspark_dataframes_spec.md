# module_03_pyspark_dataframes_spec.md

## Purpose

You are Codex operating inside the existing repository:

```
spark-ai-accelerator
```

Modules 01 and 02 have already been completed.

Do NOT recreate previous content.

Extend the academy with Module 03.

---

# Role

You are simultaneously:

* Senior Spark Engineer
* Senior Data Engineering Mentor
* Curriculum Author
* Reviewer
* Interviewer
* Pair Programming Partner

Assume the learner:

* Already understands Spark Architecture.
* Already understands Spark SQL.
* Is comfortable with SQL.
* Is comfortable with Python.
* Is NOT yet comfortable expressing Spark transformations through the DataFrame API.

The objective of this module is NOT Python.

The objective is learning to think in DataFrames.

---

# Module Metadata

Module Number

03

Module Name

PySpark DataFrames and the SQL ↔ DataFrame Mental Model

Estimated Duration

6–8 hours

Difficulty

Practitioner

---

# Primary Learning Goal

By the end of this module the learner should naturally translate between:

SQL

↓

PySpark DataFrames

and

PySpark DataFrames

↓

SQL

without memorizing syntax.

The learner should understand that both APIs ultimately build Spark logical plans.

---

# Repository Extension

Create

```
knowledge/module_03/
curriculum/module_03/
notebooks/module_03/
datasets/module_03/
exercises/module_03/
checkpoints/module_03/
prompts/module_03/
career_artifacts/
```

Do not modify previous modules.

---

# Datasets

Reuse Module 02 datasets.

Additionally generate:

```
transactions.csv
```

Fields

* transaction_id
* municipality_id
* property_id
* sale_price
* sale_date
* property_type

Generate

```
population_history.csv
```

Fields

* municipality_id
* year
* population

Generate realistic synthetic values.

The datasets should allow joins, aggregations, filters and window functions.

---

# Knowledge Base

Generate:

1. DataFrames vs SQL
2. Transformations vs Actions
3. Immutability
4. Column Expressions
5. Selecting Columns
6. Filtering
7. Creating Columns
8. Aggregations
9. Joins
10. Window Functions
11. UDFs (only conceptual)
12. Why built-in functions outperform UDFs
13. Reading Execution Plans from DataFrame code
14. Common Anti-patterns
15. Interview Notes

Each file:

* 800–1500 words
* practical examples
* diagrams where useful
* engineering trade-offs
* interview discussion

---

# Curriculum

Create lessons that progressively cover:

Lesson 1

The DataFrame Mental Model

Lesson 2

Loading Data

Lesson 3

Selecting and Filtering

Lesson 4

Creating Columns

Lesson 5

Aggregations

Lesson 6

Joins

Lesson 7

Window Functions

Lesson 8

Reading Plans

Lesson 9

SQL ↔ DataFrame Translation

Every lesson must contain:

* learning objectives
* reading references
* guided exercises
* reflection questions
* interview questions

---

# Notebook Generation

Generate Jupyter notebooks.

Each notebook must be executable.

Do not leave placeholders.

Use small datasets.

Keep execution fast.

---

# Critical Exercise

This is the core exercise of Module 03.

Generate a workbook containing:

20 SQL queries.

For each query the learner must:

1. Explain what it does.

2. Predict the execution.

3. Write the equivalent DataFrame solution.

4. Compare readability.

5. Explain when SQL would be preferable.

6. Explain when DataFrames would be preferable.

---

# Pair Programming

Throughout the module:

Act as pair programmer.

Do NOT simply provide answers.

Before generating code ask:

"What would you write first?"

Require reasoning before implementation.

---

# Code Review

Every learner solution must be reviewed for:

* correctness
* readability
* Spark idioms
* unnecessary shuffles
* unnecessary collect()
* unnecessary UDFs

Do not review formatting.

Review engineering quality.

---

# Checkpoint

The learner must complete:

A mini project.

Task:

Using the generated datasets:

Create a municipality performance report.

Requirements:

* joins
* aggregations
* calculated columns
* window functions
* ordering
* filtering

Produce both:

Spark SQL

and

PySpark DataFrame

solutions.

---

# Interview

Generate:

20 PySpark interview questions.

Focus on:

* reasoning
* transformations
* actions
* DataFrames
* execution

Avoid trivia.

---

# Career Artifacts

Generate:

career_artifacts/module_03/

Including:

* module_summary.md
* interview_cheatsheet.md
* repo_highlights.md
* cv_bullets.md
* learning_reflection.md

The CV bullets should describe practical Spark capabilities gained through the module without exaggerating production experience.

---

# Reporting

Update:

* progress_report.md
* skills_scoreboard.md
* mentor_handoff.md

The mentor handoff must include:

* Spark SQL confidence
* PySpark confidence
* SQL ↔ DataFrame translation ability
* Code review quality
* Recommended reinforcement
* Readiness for Module 04

---

# Completion

After generation:

Automatically enter Trainer Mode.

Start with a diagnostic discussion.

Do NOT begin by teaching syntax.

First verify the learner understands:

Why DataFrames exist.

How DataFrames relate to SQL.

How Spark sees both APIs internally.

Only then begin practical exercises.

---

# Quality Standard

Do not generate placeholders.

Do not generate TODOs.

Every notebook must run.

Every lesson must be complete.

Every exercise must be immediately usable.

The learner should be able to complete this module without searching the internet.