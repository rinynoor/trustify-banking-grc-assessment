# FIND-001 — Privileged MFA Coverage Gap

## Assessment Information
- Project: Trustify Banking Cyber GRC Assessment
- Risk ID: CR-001
- Control ID: CTRL-001
- Test ID: TEST-001
- Assessment Type: Synthetic control test
- Finding Status: CLOSED — SIMULATED REMEDIATION VERIFIED

## Test Result
- Privileged accounts tested: 3
- Accounts meeting criteria: 2
- Accounts failing criteria: 1
- Phishing-resistant MFA coverage: 66.67%
- Overall result: FAIL

## Finding
The synthetic account admin02 uses SMS OTP rather than
phishing-resistant MFA.

This does not represent a finding against a real bank.

## Risk Implication
The simulated control gap could increase exposure to
credential phishing and unauthorized privileged access.

## Recommended Treatment
1. Replace SMS OTP with FIDO2 for admin02.
2. Verify FIDO2 enrollment and enforcement.
3. Repeat TEST-001 after the simulated remediation.
4. Record before-and-after results.

## Acceptance Criteria
100% of simulated privileged accounts must use
phishing-resistant MFA.

## Evidence
04-compliance/tests/TEST-001-mfa-results.csv

## Remediation Status
OPEN — Not yet implemented.

## Residual Risk
Not assessed.

## Remediation Verification — TEST-001-R1

- Verification type: Synthetic dataset retest
- Original test: TEST-001 — FAIL
- Original coverage: 66.67%
- Retest ID: TEST-001-R1
- Retest result: PASS
- Retest coverage: 100.00%
- Accounts tested: 3 privileged accounts
- Failed accounts after remediation: 0
- Improvement: 33.33 percentage points

### Remediation Evidence
04-compliance/tests/synthetic-iam-remediated.csv

### Retest Evidence
04-compliance/tests/TEST-001-R1-mfa-results.csv

### Finding Closure
Status: CLOSED — SIMULATED REMEDIATION VERIFIED

The synthetic account configuration now satisfies
the defined test acceptance criteria.

This finding closure applies only to the synthetic
dataset and does not establish operational control
effectiveness or regulatory compliance at a real bank.

### Residual Risk
Not assessed at organizational level.
