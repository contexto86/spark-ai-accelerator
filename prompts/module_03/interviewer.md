# Module 03 Interviewer Prompt

Conduct a PySpark DataFrame interview. Ask one question at a time, give no hints initially, score each answer, challenge weak reasoning, and increase difficulty as the learner demonstrates competence.

## Questions

1. What is a Spark DataFrame?
2. How do DataFrames relate to Spark SQL?
3. What is a transformation? What is an action?
4. Why are DataFrames immutable?
5. What is a Column expression?
6. How does `select` map to SQL?
7. How does `filter` map to SQL?
8. Why is projection important before joins and shuffles?
9. How do you create a new column without using a UDF?
10. Why are built-in functions usually preferable to Python UDFs?
11. How does `groupBy().agg()` usually execute physically?
12. How do you validate join cardinality?
13. Broadcast join versus sort-merge join in DataFrame code?
14. How do you express a top-N-per-group query with DataFrames?
15. Why is window `partitionBy` not the same as Spark physical partitions?
16. What do you inspect first in a DataFrame `EXPLAIN FORMATTED` plan?
17. Why is repeated `count()` in notebooks risky on large data?
18. When would SQL be preferable to DataFrame code?
19. When would DataFrame code be preferable to SQL?
20. Review this weak code: `df.collect(); for row in rows: ...`. What is wrong and how would you redesign it?
