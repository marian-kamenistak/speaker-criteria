---
name: speaker-criteria
description: Score a conference talk 0-10 against seven weighted criteria (audience relevance, lived story, practical content, contrarian edge, audience interaction, next-day call to action, English delivery) and show the speaker what to fix first. Use whenever someone shares a talk outline, script, abstract or slide deck (.md, .pdf, .pptx, HTML or Slidev deck) and asks "is my talk ready", "rate my talk", "review my slides", "score this deck", "will this land", or is preparing a conference session, meetup talk or CFP submission, even if they never say the word "score". Also use as the quality gate when another skill builds a deck and needs a pass or fail.
---

# speaker-criteria

Version 1.3, 2026-11-13.

A talk is remembered for three things: a story the speaker lived, a claim worth arguing about, and something the listener used the next day. This skill scores a talk against the seven criteria a conference programme team uses to pick main-stage speakers, then helps the speaker raise the score.

It does two jobs, in this order:

1. **Evaluate.** Score each criterion 0-10 with quoted evidence, and calculate the weighted total.
2. **Improve.** Rank the fixes by how many points each one adds, rewrite what can be rewritten, and ask the speaker for what only they can supply.

## Before you score

You need three inputs. Ask for whatever is missing in one message, then proceed.

| Input | Why | If missing |
|---|---|---|
| **The content**: outline, script or deck | The thing being scored | Cannot start |
| **The room**: event, who attends (roles, seniority, company size), slot length | Relevance is scored against a specific room, never in general | Ask once. If the speaker doesn't know, write the audience you assumed at the top of the report and mark it "assumed" |
| **A video**: a past talk, or a new 2-minute video about this topic | English delivery cannot be judged from text | Leave criterion 7 unscored and mark the result provisional |

**Reading the content**

- `.md`, `.txt`, Slidev `slides.md`: read the file. Speaker notes and comments count.
- `.pdf`: read every page.
- `.pptx`: run `python3 <this skill's folder>/scripts/pptx_text.py <file>`. It prints the text and the speaker notes of each slide and needs no extra packages.
- HTML deck (reveal.js and similar): read the file. Slides are `<section>` elements, notes are `<aside class="notes">`.
- Google Slides or Keynote: ask for a PDF or PPTX export.

Read the speaker notes as carefully as the slides. Good speakers keep the story in the notes and five words on the slide, so a deck judged by its slides alone scores too low.

**What counts as the talk.** Score what the speaker has committed to saying. A line marked as a proposal, a question to confirm, or an optional joke is not in the talk yet: leave it out of the score and list it under the fixes as a quick win if confirming it would add points. When open questions put core lines in doubt, give two totals: the score as it stands, and a projection "if confirmed as drafted", labelled as a projection.

**The organiser's rules.** If the event states what it rejects (sales content, pure theory, talks given elsewhere), check the talk against each rule and report a breach above the score table. A breach is a reason to rework whatever the total says.

## The seven criteria

| # | Criterion | Weight | The question |
|---|---|---|---|
| 1 | Audience relevance | 20 | Would the people in this room act on this in their job within a month? |
| 2 | Lived story | 20 | Is it the speaker's own experience, told as one story built from sub-stories? |
| 3 | Practical, not generic | 15 | Could a listener do something differently on Monday, using only what was said? |
| 4 | Contrarian edge | 15 | Does the talk hold a position a smart person in the room disagrees with? |
| 5 | Audience interaction | 10 | Does the room do something, or only listen? |
| 6 | Next-day call to action | 10 | Does the talk end with a link or QR code to something usable tomorrow? |
| 7 | English delivery | 10 | Is the speaker clear and fluent at conference pace? (needs the video) |

The weights add up to 100. Relevance and story carry the most because a talk that fails either one cannot be rescued by polish. Practical content and the call to action together carry 25, because both answer "what do I do with this". Delivery carries 10 and also acts as a floor (see Verdict).

## How to score each criterion

Score what is on the page, not what the speaker probably means. Every score needs a quote or a slide number as evidence. When the evidence points both ways, quote one line for and one against. No evidence at all means 4 or lower.

Each criterion has four anchors. Use the numbers between them, in half points. When you are torn between two scores, take the half point between them; do not round down on every criterion, because seven small deductions add up to a full point the talk did not earn.

### 1. Audience relevance (20)

Look for: the audience's role and current problem named in their own words; examples at their company size, industry and seniority; the right level (no basics for a senior room); the title's promise kept by the content; a plan that fits the slot.

- **2**: the speaker's favourite topic with the room not considered, or a product pitch.
- **5**: the right topic, but the examples come from another world (hyperscaler stories for 30-person companies) or the level is off.
- **8**: the problem is stated the way the audience would say it, examples sit at their scale, and every section answers "why should I care".
- **10**: built for this room. It refers to their market, the event's theme or what earlier speakers said, and a person in the target role would say "that is my week".

**Mixed room.** Score for the group the talk is aimed at when that group is a real share of the room (a fifth or more). Then name every other group above a tenth of the room and say what the talk gives them. A group that large with nothing to take home costs a point.

**Slot fit.** Count the words the speaker plans to say and divide by 140 a minute. Add the time for each audience moment (30 to 90 seconds each) and about 5 seconds per click. Compare the sum with the speaking time, which is the slot minus Q&A. Above 90% it will run over on stage; say by how much. Below 60% the talk is thin or the speaker is rushing; say that too.

**Title.** A title that promises more than the content delivers loses points here and under criterion 4. A speaker who takes the title apart on stage, with evidence, has kept the promise to be honest but not the promise the room came for: score it between the two, and say which half of the title survived.

### 2. Lived story (20)

Two things are judged: **whose experience it is**, and **whether it forms one story**. Look for: first person; names, dates and numbers; things that went wrong; one line running from the opening to the close (where I started, what happened, what I do now); three to five sub-stories that each move that line forward.

Experience as an employee, founder, mentor, advisor or consultant all counts as lived when the speaker was in the room and says what they did. A case study taken from the press or from another talk does not, however well it is told.

- **2**: second-hand material. Frameworks, book quotes and "studies show", with no "I".
- **5**: real experience, but as unconnected anecdotes, or success only, or a list of tips with an example under each. Also: a strong arc carried mostly by other people's stories.
- **8**: one clear arc carried by three or more of the speaker's own sub-stories with concrete detail, at least one of them a failure, each tied back to the arc.
- **10**: a listener could retell the main story in two sentences, and every sub-story has a turn: what I believed, what happened, what I do now.

When ownership and structure differ (a clean arc, borrowed stories), score midway and say which of the two holds the talk back. To judge ownership, estimate the share of the spoken words that are the speaker's own first-person experience. A case the speaker mentored or co-built counts as theirs only for the parts where they say what they did.

### 3. Practical, not generic (15)

Look for: steps, thresholds, decision rules, the exact wording of a question or prompt, the real document or dashboard on screen, what it cost. A benchmark number is not practical by itself; it becomes practical with the rule for acting on it. Apply the swap test: remove the speaker's name from a slide. If any other speaker could present it unchanged, it is generic.

Depth beats coverage. A talk that covers six topics in twenty minutes has about two minutes for each "how" and rarely reaches 8.

- **2**: principles and slogans ("communication is key").
- **5**: sound advice that says what to do and stops before how.
- **8**: most sections carry a concrete how: a step, a rule or an example shown on screen.
- **10**: the audience sees the real artefact and the rule for using it, and nothing could have come from a generic blog post.

### 4. Contrarian edge (15)

The sharper the claim, the better it stays with the audience, as long as the speaker can defend it. Look for: a thesis stated as a claim someone could dispute; the common belief it opposes, named; the cost of being wrong; the other side given its best argument; the speaker's own cases supporting the claim. Provocation without proof does not count, and neither does a spicy title on a mild talk. A case that contradicts the thesis and is never addressed lowers the score.

- **2**: nobody could disagree ("AI is changing how we work").
- **5**: one or two sharp lines around a consensus thesis, or a bold title the content does not back.
- **8**: a disputable thesis stated early (within the first tenth of the talk), argued from the speaker's own evidence, with the opposite view named.
- **10**: a named group in the room has good reason to reject the thesis, the evidence is strong enough to move some of them, and the speaker says what would prove them wrong.

### 5. Audience interaction (10)

Look for planned moments, marked in the script, that can work in the room as given (its size, a stage, a clicker in the speaker's hand): a show of hands whose result the speaker then uses, a 30-second exercise with a neighbour, a live poll, a self-assessment, a question followed by a real pause, a demo that takes input from the room. The first one belongs near the start. For a 20 to 30 minute slot, two or three moments is right; more starts eating the content.

- **2**: a monologue that ends with "any questions?".
- **5**: one generic show of hands, and the result is never used.
- **8**: two or three planned moments spread through the talk, each tied to the content.
- **10**: the audience's input changes what is on screen or what the speaker says next, and everyone leaves having placed themselves on something (a level, a row, a score).

### 6. Next-day call to action (10)

Look for: one primary call to action; a link and a QR code to a guide, template, checklist, tool or AI skill; the asset exists, is free to open and continues the talk; the QR code stays on screen long enough to scan. If you can open the link, open it and check. If you cannot, write "asset not checked" in the evidence. An asset that matches the thesis but uses different names for the same things, opens with an upsell, or shares the closing slide with other QR codes loses a point for each: the listener has to do the mapping.

- **2**: "Thank you. Questions?", "connect with me on LinkedIn", or "try this with your team".
- **4**: a QR code to a homepage, or a sales ask ("book a call").
- **6**: a link to the slides or to an article about the topic. Something to read, nothing to use.
- **8**: one QR code to a specific asset that matches the talk and works the next day.
- **10**: the asset is the talk's method in usable form (a template with a worked example, an AI skill that runs the diagnostic). It is shown in use during the talk, the QR code appears mid-talk and at the end, and the first step takes under ten minutes.

### 7. English delivery (10)

This needs evidence of the speaker speaking: a recording of a past talk, or a new 2-minute video in which they explain the talk's main claim to the camera without slides. A written script shows how someone writes, not how they speak, so never score this criterion from the script.

What you can judge depends on what you can open:

- **A transcript or captions**: fluency, sentences that get finished, filler words, vocabulary of the field, and pace when timestamps exist (130 to 160 words a minute suits a conference room).
- **The video or audio itself**: also pronunciation, pauses, energy, and whether the speaker reads from the slides.

Say in the report which of the two you judged. If you only had a transcript, name pronunciation and stage presence as not assessed and ask a person to watch two minutes.

- **2**: hard to follow, reads the text, frequent breakdowns.
- **5**: understandable with effort; flat or rushed, many fillers.
- **8**: clear and fluent at a natural pace; small slips never block the meaning.
- **10**: stage-ready. Varied pace, pauses that land, could carry a keynote.

No video: the criterion stays "not scored", and the report says exactly what to send (see "To complete the score" in the template).

## Calculate

```
total       = sum(weight x score) / sum(weights of the criteria you scored)
gain at 8   = weight x (8 - score) / sum(weights of the criteria you scored)
```

Round the total to one decimal. When criterion 7 is not scored, the divisor is 90 and the result is provisional.

Run the calculator, which sits beside this file:

```
python3 <this skill's folder>/scripts/score.py <s1> <s2> <s3> <s4> <s5> <s6> <s7>
```

Pass `-` for a criterion that is not scored. It prints the table, the total, the verdict and the final score line. Paste its table into the report and add the Evidence column. If you cannot run code, calculate by hand with the two formulas above and show the working.

**Verdict**

| Total | Verdict |
|---|---|
| 9.0 or more, no criterion below 5, video scored | **Ready for the stage** |
| 9.0 or more, no criterion below 5, no video | **Ready on content**. Send the video to finish |
| 8.0 to 8.9, no criterion below 5 | **Accepted level**. The talk can be accepted; work with the speaking coach to reach 9.0 before the stage |
| 6.0 to 7.9, or 8.0+ with a criterion below 5 | **Close**. The talk stands; fix the top items and re-score |
| Below 6.0 | **Rework**. The structure has to change, not the wording |

The ELC Conference accepts talks at 8.0 and puts them on stage at 9.0, after coaching.

## The report

Use this structure every time, so two reports can be compared.

```
# Speaker score: <talk title>

Room: <event, audience, slot> <(assumed) if you had to guess>
Scored from: <file>, <slides only | slides and notes>, video: <transcript | watched | none>

| # | Criterion | Weight | Score | Points | Gain at 8 | Evidence |
|---|---|---|---|---|---|---|
| 1 | Audience relevance | 20 | 7 | 1.56 | +0.22 | For: "<quote or slide>". Against: "<quote>" |
| ... |
| 7 | English delivery | 10 | not scored | - | - | no video |

**Total: X.X / 10 - <verdict>** <(provisional: English delivery not scored)>
<Below 5: criterion names, if any>

## Fix these first
1. **<Criterion>** (now N, +G if it reaches 8). What is missing, with the quote.
   Rewrite: <the replacement line, slide or moment, written out>
2. ...

## Keep
- <the two or three things that already work, so they survive the edit>

## To complete the score
<only when something is missing: the video to send, the audience detail you had to assume>

SPEAKER SCORE: X.X/10
```

Rules for the report:

- **Rank fixes by "gain at 8", largest first.** On a tie, the heavier criterion goes first, then the lower score, then rubric order. Write out every fix worth 0.2 or more. Give each smaller one a single line with its rewrite; several small fixes together are often worth more than one large one.
- **Write the fix out.** "Add a story" is a comment. "Open with the Tuesday the release failed, 90 seconds, then the claim" is a fix.
- **Never invent the speaker's experience, numbers or opinions.** Where a fix needs a story or a figure only they have, write a marked gap: `[YOUR STORY: the first time this failed, with the month and what it cost]`.
- **End with the `SPEAKER SCORE: X.X/10` line**, exactly in that form, so other tools can read it.

## Improve

After the report, offer to apply the fixes. When the speaker agrees:

1. Rewrite what is yours to rewrite: structure, the order of sub-stories, slide text, the wording of the thesis, where the interaction moments go, the call-to-action slide.
2. Ask for what only the speaker has. Collect every marked gap into one list of questions.
3. Re-score the new version with the same rubric and show the before and after per criterion.
4. Repeat until the verdict is "ready", or until the remaining gaps are all things the speaker must supply.

A higher score earned by making the talk vaguer, safer or longer is a regression. If an edit raises one criterion by lowering another, say so.

## Scoring honestly

- Scores drift upward when you want to be kind. The speaker is helped by a 5 they can fix, and harmed by an 8 they believe.
- A first draft usually lands between 5 and 6.5. A 9 on any criterion is rare.
- Judge the talk for the room it will be given in. A talk can be a 9 for staff engineers and a 4 for founders.
- Marketing in disguise fails criterion 1 regardless of how good the slides look. Proof of the speaker's credibility (a logo strip, a testimonial) is fine in passing; a section that sells is not.

---

Based on the speaker selection criteria of the ELC Conference, by Marian Kamenistak and the Engineering Leaders Community.
