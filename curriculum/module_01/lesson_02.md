# Lesson 02: Driver and Executor Reasoning

## Learning objective

Separate planning and coordination from task execution, then use that boundary
to diagnose failures and unsafe patterns.

## Predict before reading

Imagine a cluster with abundant free executor memory. The application calls
`collect()` on a 40 GB result and the driver has 8 GB available. Predict:

- which process fails;
- why aggregate cluster memory does not save it;
- what architectural change is preferable to adding executors.

Then predict what differs if one executor disappears during a shuffle.

## Knowledge reference

- `knowledge/module_01/03_driver_executor_model.md`

## Practical example

A revenue pipeline is stable until an engineer converts the final distributed
DataFrame to a local pandas DataFrame for formatting. The failure is a boundary
violation: scalable work was returned to the control process. The remedy is to
format and write in distributed form, or reduce to a genuinely bounded result
before returning data.

If instead one executor repeatedly dies on a particular task, inspect task
input, spill, and skew. That is likely a per-partition execution problem rather
than driver result pressure.

## Exercise

Complete `exercises/module_01/exercise_03.md`. Draw the architecture before
writing prose, and annotate where data and control messages move.

## Reflection questions

- Which operations in your pipelines accidentally move data to a coordinator?
- Why can increasing cores per executor increase memory pressure?
- What side effects become unsafe when Spark retries a task?
- What information is lost when someone describes an executor simply as “a
  node”?

