# Trustify — Incident Response Playbook

**Project:** Indonesia Banking Cyber Resilience Assessment — November 2026
**Version:** 0.2 | **Status:** Draft, simulated tabletop only
**Authority:** Illustrative response guidance; not approved by a real financial institution.

## Purpose and activation
This playbook coordinates detection, triage, containment, recovery and post-incident review for three hypothetical scenarios: compromised banking credentials (CR-001), ransomware-related service disruption (CR-002), and delayed escalation of suspicious transactions (CR-003). Activation is a simulated decision by the Incident Commander (IC); no real banking system is accessed.

## Roles and accountability (simulated)
| Role | Responsibility | Decision authority |
|---|---|---|
| Incident Commander | Owns severity, coordination and decisions | Declares simulated incident and escalation |
| SOC Analyst | Validates alerts, preserves evidence | Recommends containment |
| IAM Lead | Reviews authentication and privileged access | Approves simulated IAM changes |
| Business Continuity Lead | Assesses recovery readiness, RTO/RPO | Recommends restoration |
| Fraud Risk Lead | Assesses transaction anomalies | Recommends escalation/holds |
| Legal/Privacy Lead | Evaluates data exposure and notification obligations | Advises on legal applicability; does not assert compliance |
| Executive Sponsor | Reviews business impact and material decisions | Approves high-impact decisions when required |

## Common incident lifecycle
1. **Detect and register:** Record timestamp, scenario ID, alert source and whether data are synthetic.
2. **Triage:** Classify suspected impact to confidentiality, integrity, availability, customer trust and financial operations. Treat severity as provisional.
3. **Preserve evidence:** Record original source, hash where appropriate, custodian, collection time and access permissions. Do not upload credentials or customer data.
4. **Contain:** Propose actions and document authorization. Never represent simulated containment as an actual production change.
5. **Investigate:** Correlate relevant evidence and record competing hypotheses, uncertainty and gaps.
6. **Recover:** Confirm recovery prerequisites, approvals, test outcomes and monitoring; do not infer readiness from synthetic timings alone.
7. **Communicate:** Use the escalation matrix and involve legal/privacy stakeholders before making any notification assertion.
8. **Review:** Document decisions, unresolved findings, owners, deadlines and verification requirements.

## Scenario A — Credential theft and suspicious login (CR-001)
**Trigger:** Simulated anomalous authentication event or MFA coverage gap.
**Evidence:** `04-compliance/tests/synthetic-login-events.csv`, `TEST-001-mfa-results.csv`, `TEST-001-R1-mfa-results.csv`, `TEST-002-detection-alerts.csv`, `FIND-001-mfa-remediation.md`.

- Validate event format and timestamps; correlate user/account identifiers only in synthetic data.
- Determine whether privileged access or customer identity workflows are in scope.
- Recommend revocation of sessions, credential reset, stronger MFA and monitoring as **hypothetical** controls.
- Retain baseline TEST-001 failure and subsequent simulated remediation retest as separate historical results.
- **Current observation:** FIND-001 is marked *closed — simulated remediation verified*. This does not demonstrate production-bank MFA effectiveness.

## Scenario B — Ransomware and recovery (CR-002)
**Trigger:** Hypothetical encryption or unavailability of critical banking services.
**Evidence:** `TEST-003-ransomware-tabletop.md`, `TEST-003-recovery-plan.md`, `TEST-003-recovery-metrics.csv`, `TEST-003-recovery-approval.csv`, `TEST-003-decision-log.csv`, `FIND-002-recovery-governance.md`.

- Isolate affected segments in the tabletop scenario and document who would authorize it.
- Assess backup integrity, dependency mapping and recovery sequence.
- Compare synthetic recovery metrics to the scenario's RTO/RPO assumptions; distinguish timing from operational readiness.
- Require documented restoration authorization, integrity checks and monitoring before simulated service resumption.
- **Open gap:** FIND-002 recovery governance remains OPEN. TEST-003 is PENDING; simulated RTO/RPO results alone do not close it.

## Scenario C — Suspicious transaction escalation (CR-003)
**Trigger:** Hypothetical suspicious transaction alert requiring ownership and escalation.
**Evidence:** `TEST-004-synthetic-transaction-alerts.csv`, `TEST-004-escalation-timeline.csv`, `TEST-004-escalation-sla-results.csv`, `TEST-004-raci-matrix.csv`, `TEST-004-decision-log.csv`, `FIND-003-escalation-governance.md`.

- Record alert classification, priority and supporting synthetic observations.
- Identify first responder, Fraud Risk Lead, Incident Commander and escalation approver.
- Check simulated response time against documented scenario SLA; retain raw timeline.
- Document unresolved decisions and approvals; do not claim actual transaction holds or customer impact.
- **Open gap:** FIND-003 escalation governance remains OPEN. TEST-004 is PENDING despite synthetic SLA results.

## Escalation and communication template
| Field | Required entry |
|---|---|
| Incident ID | SIM-IR-YYYYMMDD-NNN |
| Trigger and timestamp | Source event and time zone |
| Scenario/risk | CR-001 / CR-002 / CR-003 |
| Impact and uncertainty | Facts separated from assumptions |
| Evidence IDs/paths | Relative repository paths |
| Incident owner | Simulated role |
| Decision and approver | Named role; pending if unverified |
| Next update | Agreed checkpoint, not invented |
| Legal/privacy review | Pending / reviewed with evidence |
| Closure evidence | Verification artifacts and reviewer |

## Acceptance criteria and known limitations
A tabletop may be documented as executed when inputs, participants/roles, decisions and results are recorded. It may be called **governance-closed** only when missing approvals, responsibilities and verification are evidenced. This repository currently has one simulated closed finding (FIND-001) and two open findings (FIND-002 and FIND-003). No real incident handling, legal notification, or bank control certification is claimed.

**Next actions:** Review governance approvals for FIND-002 and FIND-003, validate applicability of regulatory references, and obtain an independent QA review of the playbook.
