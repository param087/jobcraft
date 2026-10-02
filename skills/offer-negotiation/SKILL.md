---
name: offer-negotiation
description: Help the user evaluate a job offer and plan a negotiation using the offer details and market numbers they provide. Use when the user asks how to negotiate salary, respond to an offer, compare multiple offers, or write a counter-offer email. Does not supply live salary data.
---

# Plan an offer negotiation

## Inputs

- Offer details from the user: base, bonus, equity, sign-on, benefits, PTO,
  start date, location/remote terms, deadline to respond (as available).
- The user's priorities and walk-away point.
- Optional: competing offers, current compensation, market ranges the user
  has researched.

If the user has shared no offer details, ask for the components they know in
one message and stop. Otherwise proceed with what is given and mark unknowns.

## Procedure

1. **Summarize the offer** in a compact table. Where a component is unknown,
   write `unknown` — do not estimate it.
2. **Build the priority matrix** from `references/priority-matrix.md`: rank
   components as Must-improve / Nice-to-have / Fine as-is based on what the
   user said matters. If priorities were not stated, propose a ranking and
   ask the user to confirm in one line.
3. **Set the ask.** For each Must-improve item, propose a specific target
   and a fallback, using only ranges or comparables the user supplied. If the
   user has no market data, say so plainly and suggest what to look up
   (levels, location, company stage) rather than guessing a number.
4. **Write the counter-offer script**: a short spoken version (5–7 lines)
   and an email version (≤180 words). Tone: appreciative, specific,
   collaborative. One primary ask, one secondary. No ultimatums unless the
   user wants one.
5. **Anticipate responses.** Three likely replies from the employer and a
   one-line response to each (full yes, partial, no-movement).
6. **Deliver**: offer table, priority matrix, asks with fallbacks, scripts,
   responses. Finish with the recommended next action and timing relative to
   the response deadline.

## Never do

- Never state market salary figures as fact; the plugin has no live data.
- Never fabricate a competing offer or encourage the user to bluff one.
- Never provide tax or legal advice beyond suggesting the user consult a
  professional for equity or contract questions.
- Never send any message; return text for the user to send.

## Hand-off

Offer to log the outcome with `application-tracker`. Explicit user
instructions override this skill.
