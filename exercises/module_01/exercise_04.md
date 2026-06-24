# Exercise 04: Partition Reasoning

**Purpose:** Connect partition design to concurrency, skew, memory, and files.

## Scenario A — Waves

A stage has 360 partitions. The cluster can execute 60 tasks concurrently.

1. Estimate the minimum number of waves if tasks are equal.
2. Predict the effect of reducing to 30 partitions.
3. Predict the effect of increasing to 36,000 tiny partitions.
4. Explain why neither partition count alone nor average partition size proves
   the design is healthy.

## Scenario B — Skew

After grouping by `customer_id`, 359 tasks finish in 90 seconds. One task runs
for 28 minutes and spills heavily. Forty percent of records use the key
`UNKNOWN`.

Produce:

- a diagnosis;
- three UI/task metrics that support it;
- two possible remedies;
- a semantic or operational risk for each remedy;
- an explanation of why adding executors is unlikely to fix the long tail.

## Scenario C — Output layout

A 500 GB pipeline writes 80,000 small files. Another engineer proposes
`coalesce(1)`.

Design a better response. Discuss downstream consumers, sensible file sizing,
shuffle cost, and whether a separate delivery step should create a single
artifact.

## Quality bar

Use the terms partition, task, core, shuffle, skew, and spill accurately. Avoid
claiming a universal ideal partition size.

