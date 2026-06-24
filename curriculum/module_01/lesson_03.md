# Lesson 03: Partitions and Parallelism

## Learning objective

Use partitions as the bridge between data distribution, task concurrency,
memory pressure, skew, and output layout.

## Predict before reading

A stage has 240 partitions. The cluster can run 48 tasks at once.

- How many idealized waves are required?
- What happens if one partition contains 35% of all records?
- Would doubling executors necessarily halve runtime?
- What costs appear if the stage is changed to 24,000 tiny partitions?

State your predictions before consulting the chapter.

## Knowledge reference

- `knowledge/module_01/04_partitions.md`

## Practical example

A pipeline groups events by `account_id`. Most accounts have hundreds of
events, but a shared system account has 900 million. Hash partitioning sends
that key to one reducer task. Average partition size looks healthy while one
task spills heavily. The response should target the heavy key—perhaps isolate,
salt, or pre-aggregate it—not merely add workers.

The same pipeline writes 30,000 tiny files. Reducing output partitions may
improve downstream reads, but forcing one partition exchanges a metadata
problem for a serial bottleneck. File layout is part of partition design.

## Exercise

Complete `exercises/module_01/exercise_04.md`. Include both a diagnosis and the
measurement that would validate it.

## Reflection questions

- When does adding partitions improve resilience as well as speed?
- Why is average partition size an incomplete metric?
- Which transformations in a typical pipeline preserve partition locality?
- Who consumes the output files, and how should that influence partition
  count?

