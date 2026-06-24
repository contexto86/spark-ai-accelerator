# Exercise 06: Explain Spark to Three Audiences

**Purpose:** Demonstrate audience-aware architecture communication without
changing the underlying facts.

## Critical exercise

Explain Spark separately to each audience below. The three explanations must
be materially different, not the same paragraph with substituted nouns.

### 1. Data Engineer

Deliver a 250–350 word explanation using driver, executor, partition, task,
stage, DAG, lazy evaluation, and shuffle. Include one performance failure and
how you would investigate it.

### 2. PostgreSQL Developer

Deliver a 200–300 word explanation grounded in familiar database concepts.
Compare Spark planning with a relational optimizer, distributed partitions with
table/page locality, and shuffles with data redistribution for parallel
operations. Explain why Spark does not replace PostgreSQL for transactions and
indexed serving.

### 3. Engineering Manager

Deliver a 150–220 word explanation focused on business capability, operating
cost, risk, team skills, and decision thresholds. Use no more than three Spark
terms, each explained in plain language.

## Consistency check

After writing all three, produce a table:

| Claim | Data Engineer | PostgreSQL Developer | Engineering Manager |
|---|---|---|---|
| Why Spark | | | |
| How work is distributed | | | |
| Main cost/risk | | | |
| When not to use it | | | |

Verify that the facts remain consistent even though detail and vocabulary
change.

## Self-review

Score each explanation from 0–10 for correctness, depth, trade-off reasoning,
and clarity. Identify one sentence to remove because it adds jargon without
helping that audience.

