# Module 01 Learning Path: Spark Architecture

**Module:** 01  
**Name:** Spark Architecture  
**Estimated duration:** 2–4 hours  
**Difficulty:** Beginner to Practitioner

Complete sections in order. Do not read reference material while attempting a
checkpoint or interview response.

## Section 1 — Why Spark and System Choice

**Estimated Duration:** 25–40 minutes

**Objectives:**

- Explain the coordination problem Spark solves.
- Compare Spark with PostgreSQL and pandas using workload evidence.
- Reject Spark when distributed overhead is not justified.

**Materials:** `lesson_01.md`; knowledge chapters 01, 02, and 07.

**Completion Criteria:**

- Give a two-minute explanation of why Spark exists without saying only “big
  data” or “in memory.”
- Choose a system for three contrasting workloads and state the deciding
  constraints.
- Complete Exercise 01.

## Section 2 — Driver and Executors

**Estimated Duration:** 25–35 minutes

**Objectives:**

- Separate control-plane, resource-allocation, and task-execution roles.
- Diagnose driver-side versus executor-side failures.
- Explain why total cluster memory does not solve every memory failure.

**Materials:** `lesson_02.md`; knowledge chapter 03.

**Completion Criteria:**

- Draw and narrate the driver/executor model from memory.
- Predict the failure effect of losing an executor and losing the driver.
- Complete Exercise 03.

## Section 3 — Partitions and Parallelism

**Estimated Duration:** 30–45 minutes

**Objectives:**

- Connect partitions, tasks, cores, and waves of execution.
- Explain the costs of too few, too many, and skewed partitions.
- Distinguish input layout from shuffled partitioning.

**Materials:** `lesson_03.md`; knowledge chapter 04.

**Completion Criteria:**

- Estimate task concurrency for a supplied partition/resource scenario.
- Diagnose a straggler using partition-level evidence.
- Complete Exercise 04.

## Section 4 — Lazy Evaluation

**Estimated Duration:** 20–35 minutes

**Objectives:**

- Distinguish transformation planning from action-triggered execution.
- Predict repeated work caused by multiple actions.
- Choose sensible cache or materialization boundaries.

**Materials:** `lesson_04.md`; knowledge chapter 05.

**Completion Criteria:**

- Mark transformations and actions in a conceptual pipeline.
- Explain why assigning a DataFrame does not materialize it.
- Complete Exercise 05.

## Section 5 — DAGs, Stages, and Shuffles

**Estimated Duration:** 30–45 minutes

**Objectives:**

- Relate logical plans to jobs, stages, and tasks.
- Identify narrow and wide dependencies.
- Predict shuffle boundaries and their operational costs.

**Materials:** `lesson_05.md`; knowledge chapter 06.

**Completion Criteria:**

- Draw a likely stage graph for scan-filter-join-group-write.
- Explain how join strategy can alter the graph.
- Complete Exercise 02.

## Section 6 — Synthesis and Interview Readiness

**Estimated Duration:** 30–40 minutes

**Objectives:**

- Communicate Spark architecture to technical and non-technical audiences.
- Diagnose architecture scenarios with evidence rather than folklore.
- Demonstrate recall without notes.

**Materials:** `lesson_06.md`; knowledge chapter 08; checkpoint and interviewer
prompt. After completion, use knowledge chapter 09 as the review pack.

**Completion Criteria:**

- Complete Exercise 06 for all three audiences.
- Pass the Module 01 checkpoint.
- Answer at least five interviewer questions, including one scenario question,
  at practitioner quality.

## Module completion

The module is complete only when the learner can explain Spark purpose, driver,
executor, partition, DAG, and lazy evaluation without notes, and can defend
when Spark should and should not be used.
