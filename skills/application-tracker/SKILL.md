---
name: application-tracker
description: Maintain a job-application tracker table in the conversation. Use when the user wants to log an application, update its status, review their pipeline, see what needs follow-up, or export the tracker. Data lives only in the chat and files the user keeps.
---

# Track job applications

## How the tracker works

The tracker is a markdown table the user owns. It exists only in the
conversation (and any file the user saves). Nothing is stored elsewhere.
Reproduce the full table after every change so it is always current.

## Inputs

- A new application (company, role, date, source, status, link, notes), or
- A status update ("heard back from Acme", "rejected by Globex"), or
- A request to review the pipeline or export it.

If the user wants to start tracking but gives no entries, show the empty
template from `assets/tracker-template.md` and ask for the first application
in one line.

## Procedure

1. **Locate the current table** in the conversation. If the user pasted a
   CSV or table, adopt it as the source of truth.
2. **Apply the change.** Add a row, update the Status and Last update
   columns, or append to Notes. Use the status vocabulary in the template.
   Record only what the user told you; never infer a status.
3. **Flag follow-ups.** Any row in Applied or Interviewing with no update in
   7+ days gets a one-line nudge under the table (dates come from the table;
   if a date is missing, ask rather than assume).
4. **Pipeline review** when asked: counts by status, upcoming interviews,
   stale items, and any offer deadlines.
5. **Export** when asked: output the table as CSV in a code block the user
   can copy or save.
6. **Deliver**: the updated full table, then follow-up flags, then a one-line
   next action.

## Never do

- Never invent companies, dates, or statuses.
- Never delete rows without an explicit instruction; mark them Withdrawn or
  Rejected instead.
- Never contact companies, check inboxes, or browse job boards.

## Hand-off

If the user adds an application without tailored materials, offer
`tailor-resume` or `cover-letter`. If a row moves to Offer, offer
`offer-negotiation`. Explicit user instructions override this skill.
