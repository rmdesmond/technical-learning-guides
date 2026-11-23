# The learning guide prompt

Every subject starts here. The learning guide this produces is the base guide.
The other three guide types are built from it:

1. **Learning guide** (this prompt): `<subject>-learning-guide.pdf`
2. **Matn**: [matn-prompt.md](matn-prompt.md), `<subject>-matn.pdf`
3. **Beyond the Basics**: [beyond-the-basics-prompt.md](beyond-the-basics-prompt.md), `<subject>-beyond-the-basics-learning-guide.pdf`
4. **Way Beyond the Basics**: [way-beyond-the-basics-prompt.md](way-beyond-the-basics-prompt.md), `<subject>-way-beyond-the-basics-learning-guide.pdf`

## The prompt

Replace `<subject>` with a technical field, subject or particular tool:

```text
If someone doesn't know anything about <subject> at all, how would you
introduce them to it? And then write the learning guide for it.
```

## What a finished learning guide contains

The existing guides share these features. Check a new guide against them
before you commit it:

- A title page that says who the guide is for, how long it takes and which
  version of the tool it targets.
- A "Before you start" page that sets up the tool.
- The problem the subject solves comes first, before any syntax.
- One new idea per chapter, all on one example that grows chapter by chapter.
- Exercises and checklists to tick, and "Common trap" boxes.
- A "Beyond the basics" roadmap at the end that lists what was left out on
  purpose and suggests an order for learning it. This roadmap is where the
  Beyond the Basics guide starts.
