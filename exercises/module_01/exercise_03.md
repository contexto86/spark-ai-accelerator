# Exercise 03: Driver and Executor Reasoning

**Purpose:** Diagnose problems by locating responsibility in the architecture.

## Part A — Draw the system

Draw a driver, cluster manager, and three executors. Annotate:

- plan construction;
- resource allocation;
- task scheduling;
- partition processing;
- cached data;
- shuffle output;
- small results returned to the application.

Explain why an executor is not necessarily the same thing as a physical node.

## Part B — Diagnose four incidents

For each incident, state the likely constrained component, two hypotheses, the
first evidence you would inspect, and a safe response.

1. The driver exits while executors have free memory after `collect()`.
2. One executor repeatedly disappears on the same aggregation task.
3. Half the executor cores remain idle during a stage with ten partitions.
4. An external service receives duplicate requests after a task failure.

## Part C — Failure reasoning

Compare these failures:

- one task fails;
- one executor disappears after writing shuffle blocks;
- the driver process disappears.

For each, explain what Spark can retry or recompute and what application state
is at risk.

## Quality bar

A strong answer keeps control-plane and data-plane concerns separate, connects
tasks to partitions, and recognizes that retry makes non-idempotent side
effects unsafe.

