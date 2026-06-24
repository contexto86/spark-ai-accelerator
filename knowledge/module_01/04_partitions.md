# Partitions: Spark's Unit of Parallel Work

A partition is a logical chunk of a distributed dataset. For a given stage,
Spark generally schedules one task per partition. Partitions therefore connect
data layout to parallelism, memory pressure, shuffle behavior, and output-file
shape.

This is more precise than saying a partition is “a piece of a file.” An input
partition may correspond to a file split, an entire small file, a range from a
database read, or a partition supplied by a data source. After transformations,
partitions may be reorganized independently of the original files.

## The partition-to-task relationship

For a stage with 400 partitions, Spark can create roughly 400 tasks:

```text
Stage
  partition 0  -> task 0  -> executor/core
  partition 1  -> task 1  -> executor/core
  ...
  partition 399 -> task 399 -> executor/core
```

If the cluster can run 40 tasks concurrently, the stage proceeds in about ten
waves, assuming tasks take similar time. If one partition is much larger than
the others, one task may continue after the rest finish. This “long tail” is a
classic symptom of skew.

Partitions create independent scheduling units, but not all operators preserve
them. A filter normally processes each input partition locally and emits a
corresponding output partition. Grouping by a key typically requires all
records with that key to meet, creating a shuffle and new downstream
partitions.

## Too large, too small, or uneven

A partition that is too large can make one task exceed memory, spill heavily,
or take so long that retries are expensive. A partition that is too small
causes task scheduling, file opening, serialization, and output metadata to
consume a disproportionate share of runtime.

There is no universal ideal size. File format, compression, operator type,
available executor memory, CPU cost per record, and downstream writes all
matter. A compressed 200 MB input split may expand into much more in memory.
A partition used for a wide aggregation needs more working memory than one
used for a simple projection.

The engineering objective is not a magic number. It is:

- enough partitions to keep available cores busy;
- partitions small enough to fit task working state safely;
- partitions large enough to amortize scheduling and I/O overhead;
- a reasonably even distribution of work;
- an output-file count appropriate for consumers.

## Input partitions and the small-files problem

Object storage often accumulates thousands or millions of small files. Each
file may require listing, metadata, authentication, and open operations. Even
when Spark combines some small files into input partitions, planning and
metadata overhead can dominate.

For example, reading 500 GB as 2,000 well-sized columnar files is different
from reading the same bytes as five million JSON files. Total volume is equal,
but the second workload stresses file listing, driver planning, task setup, and
parsing. Compaction and sensible table layout are architectural performance
features, not housekeeping.

## Narrow and wide transformations

A **narrow transformation** allows each output partition to depend on a small
number of input partitions, usually one. Examples include many filters,
projections, and element-wise calculations. Spark can pipeline these
operations in one stage.

A **wide transformation** requires data from many input partitions to produce a
downstream partition. Grouping, distinct operations, many joins, and global
sorts often create this pattern. Spark performs a shuffle:

```text
Before: partitioned by input layout
P0: A, C, A       P1: B, A       P2: C, B

Shuffle by key

After: partitioned by key hash/range
Q0: all A         Q1: all B      Q2: all C
```

The shuffle is expensive because records are serialized, written, transferred,
fetched, and possibly spilled. Partition count after the shuffle controls both
parallelism and per-task load.

## `repartition` versus `coalesce`

Conceptually, repartitioning creates a new distribution and usually involves a
shuffle. It is appropriate when increasing parallelism, balancing partitions,
or arranging data by keys for downstream work.

Coalescing is commonly used to reduce partition count while avoiding a full
shuffle. Because it merges existing partitions, it can preserve imbalance. It
is useful for modest reductions after filtering, but collapsing a large
dataset to one partition creates a serial bottleneck.

The habitual `coalesce(1)` before writing is a production smell. It may create
one convenient file, but it routes all output through one task, sacrifices
parallelism, and may cause failure. If a downstream interface requires one
file, consider whether that requirement belongs in a separate small-data
delivery step.

## Key partitioning does not remove all shuffles

Engineers sometimes call `repartition("customer_id")` and assume all later
operations avoid exchange. Spark’s optimizer reasons about distribution
requirements, but file writes, transformations, adaptive execution, and loss
of partitioning metadata can change the plan. The physical plan is the source
of truth.

Partitioning by a low-cardinality key is also dangerous. Repartitioning global
data by a `country` column with five dominant values can produce a few huge
partitions, not healthy parallelism. High cardinality alone is not enough
either; frequency distribution matters.

## Skew as a partition problem

Suppose 45% of events have `customer_id = "unknown"`. A hash-based aggregation
or join sends those rows to one downstream partition. Most tasks finish
quickly; the “unknown” task spills or fails. Adding executors does little
because one partition cannot be split automatically in every plan.

Potential responses include filtering invalid keys, processing heavy keys
separately, salting keys, pre-aggregating, broadcasting a small join side, or
using adaptive skew handling. Each changes semantics or cost, so the remedy
must follow diagnosis.

## Practical inspection

Useful questions include:

- How many input files and input partitions exist?
- How many tasks does each stage create?
- Are task durations and shuffle sizes evenly distributed?
- What is the largest partition, not just the average?
- Does the write produce many tiny files?
- Which operation changes the partitioning?

Spark’s UI and physical plan can answer much of this. Aggregate cluster metrics
often hide the one pathological partition that controls completion time.

## Interview framing

A strong definition is:

> A partition is Spark’s logical unit of distributed data and, within a stage,
> usually maps to one task. Partition count controls available parallelism;
> partition size and skew control per-task memory and duration. Wide
> transformations redistribute records into new partitions through a shuffle.

Then explain a trade-off. More partitions can improve concurrency and reduce
per-task memory, but excessive partitions increase scheduling and file
overhead. Fewer partitions reduce overhead, but may underuse the cluster and
create oversized tasks. The mature answer is not “more partitions are better.”
It is “partition design should fit data distribution, operator behavior,
resources, and downstream file requirements.”

