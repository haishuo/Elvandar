# Templates — Instructions for Claude

This folder contains templates for recurring document types in the Elvandar series. Before using any template, read it in full — each one includes notes on format, tone, and intent.

---

## Generating Beat Drafts

### Inputs
1. **The chapter skeleton** — found in the book's main directory, named `book[N]_chapter_skeleton.md`. This is the authoritative source for chapter titles, chapter order, and what each chapter is meant to accomplish narratively.
2. **Beat Draft Template** — `Templates/Beat Draft Template.md`. Read this before generating any beat draft.
3. **Existing beat drafts** — found in another book's `Beat Drafts/` folder. Read at least one before starting, to calibrate tone and analytical register.

### Output
Save each beat draft to:
```
[Book Folder]/Beat Drafts/Chapter [X] - [Title].md
```
For example: `Book 3 - Crown Jewel/Beat Drafts/Chapter 1 - Scars.md`

The chapter title in the filename should match the title used in the skeleton.

### Process
1. **Read the skeleton first.** Before generating anything, read the full chapter skeleton and flag any ambiguities, gaps, or potential issues to the author. Resolve these before generating.
2. **Generate all beat drafts in parallel.** Once the skeleton is confirmed, launch one sub-agent per chapter. Each agent receives: the skeleton entry for its chapter, the Beat Draft Template, and at least one example beat draft from a previous book for tone/format calibration.
3. **Save immediately.** Each agent saves its beat draft to the correct file before finishing.
4. **Review together.** Once all drafts are generated, go through them with the author chapter by chapter, revising as needed.

Do not generate one beat draft at a time and wait for approval before continuing — the bulk approach is more efficient. Generate everything first, then review.

---

## Character Pronoun Reference

Always read a character's file in `/People/` before writing beats that feature them. The following are easy to get wrong:

- **Sa Ko Ren** — she/her. The name reads ambiguously; she is female. Her character file is `/People/Sa Ko Ren.md`.

When grepping for pronoun errors, note that a character's name may appear in one sentence and the incorrect pronoun in the next — a same-line grep will miss these. Read surrounding context carefully.

---

## Other Templates

*(Add entries here as new templates are created.)*
