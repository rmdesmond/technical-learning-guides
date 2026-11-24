When the user asks “Someone doesn’t know <SKILL> at all. How would you introduce it to them?”, answer conversationally: frame the problem the tool solves before any syntax, give the smallest working example, name the one mental model that makes it click, and say what to deliberately skip at first. When they follow up with “and next?”, introduce exactly one new idea that a learner would be forced to meet next on a real project, and don’t overburden the step.

When the user asks to build the learning guide (or to turn the conversation into a PDF), read prompts/learning-guide-prompt.md in this project and follow it for that skill, keeping whatever has already been covered in the chat as the opening chapters. 

When the user asks for a matn of a skill (or “the matn for <SKILL>“, “distil <SKILL> into a matn”), A matn is a short, terse, numbered primer with one chapter per chapter of that skill’s learning guide, stating the skeleton without explaining it. If <skill>-learning-guide.pdf does not exist in the project yet, first build the learning guide by following prompts/learning-guide-prompt.md, deliver it, then produce the matn from it. 

A beyond-the-basics guide is the next guide after the learning guide, if the user asks for it.

A way-beyond-the-basics guide goes even further, if the user asks for it.
