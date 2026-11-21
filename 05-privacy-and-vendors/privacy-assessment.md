# Privacy Impact Assessment — Trustify

**Project:** Indonesia Banking Cyber Resilience Assessment — November 2026
**Assessment type:** Simulated, scenario-based privacy assessment
**Institution:** Hypothetical banking environment
**Status:** Draft — pending independent review
**Version:** 0.2

## 1. Objective and scope

Identify privacy risks associated with hypothetical banking
authentication, fraud monitoring, and incident response workflows.

This assessment does not evaluate a real bank or use actual
customer personal data.

## 2. Data inventory

| Data category | Hypothetical purpose | Sensitivity |
|---|---|---|
| Customer identity data | Identity verification | High |
| Authentication metadata | Account security monitoring | High |
| Transaction metadata | Fraud detection | High |
| Security event logs | Incident investigation | High |
| Incident case records | Escalation and response | High |

All examples in this repository use synthetic or illustrative data.

## 3. Hypothetical data flow

1. Customer initiates authentication.
2. Identity service evaluates authentication factors.
3. Security monitoring receives relevant event metadata.
4. Fraud monitoring evaluates suspicious activity.
5. Authorized personnel investigate and escalate incidents.
6. Records are retained or deleted according to an approved policy.

This is a conceptual workflow, not a verified bank architecture.

## 4. Privacy risk scenarios

| Risk ID | Scenario | Potential impact | Proposed control |
|---|---|---|---|
| PR-001 | Excessive access to customer identity data | Unauthorized disclosure | Least privilege and access review |
| PR-002 | Sensitive information exposed in security logs | Privacy breach | Data minimization and log masking |
| PR-003 | Excessive retention of incident records | Unnecessary exposure | Retention schedule and secure deletion |
| PR-004 | Uncontrolled sharing with third parties | Data leakage | Vendor due diligence and contractual safeguards |
| PR-005 | Unauthorized access following credential theft | Account and privacy compromise | Phishing-resistant MFA and anomaly monitoring |

## 5. Risk linkage

- PR-005 relates to CR-001: credential theft.
- PR-002 relates to CR-003: suspicious transaction monitoring.
- PR-003 relates to incident investigation and governance.
- PR-004 requires separate third-party risk assessment.

These linkages are analytical assumptions.

## 6. Proposed privacy controls

- Apply least-privilege access and role-based authorization.
- Minimize personal information collected in security logs.
- Mask sensitive identifiers in monitoring dashboards.
- Define retention periods and deletion procedures.
- Maintain audit trails for privileged access.
- Establish breach escalation and notification procedures.
- Assess third-party data processing arrangements.

Implementation and effectiveness have NOT been verified.

## 7. Legal and regulatory considerations

Relevant Indonesian privacy and banking requirements
must be checked against authoritative legal sources.

Potentially relevant framework:
- Indonesia Personal Data Protection Law (UU No. 27/2022).
- Applicable OJK banking cybersecurity requirements.

This document does not claim legal compliance.
Specific obligations and provisions require verification.

## 8. Evidence references

- EV-001: Public reporting on banking cybersecurity concerns.
- EV-002: Public reporting on OJK cybersecurity warnings.
- EV-003: Public reporting on national cyber threat mitigation.
- CR-001 and CR-003: Illustrative risk scenarios.
- TEST-001 and TEST-002: Synthetic authentication control tests.

Public news is contextual evidence, not proof of a bank's
privacy-control implementation.

## 9. Assessment limitations

- No access to production banking systems.
- No real customer records or personal information.
- No verified data processing inventory.
- No actual vendor agreements or retention policies.
- No independent legal or privacy compliance review.

## 10. Preliminary conclusion

Five illustrative privacy risk scenarios have been identified.

Proposed controls are documented, but implementation,
residual risk, and control effectiveness remain NOT ASSESSED.

**Overall status: DRAFT — NOT A REAL BANK PRIVACY AUDIT.**
