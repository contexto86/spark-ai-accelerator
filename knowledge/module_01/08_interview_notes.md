# Spark Architecture Interview Notes

This chapter is a speaking guide, not a glossary. Architecture interviews test
whether you can connect concepts, predict behavior, identify bottlenecks, and
make trade-offs under incomplete information. Definitions matter, but
reasoning earns the stronger signal.

## The 90-second architecture answer

A compact explanation of Spark should cover purpose, components, and execution:

> Spark is a distributed computation engine for data workloads whose volume,
> runtime, or resilience requirements justify cluster execution. A driver
> builds and optimizes plans, divides actions into jobs and stages, and
> schedules tasks. Executors run those tasks over data partitions and produce
> shuffle or final output. Transformations are lazily recorded, so Spark can
> optimize the complete plan before an action triggers execution. Wide
> operations redistribute data and form costly shuffle boundaries.

Finish with judgment:

> I would not use Spark automatically. For transactional serving, selective
> database queries, or data that fits comfortably on one machine, a simpler
> system is often faster and cheaper.

That answer creates several follow-up paths. Be ready to go deeper rather than
adding every detail up front.

## Concept map

```text
Why Spark?
  parallel scale + recovery
          |
          v
Driver plans and schedules ---- cluster manager allocates resources
          |
          v
Jobs -> stages -> tasks
          |         |
      shuffles    one partition per task, usually
          |
          v
Executors process, cache, spill, and write
```

Lazy evaluation sits above this execution hierarchy. It allows transformations
to accumulate into a plan before actions create jobs.

## High-quality definitions

**Driver:** The application control process that creates the Spark context,
builds and optimizes plans, schedules tasks, and tracks execution. Large
result collection and enormous plans can exhaust it.

**Executor:** An application-specific worker process that runs tasks, stores
cached partitions, and handles shuffle data. Executor loss is often recoverable
through task retry and lineage.

**Partition:** A logical chunk of distributed data and normally the input to
one task in a stage. Partition count affects parallelism; size and skew affect
task memory and duration.

**DAG:** The directed acyclic dependency graph of computation. At runtime,
actions lead to jobs, shuffle boundaries divide work into stages, and stages
contain tasks.

**Lazy evaluation:** Spark records transformations and delays row processing
until an action requires a result, enabling whole-plan optimization and also
making repeated actions a potential source of recomputation.

**Shuffle:** Redistribution of records across partitions to satisfy a key or
ordering requirement. It involves network, serialization, disk, and
coordination cost.

## Predictive reasoning patterns

Interviewers often present symptoms instead of asking for definitions.

### “One task takes 40 minutes; all others take two.”

First hypothesis: skewed partition or input split. Compare task input size,
shuffle read, spill, and key distribution. More executors may not help because
the unit of straggling work is one task. Potential remedies depend on the
operator: heavy-key isolation, salting, pre-aggregation, filtering bad keys, or
changing join strategy.

### “Executors are idle while the application is slow.”

Possible causes include too few partitions, work running on the driver,
waiting for one straggler, slow source listing, or an action collecting data.
Inspect active stages and the driver rather than assuming CPU shortage.

### “The driver dies, but executor memory is mostly free.”

Look for `collect`, `toPandas`, large local objects, excessive task metadata,
or a huge plan. Aggregate cluster memory cannot protect a driver from a
control-plane or result-materialization failure.

### “A pipeline became slower after adding a count for logging.”

The count is an action. It may execute the entire upstream lineage, after which
the write executes it again. Consider removing the action, combining metrics
with the main processing, or persisting at a justified reuse boundary.

### “A group-by spills heavily despite a large cluster.”

Examine per-partition state and skew. Total memory is not fungible across one
oversized task. Increase parallelism if partitions are uniformly too large;
handle heavy keys if they are uneven; reduce data before the shuffle where
possible.

## Comparisons worth articulating

### Spark versus PostgreSQL

PostgreSQL is a transactional relational database with indexed access and
concurrent serving. Spark is a distributed computation engine for parallel
bulk transformations. A database may outperform Spark when data already lives
there and selective queries or transactions dominate.

### Spark versus pandas

pandas is local and eager in one process, with low overhead and an expressive
Python ecosystem. Spark distributes partitioned work and tolerates some worker
failures, but adds scheduling and shuffle costs. Choose from working-set size,
SLA, and operational requirements.

### Narrow versus wide

Narrow transformations can be computed from local partition dependencies and
pipelined. Wide transformations require redistribution, usually creating a
shuffle and stage boundary. The distinction predicts data movement, not
business complexity.

### Cache versus checkpoint

Caching retains materialized partitions for reuse and can fall back to lineage
for recomputation. Checkpointing writes reliable state and truncates lineage.
Use caching for repeated computation savings; use checkpointing when lineage
length or recovery semantics justify a durable boundary.

## Trade-offs to mention naturally

More partitions increase potential concurrency and reduce per-task data, but
increase scheduling and file overhead. Larger executors provide more memory
per process, but too many cores can create concurrent memory pressure and
larger failure impact. Broadcasting avoids shuffling a large side, but consumes
memory on every executor and depends on accurate size assumptions.

Caching avoids recomputation, but consumes storage memory and adds
materialization cost. Pushing data through Spark can scale a transformation,
but extracting from a database may overload the source. Every optimization
moves cost; say where the cost goes.

## Communicating to different audiences

For a data engineer, use execution terms: plans, partitions, stages, shuffles,
skew, and sinks.

For a PostgreSQL developer, bridge from familiar concepts: Spark has a
relational optimizer, but executes a query across worker processes and
partitioned files rather than serving indexed transactional tables. A shuffle
is somewhat analogous to redistributing rows for a parallel hash operation,
but across an application cluster.

For an engineering manager, focus on outcomes and costs: Spark shortens large
batch processing through parallelism and improves recovery from worker
failures, but introduces platform complexity, specialist debugging, and
potential infrastructure spend.

Different vocabulary is not dumbing down. It is selecting the model that helps
the audience make the next decision.

## Common weak answers and repairs

“Spark is faster because it uses memory.” Repair it by noting that Spark can
spill, many jobs are I/O-bound, and speed comes from parallel execution,
optimization, and reduced unnecessary I/O—not memory alone.

“An executor is a node.” Repair it: an executor is a process allocated to an
application; a host can run multiple processes depending on the environment.

“One partition equals one file.” Repair it: input sources may map files or
splits to partitions, and shuffles create new logical partitions.

“Lazy evaluation means nothing runs until collect.” Repair it: many actions,
including counts and writes, trigger execution; metadata work can happen
earlier.

“More executors make every job faster.” Repair it: parallelism is bounded by
tasks, skew, source throughput, shuffle, and serial work.

## A response structure for scenario questions

Use four moves:

1. **Clarify:** What is the data volume, SLA, key distribution, and observed
   stage behavior?
2. **Hypothesize:** Name two or three likely causes, ordered by evidence.
3. **Verify:** Identify the plan, UI metric, or experiment that separates them.
4. **Act with trade-offs:** Propose a remedy and state its cost or risk.

This structure prevents configuration guessing.

## Final readiness test

Without notes, draw driver, cluster manager, and executors. Explain how a
filter-join-group-write pipeline becomes jobs, stages, and tasks. Mark the
likely shuffles, state how partitions determine concurrency, and describe what
happens if an executor disappears. Then choose between PostgreSQL, pandas, and
Spark for three concrete workloads.

If you can do that clearly, answer challenges without slogans, and reject
Spark when its overhead is unjustified, you are ready for an architecture
screen at the practitioner level.

