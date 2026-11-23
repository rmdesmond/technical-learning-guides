# The matn prompt

A matn is the condensed form of a learning guide: the skeleton of the subject,
to be memorized, that reminds you of what the full guide covers. It states
without explaining. Its chapters match the learning guide's chapters one to
one, with numbered lines in each chapter.

Input: a finished `<subject>-learning-guide.pdf`.
Output: `<subject>-matn.pdf`, saved in the same subject folder.

## The prompt

```text
TODO: paste the exact prompt used to produce the matn.
```

## What a finished matn contains

Taken from the existing matns (CMake, Google Test, Linux command line):

- A title page with the chapter count and line count, plus "What this is",
  "How to use it" and the tool version.
- The same chapters as the learning guide, each with a short title
  ("On generation", "On targets", ...).
- Numbered lines that run on across chapters, one statement per line.
