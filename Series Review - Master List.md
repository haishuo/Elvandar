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
| **Book 3 — in draft** | 2 | ch6 beat draft in progress; `_WORKING_NOTES.md` to salvage and delete |
| **Open questions** | 0 | — |

**Nothing outstanding in either finished book.** Every item ever filed against Books 1 and 2 is closed,
withdrawn, or applied. Book 3 is live work rather than review findings — see [§3](#3-outstanding-work).

**Book 3 is 20 chapters as of 2026-08-03**, not 19. `Chapter 6 - Fair Price` was inserted between
*Hubris* and *Wonder* to carry the return from Uratha and the purchase of a supply line into the Warrens;
everything from *Wonder* down shifted by one, and *Wonder* is now **ch7**. Prose exists for ch1–5 and ch7.

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

**Where the work happens, from 2026-08-03; relocated 2026-08-04.** Drafting runs in the worktree at
`../Elvandar-worktrees/book3-prose` on branch `book3-prose`; `main` holds finished work. The author reads
progress through **Elvandar Viewer** (`Tools/elvandar_viewer`), which is worktree-aware — verified against
its own `GitClient`: it resolves `--absolute-git-dir` and `--git-common-dir` separately, so its live-update
watcher follows a worktree's metadata correctly rather than looking for a `.git` folder that isn't there.

**The worktree lives outside the repository, and that is not cosmetic.** It sat at
`.claude/worktrees/book3-prose` for one day and cost most of a session, because the Viewer's own
`repository.py` carries `.claude` in `IGNORED_NAMES` *and* filters every dotted name, and Finder hides
dot-directories too. Six commits — the emphasis pass, the *earth* and *Gods* fixes, `Names.md` — were
pushed to a folder the author's reader is built never to display, and he was told to go and read them
there. **The exclusion is correct and the placement was wrong.** A worktree the author cannot open is
worse than no worktree, because the work looks done from this side and does not exist from his. Any future
worktree goes in a visible sibling directory, never inside the repo and never under a dotted path.

**Two disciplines, and they exist because both failed on 2026-08-03.** **Push after every commit**, because
fifteen commits once sat unpushed through four rounds of revision and the author was giving notes on a
chapter he could not read. And **merge to main and delete or re-sync the worktree the moment a chapter is
done**, because a stale worktree left a second copy of the book on disk showing the previous day's state —
no ch6 at all, *Wonder* still numbered ch6 — and it was opened and read as current. **A worktree that has
outlived its purpose is not clutter; it is a wrong copy of the book with an equal claim to being real.**

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
- **A beat draft's body is the page.** The numbered beats are what happens; instructions to the drafter go around them, never inside them. Full statement of the rule and its provenance in `Templates/Beat Draft Template.md`; the sweep that applied it across all 64 drafts is in the changelog under 2026-08-02.

---

## 2. Cross-book threads

These are the spine. Each is already working; each could be broken by an unwary revision.

**The hands.** B1 ch1 "The Healer's Hands" (tweezing glass, washing blood away) → B2 ch13 "Clean Hands" (*"he had just spent a night being him to the letter, and the proof was there at the ends of his own wrists, unmarked"*) → B2 ch17 (he takes his own pulse, finds it steady, and cannot make the diagnosis land on himself).

*(A fourth instance was written into B3 ch4's closing beat on 2026-08-02 — *"an interesting thing to feel in a room, at a table, with clean hands"* — and cleared here on the argument that it inverted the image rather than repeating it. **The whole closing beat was then cut the same day** as summary, and the fourth instance went with it. **Three remains the shape**, and the standing note stands: do not add a fourth without a reason written down here first.)*

**Frozen silence → chosen silence.** B1 ch1: rooted to the paving stones while Tam is taken, because acting means saying his own name. → B1 ch8: Elara asks him at the gate why he didn't, and *"nothing came out of it. The same nothing, arriving in the same order."* → B1 ch19: Farleen argues him down a maze in five stages and he answers none of them. → B2 ch16: he refuses Rosik the argument, and the text distinguishes the two explicitly. **This is the arc, and it spans two books.** Book 1 not closing it is correct.

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

**Melina works it out.** Nobody tells her; she is Truth Seeker primary with a lifetime of mapping gaps, and **the evidence is the alias.** Her father spent eight years publicly calling himself *Master Fen*, and a daughter patient enough to ask whose surname that was has a trail at the other end: Rosik executed a servant in front of witnesses, and B1 ch22 has Xion learning the details *"in pieces, from people who'd been standing in the room."* Some of them are alive twenty years later. The memorial was hidden in plain sight for two decades and one person read it.

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

**The Mistress's standing invitation — opened B1 ch21, answered B3 ch2, and still not paid.** She ends
the Book 1 scene with *"when you take the throne — and you will — if you ever figure out what you are,
find me. We should talk."* B3 ch2 is Elara arriving without the answer, and the Mistress trades anyway:
**whatever is behind the Brass Door, she hears it from Elara directly, before the court and before it is
written anywhere.** That promise is now load-bearing in two directions. It is why the Long Knives permit a
camp in the chamber they have guarded for generations, which is what ch6's expedition and ch9's exit both
sit on top of. And it is a debt with a due date: **the moment Lathion is opened, Elara owes her a briefing
ahead of her own court**, and nothing yet written shows her paying it. Do not quietly drop it, and do not
let the ch6 wonder chapter carry the payment — that scene takes one emotion.

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

**B3-1 — `Chapter 8 - Inhabitants` and `Chapter 9 - Neighbours` are drafted and written; prose for
`Chapter 10 - The Repository` not started.** The two were one 7,400-word chapter until 2026-08-04 and
were split at the seam after the Rending exchange — *"The number did not move."* Act II now runs
3,050 / 4,590 / 2,810, which is the shape a wonder sequence wants rather than one short chapter and one
outsized one. Book 3 is **21 chapters**.

Three things the remaining Lathion chapters must hold. **Nothing in the city is damaged or declining** —
the Lathionese closed the house and walked out, and any beat implying decay argues against the bequest
framing. **Nothing may date the city before the characters date it**: three separate narration lines had
to be cut for asserting *twenty years* ahead of the discovery, and the seal date of two thousand years is
a number no character can ever have. **Elara does not read** — impressions only, and the scholars' shift
from *what does this say* to *is this important* is the political seed.

**B3-2 — two threads inherited from `_WORKING_NOTES.md`, which was salvaged and deleted 2026-08-04.**

- **The Places-vs-map audit is unfinished.** All `Places/` files were being rewritten to match the
  canonical painted map (`Places/elvandar_map_painted.png`). The Erulian file is corrected — Erulius
  sits far southeast on the Azure Sea and does **not** border Vartonne. **The other nations were never
  checked**, and nothing else records that the job was left half-done.
- **Draskin's description in `Chapter 4 - Negotiations` may contradict `Hubris` and `The Scholar's
  Crown`.** Flagged when those chapters were drafted and never resolved. Check before Act III drafting
  reaches him.

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

**Grain was Rosik's leash on Ronas, and it is the only thing that could have been.** The leash is
everywhere in canon as language — *attack dog*, *a trained dog barking when Rosik points* — and was
never once specified. It cannot be money or force: Ronas has a cartel, absorbed every rival gang, and
took his Coterie seat by sustaining a two-month labour stoppage against the other three houses. It is
the grain going down the shafts, and it holds because he is a Competitor-primary who **cannot afford to
be seen having a Caretaker's reasons**. The price of snapping it falls on people he can never admit he
protects, and dressed as a labour-for-grain contract it gave him the pragmatic cover his world demands.
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

**The numbers, exactly.** Kaha'an is 150,000–200,000 on the surface plus 60,000 below. Lathion's
terraces feed 100,000. So Lathion could have fed the Warrens nearly twice over and **could never have
fed the city** — it was never an answer to the import dependency, only to the Warrens', and it is
unreachable. The population that starves sits on top of double the food it needs. See
`Book 3 - Crown Jewel/_LATHION_AFTER.md` for why none of it comes up.

### Lathion after the Door — **AUTHOR'S RULING 2026-08-04**

**Lathion is a dig site, not a destination.** Its existence becomes known; access does not follow.
The Great Shaft is gone, the only route is the Long Knives' road through Dead Man's Passage, and B3 ch6
settled that the road cannot become a supply line. All traffic is porters, so **knowledge flows out and
tonnage does not** — purification and energy reach the world as designs rebuilt on the surface, which is
also why the reverse-engineering takes the years Book 4 requires. The city becomes a small, expensive,
jointly-staffed research station under Balishan sovereignty with the Destiny Engine sealed and cordoned,
and **the Green Cities are its actual output**: the bequest reaches the living as somewhere else to
live. Nobody moves in, for six reasons that are Book 6's business and must not be argued on the page in
Book 3.

**Full brief, written for the Book 3 drafting session:** `Book 3 - Crown Jewel/_LATHION_AFTER.md`. It
carries the prohibitions (no reopened Great Shaft ever, no food convoys, no crown map, no settlement)
and the Book 6 correction below.

**Book 6's ignorance premise — CLOSED, applied 2026-08-04.** `book6_outline.md` had said nobody ever
learns the Warrens are Lathionese — *"The tunnels are old. That's all anyone knows"* — which Book 3
makes impossible, since the expedition descends through those tunnels to reach the Door and the empire
then spends twenty years building from Lathionese designs. **Ruled: everyone knows exactly what the
tunnels are, and it does not help.** Knowing whose machines these are is not the same as being able to
maintain them; Balisha holds *design* knowledge, extracted a notebook at a time and rebuilt in surface
workshops, which does not extend to keeping a five-thousand-year-old system alive in place. The
engineers can read the machine and cannot save it.

**No revelation scene, and no character treats the connection as news.** The origin is as unremarkable
as the age of a cathedral. And the correction strengthens the book rather than patching it: it is the
same lesson Book 6 already teaches through Melina — *a thorough and correct account of a thing is not
the power to change it* — so the surveys fail the way her models fail. **Do not point at the rhyme.**

### Lathion's two entrances — **AUTHOR'S RULING 2026-08-04**

**The Great Shaft was the front door; the Brass Door is the freight entrance.** For the three
millennia Lathion was open, arrivals came down the Great Shaft — a finished vertical bore from the
surface into the Crown's Arrival Halls, served by an elevator **spine**: a ceremonial main car for
delegations, smaller cars for routine traffic, freight lifts on their own tracks. The Brass Door is
the loading dock at the back of the building, which is why its antechamber is a bare eight-meter room
and why the passage below it is well-made and unbeautiful. Full description in `Places/Kaha'an/Lathion_
Physical Layout and Geography.md`.

**Three things ruled and not to be reopened:**

1. **The Great Shaft was collapsed and *filled*.** There is no open pit under Kaha'an and no surface
   trace. An open shaft would be found, and the premise that the surface has forgotten Lathion depends
   on there being nothing to find.
2. **The elevators were destroyed and stripped**; the recoverable parts went back into the city.
3. **The Repository does not hold the reason Lathion sealed itself.** B3 ch10 walks the expedition into
   the Repository, so this needs to be settled before the chapter is drafted: the reason went with the
   people who had it. Do not plant an answer nobody pays.

**Dead Man's Passage is natural caverns — not Lathionese construction, not a designed maze.** A cut
haul road once descended through the caves to the Door and was **deliberately collapsed** at the
sealing (demolition, not decay — Lathionese work does not decay). What survives is bare geology. There
is no "true path" marked in Lathionese symbols; the Long Knives' map was bought with corpses, which is
what B1 ch20, B3 ch6 and the Factions doc have always said. The three-way contradiction between the
Lathion layout, Kaha'an geography and B3 working notes is closed; all four docs now agree.

**Blast radius: none in the prose.** No chapter, beat draft, skeleton or Royal Road file changed. B1
ch19–21 and ch23 name the Passage repeatedly and never say who cut it.

### Lathion's canonical visual — **AUTHOR'S RULING 2026-08-04**

`Places/Kaha'an/Lathion - First Entry.png` is the canonical location illustration for the Crown at the
end of B3 ch7, *Wonder*. Its visual register is binding: **dense concentric city-rings, radial streets,
pale civic surfaces over a dark mechanical understructure, brass ribs, integrated blue-white systems,
living garden terraces, and the open central shaft descending toward the Core's warm glow.** Lathion is
a city built into one operating machine, not a conventional bright palace district and not a decayed
steampunk ruin. The illustration is not a scale drawing; the prose and `Lathion_ Physical Layout and
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

---

## 7. Open questions

**None currently open.** The three items opened on 2026-08-02 were all ruled on the same day and are
recorded in the changelog: the birthdays are **pinned** (`Story Timeline.md`), the Mistress's relation to
Xion is **canon and not a thread**, and Book 4 **has no relay**. See [§2](#2-cross-book-threads) and the
changelog for each.

**One warning survives them, and it is not a question.** The months-never-years rule must not be
over-applied now that Book 3 has a span. *"Years ago"* is still wrong everywhere inside Books 1–3, but by
the back half of Book 3 a character can truthfully say *a year ago* about Book 1. The rule exists to
prevent inflation; **the opposite error is now equally available.** Check the week table in
`Story Timeline.md` before writing any interval, in either direction.

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
