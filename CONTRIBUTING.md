# Contributing

## How a guide is produced

Guides are made in a Claude project. Put [`prompts/instructions.md`](prompts/instructions.md)
in the project instructions and add [`prompts/learning-guide-prompt.md`](prompts/learning-guide-prompt.md)
to the project files.

1. **Introduction.** Ask "Someone doesn't know `<SKILL>` at all. How would you
   introduce it to them?" Ask "and next?" until you're ready for the guide.
2. **Learning guide.** Ask for the learning guide. Claude follows
   `learning-guide-prompt.md` and keeps the conversation so far as the
   opening chapters. Work through the result yourself, typing every example,
   and fix what breaks. The file is `<skill>-learning-guide.pdf`.
3. **Matn.** Ask for "the matn for `<SKILL>`". Claude builds it from the
   learning guide, one chapter per guide chapter. Check that the chapters
   match one to one. The file is `<skill>-matn.pdf`.
4. **Beyond the Basics.** Ask for it when the learning guide's "Beyond the
   basics" roadmap is where your projects are heading. The file is
   `<skill>-beyond-the-basics-learning-guide.pdf`.
5. **Way Beyond the Basics.** Ask for it after Beyond the Basics. The file is
   `<skill>-way-beyond-the-basics-learning-guide.pdf`.

A subject can stop at any step. Only the learning guide is required.

## Adding a guide

1. Put the PDF in its subject folder, `guides/<n>-<group>/<subject>/`. If the
   subject is new, create its folder in the group where a learner meets it
   first.
2. Add the subject's row to the README catalogue, or add a link to its existing row.
3. Add a line to [CHANGELOG.md](CHANGELOG.md).
4. Add the subject or topic guide to `scripts/build-tracker.py` and
   `scripts/build-binder-cover.py`, and rebuild the tracker and binder cover
   (see [Scripts](README.md#scripts)). If you added a group, update and
   rebuild `START-HERE.pdf` with `scripts/build-start-here.py`.

If a guide doesn't fit any existing group, the grouping is probably wrong.
Fix the grouping first.

## Conventions

- File names are lowercase and hyphenated: `<subject>-learning-guide.pdf`,
  `<subject>-matn.pdf`, `<subject>-beyond-the-basics-learning-guide.pdf`,
  `<subject>-way-beyond-the-basics-learning-guide.pdf`. A topic guide inside
  a subject folder uses the topic in place of the subject, for example
  `cpp/move-semantics-learning-guide.pdf`. Never rename a file once it is
  published.
- Each subject lives in exactly one group folder.
- Commit a guide as a PDF only. Keep the conversation and the guide's own
  build script out of the repo. `scripts/` is only for tools that work on
  the repo as a whole.
- To revise a guide, overwrite the file and add a CHANGELOG line. When a batch
  of changes lands, tag the repo with the month, for example `v2026.11`.
- Short reference sheets go in `cards/`, never in `guides/`.
- Before committing a PDF, check it for personal information, including its
  metadata (Author, Creator).

## Review

Before a guide is merged, someone other than the author works through it
from start to finish on a clean machine, at the tool version the guide states.
