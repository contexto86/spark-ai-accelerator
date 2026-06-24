# Lesson 04: Lazy Evaluation

## Learning objective

Read Spark code as a deferred plan, predict when execution happens, and make
materialization decisions deliberately.

## Predict before reading

An expensive transformed DataFrame is assigned to `clean`. The application
runs `clean.count()` and then writes `clean`.

- How many actions exist?
- Which upstream work may repeat?
- Does the variable assignment store rows?
- When would caching help, and when would it make the job worse?

## Knowledge reference

- `knowledge/module_01/05_lazy_evaluation.md`

## Practical example

A team adds five counts between pipeline steps for observability. Runtime grows
from 30 minutes to two hours. Each count can trigger the lineage available at
that point. Better designs might compute quality metrics in the main flow,
persist once at a high-reuse boundary, or materialize a durable intermediate
that also improves restartability.

Lazy evaluation also enables optimization. If only three columns survive and a
filter can be pushed into a columnar source, Spark may avoid decoding much of
the input. Opaque logic can reduce this freedom.

## Exercise

Complete `exercises/module_01/exercise_05.md`. Your answer must distinguish
logical optimization, physical execution, persistence, and checkpointing.

## Reflection questions

- Which actions in your current jobs are used only for logging?
- What evidence would justify caching a DataFrame?
- When is a durable table better than an in-memory cache?
- Why can an error appear on a write rather than at the transformation that
  introduced it?

