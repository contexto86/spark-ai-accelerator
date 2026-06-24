# Lazy Evaluation

Spark transformations are usually lazy: calling operations such as `select`,
`filter`, or `join` describes a result but does not immediately process all
rows. Execution begins when an action requires a materialized result, such as a
write, count, collection, or display.

Lazy evaluation is not procrastination for its own sake. It gives Spark a view
of the whole computation before committing resources. With that view, the
optimizer can remove unnecessary work, combine operators, push filters toward
data sources, prune columns, and choose physical strategies.

## Transformations build a plan

Consider this conceptual workflow:

```python
events = read_events()
paid = events.filter("status = 'paid'")
summary = paid.groupBy("country").sum("amount")
summary.write(...)
```

The first three statements primarily construct a logical plan. The write is an
action and triggers execution. Spark may determine that only `status`,
`country`, and `amount` are needed, push the status predicate into a columnar
reader, and pipeline projection and filtering in the scan stage.

The programmer described *what* should be produced. Spark retains freedom over
*how* to produce it:

```text
Unresolved logical plan
        |
        v  resolve tables, columns, types
Analyzed logical plan
        |
        v  rule-based optimization
Optimized logical plan
        |
        v  select algorithms and exchanges
Physical plan
        |
        v  action triggers jobs/stages/tasks
Execution
```

This separation resembles a relational database optimizer more than an
ordinary eager Python collection pipeline.

## Optimization opportunities

**Predicate pushdown** asks a source to avoid reading irrelevant rows or row
groups when its capabilities and statistics permit. **Column pruning** avoids
decoding columns not needed downstream. **Constant folding** simplifies fixed
expressions. **Operator reordering or simplification** can reduce work while
preserving semantics. Join planning may use size estimates and configuration
to choose broadcast or shuffle-based strategies.

These optimizations are possible because the expression tree remains visible
to Spark. Opaque user-defined functions can limit that visibility. A Python UDF
may hide semantics that built-in expressions expose to the optimizer and may
introduce serialization boundaries. This does not mean UDFs are forbidden; it
means they spend optimization freedom and should be justified.

## Actions and repeated computation

Laziness creates a common surprise:

```python
clean = expensive_transform(raw)
clean.count()
clean.write(...)
```

The count and write are separate actions. Unless Spark can reuse an exchange
or the dataset is persisted appropriately, the expensive lineage may execute
twice. Assigning a DataFrame to a variable does not store its rows; the
variable represents a plan.

Caching or persistence can intentionally retain computed partitions for reuse,
but it is not free. Cached data consumes executor memory or disk, may be
evicted, and adds materialization cost. Cache when repeated downstream actions
save more than storage and lifecycle management cost. Unpersist when the reuse
window ends.

A good test is to ask: How many times will this result be reused, how expensive
is recomputation, how large is the materialized representation, and what other
executor state will it displace?

## Laziness and debugging

An invalid data conversion may not fail at the line where the transformation
is written. The error may surface later at an action because that is when rows
are processed. Similarly, a job can appear to “hang on count,” even though the
count merely triggered a long upstream chain.

Debugging requires tracing the lineage behind the action. Inspect the plan,
identify stage boundaries, and use targeted actions only when needed.
Peppering a pipeline with counts for logging can multiply runtime by executing
large lineages repeatedly.

For validation, it can be better to compute metrics within the same planned
workflow, persist at deliberate boundaries, or sample small subsets. The
principle is to make materialization explicit in your mental model even though
the API looks sequential.

## Lazy does not mean nothing happens

Some API calls must perform limited work before the final action. Schema
inference may inspect data. File listing and metadata retrieval can happen
during planning. Creating a session or requesting resources has operational
effects. The useful statement is not “Spark does absolutely nothing until an
action,” but “distributed transformation of dataset rows is generally deferred
until a result is required.”

This nuance matters in interviews because categorical slogans are easy to
challenge.

## Eager checkpoints and materialization boundaries

Long or complex lineages can become costly to replan or recompute. Persistence
retains data while preserving lineage as a recovery path. Checkpointing writes
data to reliable storage and truncates lineage. They address related but
different concerns.

For iterative algorithms or streaming state, a checkpoint may be important for
recovery. In ordinary batch pipelines, writing an intermediate table can also
serve as an operational boundary: it enables restart, data quality inspection,
and decoupled scheduling. The trade-off is additional I/O and storage.

An experienced engineer does not maximize laziness. They choose where deferred
optimization is beneficial and where a durable boundary improves operability.

## Practical example: customer features

Suppose a feature job reads two years of transactions, filters to active
accounts, joins customer attributes, and computes ten aggregates. Three models
consume the same features.

If each model triggers its own action from the full lineage, the shared work
may repeat. Options include persisting the feature DataFrame during one
application or writing a curated feature table used by separate jobs. The
choice depends on reuse duration, failure isolation, reproducibility, and cost.

If all consumers execute immediately in one reliable application, persistence
may be enough. If models run independently or need auditability, a durable
table is likely better. Lazy evaluation explains the repeated work, but system
boundaries determine the solution.

## Interview framing

A strong answer is:

> Lazy evaluation means Spark records transformations as a logical plan and
> delays distributed execution until an action requires a result. This enables
> whole-plan optimization such as predicate pushdown, column pruning, and
> physical strategy selection. It also means separate actions may recompute the
> same lineage unless data is persisted or materialized deliberately.

Be ready to distinguish transformations from actions, explain why a variable
does not imply materialization, and discuss when caching harms rather than
helps. The important insight is that laziness changes engineering behavior:
read code as a plan, count actions, and choose materialization boundaries based
on reuse and recovery requirements.

