# Exercise 02: Architecture Comparison

**Purpose:** Select PostgreSQL, pandas, or Spark from workload shape.

## Workloads

For each workload, choose a primary execution system and defend the choice:

1. A notebook explores a 3 GB sample and creates charts.
2. An API reads and updates account state with transactional guarantees and a
   50 ms latency target.
3. A nightly job joins 3 TB of events with 400 GB of history.
4. A 120 GB aggregation runs weekly and completes in 20 minutes on one
   inexpensive server; the SLA is two hours.
5. Data already resides in PostgreSQL; an indexed query touches 0.1% of rows.
6. A 1 TB object-store dataset must be scanned, filtered, and written in
   partitioned columnar form after any worker failure.

## Deliverable

Create a decision table with these columns:

| Workload | Choice | Deciding constraint | Rejected alternative | Evidence that could reverse decision |
|---|---|---|---|---|

Then design a hybrid architecture using all three systems for a product
analytics platform. State the responsibility and data boundary of each system.

## Challenge

Someone argues: “Spark scales, so using it now avoids a future migration.”
Respond in 200 words. Compare present coordination cost with projected scale
and explain how you would define a measurable migration threshold.

## Quality bar

Do not rank systems globally. Show that transactions, latency, data gravity,
working-set size, concurrency, and team operations can outweigh raw scale.

