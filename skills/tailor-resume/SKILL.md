---
name: tailor-resume
description: Tailor, optimize, or ATS-check a resume against a specific job description the user provides. Use when the user asks to match their resume to a role, improve resume bullets for a posting, find missing keywords, or make a resume ATS-friendly.
---

# Tailor a resume to a job description

## Inputs

- Resume text or attached file (required).
- Job description text (required).
- Optional: target length, seniority, or sections to leave untouched.

If either required input is missing, ask for it in one short message and
stop. If both are present, proceed without asking anything.

## Procedure

1. **Extract requirements from the job description.** List must-have skills,
   tools, domain terms, and responsibilities. Note the exact phrasing the
   employer uses; ATS matching is often literal.
2. **Build the keyword-gap table.** For each requirement mark one of:
   `Present` (appears in the resume), `Partial` (related experience exists but
   different wording), `Missing` (no evidence in the resume). Load
   `references/ats-rules.md` for matching rules.
3. **Rewrite bullets for `Present` and `Partial` items only.** Use the
   formula in `references/bullet-formula.md`. Keep every fact traceable to the
   original resume. Reword, reorder, and quantify only with numbers the user
   supplied.
4. **Handle `Missing` items honestly.** Do not add them to the resume. List
   them separately as "Gaps to address" with one line on how the user could
   speak to each in a cover letter or interview, or whether to skip the role.
5. **Run the ATS format check** from `references/ats-rules.md` and report
   issues (tables, columns, graphics, headers in images, unusual section
   names, missing contact line).
6. **Deliver** in this order: summary (2 lines), keyword-gap table, revised
   sections or bullets, gaps to address, ATS format notes.

## Never do

- Never invent employers, titles, dates, degrees, certifications, tools, or
  metrics.
- Never upgrade a `Partial` to `Present` by implying experience the resume
  does not show.
- Never remove a section the user asked to keep.
- Never search the web for the company or role; work from the text provided.

## Hand-off

End with one line offering the natural next step, for example drafting a
cover letter with `cover-letter` or preparing with `interview-prep`.
Explicit user instructions override this skill.
