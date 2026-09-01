---
id: sop-60
title: "SOP maintenance and blueprinting"
type: procedure
section: 60-practice-ops
owner: LA
modes: [A, B]
source:
  bowen: ["Ch. 6 — blueprint every client-experience and business system; precisely define, perfect and write it down; staff have access and improve it; the founder does not blueprint alone", "Ch. 6 — service failures resolved same day and used to improve the system"]
  hughes: []
  other: ["Palaveev — the service-process definition checklist; hiring before the recipes exist as the named failure mode (paraphrased)"]
extension: false
status: draft
updated: 2026-09-01
---

# 60 — SOP maintenance and blueprinting

This library is the practice's blueprint. It is only worth what it says today, so it is reviewed on a calendar, corrected whenever a service failure or a new hire exposes a gap, validated by the build tooling, and published in one shareable page. This procedure is how that happens and who does it.

## Purpose

- Keep every procedure precise, current and actually followed — the difference between a documented system and a good intention.
- Turn service failures and new-hire questions into SOP improvements within the month.
- Make the library the training curriculum and the proof, for the firm and for clients, that the practice runs on a system.

## Trigger

Quarterly (SOP 74) and annually (T15, Q1 slot); and on any event: a service failure traced to a procedure (SOP 23), a new hire's question during onboarding (SOP 73), a regulatory or firm-policy change, a new service or template, or a document's `updated` date passing twelve months.

## Roles

Owner: LA · Does: CSA as librarian (status tracking, build runs, change log, publishing), each document's owner for its review · Consulted: SA/AA as peer reviewers of changes; [Firm Compliance] for anything touching disclosures, consent or recording.

## Timing

| Cadence | Action |
|---|---|
| Continuous | Change requests logged as they arise |
| Monthly | Service-failure log mapped to SOP steps (SOP 74) |
| Quarterly | SOP review in the quarterly meeting: changed, failed, missing |
| Annually (Q1) | Every document read by its owner; coverage audit; rebuild and republish; version tag |
| On hire | The new hire's questions reviewed at the 90-day review and fixed |

## Inputs

- Service-failure log (SOP 23); onboarding questions (SOP 73); quarterly-review notes (SOP 74).
- The build tooling: `python3 build/build.py --check`, `--write-index`, `--write-sources`, and the build itself.
- `build/_skeletons.md` — the conventions every document follows.

## Prep checklist

- [ ] Change log current in the team folder (date, document, what changed, why, who reviewed).
- [ ] For the annual review: each owner has the list of documents they own with `updated` dates.
- [ ] `--check` passes on the current library before edits begin.

## Procedure

1. **Own the library.** The LA is accountable for the content; the CSA is the librarian who tracks status, runs the tooling and publishes. Every document has an owner in its front matter.
2. **Keep the status lifecycle.** `draft` → `in use` (after the LA has run it once with a client) → `reviewed` with a new `updated` date at each annual review. A document with an `updated` date older than twelve months is flagged in the quarterly review.
3. **Change control.** Anyone may propose a change; the document's owner drafts it; a second professional peer-reviews it (for a one-professional practice, the LA reviews the CSA's drafts and a sister-company colleague reviews the LA's when the change is material); the LA approves. Changes that alter what a client experiences — a meeting's structure, a report, a contact rule — are communicated to affected clients in the next confirmation letter or progress meeting (SOP 21), never discovered by them.
4. **Map every service failure to a step.** In the monthly review, each entry in the failure log is traced to a procedure step that was missing, unclear or skipped. Missing or unclear → change request; skipped → coaching, and a check on whether the step is realistic.
5. **Run the quarterly SOP review** (SOP 74 item): documents changed this quarter; documents implicated in failures; gaps noticed in client work; templates that were worked around rather than used — a workaround is a template defect.
6. **Run the annual review (Q1).** Every owner reads every document they own with a client from the last quarter in mind and either confirms it or changes it. Then the coverage audit below. Then the rebuild: `--check` must pass; `--write-index` and `--write-sources` regenerate the README index and SOURCES; the build produces the shareable page; the repository is tagged with the year.
7. **Treat the library as the curriculum.** New hires read it in the order set in SOP 73 and log every question; the 90-day review turns those questions into changes. A question a new hire had to ask is a sentence the document is missing.
8. **Invite improvement from the people who run the steps.** The CSA and SA carry out most of the procedures daily and see the friction first; their suggestions are reviewed within the quarter and credited in the change log. The founder does not blueprint alone.
9. **Publish and share.** After each annual review and after any material change, republish the page and tell the team where the current version is. Old versions are kept for reference, never used.

!!! extension "Beyond Bowen"
    **Service-process coverage audit** — once a year, confirm the library answers each of these for the practice; every "no" or "unclear" becomes a change request.

    - What information do we collect from a prospective and current client, where is it stored, and how is it secured?
    - How are services proposed, with what documents, and who signs off?
    - How is the fee determined for each segment and scope (T05; SOP 14)?
    - Which legal documents and disclosures does each engagement require, and who checks them?
    - What is the scope of planning we deliver, with which tool, and what exceptions are permitted?
    - What is the investment philosophy, how is it implemented, and which decisions belong to the firm's platform rather than to us?
    - When is a portfolio or a report customized, and how is that customization priced?
    - Which reports go to which clients, on what cadence?
    - Who is each client's point of contact, for what, and in which situations does that change?
    - How often does each segment meet us, and what is the standard preparation?
    - How are plans, portfolios and client data reviewed and updated, and how are changes decided, implemented and recorded?
    - Who trades and how (platform), and what do we verify?
    - How does the investment committee (firm) communicate decisions to us, and how do we pass them to clients?
    - What is the quality-control process that prevents errors in plans, portfolios and documents?
    - Which steps in the library are performed by borrowed specialists or vendors, and what would happen if each disappeared tomorrow?

## Follow-up

- Within the week: change requests from failures and new-hire questions logged.
- Within the quarter: changes drafted, peer-reviewed, approved, and clients told where the experience changes.
- Annually: rebuild, republish, tag; the coverage audit's open items carried into the next quarter's list.

## Outputs and records

| Output | Where it lives | Owner |
|---|---|---|
| Change log | Team folder | CSA |
| Updated documents with new `updated` dates and status | Library | Document owner |
| `--check` result, README index, SOURCES | Library (generated) | CSA |
| Published page and version tag | `dist/` and the shared link; repository tag | CSA |
| Coverage-audit results and open items | Team folder; quarterly review | LA |

## Do / Don't

**Do**

- Change the document, not just the behavior; a fix that lives in one person's head is not a fix.
- Keep the tooling green — a broken link or a missing section is a symptom of a document nobody is using.
- Credit the people who improve the blueprints.

**Don't**

- Don't hire before the recipes are written; the first professional's productivity depends on this library existing.
- Don't let documents drift into "everyone knows we don't really do that" — remove or fix the step.
- Don't change a client-facing procedure without telling the affected clients.

## Mode A / Mode B

### Mode A — whole family

- Family-layer documents (40–48) are reviewed with the last family meeting and trustee cycle in mind; T14 and T16 usage is part of the audit.

### Mode B — individual within a larger team

- SOP 33 and T05 are reviewed against every current FCT protocol; any protocol a family's central team imposed in writing is reflected in the library, not held only in email.

## Metrics

- Documents with an `updated` date within twelve months (target 100%).
- Service failures mapped to an SOP step within the month (target 100%).
- New-hire questions converted to changes by the 90-day review (count; trend down over successive hires).

## Related

- [SOP 74 — Team operating rhythm](../70-team-building/74-team-operating-rhythm.md) · [SOP 73 — Onboarding and relationship transition](../70-team-building/73-onboarding-and-relationship-transition.md)
- [SOP 23 — Service failure recovery](../20-ongoing-service/23-service-failure-recovery.md) · [SOP 21 — Service standards and contact plan](../20-ongoing-service/21-service-standards-and-contact-plan.md)
- [T15 — Annual service calendar](../templates/T15-annual-service-calendar.md)
- Conventions: `build/_skeletons.md`

## Source

- Bowen, *Breaking Through*, Ch. 6 — blueprint every client-experience and business system; write it down precisely; give staff access and invite improvement; assign the blueprinting to key staff under the founder's guidance; resolve and learn from service failures (adapted).
- Palaveev, *The Ensemble Practice*, Ch. 3 and 12 — write the recipes before hiring; the service-process definition questions (paraphrased and rewritten as our coverage audit).
- Extension — the status lifecycle, change control and tooling steps are ours.

### Appendix — fields the library assumes exist in [CRM]

| Field | Set by | Used by |
|---|---|---|
| Process preference (how and how often the client wants contact) | SOP 10 | 05, 20, 21, 22 |
| Personality note (SOP 04 type and cues) | SOP 10 | 05, 12, 20 |
| Mode and scope rung; who is the client; who may instruct | SOP 02 / T05 | all |
| Consent flags (what may be shared with whom) | T05 / T14 | 05, 21, 22, 33, 71 |
| Red flags and next-contact triggers | SOP 22 | 21, 74 |
| Asks log (assets and introductions: date, outcome, thank-you sent) | SOP 50 | 14, 16, 20 |
| Second-chair and relationship-manager / owner status | SOP 73 | 21, 74 |
| Borrowed-specialist engagements and hours | SOP 71 | 70, 74 |
| Service-failure entries and resolution | SOP 23 | 60, 74 |
