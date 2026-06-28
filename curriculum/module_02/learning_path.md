# Module 02 Learning Path: Spark SQL Fundamentals

**Module:** 02  
**Name:** Spark SQL Fundamentals  
**Estimated duration:** 4-6 hours  
**Difficulty:** Practitioner

Complete sections in order. The purpose is not to memorize SQL syntax. The purpose is to understand how Spark executes SQL workloads on distributed data.

## Sections

### Loading Data

**Objectives:**
- Read CSV data into Spark DataFrames
- Inspect schema and row counts
- Explain lazy loading versus action-triggered scans

**Reading references:** `knowledge/module_02/01_spark_sql_overview.md`, `knowledge/module_02/02_loading_data.md`.

**Exercises:** `exercise_01_load_csv_data.md`.

**Completion check:** Explain what Spark must physically do, not just what the SQL returns.

### Temporary Views

**Objectives:**
- Create temporary views from DataFrames
- Use Spark SQL against views
- Explain session scope and non-persistence

**Reading references:** `knowledge/module_02/03_temp_views.md`.

**Exercises:** `exercise_02_create_temp_view.md`.

**Completion check:** Explain what Spark must physically do, not just what the SQL returns.

### Aggregations

**Objectives:**
- Write GROUP BY queries
- Connect aggregations to shuffle reasoning
- Validate aggregate results

**Reading references:** `knowledge/module_02/04_aggregations.md`.

**Exercises:** `exercise_03_count_by_canton.md`, `exercise_04_average_accessibility_by_canton.md`.

**Completion check:** Explain what Spark must physically do, not just what the SQL returns.

### Joins

**Objectives:**
- Join multiple module datasets
- Check row counts and join keys
- Reason about broadcast and shuffle joins

**Reading references:** `knowledge/module_02/05_joins.md`.

**Exercises:** `exercise_05_join_accessibility_population.md`.

**Completion check:** Explain what Spark must physically do, not just what the SQL returns.

### Window Functions

**Objectives:**
- Use ROW_NUMBER for ranking
- Partition windows by canton
- Explain sort and partition requirements

**Reading references:** `knowledge/module_02/06_window_functions.md`.

**Exercises:** `exercise_06_rank_with_row_number.md`, `exercise_07_top_n_municipalities.md`.

**Completion check:** Explain what Spark must physically do, not just what the SQL returns.

### Query Plans

**Objectives:**
- Read logical and physical plans
- Identify scans, joins, aggregates, and exchanges
- Map plans back to Module 01 concepts

**Reading references:** `knowledge/module_02/07_query_plans.md`, `knowledge/module_02/08_explain_plans.md`.

**Exercises:** `exercise_08_explain_query_plan.md`.

**Completion check:** Explain what Spark must physically do, not just what the SQL returns.

### EXPLAIN and PostgreSQL Comparison

**Objectives:**
- Use EXPLAIN FORMATTED
- Compare Spark SQL and PostgreSQL execution
- Diagnose bad query shapes

**Reading references:** `knowledge/module_02/08_explain_plans.md`, `knowledge/module_02/09_spark_vs_postgresql.md`, `knowledge/module_02/10_common_mistakes.md`.

**Exercises:** `exercise_09_compare_spark_sql_postgresql.md`, `exercise_10_diagnose_bad_query.md`.

**Completion check:** Explain what Spark must physically do, not just what the SQL returns.

## Module Completion

The module is complete when the learner can load data, create temp views, write aggregations, joins, and windows, and interpret EXPLAIN output without guidance. The final verbal model should be: Spark SQL is SQL running on a distributed execution engine.

