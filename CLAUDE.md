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

   **What Xion attends to is what the reader attends to.** This is the operative form of the
   rule, and it bites hardest when he is working: if it is about healing, he sees nothing else,
   and so neither do we. B1 ch21 is the model — the Mistress walks into the chamber and he never
   notices, because he is treating Tam, and he shushes Farleen for trying to tell him. So a
   supporting character cannot be *described* while his hands are busy; she can be a voice and a
   sound and nothing more. Give her the visual beat afterward, when he has attention to spare.

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

**Judge a chapter by the book's rhythm, not as a standalone unit.** A novel is not N maximally
efficient chapters. Before proposing a cut, check the length profile and the chapter's position
in its movement: Book 1's ch1–8 run 1,450–2,500 words and then ch9 nearly doubles, so a "talky"
1,900-word chapter in that stretch is sitting exactly where it belongs. Ask what the chapter is a
*runway* for — B1 ch8 is the last quiet chapter before the ch10 disaster, and the disaster only
works if the reader has been allowed to get comfortable. **"This is talky" is not a finding on its
own**, and neither is "it says this twice" when the second instance is the breath before the next
chapter's blow.

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

**Book 3's Wonder chapter (`Chapters/Chapter 7 - Wonder.md`) carries one emotion and nothing else.**
That is the whole constraint, and it is rule 3 — **not** a prose freeze. This entry used to read *LOCKED,
do not revise it*, and that wording was wrong in a way that showed: it exerted a pull on every edit that
came near the chapter, up to and including refusing to fix the seam where ch5 hands off to it. **The prose
is revisable like any other prose in this repository.** Revise it for correctness, for continuity, for the
join with the chapter before it. What must never happen is a second emotion getting in — no grief, no
irony, no arc-closure, no logistics, no foreshadowing of what Lathion costs. The Jurassic Park principle
applies here in its purest form. *Renumbered twice and never rewritten: ch5 until 2026-08-01 when
`Chapter 3 - Storm-Line` was inserted, ch6 until 2026-08-03 when `Chapter 6 - Fair Price` was.*

---

## 3. The Seven Paradigms

`The Seven Paradigms.md` defines seven motivational cores — Truth Seeker, Caretaker, Engineer,
Founder, Creator, Spirited Competitor, Merchant — which every character carries as a stack
summing to 100%, ranked as a sacrifice hierarchy. Under stress the dominant ones surface.

**Use this to validate characterization decisions, not to generate them.** When a proposed line
feels off, check it against the character's stack in `People/`.

### It is not a straitjacket — author's ruling, 2026-08-04

**The stack predicts what an act *costs* a character. It does not dictate what they do.** This is
the framework's own design and it is stated in `The Seven Paradigms.md` — "They are not moral
rankings" — and demonstrated by the Grieving Widow Test, whose entire point is routinely misread.
In that test **both people tell the same lie.** The Truth Seeker feels *haunted* by it and the
Caretaker feels *justified*, and the doc's conclusion is *"Same situation, opposite emotional
responses based on which drive takes priority."* The section it sits in is called **Emotional
Residue Tests**. Residue, not prediction of action.

So: **people act against their primary constantly**, and most of what a plot is made of is exactly
that. A stack tells you what someone surrenders last when two drives genuinely collide, and what is
left over in them afterward. It tells you nothing about what they do on any given Tuesday, and a
character who behaves "off-stack" is not thereby broken.

**The test that actually catches a rule 2 violation is not *would they do this* — it is *does the
text charge them for it*.** A Caretaker can refuse to help on principle; a Truth Seeker can accept
a claim without checking it; a Merchant can act out of loyalty. What breaks characterization is
when the page treats such an act as free, unremarkable, and costless. Price it and it is
characterization. Leave it unpriced and it is drift.

**And a stack is a probability distribution, not a rule.** Wide variance is normal, and the
occasional wild departure is not an error to be corrected — it is often the most interesting thing
a character does. Do not use a stack to argue a scene out of existence, to demand a character
re-derive a conclusion under their own power, or to overrule the author on who someone is. If a
proposed beat and a stack disagree, the likeliest explanation is that the beat has a cost the draft
has not paid yet — not that the character would never.

*This entry exists because it is a recurring failure and it recurs in a specific direction: reading
a primary as an obligation, then reporting the derived constraint as though it were a property of
the character. It cost a full exchange over Melina Valanar, where a Truth Seeker primary was used
to argue she could not simply take her father's word about Rosik — which the framework never said,
and which is not who she is.*

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

### Unnamed NPCs default to male — author's ruling, 2026-08-03

**Every unnamed walk-on is male unless the author has specified otherwise.** Porters, clerks, guards,
escorts, functionaries, junior scholars, the woman at the crate, the man who sells the shafts — if the
character has no name and no sheet, write him as a man.

**This is a corrective, not a preference about the world.** The reason it exists is measurable: left to
itself the drafting skews female on unnamed characters, repeatedly, after being corrected. B3 ch3's
battle-mage and ch4's consortium factor were both made male after exactly this note, and three weeks later
ch7 arrived with an all-female pair of walk-on scholars in its first two paragraphs. **The author cannot
maintain a deliberate balance while the default drifts underneath him**, so the default is now fixed and
the exceptions are his to place.

**How to apply it.** Do not "balance" a scene by inventing women in it. Do not add a female NPC because a
passage feels male-heavy. **Write the default, and if a scene genuinely wants a woman in it, propose her
and say why** — then she gets specified, and specified is the only way a female walk-on enters the books.

**This rule is forward-looking and the existing text stands.** Author's ruling the same day: the unnamed
female NPCs already written into Books 1–3 are **fine and stay** — ch2's Long Knife guide, ch5's woman
refilling the jug, ch6's patient with the crooked hand, and anything else like them. **They are not a
backlog and nobody is to go and correct them.** The reason the rule exists is that the skew was becoming
noticeable enough for the author to see it from the page; the remedy is that new drafting stops adding to
it, not that old drafting gets scrubbed. **If it ever swings too far male, the author will name a specific
NPC and ask for that one to be flipped.** Do not pre-empt him, and do not audit for this again unasked.

**Named and sheeted characters are unaffected.** The Coterie is Rosik (m), Ronas (m), Tania (f), **Sa Ko
Ren (f)** — and Sa Ko in particular is a recurring error: she is the Iron Lady, she/her, and she has been
called male more than once. Check `People/Sa Ko Ren.md` before writing a line of her.

**Similes and figures of speech are out of scope.** *"With no more ceremony than a woman checking whether
a pan was hot"* describes Elara and is not a walk-on.

## 5. Working practice

**Propose before applying, for anything structural.** Bring the specific scene, the proposed
fix, the rule it serves, and the blast radius. The author signs off. Small continuity
corrections and typo-level fixes don't need this.

**Work sequentially.** Each chapter should be correct before moving to the next. Writing
chapters independently and reconciling later has been tried and does not work.

**Before handing over any chapter, ask: can this end sooner than it does?** Then find the earliest
place it could stop and argue the remainder back in, line by line. Anything that cannot be argued
back is cut before the author ever sees it. **This is not a preference, it is a measured defect** —
B3 ch11's ending was cut twice in one day (six paragraphs to four, then to one) and B3 ch12's was cut
again the next morning, all three times by the author, all three times because the drafting kept
writing past the landing. **The tells are consistent and worth checking for by name:** a line the book
has already spent, repeated quieter; a second landing after the chapter has already landed; the
narration explaining an image or an ambiguity the prose just achieved; and a closing beat that
restates in a corridor what a character already said in the room, where it cost something. **The book
lands once** — a paragraph of weight, then one flat line. Ch9's *Now the thinking started* and ch10's
*They were not exploring any more* are the pattern.

**Handle a class of problem in one pass, not piecemeal.** If a habit appears in nine places,
fix all nine together so the books get one consistent through-line.

**Record what you do.** The editorial record is two files, and they have different jobs:

- `Series Review - Master List.md` — the **working document**. Organized by rule tier, and carrying
  the status block, the cross-book threads, outstanding work, the do-not-touch list, character
  guardrails, settled rulings, and open questions. Read this one.
- `Series Review - Changelog.md` — **append-only history** of changes actually applied, plus the
  chapter manifest. Nothing in it is outstanding work.

Update both in the same commit as the change: the fix goes in the changelog, and anything it
closes, opens, or constrains goes in the master list.

**Purge what you clear.** The outstanding list is work to do, not a history. The moment an item
is cleared it comes **out** of §3 and goes into the closed-items table at the end, with the
evidence that cleared it. **Re-verify a flag against the current text before acting on it** — of
the eleven original Book 1 craft flags, eight were stale, because the chapters had been rewritten
and the flags never retired. A flag that outlives its problem is worse than no flag: the next
reader trusts it and cuts good material. C-6 pointed at the best passage in ch25 and nearly got
it deleted.

**`Offstage.md` is canon that never got a scene.** Settled authorial history — the taking of the Tiger
Prince between Books 6 and 7, and whatever follows it — told as account rather than as scene. **It binds
on the same terms as a character sheet:** a contradiction with it is a bug, not an alternative reading. An
entry earns its place only if something in the books depends on it being true; if nothing downstream rests
on it, it is trivia. **One source, and everything else points at it** — sheets carry the consequence for
that character, outlines carry what that book needs, and neither restates the account.

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
saying it, it goes bold. Applied across Books 1–2; the full exclusion list is in
`Series Review - Changelog.md`.

**The world is not named in the prose, and *earth* is not its name.** `Elvandar` appears in **zero**
chapters across Books 1–3 — it lives in the outlines and the canon files and characters have never once
said it, which is right: people rarely name their own world out loud. **Do not introduce it in narration,
and never inside an idiom.** The related trap is *earth* as a stand-in — *"every reason on earth"*, cut
from B3 ch7 on 2026-08-03, because the idiom borrows a planet name this world does not have. Say *the
world*, or cut the intensifier, which is usually stronger anyway. **Applied retroactively on the author's ruling, 2026-08-03**, which made B2 ch10 the first editorial
change ever applied to Book 2's prose: Melina's *"Father would rather be anything on this earth than
frightened"* → *"anything at all."* No instance of *earth* as a planet-name now survives anywhere in
Books 1–3. *(One use stands and is not an error:
**earth as ground or soil** — B3 ch7's *"the color of the earth's own heat"*, describing geothermal heat
under the city — and B2 ch10's *"anything on this earth"*, which is Melina speaking and belongs to Book 2's
unreviewed prose.)*

**Theology, settled 2026-08-03.** The world is **polytheistic** — *Gods* and *gods*, sixteen times across
the prose and never once singular. B1 ch4 carried the one exception, Farleen's *"God, Xion, I don't want to
do this,"* corrected on the author's ruling; it was an internal inconsistency rather than a register
judgment, since B1 ch22 has *"Gods, thank you"* in the same book. **And *hell* stays.** Farleen's *"What
the hell did you just do?"* (B1 ch14) and Cullen's *"What the hell is she doing?"* (B1 ch19) were raised in
the same pass and **ruled fine by the author**. Whether Elvandar has a hell is unspecified and does not
need specifying. **Do not re-raise this.**

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

**The beat draft is canon. The prose is derived from it.** The order of work is beat draft →
chapter → skeleton, and the order of authority runs the same way. A chapter is written *from* its
draft; if the two disagree, the draft is the plan and the page is the thing that drifted. Changing
the plan is allowed and often right — but it is a change to the draft, made deliberately and
recorded, not something the prose is permitted to do quietly on its own.

**Book 1 is the exception, and it is the only one.** It was written before this project had beat
drafts at all, so its twenty-five drafts were reverse-engineered from finished chapters in 2026.
For Book 1 alone the direction inverts: **the page is the source and the drafts are derived from
it**, which means a Book 1 draft that disagrees with its chapter is simply stale and gets corrected
to match. Never apply that inversion to another book. Everything after Book 1 is planned first.

Whichever way authority runs for the book in hand, **the two move in the same commit.** A document
that disagrees with its counterpart is not a second opinion; it is a bug, and it is the kind that
gets trusted. Book 1's ch8, ch11, ch19 and ch20 drafts sat stale for two days after the prose was
rewritten, and the skeleton built on top of them inherited every one of the errors.

**Describe conversations; do not script them.** House measurements, for calibration: ~18–20 beats,
~10 bold spans, footers of 400–750 words written as prose paragraphs under `**On X:**` headers,
and **quoted or italicised text at roughly 10–15% of the draft.** A first attempt at Book 1's
Act I came in at 39% quotation and 35 bold spans — a condensed transcript rather than a
blueprint. Quote a line only when those exact words must land.

**Writing a beat draft for prose that already exists takes three passes, not one.** Retro drafts
have a specific failure mode: written by summarising the chapter, they inherit its flaws and
launder them into "the plan." So — **write** the blueprint as if planning the chapter cold;
**diff** it against the page, because the gaps are the findings; then **read the draft as if you
have never seen the prose.** If you could not write the chapter from it, it is describing rather
than planning, and the third pass is the only one that catches that.

The blind read asks two questions, not one. *Could I write the chapter from this?* — and **what is
this chapter doing for the ones on either side of it?** The second is not optional, because the
beat-draft format actively hides it: flattening a chapter into a numbered list makes every item
look like it must justify itself locally, which is exactly the bias that produces bad tightening
notes. Both structural cuts this method has proposed so far were wrong, and wrong in the same
direction. Check the length profile before writing the footer.

**Chapter skeletons are built from the beat drafts, not before them.** `*_skeleton.md` is a
derived artifact, assembled bottom-up from the drafts once a book has a full set of them — never a
top-down outline the drafts are then made to match. It is the last document in the chain and the
first one to go quietly wrong, because nothing downstream of it complains when it drifts. **When a
beat draft changes, the skeleton entry for that chapter changes with it.**

**Character sheets:** stack first, then function, then guardrails. The guardrails are the point —
they are what stops a character from drifting between books.

### Which document holds what — author's ruling, 2026-08-14

**Beat drafts record story beats, not characterization. Outlines record structure and placement.
Sheets record who someone is and how to write them.** If you find yourself writing characterization
into a beat draft or an outline, that is not a stylistic wobble — **it is the signal that the
character needs a sheet of his own**, and the fix is to make one and move it.

**Who gets a sheet is decided by whether the characterization matters, not by how many books
someone appears in.** Unnamed walk-ons never do. Characters who exist to fill a role usually do
not. **Anyone whose characterization is important enough to crystallize — or important enough that
the planning documents have started enforcing it — does.** A character in one scene can need a
sheet if the scene depends on knowing him; a character in eight books needs none if he is only ever
furniture.

**The distinction is originating versus referencing, and only one of them is the leak.** A beat
draft *citing* an established stack to justify why a beat must go a certain way is correct and
expected — that is what §3 means by using the framework to validate decisions. **The leak is a
planning document being the only place a character's characterization exists.** *(Swept
2026-08-14: nine planning documents across Books 1, 2, 3, 6 and 7 reference paradigm stacks, and
every one of them was referencing a sheet. Clean.)*

*This entry exists because `People/Bittek Sarn.md` was argued against twice on the grounds that
"sheets stop drift between books" and Sarn appears in one — which took the line above describing
what guardrails **do** and made it a rule about who **qualifies**. The outline then had to absorb a
stack, a psychology and five behavioural rules, and ended up containing the sentence "this is a
constraint on how to write his restraint, not a beat" — a line inside a document of beats,
announcing it was in the wrong file. **That sentence is the tell. Watch for it.***

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
                     sync_art.sh — moves images between the repo and Backblaze B2
Character Art/       UNTRACKED. Lives in B2; on disk here for the Viewer. See below.
Offstage.md                  canon that never got a scene — see below
Names.md                     the cast register — every named person, Books 1-8; check before coining
Story Timeline.md            in-series chronology (authoritative on timing)
Global Historical Timeline.md
The Seven Paradigms.md       the characterization framework
Series Review - Master List.md   editorial record and outstanding work
Series Review - Changelog.md     applied changes (append-only history)
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

**Raster images are not in git. They live in Backblaze B2 — author's ruling, 2026-08-05.**
The bucket is `haishuo-writing-images`, this project's prefix is `elvandar/`, and paths inside it
mirror the repository, so a restore is a straight copy back into the repo root. B2 file versioning
is on, which is what replaces the history git was providing.

```
./Tools/sync_art.sh status     what differs between local and B2 (default)
./Tools/sync_art.sh verify     compare every file by hash
./Tools/sync_art.sh push       upload  — DRY RUN unless you add --yes
./Tools/sync_art.sh pull       download — DRY RUN unless you add --yes
```

**The script is identical in every writing project and differs only in its `PREFIX` line.**
`Psion the Fraying` and `DnD Artificer Rework` carry the same file at their own roots. If you fix
something in it, fix it in all three — a script that has drifted between copies is the same class of
bug as a stale beat draft.

**The reasoning, so it is not relitigated.** Git stores meaning in text: a three-word edit to a beat
draft costs bytes and reads as three words. A PNG has no diffable interior, so git stores a whole new
multi-megabyte object and gives nothing back — you pay git's storage model and receive none of its
benefit. Before this change the images were **99% of the repository**: the entire textual history of
all eight books packs to 1.2 MB, and the images were 122 MB. **Art needs durability, not history**,
and that is a different problem with a different tool.

**The working copy stays on disk and that is deliberate.** The Viewer resolves inline embeds against
the document's own folder on the filesystem, so images render there exactly as before — `.gitignore`
is invisible to it. A **fresh clone has no images**; run `sync_art.sh pull --yes` after cloning.

**SVG is tracked and must stay tracked.** It is XML text, it diffs, all five in `Places/` total
115 KB, and `elvandar_map_v1.svg` plus `render_elvandar_map.py` are the sources
`elvandar_map_painted.png` is rendered from — which is why that 10 MB PNG is build output and had no
business being in git under any reading.

**One known casualty, accepted.** `Places/Kaha'an/Lathion_ Physical Layout and Geography.md` embeds
`Lathion - First Entry.png`. It renders correctly in the Viewer and shows a broken image on
github.com, because GitHub renders from the repository tree and cannot see your disk. **Do not
"fix" this by re-adding the PNG.**
