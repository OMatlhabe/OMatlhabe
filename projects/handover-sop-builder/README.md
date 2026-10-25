# Handover SOP Builder

An agent skill that helps you write standard operating procedures (SOPs) good enough for someone who was never in the room to **take ownership, run the process correctly, troubleshoot failures, and maintain it without you.**

It works for any process: finance, operations, sales, support, IT, HR, or technical systems.

## Why this exists

Most SOPs describe what was done. A handover SOP has to let a stranger do it. This skill combines two ideas:

1. A co-authoring workflow: gather context, draft section by section, and test the document with a fresh reader.
2. A handover-specific structure: access, exceptions, troubleshooting, tribal knowledge, open items and a first-30-days plan.

Built by Oratile Matlhabe with Claude (Anthropic), and inspired by the co-authoring workflow in [Anthropic's public skills repository](https://github.com/anthropics/skills).

## What it does

| Stage | What happens |
| --- | --- |
| 0. Intake | Reads your existing slides, docs, emails and screenshots first |
| 1. Gap questions | Asks only what the sources cannot answer |
| 2. Draft | Builds a 17-section SOP, marking every unknown as `[TO CONFIRM]` |
| 3. Reader test | Independent reviews quiz it, walk through it cold, and drill failures; records gaps and readiness; scores do not guarantee real-world correctness |
| 4. Finish | Open-items register, sign-off, onboarding plan, review reminder |

## Install

[**Download Handover SOP Builder (.skill)**](https://github.com/OMatlhabe/OMatlhabe/releases/download/handover-sop-builder-v1.0.0/handover-sop-builder.skill)

The download is a ZIP-format `.skill` package containing the reviewed source, example, README, validation notes and MIT licence. Extract it if your host expects a skill folder. Version 1.0.0 is published as a [GitHub Release](https://github.com/OMatlhabe/OMatlhabe/releases/tag/handover-sop-builder-v1.0.0), with the `.skill` package attached under Assets.

Copy `SKILL.md` into a folder named `handover-sop-builder` within your agent's skills directory (for example `~/.claude/skills/handover-sop-builder/`) or follow your host application's documented custom-skill import process. Import support differs by product; a Markdown upload alone does not install a skill everywhere.

## Use

Say something like:

- "Write a handover SOP for our weekly invoice run. I've attached the old slides."
- "Turn this runbook into a proper SOP and test it."
- "Document this process so my backup can run it while I'm away."

Provide whatever you have: slides, documents, emails, screenshots, notes. Messy is fine.

## Tips for the best result

- Name who takes over and how experienced they are.
- Share screenshots of the tools. The skill quotes button and menu labels exactly.
- Tell it what has gone wrong before. Troubleshooting is usually the weakest section.
- Answer gap questions in shorthand ("1: yes, 2: see ticket, 3: no").
- Do not skip the reader test. It is what catches the guesses you no longer notice.

## What it will not do

- It will not invent names, addresses, numbers or steps. Gaps are marked and tracked.
- It will not put credentials in the document.

## Files

- `SKILL.md`: the skill itself
- `examples/example-sop.md`: a short fictional example of the output style

## Licence

MIT. See `LICENSE`.

## Portfolio evidence and limits

Created by Oratile Matlhabe. This is a reusable agent instruction skill, not an autonomous application. The example is fictional and abridged, not an approved payment procedure. Review findings and test limits are documented in [VALIDATION.md](VALIDATION.md). No measured time savings or production adoption are claimed.
