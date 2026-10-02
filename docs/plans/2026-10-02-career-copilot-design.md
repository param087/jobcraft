# JobCraft — Design

**Date:** 2026-10-02
**Status:** Approved
**Platform:** ChatGPT / Codex Plugins (universal directory), skills-only shape

## Goal

Ship a skills-only plugin to the public plugin directory for distribution and
visibility. No MCP server, no hosting, no third-party integrations.

## Positioning

"Job search workflows that run on *your* documents." Users paste or attach a
resume and a job description. The plugin never fetches from job boards or
LinkedIn (avoids the unofficial-connector and scraping rules in the plugin
guidelines).

## Skills

| Skill | Trigger | Input | Output |
|---|---|---|---|
| `get-started` (onboarding) | first use / "what can you do" | none | one-line intro, asks for resume + JD, lists skills |
| `tailor-resume` | tailor/optimize resume for a JD | resume + JD | keyword-gap table, rewritten bullets, ATS notes |
| `cover-letter` | write a cover letter | resume + JD (+ tone) | ≤300-word letter, unverifiable facts flagged |
| `interview-prep` | prep for an interview | JD + resume (+ company) | question bank by category, STAR drafts, questions to ask |
| `offer-negotiation` | negotiate an offer | offer details from user | priority matrix, counter script, email template |
| `application-tracker` | track applications / pipeline | status updates | markdown table the user owns, in-chat |

## Intentional exclusions (drive negative test cases + refusal copy)

- No job-board / LinkedIn search or scraping
- No auto-submitting applications or sending emails
- No fabricated experience, degrees, titles, dates, or metrics
- No live salary/market data claims; user supplies ranges

## Skill authoring rules

- `description` = trigger conditions; body = procedure.
- Produce output on the first turn; at most one clarifying question.
- Explicit "never infer" list in every skill.
- User instructions override skill guidance.
- End each skill by handing control back and naming the next skill.

## Package

Portable Agent Plugins layout: root `plugin.json` with
`extensions.com.openai.interface`, `skills/<name>/SKILL.md`, `assets/`.
No `.app.json`, no `hooks/` (those block submission).

## Testing

- `scripts/validate.py` checks manifest schema-lite rules and SKILL.md
  frontmatter.
- Local install via `~/.agents/plugins/marketplace.json` → ChatGPT desktop.
- Manual test matrix in README (direct / indirect / missing input /
  out-of-scope / fabrication bait per skill).

## Risks

- Docs: skills-only plugins "may be subject to additional eligibility
  requirements." Mitigation: ship; fallback is workspace/personal marketplace.
- Listing URLs (website/support/privacy/ToS) needed to avoid dashboard
  warnings; host a static page.
