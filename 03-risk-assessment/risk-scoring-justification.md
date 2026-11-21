# Trustify — Risk Scoring Justification

## Assessment Context

Project: Indonesia Banking Cyber Resilience Assessment
Assessment Type: Public-source, simulated GRC assessment
Method: Likelihood (1–5) × Impact (1–5)

All risk scores are illustrative scenario estimates.
No confidential banking systems or internal controls
have been examined.

## CR-001 — Unauthorized Account Access

Threat: Phishing and credential theft
Likelihood: 4 (Likely)
Impact: 5 (Severe)
Inherent Score: 20 (Critical)

Likelihood rationale:
Assumes a scenario with uneven phishing-resistant
MFA coverage and exposure to credential theft.
The rating is a scenario assumption, not a measured
frequency of successful attacks.

Impact rationale:
A successful compromise could expose customer
accounts, cause financial loss, and affect trust.

Evidence:
EV-001 — Public threat activity reporting
EV-003 — BSSN clarification

Evidence limitation:
Neither source establishes a successful compromise
at any specific bank.

## CR-002 — Ransomware Service Disruption

Threat: Ransomware
Likelihood: 3 (Possible)
Impact: 5 (Severe)
Inherent Score: 15 (High)

Likelihood rationale:
Assumes ransomware is a plausible threat while
backup and recovery readiness are unknown.
No actual ransomware incident has been established.

Impact rationale:
A severe incident could interrupt critical banking
services and affect operational continuity.

Evidence:
EV-001 — General cyber threat context
EV-003 — Threat telemetry clarification

Evidence limitation:
These sources do not establish ransomware-specific
activity at a particular bank.

## CR-003 — Delayed Transaction Escalation

Threat: Fraud or abnormal transactions
Likelihood: 4 (Likely)
Impact: 5 (Severe)
Inherent Score: 20 (Critical)

Likelihood rationale:
Assumes escalation criteria and incident ownership
require review in the simulated organization.

Impact rationale:
Delayed escalation could increase financial loss
and impair incident response.

Evidence:
EV-002 — Reported OJK vigilance response
EV-003 — BSSN clarification

Evidence limitation:
The sources do not establish that any bank has
failed to escalate suspicious transactions.

## Assessment Limitations

1. No internal bank data was examined.
2. No penetration testing was performed.
3. No actual control effectiveness was measured.
4. Risk ratings are scenario-based assumptions.
5. Residual scores remain unassigned.
6. Results must not be presented as audit findings
   against any named financial institution.

## Next Validation Requirements

- Define simulated control baseline.
- Document control assessment criteria.
- Identify acceptable validation evidence.
- Conduct a controlled tabletop exercise.
- Review and approve risk treatment proposals.
