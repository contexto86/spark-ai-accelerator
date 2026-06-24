# Progress Report

Module: 01 — Spark Architecture

Completion Date: June 24, 2026

Time Invested: Not recorded

## Topics Covered

- Why Spark exists and when distributed computation is justified.
- Spark versus PostgreSQL and pandas.
- Driver and executor responsibilities.
- Partitions, tasks, parallelism, waves, skew, hot keys, and salting.
- Lazy evaluation, transformations, actions, repeated lineage, and caching.
- Jobs, stages, narrow dependencies, wide dependencies, and shuffles.
- Executor failure, lost shuffle blocks, recomputation, and driver failure.
- Small-file overhead and the serial bottleneck caused by `coalesce(1)`.
- Audience-specific explanations for a PostgreSQL developer and an engineering
  manager.
- Exercise 01 completed.
- Exercise 02 completed.
- Exercise 03 completed.
- Exercise 04 completed.
- Exercise 05 completed.
- Exercise 06 completed.
- Formal no-notes checkpoint completed.
- Short mock interview completed.
- Driver OOM from `collect()`, executor skew failures, low partition
  parallelism, and idempotent external side effects were practiced.

## Strengths

- Selects Spark from workload constraints rather than data volume alone.
- Clearly explains driver, executor, partition, task, stage, and shuffle.
- Understands that skew creates a straggler that more executors cannot
  automatically solve.
- Understands action-triggered execution and when caching avoids expensive
  recomputation.
- Correctly rejects Spark for transactional APIs and workloads already meeting
  their SLA on simpler infrastructure.
- Communicates trade-offs clearly and improves answers after targeted
  correction.
- Gave an interview-ready PostgreSQL-developer explanation of Spark that
  accurately covered planning, parallel tasks, partitions, shuffles, and OLTP
  boundaries.

## Weaknesses

- Initially uncertain about stages, shuffles, and executor-loss recovery; these
  improved through guided scenarios.
- Continue refining PostgreSQL comparisons: data residing there does not prove
  it fits on one server, and PostgreSQL also performs query planning.
- Initially underestimated pandas for a 3 GB exploratory workload.
- Driver-side versus executor-side diagnosis improved during Exercise 03;
  continue occasional no-notes recall.
- Small-file overhead, cache placement, and idempotent task side effects should
  be revisited in later performance modules.

## Recommended Reinforcement

- Reinforce why keeping large results distributed is better than simply
  increasing driver memory for `collect()`.
- Review why task retries require idempotent external operations.
- Practice identifying which lineage is repeated by multiple actions.
- Revisit input-file layout versus logical Spark partitioning.
- Practice diagnosing low task counts versus skew: too few partitions is not
  the same as hot-key skew.

## Readiness Score

Formal checkpoint: 8/10.

Short mock interview: average 8/10 — Practitioner.

Module status: complete. Recommended next module: Spark SQL / DataFrame
execution basics, while carrying forward architecture diagnostics.
