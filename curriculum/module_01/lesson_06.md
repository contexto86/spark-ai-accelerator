# Lesson 06: Architecture Synthesis

## Learning objective

Explain Spark architecture accurately at different levels, defend system
choices, and answer scenario questions with evidence and trade-offs.

## Predict before reading

Explain Spark aloud in 60 seconds without using the phrases “big data” or “in
memory.” Include driver, executor, partition, lazy evaluation, DAG, and one
reason not to use Spark.

Then repeat for a manager who needs to approve platform investment. Notice
which details should change and which claims must remain true.

## Knowledge reference

- `knowledge/module_01/08_interview_notes.md`
- Revisit chapters 01–07 only for gaps revealed by your attempt.

## Practical example

An interviewer says: “Our Spark job has 2,000 cores, but the final stage uses
one core for 50 minutes. What would you do?” A strong response does not request
more cores. It clarifies partition count and key distribution, inspects task
metrics and the physical plan, hypothesizes a global operation or skew, then
proposes a change with its trade-offs.

## Exercises

Complete `exercises/module_01/exercise_06.md`, then attempt
`checkpoints/module_01/checkpoint.md` without notes. Use
`prompts/module_01_interviewer.md` for interview practice.

## Reflection questions

- Which architecture concept is hardest to explain without jargon?
- Do your answers name evidence that would falsify your first hypothesis?
- Can you explain the cost moved by each proposed optimization?
- Can you reject Spark confidently without sounding unfamiliar with it?

