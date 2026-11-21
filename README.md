# Trustify | Indonesia Banking Cyber Resilience Assessment — November 2026

**GRC project portfolio case study · Project owner: Riny Noor**

Trustify demonstrates an evidence-led Governance, Risk and Compliance (GRC) workflow for a fictional Indonesian banking scenario. It documents the journey from project idea and scope definition through threat intelligence, risk assessment, control mapping, synthetic testing, findings, remediation, reporting and quality assurance.

> **Important scope statement:** This is a simulated educational portfolio. No real bank was engaged, audited, accessed, tested or assessed. All account, transaction, login, recovery and tabletop records are synthetic. Public reporting is cited as contextual evidence, not proof of a successful compromise or a control failure at any real institution. This work is not an audit opinion, certification or legal/regulatory compliance attestation.

---

## Open the portfolio

| Destination | What you will find |
|---|---|
| **[OPEN MAIN PROJECT PORTFOLIO](https://rinynoor.github.io/trustify-banking-grc-assessment/)** | Recruiter-friendly project story, methodology, project journey, results, evidence library, findings, deliverables and conclusion. |
| **[OPEN INTERACTIVE GRC DASHBOARD](https://rinynoor.github.io/trustify-banking-grc-assessment/08-dashboard/)** | Dashboard view of risks, controls, tests, findings, evidence and limitations. |
| [Browse the GitHub repository](https://github.com/rinynoor/trustify-banking-grc-assessment) | Source files, supporting documentation, datasets and scripts. |

**Important:** HTML pages should be opened through the GitHub Pages website links above, not through GitHub's `blob/.../*.html` source view. If a Pages link does not load, enable GitHub Pages in **Settings → Pages** using branch `main` and folder `/(root)`, then wait for deployment to finish.

## Project story and governance records

1. [Project overview](PROJECT-OVERVIEW.md) — business context, project purpose, scope and methodology.
2. [Project timeline](PROJECT-TIMELINE.md) — recorded work history and Git milestones.
3. [Issue register](ISSUE-REGISTER.csv) — issues, current status and closure evidence required.
4. [Findings and remediation register](FINDINGS-AND-REMEDIATION.csv) — test findings, remediation and retest status.
5. [Project results](PROJECT-RESULTS.md) — outcomes, metrics, open work and limitations.
6. [Changelog](CHANGELOG.md) — repository change history.
7. [Disclaimer](DISCLAIMER.md) — assumptions and limitations.

## Deliverables library

### 01 · Project charter
- [Project brief](01-project-charter/project-brief.md)
- [Scope and methodology](01-project-charter/scope-and-methodology.md)

### 02 · Threat intelligence and evidence
- [Evidence register — EV-001 to EV-003](02-threat-intelligence/evidence-register.csv)
- [Incident and threat timeline](02-threat-intelligence/incident-timeline.md)
- Source notes: [EV-001](02-threat-intelligence/sources/EV-001.md) · [EV-002](02-threat-intelligence/sources/EV-002.md) · [EV-003](02-threat-intelligence/sources/EV-003.md)

### 03 · Cyber risk assessment
- [Cyber risk register](03-risk-assessment/cyber-risk-register.csv)
- [Risk methodology](03-risk-assessment/risk-methodology.md)
- [Risk scoring justification](03-risk-assessment/risk-scoring-justification.md)

### 04 · Compliance and control testing
- [Compliance control matrix](04-compliance/compliance-control-matrix.csv)
- [Control assessment checklist](04-compliance/control-assessment-checklist.csv)
- [TEST-001 MFA baseline](04-compliance/tests/TEST-001-mfa-results.csv) · [TEST-001-R1 retest](04-compliance/tests/TEST-001-R1-mfa-results.csv) · [FIND-001 remediation record](04-compliance/tests/FIND-001-mfa-remediation.md)
- [TEST-002 detection script](04-compliance/tests/detect_suspicious_login.py) · [Synthetic login events](04-compliance/tests/synthetic-login-events.csv) · [Generated detection alerts](04-compliance/tests/TEST-002-detection-alerts.csv)
- [TEST-003 recovery plan](04-compliance/tests/TEST-003-recovery-plan.md) · [Recovery metrics](04-compliance/tests/TEST-003-recovery-metrics.csv) · [FIND-002 recovery governance](04-compliance/tests/FIND-002-recovery-governance.md)
- [TEST-004 incident escalation assessment](04-compliance/tests/TEST-004-incident-escalation.md) · [Decision log](04-compliance/tests/TEST-004-decision-log.csv) · [RACI matrix](04-compliance/tests/TEST-004-raci-matrix.csv) · [Escalation timeline](04-compliance/tests/TEST-004-escalation-timeline.csv) · [SLA results](04-compliance/tests/TEST-004-escalation-sla-results.csv) · [FIND-003 escalation governance](04-compliance/tests/FIND-003-escalation-governance.md)
- [TEST-005 regulatory gap analysis](04-compliance/tests/TEST-005-regulatory-gap-analysis.md) · [Regulatory requirements](04-compliance/tests/TEST-005-regulatory-requirements.csv) · [Regulatory source register](04-compliance/tests/TEST-005-regulatory-sources.csv)

### 05 · Privacy and third-party risk
- [Privacy assessment](05-privacy-and-vendors/privacy-assessment.md)
- [Third-party risk assessment](05-privacy-and-vendors/third-party-risk.md)

### 06 · Incident response
- [Incident response playbook](06-incident-response/incident-response-playbook.md)

### 07 · Executive reporting
- [Executive summary](07-executive-report/executive-summary.md)

### 08 · Dashboard
- **[Open the rendered Interactive GRC Dashboard](https://rinynoor.github.io/trustify-banking-grc-assessment/08-dashboard/)** — opens the dashboard as a website, not as HTML source.
- [Dashboard source file (HTML)](08-dashboard/index.html) — technical source code for inspection only.

### 09 · Quality assurance
- [Final QA checklist](09-quality-assurance/final-qa-checklist.md)
- [KPI scorecard](09-quality-assurance/kpi-scorecard.csv)
- [Review log](09-quality-assurance/review-log.md)
- [Revision response matrix](09-quality-assurance/revision-response-matrix.csv)

## Results at a glance

- 3 public-source evidence records documented; primary telemetry and original agency records remain pending.
- 3 hypothetical banking cyber-risk scenarios recorded.
- TEST-001 synthetic MFA baseline: **FAIL**; TEST-001-R1 synthetic retest: **PASS**.
- TEST-002 generated **2 alerts from 10 synthetic login events**.
- TEST-003 and TEST-004 tabletop artifacts are documented; assessment status remains **PENDING**.
- TEST-005 regulatory applicability remains **NOT ASSESSED / pending verification**.
- FIND-001 is closed only for the synthetic dataset; FIND-002 and FIND-003 remain open.
- Independent review has **not** been performed.

These results describe the project artifacts and synthetic exercises only. They must not be interpreted as the security posture, compliance status or audit result of a real bank.

## Traceability model

**Public evidence (EV) → hypothetical risk (CR) → control objective (CTRL) → test (TEST) → finding (FIND) → remediation/retest → executive reporting.**

The repository preserves the distinction between reported threat activity, verified primary evidence, simulated test results and unresolved assessment items.

## Contact and professional profile

**Riny Noor** · GRC / Cybersecurity Risk / IT Governance portfolio case study

For professional discussion, use the project owner’s LinkedIn profile and share the **main portfolio website** link above rather than a raw HTML source link.

---

*Portfolio demonstration only. Review [DISCLAIMER.md](DISCLAIMER.md) and [PROJECT-RESULTS.md](PROJECT-RESULTS.md) before interpreting or reusing any result.*
