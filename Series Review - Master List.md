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
| **Craft — Book 1** | 1 | C-21 |
| **Craft — Book 2** | 0 | — |
| **Open questions** | 0 | — |

**1 item outstanding across both books**, craft-tier, and it is a judgment call rather than a defect.
Nothing in Books 1–2 currently breaks a rule.

**Before flagging anything here as outstanding, check the history.** This document has now produced
more stale entries than live ones. Eight of the original eleven Book 1 craft flags were stale — the
chapters had been rewritten and the flags never retired — and a further twelve entries turned out to
be already fixed, six caught by re-reading the prose and six more only found by searching commit
messages (`git log --all --grep="C-N"`) and grepping for the exact phrase an entry quotes. Reading
the chapter is not sufficient; an entry can describe a problem a later commit solved in a way the
entry never anticipated. **A flag that outlives its problem is worse than no flag**, because the next
reader trusts it and cuts good material — C-6 pointed at the best passage in ch25 and nearly got it
deleted.

**Numbering note.** C-16 through C-21 as filed below are the local series. **C-22 through C-28 came
in from the cloud branch on 2026-07-29, where they were numbered C-16 through C-22**; both lines had
invented C-16 onward independently for different items. The mapping is in the changelog under the
merge entry, and the branch's own commit messages still use the old numbers.

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

---

## 2. Cross-book threads

These are the spine. Each is already working; each could be broken by an unwary revision.

**The hands.** B1 ch1 "The Healer's Hands" (tweezing glass, washing blood away) → B2 ch13 "Clean Hands" (*"he had just spent a night being him to the letter, and the proof was there at the ends of his own wrists, unmarked"*) → B2 ch17 (he takes his own pulse, finds it steady, and cannot make the diagnosis land on himself). Do not add a fourth without reason; three is the shape.

**Frozen silence → chosen silence.** B1 ch1: rooted to the paving stones while Tam is taken, because acting means saying his own name. → B1 ch8: Elara asks him at the gate why he didn't, and *"nothing came out of it. The same nothing, arriving in the same order."* → B1 ch19: Farleen argues him down a maze in five stages and he answers none of them. → B2 ch16: he refuses Rosik the argument, and the text distinguishes the two explicitly. **This is the arc, and it spans two books.** Book 1 not closing it is correct.

**The test, for any silence not yet written.** Put the best available defence to him and see whether he takes it.

| Silence | Defence | He says |
|---|---|---|
| Mira, at fifteen — B1 ch22 | terrified of his father, and it would have changed nothing | *"I didn't even try."* |
| Tam, in the square — B1 ch1 | speaking ends Master Fen and eight years of work | *"I could have saved him then and worked the clinic out later."* |
| Elara, at the gate — B1 ch8 | he still can't tell her what he is | *"She deserves the truth, not silence."* |
| Rosik's study — **B2** ch5 | Rosik feeds on arguments; it would move nothing | **he agrees** |
| The disinheritance — **B2** ch16 | the same | **he agrees** |

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

**The two sights.** Mira gave him the healer's eye; Rosik gave him the geometry. B2 ch11–12 has him partition them deliberately and use his father's on purpose for the first time (*"that one was Mira's… he would not drag it down into this"*). The inheritance is tracked, not blurred — keep it that way.

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

| # | Item |
|---|---|
| C-21 | **Narrowed, and it is a judgment call rather than a defect.** One surviving closing swell: ch22's *"This was our first real fight." / "It was a good one."*, landing a beat after the Mira confession. ch6's *"counted themselves lucky to survive until sunset"* and ch23's four paragraphs of *"Tomorrow everything would change"* were removed by the C-22 ending pass. **ch22 is do-not-touch for the confession itself** — this is the two lines after it, not the scene, and the argument for keeping them is that they are the only air the chapter gives the reader. Needs the author, not a pass. |

*C-3, C-17 and C-19 were closed by work that came in with the cloud-branch merge; C-16 and C-18 were
fixed on 2026-07-29. Evidence for all five in [§6](#6-settled-rulings).*

### Craft — Book 2

**None outstanding, and empty for the first time.** C-12 through C-15 were re-verified and closed;
C-26, C-27 and C-28 were opened in their place and all three are applied — see
[§6](#6-settled-rulings).

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

## 7. Open questions

**None currently open.** Everything previously listed here has been decided; see [§6](#6-settled-rulings).

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
