# PostgreSQL vs. pandas vs. Spark

Choosing among PostgreSQL, pandas, and Spark is not a contest with a universal
winner. They solve overlapping but differently shaped problems. A strong data
engineer chooses from workload properties: data size, concurrency, latency,
transaction requirements, transformation shape, operational environment, and
team capability.

## Three different centers of gravity

PostgreSQL is a durable relational database. Its center of gravity is
transactional correctness, indexed access, concurrent clients, and relational
query execution close to stored data.

pandas is an in-process analytical library. Its center of gravity is expressive
single-machine manipulation, exploration, and integration with Python’s data
science ecosystem.

Spark is a distributed computation engine. Its center of gravity is planning
and coordinating parallel transformations over partitioned data.

| Question | PostgreSQL | pandas | Spark |
|---|---|---|---|
| Primary execution | Database server | One Python process | Driver plus executors |
| Typical state | Durable tables | Process memory | Distributed files/tables and executor memory/disk |
| Transactions | Strong ACID support | Not a database concern | Depends on sink/table format |
| Scale-up/out | Primarily scale-up, replicas and extensions | Scale-up | Scale-out |
| Startup overhead | Low for an existing server | Very low | Material |
| Best latency profile | Point queries and relational workloads | Interactive local analysis | Large parallel jobs |
| Failure recovery | WAL, replication, transactions | Process-level recovery | Task retry and lineage |

The table is a map, not a benchmark. PostgreSQL can process very large tables,
pandas can work beyond RAM with careful techniques, and Spark can run locally.
The question is where each system remains operationally natural.

## Example: daily product analytics

Suppose an application produces 30 million events per day.

If analysts need indexed lookups, dashboard queries, row-level updates, and
consistent transactions over a curated subset, PostgreSQL may be the right
serving and analytical store. Proper indexing, partitioned tables, materialized
views, and query tuning can go far.

If a data scientist wants to explore a 2 GB extract, test features, and plot
distributions, pandas is likely superior. It has almost no distributed
coordination cost and gives immediate access to Python libraries.

If the pipeline must scan a year of raw events in object storage, join them
with large dimension histories, sessionize by user, and finish every morning,
Spark becomes credible. It can distribute the scan and transformations across
many executors.

The architecture may use all three:

```text
Object storage --Spark batch--> curated tables
                              |
                              +--> PostgreSQL serving subset
                              |
                              +--> pandas sample for exploration
```

Good architecture composes systems instead of forcing one system into every
role.

## Memory and execution behavior

pandas generally materializes data in the memory of one process. Vectorized
operations are efficient, but a join can require several times the input size
because both inputs, indexes, and output coexist. When the process exceeds
available memory, failure can be abrupt unless the workflow is explicitly
chunked.

PostgreSQL has a mature buffer manager and can spill sorts or hash operations
to disk. It does not require the entire table in RAM. Its optimizer can exploit
indexes and statistics, making it extremely effective when queries touch a
small fraction of data.

Spark distributes partitions across executor processes. It can spill and
recompute, but distribution does not abolish memory constraints. Each task must
fit its working state into an executor’s available memory or spill safely.
Skew can send a disproportionate group to one task, causing a job to fail even
when total cluster memory looks generous.

## Data movement is the hidden tax

PostgreSQL usually executes where the database pages live. pandas reads data
into one process. Spark may move records across the network during shuffles.
That flexibility is powerful but expensive.

Consider grouping sales by `customer_id`. If source partitions are organized
by date, records for the same customer are scattered. Spark must exchange data
so equal keys reach the same downstream partition. The cost includes
serialization, network I/O, disk spill, and scheduling. On 500 MB, this
machinery can be slower than pandas or PostgreSQL. On 5 TB, it may be the only
practical path to the SLA.

## Concurrency and operational intent

PostgreSQL is designed to serve multiple clients and protect shared mutable
state. Spark applications are usually jobs with finite plans or continuous
streaming queries. A Spark driver is not a general transactional service.

pandas is usually controlled by one analyst or application process. Its
simplicity is a strength: debugging is local, functions are ordinary Python,
and errors have a small blast radius.

Spark demands more operational machinery: cluster allocation, job monitoring,
logs from distributed processes, dependency management, data layout, and cost
controls. The relevant comparison is therefore not only runtime. Include
engineering time, on-call complexity, and infrastructure cost.

## Decision framework

Ask these questions in order:

1. Can an existing database answer the problem with a clear schema, suitable
   indexes, and acceptable load?
2. Can one adequately sized machine process the data within the SLA?
3. Is the workflow primarily interactive exploration, transactional serving,
   or repeatable bulk computation?
4. Does parallelism outweigh startup and shuffle overhead?
5. Is the team prepared to operate and debug a distributed system?

Choose PostgreSQL when durability, transactions, concurrent access, and
selective queries dominate. Choose pandas when data fits comfortably on one
machine and iteration speed matters. Choose Spark when the workload benefits
materially from parallel execution and distributed recovery.

## Anti-patterns

Using Spark to execute thousands of tiny queries against PostgreSQL can overload
the database and produce poor parallelism. Pulling a billion rows from
PostgreSQL into pandas merely transfers the capacity problem. Treating Spark as
a row-by-row API discards its set-oriented optimizer.

Another anti-pattern is choosing by raw input size alone. A 2 TB append-only
scan may be easy to parallelize, while a 200 GB skewed graph-like join may be
hard. Transformation shape and intermediate state matter as much as bytes.

## Interview framing

An interview-ready comparison should state workload boundaries, not slogans.
For example:

> PostgreSQL is my default when I need transactional persistence, indexed
> relational access, or concurrent serving. pandas is ideal for local,
> memory-bounded analysis. Spark is justified when a bulk transformation
> requires cluster parallelism or distributed fault recovery. I would validate
> the choice with data volume, intermediate size, SLA, concurrency, and
> operational cost.

Then offer an example where you would deliberately not use Spark. That shows
engineering judgment: the ability to choose the least complex system that
reliably meets the requirement.

