# Trustify — Final Portfolio QA Checklist

**Status:** SELF-REVIEW CHECKLIST; independent review NOT ASSESSED.
**Context:** Illustrative Indonesian banking cybersecurity GRC portfolio, November 2026. No live bank audit.

## A. File and source integrity

- [ ] Confirm all 12 core deliverables exist and contain substantive content (not merely non-empty files).
- [ ] Confirm CSV headers and risk/control/evidence IDs match their references.
- [ ] Verify EV-001 through EV-003 point to traceable public sources and accurately describe them.
- [ ] Check no real customer data, credentials, internal bank documents, or secrets are present.
- [ ] Check dashboard imports current project CSVs; distinguish imported values from historical snapshots.

## B. Assessment and governance

- [ ] Check CR-001, CR-002, CR-003 inherent scores against the documented methodology.
- [ ] Leave residual scores as NOT ASSESSED until justified by documented control effectiveness.
- [ ] Confirm TEST-001 baseline FAIL and TEST-001-R1 simulated PASS remain separately documented.
- [ ] Confirm TEST-002 synthetic PASS; TEST-003, TEST-004, TEST-005 PENDING.
- [ ] Confirm FIND-001 CLOSED (simulated); FIND-002 and FIND-003 OPEN.
- [ ] Verify any actual owner approvals, treatment deadlines, or recovery approvals before claiming closure.
- [ ] Check OJK citations, provision text, version and applicability with authoritative sources; until then mark PENDING VERIFICATION.
- [ ] Do not imply external audit, assurance, bank endorsement or legal compliance.

## C. KPI definitions

- [ ] KPI-01 12/12 means file availability only, not assessed deliverable quality.
- [ ] KPI-02 3/3 means documented evidence traceability only.
- [ ] KPI-03 0/3 means residual risk/control effectiveness not assessed.
- [ ] KPI-04 2/5 counts completed synthetic tests only.
- [ ] KPI-05 0/3 means verified high/critical treatment coverage is incomplete.
- [ ] KPI-06 1/3 is simulated finding closure, NOT independent review closure.
- [ ] Recompute KPI values from source CSVs before public release; document calculation date and method.

## D. Publication

- [ ] Confirm README links to dashboard, evidence, methodology, limitations and QA checklist.
- [ ] Ensure the disclaimer is prominent on GitHub and dashboard.
- [ ] Test dashboard locally with CSV imports and inspect for blank/misaligned columns.
- [ ] Review screenshots to ensure no private filesystem paths or personal information are visible.
- [ ] Add independent reviewer name/sign-off only if review actually occurs.

## Review record

Reviewer: NOT ASSIGNED
Independent QA outcome: NOT ASSESSED
Open issues: FIND-002, FIND-003, residual risk, regulatory verification, treatment effectiveness

This checklist is not proof that any item has been completed.
