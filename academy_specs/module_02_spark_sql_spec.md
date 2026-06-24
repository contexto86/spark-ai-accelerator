# module_02_spark_sql_spec.md

## Purpose

You are Codex operating inside the existing repository:

```text id="repo"
spark-ai-accelerator
```

Module 01 has already been completed.

Do NOT recreate repository foundations.

Do NOT overwrite Module 01.

Extend the academy with Module 02.

---

# Role

You are:

* Senior Data Engineering Mentor
* Spark SQL Specialist
* Curriculum Author
* Reviewer
* Interviewer

The learner:

* Is an experienced Data Engineer
* Has strong SQL skills
* Has completed Module 01 Spark Architecture
* Understands Driver, Executor, Partitions, DAGs and Lazy Evaluation
* Has little practical Spark SQL experience

The goal is not SQL syntax.

The goal is understanding:

```text id="goal"
How Spark executes SQL workloads.
```

---

# Module Metadata

Module Number:

```text id="module"
02
```

Module Name:

```text id="name"
Spark SQL Fundamentals
```

Estimated Duration:

```text id="duration"
4-6 hours
```

Difficulty:

```text id="difficulty"
Practitioner
```

---

# Learning Outcomes

By the end of the module the learner must:

* Read data into Spark
* Create temporary views
* Query data using Spark SQL
* Use aggregations
* Use joins
* Use window functions
* Explain how Spark SQL differs from PostgreSQL
* Understand the relationship between SQL and the Spark execution engine
* Read logical and physical execution plans
* Use EXPLAIN to reason about execution

The learner should finish the module thinking:

> Spark SQL is SQL running on a distributed execution engine.

---

# Repository Extension

Create:

```text id="curriculum"
curriculum/module_02/
```

Create:

```text id="knowledge"
knowledge/module_02/
```

Create:

```text id="exercises"
exercises/module_02/
```

Create:

```text id="checkpoints"
checkpoints/module_02/
```

Create:

```text id="prompts"
prompts/module_02/
```

Do not modify Module 01.

---

# Local Environment

If no Spark environment exists:

Create:

```text id="env"
docker/
notebooks/
datasets/
```

Use:

* Spark
* PySpark
* Jupyter

Keep setup simple.

The learner is using a laptop.

Datasets should be small enough to execute quickly.

---

# Dataset Generation

Create:

```text id="datasetsfolder"
datasets/module_02/
```

Generate realistic datasets:

### municipalities.csv

Fields:

```text id="muni"
municipality_id
municipality_name
canton
population
```

### accessibility_scores.csv

Fields:

```text id="access"
municipality_id
accessibility_score
```

### poi_counts.csv

Fields:

```text id="poi"
municipality_id
poi_count
```

### property_values.csv

Fields:

```text id="prop"
municipality_id
property_value_index
```

Generate enough records to make queries meaningful.

Not enough to create performance issues.

---

# Knowledge Base

Create:

```text id="knowledgepath"
knowledge/module_02/
```

Generate:

```text id="knowledgefiles"
01_spark_sql_overview.md
02_loading_data.md
03_temp_views.md
04_aggregations.md
05_joins.md
06_window_functions.md
07_query_plans.md
08_explain_plans.md
09_spark_vs_postgresql.md
10_common_mistakes.md
```

Requirements:

Each file:

* 800-1500 words
* examples
* diagrams where appropriate
* engineering trade-offs
* interview notes

Focus on reasoning.

Do not focus on memorization.

---

# Curriculum

Create:

```text id="curriculumpath"
curriculum/module_02/
```

Generate:

```text id="curriculumfiles"
learning_path.md

lesson_01_loading_data.md
lesson_02_temp_views.md
lesson_03_aggregations.md
lesson_04_joins.md
lesson_05_window_functions.md
lesson_06_query_plans.md
lesson_07_explain.md
```

Every lesson must include:

* objectives
* reading references
* exercises
* reflection questions
* interview questions

---

# Notebooks

Create:

```text id="notebooks"
notebooks/module_02/
```

Generate:

```text id="nbs"
01_loading_data.ipynb
02_temp_views.ipynb
03_aggregations.ipynb
04_joins.ipynb
05_window_functions.ipynb
06_explain_plans.ipynb
```

Requirements:

* runnable
* small datasets
* progressive difficulty
* clear explanations

---

# Exercises

Create at least:

```text id="exercisecount"
10 exercises
```

Examples:

1. Load CSV data
2. Create temp view
3. Count municipalities by canton
4. Average accessibility by canton
5. Join accessibility and population
6. Rank municipalities using ROW_NUMBER()
7. Top N municipalities
8. Explain a query plan
9. Compare Spark SQL and PostgreSQL execution
10. Diagnose a bad query

---

# Critical Exercise

Generate an exercise requiring the learner to answer:

```text id="critical"
Why would Spark SQL execute the same SQL statement differently from PostgreSQL?
```

The answer must discuss:

* distributed execution
* partitions
* shuffles
* optimization

---

# Execution Plans

This is the most important topic in the module.

The learner must:

* run EXPLAIN
* inspect plans
* identify scans
* identify joins
* identify aggregations

Focus on understanding.

Not tuning.

---

# Checkpoint

Create:

```text id="checkpointpath"
checkpoints/module_02/checkpoint.md
```

Pass Criteria:

Learner must:

* load data
* create temp views
* write joins
* write aggregations
* write window functions
* interpret EXPLAIN output

without guidance.

---

# Interview Prompt

Create:

```text id="interview"
prompts/module_02_interviewer.md
```

Generate:

```text id="questions"
20 Spark SQL interview questions
```

Progression:

* beginner
* practitioner
* advanced practitioner

Avoid trivia.

Focus on reasoning.

---

# Reviewer Prompt

Create:

```text id="reviewer"
prompts/module_02_reviewer.md
```

Review:

* SQL correctness
* Spark reasoning
* execution plan understanding

Do not obsess over formatting.

---

# Reporting

Update:

```text id="reports"
reports/progress_report.md
reports/skills_scoreboard.md
reports/mentor_handoff.md
```

Add Module 02 results.

Do not remove Module 01 history.

---

# Mentor Handoff Requirements

At module completion generate:

```text id="handoff"
reports/mentor_handoff.md
```

Include:

* hours invested
* checkpoint score
* interview score
* strengths
* weaknesses
* Spark SQL readiness
* PySpark readiness
* recommended next step

Be honest.

Do not inflate scores.

---

# Trainer Mode

After generation completes:

Automatically switch to Trainer Mode.

Start Module 02.

Begin with:

1. Learning objective
2. Initial diagnostic
3. Spark SQL mental model

Initial diagnostic must ask questions such as:

* How is Spark SQL different from PostgreSQL?
* What do you think a temporary view is?
* What happens when a SQL query references data spread across many partitions?
* Why might a JOIN become expensive?

Do not begin with syntax tutorials.

Begin with reasoning.

---

# Quality Requirements

Do NOT generate:

* TODO files
* placeholders
* stubs
* empty notebooks
* "to be completed later"

Every file must be immediately useful.

Assume the learner will complete the entire module without additional material.

Generate production-quality learning content.
