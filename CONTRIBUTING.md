# Contributing

## How a guide is produced

1. **Learning guide.** Run [the learning guide prompt](prompts/learning-guide-prompt.md)
   for the subject. Work through the result yourself, typing every example,
   and fix what breaks. Export it as `<subject>-learning-guide.pdf`.
2. **Matn.** Run [the matn prompt](prompts/matn-prompt.md) on the finished
   learning guide. Check that its chapters match the guide's chapters one to one.
3. **Beyond the Basics.** Run [the Beyond the Basics prompt](prompts/beyond-the-basics-prompt.md),
   starting from the learning guide's "Beyond the basics" roadmap.
4. **Way Beyond the Basics.** Run [the Way Beyond the Basics prompt](prompts/way-beyond-the-basics-prompt.md)
   on the Beyond the Basics guide.

A subject can stop at any step. Only the learning guide is required.

## Adding a guide

1. Put the PDF in its subject folder, `guides/<n>-<group>/<subject>/`. If the
   subject is new, create its folder in the group where a learner meets it
   first.
2. Add the subject's row to the README catalogue, or add a link to its existing row.
3. Add a line to [CHANGELOG.md](CHANGELOG.md).

If a guide doesn't fit any existing group, the grouping is probably wrong.
Fix the grouping first.

## Conventions

- File names are lowercase and hyphenated: `<subject>-learning-guide.pdf`,
  `<subject>-matn.pdf`, `<subject>-beyond-the-basics-learning-guide.pdf`,
  `<subject>-way-beyond-the-basics-learning-guide.pdf`. Never rename a file
  once it is published.
- Each subject lives in exactly one group folder.
- Commit PDFs only. Keep the conversation and any build script out of the repo.
- To revise a guide, overwrite the file and add a CHANGELOG line. When a batch
  of changes lands, tag the repo with the month, for example `v2026.11`.
- Short reference sheets go in `cards/`, never in `guides/`.
- Before committing a PDF, check it for personal information, including its
  metadata (Author, Creator).

## Review

Before a guide is merged, someone other than the author works through it
from start to finish on a clean machine, at the tool version the guide states.
