# When Not to Use Spark

Knowing when to reject Spark is part of Spark expertise. Distributed execution
adds startup, scheduling, serialization, network, storage, observability, and
operational costs. If a workload does not need the benefits those costs buy,
Spark is unnecessary architecture.

The governing principle is simple:

> Use the least complex system that meets correctness, scale, latency,
> reliability, and cost requirements with reasonable headroom.

## Small and medium data that fits comfortably on one machine

If a dataset and its largest intermediate state fit on a well-sized machine,
single-node tools often win. pandas offers a rich Python workflow. Columnar
engines and embedded analytical databases can scan and aggregate substantial
data efficiently. PostgreSQL can execute relational transformations with
mature spill behavior.

Spark may spend more time starting executors, listing files, scheduling tasks,
and exchanging metadata than doing useful work. “The company has a Spark
cluster” is not a workload requirement.

Be careful with the phrase “fits in memory.” A 20 GB input can create a 100 GB
join or sort intermediate. Conversely, a 200 GB columnar dataset may be easy
for a single node if predicate and column pruning reduce the actual scan. Use
measured working state and SLA, not raw file size alone.

## Low-latency transactional serving

Spark is not an online transaction processing database. It does not provide
the natural indexed point updates, multi-user concurrency control, constraints,
and millisecond request behavior expected from PostgreSQL or similar systems.

A web request that asks for one customer’s current balance should query a
serving store, not start a Spark job. Spark may prepare or refresh the serving
table, but it should not sit in the synchronous request path.

Similarly, a business process requiring atomic updates across related records
belongs in a transactional system. Table formats can add transactional
semantics to analytical storage, but that does not make Spark an OLTP engine.

## Tiny, frequent tasks

Suppose 50 KB files arrive every second and each requires a trivial mapping.
Launching independent Spark jobs for each file creates extreme overhead.
Options include buffering events into useful batches, using a lightweight
consumer, or using a stream-processing design sized for continuous work.

Spark Structured Streaming may be appropriate when the continuous workload
has meaningful volume and stateful analytical transformations. The warning is
against using cluster-scale machinery for tiny isolated units, not against all
streaming use.

## Workloads dominated by external side effects

Spark excels when tasks transform partitioned data. It is often a poor fit for
calling a rate-limited REST API once per row, sending emails, or performing
small transactional writes. Massive task concurrency can overwhelm the
external service, retries can duplicate side effects, and network latency
leaves executor cores idle.

If an external interaction is required, batch requests, control concurrency,
make operations idempotent, and question whether a distributed data engine is
the correct coordinator.

## Highly iterative, fine-grained mutable algorithms

Spark’s model favors coarse-grained transformations over immutable,
partitioned data. Algorithms requiring frequent low-latency mutation of shared
state or dense communication between workers may fit specialized graph,
numerical, or distributed training systems better.

Spark can run iterative algorithms and cache data, but capability is not the
same as optimal fit. Each iteration may trigger stages, synchronization, and
shuffle. Compare the communication model with the workload’s natural shape.

## When a database already owns the data and query

Extracting a large table from PostgreSQL into Spark just to perform an
aggregation the database could execute is often wasteful. It consumes database
connections and network bandwidth, loses index and optimizer advantages, and
creates another operational system.

Push appropriate work to the database and extract reduced results. Spark makes
sense when combining multiple large sources, applying transformations the
database cannot support economically, or offloading work for a justified
reason. Data gravity matters: moving computation to data is often cheaper than
moving data to computation.

## Organizational readiness

A technically feasible Spark solution may still be wrong if the team cannot
operate it. Distributed failures require access to driver and executor logs,
stage metrics, data lineage, and resource controls. Poorly governed Spark can
produce runaway cost, small-file proliferation, and brittle jobs understood by
one person.

This is not an argument to avoid learning. It is an architectural cost to
include. A simpler system that the team can test, observe, and repair may offer
better real reliability than a theoretically scalable design.

## Warning signs of unjustified Spark

- The result and all intermediates are a few gigabytes.
- The job runs once per day but cluster startup dominates runtime.
- The main operation is a selective indexed lookup.
- The requirement is millisecond response time.
- Engineers call `collect()` immediately and do the real work locally.
- A single output file is mandatory and the pipeline ends with a huge
  `coalesce(1)`.
- Most task time is waiting on a third-party API.
- The workload has no measured scale or SLA evidence.

None is an automatic verdict, but each shifts the burden of proof toward a
simpler alternative.

## A practical decision record

Before adopting Spark, document:

1. Current and projected data volume.
2. Largest expected intermediate state.
3. Required completion time and concurrency.
4. Failure and restart requirements.
5. Candidate alternatives and why they miss requirements.
6. Estimated infrastructure and operational cost.
7. A benchmark representative of the difficult part.

For example, if a 300 GB transformation completes in 18 minutes on one
reasonably priced machine against a 60-minute SLA, a cluster may offer little
business value. If the workload is projected to reach 5 TB and must complete
in 30 minutes with retryable partitioned processing, Spark has a clearer case.

## Hybrid architectures

Rejecting Spark for one layer does not reject it everywhere. A common design
uses Spark for periodic bulk transformations, an analytical warehouse for
interactive BI, PostgreSQL for serving, and pandas for local analysis.

```text
raw data -> Spark bulk curation -> analytical tables
                                      |
                                      +-> BI engine
                                      +-> serving database
                                      +-> pandas extracts
```

The architectural skill is assigning each responsibility to a system aligned
with its access pattern.

## Interview framing

When asked when not to use Spark, avoid only saying “small data.” Give several
dimensions:

> I would avoid Spark for low-latency transactional serving, small workloads
> that fit comfortably on one machine, tiny per-event jobs, or workflows
> dominated by external side effects. I would first test whether the existing
> database or a single-node analytical engine meets the SLA. Spark is
> justified when parallelism and distributed recovery outweigh its
> coordination and operating costs.

Then describe evidence that would change your decision. Strong engineers can
say both “not yet” and “now the threshold has been crossed.”

