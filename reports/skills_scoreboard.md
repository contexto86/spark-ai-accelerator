# Skills Scoreboard

Use a 0–10 scale. During Module 01, update only Spark Architecture, Partitions,
and Interview Readiness. Leave later-module skills at zero.

| Skill | Score |
|---|---:|
| Spark Architecture | 8/10 |
| Spark SQL | 8/10 |
| PySpark | 6/10 |
| Partitions | 8/10 |
| Performance | 5/10 |
| Delta Lake | 0/10 |
| Interview Readiness | 8/10 |

## Module 01 Evidence

- Spark Architecture: Connected explanation of purpose, driver/executors, lazy
  evaluation, jobs, stages, tasks, and shuffles. Guided checkpoint scored
  8.5/10; formal no-notes checkpoint scored 8/10. Module 01 completed.
- Partitions: Correctly reasons about task waves, skew, stragglers, salting,
  why `coalesce(1)` defeats parallelism, and why too few partitions leave
  cores idle.
- Interview Readiness: Short mock interview averaged 8/10. Strong
  system-selection, skew, repeated-action, and PostgreSQL-audience answers.
  Continue sharpening low-partition versus skew diagnosis and OLTP wording.

## Module 02 Evidence

- Spark SQL: Checkpoint-style closeout scored 7.5/10. Learner explains Spark
  SQL as SQL intent translated into distributed scans, joins, exchanges,
  aggregates, windows, sorts, and driver results. Reads physical plans with
  `BroadcastExchange`, `BroadcastHashJoin`, `HashAggregate`, `Window`,
  `WindowGroupLimit`, `Sort`, `Exchange`, and `AdaptiveSparkPlan`.
- PySpark: Learner set up a local notebook environment, loaded module CSVs,
  created temp views, ran Spark SQL, used explicit schemas, adjusted
  `spark.sql.shuffle.partitions`, and inspected plans. Continue reinforcing
  complete checkpoint SQL and window syntax.
- Performance: Learner can reason about shuffle partition counts, row width,
  projection before expensive operators, broadcast versus shuffle joins,
  global sort cost, top-N window optimization, and duplicate-key join
  diagnostics. Full tuning is reserved for a later performance module.

## Module 03 Evidence

- Spark SQL: Module 03 reinforces SQL by requiring translation between SQL and
  DataFrame solutions. Score remains unchanged until learner performance is
  assessed.
- PySpark: Module 03 materials are generated for focused PySpark DataFrame
  training. Current score remains 6/10 until DataFrame API fluency,
  translation skill, and code review quality are demonstrated.
- Performance: Module 03 includes plan-reading and anti-pattern review for
  DataFrame code, including row width, UDFs, `collect()`, joins, windows, and
  shuffles. Score remains unchanged because full performance tuning is still a
  later module.
