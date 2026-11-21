# TRUSTIFY — Project Timeline & Activity History

**Period represented:** 21 November 2026 repository activity  
**Basis:** Git commit history and artifacts visible in the repository. Earlier research and drafting discussions are summarized only where they are supported by the project record; exact times are not invented.

| Sequence | Date/time (UTC) | Activity | Work performed | Recorded outcome |
|---|---|---|---|---|
| 1 | 21 Nov 2026, 01:26 | Repository baseline | Initial portfolio structure and 50 files committed | Initial commit `963c407` |
| 2 | 21 Nov 2026, 01:36 | Threat evidence review | Updated EV-001 status and limitations for reported FortiGuard financial-sector telemetry | `238c7c8`; primary telemetry still pending |
| 3 | 21 Nov 2026, 01:38 | OJK evidence review | Updated EV-002 based on ANTARA reporting of OJK coordination and monitoring guidance | `0da5f31`; original circulars and underlying records pending |
| 4 | 21 Nov 2026, 01:39 | BSSN evidence review | Added BSSN-reported mitigation measures and limitations to EV-003 | `6497528`; primary BSSN records and FortiGuard snapshot pending |
| 5 | 21 Nov 2026, 01:46 | Control traceability correction | Refined risk/control mappings and assessment checklist references | `41945b5` |
| 6 | 21 Nov 2026, 01:54 | Escalation traceability correction | Corrected TEST-004 and FIND-003 relationship from CTRL-002 to CTRL-003 | `8adf8d9` |

## Workstream history reflected in the artifacts

### A. Project definition
- Established a fictional Trustify portfolio identity and a hypothetical Indonesian banking assessment.
- Defined boundaries: no real bank engagement, production access, customer data, or compliance certification.
- Created project brief and scope/methodology.

### B. Threat intelligence
- Recorded three media-based evidence items (EV-001 to EV-003).
- Separated time-specific FortiGuard telemetry figures reported by media from confirmed cyber incidents.
- Preserved limitations: original dashboard snapshots, vendor counting methodology, and primary agency records were not independently obtained.

### C. Risk assessment
- Created CR-001 credential theft/unauthorized access, CR-002 ransomware/service availability, and CR-003 suspicious-transaction escalation.
- Scored inherent likelihood and impact using illustrative assumptions.
- Residual risk remains unassessed; treatment plans require completion.

### D. Control tests and simulated exercises
- TEST-001: synthetic privileged MFA baseline (FAIL) and TEST-001-R1 synthetic retest (PASS).
- TEST-002: detection script processed 10 synthetic login events and generated 2 scenario alerts.
- TEST-003: ransomware recovery tabletop artifacts exist; formal assessment remains PENDING.
- TEST-004: transaction escalation tabletop artifacts exist; formal assessment remains PENDING.
- TEST-005: regulatory evidence gap analysis remains PENDING / NOT ASSESSED.

### E. Quality and reporting
- Added control/evidence traceability corrections.
- Executive summary and KPI artifacts document limitations and the need for independent review.
- Independent QA has not been performed.

## How to read this timeline

The commit timestamps document when changes were saved to GitHub. They do not establish the full duration of analysis, prove that every listed artifact was independently reviewed, or serve as external approval. Earlier project discussions and local work not represented by commits are not assigned invented dates here.

## Next close-out actions

1. Reconcile the regulatory matrix against authoritative OJK/BI texts and state applicability boundaries.
2. Correct the EV-002 claim wording and make source verification status consistent.
3. Reconcile issue/finding status and KPI definitions across all project artifacts.
4. Perform a final structural/content QA pass.
5. Obtain a real independent reviewer if the portfolio is to claim independent review.
