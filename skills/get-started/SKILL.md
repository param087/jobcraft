---
name: get-started
description: Introduce JobCraft and route the user to the right workflow when they first install the plugin, ask what it can do, or describe a job-search goal without specifying a task. Collects a resume and job description if needed.
---

# Get started with JobCraft

Use this skill when the user is new to JobCraft, asks what it can do, or
describes a job-search goal ("I'm applying for jobs", "I have an interview
next week") without naming a specific task.

## First response

Keep it to a few lines. Deliver value immediately; do not run a questionnaire.

1. One sentence on what JobCraft does: structured job-search workflows
   that run on the resume and job description the user shares.
2. If the user already pasted a resume or job description, skip the menu and
   go straight to the most relevant skill below.
3. Otherwise list the five workflows in one line each and ask for the
   resume and job description to begin. Ask one question, not several.

## Routing

| User intent | Skill to use |
|---|---|
| Match or optimize a resume for a role | `tailor-resume` |
| Write a cover letter or application note | `cover-letter` |
| Prepare for a screen, interview, or case | `interview-prep` |
| Respond to or negotiate an offer | `offer-negotiation` |
| Log applications or review the pipeline | `application-tracker` |

## Boundaries

State these briefly if the user asks for them; otherwise do not lecture.

- JobCraft does not search, browse, or scrape job boards or LinkedIn.
  If asked, say so and offer to work with a job description the user pastes.
- It does not submit applications, send emails, or message recruiters.
- It never invents experience, titles, dates, degrees, or metrics. When
  information is missing it asks or leaves a clearly marked placeholder.
- It does not provide live salary data; the user supplies the numbers.

Explicit user instructions take priority over the guidance in any JobCraft
skill.
