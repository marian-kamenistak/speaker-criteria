# speaker-criteria

Find out if your talk is ready for a conference stage, and what to fix first. This Claude skill scores a talk from 0 to 10 on seven weighted criteria, with a quote from your own slides behind each score.

From the [Engineering Leaders Community](https://www.engineeringleaders.io/). These are the criteria the ELC Conference programme team uses to pick its speakers.

## What you get

- A score from 0 to 10 for each criterion, with a quote or a slide number from your talk as evidence.
- A weighted total and a verdict.
- The fixes, ranked by how many points each one adds. Each fix is written out as the new line, slide or audience moment.
- A list of questions for the stories and numbers only you have. The skill does not invent your experience.

It also counts the words you plan to say, at 140 a minute, and tells you if the talk will run over your slot.

## The seven criteria

| # | Criterion | Weight | The question |
|---|---|---|---|
| 1 | Audience relevance | 20 | Would the people in this room act on this in their job within a month? |
| 2 | Lived story | 20 | Is it your own experience, told as one story built from sub-stories? |
| 3 | Practical, not generic | 15 | Could a listener do something differently on Monday, using only what was said? |
| 4 | Contrarian edge | 15 | Does the talk hold a position a smart person in the room disagrees with? |
| 5 | Audience interaction | 10 | Does the room do something, or only listen? |
| 6 | Next-day call to action | 10 | Does the talk end with a link or QR code to something usable tomorrow? |
| 7 | English delivery | 10 | Are you clear and fluent at conference pace? |

The weights add up to 100. Relevance and story carry the most, because polish cannot rescue a talk that fails either one.

## Pass marks

| Total | Verdict |
|---|---|
| 9.0 or more | **Ready for the stage** |
| 8.0 to 8.9 | **Accepted level**. The talk can be accepted. Work with the speaking coach to reach 9.0 before the stage |
| 6.0 to 7.9 | **Close**. The talk stands. Fix the top items and score it again |
| Below 6.0 | **Rework**. The structure has to change, not the wording |

The ELC Conference accepts talks at 8.0 and puts them on stage at 9.0, after coaching.

A criterion below 5 keeps the talk at "Close", whatever the total. A 9.0 without a video reads "Ready on content" until you send the video. A first draft usually lands between 5 and 6.5.

## What to give it

1. **Your talk.** An outline, a script or a deck as `.md`, `.pdf` or `.pptx`. Speaker notes count, so leave them in.
2. **The room.** The event, who attends and how long your slot is. Relevance is scored for one specific room.
3. **A video.** A past talk, or a new 2-minute video where you explain the main claim of the talk to the camera, without slides. English delivery is scored from the video. Without it the skill scores six criteria and marks the result provisional.

## Install

### claude.ai

1. Download [speaker-criteria.zip](https://github.com/marian-kamenistak/speaker-criteria/releases/latest/download/speaker-criteria.zip).
2. Sign in at claude.ai and open **Customize**, then **Skills**.
3. Click **+**, then **Create skill**, then **Upload a skill**, and choose the zip.
4. Start a new chat and attach your talk.

Skills need code execution turned on. On Team and Enterprise plans an owner turns it on for the whole organisation.

### Claude Code

```bash
git clone https://github.com/marian-kamenistak/speaker-criteria ~/.claude/skills/speaker-criteria
```

Start a new session and the skill loads from `~/.claude/skills/`. The two scripts need Python 3 and no extra packages.

## Use it

Attach the talk and write:

```
Score my talk with speaker-criteria. The deck is attached.
Room: a conference for engineering leaders, 300 people, mostly engineering managers and CTOs. 25-minute slot.
Video of my last talk: <link>
```

The report has a score table, the fixes in order, and the two or three things to keep. This is the table for a first draft with no video yet:

```
| # | Criterion | Weight | Score | Points | Gain at 8 |
|---|---|---|---|---|---|
| 1 | Audience relevance | 20 | 7 | 1.56 | +0.22 |
| 2 | Lived story | 20 | 6 | 1.33 | +0.44 |
| 3 | Practical, not generic | 15 | 6.5 | 1.08 | +0.25 |
| 4 | Contrarian edge | 15 | 5 | 0.83 | +0.50 |
| 5 | Audience interaction | 10 | 4 | 0.44 | +0.44 |
| 6 | Next-day call to action | 10 | 6 | 0.67 | +0.22 |
| 7 | English delivery | 10 | not scored | - | - |

Total: 5.9 / 10 - Rework (provisional: English delivery not scored)
Below 5: Audience interaction

SPEAKER SCORE: 5.9/10
```

"Gain at 8" shows how much the total grows if that criterion reaches 8. Here the contrarian edge comes first.

Then ask Claude to apply the fixes. It rewrites what it can, asks you for the missing stories, and scores the new version.

## Pitch your talk

- Pitch a conference talk: https://elc-conference.io/cfp/
- Pitch a meetup talk: https://www.engineeringleaders.io/cfp/

MIT licensed.
