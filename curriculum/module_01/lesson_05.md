# Lesson 05: DAGs, Stages, and Tasks

## Learning objective

Translate a high-level transformation into a likely execution graph and use
shuffle boundaries to reason about cost and failure.

## Predict before reading

For this pipeline, mark likely narrow and wide operations:

```text
read trips -> filter valid -> join customers -> group by region -> write
```

Draw one version where both join inputs are large and another where customers
can be broadcast. Predict how the stage graph changes.

## Knowledge reference

- `knowledge/module_01/06_dags.md`

## Practical example

Trips are partitioned by date, but the join requires `customer_id`, and the
final aggregation requires `region`. A shuffle join may redistribute both
inputs by customer, followed by another redistribution by region. Filtering
invalid trips before the first exchange reduces network and disk cost.
Broadcasting a sufficiently small customer table may remove the first large
shuffle, but consumes memory on each executor.

## Exercise

Complete `exercises/module_01/exercise_02.md`. Include an ASCII DAG and identify
where a lost executor could force upstream recomputation.

## Reflection questions

- Why does a shuffle usually divide stages?
- How can one slow upstream task delay many downstream tasks?
- What is the difference between an orchestration DAG and a Spark execution
  DAG?
- Which physical-plan choice would most change your predicted graph?

