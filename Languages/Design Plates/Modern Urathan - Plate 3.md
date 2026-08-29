# Modern Urathan — Design Plate 3

**Status:** APPROVED — canon, 2026-08-22  
**Created:** 2026-08-22  
**Depends on:** Modern Urathan Plate 1's working sound changes and grammar  
**Generative test:** A regular decimal numeral system from zero through indefinitely large values, with
ordinals, fractions, decimals, digit strings, and explicit scale recursion

This plate gives Standard Modern Urathan a deliberately regular counting system. It does not reconstruct
the system from any number currently written in English in the books; no native Urathan numeral appears
in prose. The design follows the culture instead: scholars with a centralized school system, a national
examination, extensive record-keeping, and very strong opinions about classification would standardize
quantity until its spoken structure could be parsed almost mechanically.

The result is decimal and triad-grouped. It has no special ten-thousand unit and no arbitrary sequence of
unrelated words equivalent to *million, billion, trillion,* and their successors.

## 1. Historical shape

The approved Early Imperial Balishan plate establishes **an, du, sei, kau, pem,** and **des** for one
through five and ten, then deliberately leaves the rest unbuilt. This plate extends that numeral lexicon
without claiming that every modern Balishan daughter adopted Uratha's later grammar.

Three historical layers produce the modern system:

| Layer | Development |
|---|---|
| Imperial inheritance | The academy inherits decimal counting, the first five digit roots, and **des** “ten.” |
| Provincial standardization | Examiners select one short form for each remaining digit and establish **hek** “hundred” and **mir** “thousand” as the only ordinary place-rank words. |
| Independent Urathan reform | Tower mathematicians mandate exact coefficient–rank order, triads from the right, a spoken zero-gap rule, decimal positional notation, and productive scale expressions with **kel** “count; measure.” |

The reform does not require every villager to speak like a ledger. It creates a single form that schools,
surveyors, engineers, physicians, tax offices, and scholars can all treat as exact. Casual speech may
shorten predictable pieces; High Exam answers may not.

Standard Balishan's complete large-number system remains unbuilt. Urathan can be known to have regularized
away inherited and regional variation without inventing that variation merely to make Uratha look tidy.

## 2. The ten digits

| Value | Modern Urathan | Pronunciation | History |
|---:|---|---|---|
| 0 | **nu** | **NOO**, /nu/ | mathematical use of ordinary negator **nu**, “none; no quantity” |
| 1 | **an** | **AHN**, /an/ | inherited Imperial **an** |
| 2 | **du** | **DOO**, /du/ | inherited Imperial **du** |
| 3 | **sei** | **SAY**, /sei/ | inherited Imperial **sei** |
| 4 | **ko** | **KOH**, /koː/ | Imperial **kau**, regularly smoothed by Plate 1 **au > o** |
| 5 | **pem** | **PEM**, /pem/ | inherited Imperial **pem** |
| 6 | **vek** | **VEK**, /vek/ | opaque Imperial numeral selected by the provincial standard |
| 7 | **zhu** | **ZHOO**, /ʒu/ | Imperial **ju**, regularly simplified by Plate 1 **j > zh** |
| 8 | **tae** | **TAY**, /teː/ | Imperial **tai**, regularly smoothed by Plate 1 **ai > ae** |
| 9 | **nor** | **NOR**, /nor/ | opaque Imperial numeral selected by the provincial standard |

Numeral roots carry no descriptive etymologies. They are old, frequent, and semantically indivisible.
Plate 3 does not invent meanings such as “two hands” or “the complete number” to make opaque digits look
poetic after the fact.

The use of **nu** for both ordinary negation and numeric zero is not ambiguous inside a number. Before a
predicate it negates; alone or in a numeral slot it names zero. Mathematical writing supplied the social
pressure that turned “none” into a full number rather than a mere absence.

## 3. The three ordinary rank words

| Value | Urathan | Function |
|---:|---|---|
| 10 | **des** | ten; the first decimal rank |
| 100 | **hek** | hundred; the second decimal rank |
| 1,000 | **mir** | thousand; the first triad scale |

There is no separate word for ten thousand or hundred thousand:

| Value | Structure | Urathan |
|---:|---|---|
| 10,000 | ten × thousand | **des mir** |
| 100,000 | hundred × thousand | **hek mir** |

Exact classroom and mathematical speech may make the implicit coefficient one audible—**an des mir,
an hek mir**—when parsing rather than brevity matters. Ordinary careful speech permits **des mir** and
**hek mir** because **des** and **hek** already denote complete coefficient groups.

## 4. Numbers below one thousand

Within a triad, ranks descend from left to right:

> **coefficient + hek, coefficient + des, final digit**

Every pronounced rank has its coefficient before it. A missing internal rank is marked once by **nu** if
a lower nonzero value follows. **Nu** covers one or more consecutive empty places; speakers do not recite
an inventory of absent ranks.

| Number | Analysis | Standard Urathan |
|---:|---|---|
| 5 | five | **pem** |
| 10 | one ten | **an des** |
| 11 | one ten one | **an des an** |
| 20 | two ten | **du des** |
| 42 | four ten two | **ko des du** |
| 99 | nine ten nine | **nor des nor** |
| 100 | one hundred | **an hek** |
| 101 | one hundred, gap, one | **an hek nu an** |
| 105 | one hundred, gap, five | **an hek nu pem** |
| 110 | one hundred one ten | **an hek an des** |
| 125 | one hundred two ten five | **an hek du des pem** |
| 408 | four hundred, gap, eight | **ko hek nu tae** |
| 999 | nine hundred nine ten nine | **nor hek nor des nor** |

This is the form taught on the High Exam. It contains no special teens, no inversion equivalent to
“four-and-twenty,” and no morphophonemic changes triggered by particular digits.

In casual speech, **an** may be omitted before **des** when ten is the highest rank: **des an** for eleven.
That shortening is ordinary, but the fully explicit **an des an** is never wrong and is preferred in
dictation, measurement, and testimony.

## 5. Thousands and triad grouping

Numbers are divided into groups of three digits from the right. A nonzero group is spoken as an ordinary
sub-thousand numeral followed by its scale. The units group has no scale word.

| Number | Group structure | Standard Urathan |
|---:|---|---|
| 1,000 | one × thousand | **an mir** |
| 1,001 | one thousand, gap, one | **an mir nu an** |
| 1,010 | one thousand, gap, one ten | **an mir nu an des** |
| 1,100 | one thousand one hundred | **an mir an hek** |
| 1,205 | one thousand two hundred, gap, five | **an mir du hek nu pem** |
| 10,000 | ten thousand | **des mir**; exact parsing **an des mir** |
| 25,000 | two ten five thousand | **du des pem mir** |
| 100,000 | hundred thousand | **hek mir**; exact parsing **an hek mir** |
| 125,000 | one hundred two ten five thousand | **an hek du des pem mir** |
| 125,408 | 125 thousand, 408 | **an hek du des pem mir ko hek nu tae** |

A single **nu** marks a gap between the scale-bearing group and the next nonzero group. Thus 100,005 is
**an hek mir nu pem**, not a recital of every empty hundred, ten, and unit position in the missing group.

The written standard groups digits in triads from the right. This plate establishes the grouping and the
existence of a zero digit, not the shapes of Urathan numeral glyphs or the mark used as a separator.

## 6. Large scales without arbitrary names

Urathan does not create an unrelated lexical word for each new group of three zeroes. It grammaticalizes
inherited **kel**, “count; measure,” as a scale-index linker:

> **base + kel + exponent**  
> “the base raised to the stated count”

With **mir** as the triad base:

| Value | Mathematical structure | Urathan scale |
|---:|---|---|
| 10³ | 1,000 | **mir** |
| 10⁶ | 1,000² | **mir kel du** |
| 10⁹ | 1,000³ | **mir kel sei** |
| 10¹² | 1,000⁴ | **mir kel ko** |
| 10¹⁵ | 1,000⁵ | **mir kel pem** |
| 10¹⁸ | 1,000⁶ | **mir kel vek** |
| 10²¹ | 1,000⁷ | **mir kel zhu** |
| 10²⁴ | 1,000⁸ | **mir kel tae** |
| 10²⁷ | 1,000⁹ | **mir kel nor** |
| 10³⁰ | 1,000¹⁰ | **mir kel an des** |

Thus there is **no irreducible standard word for “million.”** The ordinary standard says **mir kel du**,
three short words that state exactly what the scale is. A speaker never has to memorize whether a rare
large-number name contains six zeroes, nine, twelve, or sixty.

A coefficient precedes the complete scale phrase:

| Number | Urathan |
|---:|---|
| 1,000,000 | **an mir kel du** |
| 2,000,000 | **du mir kel du** |
| 100,000,000 | **an hek mir kel du** |
| 1,000,000,000 | **an mir kel sei** |
| 7,000,000,000 | **zhu mir kel sei** |

In a multi-group number, each scale phrase is spoken as a unit, with a slight juncture afterward:

> **an mir kel du | du hek sei des ko mir | pem hek vek des zhu**  
> one million | two hundred thirty-four thousand | five hundred sixty-seven  
> **1,234,567**

The vertical stroke is linguistic analysis, not punctuation in ordinary writing. It marks the brief
spoken grouping that prevents the scale exponent from being mistaken for the next coefficient.

## 7. Arbitrary powers and scientific scale

Because **kel** is productive rather than a frozen large-number construction, any positive base can take
an exponent:

| Expression | Reading | Value |
|---|---|---:|
| **des kel du** | ten to the second count | 10² |
| **des kel sei** | ten to the third count | 10³ |
| **des kel vek** | ten to the sixth count | 10⁶ |
| **mir kel du** | thousand to the second count | 10⁶ |
| **du kel an des** | two to the tenth count | 2¹⁰ |

Consequently **des kel vek** and **mir kel du** denote the same magnitude from different useful
perspectives. The former belongs naturally in logarithms, scientific notation, and proofs; the latter in
ordinary large-number grouping.

Exponents are themselves ordinary numerals and can recurse without a new vocabulary ceiling. Formal
notation supplies brackets where the spoken phrasing would become unwieldy. Plate 3 does not pretend that
humans enjoy hearing a thousand-word exponent merely because the grammar permits one.

## 8. Decimal fractions and digit strings

Inherited **koi**, “boundary; meeting edge,” becomes the spoken decimal point. Everything after **koi** is
read digit by digit, including every **nu**:

| Written value | Urathan | Literal reading |
|---:|---|---|
| 0.5 | **nu koi pem** | zero point five |
| 1.25 | **an koi du pem** | one point two five |
| 3.1415 | **sei koi an ko an pem** | three point one four one five |
| 6.02 | **vek koi nu du** | six point zero two |

The same digit-by-digit register is used for catalogue numbers, room identifiers, specimen codes, and
other strings that look numeric but are not quantities:

| String | Quantity reading | Identifier reading |
|---:|---|---|
| 125 | **an hek du des pem** | **an du pem** |
| 1005 | **an mir nu pem** | **an nu nu pem** |

Context normally distinguishes them. Formal dictation can introduce a string as a catalogue, sequence,
or measured quantity before reading it.

## 9. Fractions, ratios, and percentages

Inherited **tir**, “cut; divide cleanly,” links numerator and denominator:

> **numerator + tir + denominator**

| Fraction | Urathan | Literal structure |
|---:|---|---|
| 1/2 | **an tir du** | one divided by two |
| 3/4 | **sei tir ko** | three divided by four |
| 7/10 | **zhu tir an des** | seven divided by ten |
| 25/100 | **du des pem tir an hek** | twenty-five divided by one hundred |

This analytic form remains exact regardless of whether reader-facing English calls the result *one half,
three quarters,* or *twenty-five percent*. Common household speech may possess shorter inherited fraction
words later; mathematical Urathan does not require them.

A percentage is simply a ratio whose denominator is **an hek**. No separate percent morphology is needed.

## 10. Ordinals

Early Imperial **-ya** survives as an ordinal enclitic applying to the complete numeral phrase. It is
joined to the final spoken element in romanization; analysis writes **=ya** to show that its scope is the
whole number rather than merely the last digit.

| Ordinal | Surface romanization | Analysis |
|---:|---|---|
| first | **anya** | *an=ya* |
| third | **seiya** | *sei=ya* |
| tenth | **an desya** | *an des=ya* |
| twenty-first | **du des anya** | *du des an=ya* |
| 125th | **an hek du des pemya** | *an hek du des pem=ya* |
| millionth | **an mir kel duya** | *an mir kel du=ya* |

This creates one ordinal rule for every magnitude. The language does not need separate irregular forms
equivalent to *first, second,* or *third* in the exact register, though casual inherited speech may later
supply them.

## 11. Parsing rules in compact form

The standard can be stated as a small algorithm:

1. Use decimal positional value.
2. Divide the written number into three-digit groups from the right.
3. Within each group, say nonzero coefficients before **hek** and **des**, then the final digit.
4. Say **nu** once when one or more omitted internal places separate two nonzero values.
5. After each non-unit group, say **mir** for group one or **mir kel N** for group N.
6. Read digits individually after **koi** or when the sequence is an identifier rather than a quantity.
7. Add **=ya** to the final spoken element for an ordinal.
8. Put **tir** between numerator and denominator for an exact fraction.

A child who knows the ten digit roots, **des, hek, mir, kel, koi, tir,** and **-ya** possesses the full
productive system. Larger values add no lexical burden.

## 12. Cultural consequences

Urathans regard this regularity as evidence that their educational system works. They are not wholly
wrong. The standard reduces ambiguity in engineering quantities, taxes, medical doses, archival shelf
marks, and spoken transcription. It also makes several social judgments easy to disguise as judgments
about correctness:

- Tower-trained speakers use explicit coefficients and clean triad junctures.
- Ordinary speakers omit predictable **an**, compress pauses, and retain local fraction words.
- Bakarn labor registers may preserve older counting forms or develop faster workplace contractions.
- Examiners can call a perfectly intelligible regional number “imprecise” because it does not match the
  mandated parse.
- Scholars congratulate themselves for making numbers democratic while access to the schools that teach
  the standard remains radically unequal.

The system is genuinely efficient. Its use as a class gate is also genuine. Uratha sees no contradiction.

## 13. Reader-facing policy

The novels continue to write numbers in ordinary English words or digits. A reader does not need to learn
**an hek du des pem** merely because an Urathan says 125. Native number speech should appear only when it
does narrative work: a lesson, riddle, inscription, disputed measurement, mathematical proof, accent cue,
or a moment when exact parsing matters.

This is the same translation policy as the Tower names. The language exists beneath the prose without
requiring every line of prose to exhibit it.

## 14. Approved boundary and future extensions

Approval of this plate establishes:

- Modern Urathan digit names zero through nine;
- **des, hek,** and **mir** as ten, hundred, and thousand;
- strict coefficient-before-rank construction;
- triad grouping and the absence of a ten-thousand scale word;
- **nu** as zero and a single spoken gap marker;
- **kel** as the productive exponent and scale-index linker;
- **koi** as decimal point, **tir** as fraction division, and **=ya** as the ordinal marker;
- reader-facing translation rather than routine native numerals in prose.

It does not establish numeral glyph shapes, arithmetic operator vocabulary, measurement units, currency
subdivision, colloquial fraction lexemes, regional dialect systems, or Standard Balishan's complete
number grammar.

Possible later extensions, none of which reopen the approved core, are:

- **Digits six through nine:** judge **vek, zhu, tae, nor** by sound and dictation contrast.
- **Rank words:** judge **hek** and **mir** as a pair with inherited **des**.
- **Explicit one:** decide how strongly ordinary speech favors **an des** over shorter **des**, while
  retaining the exact-register form.
- **Large scale:** retain transparent **mir kel N**, or permit one or two lexicalized everyday contractions.
- **Zero gaps:** retain a single **nu** for any omitted run, or require more positional detail in formal
  dictation.

The plate succeeds if 125 is immediately constructible, 100,000 requires no special ten-thousand unit,
and a number larger than anyone has ever needed can still be named without opening a dictionary.
