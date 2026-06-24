# Exercise 01: Why Spark Exists

**Purpose:** Justify distributed processing from constraints rather than
fashion.

## Scenario

A retailer receives 2.5 TB of compressed clickstream data per day. The daily
pipeline removes bots, joins product and campaign history, sessionizes events,
and produces 15 GB of aggregates. It currently takes nine hours on one machine;
the business requires completion in two hours. The source data is immutable,
and occasional worker failure must not restart the entire run.

## Tasks

1. Identify at least four constraints that are relevant to the technology
   choice. Separate raw-data size from intermediate-state risk.
2. Explain which coordination responsibilities Spark can assume.
3. State what Spark does **not** solve automatically.
4. Propose the strongest non-Spark alternative and explain what evidence would
   make it preferable.
5. Write a 150-word architecture decision: recommendation, rationale, risks,
   and one benchmark required before adoption.

## Counterfactual

Now change the input to 8 GB, the SLA to four hours, and the result to 300 MB.
Revise the decision. Do not merely replace “Spark” with “pandas”; explain which
cost-benefit relationship changed.

## Quality bar

A strong response discusses parallelism, data movement, fault recovery,
intermediate size, operational cost, and the simplest viable alternative. “The
data is big” is not sufficient.

