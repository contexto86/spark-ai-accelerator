# Lesson 01: Why Spark Exists

## Learning objective

Develop a decision-oriented explanation of Spark: the distributed coordination
problem it solves, the costs it introduces, and the conditions under which it
is a better choice than PostgreSQL or pandas.

## Predict before reading

For each workload, choose PostgreSQL, pandas, or Spark and name the limiting
factor:

1. Explore a 1.5 GB campaign extract interactively.
2. Serve indexed customer balances with transactional updates.
3. Join 4 TB of events to 600 GB of history inside a two-hour batch window.

Now predict what engineering responsibilities appear when workload 3 moves
from one machine to a cluster.

## Knowledge references

- `knowledge/module_01/01_why_spark_exists.md`
- `knowledge/module_01/02_postgres_vs_pandas_vs_spark.md`
- `knowledge/module_01/07_when_not_to_use_spark.md`

Read them while testing your initial choices. Revise a choice only when you can
state the evidence that changed it.

## Practical example

A logistics company receives 3 TB of daily scans and GPS pings. It must
deduplicate events, join route metadata, and aggregate delivery performance by
depot. Spark is plausible because the bulk scan, join, and aggregation can be
partitioned, the SLA requires parallelism, and failed tasks should be retried.
Spark is not necessarily the serving layer: the final depot metrics may be
published to PostgreSQL or a warehouse.

## Exercise

Complete `exercises/module_01/exercise_01.md`. For the final scenario, produce a
short architecture decision record rather than a product slogan.

## Reflection questions

- Which constraint justifies distribution in your own largest pipeline?
- What is the largest intermediate state, not merely the raw input?
- What would have to become true before you replaced a single-node solution
  with Spark?
- Which operational costs would be easy for your team to underestimate?

