# ATS matching and formatting rules

## Keyword matching

- Match the employer's exact terms where truthful ("PostgreSQL" vs
  "Postgres", "stakeholder management" vs "worked with stakeholders").
- Include both the acronym and the expansion the first time a term appears
  (e.g. "Applicant Tracking System (ATS)").
- Place the strongest matches in the summary and the most recent role.
- Mark a requirement `Partial` when the resume shows the capability under a
  different name or in an adjacent tool; rewrite using the employer's term
  only if the underlying work genuinely matches.
- Mark `Missing` when there is no evidence. Never bridge a gap by inference.

## Formatting checks

Flag any of the following:

- Multi-column layouts, text boxes, tables used for layout.
- Contact details or section headers inside images or page headers/footers.
- Non-standard section names ("My Journey" instead of "Experience").
- Dates missing month or year, or inconsistent date formats.
- Fonts or symbols that may not parse (icons for phone/email, fancy bullets).
- Missing one-line contact block: name, location, email, phone, link.
- Length: 1 page for under ~5 years of experience, 2 pages otherwise, unless
  the user specifies.

## Output table format

| Requirement (JD wording) | Status | Evidence in resume | Action |
|---|---|---|---|
| Python, 3+ years | Present | "Python backend services, 2021–2024" | Keep; move to summary |
| Kubernetes | Partial | "Deployed Docker services on ECS" | Reword only if K8s was used; otherwise list as gap |
| Series A fundraising | Missing | none | Address in cover letter or skip |
