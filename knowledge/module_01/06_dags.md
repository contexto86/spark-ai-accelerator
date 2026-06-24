# DAGs, Jobs, Stages, and Tasks

Spark represents computation as a directed acyclic graph, or DAG. “Directed”
means dependencies have an order: an output depends on earlier inputs.
“Acyclic” means the dependency graph does not loop back into itself. Iterative
algorithms can repeat actions at the application level, but each submitted
execution graph has a finite dependency structure.

The DAG is useful because a real pipeline rarely fits a single map and reduce.
It may scan, filter, join, aggregate, rank, and write. Spark can reason about
that chain, pipeline compatible operators, and place stage boundaries where
data must be exchanged.

## Several related plans

“The DAG” is often used loosely. It helps to distinguish layers:

- The logical plan describes relational operations and expressions.
- The optimized logical plan reflects semantic rewrite rules.
- The physical plan chooses execution operators and distribution strategies.
- The scheduler creates jobs, stages, and tasks when actions run.

These views are related but not identical. A UI stage graph is not simply the
same object as the SQL logical plan.

```text
DataFrame/API expressions
          |
          v
 logical and physical planning
          |
          v
 Action -> Job
           |
           +--> Stage 0: scan/filter/map tasks
           |       |
           |       +-- shuffle files
           |
           +--> Stage 1: join/aggregate tasks
                   |
                   +--> final write
```

## Jobs

An action usually creates one or more jobs. Calling a count triggers work to
produce a scalar. Writing a DataFrame triggers work to produce files or table
changes. A single application may execute many jobs because it contains
multiple actions.

This explains why source code line count and runtime work are weakly related.
Ten transformations followed by one write may form one optimized execution,
while one transformed DataFrame followed by five actions can launch repeated
jobs.

## Stages and shuffle boundaries

A stage contains tasks that can be executed without requiring a full
redistribution from the current stage’s output. Narrow dependencies can be
pipelined. A sequence such as scan, project, filter, and compute an expression
may run within the same task over each input partition.

A wide dependency generally creates a stage boundary. Before a downstream
group-by can aggregate all rows for a key, upstream tasks write shuffle
partitions. Downstream tasks fetch the relevant blocks from many upstream
tasks.

```text
Narrow pipeline:
scan P0 -> filter -> project -> partial result
scan P1 -> filter -> project -> partial result

Wide exchange:
all partial results --shuffle by customer_id--> grouped partitions
```

The next stage cannot fully proceed until required upstream shuffle outputs are
available. This coordination contributes to long-tail sensitivity: one slow
upstream task can delay many downstream consumers.

## Tasks

A task is the smallest unit the Spark scheduler sends to an executor. Within a
stage, tasks usually correspond one-to-one with partitions. Tasks run the same
operator logic on different data.

If a task fails, Spark can retry it. If an executor containing shuffle outputs
is lost, upstream tasks may need to rerun before downstream stages can
continue. The DAG and lineage provide the information necessary for that
recovery.

Task metrics reveal the physical reality hidden by high-level code:

- input records and bytes;
- executor CPU and wall time;
- shuffle read and write;
- memory and disk spill;
- serialization time;
- skew across task durations.

Reading these distributions is often more useful than looking only at total
job duration.

## A join example

Assume trips are partitioned by day and customers are partitioned by ingestion
batch. The query joins on `customer_id` and groups revenue by region.

If neither side satisfies the join’s distribution requirement and both are
large, Spark may shuffle both by customer ID. After the join, grouping by
region may require another exchange because the data is distributed by a
different key. The physical plan can therefore contain two expensive
boundaries.

If the customer table is small enough to broadcast, Spark can send it to each
executor and avoid shuffling the large trips side for the join. The later
region aggregation may still shuffle. “The query has a join” is insufficient
for predicting stages; join strategy matters.

## DAG reasoning for performance

When a job is slow, identify:

1. Where are the exchanges?
2. How many bytes cross each exchange?
3. Can filters or projections reduce data before the exchange?
4. Is a join strategy causing unnecessary movement?
5. Are downstream partitions balanced?
6. Are multiple actions rebuilding the same graph?

This turns tuning from configuration folklore into plan-level reasoning.
Increasing executor memory without understanding the DAG may simply make an
unnecessary shuffle more expensive at a larger scale.

## DAG complexity and lineage

Programmatically generated pipelines can create enormous plans: thousands of
unions, repeated column additions, or deeply nested expressions. Even before
executors process data, the driver may spend significant time analyzing and
optimizing the plan. This is a reminder that distributed execution has a
control-plane cost.

Long lineage also affects recovery. If a late partition is lost, recomputation
may traverse many ancestors. Caching a reused branch or materializing a durable
intermediate can shorten practical recovery, at the cost of storage and I/O.

## DAG versus business workflow

An orchestration DAG and a Spark execution DAG operate at different levels. An
orchestrator may represent:

```text
ingest -> validate -> Spark transform -> publish -> quality report
```

Inside the Spark transform task, Spark builds its own jobs, stages, and tasks.
Confusing the two can lead to vague failure analysis. “The DAG failed” should
prompt: which DAG, at what layer, and which dependency?

## Interview framing

An interview-ready explanation is:

> Spark models dependencies as a DAG. When an action executes, the scheduler
> organizes work into jobs. Shuffle dependencies usually divide a job into
> stages, and each stage runs tasks over partitions. Narrow operations can be
> pipelined; wide operations require data exchange and create coordination,
> network, and spill costs.

A deeper follow-up is to draw a scan-filter-join-group-write pipeline and mark
possible shuffle boundaries. State that the exact graph depends on the
physical plan—for example, a broadcast join changes the boundary. This shows
you understand a DAG not as a vocabulary item, but as a tool for predicting
runtime behavior.

