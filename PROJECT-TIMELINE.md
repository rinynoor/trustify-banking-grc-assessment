# TRUSTIFY — Project Timeline & Activity History

**Period represented:** 21 November 2026 repository activity  
**Basis:** Git commit history and artifacts visible in the repository. Times are UTC. Earlier offline analysis is not assigned invented dates.

| Sequence | Time (UTC) | Activity | Work performed | Recorded outcome |
|---|---|---|---|---|
| 1 | 01:26 | Repository baseline | Initial 50-file project structure and assessment artifacts | `963c407` |
| 2 | 01:36 | Threat evidence review | EV-001 status and limitations updated | `238c7c8`; primary telemetry pending |
| 3 | 01:38 | OJK evidence review | EV-002 updated from ANTARA reporting | `0da5f31`; original OJK records pending |
| 4 | 01:39 | BSSN evidence review | EV-003 mitigation statements and limitations recorded | `6497528`; original BSSN records and telemetry pending |
| 5 | 01:46 | Control traceability | Risk/control mappings and checklist references refined | `41945b5` |
| 6 | 01:54 | Escalation traceability | TEST-004 and FIND-003 corrected from CTRL-002 to CTRL-003 | `8adf8d9` |
| 7 | Documentation consolidation | Added project overview, timeline, issue register, findings/remediation register, results and changelog | Commits `937899b`, `80fcfb6`, `cf1f20d`, `51c459a`, `4641657`, `d29a752` |
| 8 | Documentation and regulatory refinement | Updated README/start guide, corrected EV-002 telemetry wording, added official OJK/BI source register, revised TEST-005 requirements and analysis, updated control matrix, KPI and executive report | Commits `9da3336`, `5b5d597`, `18ca711`, `8eec640`, `f463db7`, `2a865cc`, `6fb0860`, `a777e29`, `70ca8c7`, `c82cfd5`, `c205bfb`, `17b1246` |

## Workstream history

### A. Project definition
- Established a fictional Trustify portfolio identity and a hypothetical Indonesian commercial-bank scenario.
- Defined boundaries: no real bank engagement, production access, customer data, or compliance certification.
- Created project brief, scope/methodology and a consolidated project overview.

### B. Threat intelligence
- Recorded three media-reported evidence items (EV-001 to EV-003).
- Distinguished reported FortiGuard activity from successful compromises or confirmed incidents.
- Corrected EV-002 wording to state the ANTARA article's 1.9 million blocked attacks and 999,000 financial-sector figure without the earlier ambiguous wording.
- Original historical FortiGuard snapshots and counting methodology remain unavailable.

### C. Risk assessment
- Created CR-001 credential theft/unauthorized access, CR-002 ransomware/service availability, and CR-003 suspicious-transaction escalation.
- Inherent scores are illustrative assumptions.
- Residual risk and treatment effectiveness remain NOT ASSESSED.

### D. Control tests and exercises
- TEST-001 synthetic MFA baseline FAIL; TEST-001-R1 synthetic retest PASS.
- TEST-002 processed 10 synthetic login events and generated 2 scenario alerts.
- TEST-003 recovery tabletop artifacts exist; result remains PENDING.
- TEST-004 escalation tabletop artifacts exist; result remains PENDING.
- TEST-005 official OJK/BI source pages have been identified and the preliminary mapping updated; clause-level and entity applicability review remains pending.

### E. Documentation and reporting
- Added a project overview, work history, issue register, findings/remediation register, project results and changelog.
- Reconciled executive reporting and KPI definitions with the synthetic test evidence.
- Independent QA has not been performed.

## How to interpret this history

Commit timestamps establish when repository changes were saved. They do not prove that every artifact was independently reviewed or that external assurance was obtained. Earlier work not represented by Git commits is not assigned invented dates.

## Current stopping point

The documentation package is consolidated and the regulatory source baseline has been refreshed. Remaining items are explicitly tracked in `ISSUE-REGISTER.csv`: primary telemetry corroboration, treatment/residual risk, recovery and escalation governance, exact regulatory clause/applicability review, and independent QA. They are not silently marked complete.
