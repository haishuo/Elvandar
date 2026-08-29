# Series Review — Master List

The working editorial document for the series. Both books read in full: **Book 1** (ch1–25),
**Book 2** (ch1–20).

Organized by the rule hierarchy rather than by book, so the through-line is the structure of the
document rather than an afterthought in it.

Applied changes live in **`Series Review - Changelog.md`** — history, not work.

Both books also have a full set of beat drafts now — Book 1's twenty-five written retroactively from
the finished prose, plus `book1_chapter_skeleton.md`. Anything structural should be checked against
them before it is proposed against the prose.

---

## Status at a glance

| Tier | Outstanding | |
|---|---:|---|
| **Rule 1** — coherence | 0 | — |
| **Rule 2** — characterization | 0 | — |
| **Rule 3** — single-emotion integrity | 0 | — |
| **Craft — Book 1** | 0 | — |
| **Craft — Book 2** | 0 | — |
| **Book 3 — in draft** | 1 | Places-vs-map audit unfinished |
| **Book 6 — in draft** | 0 | — |
| **Open questions** | 0 | — |

**Nothing outstanding in either finished book.** Every item ever filed against Books 1 and 2 is closed,
withdrawn, or applied. Book 3 is live work rather than review findings — see [§3](#3-outstanding-work).

**Book 3 is 21 chapters as of 2026-08-04.** `Chapter 6 - Fair Price` was inserted between *Hubris* and
*Wonder* on 2026-08-03 to carry the return from Uratha and the purchase of a supply line into the Warrens,
shifting everything from *Wonder* down by one — *Wonder* is now **ch7**. Then `Inhabitants` and `Neighbours`
were split out of one 7,400-word chapter on 2026-08-04. **Prose exists for ch1–13**; beat drafts exist for
all twenty-one. Next prose is `Chapter 14 - Ruthless Calculus`. **Ch10 and ch11 were retitled on
2026-08-14** — `Bequest` and `Time`, replacing `The Repository` and `The Destiny Engine`.

**Before flagging anything here as outstanding, check the history.** This document has now produced
more stale entries than live ones. Eight of the original eleven Book 1 craft flags were stale — the
chapters had been rewritten and the flags never retired — and a further twelve entries turned out to
be already fixed, six caught by re-reading the prose and six more only found by searching commit
messages (`git log --all --grep="C-N"`) and grepping for the exact phrase an entry quotes. Reading
the chapter is not sufficient; an entry can describe a problem a later commit solved in a way the
entry never anticipated. **A flag that outlives its problem is worse than no flag**, because the next
reader trusts it and cuts good material — C-6 pointed at the best passage in ch25 and nearly got it
deleted.

**And the same rule now applies to design notes, not just to flags (2026-08-03).** The B1 ch2 beat draft
asserted that Xion's forgetting of Tam was deliberate and collected in ch12, *"when Tam's parents arrive
and he has to be reminded the boy exists at all."* **ch12 does not do that** — he recognises the name
immediately and the parents bring information rather than a rebuke. The payoff lived in the document
alone, and it was being used to defend a rule 2 fault against an author-raised complaint that was correct.
A note claiming a chapter pays something must be checked against that chapter's prose before it is allowed
to veto anything. This one survived a full retro-drafting pass, a rule-hierarchy audit and a stale-flag
purge without anyone opening ch12.

**Numbering note.** C-16 through C-21 as filed below are the local series. **C-22 through C-28 came
in from the cloud branch on 2026-07-29, where they were numbered C-16 through C-22**; both lines had
invented C-16 onward independently for different items. The mapping is in the changelog under the
merge entry, and the branch's own commit messages still use the old numbers.

**Where the work happens — author's ruling, 2026-08-04. There is one checkout and one branch.** Drafting
runs on `main` in `/Volumes/Archive/Documents/Writing/Elvandar`, and that is the only copy of the book on
disk. The author reads progress through **Elvandar Viewer**, which now lives in its own repository at
`/Volumes/Archive/Documents/Dev/elvandar-viewer` — it is a tool, not part of the series, and it was removed
from `Tools/` deliberately. `Tools/` holds `royalroad_export.py` and nothing else.

**The worktree is gone and is not to be recreated.** From 2026-08-03 to 2026-08-04 drafting ran in a
worktree on a `book3-prose` branch — first at `.claude/worktrees/book3-prose`, then relocated to a visible
sibling directory — and **the entire arrangement was a workaround for a problem that no longer exists**. The
Viewer could not display a path under `.claude` (`repository.py` carries it in `IGNORED_NAMES` and filters
every dotted name; Finder hides dot-directories too), so six commits were pushed somewhere the author's
reader is built never to show. The relocation outside the repo fixed the visibility and kept the real cost:
**a second full copy of the book on disk, which went stale within a day and was read as current** — no ch6
at all, *Wonder* still numbered ch6.

**A branch does the job a worktree was doing here, without the duplicate.** Nothing in this project needs two
checkouts live at once — one person drafts one chapter at a time, sequentially. When `book3-prose` was
finally removed as a worktree it was identical to `main` commit-for-commit, which is the plainest possible
statement that the second copy earned nothing. **`book3-prose` survives as an ordinary branch** and is
fast-forwarded to `main`. Branch and switch **in place**; do not check a branch out somewhere else.

**And the Viewer reads a branch without checking it out** — verified 2026-08-04 against the live repository.
Its branch selector lists *Working tree · main* plus *Committed · <branch>* for every branch, and selecting
one renders that branch's whole tree through Git objects: all nine Book 3 chapters listed, ch9 read at
14,945 characters, with no `git checkout` anywhere. That is the entire capability the worktree was invented
to provide. **Keep every branch fast-forwarded**, though — a branch left behind `main` shows the older book
when it is selected, which is the worktree's failure mode at a tenth of the price.

**One discipline survives, and it is the one that matters. Push after every commit** — fifteen commits once
sat unpushed through four rounds of revision while the author was giving notes on a chapter he could not
read.

**Sections:** [1. Rule hierarchy](#1-the-rule-hierarchy-authors-binding) · [2. Cross-book threads](#2-cross-book-threads) · [3. Outstanding work](#3-outstanding-work) · [4. Do not touch](#4-do-not-touch) · [5. Character guardrails](#5-character-guardrails) · [6. Settled rulings](#6-settled-rulings) · [7. Open questions](#7-open-questions) · [8. Observations that are not fixes](#8-observations-that-are-not-fixes)

---

## 1. The rule hierarchy (author's, binding)

When these conflict, the lower number wins. Everything else in this document is subordinate to them.

0. **Book 1 only — remember what the name of the book is.** The camera stays on Xion's shoulder. Not craft — the theme. Janice, Farleen, Elara and the rest exist through Xion's eyes and ears; the camera is *in* him or *on* him. **What Xion attends to is what the reader attends to**, and it bites hardest when he is working: B1 ch21 is the model, where the Mistress walks into the chamber and he never notices because he is treating Tam. Moving the camera off him is allowed but must be argued for, and the argument has to be about why *this* scene earns it in a book called *The Grain Merchant's Son* — establishing the whole book, or ending it on a cinematic pull-away. Inside the body of the book, assume the move is wrong ~99 times in 100.
1. **Things must make sense.** If something becomes logically incoherent, the plot changes to fix it.
2. **Characters must behave like themselves.** No adjusting a personality to make a point. *The plot serves at the sufferance of characterization, never the reverse.*
3. **A scene designed for one emotion stays that way** — wonder, joy, triumph, despair. Resolution may happen around the edges. It must never dilute.
4. **Thematic resonance ranks last.** Permitted only where it does not conflict with 1, 2, or 3.

**Reviewer's failure mode, recorded so it can be caught:** several suggestions this session reached for thematic shape and had to be paid for out of a higher rule — an invented watcher in B1 ch1 that contradicted ch4's premise (rule 1), a downbeat added to B1 ch25's closing roll call (rule 3), and a request that Rosik be given an interlocutor in B2 ch5 (rule 2 — Xion's silence there is in character, and Rosik encountering no resistance *is* Rosik). A fourth: the B2 clinic-sequencing "problem," raised as rule 1 incoherence, which was not one. The tell is consistent — adding something because it *rhymes*, or inflating a flag because it was predicted. "This would be more resonant" is a signal to check the three rules above it first.

### Craft principles (subordinate to the hierarchy)

- **A recurrence must change someone's position, not their volume.** B1 ch22 is the model: Elara reaches for the same weapon she used in ch15 and this time he breaks. B2 ch12 is the better model: Melina gives the same counsel a fourth time and he *agrees with her*, and is destroyed by agreeing.
- **Some scenes take one emotion, and hedging them is a loss.** B1 ch25 is triumph, full stop — the Jurassic Park reveal, not Malcolm at lunch. The contrast in adjacent chapters is what earns it.
- **Do not invent a payoff for something the text already paid off better nearby.**
- **State emotional content through action where the action already carries it.**
- **Never write an interval without checking the week number.** `Story Timeline.md` already says this in
  both directions; it is repeated here because it is the one craft rule that has been broken by drafting
  more than any other. **The specific failure is *"two years"* used as generic shorthand for *long enough
  to know someone well*** — five instances across B3 ch9–ch12, corrected 2026-08-08, one of which (*a
  house that had not written to the Valanar administration in two years*) described a silence longer than
  the administration had existed. **At B3 ch12 the whole saga is about twelve and a half months old.** The
  interval a character can truthfully reach for in late Book 3 is **a year**, and by ch21 *the better part
  of a year*. Anything longer is drafting reflex, not chronology. **Every error this check has ever found
  inflates** — nine across Books 1–3 on the 2026-08-08 audit, and not one ran short. That is the direction
  to suspect.
- **A beat draft's body is the page.** The numbered beats are what happens; instructions to the drafter go around them, never inside them. Full statement of the rule and its provenance in `Templates/Beat Draft Template.md`; the sweep that applied it across all 64 drafts is in the changelog under 2026-08-02.

---

## 2. Cross-book threads

These are the spine. Each is already working; each could be broken by an unwary revision.

**The hands.** B1 ch1 "The Healer's Hands" (tweezing glass, washing blood away) → B2 ch13 "Clean Hands" (*"he had just spent a night being him to the letter, and the proof was there at the ends of his own wrists, unmarked"*) → B2 ch17 (he takes his own pulse, finds it steady, and cannot make the diagnosis land on himself).

*(A fourth instance was written into B3 ch4's closing beat on 2026-08-02 — *"an interesting thing to feel in a room, at a table, with clean hands"* — and cleared here on the argument that it inverted the image rather than repeating it. **The whole closing beat was then cut the same day** as summary, and the fourth instance went with it. **Three remains the shape**, and the standing note stands: do not add a fourth without a reason written down here first.)*

**Frozen silence → chosen silence.** B1 ch1: rooted to the paving stones while Tam is taken, because acting means saying his own name. → B1 ch8: Elara asks him at the gate why he didn't, and *"nothing came out of it. The same nothing, arriving in the same order."* → B1 ch19: Farleen argues him down a maze in five stages and he answers none of them. → B2 ch16: he refuses Rosik the argument, and the text distinguishes the two explicitly. **This is the arc, and it spans two books.** Book 1 not closing it is correct.

**The Crown, and what Uratha does about it.** B3 ch9: the scholars stop asking *what does this say* and start
asking *is this important*, and Elara becomes **"a phenomenon they orbit rather than a colleague"** — planted
in a week when nobody is acting in bad faith. → B3 ch12: Uratha trades the Crown away believing it dead. →
**B3 ch13: it ignites on her head**, the delegation's shock is masked in seconds, and the century-old excuse
that the artifact was malfunctioning dies in front of the whole court. → **B4–B7: they do not try to get it
back**, because it is still dead for them and always would be; they reinterpret it as **Valanar blood**,
which turns a verdict into a research problem, and the research subject is Elara. Quiet the whole way —
access requests, papers taking her as their subject, an institutional wish to have her where she can be
observed, and nothing a Balishan character could point at. → **B8: the Globehall**, and the reader should
arrive already knowing what this institution does to a mind it finds interesting. **The thread is the study,
not the object.** Full ruling in `Places/Uratha/Uratha_ The Land of Scholars.md`, "What ch13 does to them."

**The empty Grain chair.** B2 ch16–19: Rosik exiled, the cartel broken, Melina Kemvimore dead. → **B3 ch1,
already written and doing the whole job**: *"The first was Grain. There was no one to send… the thing that
had made those parts into a cartel had been a single man's attention, and that attention was somewhere east
of the border and not coming back. **Someone would eventually sit there. Xion had opinions about who. He
kept them.**"* → B6: nobody ever did sit there, the market will not haul bulk grain down to customers with
no money, and the Warrens are in famine. **The plant is that sentence**, and it is a plant precisely because
it sounds like a loose end being tidied rather than a fuse being lit.

*Xion keeping his opinions is the first of the two refusals that leave the chair empty for good; **Melina's
is the second**, twenty years on, and she inherits hers from him — see her sheet and* How Kaha'an eats, and
the empty chair *below.*

**Do not add a second Grain beat to Book 3.** Checked chapter by chapter on 2026-08-04: the back half is
treaty (ch12), ceremony (ch13), the love triangle (ch15–16), Kalden (ch18), Terinok (ch19) and the
threshold (ch21), whose beat draft states outright that its job is *"to receive that weight rather than
generate new weight."* There is nowhere to put it that does not damage a chapter, and a second instance in
the same book would be volume rather than movement. **The escalation is in Book 5** *(applied 2026-08-04)*,
in the post-war reconstruction material and not in a scene of its own: the war was fought by severing
supply corridors, so reclamation gets funded as **food security** out of the war ministry's reasoning, and
the chair nobody filled stops being untidiness and becomes exposure — a state strangled once, with no one
coordinating its capital's food. **The choice made there is the correct one and it is why Book 6 happens**:
offered the immediate fix (refill the chair, restore a guaranteed flow) and the structural one (grow our
own and never be strangled again), Balisha takes the structural fix, which is right, and is generational,
and feeds nobody this winter. They pick the fix that solves it forever over the one that solves it now,
for people who have no vote and are not in the room. **The word *Warrens* is never said in Book 5, and
nobody notices the trade.**

**The Warrens chair.** B1 ch1: Xion frozen while Tam is taken. → B3 ch1: he asks that the council's first
sitting be about the Warrens, *"because there was a chair in this room that nobody was sitting in and it
was going to stay empty until somebody went down there and asked."* → B3 ch3: deferred, and nobody argues,
because *the Warrens will keep.* → **B3 ch6: he goes down and asks, and the chair is granted as the price
of a right of way** — the one thing he said it must never be. **Book 4 inherits a seated Warrens that was
seated for the wrong reason**, and nothing in Book 3 tells him so. Do not let a character deliver that
verdict to his face; it is the same failure mode as telling him he became his father (see [§6](#6-settled-rulings)).

**The Warrens seat, and what it does to Book 6 — OPEN, needs the author's ruling.** B3 ch6 does not give
Ronas a handshake. It puts a standing council seat **into a written instrument of the crown**, in the same
clause as four months of passage, minuted, on the schedule, non-lapsing. **That paper still exists in Book
6**, twenty years later, and it changes the Ronas confrontation at its root.

*Recorded here because `book6_outline.md` currently contains no version of this beat at all.* The author
recalls one — Ronas protesting *you can't just move sixty thousand people*, invoking a deal with Elara,
and Melina answering that she is not her mother and he never had a deal with **her** — and it is not in
the Book 6 outline, the series outline, `Offstage.md`, or this document. It was a conversation that never
got written down. **The version below is a proposal, not a ruling.**

**Why the remembered version no longer works.** *You never had a deal with me* repudiates a written
instrument of the crown, and that is the one thing this dynasty is careful never to do — B3 ch13's whole
cold open turns on Elara being treaty-clean, which is what keeps her from being the war's aggressor. It is
also **off-stack for Melina**, who is Truth Seeker primary and Engineer second: she does not dismiss a
document, she reads it correctly.

**The version the instrument actually produces is colder and better.** Melina does not deny the seat. She
reads what it is a seat *for*. **It is the Warrens' chair** — Xion's own framing on the page, *"the Warrens
had entered the government of Balisha as a term of sale"* — and she is not breaking the agreement, she is
**dissolving the party to it.** Empty the Warrens and there is no constituency, and no seat, and no deal
broken. Legal, precise, and exactly what a book called *Necessary Measures* is for. Ronas's *you can't just
move sixty thousand people* stops being a moral appeal and becomes the accurate observation that she is
about to abolish his standing rather than revoke it.

**And it detonates B3 ch6's closing line in his daughter's mouth.** Xion walks out of the Iron Hall
understanding that *the way to be governed by Balisha was to be holding something Balisha wanted.* Twenty
years later Melina supplies the corollary he never said: **stop holding it and you stop being governed —
you get moved.** He is alive to hear it. **Nobody explains this to him and he does not say it aloud**; the
same rule as the father verdict applies, and for the same reason.

**Two open questions the author should settle before Book 6 drafts.**
1. **Did Ronas ever sit in the chair?** The strongest answer is yes, for twenty years, losing every vote —
   the exact shape of his Coterie seat, a second lifetime of holding a position that never wins. It also
   means the council watched him age.
2. **Whose seat is it — the Warrens' or the Slavers'?** B3 ch6 leaves this genuinely ambiguous: Xion
   thinks *the Warrens*, Ronas takes it as *his*. **That ambiguity is an asset and should be resolved on
   the page in Book 6, not retrofitted into Book 3**, because it is precisely what the succession contest
   Melina plans for would fight over.

**The test, for any silence not yet written.** Put the best available defence to him and see whether he takes it.

| Silence | Defence | He says |
|---|---|---|
| Mira, at fifteen — B1 ch22 | terrified of his father, and it would have changed nothing | *"I didn't even try."* |
| Tam, in the square — B1 ch1 | speaking ends Master Fen and eight years of work | *"I nearly said them."* — and then, B1 ch11: *"I still don't know whether I decided or whether I couldn't move."* |
| Tam, on the cot the same night — B1 ch1 | he did not know where they had taken the boy, and could not have found out | **he does not offer it.** The triage returns *no* and he never names the reason. See the constraint below. |
| Elara, at the gate — B1 ch8 | he still can't tell her what he is | *"I couldn't."* — and she answers *"You just did."* |
| Rosik's study — **B2** ch5 | Rosik feeds on arguments; it would move nothing | **he agrees** |
| The disinheritance — **B2** ch16 | the same | **he agrees** |

**A note on the quotations in this table, and in this document generally.** Two rows once carried
lines that **exist nowhere in the prose** — paraphrases of Xion's position written in quotation marks
and then cited as evidence. Both are corrected. **Every verbatim-style citation in this file has since
been checked against the chapters**; what remains unmatched is either a deliberate quotation of text
that was *removed* (recorded so it is not reintroduced) or a compression marked with an ellipsis or a
slash. **If you add a quotation here, grep it first.** The register is not exempt from the rule it
enforces on everything else.

**The ch1 cot beat is a hard constraint on this thread (added 2026-08-03).** He now attempts the rescue on
the page and fails, which is what makes the ch2 substitution legible instead of offstage. **The failure may
never resolve into a verdict about his name.** Any sentence of the form *the one thing that would have
worked was saying who I am* converts the freeze into an alibi, gives him an answer to Janice's
*"you couldn't say your own name out there"* — which must stay unanswerable — and pre-spends ch11. The
permitted maximum is what is on the page: *the true one had already been handed to him that evening, in a
market square, by his own body, standing still.* Outcome named, reason refused. **He also may not name
Mira there**; the reader has *"two words, that was all it had taken"* sixty lines earlier and does not need
help, and ch22's *"I didn't even try"* is the only place that parallel gets spoken.

**Both accepted silences are in Book 2, and both are protecting Xion himself.** That is the whole of the difference.

**Rejects the defence → frozen. Accepts it → chosen.** A wound does not take mitigation; only a decision can be defended. Applies to scenes that don't exist yet, which the two-example version of this thread could not do.

**"Chosen" does not mean "clean."** The Rosik silences are decisions, and he will argue for them — but see below: they rest on a wound he cannot see, which is why the test sorts them here rather than with the others.

**Why the same defence gets opposite verdicts.** *"It would have changed nothing"* is offered for Mira and rejected, and the identical argument is offered for Rosik and accepted. The difference is **who is being protected.** Every rejected silence had somebody else in the room. Both accepted ones have only him.

There are two reasons stacked in the Rosik silences, and they must not be collapsed into one:

1. **Tactical, and correct.** He has fought his father before and lost, repeatedly, and is not stupid enough to run the same play expecting a different outcome. B2 ch5 states it flat: *"Rosik did not lose arguments — he fed on them."*
2. **Moral, and the wound.** Even winning would benefit nobody but him. At fifteen he convicts himself for not speaking for Mira — but put him against that wall instead, and he would not hold anyone else's silence against them for a moment. **Everyone is owed someone to speak for them. Except him.**

The first reason is *true*, which is precisely what lets the second one hide behind it.

**This is the same trait as the ledger** ([below](#2-cross-book-threads)) — he pays in and never draws. Janice's gift and Elara's absolution are refused for the identical reason he will not argue on his own behalf: he does not count himself among the people owed anything. B1 ch11's *"he left it shut"* is the one exception in two books, which is why it carries the weight it does.

**Why he doesn't count himself** is in the Xion guardrail at [§5](#xion--the-mira-moment-b1-ch22-rewritten-2026-07-27), under *the verdict*. Note that the Rosik silences are **not an exemption he grants himself** — in his own accounting they are not the same act and never arise, because there was nobody else in the room.

**Not the cold, and not inherited — author's ruling.** B2 ch5 puts it on the page in the warm stretch, long before the cold arrives: accused in the study of turning Elara against the Coterie, Xion has the reply *"whole and sharp, sitting behind his teeth"* — and swallows it, because *"**Rosik did not lose arguments — he fed on them**, turned every true thing you set in front of him into more ground to stand on."* That is Xion's own twenty-three years of data, stated flat.

Note the **order** in that paragraph: he reasons his way to the decision, and *then* remembers *"Don't hand him the argument. Melina had known."* Her line arrives as corroboration, not instruction. She is an older sister worrying about her brother; he would have done it regardless.

**Do not write this silence as contamination, and do not write it as ambiguous.** Xion is not stupid. Knowing your opponent is not the same as becoming him.

**The name.** B1 ch1: he cannot say *"I am Xion Kemvimore"* to save Tam. → B1 ch8: he says it at a district gate to save himself a walk, and it works instantly — the guard never touches the ledger, while the man ahead of him is written down and turned away. Elara watches, and convicts him for it. → B1 ch11: the trade gets named — four words free the boy and end Master Fen in the same breath. → B2 ch3: he says it to save Sela, it works, and *"Master Fen could not get one cup past this man's ledger. Only the other one could do that."* The price of the outcome is the thing he was. **ch8's use must stay trivial.** The moment it costs him something there, B2 ch3 has nothing left to spend.

**Two words.** B1 ch1 *"Two words. That was all it had taken."* → B1 ch22 *"Execute her."* → B1 ch13 Janice's *"My choice"* (a decision imposed, then a decision reclaimed). The compression is the unit of measurement in this world.

**"Did it anyway."** B1 ch18 (treating Varris against Farleen's warning) → B2 ch1 (*"He went anyway. That, he was beginning to understand, was simply who he was"*) → B2 ch2 (*"He sent it anyway"*). The trait's signature phrasing.

**The Janice chair** — the ally with better information who says stop and is right. Janice (B1 ch1, ch13) → Farleen (B1 ch14–19) → Elara (B1 ch15, ch22) → **Melina (B2 ch1–12)**. Melina is the terminal form: he doesn't dismiss her counsel, he *incorporates* it, stakes the plan on Rosik's reasonableness, and is wrong, and being wrong kills her.

**His father's ledgers.** B1 ch5: Elara asks whether the arrangements exist on paper, and Xion answers *"On paper"* without thinking, because he has known which of the three rooms was shown to magistrates since he was nine and it has never once presented itself as a fact worth saying. She files it and doesn't follow up. → B2 ch12: *"he had understood that since he was old enough to notice which ledgers his father kept in which rooms"* → B2 ch13: six teams carry them out at once, and *"there was not one lawful thing his father could do about any of it."* The seed is a question Xion answers carelessly; the payoff is Xion using the answer roughly a year later. (Series timing: the whole saga so far measures in **months**, never years — B2 spans ~5 months, B3 opens weeks after it.)

**The ledger (the other one).** Everyone settles their account with Xion and states it — Korvin, the food vendor, Rykan's cousin (*"after this, we're even"*). His own never closes. Janice's B1 ch13 gift (*"You don't get to write it down"*) and Elara's B1 ch22 absolution are both things he cannot receive.

**One exception, and it is load-bearing.** B1 ch11: Elara offers **complicity, not credit** — *"I was accusing you of doing what I did"* — which does not touch his ledger, so he can take it, and does, by not arguing: *"he left it shut."* It is the only gift in two books he fails to refuse. That is what makes ch22's absolution worse rather than redundant: he managed it once, and after Tam he cannot. Do not let ch11's version read as forgiveness, and do not let anyone offer him credit there.

**Becoming Rosik, and the fault line.** B2 ch12–16: the operational picture assembles and the cold takes over — *"It did not feel like a decision… the part of him that read such pictures was the only part still fully awake."* → B2 ch18: he loads Melina's death as leverage on Sa Ko Ren, sees himself doing it, and says **"Don't."** → B2 ch20: the low wall, the engine with nothing left to burn, and *"the cold broke… the way a wall goes, which is from the inside."* He knows what he became. He arrives at it alone and mid-act. **The difference between him and his father is not capability — it is that he has a fault line.** Nobody says any of this aloud, ever.

**Rosik unmasked → Rosik at the servants' gate.** B1 ch10 (no mask at a masquerade, the room reorders around him) → B2 ch19 (the back gate, in the dark, in a plain carriage). Explicitly recalled in the ch19 text.

**Asking after Tam — three beats, and Elara's position moves in each (built 2026-08-03).** B1 ch2: Kael
predicts it before Xion can — *"you'll ask her about the boy" / "You will"* — and Xion tries *she might
know something* into a silence and folds it himself. → B1 ch5: he asks, and she refuses **on capability,
not willingness** — no name she can use out here, no writ, nobody who owes her anything — and closes it
with *"Ask me again when I'm somebody."* → B1 ch12: the parents supply *Warrens*, and she volunteers
before he can ask, with no run-up in front of it.

**Two things this thread protects.** The refusal in ch5 is **rule 1 load-bearing**: ch12's engine is that
he does not learn where the boy is until the parents say so, so any version in which Elara can help
destroys the second half of the book. And ch2's beat 9b is a promise to the reader — **cut it only
together with ch5's beat 11a, or the promise goes unpaid.** The whole run also keeps Tam live across the
six chapters (ch5→ch12) in which he is otherwise unmentioned.

**Nothing anywhere points at the rhyme**, and nothing may: a man who could not say his own name in a
market square is turned down by a woman who has not got one to say. Available to the reader, invisible to
both characters and to the narrator.

**Consent — "Can I have a look?"** B1 ch1 (asks a twelve-year-old's permission) → B1 ch19 (**first break**: carries a delirious Tam into Long Knife territory; the one person who cannot consent is the one endangered) → B2 ch3 (asks the child, *orders* the tally-man — both behaviors, correctly assigned, in one scene) → B2 ch11 (*"no one had said he could, and there was no one left in the room to say he couldn't"*). Watch this in Book 3: **the moment he stops asking is the moment the wound is driving him instead of the practice.**

**The take-over — one faculty engages, the world outside it goes dark.** *Author's observation,
verified against both books; it was already in the text and neither of us put it there on purpose.*

Xion's hallmark is not focus exactly. It is **a part of him taking over without consulting him**, and
the phrasing is nearly identical across four years of drafting: B1 ch1 *"He went in through the bodies
**without deciding to**"* → B1 ch18, healing, *"And then the other thing took over, the way it always
did, **before Xion had decided anything at all**"* → B2 ch16, the cold, *"**It did not feel like a
decision.** Decisions had a texture, a moment of weighing, and there was no weighing in this."*

Both versions narrow the world to a single channel. B2 ch16's *"the only part still fully awake"* is
the same sentence as B1 ch21, where the Mistress walks into the chamber and he never notices.

**Similar in shape, different in kind — and the text already insists on it**, B2 ch11: *"**Not the
healer's eye** — that one was Mira's… **The other sight. His father's**."* **What separates them is
what survives inside the tunnel.** Healing excludes the world but the *patient* is in it. The cold
excludes the world and what remains is a *picture* — B2 ch16, flatly: *"It was a lever. **In the
operational picture, everything was**."* Everything, including Melina, which is what ch18's *"Don't."*
is about.

**The break is the Mistress entrance at scale.** B2 ch20: the memory *"came from **an angle the cold
had never been made to guard**, because it had never been a threat, and so it came straight through."*
In ch21 that costs him a flush up the neck. In ch20 it costs him the ground he was standing on.

**Corollary — the freeze is the same machinery returning *no*.** B1 ch1: *"He stopped, and stayed
stopped, and it was the correct decision, and being correct did nothing for him at all."* The
assessment completes and the answer is *don't move*, which is worse. **This reading stays in the
notes.** Putting it on the page would hand him the structural alibi for his paralysis that
[§5](#5-character-guardrails) prohibits.

**"The other thing" — CLOSED, and the phrase is deliberately *not* reserved.** Take-over uses: B1 ch18
(the healer), B2 ch11 (Rosik's sight), B2 ch8 (**Kalden's**). Plain idiom: B2 ch4 ×2, ch9, ch10.
Reserving was rejected on three grounds — the Kalden instance is in B2 ch8, which is do-not-touch;
spending Book 2's first editorial changes on a phrase is bad economy; and the rhyme already exists at
the only two places it needs to, where ch11 draws the contrast explicitly. It is plain idiomatic
English and will keep wanting to appear across six more books. **Do not attempt to reserve it later.**
*Applied:* the ch1 instance was cut — introduced during review rather than authorial, the weakest of
the three (a habit, not a seizure of control), and a third statement of involuntariness in a chapter
that already had two.

**The Long Knives are waiting on Elara.** B1 ch21: the Mistress has guarded the brass door for
generations without knowing what it is, meets the first person in centuries who can make it respond,
and finds out Elara knows nothing. She lets one moment of disappointment show, closes, and issues a
standing invitation — *if you ever figure out what you are, find me* — with the explicit note that
**the Long Knives have waited this long and can wait longer.** Nothing in Book 1 collects it. It is
the oldest open question any faction in the series has, it is held by somebody who is neither ally nor
antagonist, and it is aimed at the one thing Elara cannot supply. Do not let a revision convert the
Mistress into a mentor, a patron, or an enemy; her whole position is that she is *waiting*.

**The waiting now has an author-facing origin, settled 2026-08-22.** At Hauren's sealing roughly two
thousand years ago, the Haureni commissioned a small trusted human custodial order to control the final
approach to the Brass Door. Surveillance, route control, hidden movement, and silent killing began as the
instruments of that charge. The original Late Open Halauri name, patron, reason, and knowledge of what
lay behind the Door were lost across two millennia; the mandate survived and the institution became the
Modern-Balishan-named **Long Knives**. The Mistress does **not** know the history. Her leverage theory is a
modern rationalization for the duty she inherited. The modern route map was rebuilt through deaths after
the founding route knowledge was lost—it is not a two-thousand-year-old chart—and Book 3's *the route is
the guild* remains untouched. `Offstage.md`, “The First Charge of the Long Knives,” is the single source.

**The wound in front of him — B1 ch22 planted, Book 7 collects.** *The authority for this book is `Book 7 - Last Debts/book7_outline.md`, which is detailed and predates all of this; everything below has been reconciled against it, and the one place it was overridden is flagged there in its own structural note.* *Planned, not written. Constraints only; the staging belongs to Book 7's beat drafts.*

In ch22 Xion says, at the top of his voice, that healers are not judges, that they do not decide who is worthy of care, that they treat the wound in front of them — **and he says it about Rosik**: *my father decided Mira didn't deserve to live. Two words and she was gone. So no — I won't make those judgments.* That is a plant, and the outline puts Rosik on the ground in front of him in Book 7, dying of an Arol Batae spear, having come there to kill him. Xion works on him. It is not forgiveness and it is not belief; it is the only thing he has ever been able to do with a body in front of him. **He fails.**

**He asks permission.** *Can I have a look?* — the eighth-book instance of a first-chapter habit, and the last test of the consent thread above. It also hands Rosik the choice Rosik never gave Mira, who went out of the east hall on two words with nobody's leave asked, and **no line of dialogue may decode any of that.**

**Rosik's failure to understand is an action, not a speech.** He does not consent and does not refuse, because he does not know what the question is. He gets no epiphany, no softening and no explanation of himself — that is the Rosik guardrail and it holds to the last page of him.

**The scene is not about the contrast, and this is the one way to ruin it.** The guardrail is explicit that the difference between the two men is *not capability and not virtue* but the fault line. A scene in which Xion is visibly noble and his father is too limited to see it is the moral framing this series has refused for seven books. **Nobody may praise him for it, in the moment or afterward.**

**Book 7's POV enforces that for free, and this is why the beat is possible at all.** Book 7 belongs to Tiberian and Melina — the outline declares the shift at Book 5 and Book 8 changes it again, so the next-generation trilogy carries it. **Xion has no interiority available in Book 7**, so the scene can only be witnessed. The reader never learns what he thought he was doing, and the question of whether he knew never arises.

**What it does to Tiberian, who is the reason to write it.** He reads it as confirmation of the thing he has believed since he was small — that his father always knows the right thing to do — and asks himself whether he could have done it, and concludes he does not know, and that this is what makes his father what he is. **He is wrong, and nobody corrects him.** The reader has read Book 1 and knows what Tiberian does not: this is not a moral achievement, it is a compulsion assembled at fifteen years old out of Mira and never once revised. **Tiberian is reading a wound as a virtue.** That misreading is the beat's whole value and it must not be resolved — no character explains it to him, and Xion least of all, since Xion has never been able to say it about himself.

**Melina sees a different thing, and hers is the sharper one.** Truth Seeker → Engineer: she watches a man do something with no weighing in it whatsoever, and she is the one whose Book 6 near-ruin was that endless analysis is its own cowardice. Same act, two children, two irreconcilable lessons — which is the family's fault line drawn in one image.

**The sequence, settled by the author 2026-07-30**, and reconciled against `Book 7 - Last Debts/book7_outline.md` on 2026-07-31. **Tiberian rides out and meets Kalden in the field, well clear of Kaha'an's walls** — not at the frontier, and not at the gates. He will not let a foreign mercenary force entrench on Balishan soil, and Rosik's model is built on exactly that: **the better part of a day with Tiberian, Kess Ashwood and a substantial Arol Batae contingent committed somewhere he is not.** **Rosik's plan was sound and it very nearly worked — do not write it as a miscalculation.** The loud doomed army was always a lure, and stopping it at the frontier is exactly what it was for: it puts the Crown Prince days away from his father. Rosik was **counting on Kalden to hold Tiberian for two hours**, which is not a wild assumption — Kalden did precisely that at Silaris. In that version Melina's dispatch reaches Tiberian *with a battle in progress*, and Tiberian very probably stays, because duty holds him where nothing else could.

**The mechanism, which Kalden never heard, and the geography that made it sound.** Erulius is east of Kaha'an across the Balishan Desert, and **the Golden Path is the only road** — leaving it is death, so Kalden's army cannot flank, feint or choose an approach. **Rosik never had to predict where Tiberian would go**; there was nowhere else for either of them to be. Two armies closing on one road meet about a hundred miles east of the city, and the engagement keeps Tiberian, Kess and the Arol Batae contingent committed there for what should be the better part of a day. **His estimate is empirical, not abstract:** Kalden and Tiberian have fought one campaign to its conclusion already and it occupied Tiberian for most of a day, and Rosik discounts for terrain but not for the opponent, because it is the same opponent. **The only observed result of *Kalden versus Tiberian* is measured in hours.** His sample size is one, and the variable that mattered was not in it — the Kalden of Silaris was years younger and considerably less ruined. That window puts Kaha'an on a war footing — **and a city on a war footing looks outward.** That was the window. Rosik burned what little of his network still existed in the capital to establish where Xion would be, went in on the old Long Knife tradecraft he had before he was ever a grain lord, and meant to take him inside the chaos.

**What defeated it was contingency, not error.** Kalden's accumulated medical ruin all came due at once and he died of a massive stroke **without swinging a sword**, and his mercenaries — loyal to coin and not to crown — dispersed the moment their client hit the ground, stripping his body of valuables on the way out. Nobody could have forecast that, least of all a man reasoning from Silaris. **The farce of Kalden's death is not evidence that Rosik was wrong.** A later pass reading that sequence will be tempted to treat the whole scheme as a botch; it was not. It was correct, and it was beaten by a heart.

**And he goes in blind, which is the whole tragedy of it.** He is inside Kaha'an with no network left — he burned all of it buying the model. **He has no way on earth to know Kalden is dead** — he knows only that the plan is in motion, so he continues. What he can read is the building: guard posture tightening, the corridor he expected to be thin no longer thin. His craft tells him conditions have worsened. **It does not and cannot tell him why**, and for all he knows this is a lull inside a campaign still running. He reads a bad hour. It is the end. He goes, because the network is spent and there is no second attempt to hold anything back for, and a spear finds a man who a day earlier would have walked past it unseen.

**He never learns any of it.** He dies not knowing that Kalden fell in minutes without drawing a sword, that the mercenaries looted the body, or that the crisis he was moving inside had been over for a day. **Rosik dies not understanding two separate things** — why the man he came to kill knelt down to save him, and why the plan he spent twenty years' craft on came apart. Nobody tells him either. *Do not give him a moment of realisation.*

Then, in order: **(1)** Melina, holding the city, gets a field report so fast and so clean it does not add up — Kalden dead in minutes, the mercenaries dispersing without a fight — and **orders patrols raised everywhere on the assumption that something else is happening that nobody has seen yet.** **(2)** Rosik turns a corner that should have been clear for another twenty minutes and takes an Arol Batae spear from a warrior who does not know his name. **(3)** It does not kill him outright and the guards do not want it to: they have an unidentified intruder who got through two perimeters, and **they want him alive to question**, so they carry him to the nearest man who can keep a body breathing. **(4)** Xion is brought that body, sees whose it is, asks permission and works. **(5)** Melina comes to see what her patrols caught, and finds her father trying to undo her own order. **(6)** Xion fails. **(7)** Tiberian arrives too late, and Melina briefs him.

**Melina's order is what kills Rosik, and she is in the room for the consequence.** This is her culmination and it was already designed: acting on partial intelligence before the data is complete, which is the lesson the Warrens cost her. **She is named for the aunt Rosik's own decisions killed**, and the loop closes with her call ending him. Do not move that to anybody else — and note that it also gives her presence at the treatment a reason better than proximity.

**POV: Melina for the death, Tiberian for the arrival.**

**Kalden does not know he is a diversion, and that is the point of him.** He believes this is his great glory. He believes **Rosik Kemvimore is the only man in Elvandar who truly understands him** — that a pincer of siege from without and subversion from within will take the city, and that he will finally have Xion Valanar kneeling and his destiny restored. Rosik knew from the first day that the attack was doomed and **never said so — and never said otherwise either.** He does not lie to Kalden at any point; the full pitch and its truth-values are at `Offstage.md`, "The Recruitment of Kalden Erulius." **Every claim he makes is true, and the deception is entirely in the order he makes them and in his declining to correct what Kalden infers.** When Kalden describes the city falling, Rosik neither agrees nor disagrees; he moves to the next practical question, and Kalden experiences that as confidence. **Do not write Rosik promising a glorious victory.** Silence where a correction belonged is the instrument, and it is the same one as the omission in the pitch — the craft is not lying, it is knowing which true thing to say and when to say nothing. Even if some part of Kalden suspects, his sheet is explicit that he cannot process a defeat except as persecution, so he never lets the suspicion finish forming.

**This is Rosik's own teaching applied to a person.** B2 ch12: *every structure has one member bearing more of the load than the rest; find it, pull it, and stand back while the weight does the work of falling.* Kalden's pride is that member. Rosik did not recruit an ally — he located a load-bearing vanity, pulled it, and stood back. **He never explains any of this to anyone, on the page or off it.**

**The wound is carried to him, and he does not go looking.** This is load-bearing. If Xion seeks Rosik out he has *intent*, and intent is the one thing that kills the scene — it converts a compulsion into a demonstration. The body arrives in front of him and the other thing takes over before he has decided anything, exactly as it has since B1 ch18. Someone else put the wound there. He only treats it.

**And this is what makes Tiberian consistent across both versions, which matters because a reader will otherwise call him impulsive.** He rides **because there is nothing left in the field to hold him** — the enemy is dead, the army has dissolved, there is no command left to exercise. Under the conditions Rosik designed for, with a battle still running, the same man stays. Same character, different facts. *A review proposal that he should hold position was rejected on characterization grounds; the rejection stands, and this is why it was the situation and not the man.*

**Tiberian rides alone, ahead of his column, and it accomplishes nothing.** He is Caretaker primary, he leads from the front, and there is no version of him that waits for an escort with that message in his hand. **He does not need to be different from his father for this to work — he needs to be the same.** It is the identical reflex Xion has run since Book 1, *he went anyway*, aimed at a different object and producing the same result: too late, and he would do it again tomorrow. So when he asks whether he could have done what his father did, he is not asking from outside; he has just spent the ride proving he has the same engine. What he is actually asking is whether he could have pointed it at **the man who came to kill his father** — and the answer is no, and that is why the beat reads as awe rather than distance. *A version in which Tiberian holds position and lets duty win was proposed during review and rejected: it was arc-shaped rather than character-shaped, and the plot serves at the sufferance of characterization, never the reverse.*

**Elara is in the room and does not intervene.** She tried to absolve Xion once, in B1 ch22, and watched it fail without understanding why; she is the one person present who knows exactly what she is looking at. **Nobody in that room explains it to anybody**, then or afterward.

**Rosik is their grandfather, and neither twin has ever met him** — he has been in exile since Book 3. Tiberian rides back not knowing whether his father is alive, and arrives to find him unhurt, a grandfather he never knew dead on the floor, and his father having spent those hours trying to save the man who came to murder him.

**What the twins know, and what nobody will ever tell them.** They know the name. Rosik is the shape their family is built around — grandfather, Lord of Grain, exiled, the man who disinherited their father — absorbed the way Melina Valanar absorbed her aunt's death, *"not as a wound but as a shape."* **So nobody explains the relation to anybody.** Melina names him in her account because a complete account names him, and the instant *Rosik Kemvimore* is in the room the relation is in the room. Her own sheet states the family's mechanism for exactly this: **the name is the speech.** Do not have a character gloss it.

**Tiberian does not know about Mira, and never will.** Xion does not volunteer it, in any book. **Elara will not repeat it** — she understands what it cost him to say it once, and she takes it to the grave; see her guardrail in [§5](#5-character-guardrails).

**Melina works it out.** Nobody tells her; she is Truth Seeker primary with a lifetime of mapping gaps, and **the evidence is the alias.** Her father spent eight years publicly calling himself *Master Fen*, and a daughter patient enough to ask whose name that was has a trail at the other end: Rosik executed a servant in front of witnesses, and B1 ch22 has Xion learning the details *"in pieces, from people who'd been standing in the room."* Some of them are alive twenty years later. The memorial was hidden in plain sight for two decades and one person read it.

**Cap what she gets, because the cap is doing work.** She can reconstruct an apothecary named Mira Fen, at the Kemvimore estate, executed by Rosik around the time her father was fifteen. She does **not** have the east hall, the two words, the flower and the note — and above all she does not know that **Xion was standing there and said nothing.** She knows there is a wound; she does not know its shape, and she knows that she doesn't. **Only Elara has the whole of it, because only Elara got it from him.** So Melina could not correct her brother even if she chose to.

**And she chooses not to.** She works out that this is private, that her father has never wanted it known, and she sits on it — **one of the few things she keeps from Tiberian**, who she otherwise tells everything. Nobody gave her a confidence to keep; she imposed one on herself about a thing she went and dug up. That is the whole of her character in one decision.

**Elara does not know that Melina knows.** Two women holding the same thing from opposite directions, neither acknowledging it to the other, and neither of them ever raises it.

**If Tiberian ever learned — and he will not — he would agree with her.** His father's past belongs to his father, who never volunteered it and was never asked, and that is how it was. **Do not stage this as a betrayal, do not build a discovery scene around it, and do not let any character treat Melina's silence as a failure of loyalty.** It is recorded so that a later pass knows the moral verdict without ever needing to dramatise it.

Three people hold pieces of it and none of them will ever speak, which has two consequences and both are load-bearing.

**Tiberian's misreading is permanent, not merely uncorrected.** He cannot read the act as a wound because nobody has ever told him there was one — so he is not being naive, he is **reasoning correctly from information his father curated by silence.** And there is no mechanism anywhere in the remaining books by which he could find out. He will carry Xion as a moral compass for the rest of his life, calibrated on a scene he is structurally incapable of reading. **Xion's refusal to explain himself is the thing that guarantees his son will misunderstand him admiringly, forever.**

**And Mira dies with them.** Elara has all of it and will not say it; Melina has half of it and will not say it; Xion has never said it unprompted in his life. **The reader holds more than any character except Elara**, and has since B1 ch22.

**The two sights.** Mira gave him the healer's eye; Rosik gave him the geometry. B2 ch11–12 has him partition them deliberately and use his father's on purpose for the first time (*"that one was Mira's… he would not drag it down into this"*). The inheritance is tracked, not blurred — keep it that way.

**How each man holds the faculty — and it is not the same, which is the whole comparison.** Xion carries two inherited sights and **Rosik has one.** There is no evidence anywhere that Rosik possesses anything resembling the healer's eye; his entire architecture is structural, and B2 ch12 has him teaching it as a method — *find the member bearing more of the load than the rest, pull it, and stand back.*

**Rosik deploys his. Xion's seize him.** That is the difference, and it is not a difference of degree. Rosik's geometry is an instrument he picks up: he waited twenty years, every move chosen, the technique articulable enough to hand to a child. Xion's faculties arrive without consulting him — B1 ch18, healing: *"the other thing took over, the way it always did, before Xion had decided anything at all."*

**And this is the horror of Book 2, stated precisely.** When Xion finally uses his father's sight on purpose, **it takes him over too** — B2 ch16: *"It did not feel like a decision. Decisions had a texture, a moment of weighing, and there was no weighing in this,"* and *"the part of him that read such pictures was the only part still fully awake."* He inherited the instrument and it turned out to work like his wound. **In the father it is a tool. In the son it is a possession.** The reason is that Xion's faculties sit downstream of a compulsion and Rosik's do not — Rosik has appetite, and appetite can wait twenty years.

**The fault line follows from exactly this, and is not a moral fact.** An instrument can be set down; a possession cannot. **Rosik never breaks because nothing has ever had hold of him.** Xion breaks in B2 ch20 — *"the way a wall goes, which is from the inside"* — because something always does. This is the mechanism under the ruling at [§6](#6-settled-rulings) that the difference between them is *not capability and not virtue*.

**And it is why Rosik cannot understand the Book 7 scene.** In his model a faculty is something you *use*, and using one on the man who came to kill you does not compute. **He has no category for being seized.** His incomprehension is therefore structural rather than moral — the concept is missing from his architecture, not beneath his notice. **Never stage it as a man too limited to recognise virtue.** He is missing a faculty, not a virtue, and that distinction is the difference between the scene working and the scene becoming the thing this series has refused for seven books.

**What boxed Rosik in, recorded 2026-07-31.** Source is the plan section of `Book 7 - Last Debts/book7_outline.md` — "The clock," "The problem he had to solve," "The lever," "Why Kalden, and why Kalden is free." Three constraints, and each of them closes off an easier version of the book. **Kess Ashwood is the real obstacle** — she tracks by scent, takes no orders, wants nothing, and cannot be bought or moved by any lever he owns, so the whole apparatus exists to carry her out of the city behind Tiberian, whom she follows. **He is out of money** — Xion took the shadow funds in Book 2, so he cannot buy an army, which is why the patsy has to be a man who needs agreeing with rather than paying. **And the Warrens are being emptied into the Green Cities**, which is why it is this year: his base and his information are a wasting asset, and there is no second attempt to preserve. **He never identifies the cause** — he experiences sources drying up and reads it as attrition, because nobody is doing anything to him and intention is the only thing he can read. Do not give him a line about it, and do not let another character draw the connection.

**The two antagonists die days apart in Book 7 and fail in inverse ways.** Recorded 2026-07-31; the note lives at the head of Act III in `Book 7 - Last Debts/book7_outline.md` ("The two deaths are opposites") and both sheets point at it. The constraint in one line: **Kalden had every advantage and squandered it; Rosik's plan was sound and lost to two things that had no intention in them to read** — an artery, and an analyst who moved before the data was in. **Do not write Rosik's failure as folly**, because the series' position is that the difference between him and his son was never capability, and Book 2 spends four chapters establishing it.

**The four unopened letters — planted B1 ch1, detonates B2 ch1–ch2.** Ch1's estate room contains nothing
Xion chose except a false-bottomed box of money *"and the letters. There were four of them on the table by
the window, in his sister's hand."* He opens none of them, and the text gives the reason rather than the
mystery: answering means deciding what to say about a life he cannot describe. **That is the only trace of
Melina in the whole of Book 1** — she is not named, does not appear, and is not referred to again, and all
three of those are deliberate.

**Why it stops there — author's ruling, 2026-08-07.** Putting Melina into Book 1 properly was considered and
declined. **An introduced sister creates an obligation Book 1 cannot pay:** after ch10 the book goes
underground and stays there — Warrens, Long Knives, Brass Door, the trial, the coronation — and she has no
natural place in any of it, so a named character established in ch1 and absent for twenty-four chapters
would be worse than no sister at all. **And B2 does not need the help**: its ch1 introduces her completely
in about fifteen lines, and the prose says so — *"the whole map of them in four exchanges."* Her death is
fifteen chapters after that, which is all the runway it needs. **Naming her in B1 ch1 would convert texture
into a promise. Leave her unnamed.**

**What it pays.** B2 ch1's *"You put far less in letters, for years"* stops being characterisation and
becomes a callback, and B2 ch2 — titled `Letters`, opening *"The letter he sent ran four pages. The letter
that came back ran four lines"* — becomes a **reversal**: the man who could not start one in Book 1 writes
four pages in Book 2, once he has nothing left to conceal. **Do not pay this off inside Book 1.** The seed
is Book 1's and the detonation is Book 2's, and the gap is the point.

**The Mistress's standing invitation — opened B1 ch21, answered B3 ch2, and still not paid.** She ends
the Book 1 scene with *"when you take the throne — and you will — if you ever figure out what you are,
find me. We should talk."* B3 ch2 is Elara arriving without the answer, and the Mistress trades anyway:
**whatever is behind the Brass Door, she hears it from Elara directly, before the court and before it is
written anywhere.** That promise is now load-bearing in two directions. It is why the Long Knives permit a
camp in the chamber they have guarded for generations, which is what ch6's expedition and ch9's exit both
sit on top of. And it is a debt with a due date: **the moment Hauren is opened, Elara owes her a briefing
ahead of her own court**. Do not let the ch6 wonder chapter carry the payment — that scene takes one
emotion.

**Where it is paid — settled 2026-08-06, and it nearly was dropped.** Ch11 triggers the promise twice in
forty seconds: the Engine answers the B1 ch21 question of *what she is*, and the Door is open and she knows
what is behind it. **Ch12's draft then had her at a table with Draskin at noon trading Hauren — the court
hearing it, and a treaty written down — with the Mistress unmentioned in the entire chapter.** As planned,
Elara would have broken her word on the page and no one in the book would have noticed. The fix is
**ch12 beats 1–2: the Mistress is received at dawn, ahead of everything**, told the truth and not a version
of it, and the payment is priced — it runs late, it keeps a head of state waiting, and Elara never explains
why to anybody. **Ch11 sets it up from Xion's side** in the Warrens crossing: he registers the account as
nine hours overdue, and understands that the Mistress will not send anyone, because waiting is the whole
message. **What she is not told is the part about Elara herself**, and she notices the hole and does not
reach into it — leave that where it is.

**The Mistress is Xion's grandmother — true, canon, and not a thread. Author's ruling, 2026-08-02.**
`Places/Kaha'an/The Long Knives_ Death Merchants of Kaha'an.md` records her as Rosik's mother, hidden from
all but a handful, and that stays. **What was wrong was treating it as a planted seed awaiting payment.**

**A fact can be true and load-bearing on nothing.** The author's framing, kept verbatim because it is the
general principle and not just this case: *write a novel about the life of FDR — was Teddy Roosevelt
related to him? Sure, and maybe it's fun trivia, but the novel works perfectly fine without mentioning
Teddy once. It can remain true and still be irrelevant to the story you are telling.*

**So this is not owed a payoff and no later book should feel obliged to find one.** The "never plant what
isn't paid" rule cuts the other way here — the correct fix was not to schedule a detonation but to stop
depositing. The one beat in B3 ch2 that read as a deposit (an unreadable look held a moment too long) has
been softened to what it always actually was: an old woman recognising the healer she met in her own
tunnels, who is now First Counselor to the Crown. Fully motivated on its face, with nothing underneath it
for a reader to be waiting on.

**Elara's "note it" — the Warrens are not governed and she knows it.** B3 ch2: Vesk buys eleven days of
Slaver-held shafts from a lieutenant who does not know or care that the crown has been writing to his
king, and Elara's whole response is to have it written down and put in front of her *"when there's time to
do something about it."* That is characterization working correctly — she does not solve it in a chapter
that belongs to the door — **but it is also a promise to the reader**, made on the same trip in which ch1's
empty Warrens chair is still empty. Ronas Dermir is unresolved from ch1 through ch19 as the skeleton
stands. **Either the crown reaches him, or somebody names the fact that it never did.** Silence is the one
option this thread does not have.

**Casting minor characters — a standing check, added on the author's ruling 2026-08-02.** The author flagged
that the invented minor cast of B3 ch1–4 had gone lopsided. **The raw count was 3 female to 6 male, so the
count was not the problem — the *slots* were.** Every minor character given interiority, expertise or a
beat of their own came out female (the Long Knives guide, the silent Tor'anar who goes still when the grant
lands, Engineer Adren Thulgrav, the Gunastran factor), while every male one was a functionary with no inner
life (the undersecretary, the surveyor, the quartermaster, the junior adviser). Storm-Marshal Ilareth was
the single exception. **A reader registers the characterized roles, not the headcount**, which is why it
read as *every NPC*.

**It compounds, because the senior canon cast is already female-weighted by design** — Elara, Sa Ko Ren,
Tania Larannas, Janice, Farleen, the Mistress, Melina, Kess, Ondra Kelgrav, Thalia Neth, Perrin Halmore,
Wilka Zarnstran. That is the series as built and none of it is in question. **What it means is that female
is not a neutral default for a new expert role; it is a thumb already on the scale.**

**The check, before writing any new minor character with a line of characterization:** list the last three
or four invented roles of comparable weight and see which way they lean. If the notable slots have been
running one way, cast the other. **Ruled 2026-08-02: the ch3 battle-mage and the ch4 factor are male**; the
guide and Thulgrav stay as written.

---

## 3. Outstanding work

Resolved items and their closing evidence live in [§6](#6-settled-rulings), so nothing below is finished.

### Rule 1 — coherence

**None outstanding.** Every continuity error found in Books 1 and 2 has been fixed (see the changelog).

**N-1 was opened and closed on 2026-08-21** — *Harkin Vess* against *Tarren Vesk*. Ruled not a problem by the
author the same day; see §6, **A name collision needs weight on both sides**. Do not re-raise it.

The last item closed here was not an error in the prose but an error in the sheets — B2 ch7's
*"Twenty-six years old and still the family's smile"*, briefly changed to thirty and then reverted,
because the prose was right and the sheet was wrong. **Melina's age is fixed by B2 ch7 and by nothing
else.** Full reasoning in the changelog.

### Rule 2 — characterization

**None outstanding.** R2-1 (B1 ch18's untreated child) was the last item and is closed — see [§6](#6-settled-rulings).

### Rule 3 — single-emotion integrity

**None outstanding.** B1 ch25's triumph is protected and two dilutions have been removed. B2's single-emotion chapters (ch15's dread→grief, ch20's break) are clean — ch15's opening hope is setup for the drop, not dilution.

### Craft — Book 1

**None outstanding.** C-21 was the last item and is applied — see [§6](#6-settled-rulings). C-3, C-17
and C-19 were closed by work that came in with the cloud-branch merge; C-16, C-18 and C-21 were fixed
on 2026-07-29.

### Craft — Book 2

**None outstanding, and empty for the first time.** C-12 through C-15 were re-verified and closed;
C-26, C-27 and C-28 were opened in their place and all three are applied — see
[§6](#6-settled-rulings).

### Book 3 — in draft

These are live work, not review findings against finished prose.

**B3-1 is closed** — the Hauren arc is written through ch13 and the three constraints it carried are
now a settled ruling; see [§6](#6-settled-rulings).

### Book 6 — in draft

**B6-1 is closed.** Both open questions were ruled on 2026-08-14 — see [§6](#6-settled-rulings). Book 6's
design work has nothing outstanding; `book6_outline.md` holds the structure and `People/Bittek.md` holds
the character.

**B3-2 — two threads inherited from `_WORKING_NOTES.md`, which was salvaged and deleted 2026-08-04.**

- **The Places-vs-map audit is unfinished.** All `Places/` files were being rewritten to match the
  canonical painted map (`Places/elvandar_map_painted.png`). The Erulian file is corrected — Erulius
  sits far southeast on the Azure Sea and does **not** border Vartonne. **The other nations were never
  checked**, and nothing else records that the job was left half-done.
- **Draskin's description in `Chapter 4 - Negotiations` may contradict `Hubris` and `The Scholar's
  Crown`.** Flagged when those chapters were drafted and never resolved. Check before Act III drafting
  reaches him.

### Languages — in development

**Generative priority — AUTHOR'S RULING, 2026-08-22.** Language creation now follows the same iterative
authority as canonical character art: build the artifact until the author approves it, then retrofit
canon to agree. History and culture constrain the speakers, contact routes, institutions, and registers;
the existing name corpus does **not** select the language's sounds, roots, grammar, or derivations.

**Protection ladder clarified by the author, 2026-08-22.** P0 now contains **Xion, Elara, Valanar,
Kemvimore, Rosik, Kaha'an,** and the complete institutional name **Arol Batae**. P0 compels accommodation:
the language history must reach these forms however much legitimate historical layering that requires.
P1 contains words present in chapter prose. They are nearly fixed and should survive whenever a natural
route exists, but they may change before the language is contorted around them. P2–P4 have no linguistic
design authority; they may be ignored during construction and should be replaced when their register is
wrong.

`Languages/Design Plates/Early Imperial Balishan - Plate 1.md` is the first clean generative proposal and
was **approved by the author on 2026-08-22**. It is now the canonical foundation for Early Imperial
Balishan. The earlier contact phonologies,
settlement derivations, imperial cluster, *fen/sar/len/sathen*, *dal/seldal*, *-annas*, and *Hadris* are
now candidates from a superseded reconstruction plate. None is grandfathered; each may return only by
winning on the merits of an approved language.

`Languages/Design Plates/Late Open Halauri - Plate 1.md` is now the **working, unapproved** proposal for
the final broadly surface-facing stage of living Open Halauri. It independently supplies metropolitan
SOV and taught contact SVO registers, case marking, institutional and place derivation, a seed lexicon,
formal claim-source clitics, and a first cognate pool aimed toward approved EIB. It derives P0 *Kaha'an*
from *kaha* “sovereign public authority” + narrow office-seat *-'an*, and P0 *Arol Batae* from *arol* “old”
+ *bata-e* “constituted guarding body.” The plate remains generally unapproved, but its roots ***lita***
“open; expose access” and ***rava*** “assembled civic community,” plus the compound ***Litarava***, are
canonical in the bounded province-name history through the approved Balishan realm/province plate. No
other form becomes canon merely through that bounded approval.
**Example notation is explicit as of 2026-08-22:** bold first lines are ordinary author-facing
romanization with affixes and clitics joined; italic second lines are morphological analysis, where `-`
marks an affix boundary and `=` marks a clitic. The native script and its spacing remain unbuilt.

`Languages/Design Plates/Late Open Halauri - Plate 2.md` is the **working, unapproved** productive test
for ***-'an***. The apostrophe writes an actual /ʔ/, and the construction is not ordinary possession:
genitive *-n* answers “whose?”, ordinary site *-eth* says work happens there, and *-'an* forms the
recognized locus where an institution is legally present and able to issue effective acts. The fresh
family was generated before returning to P0: **veda'an, esha'an, netha'an, ketha'an, vela'an, riena'an,
bata'an,** and **thuma'an**. *Kaha'an* is therefore the sovereign and historically surviving member of a
real construction, not the only word invented to justify itself. None of the new forms is canon until the
author approves the plate or a bounded part of it.

The construction also produces a historically useful near-collision: Late Open ***kahan doma***
/ˈka.han ˈdo.ma/ is “a building of the Crown,” with case suffix *-n*, while ***Kaha'an*** /ka.ˈha.ʔan/
is the complete noun “Royal Seat,” with derivational *-'an*. Human glottal loss makes the descendants easy
to confuse and permits later folk etymology, while the learned apostrophe preserves the older distinction.

**Urathan pronunciation — AUTHOR'S RULING, 2026-08-22.** Kaha'ani residents call their city
**kah-HAN**, /kaˈhan/; Urathans call it **kah-HAH-an**, /ka.ˈha.ʔan/, and characteristically enunciate the
hiatus and glottal stop. The Urathan form is not confined to formal citation: Collegiate renewal has made
the learned pronunciation the standard Urathan proper name inside otherwise ordinary speech. An Urathan
using **kah-HAN** is accommodating or code-switching toward the city. To Kaha'ani ears, the Urathan
default sounds book-taught and determined to pronounce the city's own name more correctly than its
inhabitants do—which is exactly the intended cultural effect.

**The name *Lathion* was an authorized replacement target — AUTHOR'S RULING, 2026-08-22.** It was not P0
and, despite appearing in Book 3 prose, received no P1 design deference. The Foundational city-name plate
generated the original name from the founding event, carried it through three millennia of native change,
and then through human surface transmission before the reader-facing replacement was approved. Verified
pre-migration blast radius: **zero occurrences in Book 1–2 prose; 33 occurrences across eight Book 3
chapter files; 124 across sixteen Book 3 beat drafts; 33 generated Book 3 HTML occurrences; 1,523 total
occurrences across 94 current repository files excluding `TGMS - OLD/`.**

`Languages/Design Plates/Foundational City Name - Plate 1.md` is the first working native-name plate. The
author's 2026-08-22 preference promotes ***Halauren*** (Late Open city endonym) and ***Halauri*** (native
people, language, and adjective) as the lead ancient suite, from Foundational *Halā-qur-ēna*, “Life Under
Shelter” or historically “the Refuge of the Living.” This permits the city to have begun as an actual
refuge while leaving what drove the elves underground deliberately unknown; no Halauri survive and no
surface account reaches the founding. Refuge does not predict the sealing three thousand years later.

`Languages/Design Plates/Halauren Name Transmission - Plate 1.md` separates that endonym from the modern
human name. `Languages/Design Plates/Surface Halauric Bridge - Plate 1.md` now tests the bridge on
forty-one unrelated cognates before applying it to the city-name. The resulting approved modern suite is
***Hauren***, **HOW-ren**, /ˈhau.rən/, for the city and ***Haureni***, **HOW-reh-nee**, /ˈhau.re.ni/, for
the people, language, and adjective. Native *Halauri* and learned *Halauren/Halaurena* remain distinct
historical forms. **The author approved the native name, full transmission, bridge, and modern suite on
2026-08-22.** *Lathion/Lathionese* are retired labels. The separate controlled migration conformed Book 3
prose, its beat drafts and skeleton, generated Royal Road HTML, and downstream current canon to
**Hauren/Haureni**; ancient native and author-facing linguistic contexts use **Halauri/Halauric**.

**Place-names are now derived as transmission histories, not one-step glosses.** `Languages/Toponymy and
Name Transmission.md` records the first naming community, original referent, source language, borrowing
and inheritance stages, regular sound changes, modern endonyms/exonyms, reader-facing translation, and
protection tier for each important place. A location may carry separate names for its landform,
settlement, imperial construction, transferable title, province, and modern state. The immediate plate
order is Old/Open Halauri; the Surface-Halauric bridge into approved EIB; modern Balishan/Kaha'ani and
Vartonnian; Terinoki; Urathan; Erulian; Gunastran; Silarian; and Frozen North languages only when needed.

`Languages/Design Plates/Modern Balishan - Plate 1.md` is the **working, unapproved** national and Kaha'ani
daughter-language proposal. It keeps the approved Early Imperial SVO, prepositional, particle-based frame;
retains **c** /ts/, **j** /dʒ/, and **ai/au/oi** in ordinary speech; and makes urban Kaha'ani distinct
through frequency-driven contraction, cliticization, and commercial ellipsis rather than reader-facing
eye-dialect. Its learned court channel remains socially and phonetically distinct. The independent
geographic test generates inherited and new vocabulary for the old fertile heartland, port infrastructure,
and post-Rending desert, then separates opaque pre-imperial names, **-ava** imperial foundations,
function/terrain compounds, locally compressed names, and transparent post-Rending names. The P0 suite
fits without a new ordinary phoneme or single-use grammar rule. No generated Modern Balishan form or map
replacement is canon until the author approves this plate or a bounded subsystem.
The post-generation comparison also exposes one real decision: the superseded reconstruction's proposed
respect title **sar** collides with canonical Early Imperial **sar** “seed.” Homophony is possible but is
not presumed merely to preserve the older coinage; the honorific must win a controlled test or change.

`Languages/Design Plates/Modern Balishan - Plate 2.md` is the **approved canonical lost-province suite**.
The Rending makes the corpus unusually free: none of the lost settlements is a navigable present-day
destination, and the former support labels had no chapter-prose footprint. The canonical settlements are
**Talrava, Gonmer, Yelava, Unava, Tirun, Feshber,** and **Durcai**. The canonical landmarks and works are
**Dunyelas** forest, **Dunkargar** fortress, **Limel Mar** Great Plain, **Gonmel Mar** Great Grainlands,
**Yeltal** river, **Yelpas** forest passage, **Unpel Dun** northern aqueduct, **Maulom** harbor basin, and
the **Maukaras** reef coast. **Dunyelas** replaces *Deepwood Forest* and **Dunkargar** replaces *Fort
Dinkarth* in current canon. `Places/Balisha/Pre-Rending Litrava.md` records how the settlements, farms,
water system, coast, and northern tariff bypass functioned as one country before the Rending removed every
node outside protected Kaha'an. This bounded approval canonizes only the geographic material required by
the suite; Modern Balishan Plate 1 remains otherwise working.

`Languages/Design Plates/Balishan Realm and Province Names - Plate 1.md` is the **approved canonical**
realm/province split. It generates western substrate ***bal***, an apportioned common share carrying an
obligation, and fossil territorial ***-isha*** before deriving pre-imperial Vartonne-country
***Balisha***, “share-country.” The country-name widens to Valan's polity, then remains attached to the
portable Crown and state after the capital transfer and Vartonne's secession. **The author revised the
eastern suite on 2026-08-27:** Late Open Halauri ***Litarava***, *lita + rava*, “the Community of the
Opening,” becomes human ***Litrava***, **LIT-rah-vah**, /ˈlit.ra.va/. It first names the recognized human
surface community around Hauren's opened access, then broadens into the country and province containing
Kaha'an. Litrava is the seventh province while Balisha remains the supra-provincial empire and later
successor state; approved territorial ***-an*** regularly gives ***Litravan*** /ˈlit.ra.van/. The Rending
destroys Litrava as a functioning country and explains why the state-name, but
not the province-name, remains ordinary modern geography. Supporting geography and the map are conformed;
chapter prose already used only generic references and did not change.

**Talrava remains canonical by authorial ruling, 2026-08-27.** Its resemblance to *Litrava* is a genuine
etymological family resemblance, not an accidental near-duplicate: contact-era *Litarava > Litrava* and
younger Early Imperial *Talarava > Talrava* independently preserve Halauri-derived *rava* “civic
community/city.” The former is an opaque country-name by Year 0; the latter is the transparent “river
city” inside it.

**Legacy note:** the remainder of this language subsection records the superseded reconstruction pass.
Its history and cultural findings remain useful; its linguistic “settled,” “binding,” and “passed” labels
have been overridden by the ruling above and carry no current authority.

**L-1 — culture-first reconstruction is open.** The language material now lives under `Languages/` and
begins with `Ethnolinguistic History.md`. The inherited naming guide remains authoritative for explicit
authorial rulings but its proposed family tree, phonological signatures and etymologies are working
hypotheses until culture and chronology support them.

**Urathan genealogy is settled:** it descends from Imperial Balishan, with at least 349 years of independent
development between secession in 695 BR and Book 1 in 1044 BR, plus an older period of differentiation as an
academy, city and province inside the empire. **Its scholarly register is deliberately re-Halaurized**, not
merely conservative: scholars revive old roots and coin new compounds in the prestige tongue because age
signals dignity, precision and institutional authority. `Languages/Urathan.md` holds the full register
model. Its first controlled contrasts are inherited root stress versus learned penultimate stress,
ordinary loss of /ʔ/ versus restoration in citation, SVO vernacular clauses versus cultivated verb-final
academic structures, and inherited vocabulary versus revived or newly coined Hieratic material. The exact
academy founding date and local population remain open, so Urathan is not yet assigned exclusively to the
Vartonnian or Kaha'ani daughter branch.

`Languages/Design Plates/Modern Urathan - Plate 1.md` is the **working, unapproved** full-language
proposal. It derives a brisk Imperial-Balishan vernacular beneath a deliberately archaizing Collegiate
register, then tests that machinery on Uratha's state intelligence and research-enforcement service. The
generated full title is *Vela Theraris, Rava Eshais va Koiathu Vedaris Kethae*, “The Constituted Commission
for Licensed Inquiry, Civic Order, and Extraordinary Mandates.” **Approved 2026-08-22:** the common
formal name is ***Vela Theraris*** and ordinary speech uses ***the Theraris***. The two-word form is a
complete service-name on the same terms as *Arol Batae* and *Kaha Batae*, not an incomplete clipping.
P3 *Ilhamori* and its unsupported “eternal flame” analysis are retired. This bounded approval does not
approve the remainder of Modern Urathan Plate 1.

`Languages/Design Plates/Modern Urathan - Plate 2.md` is the **working, unapproved** Tower-name test. It
treats the familiar English Tower names as reader-facing translations, distinguishes physical **durdom**
from institutional **Dur**, and generates the native common suite **Palmur Dur, Zhalkar Dur, Nirkar Dur,
Senkar Dur, Selkar Dur, Halkar Dur, Mosar Dur, Noskar Dur,** and **Nosyel Dur**. It also generates current Collegiate charter titles
and three secret registers: whispered **Nosyel Dur** “Ebony Tower,” technical **Limzhomor** “Globehall,”
and ledger euphemism **Koiathu Rienaeth** “Extraordinary Preservation Annex.” No generated Plate 2 form
is canon until the author judges the complete suite.

`Languages/Design Plates/Modern Urathan - Plate 3.md` is the **approved** Modern Urathan numeral system.
It preserves inherited **an, du, sei, kau > ko, pem,** and **des**, generates the remaining standardized
digits **nu, vek, zhu, tae, nor**, and builds every ordinary quantity from coefficient-before-rank
**des** “ten,” **hek** “hundred,” and **mir** “thousand.” Values are grouped in triads; ten thousand is
**des mir**, hundred thousand **hek mir**, and no separate ten-thousand rank exists. Large scales use
productive **kel** “count; measure”: **mir kel du** is 1,000² or one million, **mir kel sei** is 1,000³,
and the exponent can itself be any numeral. The plate also proposes **nu** as zero/gap, **koi** as decimal
point, **tir** for fractions, and inherited **=ya** for ordinals. **Approved 2026-08-22:** the full spoken
system and its reader-facing translation policy are canon; glyph shapes, measurement units, arithmetic
operators, currency subdivision, and regional counting systems remain open extensions.

**Vartonne's origin is settled:** the river settlement and its name predate the empire; Valan I Valanar's camp
absorbed it in 0 BR and founded the monumental concentric capital later histories mean by "the city." The
settlement/capital distinction also lets House Kemvimore's lineage predate the imperial city without
predating human settlement on the site. `Languages/Balishan.md` holds the foundation. **Valan I Valanar is
the founding emperor**, and the overview's former "several dynasties" are successive reigning branches of
House Valanar: cadet lines and marriages change the ruling branch without breaking the house's seven-century
continuity. The throne-name pool accumulates after Valan I rather than predating him.
The name itself is now derived in `Languages/Halauric Core Lexicon.md`: CON *vart* “confluence,
meeting-center” + borrowed LOL *onna* “established settlement” gives **“Settlement at the Confluence”**
and modern **VAR-ton**, /ˈvar.ton/. “Heart-place” is the legitimate poetic interpretation, not the narrow
gloss.
**There is no question to solve in the state and capital having different names:** Balisha is the realm;
Vartonne is a city; Kaha'an is the capital-title. What *Balisha* denoted before the empire is an eventual
etymology question, not a coherence gap.

**The founding coalition is settled at the institutional level.** Valan's following supplied command and
arbitration; Vartonne supplied river transport, agriculture, markets, and the first capital's daily base;
Marresonne supplied commercial networks, scribal practice, and transmitted Halauri learning. Valan won
Terinok's blades through demonstrated martial worth, but its cantons did not surrender the Warrior's Code,
internal command, or sovereignty. A later emperor's attempt to subordinate the Code broke that conditional
oath; Elara's Book 3 alliance restores the founding relation between worthy Valanar and equal cantons.
`Languages/Early Balishan Culture.md` holds the full cultural and linguistic consequences. The precise feat,
oath form, and Valan's pre-imperial origins remain later construction questions rather than continuity gaps.

**The 500 BR imperial hinge and population transfer are settled.** The move begins under the fiction of a
temporary or seasonal eastern court and becomes permanent across successive reigns. The imperial household,
Kaha Batae, resident envoys, portable government, maritime and foreign offices, ambitious noble branches,
financiers, clerks, artisans, servants, suppliers, and other people whose livelihoods depend on access
follow the throne to Marresonne. The court does not replace the port population. Their Imperial Balishan
enters local marriages, schools, offices, and workshops, and the city renamed *Kaha'an* becomes the social
center of a new coastal court koine.

**What stays is equally causal.** Vartonne retains the Hall of Records, land and grain machinery, old
courts, cathedral establishments, hereditary offices, estate administration, and most ordinary residents.
Its formal register preserves old legal syntax, role relics, and procedures because those forms continue to
authorize those institutions; spoken Vartonnian nevertheless keeps changing through western syncope and
final-vowel loss. Conservatism is institutional, not linguistic stasis.

**The first imperial daughter split is established.** Common Imperial Balishan retains its
Vartonnian-derived SVO and prepositional frame. Transferred Court Balishan admits coastal /s/ outcomes,
fuller weak vowels, harbor and commercial usage, and intensified Hieratic renewal beside western compact
forms already spread through the koine. Modern Balishan is the national/administrative descendant centered
on the surviving capital; Kaha'ani is its urban dialect and cultural adjective. The Rending produces rapid
dialect leveling among refugees, not a new language in twenty years. Vartonnian remains mutually
intelligible but diverges most sharply in archival, ceremonial, rural, and deliberately national speech.
`Languages/Imperial Balishan.md` is authoritative for the transfer and first correspondences.

**Balishan genealogy is settled:** Proto-Balishan and Imperial Balishan descend from human-nativized
Surface Halauric, rather than from an unrelated human language carrying only prestigious Halauri
loans. Living metropolitan Halauri develops through the sealed period into Terminal Halauri;
Hieratic Old Halauri continues as a conservative but historically changing human textual tradition;
Surface Halauric develops into the Vartonnian/Marresonnian continuum and the imperial koine. An older
human **Ancestral Continental** stratum survives as substrate in its sounds, constructions, names, and
vocabulary. Its independent branches are deliberately unassigned: Terinoki, Old Gunastran, and Erulian
will not be forced into one deep family before their peoples are built. `Languages/Language Families.md`
is authoritative for this relationship.

**Hauren's contact culture is settled at the language-facing level.** The Great Shaft, Arrival Halls, and
Diplomatic Quarter sustained routine diplomatic, mercantile, instructional, freight, visitor, and refugee
traffic. Crown officials, interpreters, teachers, copyists, merchants, technical instructors, apprentices,
and surface communities used a teachable contact register; growing human-to-human use turned it into
Surface-Halauric mother tongues without Halauri conquest. Hauren itself had broad functional civic
literacy but tiered access to advanced texts, one related script tradition with multiple hands and
technical extensions, and distinct household, civic, Crown, Athenaeum, Forge, Arcanum, and Repository
registers. The sealing ends contact while speech continues changing on both sides. `Languages/Halauri
Culture.md` is authoritative; the reason for the sealing remains canonically lost. Exact lifespan,
constitution, theology, household form, glyphs, and sealed-period sound changes remain construction
questions, not continuity gaps.

**The attested-form inventory is established.** `Languages/Attested Forms Register.md` separates forms
from proposed etymologies and assigns five change-cost tiers: protected/locked, prose-established,
load-bearing planned, supporting-canon, and disposable construction material. **Xion, Elara, Valanar,
Kemvimore, Rosik, Kaha'an, Balisha, and Balishan survive any reconstruction;** prose forms strongly govern
it; off-screen forms may change only after the relevant sound system demonstrates a real conflict.
Silaris is fully available for later replacement but not presently inconsistent. Uratha's off-screen
Latinate map names (*Lumina Vale, Empirica, Memorium, Agraria*) are the clearest future register audit.
The old naming guide's root glosses remain hypotheses, and the apostrophe is no longer treated as an
automatic family marker across unrelated Halauri-looking and Terinoki forms.

**The inventory exposed one continuity question rather than silently solving it:** the Vartonne dossier
names **Emperor Varellian IV** as the ruler who moved the court in 500 BR, but *Varellian* is absent from
the settled throne-name pool; the Silaris dossier also supplies **Tiberan II**, while Elara's father is
Tiberan IV. Both are now indexed in `Names.md` and the forms register. Determine whether the throne-name
pool is incomplete or whether either off-screen historical name should change before deriving royal
morphology.

**The first contact-era phonologies and ordered daughter changes are established.** `Languages/Late Open
Halauri.md` defines the teachable public register: five stable vowels, default penultimate stress, clear
hiatus, ordinary voiced and voiceless stops, **th** /θ/, **sh** /ʃ/, rare learned **x** /ɕ/, phonemic **'**
/ʔ/, and predominantly simple onsets. `Languages/Ancestral Continental.md` defines the minimal human
substrate profile: initial root stress, unstressed centralization and loss, broad clusters and codas,
disfavored hiatus, and no common /θ/, /ɕ/, or /ʔ/ contrasts. The interaction supplies a mechanism for
Surface-Halauric reduction and clusters without making it “bad Halauri.” `Languages/Early Surface
Halauric.md` orders that interaction, distinguishes coastal Marresonnian from western Vartonnian
outcomes, and explains how the later imperial koine can inherit from both. `Languages/Grammar
Foundations.md` now supplies the minimum structural history: Late Open has head-final noun phrases,
verb-final neutral civic clauses, final role marking, and productive linking vowels; Ancestral Continental
has the same modifier-before-head order but ordinary SVO clauses, prepositions, and direct compounds.
Early Surface keeps the shared noun-phrase order while shifting its ordinary clause frame and spatial
grammar toward the substrate. `Languages/Halauric Core Lexicon.md` passes the first lexical test: LOL
*on-* “dwell permanently” + result/place *-na* produces *onna* “established settlement,” whose coastal,
western, and documentary descendants yield **-onne**. CON *vart + onna* regularly produces *Vartonne*;
LOL *marreth* “sheltered deep-water sea-harbor” + *onna* regularly produces coastal *Marresonne* through
/θ/ > /s/ and vowel reduction. The earlier off-screen placeholder *Marrethonne* is retired because keeping
it would require a learned spelling exception for a form the story does not need to protect.
The second controlled test derives the imperial cluster: whole-title LOL *Kaha'an* through Hieratic
transmission; human learned *Kaha Batae* and post-Rending *Arol Batae*; and hybrid *Arol Rhutan*, whose
ordinary inherited head descends from LOL *re-hutan*. Exact grammatical exponents and almost all other
roots remain uncoined.

**The imperial transmission test also passes.** Existing western /t/, coastal /s/, and learned /θ/
channels; ordinary loss versus learned restoration of /ʔ/; root-initial inherited stress versus
penultimate learned stress; and ordinary hiatus repair versus careful retention survive the capital move
as social alternatives within one political language. No protected or prose-established form requires a
respelling.

**The first productive Imperial-Balishan morphology test passes.** Early Imperial polity-relational
***-an*** /an/ derives *Balishan* and *Urathan* from the realm stems, with regular *a + a* coalescence.
Marresonnian–Late Imperial settlement-relational ***-i*** /i/ derives city-local *Kaha'ani* from the whole
title; historical /ka.ˈha.ʔa.ni/ regularly yields native Kaha'ani /kaˈha.ni/. The semantic division is
now binding: *Balishan* and *Urathan* operate at polity,
people, and national-language scale; *Kaha'ani* names an inhabitant, urban cultural adjective, or the
capital's dialect/accent. One person can be both Balishan and Kaha'ani. LOL bound *-'an* inside *Kaha'an*
is a third, older morpheme meaning a governing seat. *Terinoki, Gunastran, Erulian, Marresonnian,* and
*Vartonnian* are not pulled into the system by visual resemblance. No name changes were required.

**The first ordinary Balishan lexical test passes.** CON ***fen*** /fen/, **FEN**, means “prepare plant
remedies; herbal medicine as skilled work.” Its stressed CVC form survives Surface-Halauric change
unchanged. Zero derivation supplies the activity, craft, and practitioner without a suffix; context and
the existing optional-number grammar distinguish “herb-work,” one *fen*, and multiple practitioners.
The word has no gender—“Mira the herb-woman” is an English explanation, not a feminine form.

The semantic boundary is binding: ***fen*** is herbal/apothecary work, not the general word for every
healer. Mira was both a *fen* and a healer; Xion learned *fen* from her and extended his practice into
wounds, infection, surgery, and broader care. Master Keelen demonstrates that an apothecary can use his
personal name rather than *Fen* as a compulsory title.

The three fixed story forms use the common noun differently. ***Mira Fen*** is personal name plus
occupational byname. ***Master Fen*** is native *sar Fen*, a respect title plus trade used as a complete
working identity—effectively “respected [the] Herb-worker”—which is why it is anonymous. ***Xion Fen*** is the crown
allowing a common trade noun to occupy the imperial house-name field. Capitalization reflects the
author-facing byname or title; it is not spoken morphology. None of the three creates a surname, house,
Fen lineage, or Fen cousin. `Languages/Halauric Core Lexicon.md` is authoritative.

**The first ordinary Balishan honorific test passes.** CON ***sar*** /sar/, **SAHR**, survives unchanged
as an invariant title placed before a personal name or occupational byname. It recognizes a socially
established adult or someone acting in a respected skilled capacity; it is not a guild grade, licence,
house name, or noble rank. English translates the same genderless form as *Master* or *Mistress*.

The four closed examples are native *sar Fen, sar Janice, sar Keelen,* and *sar Keya*: reader-facing
*Master Fen, Mistress Janice, Master Keelen,* and *Mistress Keya*. Keya is the controlling edge case—she
is Xion's older patient, not a practitioner—so the title marks ordinary adult respect rather than mastery
of a craft. Janice's bare *Fen* remains an intimate omission. Noble *young master*, cartel or corps
headship, mastery grades, and the Long Knives' unique *Mistress* are separate English senses and remain
uncoined in Balishan.

**The first ordinary Balishan medical-register test passes.** CON ***len*** /len/, **LEN**, means “treat or
mend a sick or injured living body” and zero-derives the practice and practitioner translated
*healing/healer*. It is broader than *fen*, does not promise a cure, and does not lexically contain Xion's
ethical rule that healers treat the wound in front of them. That rule belongs to his and Mira's vocation,
not to every speaker's dictionary.

CON practical-service site suffix ***-um*** /um/ reduces regularly to /əm/ in Surface Halauric. It gives
***lenum*** /ˈle.nəm/, **LEN-əm**, “clinic,” and ***fenum*** /ˈfe.nəm/, **FEN-əm**, “apothecary shop or
workroom.” The suffix classifies recurring organized work rather than architecture. Master Fen's back room
is a *lenum* while patients can be received there and merely a room when the practice ends; Mira is the
estate *fen*, while Keelen's apothecary as a place is his *fenum*.

Learned LOL ***sathen*** /ˈsa.θen/, **SAH-then**, combines *sath-* “diagnose a living body's internal
condition from signs” with specialist *-en*. It is the competence term translated *physician*, not a legal
licence or palace appointment. Xion is truthfully *fen, len,* and *sathen*. Mira and Keelen are securely
*fen* and *len* without the corpus requiring the learned title; palace physicians are institutionally
appointed *sathen*, with robes marking the appointment rather than creating the lexical category. The
forms overlap rather than making a rank ladder.

The native forms behind *medicine, surgeon, midwife, bonesetter, hospital,* and other specialties or
institutions remain uncoined. No specialist list follows automatically from this controlled cluster.

**The first Balishan household and chartered-House test passes.** CON ***dal*** /dal/, **DAHL**, names the
functioning household maintained under one continuing provision, roof, and domestic authority. It can
include blood kin, married-in members, wards, servants, and dependants; it names neither the building nor
nobility. LOL legal ***sel-*** /sel/ “enter or constitute in authoritative public record” precedes it in
mixed EIB ***seldal*** /ˈsel.dal/, **SEL-dahl**, the crown-recognized legal body translated as capitalized
***House***.

The system keeps five axes separate: biological blood, *seldal* membership, the second name carried in
records, heirship, and present office. Marriage instruments decide House entry for spouses and recognized
children; individual charters govern succession. There is no universal paternal, maternal, male, or
firstborn default. Rosik can marry into and later head Kemvimore; Xion can lose heirship before ceasing to
bear its name; he can later enter Valanar at marriage without changing his ancestry.

Fossil patronymic ***-annas*** /an.nas/ gives *Lar-annas*, “descendants or issue of Lar,” but is no longer
productive. House names share a legal slot rather than a noble suffix: opaque native *Kemvimore* and
***Hadris*** /ˈhad.ris/, neo-Halauri *Valanar*, purchased *Darfi*, foreign *Sa Ko Ren*, stolen *Dermir*,
exceptional *Fen*, and reader-translated *Greystone* reach it through different histories.

**Tobias Valorian is now Tobias Hadris.** *Valorian* falsely implied kinship with *Valanar* and worsened
the closed V-initial cluster. **Hadris**, **HAD-riss**, /ˈhad.ris/, is a compact, collision-free native
charter-name. The change is nominal only across B3 ch1, ch3, and ch4; Hadris's actions, House history,
politics, titles, and characterization are unchanged. Older changelog entries retain the former name as
historical records.

**Transparent English House names are translations, not phonological evidence.** *Greystone, Umberlow,
Ashworth, Blackmoor, Silverbrook, Thornwood, Whitmore, Fairwind,* and *Ironwood* may remain reader-facing
semantic renderings while their native sound-forms stay uncoined, exactly as *Long Knives* translates a
meaningful Modern Balishan name. Dossier-only opaque names remain provisional until their historical
language layer is demonstrated.

**The protected-form test passes without one-source flattening.** *Kaha'an, Balisha, Hauren, Elara,
Valanar, Melina, Ilareth, Ormuth, Tor'anar,* and *Arol Batae* fit direct, Hieratic, or neo-Halauri sound
shapes; *Rosik* and *Kemvimore* can be substrate or mixed; *Vartonne* and *Marresonne* now have controlled
mixed and inherited-coastal derivations; other national forms remain outside the family. Written
**Xion** fits Late Open /ɕ/, but its ordinary Modern Balishan initial is
now fixed by authorial ruling as **ZY-on**, /ˈzaɪ.ən/. It follows a learned Marresonnian–Hieratic chain:
/ˈɕi.on/ > /ˈzi.on/ > [ˈziː.on] > /ˈziː.ən/ > /ˈzaɪ.ən/. The conservative spelling and modern pronunciation
therefore reinforce rather than contradict one another; no clipped longer form is required.

**The confirmed imperial cluster is fully derived.** LOL *kaha* means sovereignty as an office, and bound
*-'an* is the seat in which authority is instantiated. Their lexicalized title *Kaha'an*, **“Royal Seat”**
or literally “Seat of Sovereignty,” passed whole through the Hieratic tradition; the Valanar court made it
transferable. Native Kaha'ani pronunciation is **kah-HAN**, /kaˈhan/: ordinary glottal loss and vowel
contraction made the two-syllable form categorical enough to function as a local shibboleth, reinforced
by residents' constant use of the city-name. Historical **kah-HAH-an**, /ka.ˈha.ʔan/, survives in fixed
coronation language, Hieratic citation, standard Urathan usage after Collegiate renewal, and some foreign
reading traditions. In ordinary city conversation it sounds book-taught and can identify an outsider. The same
distribution gives native *Kaha'ani* /kaˈha.ni/ beside instructed historical /ka.ˈha.ʔa.ni/. The spelling
remains *Kaha'an*; *Ka'han* is only a pronunciation aid.

*Batae* is learned LOL *bat-ae*, **“appointed guard; commissioned guarding body.”** Human imperial *Kaha
Batae*, **“Imperial Guard,”** therefore combines two learned elements. After the Rending the survivors
deliberately substitute learned *arol*—“old, long-established, or belonging to the former order”—to become
*Arol Batae*, the **Old Guard**. The name is not a Modern Balishan translation: it is a solemn replacement
inside the old title, changing the authority above the same institutional head. Careful pronunciations are
**KAH-hah bah-TAH-eh**, /ˈka.ha ba.ˈta.e/, and **AH-rol bah-TAH-eh**, /ˈa.rol ba.ˈta.e/.

*Arol Rhutan*, the **Old Tunnels**, is deliberately not the same route. It combines learned *arol* with
ordinary inherited *rhutan*, **ROO-tən**, /ˈru.tən/, a lexical collective regularly descended from LOL
*re-hutan*, “interconnected tunnel system.” The count noun *hutan* means one tunnel; prefix-vowel loss and
/r + h/ coalescence explain historical **rh**. The whole phrase is **AH-rol ROO-tən**, /ˈa.rol ˈru.tən/.
Post-sealing, pre-imperial Marresonnian record-keepers formed the phrase; the empire later retained it.
This makes it a surface-registry hybrid, not the builders' own name. *Batae* is number-neutral through its
duty-holder/body derivation; *rhutan* is collective by derivation. Neither is a plural suffix. All four
formations preserve modifier-before-head order without flattening learned and inherited speech into one
register. `Languages/Halauric Core Lexicon.md` is authoritative for the derivations.

---

## 4. Do not touch

- **B1 ch18** — *"Did it anyway."*
- **B1 ch20** — the mirror throw, *"Lot of good it does him."*
- **B1 ch22** — the Mira confession.
- **B1 ch25** — the triumph.
- **B2 ch8** — the Kalden interlude. Best single chapter in the series.
- **B2 ch15** — Melina's death. Structurally exact.
- **B2 ch20** — the bench. The wordless ending is correct; do not add the stated callback.

---

## 5. Character guardrails

### Xion — the Mira moment (B1 ch22, rewritten 2026-07-27)

**He was there. He got there in time. He said nothing.** The canonical sequence:

1. At fifteen he sneaks out for a rare flower Mira had mentioned; a rainstorm catches him near the
   Warrens; he slips, hits his head, and is knocked unconscious.
2. Mira guesses where he went, braves the storm, and carries him home.
3. Rosik is waiting. He demands an explanation and **she gives him one** — the lessons, the forbidden
   knowledge, all of it. Xion is unconscious for this and learns it afterward, in pieces, from people
   who were in the room.
4. Before dawn Mira comes to his room, pries the flower out of his fist, sets it on his bedside table,
   and leaves a note: *For my best student.* **She knows what is coming.**
5. He wakes, reads it, understands, and runs barefoot through the house looking for his father.
6. **He arrives in time.** Rosik is in the east hall with Mira and two of his men, and he *waits until
   his son is through the door* before saying it. Two words. *"Execute her."*
7. Then Rosik looks at him — not anger, which Xion had seen before, but the look of a man who has
   finished deciding something and is watching to see whether anyone will be stupid enough to reopen
   it. Xion understands it in half a second.
8. He says nothing. They carry her out past him, **and he steps out of the way so they can.**

**The wound is cowardice, and that is the whole point.** Not failure to save her — he concedes himself
that nothing would have changed Rosik's mind. The charge he convicts himself on is that he was given
the one chance he would spend his life claiming he wanted, and fear closed his mouth: *"But I didn't
even **try**. There's a word for what that is."* A failure to save can be reasoned away as impossible.
A failure of nerve cannot, because the proof it was available is that he was standing right there with
the words in his mouth. He was also fifteen and afraid of a genuinely frightening man — a defense he
has never once allowed himself.

**What this earns.** Xion quotes his father's exact two words; under any version where he is absent he
has no way to have heard them. It also makes ch22's *"I watched what happens when someone plays judge
over who deserves care and who deserves death"* literal rather than figurative. And it sets the rhyme
the series runs on: **frozen silence → chosen silence.** B1 ch1, rooted to the paving stones while Tam
is taken. B2 ch16, the same hall-silence in front of the same man, chosen this time and named as
different in the text. Both are silences in front of Rosik; only one is a failure.

**Keep the slippage in his vow at the grave.** What he failed to do was *speak*; what he swears is that
he will never again fail to *act*. He converts a failure of nerve into a failure of duty and spends his
adult life discharging it in the wrong currency — which is why the compulsion is *I must not hesitate*
rather than *I must help*, and why the one move his wound forbids is the pause that would have saved
Melina.

**The verdict, and why he will not revise it.** What he carries is not vague low self-worth. It is a
*finding*, assembled from evidence and reviewed and upheld: **I froze when it mattered most, and I kept
freezing at the critical moments afterward. I can produce every excuse in the world. In the end that
only proves what I really am.** It is a horribly unfair thing to conclude about himself, and he
concludes it anyway. Three things follow, and all three are load-bearing.

**It compounds.** Each later silence is entered as further proof, so the instances in the silence thread
above are not repetitions — they accumulate, and every one is worse *for him* than the last, regardless
of what was actually at stake.

**The rule is narrow, and absolute inside its bounds:** *somebody else needed me to speak and I didn't.*
No defence is admissible against it. **The Rosik silences are not an exemption from that rule** — they
are not the same act, so in his own accounting they never come up at all. There was nobody else in the
room. He is right about that, and writing it as special pleading makes him inconsistent, which he is not.

**And he sees the excuses.** He can state each one in full — he does exactly that before rejecting it,
and says outright that he could produce every excuse in the world. **Do not write him as a man blind to
the argument.** He is not persuadable, which is a different thing and a worse one.

**And the verdict is doing work for him** — this part is a reading, but it holds everything else
together. If cowardice is simply what he is, then eight years of Master Fen is restitution and the whole
architecture stands up. Absolution would take the foundation out from under it. That is why Elara's
B1 ch22 offer **cannot** land rather than merely does not, and why Janice's ch13 gift has to be refused.
He is not being modest. He is defending the reason he gets up in the morning.

**Nobody tells him any of this**, ever — the same rule as the Rosik comparison in
[§6](#6-settled-rulings). It is his to reach, alone, or not at all.

**Superseded:** an earlier reading had him unconscious for the order and Mira dead before he woke
(commit `1f5e53d`, and a guardrail here). That was a defensible reading of the old ch22, but it left the
two-word quote unsourced and made the guilt merely a failure to protest a fait accompli. Do not restore
it. If a document says he *"woke to find her already gone"* or *"was unconscious when the execution
happened,"* it predates this revision.

### Janice

- **She never says "Xion" or "Kemvimore."** Her knowledge lives only in what she declines to ask (*"I've never asked where the money comes from"*).
- **Mira gives him the practice; Janice gives him the cover.** Values from one, tradecraft from the other.
- **Janice did not name him. She told him he needed a name.** The distinction is the relationship. Her instruction was *"You can't keep that name. Not if you want to keep doing this"* — a systems correction, delivered by a patient to her healer before she owed him anything. The word itself is Xion's, and it is Mira's: *"Fen. Master Fen."* Her answer is only *"Welcome, Master Fen."* So she **authored the security and witnessed the christening**, and that is why "Fen" in her mouth is not a nickname — it is the name she was present for, still in use eight years later, while she has never once said the other one aloud. B1 ch23 originally called her *"the woman who had given him his name"*, which collapses the two halves and hands Mira's gift to Janice; corrected 2026-07-27. If it recurs, the fix is not to re-attribute the name but to say what she actually gave him — the room, the years, and the questions she declined to ask.
- **Janice never absolves him.** She stays operational permanently. Comfort about Mira would be doing Mira's work and deflates both characters.
- **ch13's "My choice" is a gift, not a claim of authority and not noble sacrifice.** Xion's *"I can't let you do that"* must read as guilt (*whatever happens to you becomes mine to carry*), never permission-granting. Her answer closes the copper argument by conceding it: *"I'm giving you something. You don't get to write it down."*
- **Her sight is fine — author's ruling, 2026-07-29. VETOED and removed from the series.** The failing-sight thread was doing too little narrative work for what it cost. **Do not reintroduce it in any book.** What the first injury was is deliberately unspecified and must stay that way, and **Xion cured it**. See [§6](#6-settled-rulings).
- **She is the purest instance in the series of help with no ledger under it.** He cured her and she owed him nothing; her first act toward him was to hand back the correction that made his whole life possible. Two people fixed each other inside a week and neither opened an account — which is exactly the thing Xion cannot understand, and exactly what she is still refusing to become eight years later.
- **Confirmed: she is alive.** See [§6](#6-settled-rulings) for the return plan.
- **The shop never burns, in any book.** Only the six journals do, on her own counter, in B1 ch13. The building is the clinic's front half; Book 2 lives in it for nine chapters and B3 ch11 has it standing, shuttered, and impounded. Ruled 2026-08-01, but the ruling was applied only to Book 3 and B1 ch23's prose still said *"It burned … before the water crews got there"* until **2026-08-06**. What she loses is **the shop as hers, not the shop as a structure** — taken for eleven days over records that no longer existed, and never allowed back. If the phrasing recurs, the tell is a water crew, a neighbouring building, or the word *fire* attached to anything but paper.

### Farleen — green eyes, honey-blonde hair (author's ruling, 2026-08-03)

**Locked.** She had green eyes and honey-blonde hair in the author's conception from the beginning. An
early draft changed them to amber to imply a hidden blood relationship with the Mistress of the Long
Knives — a mystery with no answer behind it, invented rather than requested. That entire line is in
`TGMS - OLD/` and is non-canon, so the colouring has no remaining function.

**The eye colour must never acquire a plot function again.** If a future draft reaches for Farleen's
colouring as a clue or a link to another character, that is the same error coming back. She is
green-eyed because she is, and it means nothing.

**Do not let her eyes rhyme with Elara's.** Elara's cycle blue → amber → violet, involuntarily and
rationed; Farleen's are green and static. The text may not invite the comparison, and the Mistress has
no stated eye colour anywhere in current canon — checked — so nothing is left to reconnect them.

*Applied across seven prose instances (B1 ch3, ch13 ×2, ch14 ×2, ch16 ×2, ch25; B2 ch2), three beat
drafts (B1 ch13, B1 ch16, B3 ch20 and ch21) and `People/Farleen Darfi.md`. The single hair reference in
the prose is B1 ch13.*

### No chess metaphors — in the sheets as well as the prose

The prose rule was already in place and the prose is clean. **The sheets are now held to it too**, because
the sheets are where the temptation originates: Xion's sheet described Rosik as an *"unflappable chess
master"* twice and had him *"recognizing checkmate and conceding with dignity,"* which is precisely the
image a drafting pass would reach for and then have to be told not to use.

**A correction on the in-world question, because the obvious argument is wrong.** Chess *does* exist in
Elvandar — `Places/Uratha/The Physical Geography of Uratha.md` gives Uratha's academy "The Game Courts —
for strategic board games like chess." So the objection is not anachronism, and anyone who reaches for
that reason is arguing from an assumption rather than the worldbuilding.

The real objections are two. **Register:** chess is Urathan academy culture, not Balishan. Kaha'an runs
on ledgers, water rights, granaries and load-bearing walls; a Kaha'an narrator reaching for a Uratha
scholar's pastime to explain a grain lord is borrowing the wrong nation's vocabulary. (If a *Urathan*
character ever thinks in board games, that is characterization and entirely fair.) **Craft:** it is the
lazy default for "clever strategist," and this series already has a far better idiom of its own,
established in B2 ch12 and belonging to Rosik specifically — *every structure has one member bearing
more of the load than the rest; find it, pull it, and stand back while the weight does the work of
falling.* Use that. It is his own teaching, it is what Xion turns against him, and it carries the
architecture imagery the whole book already runs on.

**Fixed:** `Xion Kemvimore.md` ×3 (both "chess master" instances and the checkmate line);
`Elara Valanar.md` ("political pawn" → *a claim for other men to spend*).

**Deliberately left:** *endgame*, *stalemate*, *gambit*. These are dead metaphors in English — nobody
reads a board off them — and they appear in authorial framing rather than in any character's mouth. The
line is **live chess imagery applied to a person**, not chess etymology.

### Rosik

- **The Rosik charge is deferred through Book 1 and fires in Book 2.** He must read as innocent of tyranny in B1 ch13; *"I have turned into my father"* is the worst realization available to Xion and belongs to B2's arc.
- **B2 ch16's tell is lethality only.** No Long Knives, no guild, no Mistress — that is Book 7's to spend. Keep it a flicker Xion cannot name.
- **Rosik encountering no effective resistance is the point of Rosik.** Do not manufacture an interlocutor for him.

### Melina

- **She is right about the world she knows, and the world she knows stops existing.** *"Father can be reached. He always can."* Her death must not read as naivety — she is the most accurate reader of Rosik alive, and Xion agrees with her, and they are both wrong.
- **The meeting interval must vary and never become a fixed weekly ritual.** Currently: "day after tomorrow," "next week," "tomorrow," "three days," "two days," off-rhythm. A schedule would telegraph the death.

---

## 6. Settled rulings

Decided. Retained so they are not reopened or re-flagged.

### A name collision needs weight on both sides — author's ruling, 2026-08-21

**Two axes, not one, and the register only had the first one written down.** `Names.md` clears *Lyra / Lira*
on **co-occurrence** — *"they never share a book, a scene or a sentence."* That test is necessary and it is
not sufficient, because it says nothing about how often either name is actually said.

**The second axis is weight.** ***Vrek → Draskin* was a real problem** because the Scholar-King of Uratha and
the commander of the Arol Batae are both major supporting characters who recur across multiple books and are
spoken aloud constantly. ***Vess* against *Vesk* is not**, and was closed the day it was raised: **Harkin
Vess exists in one clause of one chapter of one book** — B1 ch10, where Xion names two masked guests for
Elara — and appears in no beat draft, skeleton, outline or sheet. *Sera Quillin*, named in the same sentence,
is the same. **A character who gets a few lines in one chapter does not get renamed to protect a name nobody
will carry out of the room.**

**Both are in `Names.md` now anyway**, which is the actual remedy: they were missing from the register
entirely, so the risk was never that a reader would confuse Vess with Vesk — it was that someone would later
coin *Harkin Vess* a second time, for somebody else. The register exists to stop duplicates, and a walk-on
occupying a row costs nothing.

**Applying this:** before flagging a near-collision, count the mentions on the *quieter* side. One scene and
no downstream documents means it is furniture, and furniture does not collide.

### A second name is a grant — commoners have one name — author's ruling, 2026-08-21

**`Languages/Languages of Elvandar.md` → *Who Gets a Second Name* is authoritative.** In Balisha a house name is
conferred by a throne; nobles carry one and **commoners carry a single name**. Read the rule there before
coining anyone, and read `Names.md` beside it as always.

**It is a Balishan custom, not a law of the world.** Erulian retainers and commoners are Erulian in both
halves and keep theirs; Gunastran, Uratha, Terinok, the Far East and bakarn Silaris keep their own customs —
*Perrin Halmore* is a bakarn dockworker and keeps her name. **Clan names are a different category** and
*Ashwood* is one, so Kess is unaffected. **Bought houses are still houses:** Farleen is a noblewoman of a
house her father bought, and that is the rule illustrating itself rather than an exception to it.

**The books were already doing this** — every commoner in `Names.md` already went by one name, and the file
had argued the point for Garrin a week earlier without noticing it was a rule. Three exceptions existed and
all three are resolved: **Tam** and **Arlo** lost their surnames (four prose lines, all Book 1), **Bittek**
lost his before a word of Book 6 was written, and **Ronas Dermir** keeps *Dermir* because he took it, the
same act as taking *Slaver King* and the earlier of the two.

**The load-bearing half is *Fen*, and it is not a surname.** It is the common word for herb-work — *Mira Fen*
is *Mira the herb-woman*, and *Master Fen* was always a job rather than a name. **No prose changed for it**;
two existing lines simply became literal (B1 ch18's *"Got yourself a name off it"*, B3 ch1's undersecretary
spelling *"F, e, n"*), and B3 ch1 is now a man asking the crown to enter a common noun where a house name
goes. **Consequences that bind:** *Fen* is not a family and never can be; and Melina's route to Mira runs
through people rather than records, because a trade-word cannot be looked up.

Full application in the changelog, 2026-08-21.

### Physical canon lives in one visual continuity ledger — author's ruling, 2026-08-20

`People/Basic Physical Characteristics.md` is the single source for recurring visual facts: reference age,
height, build, hair, eyes, complexion, identifying marks, and explicitly approved inheritance decisions.
Individual sheets and prose remain the evidence beneath it; old art is not allowed to fill an unspecified
field by accident. The ledger marks author rulings, textual facts, sheet-only statements, and genuinely
unset traits separately.

**Biome is not ancestry — author's ruling, 2026-08-22.** Character art must not infer complexion or ethnic
register from a location's present-day biome. Kaha'an became a desert only in the Rending, approximately
twenty years before Book 1; old Kaha'ani and Balishan court culture defaults visually toward a classical
Mediterranean, Italian/Roman register unless a stronger source says otherwise. Explicit prose, beat drafts,
character sheets and this ledger, approved family/reference models, and direct authorial instruction govern
in that order. Family resemblance and fixed complexion outrank environmental associations. An unspecified
trait must be chosen consciously rather than supplied silently by a desert stereotype.

**The calibration system is fixed, and its first six numerical heights are now canon.** Each technical
plate uses the same armorer's fitting frame, floor line, camera, lens, subject distance, neutral posture, and
flat-soled footwear. The written height remains authoritative over apparent image scale. Identity portraits
and narrative scenes stay separate from these deliberately plain measurement plates.

**Author's ruling, 2026-08-20:** Xion and Elara are each 5′11″ / 180 cm; Farleen is 5′7″ / 170 cm; Rosik is
6′1″ / 185 cm in Book 1; at sixteen, Tiberian is 5′10″ / 178 cm and Melina Valanar is 5′8″ / 173 cm. Sa Ko
Ren remains textually tall without an exact number. Adolescent measurements attach to age and are not
silently carried into adulthood.

**Elara complexion correction, 2026-08-21:** Elara's untanned natural complexion is light warm ivory/beige
with a faint olive undertone. Mainline Elara's outdoor martial training gives her a modest tan comparable
to the visible Leah reference that originally served as her direct visual conception. Leah's own outdoors-oriented
Verbena life means she is not an indoor baseline: the court-sheltered Imperial Princess AU should be fairer
than visible Leah and nearly as fair as Farleen, though fractionally warmer rather than pink or porcelain.
The substantially darker complexion in the first photorealistic model was
never supported by prose or sheet canon and appears to have been an over-reading of present-day Kaha'an as
a desert culture, despite the desert being only twenty years old. This is a complexion correction, not a
facial recast. Farleen remains slightly lighter than Elara. Corrected solo and 5′11″ calibration candidates
were approved and promoted on 2026-08-21; the previous darker versions remain archived under `Character
Art/Drafts/Elara Valanar/Complexion Correction/Superseded/`. The corrected `Xion, Elara and Farleen` group
reference was approved and promoted on 2026-08-21; its darker predecessor is preserved with the other
superseded Elara assets. The corrected `Xion and Elara` two-person reference, rebuilt from both 5′11″
calibration plates to protect their equal baseline and scale, was approved and promoted on 2026-08-21; its
darker predecessor is preserved alongside the others. The corrected `Formal Dance Practice` and `The
Vartonnian Envoy` scenes were approved and promoted on 2026-08-21, with their darker predecessors
preserved. The corrected preferred Imperial Princess AU portrait was approved and promoted on 2026-08-21;
its darker predecessor remains archived. The corrected `Expecting the Twins` scene was approved and promoted
on 2026-08-22, with its darker predecessor archived. The older direct-translation Imperial Princess
photorealistic remake was retired into the superseded archive rather than complexion-corrected; the
calibration-derived portrait is now the sole active photorealistic AU interpretation. Tiberian's and Melina Valanar's
previous models inherited the old visual drift and are no longer complexion authorities. Their corrected
solo portraits were approved and promoted on 2026-08-21: both use a light warm beige/olive inherited from
the approved parent models, with Tiberian modestly more sun-touched through martial training and Melina
closer to the parents' sheltered baseline. Their previous darker portraits remain archived. The paired
reference and height-calibration plates still require propagation of this approved ruling.

The corrected individual height-calibration plates were approved and promoted on 2026-08-21, preserving
Tiberian's 5′10″ and Melina's 5′8″ baselines; their darker predecessors remain archived. The first corrected
paired-reference candidate was rejected because it retained too much of the superseded bronze coloring,
especially on Melina, despite preserving the established two-inch difference. It remains archived as a
rejected attempt; the approved paired reference has not yet been replaced.

The stronger second-pass paired reference was approved and promoted on 2026-08-21. It brings both twins
into the same apparent range as the approved solos and height plates, with Melina subtly lighter than
Tiberian, while retaining the original paired composition and two-inch height difference. The former darker
pair remains archived. The twins' complexion correction is now fully propagated across their canonical
solo, paired, and height-calibration references.

The Elara complexion pass is closed across the active photorealistic archive: canonical solo and height
references, group references, formal dance, Vartonnian envoy, pregnancy scene, preferred Imperial Princess
AU portrait, and the twins' descendant reference suite all carry the approved ruling. Remaining darker
assets are explicitly superseded, rejected, retired, or illustrated rather than active photorealistic canon.

**Xion and Melina Kemvimore complexion ruling, 2026-08-22:** Rosik establishes the intended Kemvimore
family complexion register: light warm olive and classical Mediterranean/Italian-Roman, capable of reading
comparatively fair under indoor light. Melina shares that sheltered baseline, fractionally warmer only
through youth. Xion shares the same natural baseline and carries at most a faint additional warmth from
spending more time moving through the city. Neither is deeply tanned or bronze. Their first photorealistic
models repeated the same unsupported post-Rending desert drift corrected in Elara and Silvanno. The revised
solo portraits were approved and promoted on 2026-08-22, with their darker predecessors archived under
their respective complexion-correction draft folders. Corrected 5′11″ Xion and 5′8″ Melina calibration
plates were approved and promoted on 2026-08-22, preserving the existing heel lines, crown positions, and
written measurements; their darker predecessors are archived. Corrected two- and three-person group
references were approved and promoted on 2026-08-22, preserving the fixed 5′11″ / 5′11″ / 5′7″ relative
scale and the already-corrected Elara and Farleen complexions. Corrected versions of the three active
Xion-and-Elara scenes were approved and promoted on 2026-08-22: `Formal Dance Practice`, `The Vartonnian
Envoy`, and `Expecting the Twins`. Their darker-Xion predecessors remain archived as superseded. The
Kemvimore complexion correction is now fully propagated across Xion's active solo, height-calibration,
group-reference, and canonical-scene suite, and across Melina Kemvimore's active solo and height plate.

**Janice correction and visual ruling, 2026-08-20:** Book 3 explicitly makes Janice sixty-one; the old
ledger and sheet claims that her age was unset were stale. Her rejected failing-sight concept is purged from
the remaining sheet analysis: her sight is normal. Her approved identity design is compact, sturdy, and
vigorous, with a strong slightly square face, prominent cheekbones, a firm mouth, dark hair substantially
iron-grey in a plain braided coil, clear hazel eyes, a medium olive complexion, and capable work-worn
artisan's hands.

**Janice height ruling, 2026-08-20:** Janice stands **5′4″ / 163 cm**. Her identity portrait and technical
plate are archived separately under `Character Art/Reference Models/Photorealistic/` and
`Character Art/Reference Models/Height Calibration/`; the plate uses the common armorer's fitting frame,
flat shoes, heel baseline, and neutral posture.

**Tania Larannas visual ruling, 2026-08-21:** Tania is forty-seven in Book 1 and stands **5′6″ / 168
cm**. She has a medium, softly curvy build; deep chestnut hair beginning to silver subtly at the temples;
grey-green eyes; and a light-medium warm olive complexion. Her mature oval face has high cheekbones, a
straight nose, fine lines around the eyes, and a full but exceptionally controlled mouth; she has no scars.
Her authority is social and presentational rather than physically intimidating. The photorealistic model is
developed independently from the earlier illustration, which remains historical design material rather than
a likeness source. Her approved identity portrait and technical 5′6″ plate are archived separately under
`Character Art/Reference Models/Photorealistic/` and `Character Art/Reference Models/Height Calibration/`.

**Silvanno Larannas visual ruling, 2026-08-22; height fixed 2026-08-27:** Silvanno is twenty-three in Book 1 and stands **5′11″ / 180 cm**, lean and trim, with a
young oval face, high cheekbones, a straight nose, deep chestnut wavy hair, grey-green eyes, and a
light-medium warm olive complexion closely matching his mother Tania's. He is clean-shaven and has no
distinctive scars. His approved register is classical Mediterranean — a young Italian/Roman nobleman —
rather than a complexion inferred from Kaha'an's post-Rending desert. Dignified, practical teal court
clothing carries his Water-cartel identity without suppressing the easy confidence and kinetic physicality
established in prose. The first, substantially darker portrait is rejected and archived; the corrected
approved identity portrait is archived at `Character Art/Reference Models/Photorealistic/Silvanno Larannas.png`,
and his approved technical plate at `Character Art/Reference Models/Height Calibration/Silvanno Larannas.png`.

**Danshall Harkim visual ruling, 2026-08-27:** Danshall is in his mid-twenties at Book 4's opening and
stands **5′9″ / 175 cm**. He is lean-to-average with slightly narrow shoulders and is not physically
imposing. His approved identity fixes fair neutral freckled skin, short practical sandy-brown hair,
grey-blue eyes, substantial straight brows, and a broad softly rectangular face with modest cheekbones,
a slightly wide asymmetric nose, and a firm unsculpted jaw. He is clean-shaven and has no scars. His
amber-gold Topaz robe bears the single thin silver cuff band of a junior scholar and remains functional
rather than elegant. The active identity portrait is archived at
`Character Art/Reference Models/Photorealistic/Danshall Harkim.png`; his approved technical fitting-frame
plate is archived at `Character Art/Reference Models/Height Calibration/Danshall Harkim.png`. Its retained
construction record includes the white-background source, transparent cutout and raw deterministic
5′9″ composite under `Character Art/Drafts/Danshall Harkim/Height Calibration/`.

**Lira Harkim visual ruling, 2026-08-27:** Lira is four years younger than Danshall, approximately twenty
or twenty-one at Book 4's opening, and stands **5′5″ / 165 cm**. She has a slight-to-average unathletic build.
Her approved identity makes the sibling relationship legible through the Harkim family's fair freckled skin,
sandy-brown colouring, grey-blue eyes, substantial straight brows, broad facial foundation, modest cheekbones,
and slightly wide asymmetric nose, while giving Lira her own softer jaw, rounder cheeks, smaller chin, and
distinct mouth and eye spacing. Her straight shoulder-length hair is simply cut; plain well-mended civilian
clothing carries no Tower colour or rank marks. Her active portrait depicts her defining Book 4 introduction:
calmly packing in the modest apartment before Danshall arrives, already prepared because she memorized the
evacuation route. The earlier laboratory-like candidate is rejected for incorrectly translating Danshall's
institutional visual grammar onto a woman hidden outside that system. The approved portrait is archived at
`Character Art/Reference Models/Photorealistic/Lira Harkim.png`; her technical plate remains in production.

**Sa Ko Ren visual and origin ruling, 2026-08-22:** Sa Ko is forty-eight in Book 1 and stands **5′10″ /
178 cm**, but appears approximately in her mid-thirties. She is a Terinoki warrior who survived the Wild
Sands, found its singular windfall, and converted that capital into the forges, workshops, artisans, and
production system that became the Iron cartel. She directs and tests that system; she was never personally
a metalworker or forge laborer. Her appearance therefore follows her actual life: tall and leanly athletic,
with a lifelong soldier's balance and economy; refined East Asian features; deep black hair without silver;
dark brown eyes; a warm light-medium complexion; and no distinctive scars. Her formal register is a
Terinoki warrior-aristocratic one—wrap-front layers, a structured jacket, divided hakama, obi, and a
sheathed sword—not Kaha'ani court dress. The old corded-arms, silver-temples, and forge-burn language is
superseded. Her approved identity portrait is archived at
`Character Art/Reference Models/Photorealistic/Sa Ko Ren.png`; her approved exact 5′10″ fitting-frame
plate is archived at `Character Art/Reference Models/Height Calibration/Sa Ko Ren.png`.

**Melina Kemvimore visual and height ruling, 2026-08-22:** Melina is twenty-six in the Book 1/2
chronology and stands **5′8″ / 173 cm**. Her approved photorealistic identity is healthy and softly
slender, with a light warm-olive complexion closely matching Rosik's sheltered family baseline, near-black softly wavy hair in a polished low court
arrangement, dark brown eyes, and refined features that read credibly as Xion's sister while retaining a
trace of Rosik in the brows and habitual composure. Her restrained wheat-gold, cream and deep-brown noble
dress communicates Grain-house status through cut and fabric rather than ostentation. Her approved solo
portrait is archived at `Character Art/Reference Models/Photorealistic/Melina Kemvimore.png`; her exact
5′8″ plate is archived at `Character Art/Reference Models/Height Calibration/Melina Kemvimore.png`.
Because the generative plate repeatedly placed her around six feet, its geometry was first fixed against
the master frame with a deterministic 68-inch placement rather than treating a generated measuring scale
as authoritative. That construction introduced visible cutout artifacts, so the approved final plate is a
cohesive generative repaint locked to the corrected 5′8″ crown and brass heel-line positions. The
artifact-heavy deterministic source and rejected too-tall plate remain in the draft archive.

**Ronas Dermir visual ruling, 2026-08-22:** Ronas is forty-nine in Book 1. He is solid,
broad-shouldered, work-hardened and quietly powerful rather than bodybuilder-large, with thick strong
hands; short dark-brown hair beginning to grey at the temples; restrained dark stubble; dark hazel-brown,
hard eyes; and a warm medium complexion. The prose-established scar remains a single modest old mark
through one eyebrow, with no additional distinctive facial scars, and one side of his upper lip turns
habitually upward in skepticism or contempt. His presentation is deliberately rougher than a merchant's:
coarse homespun, battered leather, patches, repairs and scuffed boots, without noble or cartel polish. The
Iron Hall's authority is likewise salvage-built—ancient brass around rough platforms and a scarred
heavy-plank desk—not a respectable paneled office. His approved Book 1 identity portrait is archived at
`Character Art/Reference Models/Photorealistic/Ronas Dermir.png`. He stands **6′0″ / 183 cm** in Book 1:
one inch taller than Xion and Elara, two inches taller than Sa Ko, and one inch shorter than Rosik, with
his broad build making the height read more heavily than Rosik's lean frame. His approved technical plate
is archived at `Character Art/Reference Models/Height Calibration/Ronas Dermir.png`.

**Bittek visual ruling, 2026-08-22:** Bittek's Book 6 appearance is a two-stage read. At first glance he
looks hard, powerful and dangerous: blackened leather, padded shoulders, excessive straps, buckles and
studs, high boots, a deliberately wide stance, and an oversized ornate knife displayed like a credential.
Closer inspection reveals the actual man—naturally narrow-shouldered, softly built and untrained, with a
slight belly; a broad faintly toadlike face; thinning medium-brown hair combed back too carefully; close-set
brown eyes; and a light-medium sallow-warm complexion. **He is completely scarless**, including an unbroken
nose, unmarked ears and unscarred hands: he wants the proof that he paid a physical price and refuses to do
what earning it requires. The immaculate knife is status jewelry masquerading as a weapon. He is in his
early-to-mid forties and **5′10″ / 178 cm**—shorter than Xion and exactly Tiberian's height at their
late-Book-6 encounter, when Tiberian is about eighteen.
Exact age remains unset. His approved identity portrait is archived at
`Character Art/Reference Models/Photorealistic/Bittek.png`; his approved calibration plate is archived at
`Character Art/Reference Models/Height Calibration/Bittek.png`.

**Bittek confrontation ruling, 2026-08-22:** Tiberian descends into the Warrens with Kai and a strike team,
but he confronts Bittek at the taps **truly alone**. The distinction is load-bearing. Bittek never accepts a
fight he believes he might lose; organised attempts to seize him repeatedly fail because he abandons
positions, spends other people as obstacles and disappears before visible force can close. His cowardice is
operationally effective. Tiberian recognises that the only way to stop him is to offer apparent vulnerability,
leaves Kai and the squad conducting the larger operation, and approaches without hidden backup. Bittek sees an
eighteen-year-old prince of exactly his own height, mistakes the Tiger Prince's reputation for the same kind of
manufactured intimidation he uses himself, and accepts the only fight of his life because he believes it is
already won. **No strike team is present or nearby for the confrontation.**
The approved scene reference is archived at `Character Art/Scenes/Tiberian and Bittek/At the Taps.png`:
both men stand naturally at the failing water station before either weapon is drawn, with Bittek's padded
breadth and hand on the immaculate knife carrying the performance while Tiberian supplies no theatrical
gesture at all.

### Elara and Xion have no canon height relation — **AUTHOR'S RULING 2026-08-20**

**The old claim that Elara was taller than Xion is removed, not reversed.** The only prose support was
B1 ch24's description of Sa Ko Ren as *"taller than Xion, nearly matching Elara's height"*; Elara's and
Sa Ko's sheets repeated the same comparison. All three formulations traced to the repository's initial
commit, with no later authorial ruling, no independent staging anywhere in Books 1–3, and no downstream
dependency. The later retro beat draft calls Sa Ko tall and does not preserve either comparison.

The author's ruling when the sentence surfaced during visual development: **"This is almost certainly a
leftover from some older thing that I don't even remember."** He genuinely did not recall ever deciding
that Elara was taller or conceiving of the pair that way. Ch24 now describes Sa Ko as tall without using
either character as a measuring stick; the Elara and Sa Ko sheets match it. **Nothing now establishes
Elara's height relative to Xion's, and no difference should be inferred in either direction unless the
author makes a new call.** Sa Ko remains canonically tall.

### The camera does not leave Xion for a closing image — **AUTHOR'S RULING 2026-08-06**

**Stated generally by the author, so it applies past the chapter that prompted it:** *unless it is Xion's
speculation, no omniscient narrator telling the reader things Xion wouldn't know.* It was prompted by B3
ch10's final paragraph, now cut. **A chapter-closing pull-away is the specific temptation**, because the
last line of a chapter feels like a place a camera is allowed to drift, and it is not one.

**The rule that catches this in Books 2–8 is §6, not rule 0.** *(Correcting a misattribution made when this
entry was first written, 2026-08-06.)* Rule 0 — *the camera stays on Xion's shoulder* — is scoped **Book 1
only** in its own first four words, because it is the theme of a book called *The Grain Merchant's Son*,
and its named exceptions (establishing the whole book, ending the whole book) belong to it. Outside Book 1
the binding constraint is the §6 house rule, *close third-person limited; the narrator knows only what the
POV character knows*, plus whatever the chapter's own beat draft locks in its **POV:** line. **The
distinction is not academic.** Rule 0 forbids the camera leaving Xion at all; §6 forbids the narrator
knowing what its POV character does not — which permits a **deliberate, planned POV break to another
character**, and Book 3 has two of them on the books already (ch14, Ondra Kelgrav; ch18, Kalden Erulius).
An argument that reaches for rule 0 outside Book 1 will over-forbid, and will over-forbid in the direction
of refusing moves the plan already contains.

**Be precise about which rule catches it, because the two fail differently.** B3 ch10's cut line —
*"Below all of it, from somewhere under the last level anybody had seen, the pulse came up through the
stone"* — contained **no fact Xion lacked.** He hears the pulse, and he knows how far the expedition has
mapped, so the inference was his to make. What was wrong was **camera position**: *below all of it*
stations the reader beneath the city, where Xion is not. So the test is not only *does he know this*, it is
also *where is this sentence standing*. A version of that line observed from his shoulder would have been
legal — and would still have been cut, for the separate reasons in the ch10 draft's beat 19 note.

### Images live in Backblaze B2, not in git — **AUTHOR'S RULING 2026-08-05**

**Raster images are not tracked in this repository and are not to be re-added.** They live in the B2
bucket `haishuo-writing-images` under the `elvandar/` prefix, at paths mirroring the repo, with B2 file
versioning on. `Tools/sync_art.sh` moves them; `CLAUDE.md` §7 carries the operating instructions. **All
25 PNGs were also purged from history retroactively** with `git filter-repo`, and both branches were
force-pushed.

**The author's reasoning, which is the part to keep:** *"Git's purpose was originally for code; it's not
a cold storage bin, that's literally what B2's purpose is. And art doesn't need versions the way text
does."* Git stores meaning in text — a three-word edit to a draft costs bytes and reads as three words.
A PNG has no diffable interior, so git stores a whole new multi-megabyte object and returns nothing.
**The images were 99% of the repository**: the entire textual history of eight books packs to 1.2 MB and
the images were 122 MB.

**Two carve-outs I proposed were wrong and were withdrawn.** I argued `elvandar_map_painted.png` earned
its place because the master list names it as the authority for the `Places/` audit — but being *cited*
is not needing *history*, and the audit wants the current map, not its ancestors. It is also **generated
output**, rendered by `render_elvandar_map.py` from `elvandar_map_v1.svg`, both of which remain tracked.
I then argued for keeping `Hauren - First Entry.png` because a canon file embeds it — but the Viewer
resolves embeds against the filesystem, so it renders fine locally, and only github.com shows a broken
image. **Ruled acceptable. Do not re-add the PNG to fix it.**

**SVG stays tracked and this is not an inconsistency.** It is XML text, it diffs, and the five in
`Places/` total 115 KB.

**A fresh clone has no images.** Run `./Tools/sync_art.sh pull --yes` after cloning. The Viewer is
unaffected on this machine because it lists and resolves from the working tree, which `.gitignore` does
not touch.

### Retired visual assets have no authority — **AUTHOR'S RULING 2026-08-22**

**The earlier illustrated suite is retired in full.** All fifteen illustrated character models, the
illustrated Xion-and-Elara masquerade scene, and the original illustrated Imperial Princess Elara AU image
now live under `Character Art/Retired/`. The Xion-and-Farleen AU `Garden Reception.png` is retired there as
well. These eighteen images are historical visual-development records only: they do not establish canon,
do not establish AU continuity, and must not be supplied as reference inputs for new generations.

**No active likeness is better than a misleading one.** Kess Ashwood's retired illustration did not fill
her earlier vacancy; her independent age-eighteen photorealistic portrait was approved and promoted on
2026-08-22 and now supplies her active likeness. Kael Issamil's first candidate was rejected because it
resembled Xion too closely. His independent second candidate was approved and promoted on 2026-08-22 and
now supplies his active likeness. `Character Art/README.md` is the authority for whether an image is active,
alternate-universe material, a superseded draft, or retired outright.

**Kess Ashwood visual ruling, 2026-08-22:** Kess is approximately eighteen when Tiberian frees her near the
end of Book 6, the same age as the Valanar twins at that point. This is her age at liberation, not the age
at which the Warrens began making her fight. The first independent photorealistic candidate read too old
and is rejected; the approved identity-preserving revision retains the same face and lean pit-fighter build
while correcting her apparent age to the late teens. She is **5′9″ / 175 cm**, exactly one inch shorter than
Tiberian at their meeting, with dark ash-brown roughly cut hair, grey-hazel eyes, a light-medium neutral olive
complexion, small ordinary fighting marks but no decorative facial scar, repaired Warrens fighting clothes,
and no literal animal features in human form. Her active portrait is
`Character Art/Reference Models/Photorealistic/Kess Ashwood.png`.

Her approved 5′9″ fitting-frame plate is the first complete use of the white-background calibration pipeline:
identity-preserving white studio source, deterministic extraction and placement against the immutable master
room, then AI integration limited to edge, shadow and lighting repair. The first composite was rejected after
measurement showed a roughly two-inch visual difference from Tiberian. The corrected candidate places the
crown fourteen pixels below his on the identical 1024×1536 frame—one ruler inch—and was approved and
promoted on 2026-08-22 to `Character Art/Reference Models/Height Calibration/Kess Ashwood.png`.

**Kael Issamil visual ruling, 2026-08-22:** Kael is twenty-three in Book 1 and **5′10″ / 178 cm**, with a
medium practical build and light-medium warm-olive complexion one subtle shade darker and warmer than Xion
and Silvanno. His approved design uses a broad rectangular face, firm jaw, heavy level brows, hazel-brown
eyes, and short brushed-back medium-dark chestnut hair. He is clean-shaven and unscarred. Structured
charcoal Iron-clan professional clothing, restrained copper/rust accents, and a folio establish him as an
operations coordinator from an industrial minor house rather than a smith, warrior, laborer, or court
peacock. His visual register is quiet, analytical and deliberately easy to overlook.

Kael's 5′10″ fitting-frame plate was approved and promoted on 2026-08-22. Five earlier generative attempts
are archived as rejected because they failed the technical ruler geometry: excessive height, feet below
the heel line, overcorrection to approximately 5′6″–5′7″, renewed baseline drift, and failure to preserve
an approved 5′10″ donor plate. The active plate instead derives its geometry from Xion's approved 5′11″
plate, holds the same heel line, and places Kael's crown exactly one inch tick lower.

**Fitting-frame construction ruling, 2026-08-22:** Height is a deterministic geometry problem, not a
generative suggestion. For every future plate, first generate the character alone in normal clothing,
standing naturally in a neutral frontal pose against a pure, evenly lit white background. The full body and
both feet must be visible, with no scenery or floor clutter and no more than a faint contact shadow. Cut out
that clean figure and composite it onto the immutable master fitting-frame room at the exact pixel height:
boot soles on the brass baseline, crown at the required ruler coordinate. Only then use AI image editing to
repair cutout edges, contact shadows, lighting mismatch and visible seams; the cleanup pass must preserve the
approved identity, clothing, pose and frame geometry rather than redesigning the plate. Check the crown and
heel coordinates again afterward because cleanup can drift them. This is the successful Melina Kemvimore
pattern, now made explicit as **white-background generation → deterministic placement → AI integration**, and
it replaces repeated attempts to make a generative model obey a ruler directly.

### B3 ch10's length stands at 7,454 words — **AUTHOR'S RULING 2026-08-05**

**`Bequest` is the longest chapter in Book 3 and that is fine.** *(Titled `The Repository` when this was
ruled on; retitled 2026-08-14.)* It was raised as a concern and the
author ruled on it directly: *"Ch10 length seems fine to me."* **Do not propose cutting it again**, and do
not treat the profile as an argument on its own — 7,454 against an Act II of 3,051 / 4,716 / 2,808 looks
outsized in a table and reads correctly on the page, which is exactly what the house rule about judging a
chapter by the book's rhythm rather than as a standalone unit is for.

The concern was reasonable when raised and is recorded so the reasoning survives: 7,400 is the number that
got `Inhabitants` split on 2026-08-04, and all nineteen beats were already executed, so any further
reduction would have cost a beat rather than tightening prose. Three routes were offered — thin the
theoretical-region section, cut the watching beat, or split at the schematics — and **none was taken.**
The open question of whether ch10 should outweigh ch11 resolves itself when ch11 is written; if the Engine
chapter wants more room than the Repository, it takes it.

### The `A Warrior's Heart` chapter reference — **AUTHOR'S RULING 2026-08-05**

**`A Warrior's Heart` beat 48 reads *"the war that was abstract in Chapter 15"* — `The Proposal` — and that
is settled.** It was the one reference the 2026-08-05 renumbering sweep left alone rather than guess at,
because the draft is pre-split vintage (its Vartonne reference needed Ch16 → Ch17) and the stale number,
14, also happened to land on a defensible chapter under the current numbering.

**The tiebreaker was content, not vintage.** That footer describes what the *reader* needs to feel, and
`Ruthless Calculus` (ch14) is where the reader is told the war is certain — Gunastran votes, commits, and
goes looking for allies. The abstraction ends there, so ch14 cannot be the "before" state. `The Proposal`
fits: the war is still being negotiated around while Kalden's offer is live, ch16 is where they choose each
other and it becomes real, and the skeleton's own ch19 entry dates the change to exactly that — *"the war
she and Xion chose each other into is no longer abstract."*

**The counter-reading is recorded and rejected**, so it is not rediscovered as a finding: from Xion and
Elara's vantage the war genuinely *is* abstract in `Ruthless Calculus`, since that chapter's whole engine is
that the reader knows what they cannot. Read as tracking the characters, ch14 would have been right. It
tracks the reader. **Do not re-open this.**

### The Paradigms are not a straitjacket — **AUTHOR'S RULING 2026-08-04**

**The stack predicts what an act costs a character; it does not dictate what they do.** Full entry now
in `CLAUDE.md` §3, which also replaces the old examples — *"a Caretaker refusing to help on principle"*
was listed there as a rule 2 violation and is nothing of the kind. **The test is not *would they do
this*, it is *does the text charge them for it*.** Priced, it is characterization; unpriced, it is
drift. The Grieving Widow Test is the anchor and it is routinely misread: **both people tell the same
lie**, and the section it lives in is called *Emotional Residue Tests*.

Recorded because the failure recurs in one direction — reading a primary as an obligation and then
reporting the derived constraint as a property of the character. It cost an exchange over Melina, where
Truth Seeker primary was used to argue she could not take her father's word about Rosik. The framework
never said that.

### Melina Valanar and her parents — **AUTHOR'S RULING 2026-08-04**

**She takes her parents' opinions far more seriously than her public affect suggests**, and Xion's most
of all. The outward read is cool, unflappable, faintly Rosik-shaped, apparently unemotional; it is
wrong, she simply is not expressive, and **Tiberian knows the difference**. On Rosik this is decisive:
her father's disapproval of the man and his methods makes her dubious of them. Not evidence she weighs
and sets aside — it *colours* her. She is not biddable on anything else and will take a position against
either parent and hold it; this is specific and familial.

**Consequence: she never takes the grain chair.** Two reasons, unequal in kind — the Green Cities are
the better solution and she can show her working, and beneath that, her father would rather chew broken
glass than sit in it. **Nobody names either, nobody asks her, and there is no refusal scene**: the chair
has stood empty her whole life and simply never gets priced. Full text in `People/Melina Valanar.md`,
Relationships and the Book 6 arc. **Not a flaw, not an arc, not to be overcome.**

### How Kaha'an eats, and the empty chair — **AUTHOR'S RULING 2026-08-04**

**Kaha'an grows almost nothing.** House Kemvimore controlled the arable land, the importation, the
granaries and the rationing, and the overwhelming majority of what came in — certainly the good of it —
went to the Noble District. The Warrens got bulk grain in increments, on a schedule, paid in coin,
labour and *help*. Brutal, extractive, and people starved under it; Rosik's sheet already calls them
*"an acceptable inefficiency."* **But it was predictable**, and that is the thing that later goes away.

**Rosik held Ronas with two levers, and only one of them holds.** *(Revised to both levers 2026-08-04.)*
There is a **retainer**, paid out of the shadow accounts, which is why the Coterie must never learn where
the Slaver King's muscle really comes from. And there is the **grain** going down the shafts at a
sweetheart price. The retainer alone does not survive scrutiny — Ronas has a cartel, absorbed every rival
gang, and took his Coterie seat by sustaining a two-month stoppage against the other three houses; money
has substitutes, and a lever with exits is a contract. **Grain has none**, because the same house owns the
arable land and the import routes and there is no price sixty thousand destitute people could meet.
**Take the money and Ronas is poorer. Take the grain and the Warrens die.** It holds a Competitor-primary
for twenty years because the cost of snapping it falls on people he **cannot afford to be seen having
reasons about**, and a bulk-supply contract lets him be leashed in public and call it commerce.

**Both levers break in one night, which is what makes the heist total** — the shadow funds paid the
retainer *and* covered the fraud that kept the grain moving at all.

**The Grain cartel's books are cooked, Enron-style — author's ruling, 2026-08-04.** The aboveboard
accounts show an operation that pays for the food it imports. It does not and has not since the Rending.
**One catastrophe made Kaha'an unavoidable and unable to feed itself in the same hour**: the Rending
destroyed the farmland *and* killed the Dunyelas–Yelpas bypass routes that had let caravans avoid the capital's
tariffs, so the city became the only road across Elvandar at the moment it stopped being able to grow
anything. The tariff income is enormous and geographic — the Suez/Singapore/Constantinople position, the
Golden Path being the only way through a desert that kills you. The food deficit is nearly as enormous.
The gap, plus everything that can never be a line item (the retainer, the sweetheart supply, the bribes,
the Long Knives back-channel), is closed out of the shadow funds. **The city has been quietly insolvent at
the level of dinner since the Rending, and one man's crimes covered the difference.** Full economy in
`Places/Kaha'an/Kaha'an_ The Desert Crossroads.md`.

**Consequences, all of which strengthen what was already there:**

- **Why nobody took the chair.** The most valuable asset in Balisha was fictional. Anyone who did due
  diligence walked away. That is a far better answer than *nobody wanted it*.
- **Why Book 3's treasury is empty** despite Balisha owning the richest position on the continent: Elara
  inherits the revenue *and* the obligation, and the criminal surplus that closed the gap is gone. Not
  *Balisha is poor* — **Balisha holds the only road in Elvandar and it is still not enough.**
- **Motive is not function, and Rosik's stack survives.** He accumulated because *more* is its own
  reward; a drive with no terminal state also expands the flagship past what it can carry, and the hoard
  quietly covered the difference while remaining far larger than the hole. He never framed it as propping
  anything up. **The books were cooked by a man not, in the first instance, lying to anybody else.**
- **The continent's read on Balisha stands and gets a second floor.** `Places/Elvandar.md` records greed —
  ever-increasing tolls, wealth piling behind the walls. True. The tolls also climb because the deficit
  grows every year. **Rapacious and drowning at once**, and the difference is distributional rather than
  aggregate, so Book 1's indictment is untouched.
- **Xion knew it was a hoard and did not know it was load-bearing.** Keep this clean: it is what makes B2
  ch14's *"He had pictured a cost he could name"* exact. **He holds the true books and this still
  holds**, because *he read them for what he went in for* — leverage on the coalition, which he found and
  used to dismantle Tania and Sa Ko Ren. Nobody asked whether the cartel was solvent, because that was
  not a question anyone in the room had. **The most important fact in Kaha'an sat correctly filed and
  unread**, and a thorough, accurate reading missed the thing outside the question it was asking — the
  same shape as Melina's models in Book 6. **Never point at the rhyme.** Confirmed on the page in B3 ch1:
  *"The seizure records out of House Kemvimore. Do they include any accounting of persons the cartel
  held?"* — the Caretaker reading the Merchant's ledgers for the only thing in them he cares about.

**And the books are the mechanism under Book 6's rhyme, which had only been asserted.**
  `book6_outline.md` says Xion's certainty about Rosik *"was not laziness; it was twenty-three years of
  the most careful reading he had ever done, and the reading was correct right up until the man stopped
  being someone a reading applies to"* — true, and silent on *why that night*. **The ledgers answer it.**
  His model was accurate: Rosik does not panic over money. It broke on an input Xion did not know he was
  holding. **He thought he was taking the wealth and the leverage; he took the floor.** So B2 ch12's
  *"some part of Xion doubted the man was built for it"* is **not hubris being punished** and must never
  be played that way — it is a correct model meeting the one variable outside its domain, which is
  Melina's Book 6 failure twenty years early and in her father. **Neither book points at it.** His plan in
  order — strip, force the withdrawal, try him for the regicide Xion wrongly believes he ordered, reform
  Grain in the clear space — is recorded on his sheet; *the trial is the most ironic item on it, since it
  is the step that most needs a calm man across the table.*

**The books are why Rosik panics, and the money is not.** *(Ruling 2026-08-04; B2 ch13 reweighted to
  match — the ledgers moved from a secondary find at two sites to the point of the raid, and Kael's
  *"the money's the most of it"* became *"a great deal of it."*)* The man does not flinch at being marked
  for assassination, because a knife threatens his life and his life is not what he is; **position** is.
  Money is *less*, unbearable and survivable. The true books are **proof** — of the arrangements, and of
  twenty years of insolvency covered out of criminal money — and there is no negotiating with someone
  holding proof, nor running a fraud that size from memory afterward. **That is why the long bloodless
  bargaining Xion waits two days for in ch14 never opens**, and why what comes instead is chaos: make the
  city need him too badly to read what it is holding. Still Merchant shadow — he would call it strategy,
  and it is also an accumulator refusing the fact of less.

**Nobody in the story ever assembles the chain.** The reader does, and that is the payment. Do not write a
discovery scene, and do not let anyone deliver the accounting — if it ever surfaces it is one person
failing to make the numbers work and giving up.
He could be leashed in public and call it commerce. It also puts a second floor under his Book 2 warning
to Rosik: he knows exactly what a disordered Warrens does to a food chain that runs on goodwill.

**The precondition fired, and the prose lost — author's ruling, 2026-08-04.** B2 ch17 *did* contradict
this: it had Xion open with *"of course I know he pays you out of the shadow accounts… he can't keep you
on his coin much longer."* **The author ruled it a rule 1 error and changed the prose**, on the ground
that a cash retainer does not survive scrutiny — you cannot buy a man with his own cartel who won his
Coterie seat by outlasting a two-month stoppage against all three other houses. **You can feed his
city.** ch17, its beat draft, the Book 2 skeleton, both sheets and the Royal Road file now carry the
food version. **The shadow funds are untouched in every other respect** — they prop up Grain in general,
their loss bankrupts Rosik, and Book 7's *he cannot buy an army* still stands.

**The sweetheart price is the load-bearing detail:** the Warrens are destitute and there is no market
rate sixty thousand of them could meet, so the grain goes down below any price anyone else could get,
and the supply exists purely on Rosik's sufferance. That is what makes it a leash rather than a trade.

**And Ronas does not become a hostage.** ch17 now closes it off in Xion's read — he took his cut off the
top of every load for twenty years, the Warrens paid twice, at the shaft and in the men who came to
collect, and he never held that line for free.

**The chair empties in Book 2 and stays empty.** Rosik exiled, the Grain cartel smashed. Melina
Kemvimore is dead; **Xion will not sit in his father's chair, ever, and this is not to be dramatised as
a hard duty nobly declined.** And the crown does not take it either, on principle — Elara broke the
cartels *because* a chokehold on necessity was the injustice, and a crown grain monopoly is the thing
she overthrew wearing a better hat. So food goes to the market at market price, and the market declines
to haul bulk grain four hundred meters down to customers with no money. Shipments become irregular,
then rare. **By Book 6 the Warrens are in famine, and it is the empire's doing rather than the
machinery's.**

**The trap, and it must be closed on the page:** this is *not* "the cartels were better." Rosik's system
fed people as an instrument of control and let a tolerable number die; the market feeds fewer and
controls no one; neither defends the other. **The failure is not the breaking — it is twenty years of
not building**, because the people it hurt had no vote. Same indictment the series already levels.

**Consequence for Ronas:** with grain unreliable, he brokers what still comes down, and by Book 6 the
Slavers *are* the food system. That is what makes him indispensable and unavoidable, and it is why
Melina has to deal with him at all.

**Consequence for the Green Cities: they are food security, not charity.** Empires do not fund
generational desert reclamation as mercy. A capital of ~200,000 fed by imported grain along one desert
road is a siege waiting to happen, and the Compact War proves it. The relocation is a second use found
for a war ministry's project — which is also what finally makes Book 6's *"nothing material stands in
the way"* true and earned. **No character says any of this.**

**The numbers, exactly.** Kaha'an is 150,000–200,000 on the surface plus 60,000 below. Hauren's
terraces feed 100,000. So Hauren could have fed the Warrens nearly twice over and **could never have
fed the city** — it was never an answer to the import dependency, only to the Warrens', and it is
unreachable. The population that starves sits on top of double the food it needs. See
`Book 3 - Crown Jewel/_HAUREN_AFTER.md` for why none of it comes up.

### Hauren after the Door — **AUTHOR'S RULING 2026-08-04**

**Hauren is a dig site, not a destination.** Its existence becomes known; access does not follow.
The Great Shaft is gone, the only route is the Long Knives' road through Dead Man's Passage, and B3 ch6
settled that the road cannot become a supply line. All traffic is porters, so **knowledge flows out and
tonnage does not** — purification and energy reach the world as designs rebuilt on the surface, which is
also why the reverse-engineering takes the years Book 4 requires. The city becomes a small, expensive,
jointly-staffed research station under Balishan sovereignty with the Destiny Engine sealed and cordoned,
and **the Green Cities are its actual output**: the bequest reaches the living as somewhere else to
live. Nobody moves in, for six reasons that are Book 6's business and must not be argued on the page in
Book 3.

**Full brief, written for the Book 3 drafting session:** `Book 3 - Crown Jewel/_HAUREN_AFTER.md`. It
carries the prohibitions (no reopened Great Shaft ever, no food convoys, no crown map, no settlement)
and the Book 6 correction below.

**Book 6's ignorance premise — CLOSED, applied 2026-08-04.** `book6_outline.md` had said nobody ever
learns the Warrens are Haureni — *"The tunnels are old. That's all anyone knows"* — which Book 3
makes impossible, since the expedition descends through those tunnels to reach the Door and the empire
then spends twenty years building from Haureni designs. **Ruled: everyone knows exactly what the
tunnels are, and it does not help.** Knowing whose machines these are is not the same as being able to
maintain them; Balisha holds *design* knowledge, extracted a notebook at a time and rebuilt in surface
workshops, which does not extend to keeping a five-thousand-year-old system alive in place. The
engineers can read the machine and cannot save it.

**No revelation scene, and no character treats the connection as news.** The origin is as unremarkable
as the age of a cathedral. And the correction strengthens the book rather than patching it: it is the
same lesson Book 6 already teaches through Melina — *a thorough and correct account of a thing is not
the power to change it* — so the surveys fail the way her models fail. **Do not point at the rhyme.**

### Hauren's two entrances — **AUTHOR'S RULING 2026-08-04**

**The Great Shaft was the front door; the Brass Door is the freight entrance.** For the three
millennia Hauren was open, arrivals came down the Great Shaft — a finished vertical bore from the
surface into the Crown's Arrival Halls, served by an elevator **spine**: a ceremonial main car for
delegations, smaller cars for routine traffic, freight lifts on their own tracks. The Brass Door is
the loading dock at the back of the building, which is why its antechamber is a bare eight-meter room
and why the passage below it is well-made and unbeautiful. Full description in `Places/Kaha'an/Hauren_
Physical Layout and Geography.md`.

**Three things ruled and not to be reopened:**

1. **The Great Shaft was collapsed and *filled*.** There is no open pit under Kaha'an and no surface
   trace. An open shaft would be found, and the premise that the surface has forgotten Hauren depends
   on there being nothing to find.
2. **The elevators were destroyed and stripped**; the recoverable parts went back into the city.
3. **The Repository does not hold the reason Hauren sealed itself.** B3 ch10 walks the expedition into
   the Repository, so this needs to be settled before the chapter is drafted: the reason went with the
   people who had it. Do not plant an answer nobody pays.

**Dead Man's Passage is natural caverns — not Haureni construction, not a designed maze.** A cut
haul road once descended through the caves to the Door and was **deliberately collapsed** at the
sealing (demolition, not decay — Haureni work does not decay). What survives is bare geology. There
is no "true path" marked in Haureni symbols; the Long Knives' map was bought with corpses, which is
what B1 ch20, B3 ch6 and the Factions doc have always said. The three-way contradiction between the
Hauren layout, Kaha'an geography and B3 working notes is closed; all four docs now agree.

**Blast radius: none in the prose.** No chapter, beat draft, skeleton or Royal Road file changed. B1
ch19–21 and ch23 name the Passage repeatedly and never say who cut it.

### Hauren's canonical visual — **AUTHOR'S RULING 2026-08-04**

`Places/Kaha'an/Hauren - First Entry.png` is the canonical location illustration for the Crown at the
end of B3 ch7, *Wonder*. Its visual register is binding: **dense concentric city-rings, radial streets,
pale civic surfaces over a dark mechanical understructure, brass ribs, integrated blue-white systems,
living garden terraces, and the open central shaft descending toward the Core's warm glow.** Hauren is
a city built into one operating machine, not a conventional bright palace district and not a decayed
steampunk ruin. The illustration is not a scale drawing; the prose and `Hauren_ Physical Layout and
Geography.md` remain authoritative for dimensions and the seven-level structure. The superseded first
render was deleted when the revised image was promoted to the canonical filename.

### The beat-draft body/instruction rule — **AUTHOR'S RULING 2026-08-02. Applied to all 64 drafts**

**The rule.** The beats in the body of a beat draft are what appears on the page, and nothing that does not
appear on the page may appear there. Guardrails, negative constraints, rule citations, correction notes and
provenance go **around** the body — header block, footer under an `**On beat N:**` header, or an indented
italicised parenthesised aside under the beat they attach to. Never inside a numbered beat.

**Why.** B3 ch4's beat A4 carried *"Not from a ruin"* as a guard against a drafter still holding a retired
error. It was correct as an instruction and it went onto the page verbatim as prose, denying a ruin no
reader had reason to expect. A beat draft carries two kinds of sentence — *what happens* and *what a drafter
must not get wrong* — and the second is usually a negation, because that is the shape of a correction.
**Negations transcribe.**

**Two exclusions, recorded so a future sweep does not take them.** *Negative choices* (what a character
deliberately does not do) are events and stay in the body. *Effect analysis* (what a beat achieves) is not an
order and stays. The test is whether a sentence could be **transcribed** into narration or only **obeyed**.

**Status.** All 64 drafts swept; 43 touched, 21 already clean. `Templates/Beat Draft Template.md` now states
the rule, so drafts written from the pattern comply by default. **Books 4–8 have outlines only** — when their
drafts are written they inherit the rule from the template and need no retrofit. Nothing outstanding.

**Three findings came out of the sweep and are fixed:** B3 ch18 beat 17 described a decision taken in
Vartonne inside a chapter narrated from Xion's shoulder in Terinok, and could not have been staged; the same
beat called **Sa Ko Ren *him***; and B1 ch3 beat 15 paraphrased a line it had marked verbatim, corrected to
the prose, which is the source for Book 1. Details in the changelog.

### R2-1 — B1 ch18's untreated child — **CLOSED, fixed in the prose**

*Was:* the chapter ended with Xion holding a dangerously ill child and never treating him — closing on
his feeling instead of his hands at the exact moment his defining practice applied. Flagged as the
single highest-priority outstanding item in either book.

*Now:* ch18 l.243–273 is the field surgery. He asks for the hand he stitched in ch1 and finds what six
weeks in a collapsed tunnel made of his own work; opens it along the line it had already chosen, drains
it, spends the last of the flask flushing the wound rather than putting it in the boy (*"and hated the
trade, and made it"*), the last of the verbana, the last of Janice's linen for a binding and a sling.
Then: *"It was good work. He knew it was good work… Then he laid the backs of his fingers against Tam's
forehead and held them there, and the good work stopped mattering."* The infection is in the blood and
nothing he carries reaches blood.

### Q1 — Farleen's Book 1 exit — **CLOSED. No change**

The reviewer's note was wrong, not merely overruled. She has no role in Book 1's endgame and
manufacturing one would be shoehorning. The better reason: Book 2 defines her by **presence without
position** — *"a woman with no post, no title, no institutional reason to stay anywhere — and she
stayed."* A character whose nature is unobtrusive constancy should not get a curtain call in the last
act of someone else's book. The quiet exit is the correct shape. The handoff also needs nothing —
Book 2 ch2 opens with the pastry already an established habit.

### Q2 — B1 ch16–17 staging — **CLOSED. He stays outside; the chapter is cut hard**

The *length* cut stands on craft (3,069 words for an offstage failure reads as accident, not intent);
ch17 is now 1,680 words, the shortest chapter in Book 1. Putting Xion inside one of the three
operations does not stand: Farleen is tactically right that he is untrained, and the text says so.
What he does instead is count — *"He waited thirty-one minutes and counted them, because counting is
the only thing left he is any use for."*

### Q3 — B1 ch5's speed — **CLOSED, not a gap**

Xion agrees to become a fugitive in ~40 lines. That is correct and must not be slowed. ch3 already
establishes that refusal doesn't slow him (*"It won't stop me." / "I know."*), ch1 has Janice name the
trap exactly and he goes anyway, and ch19 states it outright: *"He didn't even really consider it."*
Fast acceptance **is** the characterization; deliberation added here would be rule 2 sacrificed to a
pacing instinct. Nor is the cost unpaid — ch7 collects it two chapters later, when he walks into his
own clinic and has to call Master Fen a friend of his.

**And the filed diagnosis was wrong in a specific way, since fixed.** The fault was never the speed.
It was that the chapter *staged a deliberation it had no room for* — ~90 words split either side of
the acceptance, enough to invite the reader to audit the decision and nowhere near enough to survive
the audit. Both passages are cut. He now agrees the way he does everything: the question is the answer
and he notices a beat late, rhyming with the ledger answer thirty lines on. A stray fountain he had
not passed went out with the second passage — the fountains are ch8's.

**Still closed after the 2026-08-03 Tam pass**, which added ~125 words to ch5. The insertion sits at beat
11a, ahead of the options at beat 12, and it is a door closing on somebody else rather than deliberation
about his own choice — Elara refuses to help him find the boy, and he signs on thirty lines later anyway,
which is the ledger trait rather than a hesitation. **It must stay short for that exact reason:** long
enough to be weighed and it starts reading as *I'll help you if you help me*.

### Janice's failing sight — **VETOED. Author's ruling. Removed from the series**

Considered as the first-patient injury and **rejected** — it was doing too little narrative work for
what it cost, and the book has enough going on. **Janice's sight is fine. Do not reintroduce it in any
book.** The first injury is deliberately unspecified and Xion **cured** it.

*Applied:* `People/Mistress Janice.md` lost the whole *Her Sight* section; B3 ch3 lost the blindness
from beats A3, A5, A8 and A10. **Blast radius was checked first and Book 1's prose has no dependency
at all** — the check also turned up a second stale citation, since the sheet had been justifying the
thread with a ch1 line (*"squinting at the gap in it"*) that does not exist in the current text.

**It tightened the ledger thread rather than loosening it.** The old logic was that he could not cure
it, only slow it, and the debt was that he asked and told her the truth. With the cure there is no
debt at any point — and B3 ch3 A5 improves most: her workroom now contains no misfortune at all and
does more damage for it, because it removes the last excuse. She did not come because there was
nothing to come for.

*Supersedes an earlier "CONFIRMED — eyesight, not hands" entry here. If a document still argues that
she goes blind, or offers her a physician for her eyes, it predates this ruling.*

### Janice's return — **CONFIRMED alive. Landed in the Book 3 beat drafts**

- **As written:** B3 ch1 beats 18–19 (Xion makes a second administrative request beside the name change — does the Kemvimore seizure record account for persons the Grain cartel held?). B3 ch3 Movement One, beats A1–A14 (Kael finds her in Rosik's hidden ledgers; the meeting; the refusal; the question; the missing dismissal).
- **Constraint honoured:** she is not in ch1. She hears about the name-taking secondhand and has nothing to say about it, because to her nothing changed — she has called him Fen for eight years.
- **Where:** Book 3, Act I. Book 3 is entirely at beat-draft stage, so insertion is cheap. Book 2 is finished and tight, and Xion's isolation there is load-bearing — handing him Janice back mid-Book-2 would soften the thing that book is about.
- **Why she never came:** she has never asked anyone for anything. Eight years housing an illegal clinic and the only thing she ever requested was one copper. She has rebuilt the shop in miniature two streets from where it stood, and it works — so there is nothing to come for, and arriving on his doorstep would be the first request she had ever made. She has been in the city the whole time. This is the trait she was built with, taken to its worst conclusion, and it does more damage without a misfortune propping it up.
- **What she says:** nothing grateful, nothing apologetic, nothing about Mira. Something operational. Best candidate is a version of the question she asked for eight years — *did you ever start charging?* She burned the ledger and it is still the only thing she wants to know.
- **Hard constraint:** she must NOT be present for Book 3 ch1's name-taking. If she is in the room the scene becomes about her, and Mira is the entire point of it. Find her after, or well before, and let her hear about it secondhand — one dry line.

### Who tells Xion he has become his father — **CLOSED. Wrong question. Author's ruling**

**Xion does not become his father.** He *became* his father for four chapters of Book 2, and he **knows
it**. Nobody needs to tell him and nobody should. B2 ch18 is not him refusing to hear it named — it is
titled `"Don't."` because *he* is the one who says it, to himself, mid-manoeuvre, with Melina's death
loaded and a woman in front of him he could spend it on. He sees exactly what he is doing while he is
doing it.

**The distinguishing fact is not that he can't do it. Book 2 proves he can.** It is that afterward,
**he breaks**. B2 ch20, the low wall: *"And the cold broke. Not all at once — the way a wall goes, which
is from the inside, out of a fault that was there long before any of it showed on the surface."* The
engine that turned grief into precision runs out of things to burn and stops, and what was underneath is
still a brother on a wall who is never going to see his sister come around that corner again.

**Rosik never breaks.** That is the whole comparison, and it is structural rather than moral — not
*Xion is better*, but *Xion has a fault line and his father does not*. Never write a scene in which a
character delivers the verdict to his face. It would tell him something he arrived at alone, under his
own power, in the middle of the act, which is worth immeasurably more.

### Resolved craft items

Fixed in the prose, verified against the chapters 2026-07-27.

| # | Was | Fixed by |
|---|---|---|
| C-2 | ch6 and ch8 have the same shape (walk, witness, explain, vow); ch6 has the better single idea. | **The framing was wrong** — the two chapters do different jobs (ch6 makes Elara the *signatory*; ch8 carries the injustice specific to a desert city) and it was never a choice between them. ch8 rewritten instead: the arch gate and its ledger, Xion spending the name on a convenience, Elara convicting him for it, **one** fountain with no statistics attached, the children in the basin left unexplained, and a single held amber. 1,906 → 1,214 words. |
| C-8 | ch21 raises a stake and dissolves it in the same chapter (the Ronas complication). | `e006531`, and on re-verification **function, not fault**. ch21 l.195 — the escort is the answer to the complication rather than a favour: *"Ronas gave you a straight road to the surface and you didn't walk it, and men like Ronas count that… My escort makes it somebody else's arithmetic."* The complication is the *mechanism* that motivates the Mistress's escort; without it her help is unmotivated charity from a character who does not do charity. **It also leaves Ronas counting a breach, which is unspent** — see [§2](#2-cross-book-threads) for the standing rule on unpaid seeds. |
| C-11 | ch18 — Ronas's dialect wobbles between registers. | `e006531`, then finished on the author's ruling that the dialect must be consistent: four remaining outliers corrected in ch18, one of which contradicted him inside forty lines (*"Patchin' people up"* against *"patching his leg"*). Rough register now holds throughout — *"I got eyes, Cullen," "Also heard you been callin' yourself Master Fen," "then you come askin' around the Crossroads."* **The voice is LOCKED on `People/Ronas Dermir.md`** with the full marker list, the drift diagnosis and a Book 6 warning. The one grammatically clean sentence (*"patterns are what I get paid to notice"*) survives deliberately — it is a shift at the punchline of the three-finger count, not a wobble: he stops sounding casual exactly where he makes the point. **Do not "fix" it.** |
| C-12 | B2 ch1 and ch3 state the same realization in the same metaphor. | **Stale — the ch1 half never existed.** The word *cell* appears **nowhere in Book 2**; the only grep hit is inside "ex**cell**ent". What ch1 l.61–65 actually does is the fix C-12 recommended, already in place: *"He had done this"*, an explicit refusal to finish the thought, and *"He turned away from where that led."* ch3 completes it and Sela's doorway closes it — suspicion in ch1, conviction in ch3, as prescribed. Residue split off as **C-28**. |
| C-13 | B2 ch6, ch7 and ch10 all close on a long summarizing paragraph of Xion alone. | **Retired — mis-specified, superseded by C-26 and C-27.** Wrong about ch7: its ending is not a long summarizing paragraph but four short lines, and one of the best in the book — *"an argument is a thing two people are having. You can lose an argument and still be in the room. / He was not in the room."* The real ending pattern is ch6 and ch10 only, now **C-27**. And the flag missed what was underneath it: a seven-instance narration verdict-stamp, now **C-26**. Recorded rather than silently rewritten, because a flag that was wrong about a good ending is exactly the failure mode this table exists for. |
| C-14 | B2 ch14 — Melina's death depends on the reader believing the Surface Warrens are lethal enough to kill a Kemvimore mid-sentence, and nothing established it. | **Closed — diagnosis wrong, no change wanted.** ch14 is 1,429 words, not 1,300; the violence is ~250 words, not ~400, and it is summary **because Xion is not there** — it arrives through Kael's contacts, Silvanno's channels and Farleen, and rule 0 holds. The chapter does not need to establish lethality, it needs **unaccountability**, and Farleen establishes it in one line with her own instrument: *"the four who did it didn't even go through his pockets… It's that it's stopped being **for** anything."* The length reads correctly too — ch13 2,629 / ch14 1,429 / ch15 2,232, short chapter before the drop, the same runway logic that protects B1 ch8. |
| C-15 | B2 ch2/ch3 both use *"You've gone somewhere" / "I'm here"*; confirm intent. | **Closed — deliberate, and the text answers it.** ch3's *"again"* plus the narration conceding the lie (*"He wasn't, quite, but he came back for her"*) makes it a running beat, and it moves: ch1 he deflects and she lets it go; ch3 he lies, the book says so, and he comes back **for her**, the last time it shows him choosing to. Melina-specific — she is the only person who notices, which is her entire function. Two instances. **Do not add a third.** |
| C-20 | ch19's objections repeat instead of escalating; ch20 runs the same shape (Farleen shouts, Elara apologises, *"Stop saying you're sorry!"*). | Rebuilt as a **descent through five arguments**, each abandoned as the last one fails: tactics (*"That's everything we came for, and it's forty feet behind you"*) → ground (*"their ground. Not their territory — their **ground**"*) → the trance (*"A woman in a fit, choosing left"*), after which she goes silent and *"Xion discovered that he wanted her to"* speak → medicine → the person. No argument now appears twice. **The medical rung is the chapter's spine:** Xion stops, lays the backs of his fingers against Tam's forehead — the ch18 gesture, returning to mean the opposite — finds she is right, and walks on. That is the first break of the consent guardrail, now on the page. ch20's fight rebuilt so Elara stops apologising and asks what Farleen cannot answer: *"If it starts again — can you stop me?" / "No." / "Neither can I."* Net length barely moved (2,427→2,410; 1,825→1,736) — substitution, not trimming. |
| C-1 | ch2 and ch3 run the same argument; ch3 should be about what they committed to, not whether he's sane. | ch3 now **inverts** it — four days of elimination convince Kael and Silvanno he is *right*, and that is why they refuse. *"I'd rather my friend was mad. Because a mad friend I can walk home."* |
| C-4 | ch17's "something feels wrong" runs four times with no new information; chapter also over-long. | One instance (l.22). Chapter is 1,680 words, the shortest in Book 1. |
| C-5 | ch24's combat trial is almost entirely commentary; the climactic test needs one concrete exchange before the analysis. | ch24 l.79–87 — the feint high, the strike driving up under the arm into the short ribs, and Sa Ko taking it without moving her feet. The exchange is not merely placed before the analysis; it is what *triggers* it, and Farleen's ch16 ribs are the measuring instrument. |
| C-6 | ch25 is mostly told; the closing roll call reads like the outline leaking through. | ch25 l.235 motivates the roll call from inside the POV — *"because he wanted to be able to remember, afterward, exactly where everyone had been standing"* — and l.237–243 then close four arcs in four sentences, all silent (Vesk's hands loose at his sides for the first time in weeks; *"Kael was counting the exits. Of course he was."*; Silvanno's raised hands; Farleen watching the room instead of the throne). The chapter ends on the dust rather than a summary: *"No one had breathed in here since the night it was sealed. / It was breathing now."* **The triumph was never the problem and remains protected — see [§4](#4-do-not-touch).** |
| C-7 | ch9's marriage-alliance cover is loaded and never tested at the ball. | ch10 l.121–139 — Tania probes the cover directly (*"is he attentive, or is he merely thorough?"*), and the text registers that three days of training covered the insults and nothing at all covered someone being kind to Elara about him. |
| C-9 | ch23's Vesk — twenty years of fury evaporates in ten lines, sequenced backwards (concedes, then attacks). | Re-sequenced and expanded to ~50 lines: the fourteen-days accounting first, Elara's account second (*"I didn't think about you"*), the concession last. |
| C-10 | ch22 — Elara reaches for the ch15 slaver argument verbatim; the text should register that she knows. | ch22 l.101 — *"the same weapon, off the same shelf… she had reached for it because the first time it had gone in."* |
| C-21 | Surviving closing swells. ch6 and ch23 were cleared by the C-22 pass; ch22's *"This was our first real fight." / "It was a good one."* remained. | **Refiled as a rule 3 item and applied.** The flag named the joke; the problem was the nine lines above it. ch22 had two endings stacked — the absolution failing (*"The words went into him and found nothing to hold on to"*, and Elara watching it fail without understanding why), and then a **repair sequence** on top of it: *we see the world differently*, *does that mean we can't—*, *no, quickly and firmly*, and the fight/good-one exchange. None of it claimed Xion had been reached, but the *shape* was reconciliation, and shape is what a reader carries out — so the failure was un-landed one paragraph after it happened. Nine lines cut; the chapter now goes from her watching it fail straight to the embrace. **It also puts Elara on her own instrument:** she reads rooms, she has just seen words fail, so she stops using them. He holds her back — he cannot take the absolution and he can take *her*, and nothing remarks on the difference. l.237's *"Both trying to find their way back to each other"* went too (the narrator announcing the scene's project, and *fading light* there pre-spent the closing image). 2,557 → 2,481 words. **The beat draft planned the cut lines and its own footer contradicted them**; footer was right, beat was wrong, and both are corrected. |
| C-16 | ch5 — *"Her voice grew stronger, more certain"* twice, four lines apart (l.99, l.103), plus *"steady, certain"* eight lines later. | The second attribution cut entirely — she is not swelling there, she is batting away an objection, and the dialogue carries it: *"Everything is dangerous in this city. Besides, I'm not helpless."* Xion looking at his bandaged shoulder is the beat that follows and it lands harder without a pause in front of it. l.99 **keeps** its swell, which is where she is actually building. *"steady, certain"* → *"steady"*; *steady* already said it. |
| C-18 | ch11 — *"Mutual vulnerability. The foundation of any good partnership."* Theme stated in dialogue. | Replaced with the concrete trade, in her register and sourced in the chapter: *"You're carrying the thing that gets me taken. I'm carrying the thing that gets you executed. It seemed only fair to me too."* The last line answers his *"Seemed only fair"* two lines above. **The theme is no longer named by anyone** — he then reaches for *partners* himself, which is better assigned: he is the one who needs to know what a thing is, she is the one who deals in what it costs. |
| C-3 | ch3's first movement is summary — four days of elimination compressed, with only Jorik dramatized. | **Closed on merit, not by a fix.** ch3 now runs four scenes, and the Amber Leaf refusal that carries the chapter is fully dramatized; the front-half compression is the chapter working, not a montage. Two independent readings reached *not a finding* separately. |
| C-17 | ch9 — the dance lesson runs three times, each closing on near-contact broken by a step back. | Closed by the C-22 pass. The near-contact beat now lands **once**, at l.119; day two is the dress and day three the complications, and the chapter ends on the cover story and the exits rather than on a fourth near-miss. |
| C-19 | ch11 and ch12 both close on Xion alone on the floor in the dark, reflecting. | Closed by the C-22 pass — ch11's reflective tail was cut and it now ends on *"She understood."* ch12's *"Count toward what?"* is unique again, and is a **deliberate rule 0 exception, author-confirmed**. |
| C-22 | The Book 1 chapter-ending pass — the narrator previewing the next chapter (*"Tomorrow they would…"*, 9 chapters), the epithet pull-away, and camera-off-Xion breaks. *(Filed on the cloud branch as C-16.)* | All 25 endings audited: 8 already worked and were untouched (ch1, 4, 10, 12, 15, 17, 19, 21); 13 fixed by deletion, ~450 words out, the working ending in almost every case already sitting one paragraph up; ch9, ch23 and ch24 **written**; ch25 handled by deletion only, with the triumph untouched per the author's condition. A rule 1 item was found inside the pass and fixed first — ch18's ending contradicted its own scene. |
| C-23 | ch9's realization stated twice. *(Branch C-17.)* | l.111 trimmed; it now lands once, at the chapter's end. |
| C-24 | ch4's betrayal — POV bends, and the author's design not recovered. *(Branch C-18.)* | POV bends replaced with **misattribution** — the method ch3 established, turned against him. Crying descriptors 12 → 5 and now escalating rather than repeating; exposition trimmed, the tumbling kept. 31 words out of ~431. **Move 1 is dead — do not revive it.** |
| C-25 | Dialogue-to-narration ratio lopsided across Act I. *(Branch C-19.)* | **Withdrawn — not a real pattern.** ch5 is 2.3:1, the same as post-fix ch1; only ch4 was lopsided, and that was C-24. Flagged off two data points and generalised. |
| C-26 | B2's narration verdict-stamp habit — seven instances. *(Branch C-20.)* | **The first editorial change ever applied to Book 2.** Seven cut (ch3, ch7, ch9, ch10, ch11, ch14, ch20); six deletions, ch11 rephrased to avoid colliding with ch9:53. Six legitimate uses deliberately left — ch2 ×2, ch7, ch11 as idiom, ch4 as dialogue, and ch18's *"The stop was the whole of it"*, which identifies which part of an utterance carried the meaning rather than stamping a conclusion. **The bookend argument for keeping ch20's instance is dead, not weakened.** |
| C-27 | B2 ch6 and ch10 both close on a long enumeration. *(Branch C-21.)* | **Investigated, reframed, then applied.** The flag as filed was largely withdrawn: the two lists differ in tense, grammar and content, sit four chapters apart, and both beat drafts specify an alone-ending as the plan. What was applied is what the flag missed — **ch10 ran the same enumeration twice**, three of six items in the closing aside being compressed restatements of three of the five *"He could not…"* clauses above them. Those three cut, the new tail (*no plan, no lever, no move anywhere in the world*) kept. Plus ch6's *"That was the sour heart of it"*, the last C-26 variant. Eighteen words out, nothing added. **Withdrawn and not to be re-raised: any cut to ch6's three-part list or to ch10's *"He could not"* list.** |
| C-28 | B2 — *cage* carries two referents twelve lines apart in ch3. *(Branch C-22.)* | Fixed in the narration rather than the dialogue, because *cage* = the token system is the established usage and Melina's line escalates it in the same breath. *"He had given her sight, and sight had become the cage"* → *"He had given her sight, and the sight was what stayed her hand."* Also more precise: the failure is an inaction, not a confinement. Six words in, six out; *cage* now has one referent across Book 2. |

---

### "Warrens" — **CLOSED. Uratha's renamed; Kaha'an's stay.** Author's ruling, 2026-08-02

Uratha's `The Bakarn Warrens` became **The Service Quarter**. Three objections, all sound: warrens are
underground and that district is not; warrens are winding and it is a built quarter; and **a civilisation
organised around precision would never use a name that imprecise.** The capital's own location list —
Great Library, Examination Grounds, Scholar's Gardens, Seven Colleges, Market District, Dormitory Quarter —
is seven flat statements of function, and "Warrens" was the only metaphor in it.

**Kaha'an's Warrens stay, and the whole canon was swept to confirm nothing else needed touching.** Every
other instance of the word in the series is Kaha'an's, and there it is correct: genuinely underground,
genuinely winding, sixty thousand people in tunnels, and load-bearing across Books 1, 2, 3 and 6, the
series outline, `Offstage.md`, and four `Places/Kaha'an/` files.

**The distinction, so this is not re-opened.** **Kaha'an names things the way cities do** — by accretion
and association, by whoever said it first, with nobody appointed to check. **Uratha names things the way an
institution does** — by function, on purpose, in a list. The word was not bad; *these particular people
would never have reached for a metaphor at all.*

**And the edge case was raised and ruled on:** Kaha'an's **Surface Warrens** are above ground, so the
letter of the first objection touches them too. They stay. The name is vernacular — the surface ruins are
called that *by association* with the warren beneath, by the people who live in both — which is exactly how
cities name things and is honest work the Uratha use was not doing.

### Who held Kalden's mortgages — settled 2026-08-05

**Authority is `Book 7 - Last Debts/book7_outline.md`, "Who held the paper"; consequence on
`People/Kalden Erulius.md`. One line of fact, deliberately not a thread — Erulius does not appear in Book 8
and nothing downstream rests on it.**

**The creditors are domestic and unnamed:** the twelve original noble houses and the Erulian banking houses
of the Amber District — the same twelve who counselled austerity after the Compact War and were overruled.
No new party, no foreign power, nothing coined.

**The fact worth having: nobody was surprised when he died, because nobody lent on the assumption he would
live.** A sanctioned rump state, a third of it seceded with the farmland, mortgaging mines and a palace to
attack the strongest power on the continent — **no one advances against that at a price assuming success.**
They priced failure, which is not lending; **it is buying the mines cheaply and waiting.** He thought he was
raising an army. They thought they were buying a country at a discount. **They were right, and it took about
six weeks.**

**So the state ends up owned by the men who told him not to**, which answers *waiting for someone else to
decide what it becomes* without any outside power acting. **And it is the last and cruellest instance of the
Gunastran ruling** — competent people pricing correctly — because what is being priced correctly here is a
man's final act of self-belief. In his own telling he is a wronged heir making a righteous stand; in the
ledgers, **he is a discount.** *Nobody says it on the page and no character ever works it out.*

**Rejected:** the Erulian Union buying the paper through intermediaries (Kalden would have found out and
would sooner have died), and **Vessel Street** — Greystone lends short against goods it can inspect and
refuses anything secured on a promise, so an unenforceable foreign mine mortgage funding an invasion of its
own crown breaks every rule that house has.

---

### Elara never sells the gate — settled 2026-08-05

**Author's ruling, and settling it exposed a hole in B3 ch1's own borrowing beat, written the same day.**
Xion gives three reasons Vessel Street will not **lend** and never answers the obvious counter: **they do not
have to lend, they can buy.** Selling the customs forward is not a loan and it defeats all three objections at
once — the houses collect at the Golden Gates themselves, so they need no record of the crown, do not care
what its accounts show, and cannot be defaulted on, because they are not owed anything; they own the year.
**It is the largest financial instrument in Elvandar and it was sitting unmentioned in the scene.** Tania
Larannas would reach it in four seconds and now does.

**Elara refuses it before Xion can speak, and the refusal is never explained on the page.** She broke the
Coterie because private hands on a city's necessity was the injustice, and **the gate is how Balisha eats** —
the food deficit is closed out of toll income. Selling it reconstitutes the Coterie in a different commodity
with the same people paying. **The room understands without a word:** the two people at that table who held
necessities privately for twenty years do not look at each other.

**And the refusal is priced, which is the part that must survive revision.** Xion runs the arithmetic because
somebody has to know the size of it — **the best offer Balisha will get this year, declined in under a
second.** No character tells her she was right. The position is that she was right *and* that it cost.

**Standing rule: she never sells the gate, in any book.** The offer stays permanently available and
permanently refused, and its never happening is the concrete institutional difference between this state and
the Coterie — demonstrated rather than stated. **If it recurs it must escalate**, per the recurrence rule:
higher price of refusal each time, **two recurrences at most across Books 4–8**, never in a scene that
already carries a fiscal argument. *(Ronas has the strongest available use of it in Book 6 — the crown that
would not privatise its own gate is about to intervene in his.)*

---

### Hauren is collateral, not cash — settled 2026-08-05

**Author's ruling.** Nothing behind the Brass Door is money. It is **schematics**, worth a century of
advancement and nothing inside ch1's nine-to-fourteen months. **What ends the fiscal crisis is that Balisha
becomes creditworthy** — the technology is valuable enough that borrowing against it is effectively unbounded
— **and they do not, in fact, borrow much. The option existing is the whole of what they lacked.**

**This closes the loop ch1 opened**, and it closes it with the same institution: the lease-houses refused a
six-week-old court with no record and nothing to pledge, and a crown that demonstrably owns a sealed city of
legendary technology holds the best security on the continent. **Act I's question is answered by Act II's
discovery**, which is what the book was already doing and had never written down.

**Placed in ch12, in one paragraph, staged as the reversal of ch1's beat 22:** the lease-houses come to the
crown, the Factor-Principal of House Greystone asks for an audience, and **not one figure in Balisha's
accounts has changed** — only what it can pledge. **Small, and nobody enjoys it.** No speech, no relief, and
nobody says *we're saved*; what Xion notices is that the street which would not see him in the spring wants
an appointment on the strength of a city full of dead people, and he does not say that either. **Act III
never mentions money again.** Recorded in the ch1 and ch12 beat drafts and the skeleton. *(Ch12 is also where
the Greystone Factor-Principal finally gets a name — deliberately uncoined until a chapter needed him.)*

---

### What the Crown gives Elara, and what Uratha does about it — settled 2026-08-05

**Two limbs of one ruling; full text in `Places/Uratha/Uratha_ The Land of Scholars.md` and
`People/Elara's Connection to Hauren.md`. Raised because the Crown does not appear once in Books 4–7.**

**Worthiness gates transmission; it does not deliver.** Opening the channel is one thing and drawing anything
through it is a skill — scholarly practice, forming a question precisely enough to be answered — and Elara
was raised by soldiers. **She gets impressions, not knowledge**, calibrated deliberately to her Hauren sense:
occasional, involuntary, un-articulable, scaled to what she is in front of, never on command. **The Crown
never solves a plot in any book.** If a scene would be materially harder without it, it is not in that scene.
**The resulting state is the point:** Uratha has every question and no worthiness, Elara has worthiness and
no questions, and the artifact's halves sit in two nations that cannot use it.

**Uratha does not want it back, and that was the wrong frame.** They gave away a dead artifact and it is
still dead for them; a Provost touching it tomorrow gets silence. **What ch13 destroys is the excuse** — the
private century-long position that the thing must be malfunctioning. **So they reinterpret rather than heed,
exactly as their own Paradigm Drift section says they always do:** the new doctrine is that the Crown answers
**Valanar blood**, which is flattering, unfalsifiable, and converts a verdict into a mechanism. **A mechanism
is a research problem, and the subject is Elara.** That is the Merchant drift performing itself in one move,
and it is the same step that built the Globehall.

**Books 4–7 carry it quiet** — access requests, questions slightly too specific, papers taking her as their
subject, an institutional wish to have her observable — **and no Balishan character can read it as anything
but scholarly enthusiasm, because for four books that is all it honestly is.** Balisha also never uses the
Crown as leverage, because leverage requires knowing its worth to the other side and Uratha's secret holds.
**Payoff is Book 8.** Recorded as a cross-book thread in §2.

---

### The Scholar's Crown reads the engine, not the output — settled 2026-08-05

**Authority is `Places/Uratha/Uratha_ The Land of Scholars.md`, *The Paradigm Drift*.** Governing one-line
statement in `Magic/elvandar_magic_system.md`. Full reasoning in the changelog.

**Raised as a two-file conflict and it was four, and the answer was already inside the Uratha file.** Its
opening line said worthiness turns on **contributing novel knowledge**; its own *Paradigm Drift* section says
*"the Crown reads the **engine**, not the **output**"* and cannot be deceived by the appearance of scholarship
when the drive underneath is accumulation. The second is right, it agrees with the magic-system file, and the
first was an older stratum surviving in four places. **Conformed:** `Uratha_ The Land of Scholars.md`,
`Magic/The Divine Artifacts of Elvandar.md`, `Magic/elvandar_magic_system.md`, `Places/Elvandar.md`.

**The novel-knowledge test is Urathan doctrine, it is wrong, and it is kept because it is load-bearing.** It
is why the Provosts respond to the silence by demanding more output — **you cannot pass a test of humility by
trying harder at achievement** — and it is what makes the Globehall look like a solution to the men who built
it, since manufacturing novel knowledge out of harvested minds is a rational answer to the wrong question.
**Do not delete it and do not state it as fact.** It is always what Uratha believes.

**All three divine artifacts test motive, none tests result**, and the Crown was the one entry breaking the
pattern: the Titan's Heart weighs dedication rather than strength attained, the Spirit's Reflection asks
whether you will face your fear rather than whether you are brave.

**Consequence for B3 ch13:** the Crown answers Elara despite her never having contributed a line of
scholarship, because it was never reading that — and refuses a Scholar-King with a library named after him.
**Also corrected in the same pass:** the silence is **nearly a century**, per `elvandar_series_outline.md` and
Book 8, not the *"recent decades"* two files carried. No living Provost has seen it work.

---

### Kaha'an's banking, and why nobody can borrow — settled 2026-08-05

**Authority is `Places/Kaha'an/Kaha'an_ The Desert Crossroads.md`, "Who clears the money, and why they hold
no seat."** Houses in `Places/Kaha'an/houses_of_kahaan.md`; full reasoning in the changelog.

**Kaha'an has a money trade and it holds no political power, on purpose.** The Rending was a mass-default
event: it destroyed the money houses more completely than anyone, because their capital was claims against
estates that had just become desert. **House Umberlow**, the pre-Rending great house, is extinct and is in
the Lost Houses for exactly this reason — it exists to be the answer to *why is there no banker on the
Coterie*.

**Nobody inherited it, and no successor state is to be written as a financial centre.** *(Twice corrected
2026-08-05 on the author's checks — first for saying Vartonne, then for saying Erulius. **Both were the same
error**: a single "banking houses" bullet in a geography file inflated into a claim about where continental
finance lives. The subject invites it; do not reinstate either.)* **Vartonne is a debtor** — declining
currency, endemic noble debt, export terms favouring Kaha'ani buyers. **Erulian wealth is extractive** —
mines, farms, timber, heavy taxation and the conscription system, per its own Economy section and Kalden's
sheet; **the twenty-year credentialing project must never be attributed to banking**, and the Imperial Mark
is a legitimacy instrument, filed on Kalden's sheet beside the Amber Palace and the Hall of Ancestors. **By
Book 7 Erulius is mortgaged to the roots.** **Uratha has no money trade and is not to be given one. Terinok
refuses paper on principle** (*"Thal'krev, thal'zhuum"* — payment in advance), so a Terinok contract must be
funded before it is signed; that constraint bites in Book 7.

**Vessel Street is a bourse, not a house** *(expanded 2026-08-05 on the author's challenge — "so much wealth
flowing through the city, none of it stays there?" The one-house version was the opposite over-correction to
the Vartonne and Erulius errors, and chokepoint finance is always plural: Galata, Antwerp, the Istanbul
sarrafs, the Karimi. Never one house, never small, never seated.)* — a dozen native houses plus resident
foreign factories, with **House Greystone** the oldest and most conservative and no longer the largest.
**The customs lease is the biggest business in the city**: a consortium advances the crown its gate revenue
each year and collects it back at the Golden Gates with a margin. It explains the climbing tolls, it is who
bridges an annual treasury against a daily city, and **it is where the wealth stays**. Still no seat, for a
better reason than portable capital: **plural and substitutable**, ruinable one at a time, impossible to
combine, and bidding against each other for next year's lease.

Greystone clears the Golden Path from Vessel Street and is rich, essential and seatless: the
Coterie seats people who hold things that **cannot be moved**, and a clearing house's capital is portable by
design. Inside the city the credit function was absorbed by the cartels, each lending against the thing it
also sells — already on the page at both ends, in Grain's promissory notes (B2 ch13) and in the debt-bondage
that feeds the Slavers (B1 ch1).

**The load-bearing constraint, and the reason this was worth settling: do not let a character solve a plot
with a loan.** Rosik cannot borrow because he cannot show the books — a lender who opens the accounts finds
the twenty-year insolvency, which is the proof Xion takes in B2 ch13. **Book 7's *he cannot buy an army* is
explained by the money trade, not threatened by it.** Elara cannot borrow because nobody lends to a claimant
on a contested throne, which makes Book 3's empty treasury harder rather than softer. **Book 8 is the first
point at which borrowing is genuinely available**, and the Greystone Factor-Principal is left unnamed
against that.

**Ruled against and do not re-raise: House Kemvimore as bankers.** Pre-Rending Kemvimore extended
agricultural credit — seed against harvest, which is where Rosik's instinct for debt-as-leverage and Book
1's fabricated debts come from — and that is the whole of it. A banking Kemvimore loses on rule 2 (his power
is hunger; the house does not want a second engine) and on rule 1 (*why can't he borrow* becomes
unanswerable). **No prose changed in any book**; the chapters never said there was no bank.

---

### Uratha's rot stays unremarked in B3 ch5 — settled 2026-08-14

**The bakarn is not a Chekhov's gun and must not be written as one.** It is not hidden and is not meant to
be: thirty per cent of the city, its own quarter, named accurately in public by an institution that names a
courtyard for the proof in its paving. **Book 4's power depends on the reader having walked past it exactly
as Xion did**, and Books 4 and 8 hurt in proportion to how much the reader liked Uratha first —
`book4_outline.md` already assumes this in as many words: *"the civilization **that dazzled Xion in Book
3**."* **Uratha's actual gun is the Globehall**, hung at one line in ch5 (*stairs going down, and* some way
*as the answer*) and flagged in that chapter's beat draft as **do not weight it**. That calibration is
correct and is not to be adjusted.

**What was applied:** ch5's Service Quarter gloss is cut — the narration passing sentence on Uratha's moral
character on day two, before the dinner and therefore before the woman refilling the jug, which turned that
discovery into confirmation of a thesis the reader had already been handed. The exchange under it (*"None,"
the escort said. "It isn't a discipline."*) stays and delivers no verdict. **The back-room recognition is
raised** in the same pass, because the answer to *make him wowed rather than analytical* was never to remove
analysis: a white tower is awe any POV character supplies, and the back room at three in the morning running
at midday in an arcade is wonder only Xion can feel. Full record in the changelog and in the ch5 beat draft,
"The verdict paragraph."

**Two standing constraints fall out of this.** **Xion always sees and never concludes** — beat 9's dinner
arithmetic is not negotiable, because a Caretaker who spent eight years in rooms where the person who
mattered was the one nobody looked at cannot be blinded to a servant by scenery; that is a **rule 2 break,
not a fix**. And **do not read ch5's absence of a verdict as a gap** and re-arm the bakarn to fill it. The
constraint is recorded in `book3_chapter_skeleton.md` at the ch5 entry so a later pass meets it there.

**Raised in the same pass, left standing, and reversed by the author within the hour — now CUT.** Ch5's
*"started being impressed in the other way, the one that has a little cold in it"* was the **third** instance
of a drafter instruction reaching the page, after ch4's *"not from a ruin"* and the Hauren-list line. Read in
place it made a stronger case against itself than the transcription did: **it announced the cold before the
evidence, and the section's own last line — *He could not decide whether that was the most impressive thing
he had ever seen or the strangest* — delivers the identical content afterward, earned and unnamed.** The
narration was explaining an ambiguity the prose then went and achieved. **Deleted rather than rephrased**, so
that a redundant sentence did not survive with its provenance merely disguised.

---

### Drafter instructions reaching the page — swept, and the scope is fixed at Book 3+ — settled 2026-08-14

**The defect:** a construction note written *to* the drafter (*this chapter must make X feel Y*, *the reader
should understand Z*, *do not let the prose warm up here*) transcribed into the prose **as narration**, so
the page asserts the intended effect instead of producing it. **Not** shared plot facts, shared imagery,
dialogue, or a draft quoting prose it wants.

**Swept across all thirteen drafted Book 3 chapters on 2026-08-14. Six confirmed; five applied, ch2's kept.**
Full record in the changelog. **ch6's was a different category** — not a transcription but a **breach of a
constraint stated in two places**, this file's skeleton (*"Nobody articulates it, least of all Xion"*) and
the beat draft footer (*"He carries it without naming it"*). **A verdict handed to Xion inside his own head
is the *nobody tells him he has become his father* failure with the messenger removed**, and that equivalence
is now the standing test for this chapter and any like it.

**DO NOT TOUCH — surfaced by this sweep and protected.** ch9's *"They were not a lost people. They were
neighbours"* (the chapter's title, Xion's in-world conclusion, the payoff of four concrete paragraphs) and
ch10's *"They were not exploring any more"* (named in `CLAUDE.md` as the model for the book's ending
rhythm). Both are verbatim against their footers and **both are correct.** *This is the C-6 hazard: a real
pattern pointing at the best sentence in a chapter.* **ch2's Farleen gloss is also a keep**, on the author's
ruling — it is Xion reading a face, which is his instrument and rule 0 working as designed.

**The scope rule, and it is structural rather than a matter of effort.** **Books 1 and 2 are permanently out
of scope.** Their beat drafts are derived *from* the prose, so a match proves nothing — *a draft written by
reading a chapter records why the chapter works, which is craft commentary, which is instruction.* The
defect is only diagnosable where the draft precedes the page. **Book 3 onward, and run per book while it is
being drafted, not retrospectively.**

**The upstream fix already exists and is working.** The 2026-08-02 instruction/body separation sweep moved
instructions out of numbered beats into footers across all 64 drafts. Ch7, ch11 and ch13 came back clean,
and **ch7 dodges the trap at its most exposed point** — its draft carries the ch4 shape verbatim (*"They are
not standing at the entrance to a ruin"*) and the prose never uses the word. **The two rules are a pair:
keep instructions out of beat bodies, then check the page for what got through anyway.**

---

### The beat-body exceptions are settled — do not re-flag them a third time — 2026-08-14

**The 2026-08-02 instruction/body rule has two recorded exceptions, and they are not oversights.** **Negative
choices** (a character visibly not doing something) are events and stay in beat bodies. **Effect analysis** (a
statement about what a beat achieves) is not an order and stays. That entry closed with *"the distinction is
recorded because a future sweep will want to take them too."*

**On 2026-08-14 a sweep of ch14–21 returned about sixty items, and the great majority were exactly those two
exceptions.** Every high-signal item was probed against the 08-02 commit and found **already present when
that sweep finished** — nothing had reaccumulated; they had been deliberately left. **All declined.** If a
future audit surfaces *"the reader sees…"* statements, *"not snobbery"*-shaped negations, or *"this is
important"* emphases inside Book 3 beat bodies, **that is this ruling, not a finding.**

**What *was* real in the same audit is the POV half**, which 08-02 was not hunting — its own record describes
the catch in the singular. **Nine unstageable beats fixed** across ch16–ch21, and the diagnostic that found
them is worth keeping: **look for a footer stating a constraint and the beat under it breaking that same
constraint.** Ch17's footer had contradicted itself (*"None of that is available to the narration"* closing on
*"The beat ends on the report being filed"* — in Vartonne), which is precisely why that beat survived the
first sweep. **A footer at war with its own beat is a bug, not a second opinion.**

### Ondra Kelgrav chairs the Consortium — CLOSED, resolved against canon 2026-08-14

**She is the Chair.** Authority is `Places/Gunastran/Gunastran_ The Land of Magi-Tech.md` (*"Current Consortium
Chair, Master Engineer Ondra Kelgrav… she chairs Book 3's vote for war"*) plus the dated 2026-08-01 ruling that
retired **Veldrin Torkal** from canon. B3 ch14's draft contradicted itself in three places — beat 3's *"not its
chair"* and a separate male chair in beats 4 and 15 — all residue from before that ruling, now conformed.
**Beat 15's tension survives the fix:** an engineer being asked to cross into policy, with the question coming
from the table and her chairing made part of the difficulty rather than a contradiction of it. *Do not
reintroduce a second chair, and do not restore Torkal.*

### Bittek gets a sheet after all — and the test for who does is not book-span — 2026-08-14

**`People/Bittek.md` exists. I argued against it twice and was wrong twice, on the same underlying
error.** The author's argument decided it and is worth preserving in his own terms.

**The reasoning I gave was that "sheets exist to stop drift *between books*" and Bittek appears in one.** That
sentence is in `CLAUDE.md`, and it is a statement of **what guardrails do**, not a rule about who qualifies
for a file. **I turned a purpose statement into an eligibility criterion** — which is precisely the error
recorded two entries below about villains and greyness, and the one `CLAUDE.md` §3 already documents about
paradigm primaries. **Three instances in one session, all the same shape: a description read as a rule.**
The tell is identical every time — a constraint that cannot be quoted from any file.

**The author's first argument was the precedent: Melina Kemvimore.** She is introduced, developed and killed
inside Book 2, and carries a 222-line sheet while her presence in Book 2's beat drafts is scattered plot
mentions. *(Checked. The register does list her as 2–8, since she is load-bearing as a wound long after she
dies, so the precedent is not quite the pure one-book case — but that distinction does not rescue my
position, it undermines it further: what her sheet demonstrates is that **the sheet is where characterization
lives regardless of span.**)*

**The second argument is the one that actually decides it, and it was drawn from my own text.** The outline
had come to contain the sentence *"This is a constraint on how to write his restraint, not a beat."*
**An outline is a document of beats and structure.** A line inside it announcing that it is not a beat is a
line advertising that it is in the wrong file. Because I had ruled out the document designed for
characterization, the outline had been absorbing characterization it is not shaped to hold — a stack, a
psychology, five behavioural rules.

**And I had the one-source principle backwards.** *"One source, and everything else points at it"* means pick
the right home and point at it from elsewhere; it does not mean refuse to create the right home. The outline
already does this correctly for Ronas — *"the constraint on Ronas's last line is on his own sheet."* I cited
the principle as a reason not to make a file, which inverts it.

**The rule is the author's and is now in `CLAUDE.md` §6, where both document types are defined.** *"Beat
drafts are for recording story beats, not characterization. If you find yourself recording characterization
in a beat draft, that is a sign the character needs to be moved to a dedicated sheet."* Who qualifies is
decided by **whether the characterization matters** — unnamed walk-ons never, role-fillers usually not,
anyone important enough to crystallize or important enough that the planning documents have started
enforcing it, yes. **Span is not the criterion.**

**His formulation is better than the one I offered and the improvement is specific: mine was descriptive and
his is diagnostic.** Saying "sheets hold who someone is" tells you how to file things you already recognise.
Saying "characterization appearing in a beat draft is the signal" tells you **when to act**, using a symptom
you can actually notice while working — which is what caught this one.

**One refinement recorded with it: the leak is originating, not referencing.** A beat draft citing an
established stack to justify a beat is correct and expected. The failure is a planning document being the
**only** place a character's characterization exists. **Swept the same day: nine planning documents across
Books 1, 2, 3, 6 and 7 reference paradigm stacks, and every one was pointing at a sheet.** Bittek was the sole
anomaly, and only because there was no sheet to point at.

**What moved and what stayed.** The outline keeps the two architectural rules — *specimen never source* and
*he never touches the child* — because both are constraints on the book's shape rather than on the man, plus
his placement in each act and what happens. Everything else moved. **The sheet is deliberately short**, and
says so: padding it would be the first symptom of the drift its own first guardrail exists to prevent.

---

### B6-1 CLOSED — Garrin named, and Bittek's Book 2 position settled — 2026-08-14

**The capable lieutenant is *Garrin*, one name.** Warrens figures in `Names.md` overwhelmingly carry a single
name, and the closest analogue is exact: *Cullen* is Ronas's other named lieutenant. Coinage note in
`Names.md`, including why *Corran* — the better-sounding candidate — was disqualified **on sound rather than
spelling**, since a hard /k/ onset would have been the fourth in a book already carrying Kess, Kai and Kael.

**And Bittek was present in Book 2 but not among the lieutenants who ran wild.** *(The outline's "twenty years"
already committed him to being in the organisation; this settles what he did.)*

**The reason the alternative was dropped is worth keeping, because it was offered as an upside and wasn't
one.** Making Bittek one of the wild ones was floated as a payoff — Melina Kemvimore's *"they're not like him,
they're worse"* turning out to be partly about him. **That payoff cannot exist.** It requires the reader to
recognise someone, and **Book 2's prose never individuates a single one of Ronas's lieutenants** — they are a
pure category, verified by search. There is nobody there to recognise, so the "connection" would have been a
fact with no reader-facing surface at all: exactly the trivia `Offstage.md`'s third test is designed to
reject.

**What replaced it is better and is the opposite of it.** Bittek's only governor is fear of the man who
punishes him, and in Book 2 **Ronas was still standing** — and demonstrated it by executing the lieutenant
who murdered Melina Kemvimore, immediately, to re-establish control. So Bittek stayed in line, and **the one
who stayed in line is the one who spent twenty years storing it up.** This supplies the *specific* execution
behind the author's own formulation that his restraint comes from having "literally seen it happen to other
lieutenants" — Book 2 already had the instance, so Book 6 does not invent one.

**It lives in the outline's Act I as a constraint on how to write his restraint, not as a beat.** No character
refers to it and the reader never needs it dated. **This is also the answer to where backstory goes when a
character has no sheet:** if it changes how a scene is written, it goes in the outline beside the scene; if it
changes nothing, it is trivia and goes nowhere.

---

### There is no rule requiring villains to be grey — and one was invented and then excepted from — 2026-08-14

**A guardrail written for Book 6's Bittek called him "a deliberate exception to the series'
characterization standard." No such standard exists.** A search of the entire repository for any rule
requiring an antagonist to be sympathetic, morally grey, or possessed of redeeming features returns nothing.
The author challenged the claim directly — *"where is it written?"* — and the answer was nowhere.

**What produced it is worth more than the correction.** The author's own observation, made while pitching the
character — *every major villain here is a study in shades of gray* — is a **description of what has been
written**. It was read as a **constraint on what may be written**, and a dispensation was then drafted against
a rule that had never existed. **The dispensation is the worse half**, because granting an exception implies
the rule is real and leaves it standing for the next reader.

**This is the failure `CLAUDE.md` §3 already documents, one level up.** That entry warns against "reading a
primary as an obligation, then reporting the derived constraint as though it were a property of the
character," and records that it cost a full exchange over Melina Valanar. The same move applied to a *pattern*
rather than a stack produces the same result. **Descriptions of the corpus are not rules governing it**, and
the tell is identical in both cases: a constraint that cannot be quoted from any file.

**The framework provides for characters like Bittek rather than tolerating them.** `The Seven Paradigms.md`
carries the Joffrey Baratheon Counterpoint as a worked example of the exact type — Merchant primary with
nothing balancing it, Spirited Competitor near-zero, *"wants the opposition disarmed first"* — presented as a
legitimate reading of a person. `CLAUDE.md` adds that the stack is for validating decisions rather than
generating them, that it "is not a straitjacket," and that the test which catches a rule 2 violation is
**does the text charge them for it**. Bittek never acts against his stack, so the test barely engages.

**The guardrail now reads as a design instruction — *he is complete as designed, do not deepen him later***
— which is the thing actually worth protecting: a future pass noticing he reads thin beside Rosik, Ronas and
Kalden, and trying to help.

---

### Tiberian kills Ronas Dermir — AUTHOR'S RULING, 2026-08-14

**Tiberian Valanar kills the Slaver King personally, in Book 6, after offering him one last chance to stand
down.** Ronas refuses: he would rather die as the Slaver King than live as king of nothing.

**This had never been written down anywhere, and the author believed it had.** Checked before recording, and
the finding is worth keeping because it is the reassuring answer rather than the alarming one: `book6_outline.md`
said only that "the crown moves against him" and that "he goes down swinging," `Offstage.md` said "when Ronas
went down," and neither sheet named a hand. **A search of every commit in the repository's history returns
nothing** — so it was never recorded and lost, it was simply never recorded. **Nothing is wrong with the
archive; the ruling was living in one head.** That is precisely the gap `Offstage.md` and this section exist
to close, and the lesson is that a *fate* is exactly the kind of fact that feels too settled to write down.

**Recorded in four places:** `book6_outline.md` (Act III and the structural note), `People/Ronas Dermir.md`
(a new death section under the voice lock), and `People/Tiberian Valanar.md` (his Book 6 entry).

**The offer is load-bearing and is not a courtesy.** Ronas is the only man in the Warrens who could actually
*deliver* a stand-down, so extending it is sound practice as well as characterization. **The consequence to
protect: anyone refused later is being refused a negotiation, not the mercy Ronas was given** — because they
control nothing and can deliver nothing. Keep that asymmetry visible or the later refusal reads as
inconsistency in Tiberian rather than as characterization of whoever is begging.

**And Ronas's last line is the highest-risk sentence in Book 6 for register drift.** His voice is locked, and
his sheet names the exact failure mode: the drift always happens in his longest and most serious speeches,
because the temptation is to let him speak "properly" when the content is grave. **A balanced antithetical
epigram is the wrong instrument**, however well it states the sentiment — the register wants dropped
auxiliaries, *ain't*, *got*, and the historical present. The Grand Hunt speech is the one licensed rise and
is explicitly not licence for this one.

---

### B3-1 — CLOSED. The Hauren arc is written, and its three constraints held — 2026-08-14

**The entry was stale and had been for eight days.** It read *"prose exists for ch1–10; `Chapter 11 - The
Destiny Engine` not started"*, and was found during the ch10/ch11 retitle: ch11 drafted 2026-08-06, ch12 the
same week, ch13 on 2026-08-13. **Prose exists for ch1–13 and the next chapter is ch14 `Ruthless Calculus`.**
This is the failure mode §5 of `CLAUDE.md` names by name — a flag that outlives its problem — and it survived
because nothing in the drafting loop goes back to the status block when a chapter lands. **Update the status
block in the same commit as the chapter, not afterward.**

**The three Hauren constraints are preserved here because they bind again in Book 7**, when the series
returns to the city (`Book 3 - Crown Jewel/_HAUREN_AFTER.md`). **Nothing in the city is damaged or
declining** — the Haureni closed the house and walked out, and any beat implying decay argues against the
bequest framing. **Nothing may date the city before the characters date it** — three narration lines were cut
for asserting *twenty years* ahead of the discovery, and the seal date of two thousand years is a number no
character can ever have. **Elara does not read** — impressions only; the scholars' shift from *what does this
say* to *is this important* is the political seed. All three held across ch7–ch11 as written.

---

### B3 ch10 and ch11 retitled — `Bequest` and `Time` — author's ruling, 2026-08-14

**The old titles were `The Repository` and `The Destiny Engine`, and both named the room rather than the
chapter.** The author raised them as too straightforward and proposed both replacements; both were adopted
whole. **No prose changed in either chapter** — the room is still called the Repository in the text, which is
correct, because the scholars derive that name from Crown-level cross-references and use it in front of the
reader.

**The load-bearing reason, and the one to keep: *Destiny Engine* is not a name the book has.** The prose calls
it *the Engine*, and *Destiny Engine* appears in **zero chapters of any book** — it lives in the canon files
(`Magic/`, `Places/Kaha'an/`, `People/Elara's Connection to Hauren.md`, the Book 8 outline) and in the
skeleton. Putting it on a chapter made the one place a workshop label leaked onto the page, and it leaked
against the standing rule that no Haureni proper name is used by any character or by the narrator in
Xion's POV. **The artifact keeps the name in the canon files; the chapter does not carry it.**

**What each title is doing.** `Bequest` is the word the ch10 draft says the chapter reaches for and cannot
hold — *"The Repository is not a library. It is a bequest. She does not use that word; she does not have to"*
— so the title is the one sanctioned place to say it, and it pays off in the closing image of a woman standing
in a house left to her. `Time` is staked in the chapter: it is one of Ormuth's four words off the wall
(*Seal. Threshold. Time.* — *Necessary*), and the chapter is metronomed by it end to end, from *made this in
months* to *they had months* to the three-second count in the last line. The pair reads as what they left and
what it cost.

**A title family now exists and is intentional:** B2 ch16 `Disinheritance`, B3 ch2 `Inheritance`, B3 ch10
`Bequest` — cast out of it, born to it and unable to use it, deliberately left by the dead. Ch11 reveals the
second and third are the same thing. **Do not add a fourth without a reason.**

**Runner-up, recorded so it is not re-proposed as new:** `Necessary`, Ormuth's fourth word. More distinctive
on a contents page, and there is house form for titling on a spoken word (B2's `Don't.`), but it aims at one
beat where `Time` covers the whole spend, and it breaks the diptych.

---

### Book 3's renumbering makes chapter numbers unsafe in the record — 2026-08-14

**`Fair Price` inserted as ch6 (2026-08-03) and `Inhabitants` split at the Rending seam (2026-08-04) shifted
every chapter below by two.** Editorial entries written before those dates name chapters that are now two
higher. The 08-02 sweep section in the changelog has been annotated with a full title mapping rather than
rewritten, since it is append-only history. **Titles are the stable identity; numbers are not.** Four stale
cross-references were already found inside ch13's own draft from the same cause. **When citing a Book 3 chapter
in any editorial document, give the title.**

**The residue itself is CLOSED.** ch15 `The Proposal` was the only draft carrying stale references to *other*
chapters — four corrected on 2026-08-14, three others in the same file left standing because they were already
right. **Every Book 3 draft was then scanned for the class and is clean**; the apparent hits elsewhere are
footers discussing their own chapter by number, which is correct usage. **The lesson worth keeping is the
method, not the count: check each reference against the chapter it names, never shift a file by a fixed
amount.** ch15 had been updated unevenly — some references short by one, some by two — so a blanket +2 would
have broken the three that were correct. **Where a number is genuinely ambiguous, make the reference
descriptive** (*"the irony this chapter runs on"*) rather than renumbering it, so it cannot go stale again.

**Amended 2026-08-14: titles are the *more* stable identity, not a permanent one.** Ch10 and ch11 were
retitled the same day, which means editorial entries written before it name `The Repository` and `The Destiny
Engine` for chapters now called `Bequest` and `Time`. **Both old titles are also room-and-artifact names that
remain correct in the prose and the canon files**, so a search for either will return live, valid hits that
must not be "corrected" — check whether a reference means the chapter or the thing before changing it. The
append-only changelog entries predating the rename were left standing, as with the renumbering.

---

### The next-generation chronology is compressed to its causal minimum — author's ruling, 2026-08-20

**Tiberian and Melina are sixteen when Book 5 opens, shortly after their birthday.** Book 5 spans several
months and they remain sixteen throughout. Book 6 follows without a discretionary inter-book gap and spans
approximately **eighteen months**; the twins enter before or around seventeen and leave at about eighteen.
Book 7 follows promptly, while they are approximately eighteen, because the accelerating Warrens relocation
is destroying Rosik's remaining Kaha'an base and gives him no reason to wait.

**Eighteen months is the minimum Book 6 can bear.** The Green Cities already exist — Book 5 funds them as
food security — so Book 6 is not buying three years of construction. It is buying surveys, conversion and
staffing, staged food and water, dependency mapping, and transitional order for sixty thousand people. A
year could still read as responsible speed at that scale. Eighteen months allows the necessary work to be
real and the final refinements to become indefensible. The delay remains the antagonist; the old three-year
ruling is superseded.

**The twins are conceived only after the Compact War.** Xion and Elara wait until victory before trying for
children; the birth occurs roughly nine months later and remains offstage. Book 4 stays entirely Harkim's and
does not acquire a Valanar-family scene to show it.

**Governing chronology principle:** spend only the time causality requires. Unassigned time remains available
for later books; no ambient year is inserted merely to make characters look older. Expansion can be added if
a drafted story eventually requires it. Compression creates larger downstream age and continuity costs.

### Melina Valanar has no pre-series intelligence masterpiece — author's ruling, 2026-08-20

**The Erulian Network Collapse, seventeen turned agents, and the honeypot are deleted, not relocated.** A
repository-wide check found every reference on Melina's own sheet and nowhere in an outline, timeline,
offstage account, or chapter. The event was self-referential résumé inflation: it existed to prove the
competence the sheet asserted and no story depended on it.

**The techniques remain available without the event.** Melina may analyze intelligence, turn an agent, feed
an adversary a false picture, or build a trap if a later scene actually requires one. None is a named past
achievement or a preserved future appointment. Her reputation is earned on the page through Silaris, the
Warrens plan and collapse, and the partial-information decision that catches Rosik in Book 7. Moving the
operation between Books 6 and 7 was rejected because that interval is deliberately short and Rosik's clock
requires it to be; preserving an unneeded event there would spend chronology to maintain a résumé.

### Rosik is 44 in Book 1 and approximately 64 in Book 7 — author's ruling, 2026-08-20

**This is the youngest chronology his established life can bear.** Melina Kemvimore is 26 in Book 1, so
Rosik fathered her at eighteen; he fathered Xion at twenty-one and was twenty-four at the Rending. His first
life is correspondingly precocious and explicit: raised inside the Long Knives, trained from childhood,
operational in his early teens, one of their premier killers by sixteen or seventeen, married into House
Kemvimore by seventeen. Any younger collapses the assassin career, failed Kemvimore assignment, defection,
manufactured noble identity, marriage and Melina's birth into an interval the characterization cannot carry.

**Book 7 is the reason the old age anchor had to move.** The compressed next-generation chronology places
the book roughly twenty years after Book 1. Preserving 58 would make Rosik approximately 78, old enough that
an intelligent former assassin should regard personal infiltration of Kaha'an as fantasy before he begins.
At approximately 64, still lean, practiced and exceptionally trained, he can honestly judge that a thinned,
modelled route is within him while also knowing that an alert palace, or four seconds with Kess, is not.
His plan remains sound. The irrational act is proceeding after Kalden's body collapses the distraction.

**Duration language follows the new anchor.** Book 7's thirty-year network and dormant-skill references are
now an adult lifetime and most of half a century. Book 2 ch15's prose — a line Rosik had spent thirty years
never crossing — remains: his operational life began in early adolescence, so the rounded duration still
holds. No chapter prose changed.

### Kalden inherits at fifteen and is 35 at the series opening — author's ruling, 2026-08-20

**Kalden is born around 1009 BR, succeeds his father at fifteen a few months before the Rending, and is
thirty-five when Book 1 opens.** His father dies after an illness. The Erulian High Council confirms
the succession without appointing a regent, and the mature government his father left behind continues the
ordinary work: experienced ministers, functioning offices, reliable revenues and a state that is already
stable. Kalden's first task is preservation, not construction.

**The Rending turns inherited trivia into the project of his life.** His father had raised him on the vague
family story that the founder of House Erulius had been blood kin to a Valanar emperor. When the
fifteen-year-old hears that the emperor and empress are presumed dead, no heir is known and Kaha'an is in
disarray, he searches the archives and reconstructs the exact history: the first Lord Erulius was a historic
Valanar emperor's third cousin twice removed, on the emperor's mother's side, through a distant shared
ancestor. This is collateral kinship, **not descent from a Valanar cadet branch.** His youth is causal rather
than incidental: the brash new prince first wants to go to Kaha'an and announce the claim; when his ministers
explain why that would fail, he listens and asks how they can make it possible.

**Do not transfer either man's work to the other.** The sound pre-Rending state belongs to Kalden's father.
The real Chancellery, military reforms, diplomatic network, infrastructure and administrative competence
Kalden develops across the next twenty years belong to Kalden. At the series opening he is not an untested
boy; he is a thirty-five-year-old ruler who has spent most of his life learning to operate and extend the
machine he inherited. He is approximately thirty-six in Book 3 and fifty-five in Book 7.

The duration correction has two clocks. Kalden's imperial self-narrative runs from the Rending to Book 7
and is about **forty years**. His imaginary war with Xion begins only after Elara chooses Xion in Book 3
and lasts **nearly twenty years**. Old thirty-year wording for either clock is superseded.

**The legal campaign is the good plan, and it is winning when Elara appears.** At fifteen Kalden has found
only a chance. In his twenties the claim stops sounding ridiculous; around thirty Erulius becomes a serious
candidate in any reopened succession; at thirty-five, absent a surviving Valanar, he has a phenomenal chance
of eventually reaching the Ruby Throne and can finally *taste* it. The succession has been deferred rather
than decided against him. His functional institutions, diplomatic network, imperial credentialing and
Secessionist Fringe have made his name the unavoidable answer whenever Kaha'an discusses reopening it. The
faction remains marginal and lacks direct authority over Rosik, Tania or Sa Ko, but that is a limitation of
an effective campaign, not evidence of twenty years of futility.

**Elara ends that viable route without wronging him.** Her return is catastrophic luck for Kalden and the
succession system functioning correctly at the same time. The news deliberately mirrors the Rending: at
fifteen he hears public tragedy and discovers private possibility; at thirty-five a joyful messenger brings
public hope and Kalden hears private catastrophe. His immediate assassination order is the Merchant wound —
an acquisition assembled for twenty years has become unavailable — overrunning Engineer patience; Founder
language is the dignified account he gives himself afterward. The Book 3 marriage proposal is the one
intelligent recovery: self-serving, geopolitically strong, and plausibly the expected dynastic choice for a
conventionally raised Elara. Her rejection makes the grievance personal and makes Xion useful as rival and,
later, scapegoat.

**The delusion is refusal to update, not the original ambition.** Kalden is competent for twenty years and
his competence improves his odds. Initially rational credentialing becomes self-mythologizing only after
Elara removes its political purpose; after the Compact War, preserving the symbols while the state collapses
becomes pure fixation. Elara is the terrible luck. Attempted regicide, war, fiscal collapse, secession and
the final mercenary effort are increasingly consequence. Reality repeatedly gives Kalden exits, and he
recodes every exit as persecution. The reader must be able to total the account; Kalden never may.

No chapter prose, beat draft or Royal Road HTML changed. The existing Book 2 chapter about Kalden remains
fully consistent: its twenty years of patience are precisely the years between his accession and Elara's
arrival.

**Height and calibration — author's ruling, 2026-08-21.** Kalden stands **5′11″ / 180 cm** at thirty-five,
the same measured height as Xion and Elara. The choice is conventional rather than symbolic: he is neither
notably short nor notably tall. His approved early-series identity model has been placed in the common
armorer's fitting room with flat-soled boots, heels on the brass baseline and crown aligned to the 5′11″
standard. The written measurement governs over any apparent variation in generative perspective.

**Character-art archive — reorganized 2026-08-21.** The flat image directory is superseded by a purpose-led
archive under `Character Art/`: approved reference models (height calibration, photorealistic, illustrated,
and group references), scenes, explicitly non-canon alternate universes, and retained drafts. The tracked
`Character Art/README.md` is the visual index and establishes the reuse order: calibration plates are the
primary “T-pose” models; photorealistic solos and group references supplement identity and relative scale;
scenes are not default model sheets; alternate-universe art never establishes canon. All forty-four raster
assets present at migration were preserved. Art remains downstream of this physical-characteristics ledger.

---

### Elvandar is the continent, and the prose may name it — settled 2026-08-29

**The world has no name; the continent is Elvandar.** `Places/Elvandar.md` is explicit and repeated — *"the
continent of Elvandar,"* *"the Balishan Empire spanned the entirety of Elvandar"* — and `Magic/The Rending.md`
calls it *"an entire continent."* The Hauren rename did not touch the referent.

**So naming the continent in prose is allowed, and the §6 rule that said otherwise was stale.** It claimed
*"`Elvandar` appears in **zero** chapters,"* which stopped being true at `da80f25`, and it reasoned from
*"people rarely name their own world out loud"* — treating the continent's name as the world's. Acting on it,
Ronas's *"Only man in Elvandar can give you that clause and mean it"* (B3 ch6) was proposed for rewriting.
**The prose stands.** It is the same continental-scope construction the books already use freely: *"one nation
on the continent"* (ch5), *"the best-read men on the continent"* (ch8), *"no arrangement of facts on the
continent"* (ch10).

**What remains banned is intensifier duty**, for either word — *"every reason on earth"*, cut from B3 ch7 on
2026-08-03, because it borrows a planet-name this world does not have. Say *the world*, or cut the intensifier.
**Do not re-flag Ronas's line.**

*This is the C-6 failure mode with a different flag: a rule whose factual premise expired, trusted by the next
reader, aimed at good material. The rule was corrected in `CLAUDE.md` and `AGENTS.md` rather than the chapter.*

---

### B3 ch10 conformed to the locked chronology — the last de-aging survival — 2026-08-29

**Elara was an infant at the Rending, not nine.** ch10 read *"nine years old and asleep in a compound on the
surface twenty years ago, and before that she had been a child in a palace"* — wrong in age, wrong in place,
and inverted in sequence. `Story Timeline.md` locks her at **20** in Book 1, *"Infant at the Rending,"* and the
ch11 beat draft has her as *"a six-month-old infant"* in the Ruby Palace cradle. Canon is **palace at the
Rending, compound afterward.**

**It was load-bearing.** Her connection to Hauren exists because she was an infant in the palace when the
Engine fired; ch10, ch11 and ch13 all rest on it. Corrected under the author's standing ruling that **where
ages conflict, the younger reading wins.** The new line stops short of the Ruby Palace cradle, which is ch11's
reveal and cannot arrive a chapter early.

**Swept for siblings and clean.** The remaining *"N years old"* instances across Books 1–3 are all correct:
Tam at twelve (ch12/14/16, consistent), Xion *"since he was nine years old"* (backstory), the sixty-nine-year-old
Aspirant Guard in `Offstage.md`, and *"a population figure eleven years old"*, already ruled correct on
2026-08-03. No other survival of the older chronology remains in the prose.

---

## 7. Open questions

**One language-history foundation is open:** the founding date and local population of Urath IV's academy.
Urathan's genealogy, Balishan's deeper Halauric ancestry, Vartonne's settlement history, Valan I Valanar's
founding dynasty and coalition, and the ordinary distinction between Balisha and its capital are settled.
The open foundation is described in
`Languages/Urathan.md` and `Languages/Ethnolinguistic History.md`; it is a design question rather than an
error in prose.

**Previously open items remain closed.** The three items opened on 2026-08-02 were all ruled on the same day
and are recorded in the changelog: the birthdays are pinned (`Story Timeline.md`), the Mistress's relation
to Xion is canon and not a thread, and Book 4 has no relay.

**And the 2026-08-05 banking and Brass Door work closed everything it opened, the same day.** Prose: B3 ch1's
borrowing beat and the customs refusal, ch4's Gunastran answer, ch6's exclusivity clause. Canon rulings in
§6: the Crown's worthiness test, what the Crown gives Elara and what Uratha does after ch13, Hauren as
collateral, Elara never selling the gate, and who held Kalden's mortgages.

**Numbering warning, kept because it caused a real misreport.** This section was once numbered 1–4
while the closed-items list used a separate Q1/Q2/Q3 scheme for different items, and three
already-closed questions were still sitting under the heading "Open questions". A reader trusted the
list rather than the drafts and reported *"Janice's failing eyesight — confirm or veto"* to the author
as live. It was not. **Do not reintroduce a parallel numbering, and do not leave closed questions
under this heading.** Refer to questions by subject.

---

## 8. Observations that are not fixes

- **Elara appears in one chapter of Book 2's twenty.** Thematically motivated — the institution separating them at the start still separates them at the end — but a reader who came for Book 1's partnership gets almost none of it. Worth holding consciously.
- **Book 1's prose is the weaker half of the series by a wide margin.** Book 2 reads as though rules 1–3 were held firmly throughout; B2 ch5 works precisely because nobody is bent to make it work.
- **The plot proves its own thesis in Book 1** — Xion doesn't rescue Tam; eight years of free medicine do, through Korvin, a vendor, a Slaver's cousin, and Varris's leg.

---

*`TGMS - OLD/` is non-canon and is excluded from all continuity checks.*

*Applied changes: `Series Review - Changelog.md`.*
