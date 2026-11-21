# Third-Party Risk Assessment — Trustify

**Project:** Indonesia Banking Cyber Resilience Assessment — November 2026
**Assessment type:** Hypothetical vendor risk assessment
**Status:** DRAFT — pending independent review
**Version:** 0.2

## 1. Assessment objective

Identify and evaluate cybersecurity, operational resilience,
privacy, and governance risks associated with hypothetical
third-party service providers in a banking environment.

No actual vendors, contracts, or production systems were assessed.

## 2. Vendor inventory

| ID | Hypothetical service | Criticality | Data exposure |
|---|---|---|---|
| VEN-001 | Cloud infrastructure and backup | Critical | Potentially high |
| VEN-002 | Identity and authentication service | Critical | High |
| VEN-003 | Fraud monitoring platform | High | High |

These are illustrative vendor categories, not named companies.

## 3. Risk assessment methodology

Likelihood and impact use an illustrative 1–5 scale.

Inherent risk = Likelihood x Impact.

Risk scores are scenario assumptions, not measured
vendor performance or verified vulnerabilities.

| Risk score | Classification |
|---|---|
| 1–4 | Low |
| 5–9 | Medium |
| 10–16 | High |
| 17–25 | Critical |

## 4. Third-party risk register

| Risk ID | Vendor | Scenario | L | I | Score | Rating |
|---|---|---|---|---|---|---|
| TPR-001 | VEN-001 | Cloud outage disrupts banking availability | 3 | 5 | 15 | High |
| TPR-002 | VEN-002 | Authentication service compromise | 4 | 5 | 20 | Critical |
| TPR-003 | VEN-003 | Unauthorized exposure of transaction metadata | 3 | 5 | 15 | High |

All ratings are illustrative inherent risk estimates.

## 5. Required control assessment

| Vendor | Control objective | Required evidence | Verification |
|---|---|---|---|
| VEN-001 | Resilience and recoverability | Recovery test reports, BCP/DR documents | NOT ASSESSED |
| VEN-002 | Strong authentication and access governance | MFA policy, access review, audit logs | NOT ASSESSED |
| VEN-003 | Transaction data protection | Data flow, encryption, retention policy | NOT ASSESSED |

## 6. Due diligence checklist

Before onboarding or renewing a critical vendor:

1. Identify service dependencies and data processing scope.
2. Establish accountable business and risk owners.
3. Review security policies and independent assurance evidence.
4. Review incident notification and escalation obligations.
5. Assess data access, encryption, retention, and deletion.
6. Evaluate subcontractor and fourth-party dependencies.
7. Verify business continuity and recovery arrangements.
8. Document residual risk and formal risk acceptance.
9. Define periodic reassessment and exit arrangements.

No due diligence completion is claimed in this project.

## 7. Contractual and governance considerations

Illustrative contract review should consider:

- Security and confidentiality obligations.
- Incident notification and cooperation requirements.
- Audit rights and assurance reporting.
- Data processing and subcontractor conditions.
- Service availability and recovery commitments.
- Secure data return and deletion on termination.

Legal applicability requires independent verification.

## 8. Linkage to Trustify risk scenarios

- TPR-001 relates to CR-002: ransomware and service availability.
- TPR-002 relates to CR-001: credential theft and authentication.
- TPR-003 relates to CR-003: suspicious transaction monitoring.

These relationships support risk traceability,
not proof that the hypothetical vendor controls exist.

## 9. Evidence references

- EV-001: Public cybersecurity reporting context.
- EV-002: Public banking cybersecurity warning context.
- EV-003: National cyber threat mitigation reporting.
- CR-001, CR-002, CR-003: Trustify risk register.
- TEST-001: Synthetic MFA configuration assessment.
- TEST-003: Synthetic recovery tabletop exercise.
- TEST-004: Synthetic escalation tabletop exercise.

No vendor-specific independent assurance documents
have been obtained or verified.

## 10. Treatment recommendations

| Risk | Proposed treatment | Accountable role (simulated) | Status |
|---|---|---|---|
| TPR-001 | Review recovery evidence and alternative arrangements | Vendor Risk Lead | PROPOSED |
| TPR-002 | Assess privileged access and authentication assurance | IAM Lead | PROPOSED |
| TPR-003 | Review data protection and incident escalation obligations | Privacy Lead | PROPOSED |

Deadlines and approvals are not yet established.
Residual risk and treatment effectiveness remain NOT ASSESSED.

## 11. Limitations and conclusion

This assessment is based on hypothetical vendor categories
and synthetic risk scenarios.

No real vendor was contacted, tested, certified,
or determined to be compliant or non-compliant.

Three illustrative third-party risks were documented:
one Critical and two High.

**Overall status: DRAFT — NOT A REAL VENDOR AUDIT.**
