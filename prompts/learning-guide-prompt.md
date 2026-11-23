# Prompt: Turn a "teach me X" conversation into a guided learning PDF

Paste the text below the line into any chat where you have been introducing a software tool, library or concept and want the rest of the journey mapped out and delivered as a self-paced PDF. It works whether the conversation has covered one step or several: Claude continues the journey on its own, then builds the guide.

Replace `<SKILL>` with the tool or concept (e.g. "Google Test", "Docker", "git rebase"). Everything else can stay as is.

---

Produce a complete, self-paced learning guide for **<SKILL>**, delivered as a PDF. Do not wait for me to ask "and next?" for each step: plan the whole journey yourself, then build the guide.

## How to plan the journey

- If this conversation has already introduced <SKILL> (an answer to "Someone doesn't know <SKILL> at all. How would you introduce it to them?" and possibly some "and next?" follow-ups), keep those steps as the opening chapters. Preserve their framing, examples and wording where they are good; do not rewrite them into something generic.
- If nothing has been covered yet, write the first chapter the way you would answer that question: the problem the tool solves, stated before any syntax; the smallest working example; what to deliberately skip at first.
- Add the next steps until the reader reaches a working, employable level of the skill. That is usually 4 to 7 chapters total. Do not pad; stop when a competent beginner could use the tool unaided on a real project.
- Every chapter introduces **exactly one new idea** and states it in one sentence at the top ("One idea: ..."). If a step needs two ideas, it is two chapters. If an idea is a minor add-on to a chapter's main idea, fold it in as an "upgrade" at the end of that chapter rather than its own chapter.
- Order the chapters by what a learner is forced to meet next on a real project, not by what is most elegant. The thing that bites them first comes first.
- Each chapter should build on the project from the chapter before, so by the end the reader has one evolving example, not a pile of disconnected snippets.
- Deliberately leave things out. Everything you skipped goes into the final "Beyond the basics" roadmap with a reason for skipping it.

## Structure of the PDF

1. **Cover.** Title ("Learning <SKILL>"), a one-line subtitle describing where the reader ends up, three short paragraphs: who it is for, how long it takes, which version(s) of the tool it targets. Date.
2. **Before you start.** Three parts:
   - *How to use this guide*: work in order, type the code, tick the checklists, read the "Common trap" boxes.
   - *Assumed knowledge*: a checklist titled "I am comfortable with" listing the prerequisites. Be honest and specific; "if any item is unfamiliar, spend fifteen minutes on it first."
   - *Setup*: a checklist titled "Installed and working" with the exact verification command for each item. Add a callout for any platform that behaves differently.
3. **Chapters.** Each one has, in this order:
   - "CHAPTER n" kicker, title, and the one-sentence "One idea" subtitle.
   - *Why*: the problem this chapter's idea solves, in plain language, before any syntax.
   - The explanation, with the minimal working code (directory layouts, files, terminal commands) in captioned code blocks. Explain what each line does the first time it appears.
   - One or more **Common trap** callouts: the mistakes almost everyone makes, and the fix.
   - Optional: a short reference table or an "upgrade" section introducing a small related tool.
   - A **Do this** checklist: 3 to 5 hands-on exercises. At least one should deliberately break something so the reader sees the failure mode and learns to read the error.
   - A **You should now be able to** checklist: 2 to 4 self-assessment statements. These should test understanding, not recall ("Predict, before building, whether..." rather than "Remember the syntax of...").
4. **Where you are now.** A "Final self-check" checklist summarising the capabilities gained across all chapters, followed by a one-page **Quick reference** table (Need → Command).
5. **Beyond the basics.** A numbered, ordered roadmap of 6 to 10 topics that were skipped, each with *What* (the concrete feature or command names) and *Why and when* (which real-project situation forces it on you). Tell the reader to pick the one their next project demands rather than learning all of them. End with a short *Recommended references* list (official docs, the one best book, one free online guide, one talk, one well-maintained real project to read) and one final habit worth forming.

## Conventions

- Prose first, syntax second. Every code block must be preceded by a sentence saying what it is for.
- Prefer the modern, recommended way of doing things and explicitly warn about the legacy way the reader will find in old tutorials.
- Use concrete, well-known examples (a popular small library, a real command) rather than invented placeholders where possible.
- Pin versions in any downloaded dependency and say why.
- Avoid "genuinely", "honestly", "straightforward". No filler, no recap paragraphs.
- Tone: direct, warm, confident. Treat the reader as a capable adult who has simply never seen this tool.

## Production

- Build the PDF with reportlab (Platypus). Letter size, one-inch margins, Helvetica body, Courier code. Code blocks in a light grey box with a caption; callouts in a tinted box with a coloured left rule (blue for information, orange for "Common trap"); checklists as rows with a drawn empty square so the reader can tick them on paper or in a PDF viewer. Footer with the guide title and page number on every page after the cover.
- Do not use Unicode box or check characters; draw the checkbox squares on the canvas.
- After building, render two or three pages to images and look at them to confirm the checkboxes, code blocks and callouts display correctly before sending.
- Name the file `<skill>-learning-guide.pdf` (lowercase, hyphenated). Send it to me, and save a copy to the attached project if one is attached.
- In your reply, give a two- or three-sentence summary of the chapter list and anything you chose to leave for the roadmap. Do not restate the contents.

---

## Notes for reuse

- The usual flow: open a chat with "Someone doesn't know <SKILL> at all. How would you introduce it to them?", ask "and next?" as many times as you like, then paste this prompt. The prompt also works as the first message in a fresh chat; it will write the introduction itself.
- If you want a particular platform or language emphasised ("Windows-first", "C, not C++", "Python bindings"), add one line after the skill name.
- The CMake guide produced on 2026-10-20 (`cmake-learning-guide.pdf` in this project) is the reference example for the format.
