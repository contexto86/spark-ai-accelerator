# Module 01 Checkpoint: Spark Architecture

Complete this checkpoint without reading notes. A mentor should ask follow-up
questions whenever an answer relies on a slogan.

## Part 1 — Core explanation

In no more than five minutes, explain:

- why Spark exists;
- the driver;
- executors;
- partitions;
- DAGs, jobs, stages, and tasks;
- lazy evaluation.

Your explanation must connect the concepts. Do not provide six isolated
definitions.

## Part 2 — Draw from memory

Draw a Spark application with one driver, a cluster manager, and at least three
executors. Add partitioned input and a pipeline containing:

```text
scan -> filter -> join -> group -> write
```

Mark likely shuffle boundaries and describe how the graph might change if one
join side can be broadcast.

## Part 3 — System judgment

For each case, state whether Spark is appropriate and defend the decision:

1. A 2 GB interactive analysis.
2. A transactional customer-balance service.
3. A 5 TB nightly transformation with a strict SLA.
4. A 150 GB weekly job that already meets its SLA on one machine.
5. A workload dominated by one REST call per row.

## Part 4 — Failure scenarios

Answer aloud:

1. Why can `collect()` fail the driver while executor memory is free?
2. Why can one skewed partition dominate stage runtime?
3. Why might a count and a write recompute the same lineage?
4. What can happen when an executor holding shuffle files disappears?
5. Why is adding more executors not a universal performance fix?

## Pass criteria

The learner passes only if they can explain Spark purpose, driver, executor,
partition, DAG, and lazy evaluation without notes, and can discuss both when
Spark should and should not be used.

Evaluate each dimension from 0–3:

| Dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Correctness | Incorrect | Major gaps | Mostly correct | Precise |
| Depth | Slogans | Definitions only | Connected concepts | Predictive reasoning |
| Trade-offs | None | One-sided | Names costs | Weighs alternatives |
| Clarity | Unclear | Fragmented | Structured | Concise and audience-ready |

**Pass threshold:** at least 9/12 overall, no zero in any dimension, and a
correct explanation of all six required concepts. If not passed, identify the
two highest-value topics to reinforce before retrying.

