# Exercise 05: Lazy Evaluation

**Purpose:** Predict execution and choose materialization boundaries.

## Conceptual pipeline

```text
raw = read events
clean = filter invalid rows from raw
enriched = join clean with customers
by_region = aggregate enriched by region

print(clean.count())
write(by_region)
```

## Tasks

1. Mark each transformation and action.
2. Describe what plans exist before the count.
3. Identify which work may execute more than once.
4. Explain why assigning `clean` or `enriched` to a variable does not store
   rows.
5. Propose one persistence strategy and one durable materialization strategy.
6. For each strategy, state when its cost exceeds its benefit.

## Optimizer reasoning

Assume the final output needs only `status`, `customer_id`, `region`, and
`amount`. Explain how lazy planning could enable column pruning and predicate
pushdown. Then describe how an opaque user-defined function could reduce the
optimizer’s visibility.

## Debugging scenario

A cast transformation is defined near the start of the file, but the error
appears only at the final write. Explain why this timing is consistent with
lazy evaluation and how you would isolate the bad data without adding many
full-data actions.

## Quality bar

Distinguish caching from checkpointing and durable table writes. Do not say
“nothing happens until collect”; name multiple actions and acknowledge metadata
or schema work that may occur during planning.

