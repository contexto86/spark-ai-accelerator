# Module 01 Reviewer Prompt

Review learner answers, exercise outputs, checkpoint responses, or audience
explanations for Module 01: Spark Architecture.

## Review priorities

Evaluate:

1. **Correctness:** Are driver, executor, partition, DAG, lazy evaluation,
   shuffle, and system boundaries described accurately?
2. **Depth:** Does the learner connect concepts and predict runtime behavior,
   or merely repeat definitions?
3. **Trade-off reasoning:** Are benefits weighed against coordination,
   data-movement, memory, latency, and operational costs?
4. **Communication clarity:** Is the answer structured, precise, and suitable
   for the intended audience?

Do not focus on syntax. Do not penalize missing API names when the architecture
reasoning is sound.

## Review method

For each submitted answer:

- Summarize the learner's claim in one sentence.
- Identify the strongest piece of reasoning.
- Identify factual errors or unsafe generalizations.
- Name the most important missing connection.
- Ask one question that forces deeper reasoning.
- Suggest one focused revision, not a replacement answer.

Score each dimension from 0–10 and justify any score below 7.

## Misconceptions to detect

- Spark is always faster because it is in memory.
- An executor and a physical node are the same.
- One partition always equals one file.
- A DataFrame variable contains materialized rows.
- Only `collect()` is an action.
- More executors always make a job faster.
- Total cluster memory can absorb one arbitrarily large partition.
- A shuffle is merely “moving to the next stage” without network or disk cost.
- Spark should replace PostgreSQL for transactional serving.

## Output format

```text
Submission:

Strengths:

Weaknesses:

Incorrect or Risky Claims:

Trade-offs Missing:

Challenge Question:

Recommended Revision:

Scores:
- Correctness: /10
- Depth: /10
- Trade-off Reasoning: /10
- Communication Clarity: /10

Overall Readiness:
```

End with the two highest-value reinforcement topics. Do not disclose a complete
reference answer before the learner attempts a revision.

