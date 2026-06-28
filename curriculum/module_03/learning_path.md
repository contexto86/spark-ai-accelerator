# Module 03 Learning Path: PySpark DataFrames and the SQL ↔ DataFrame Mental Model

**Module:** 03  
**Name:** PySpark DataFrames and the SQL ↔ DataFrame Mental Model  
**Estimated duration:** 6-8 hours  
**Difficulty:** Practitioner

The purpose is not to memorize PySpark syntax. The purpose is to think in DataFrames while preserving the Spark SQL execution model from Module 02.

## Sections


### The DataFrame Mental Model

References: `knowledge/module_03/01_dataframes_vs_sql.md`, `knowledge/module_03/03_immutability.md`.

Exercises: `exercises/module_03/exercise_01_dataframe_vs_sql.md`.
### Loading Data

References: `knowledge/module_03/02_transformations_vs_actions.md`, `knowledge/module_03/05_selecting_columns.md`.

Exercises: `exercises/module_03/exercise_02_load_module_03_data.md`.
### Selecting and Filtering

References: `knowledge/module_03/05_selecting_columns.md`, `knowledge/module_03/06_filtering.md`.

Exercises: `exercises/module_03/exercise_03_select_filter.md`.
### Creating Columns

References: `knowledge/module_03/04_column_expressions.md`, `knowledge/module_03/07_creating_columns.md`.

Exercises: `exercises/module_03/exercise_04_create_columns.md`.
### Aggregations

References: `knowledge/module_03/08_aggregations.md`.

Exercises: `exercises/module_03/exercise_05_aggregations.md`.
### Joins

References: `knowledge/module_03/09_joins.md`.

Exercises: `exercises/module_03/exercise_06_joins.md`.
### Window Functions

References: `knowledge/module_03/10_window_functions.md`.

Exercises: `exercises/module_03/exercise_07_windows.md`.
### Reading Plans

References: `knowledge/module_03/13_reading_execution_plans.md`, `knowledge/module_03/14_common_antipatterns.md`.

Exercises: `exercises/module_03/exercise_08_explain_dataframe_plan.md`.
### SQL ↔ DataFrame Translation

References: `knowledge/module_03/01_dataframes_vs_sql.md`, `knowledge/module_03/15_interview_notes.md`.

Exercises: `exercises/module_03/exercise_09_sql_dataframe_translation_workbook.md`.

## Completion Standard

The module is complete when the learner can translate realistic SQL into DataFrame code, translate DataFrame code back into SQL intent, explain the physical plan, and review PySpark code for unnecessary collects, UDFs, shuffles, wide rows, and unclear transformation structure.
