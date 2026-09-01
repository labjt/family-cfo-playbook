# Authoring conventions and skeletons

This file is the style guide for every document in the library. `build/build.py --check` enforces the parts that can be checked mechanically.

## Files, ids, anchors

| Kind | Folder | File name | `id` | Anchor in the HTML |
|---|---|---|---|---|
| SOP (procedure / spec / reference) | `NN-section/` | `NN-kebab-title.md` | `sop-NN` | `#sop-NN` |
| Template | `templates/` | `TNN-kebab-title.md` | `t-NN` | `#t-NN` |

Numbers are fixed by the plan; never renumber. Sections: `00-foundations`, `10-onboarding`, `20-ongoing-service`, `30-advanced-planning`, `40-family-layer`, `50-growth-inside-service`, `60-practice-ops`, `70-team-building`, `templates`.

## Front matter (every file)

```yaml
---
id: sop-10
title: "CCM1 — Discovery Meeting"
type: procedure            # procedure | spec | reference | template
section: 10-onboarding
owner: LA                  # role abbreviation that owns the doc
modes: [A, B]              # engagement modes the doc applies to: [A], [B], or [A, B]
source:
  bowen: ["Ch. 4 — Discovery Meeting steps and scripts"]
  hughes: ["Compact — essential questions", "Family Wealth — passion/mentor questions"]
  other: []                # Palaveev / Bonner / "extension" notes
extension: false           # true if the doc's core content goes beyond Bowen
status: draft
updated: 2026-09-01
---
```

## Document types and required H2 headings (exact text, this order)

**procedure** — `## Purpose` · `## Trigger` · `## Roles` · `## Timing` · `## Inputs` · `## Prep checklist` · `## Procedure` · `## Follow-up` · `## Outputs and records` · `## Do / Don't` · `## Mode A / Mode B` (only if `modes: [A, B]`) · `## Metrics` · `## Related` · `## Source`

**spec** (a document standard) — `## Purpose` · `## Contents` · `## Standards` · `## Refresh cadence` · `## Owner` · `## Mode A / Mode B` (if both modes) · `## Related` · `## Source`

**reference** — `## Purpose`, then free-form H2s, then `## Related` · `## Source`

**template** — `## Purpose` · `## How to use` · the template body under its own H2s · `## Related` · `## Source`

## Callouts (python-markdown admonitions; indent the body four spaces)

```markdown
!!! modeB "Mode B"
    What changes when the Advisor serves an individual inside a larger family team.

!!! extension "Beyond Bowen"
    Content that comes from Hughes / Palaveev / Bonner or is our own extension — never attribute it to Bowen.

!!! script "Say something like"
    "I'm glad you're here. Our purpose today is to find out whether we are the right firm for your family."

!!! note "Note"
    Neutral aside.

!!! warning "Caution"
    Compliance, confidentiality, or a known failure mode.
```

## Cross-links

Link to other documents with a relative path and the doc's number in the link text so the reference survives in print:
`[SOP 11 — Total Client Profile](../10-onboarding/11-total-client-profile.md)` · `[T03](../templates/T03-discovery-interview-guide.md)`.
The build rewrites these to in-page anchors. Deep links: `(../file.md#heading-slug)`.

## Placeholders

Square-bracketed, Title Case, no markdown link after them. The build highlights them. Use only these unless a new one is unavoidable (then add it to README's placeholder key):
`[Firm]` `[Advisor]` `[CRM]` `[Custodian]` `[Planning software]` `[Document vault]` `[Trust Co.]` `[ESOP Co.]` `[Firm Compliance]` `[Firm shared services]` `[Client]` `[Family]`.

Do not write a bare capitalised word in square brackets for any other purpose (it will be highlighted as a placeholder).

## Roles (abbreviations used in every doc)

`LA` Lead Advisor · `SA` Service Advisor · `AA` Associate Advisor / Analyst · `CSA` Client Service Associate · `ISB` Internal Specialist Bench (sister-company experts) · `EEN` External Expert Network · `COA` Client's Other Advisors (Mode A) · `FCT` Family Central Team (Mode B) · `[Firm Compliance]`.
Where a role is unfilled today, the LA performs it (see `03-roles-and-raci.md`). SOPs name roles, never people.

## Style rules

- Imperative voice, second person implied ("Send the confirmation within 24 hours"). Numbered steps in `## Procedure`; sub-steps as nested lists.
- Checklists as `- [ ]` items. Tables for role × step, trigger × response, and any matrix.
- Scripts: two sentences at most, adapted to a $30M+ family, inside a `!!! script` callout. Never reproduce book text; paraphrase and cite.
- Timing lives in `## Timing` (relative to the previous step: "+2 weeks after CCM1").
- `## Roles` is a one-line RACI: `Owner: LA · Does: CSA (prep, confirmations), AA (packet) · Consulted: ISB as needed`.
- `## Metrics`: at most three, each measurable from the CRM or calendar.
- `## Related`: bullet list of links.
- `## Source`: one bullet per source, e.g. `- Bowen, *Breaking Through*, Ch. 4 — Discovery Meeting overview and critical success factors (adapted).` `- Hughes, *Complete Family Wealth*, Ch. 15 — Family Executive Summary process (paraphrased).` `- Extension — not in any source.`
- Length: procedures 150–350 lines; specs 100–250; references 60–200; templates 60–200. Dense beats long.
- Mode A / Mode B section: two sub-headings `### Mode A — whole family` and `### Mode B — individual within a larger team`, each 2–8 bullets stating only what *differs* from the main procedure. Reference the scope rung (B-full / B-partial / B-narrow) where it matters.
- Every `!!! extension` block must sit in a doc whose front matter says `extension: true`, or the doc must cite the source in `## Source`.

## Skeleton — procedure

```markdown
---
(front matter)
---

# NN — Title

One-paragraph summary of what this procedure produces and where it sits in the sequence.

## Purpose
## Trigger
## Roles
Owner: … · Does: … · Consulted: …
## Timing
## Inputs
## Prep checklist
- [ ] …
## Procedure
1. **Step name.** What to do. Why (one clause).
2. …
## Follow-up
- Within 24 hours: …
- Within one week: …
## Outputs and records
| Output | Where it lives | Owner |
## Do / Don't
**Do** … **Don't** …
## Mode A / Mode B
### Mode A — whole family
### Mode B — individual within a larger team
## Metrics
## Related
## Source
```

## Skeleton — spec

```markdown
# NN — Title
## Purpose
## Contents
### Section 1 …
## Standards
## Refresh cadence
## Owner
## Mode A / Mode B
## Related
## Source
```

## Skeleton — template

```markdown
# TNN — Title
## Purpose
## How to use
## (Template body — headings, tables, blanks marked with `______` or `[Client]`)
## Related
## Source
```

## Canonical file list (link targets — use these exact paths)

```
00-foundations/01-wealth-management-model.md          sop-01 reference
00-foundations/02-engagement-modes.md                 sop-02 reference
00-foundations/03-roles-and-raci.md                   sop-03 reference
00-foundations/04-hnw-psychology.md                   sop-04 reference
00-foundations/05-client-meeting-protocol.md          sop-05 procedure
10-onboarding/10-ccm1-discovery-meeting.md            sop-10 procedure
10-onboarding/11-total-client-profile.md              sop-11 spec
10-onboarding/12-ccm2-investment-plan-meeting.md      sop-12 procedure
10-onboarding/13-investment-plan-and-ips.md           sop-13 spec
10-onboarding/14-ccm3-mutual-commitment-meeting.md    sop-14 procedure
10-onboarding/15-implementation-and-transfers.md      sop-15 procedure
10-onboarding/16-ccm4-45-day-followup.md              sop-16 procedure
20-ongoing-service/20-ccm5-regular-progress-meeting.md        sop-20 procedure
20-ongoing-service/21-service-standards-and-contact-plan.md   sop-21 procedure
20-ongoing-service/22-event-driven-contact.md                 sop-22 procedure
20-ongoing-service/23-service-failure-recovery.md             sop-23 procedure
20-ongoing-service/24-quarterly-reporting-package.md          sop-24 procedure
20-ongoing-service/25-annual-client-satisfaction-survey.md    sop-25 procedure
30-advanced-planning/30-wealth-management-plan.md             sop-30 spec
30-advanced-planning/31-expert-network.md                     sop-31 procedure
30-advanced-planning/32-expert-network-meeting.md             sop-32 procedure
30-advanced-planning/33-coordinating-with-outside-advisors.md sop-33 procedure
40-family-layer/40-family-engagement-model.md                 sop-40 spec
40-family-layer/41-family-discovery-and-executive-summary.md  sop-41 procedure
40-family-layer/42-family-member-onboarding.md                sop-42 procedure
40-family-layer/43-family-meetings.md                         sop-43 procedure
40-family-layer/44-family-capitals-assessment.md              sop-44 spec
40-family-layer/45-family-governance-readiness.md             sop-45 procedure
40-family-layer/46-trustee-beneficiary-relationship.md        sop-46 procedure
40-family-layer/47-family-bank-and-investor-allocation.md     sop-47 procedure
40-family-layer/48-trust-system-design-and-review.md          sop-48 procedure
50-growth-inside-service/50-asks-inside-service-meetings.md   sop-50 procedure
60-practice-ops/60-sop-maintenance.md                         sop-60 procedure
70-team-building/70-team-roadmap.md                           sop-70 reference
70-team-building/71-engaging-borrowed-expertise.md            sop-71 procedure
70-team-building/72-hiring-a-team-member.md                   sop-72 procedure
70-team-building/73-onboarding-and-relationship-transition.md sop-73 procedure
70-team-building/74-team-operating-rhythm.md                  sop-74 procedure
templates/T01-client-correspondence.md                        t-01
templates/T02-meeting-agendas.md                              t-02
templates/T03-discovery-interview-guide.md                    t-03
templates/T04-total-client-profile-outline.md                 t-04
templates/T05-engagement-scoping-worksheet.md                 t-05
templates/T06-investment-plan-and-ips-outline.md              t-06
templates/T07-implementation-tracker.md                       t-07
templates/T08-client-notebook-index.md                        t-08
templates/T09-expert-network-meeting-pack.md                  t-09
templates/T10-advanced-planning-tracker.md                    t-10
templates/T11-quarterly-reporting-package-outline.md          t-11
templates/T12-service-quality-instruments.md                  t-12
templates/T13-scripts-sheet.md                                t-13
templates/T14-family-map-and-matrices.md                      t-14
templates/T15-annual-service-calendar.md                      t-15
templates/T16-family-meeting-pack.md                          t-16
templates/T17-family-executive-summary.md                     t-17
templates/T18-family-balance-sheet-and-income-statement.md    t-18
templates/T19-rising-generation-learning-map.md               t-19
templates/T20-family-bank-charter-and-loan-application.md     t-20
templates/T21-structure-summary-and-communication-plan.md     t-21
templates/T22-trustee-beneficiary-meeting-pack.md             t-22
templates/T23-distribution-request-and-decision-memo.md       t-23
templates/T24-family-trust-review-outline.md                  t-24
templates/T25-specialist-engagement-scope-memo.md             t-25
templates/T26-job-description-scorecard-interview-guide.md    t-26
templates/T27-onboarding-plan-and-client-introduction.md      t-27
templates/T28-team-meeting-agendas-and-dashboard.md           t-28
```
