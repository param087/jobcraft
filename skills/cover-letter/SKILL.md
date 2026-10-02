---
name: cover-letter
description: Draft or revise a cover letter, application note, or short recruiter message from the user's resume and a specific job description. Use when the user asks for a cover letter, a "why this company" paragraph, or a tailored application message.
---

# Draft a cover letter

## Inputs

- Resume text or file (required).
- Job description text (required).
- Optional: tone (formal, warm, direct), length limit, hiring manager name,
  company facts the user wants referenced, a prior draft to revise.

If the resume or job description is missing, ask for it in one message and
stop. Otherwise proceed and infer a professional, direct tone.

## Procedure

1. **Pick the two or three strongest matches** between the resume and the
   job's core requirements. These anchor the letter; everything else is cut.
2. **Draft using `assets/template.md`.** Three short paragraphs, 220–300
   words unless the user sets a different limit:
   - Opening: the role, one line on why this company or problem, no cliches
     ("I am writing to apply").
   - Evidence: two concrete achievements from the resume mapped to the job's
     needs, with the user's real numbers.
   - Close: what the user would focus on in the first months, a clear ask for
     a conversation, thanks.
3. **Flag unverifiable claims.** Any fact about the company, team, or product
   that is not in the job description or supplied by the user goes in square
   brackets: `[confirm: company recently launched X]`. Do not assert it.
4. **Deliver**: the letter, then a 3-line "What I used from your resume" list
   so the user can check accuracy, then the list of bracketed items to
   confirm.

## Never do

- Never invent achievements, metrics, employers, or company facts.
- Never exceed the user's stated length.
- Never promise skills the resume does not show. If the user asks to claim
  something the resume lacks, say the letter cannot assert it and offer to
  phrase it as a transferable strength instead.
- Never send or submit the letter anywhere; return the text only.

## Hand-off

Offer one next step, such as `interview-prep` or logging the application with
`application-tracker`. Explicit user instructions override this skill.
