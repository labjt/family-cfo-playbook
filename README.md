# The Family CFO Practice

**📖 Read it online → https://labjt.github.io/family-cfo-playbook/**

| | |
|---|---|
| [**The Primer**](https://labjt.github.io/family-cfo-playbook/primer.html) 🧭 | The whole practice in ten chapters, at three depths — read this first |
| [**The Playbook**](https://labjt.github.io/family-cfo-playbook/playbook.html) 🏛️ | The 38 procedures and 28 templates themselves |

---

## The library

Standard operating procedures for a wealth-management practice serving families with $30M to several hundred million, delivered as the family's **personal chief financial officer**. The library is a Bowen/CEG consultative-process spine with a Hughes family-systems layer and a Palaveev team-building section. Everything here is original procedural writing informed by those sources; nothing is reproduced from them (see `SOURCES.md`).

## How to use this library

1. **Start with Foundations.** `01` gives the model and operating principles, `02` the two engagement modes, `03` who does what, `04` client psychology, `05` the protocol every client meeting follows.
2. **Run the sequence.** New client: `10 → 12 → 14 → 15 → 16 → 20`. Existing client: `10` (Rediscovery variant) `→ 20`. Whole family (Mode A): `10 → 41 → 12 … → 43`.
3. **Use the templates.** Every procedure names the template it consumes or produces (`T01`–`T28`).
4. **Follow the callouts.** *Mode B* boxes say what changes when the Advisor serves an individual inside a larger family team. *Beyond Bowen* boxes mark content from Hughes, Palaveev, Bonner, or our own extension.
5. **Keep it alive.** `60` explains how the library is reviewed; `build/build.py --check` validates it; `build/build.py` renders `dist/sop-library.html` for sharing.

## The model in one screen

- **Wealth management = investment consulting + advanced planning + relationship management** (Bowen). Advanced planning = wealth enhancement + wealth transfer + wealth protection + charitable planning. Relationship management = client relationships + expert-network relationships.
- **Complete wealth = five capitals** — human, intellectual, social, spiritual, financial — with financial capital as the tool that grows the other four (Hughes). Time is measured in generations: 20 / 50 / 100 years.
- **The consultative sequence:** Discovery → +2 weeks Investment Plan → +1 week Mutual Commitment → +45 days Follow-up → +90 days first Regular Progress Meeting → recurring at the cadence the client chose in Discovery.
- **Two engagement modes.** Mode A — the whole family is under the Advisor's umbrella. Mode B — the Advisor serves one or more individuals inside a family that has its own central team; the mandate is scoped at intake (B-full / B-partial / B-narrow) and every procedure branches on it.
- **Default confidentiality rule.** An adult's personal information is never shared upward, sideways, or with a family's central team without that person's written consent recorded on T05 / T14.

## Roles at a glance

`LA` Lead Advisor · `SA` Service Advisor · `AA` Associate Advisor / Analyst · `CSA` Client Service Associate · `ISB` Internal Specialist Bench (sister-company experts) · `EEN` External Expert Network · `COA` Client's Other Advisors (Mode A) · `FCT` Family Central Team (Mode B). **Where a role is unfilled, the Lead Advisor performs it** — see `03`.

## Scope boundary

These SOPs cover client service delivery, advanced planning, the family layer, and team building. They do **not** cover business development (handled elsewhere), portfolio construction, trading, rebalancing, or manager selection (the firm's investment platform), or the firm's compliance manual. Where a step touches those, it says so and hands off.

## Placeholder key

`[Firm]` the Advisor's firm · `[Advisor]` the Lead Advisor by name · `[CRM]` client-relationship system · `[Custodian]` custodial platform · `[Planning software]` · `[Document vault]` secure client portal / binder · `[Trust Co.]` the firm's trust company · `[ESOP Co.]` the firm's ESOP advisory company · `[Firm Compliance]` · `[Firm shared services]` borrowed operations/admin capacity · `[Client]` / `[Family]` the client's name.

## Index

<!-- index:start -->
**Foundations**

| # | Document | Type | Modes | Owner |
|---|---|---|---|---|
| 01 | [The wealth management model and operating principles](00-foundations/01-wealth-management-model.md) | reference · beyond Bowen | A, B | LA |
| 02 | [Engagement modes — Mode A / Mode B and the scoping rules](00-foundations/02-engagement-modes.md) | reference · beyond Bowen | A, B | LA |
| 03 | [Roles and RACI](00-foundations/03-roles-and-raci.md) | reference · beyond Bowen | A, B | LA |
| 04 | [High-net-worth psychology — the nine personalities and how to serve each](00-foundations/04-hnw-psychology.md) | reference | A, B | LA |
| 05 | [Client meeting protocol — the wrapper for every meeting](00-foundations/05-client-meeting-protocol.md) | procedure | A, B | LA |

**Onboarding — CCM1 to CCM4**

| # | Document | Type | Modes | Owner |
|---|---|---|---|---|
| 10 | [CCM1 — Discovery Meeting (and the Rediscovery variant)](10-onboarding/10-ccm1-discovery-meeting.md) | procedure | A, B | LA |
| 11 | [Total Client Profile — the data model every meeting feeds](10-onboarding/11-total-client-profile.md) | spec · beyond Bowen | A, B | LA |
| 12 | [CCM2 — Investment Plan Meeting](10-onboarding/12-ccm2-investment-plan-meeting.md) | procedure | A, B | LA |
| 13 | [Investment plan and investment policy statement — document standard](10-onboarding/13-investment-plan-and-ips.md) | spec · beyond Bowen | A, B | LA |
| 14 | [CCM3 — Mutual Commitment Meeting](10-onboarding/14-ccm3-mutual-commitment-meeting.md) | procedure | A, B | LA |
| 15 | [Implementation and transfers — the window between commitment and follow-up](10-onboarding/15-implementation-and-transfers.md) | procedure · beyond Bowen | A, B | CSA |
| 16 | [CCM4 — 45-Day Follow-up Meeting](10-onboarding/16-ccm4-45-day-followup.md) | procedure | A, B | LA |

**Ongoing service — CCM5 and service standards**

| # | Document | Type | Modes | Owner |
|---|---|---|---|---|
| 20 | [CCM5 — Regular Progress Meeting](20-ongoing-service/20-ccm5-regular-progress-meeting.md) | procedure | A, B | LA |
| 21 | [Service standards and the contact plan](20-ongoing-service/21-service-standards-and-contact-plan.md) | procedure · beyond Bowen | A, B | LA |
| 22 | [Event-driven contact — red flags, shocks, and life events](20-ongoing-service/22-event-driven-contact.md) | procedure · beyond Bowen | A, B | LA |
| 23 | [Service failure recovery](20-ongoing-service/23-service-failure-recovery.md) | procedure | A, B | LA |
| 24 | [Quarterly reporting package](20-ongoing-service/24-quarterly-reporting-package.md) | procedure · beyond Bowen | A, B | LA |
| 25 | [Annual client satisfaction survey](20-ongoing-service/25-annual-client-satisfaction-survey.md) | procedure | A, B | LA |

**Advanced planning and the expert network**

| # | Document | Type | Modes | Owner |
|---|---|---|---|---|
| 30 | [The wealth management plan — document standard](30-advanced-planning/30-wealth-management-plan.md) | spec | A, B | LA |
| 31 | [Expert network — build, vet, and maintain](30-advanced-planning/31-expert-network.md) | procedure · beyond Bowen | A, B | LA |
| 32 | [Expert-network meeting — quarterly case review](30-advanced-planning/32-expert-network-meeting.md) | procedure | A, B | LA |
| 33 | [Coordinating with outside advisors — the family's central team and incumbent professionals](30-advanced-planning/33-coordinating-with-outside-advisors.md) | procedure · beyond Bowen | A, B | LA |

**Family layer — Mode A**

| # | Document | Type | Modes | Owner |
|---|---|---|---|---|
| 40 | [Family engagement model — who the client is, the family map, and the Advisor's stance](40-family-layer/40-family-engagement-model.md) | spec · beyond Bowen | A, B | LA |
| 41 | [Family discovery and the family executive summary](40-family-layer/41-family-discovery-and-executive-summary.md) | procedure · beyond Bowen | A, B | LA |
| 42 | [Family member onboarding](40-family-layer/42-family-member-onboarding.md) | procedure · beyond Bowen | A, B | LA |
| 43 | [Family meetings — standing rules, the first meeting and mission session, the annual family meeting](40-family-layer/43-family-meetings.md) | procedure · beyond Bowen | A, B | LA |
| 44 | [Family capitals assessment — the qualitative balance sheet and income statement](40-family-layer/44-family-capitals-assessment.md) | spec · beyond Bowen | A | LA |
| 45 | [Family governance readiness](40-family-layer/45-family-governance-readiness.md) | procedure · beyond Bowen | A | LA |
| 46 | [Trustee–beneficiary relationship](40-family-layer/46-trustee-beneficiary-relationship.md) | procedure · beyond Bowen | A, B | LA |
| 47 | [Family bank and investor allocation](40-family-layer/47-family-bank-and-investor-allocation.md) | procedure · beyond Bowen | A | LA |
| 48 | [Trust system design and review](40-family-layer/48-trust-system-design-and-review.md) | procedure · beyond Bowen | A, B | LA |

**Growth inside service**

| # | Document | Type | Modes | Owner |
|---|---|---|---|---|
| 50 | [Asks inside service meetings — held-away assets and introductions](50-growth-inside-service/50-asks-inside-service-meetings.md) | procedure | A, B | LA |

**Practice operations**

| # | Document | Type | Modes | Owner |
|---|---|---|---|---|
| 60 | [SOP maintenance and blueprinting](60-practice-ops/60-sop-maintenance.md) | procedure | A, B | LA |

**Team building**

| # | Document | Type | Modes | Owner |
|---|---|---|---|---|
| 70 | [Team roadmap — from solo with borrowed expertise to an ensemble](70-team-building/70-team-roadmap.md) | reference · beyond Bowen | A, B | LA |
| 71 | [Engaging borrowed expertise — the internal bench and shared services](70-team-building/71-engaging-borrowed-expertise.md) | procedure · beyond Bowen | A, B | LA |
| 72 | [Hiring a team member](70-team-building/72-hiring-a-team-member.md) | procedure · beyond Bowen | A, B | LA |
| 73 | [Onboarding a team member and transitioning relationships](70-team-building/73-onboarding-and-relationship-transition.md) | procedure · beyond Bowen | A, B | LA |
| 74 | [Team operating rhythm — meetings, reviews, quality control and culture](70-team-building/74-team-operating-rhythm.md) | procedure · beyond Bowen | A, B | LA |

**Templates**

| # | Document | Type | Modes | Owner |
|---|---|---|---|---|
| 01 | [T01 — Client correspondence](templates/T01-client-correspondence.md) | template | A, B | CSA |
| 02 | [T02 — Meeting agendas](templates/T02-meeting-agendas.md) | template | A, B | CSA |
| 03 | [T03 — Discovery interview guide](templates/T03-discovery-interview-guide.md) | template · beyond Bowen | A, B | LA |
| 04 | [T04 — Total Client Profile outline (two-level)](templates/T04-total-client-profile-outline.md) | template · beyond Bowen | A, B | AA |
| 05 | [T05 — Engagement scoping worksheet](templates/T05-engagement-scoping-worksheet.md) | template · beyond Bowen | A, B | LA |
| 06 | [T06 — Investment plan and IPS outline](templates/T06-investment-plan-and-ips-outline.md) | template · beyond Bowen | A, B | AA |
| 07 | [T07 — Implementation tracker](templates/T07-implementation-tracker.md) | template · beyond Bowen | A, B | CSA |
| 08 | [T08 — Client notebook index](templates/T08-client-notebook-index.md) | template · beyond Bowen | A, B | CSA |
| 09 | [T09 — Expert-network meeting pack](templates/T09-expert-network-meeting-pack.md) | template | A, B | AA |
| 10 | [T10 — Advanced-planning tracker](templates/T10-advanced-planning-tracker.md) | template | A, B | AA |
| 11 | [T11 — Quarterly reporting package outline](templates/T11-quarterly-reporting-package-outline.md) | template · beyond Bowen | A, B | AA |
| 12 | [T12 — Service quality instruments](templates/T12-service-quality-instruments.md) | template · beyond Bowen | A, B | LA |
| 13 | [T13 — Scripts sheet](templates/T13-scripts-sheet.md) | template | A, B | LA |
| 14 | [T14 — Family map and matrices](templates/T14-family-map-and-matrices.md) | template · beyond Bowen | A | LA |
| 15 | [T15 — Annual service calendar](templates/T15-annual-service-calendar.md) | template · beyond Bowen | A, B | CSA |
| 16 | [T16 — Family meeting pack](templates/T16-family-meeting-pack.md) | template · beyond Bowen | A | LA |
| 17 | [T17 — Family executive summary pack](templates/T17-family-executive-summary.md) | template · beyond Bowen | A | LA |
| 18 | [T18 — Family balance sheet and income statement](templates/T18-family-balance-sheet-and-income-statement.md) | template · beyond Bowen | A | LA |
| 19 | [T19 — Rising-generation learning map](templates/T19-rising-generation-learning-map.md) | template · beyond Bowen | A | LA |
| 20 | [T20 — Family bank charter and loan application](templates/T20-family-bank-charter-and-loan-application.md) | template · beyond Bowen | A | LA |
| 21 | [T21 — Structure summary and communication plan](templates/T21-structure-summary-and-communication-plan.md) | template · beyond Bowen | A, B | AA |
| 22 | [T22 — Trustee–beneficiary meeting pack](templates/T22-trustee-beneficiary-meeting-pack.md) | template · beyond Bowen | A, B | LA |
| 23 | [T23 — Distribution request and decision memo](templates/T23-distribution-request-and-decision-memo.md) | template · beyond Bowen | A, B | LA |
| 24 | [T24 — Family Trust Review outline, ten-year review worksheet, and fiduciary selection questionnaire](templates/T24-family-trust-review-outline.md) | template · beyond Bowen | A, B | LA |
| 25 | [T25 — Specialist engagement scope memo and bench scorecard](templates/T25-specialist-engagement-scope-memo.md) | template · beyond Bowen | A, B | LA |
| 26 | [T26 — Job description, scorecard and interview guide](templates/T26-job-description-scorecard-interview-guide.md) | template · beyond Bowen | A, B | LA |
| 27 | [T27 — Onboarding plan, meeting-role menu and client introduction](templates/T27-onboarding-plan-and-client-introduction.md) | template · beyond Bowen | A, B | LA |
| 28 | [T28 — Team meeting agendas, dashboard, capacity check and bogey worksheet](templates/T28-team-meeting-agendas-and-dashboard.md) | template · beyond Bowen | A, B | LA |

<!-- index:end -->

## Document types

| Type | What it is | Required sections |
|---|---|---|
| procedure | a repeatable process with an owner, trigger, steps, outputs | Purpose · Trigger · Roles · Timing · Inputs · Prep checklist · Procedure · Follow-up · Outputs and records · Do / Don't · Mode A / Mode B · Metrics · Related · Source |
| spec | the standard for a document the practice produces | Purpose · Contents · Standards · Refresh cadence · Owner · Mode A / Mode B · Related · Source |
| reference | tables, formulas, matrices the procedures point to | Purpose · … · Related · Source |
| template | a fill-in artifact | Purpose · How to use · body · Related · Source |

Authoring conventions: `build/_skeletons.md`.
