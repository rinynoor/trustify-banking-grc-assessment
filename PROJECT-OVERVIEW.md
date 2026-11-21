# TRUSTIFY — Project Overview

**Project:** Indonesia Banking Cyber Resilience Assessment — November 2026  
**Portfolio owner:** Riny Noor  
**Project type:** Independent educational GRC case study using public reporting and synthetic test data  
**Version:** 1.0 documentation baseline  
**Status:** Portfolio documentation consolidated; assessment limitations and open items remain

## 1. Executive description

Trustify is a fictional consulting identity used for an independent portfolio case study. The project demonstrates how a Governance, Risk and Compliance (GRC) analyst can structure a cyber-resilience assessment for a hypothetical Indonesian commercial bank, using public reporting about cyber threats affecting the financial sector in November 2026.

The project is not commissioned by, affiliated with, or endorsed by any bank, OJK, Bank Indonesia, BSSN, or security vendor. No real bank system was accessed or tested. All account, transaction, log, recovery, role, and tabletop exercise data in the test artifacts are synthetic.

## 2. Problem statement

Public reporting in November 2026 described elevated cyber threat activity, regulatory reminders to banks, and preparedness measures by Indonesian authorities. Such reporting is useful threat context, but it does not by itself prove successful compromise, a breach at a named bank, or the effectiveness or failure of any particular bank's controls.

The project therefore asks: how can an analyst translate public threat context into a disciplined, evidence-traceable assessment of hypothetical banking risks, controls, tests, issues, and management actions without overstating what the evidence proves?

## 3. Objectives

1. Record public threat claims with source, date, exact claim, verification state, and limitations.
2. Derive clearly labeled hypothetical banking cyber-risk scenarios.
3. Map risks to control objectives and relevant frameworks/regulations.
4. Demonstrate selected control tests using synthetic data and tabletop exercises.
5. Record findings, remediation actions, retest outcomes, and unresolved governance gaps.
6. Produce an executive-level view of results, limitations, and prioritized next steps.
7. Preserve project activity and change history so another reviewer can follow the work.

## 4. Scope

**Included**
- Public-source threat context from Katadata and ANTARA reporting about OJK/BSSN statements and FortiGuard telemetry.
- Three illustrative risk scenarios: credential theft, ransomware/service disruption, and delayed suspicious-transaction escalation.
- Conceptual mapping to NIST CSF 2.0 and ISO/IEC 27001:2022.
- Preliminary review of OJK rules relevant to commercial banks and conditional BI rules for entities within BI's supervisory scope.
- Synthetic MFA configuration review and retest, synthetic suspicious-login detection, and simulated ransomware recovery/fraud escalation tabletop artifacts.
- Draft privacy, third-party risk, incident response, dashboard, executive reporting, and QA artifacts.

**Excluded**
- Penetration testing or scanning of any real bank.
- Access to production systems, customer accounts, personal data, or confidential bank documents.
- Validation of any bank's actual control design or operating effectiveness.
- Confirmation, attribution, or investigation of a real cyber incident.
- Legal opinion, regulatory attestation, audit opinion, or certification.

## 5. Methodology

1. **Source review:** capture publisher, publication date, URL, claim, evidence type, and limitations.
2. **Evidence qualification:** distinguish media-reported statements, vendor telemetry reported by media, primary regulatory text, and synthetic project evidence.
3. **Risk scenario development:** define asset/process, threat, vulnerability assumption, likelihood, impact, and inherent score.
4. **Control mapping:** link each risk to control objectives and relevant frameworks or regulations; record applicability and source verification.
5. **Synthetic testing:** run test scripts or tabletop scenarios against fictional data only.
6. **Issue management:** record baseline result, evidence, remediation, retest, closure basis, and remaining uncertainty.
7. **Reporting and QA:** summarize actual documented results and explicitly disclose open items.

## 6. Traceability model

Public evidence (EV) → hypothetical risk (CR) → control objective (CTRL) → test (TEST) → finding (FIND) → remediation/retest → executive result/KPI.

A link in this chain demonstrates documentary traceability only. It does not prove that a control exists or operates at a real bank.

## 7. Key results at the documentation baseline

- 3 public-source evidence records are documented; primary FortiGuard historical telemetry and underlying OJK/BSSN operational records remain unavailable.
- 3 hypothetical cyber-risk scenarios are documented.
- TEST-001 synthetic baseline failed the defined phishing-resistant MFA criterion; TEST-001-R1 synthetic retest passed after the simulated configuration change.
- TEST-002 generated 2 alerts from 10 synthetic login events for the defined brute-force and rapid-country-change scenarios.
- TEST-003 and TEST-004 contain tabletop artifacts, but their checklist status remains PENDING because governance evidence and approvals have not been verified.
- TEST-005 regulatory applicability and detailed mapping remain PENDING / NOT ASSESSED.
- FIND-001 is closed only for the synthetic dataset; FIND-002 and FIND-003 remain open.
- Independent quality review has not been performed.

## 8. Completion definition

This portfolio's first release is considered documented when:
- project overview, timeline, issue/finding registers, results, and changelog are present;
- the evidence and regulatory limitations are explicit;
- test results are consistent across the executive report, checklist, and issue registers;
- repository structure and documentation are navigable; and
- open issues are transparently listed rather than falsely marked complete.

This definition does **not** mean all simulated control tests passed, all regulatory requirements were assessed, or independent assurance was obtained.

## 9. Repository map

See [README.md](README.md) for the folder guide. Start with [PROJECT-OVERVIEW.md](PROJECT-OVERVIEW.md), then [PROJECT-TIMELINE.md](PROJECT-TIMELINE.md), [ISSUE-REGISTER.csv](ISSUE-REGISTER.csv), [FINDINGS-AND-REMEDIATION.csv](FINDINGS-AND-REMEDIATION.csv), and [PROJECT-RESULTS.md](PROJECT-RESULTS.md).

## 10. Professional integrity statement

The project intentionally preserves failed baseline tests and unresolved findings. It does not convert a synthetic retest into proof of real-world security, treat a media report as primary telemetry, or describe an unreviewed regulatory mapping as compliance. This restraint is part of the assessment methodology, not a project defect.
