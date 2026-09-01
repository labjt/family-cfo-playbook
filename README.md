# UHNW Family Wealth Playbook — SOP library

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
| 02 | [Engagement modes — Mode A / Mode B and the scoping rules](00-foundations/02-engagement-modes.md) | reference ·  beyond Bowen | A, B | LA |
| 03 | [Roles and RACI](00-foundations/03-roles-and-raci.md) | reference ·  beyond Bowen | A, B | LA |
| 05 | [Client meeting protocol — the wrapper for every meeting](00-foundations/05-client-meeting-protocol.md) | procedure | A, B | LA |

**Templates**

| # | Document | Type | Modes | Owner |
|---|---|---|---|---|
| 05 | [T05 — Engagement scoping worksheet](templates/T05-engagement-scoping-worksheet.md) | template ·  beyond Bowen | A, B | LA |

<!-- index:end -->

## Document types

| Type | What it is | Required sections |
|---|---|---|
| procedure | a repeatable process with an owner, trigger, steps, outputs | Purpose · Trigger · Roles · Timing · Inputs · Prep checklist · Procedure · Follow-up · Outputs and records · Do / Don't · Mode A / Mode B · Metrics · Related · Source |
| spec | the standard for a document the practice produces | Purpose · Contents · Standards · Refresh cadence · Owner · Mode A / Mode B · Related · Source |
| reference | tables, formulas, matrices the procedures point to | Purpose · … · Related · Source |
| template | a fill-in artifact | Purpose · How to use · body · Related · Source |

Authoring conventions: `build/_skeletons.md`.
