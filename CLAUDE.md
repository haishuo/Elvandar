# Elvandar — working rules

This repository is an eight-book fantasy series in draft. There is no code here. The work is
prose, beat drafts, character sheets, and worldbuilding canon, and the standards below are
editorial standards, not engineering ones. The one exception is `Tools/`, which holds the
Royal Road export script; nothing else here is code.

Read this file before proposing any change to a chapter, beat draft, or character sheet.

---

## 1. The rule hierarchy

This is the author's, it is binding, and it is ordered. When two considerations conflict, the
lower number wins. Every proposed change gets checked against these in order.

0. **Book 1 only — remember what the name of the book is.** The camera stays on Xion's
   shoulder. This is not craft, it is the theme of the book. If someone like Janice must exist,
   she exists through Xion's eyes and ears. The camera is either *in* Xion or *on* Xion, and by
   default you do not describe things Xion neither sees nor does.

   **Moving it off him is allowed, but it has to be argued for.** The argument must be about why
   *this* scene earns the move in a book called *The Grain Merchant's Son* — "we are establishing
   the entire book here," "we are ending the entire book here and this is a cinematic pull-away."
   Those are real reasons. Inside the body of the book they are also rare: assume the move is
   wrong roughly ninety-nine times in a hundred, and if the argument is not one you would write
   down, don't make it.
1. **Things must make sense.** If something becomes logically incoherent, the plot changes.
2. **Characters must behave like themselves.** No changing people's personalities to make a
   point. *The plot serves at the sufferance of characterization, never vice versa.*
3. **Scenes designed for one emotion — wonder, joy, triumph, despair — stay that way.**
   "Resolution" can happen around the edges. It must never dilute.
4. **Only here, at #4, is thematic resonance.** Only if making something more thematic does
   *not* conflict with 1, 2, or 3 is it permitted to exist.

A fix that is elegant, resonant, and loses on rule 2 is not a fix. Say so and drop it.

### Corollaries

**The Jurassic Park principle (under rule 3).** Some scenes take a single emotion and nothing
else. Book 1 ch25 is pure triumph — *"Dr Sattler, my dear Dr Grant. Welcome to Jurassic Park."*
Malcolm at lunch, not Malcolm at the gate. Do not sneak grief, irony, or arc-closure into a
scene built for one feeling. If a character's arc wants closing, close it elsewhere.

**A recurrence must change someone's position, not their volume.** A line, image, or argument
returning for the third time has to *move* something. Saying it again louder is not a
recurrence, it is repetition, and repetition is this series' dominant structural failure mode.
Watch especially for arguments that re-run instead of escalating.

**One action, five meanings.** Show-don't-tell is the old saw; the operative test is **density**.
Tywin field-dressing the stag says five things at once — steady hands and no fear of blood;
destruction is what this man *does*; he does work he could delegate; he is so used to it he can
hold a conversation through it; and the animal is his enemy's heraldic beast. One action. Five
meanings. Not one line of dialogue decodes any of it.

Measure actions against that. **An action carrying one meaning is an illustration**, and an
illustration needs dialogue to explain what it illustrates — which is telling with extra steps,
and worse when a supporting character does the illustrating, because then it costs screen time
as well. Prefer the prop already in the character's hands for other reasons: the best ones mean
several things because they *are* several things.

**Fixes work when they use the character's actual instrument.** Xion is a healer, so he reads
bodies — he does not narrate combat he cannot follow. Kael reads other men's books. Farleen
counts doors and sight lines. Elara reads rooms and strikes. Generic competent description is
almost always the wrong answer; the specific expertise is almost always the right one.

**Verify blast radius before any structural change.** Grep for downstream dependencies first.
A beat cut in ch17 can be load-bearing in ch22.

**Never plant what isn't paid.** Foreshadowing that never resolves gets cut, not kept "in case."
If a seed is planted in one book and detonates in another, record it in the cross-book threads
section of `Series Review - Master List.md`.

---

## 2. Hard canon

**`TGMS - OLD/` is NON-CANON.** Exclude it from every continuity check, grep, and citation.
It is not an earlier draft to be reconciled — it is not canon at all.

**The saga measures in months, never years.** Book 2 spans ~5 months; Book 3 opens weeks after
it. See `Story Timeline.md`, which is authoritative. Do not write "years ago" about anything
inside the Book 1–3 span.

**Terminology (locked).** *Kaha'an* = the capital city. *Balisha* = the state Elara rules today.
*The Balishan Empire* = the historical seven-province extent. The Compact = Gunastran + Erulius
+ Vartonne; the Tripartite Alliance = Balisha + Uratha + Terinok.

**The Rending** happened ~20 years before Book 1. There is only one. Never reintroduce "First
Rending" or "Sundering." `Magic/The Rending.md` is authoritative.

**Lathion.** Built ~5,000 years ago, sealed ~2,000 years ago, inhabited until ~20 years ago.
Fresh tomb, not ancient one. The Destiny Engine was built in months during the Rending crisis
and should look visibly hastier than everything around it. Characters do not know Lathionese
proper names and neither does the narrator in Xion's POV.

**Book 3 Chapter 5 (`Chapters/Chapter 5 - Wonder.md`) is LOCKED.** Do not revise it.

---

## 3. The Seven Paradigms

`The Seven Paradigms.md` defines seven motivational cores — Truth Seeker, Caretaker, Engineer,
Founder, Creator, Spirited Competitor, Merchant — which every character carries as a stack
summing to 100%, ranked as a sacrifice hierarchy. Under stress the dominant ones surface.

**Use this to validate characterization decisions, not to generate them.** When a proposed line
feels off, check it against the character's stack in `People/`. Most rule 2 violations show up
here first: a Caretaker refusing to help on principle, an Engineer offering comfort, a Merchant
acting out of loyalty.

Conflicts between characters are often unwinnable by design because their stacks differ — e.g.
Xion's primary (Caretaker) is Janice's secondary and her primary (Engineer) is his third, which
is why the copper argument has no correct answer and neither of them is wrong.

---

## 4. Character guardrails

These live in full in `People/`. The load-bearing ones:

- **Janice** never says "Xion" or "Kemvimore." She calls him Fen, always. If she ever speaks
  his real name aloud she becomes an exposition device and the relationship deflates. Her
  knowledge is conveyed only by what she declines to ask. She never absolves him, and she
  never lets him write anything down.
- **Xion** asks permission — *"Can I have a look?"* — and the moment he stops asking is the
  moment the wound is driving him instead of the practice. Track every break.
- **Elara's** royal trait (blue-to-amber) is rationed. It is involuntary and rare; count the
  occurrences before adding one.
- **Rosik** does not explain himself and encounters no resistance. That *is* Rosik. Do not give
  him an interlocutor to make a scene easier to write.
- **Mira Fen** is Xion's defining wound: *"she died, and I didn't do anything."* Every patient
  is a coin paid into a ledger that will never balance. Do not let another character take over
  that function.
- **Xion does not become his father, and nobody tells him he has.** He already went there — four
  chapters of Book 2 — and he knew it while he was doing it. B2 ch18 is titled `Don't.` because
  *he* says it, to himself, mid-manoeuvre. Never write a scene where a character delivers that
  verdict to his face; it would hand him something he reached alone and under his own power. The
  difference between him and Rosik is not capability, and it is not virtue. Book 2 proves he is
  capable. It is that afterward he **breaks** — B2 ch20, the low wall, *"the way a wall goes,
  which is from the inside"* — and Rosik never does. He has a fault line. His father doesn't.

---

## 5. Working practice

**Propose before applying, for anything structural.** Bring the specific scene, the proposed
fix, the rule it serves, and the blast radius. The author signs off. Small continuity
corrections and typo-level fixes don't need this.

**Work sequentially.** Each chapter should be correct before moving to the next. Writing
chapters independently and reconciling later has been tried and does not work.

**Handle a class of problem in one pass, not piecemeal.** If a habit appears in nine places,
fix all nine together so the books get one consistent through-line.

**Record what you do.** `Series Review - Master List.md` is the canonical record — organized by
rule tier, and carrying the cross-book threads, character guardrails, open questions, the
chapter manifest, and the changelog. Update it in the same commit as the change.

**Report honestly.** If a proposed fix was declined, say why. If a flag turned out not to be a
real problem, say so plainly and record it rather than quietly inflating it into one. Do not
claim a change is applied without applying it.

---

## 6. House style

**Prose:** close third-person limited, clean, not ornate. Sentences that work hard. Emotional
truth over explanation. The narrator knows only what the POV character knows. Match Book 1.

Avoid: stating the theme in dialogue; summarizing a scene's meaning after the scene; characters
articulating their own arcs; adverb-propped attribution; on-the-nose symbolism. When a paragraph
explains what the previous paragraph already did, cut the explanation.

**Emphasis:** single-word stress emphasis is **bold**. Italics carry everything else — interior
thought, emphasis running to more than one word, letters and documents, and a word cited as a
word. If more than one word needs the weight, it is italic, not bold.

The cited-word case is the one that gets mishandled. A word being *named* is not being stressed,
however short it is — "an officer of mine used the word `*body*`"; "`*no*` was a word for people
without the right name"; Janice's `*Fen.*` landing after she says it; Rosik's `*Building.*`.
The test: if the sentence is about the word, it stays italic; if the weight is in the voice
saying it, it goes bold. Applied across Books 1–2; the full exclusion list is in the changelog
in `Series Review - Master List.md`.

**Chapter files:** one file per chapter in `Chapters/`, named `Chapter N - Title.md` — a space
either side of a hyphen, the number unpadded, the title in Title Case. `Chapter 7 - Fine.md`,
not `chapter7.md` or `Chapter 07 - Fine.md`.

The filename is the only place the title lives. Do **not** put a `# Chapter N: Title` heading
inside the file — it was redundant with the filename and has been stripped from every chapter.
The file opens on its first line of prose.

Scene break is exactly three hyphens on their own line, `---`, blank line either side. Not four,
not five, not asterisks.

These three rules are load-bearing: `Tools/royalroad_export.py` derives the Royal Road filename
from the chapter filename, treats a leading heading as a paragraph, and renders a scene break as
`<p>---</p>`. Rename or restructure a chapter and you must regenerate — see §7.

**Beat drafts:** present-tense analytical scene outlines. Numbered beats, header block
(Timeline / Characters / Emotional work / POV), footer notes on the load-bearing decisions.
Functional planning documents, not prose. `Templates/Beat Draft Template.md` is the pattern.

**Character sheets:** stack first, then function, then guardrails. The guardrails are the point —
they are what stops a character from drifting between books.

---

## 7. Layout

```
Book N - Title/
  Chapters/          finished or drafted prose — `Chapter N - Title.md`
  Beat Drafts/       chapter plans
  Royal Road/        GENERATED paste-ready HTML. Never edit by hand.
  *_skeleton.md      chapter-level outline
People/              character sheets
Places/              geography and settings
Magic/               metaphysics, incl. the authoritative The Rending.md
Templates/           document patterns
Tools/               royalroad_export.py — regenerates every Royal Road/ folder
Story Timeline.md            in-series chronology (authoritative on timing)
Global Historical Timeline.md
The Seven Paradigms.md       the characterization framework
Series Review - Master List.md   editorial record and outstanding work
elvandar_series_outline.md
TGMS - OLD/          NON-CANON. Ignore entirely.
```

**Regenerating the Royal Road HTML.** `Royal Road/` is build output. After any prose edit,
rename, or scene-break change, run it again and commit the result alongside the prose:

```
python3 Tools/royalroad_export.py            # every book
python3 Tools/royalroad_export.py "Book 2"   # one book
```

It is idempotent — re-running over unchanged prose produces no diff, so it is safe to run at
the end of any session. Never hand-edit a file under `Royal Road/`; the next run overwrites it.
