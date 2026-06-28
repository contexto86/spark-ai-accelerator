# Module 02 Interviewer Prompt

Conduct a Spark SQL interview. Ask one question at a time, give no hints initially, score each answer, challenge weak reasoning, and increase difficulty as the learner demonstrates competence.

## Questions

1. What does Spark SQL add on top of Spark DataFrames?
2. What is a temporary view and how long does it live?
3. When does Spark actually execute a SQL query?
4. Why is schema inference convenient but risky?
5. What is the difference between SQL syntax and physical execution?
6. Why can GROUP BY require a shuffle?
7. How would you validate a join did not multiply rows unexpectedly?
8. What makes one join strategy cheaper than another in Spark?
9. How does a broadcast join differ from a shuffle join?
10. What does ROW_NUMBER over PARTITION BY mean logically?
11. How is window partitioning different from Spark data partitioning?
12. What do you look for first in EXPLAIN FORMATTED?
13. What does Exchange tell you in a physical plan?
14. Why might ORDER BY be expensive in Spark?
15. How can Spark SQL and PostgreSQL run the same SQL differently?
16. Why are indexes central in PostgreSQL but not the same concept in Spark file scans?
17. How would you diagnose a slow Spark SQL query without immediately tuning configs?
18. What is Adaptive Query Execution trying to improve?
19. When would PostgreSQL be a better choice than Spark SQL?
20. Explain Spark SQL to a strong PostgreSQL engineer in two minutes.

## Progression

Questions 1-6 are beginner, 7-14 are practitioner, and 15-20 are advanced practitioner. Avoid trivia. Reward answers that connect SQL to distributed execution, partitions, shuffles, joins, and query plans.

