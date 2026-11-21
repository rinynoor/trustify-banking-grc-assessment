# TRUSTIFY — Regulatory Evidence Gap Analysis

**Assessment:** Indonesia Banking Cyber Resilience Assessment — November 2026  
**Type:** Fictional GRC portfolio case study; no actual bank assessed  
**Overall compliance status:** NOT ASSESSED  
**Regulatory mapping status:** Preliminary source identification completed; clause-level and entity-applicability review remains open.

## 1. Regulatory baseline identified

### OJK — commercial banks
1. **SEOJK 29/SEOJK.03/2022 — Ketahanan dan Keamanan Siber bagi Bank Umum.** The official OJK page identifies the circular and its effective date (27 December 2022). The official summary describes inherent cyber risk assessment, cyber risk management, and related cyber-resilience domains.
2. **POJK 11/POJK.03/2022 — Penyelenggaraan Teknologi Informasi oleh Bank Umum.** This is the underlying OJK IT governance regulation referenced by SEOJK 29/2022.
3. **PADK OJK 1 Tahun 2026 — Penyelenggaraan Teknologi Informasi oleh Bank Umum.** The official OJK page states it is effective 1 March 2026 and applies to all commercial banks. The page states that it covers IT governance, IT architecture and strategy, IT risk management, information/network security, IT service providers, data and personal-data protection, internal control/audit, and reporting. It repeals SEOJK 21/SEOJK.03/2017; it does not state that it repeals SEOJK 29/2022.

### Bank Indonesia — conditional scope
4. **PBI 2 Tahun 2024** covers cybersecurity and information-system security for payment-system providers, money/FX market participants, and other parties regulated and supervised by BI.
5. **PADG 24 Tahun 2024**, as amended by **PADG 29 Tahun 2026** (effective 25 September 2026), provides implementing rules. PADG 29/2026 addresses, among other things, reporting deadlines/sanctions and BI designation of financial-sector vital information infrastructure.

**Applicability warning:** BI rules are not automatically applicable to every commercial-bank activity. Determine whether the hypothetical institution performs an activity or has a status within BI's regulatory/supervisory scope before mapping a mandatory obligation.

## 2. Preliminary requirement mapping

| Requirement | Source area | Project control/test link | Status |
|---|---|---|---|
| REQ-001 Cyber risk assessment and management | SEOJK 29/2022 Chapters II–III | REG-001 / TEST-005 | Preliminary mapping; not assessed |
| REQ-002 Protection of IT assets and information | SEOJK 29/2022 protection domain; PADK 1/2026 IT security | CTRL-001 / TEST-001 | Preliminary mapping; not assessed |
| REQ-003 Monitoring and detection | SEOJK 29/2022 detection domain | CTRL-001 / TEST-002 | Preliminary mapping; not assessed |
| REQ-004 Incident response and recovery | SEOJK 29/2022 response/recovery domains | CTRL-002 / CTRL-003; TEST-003 / TEST-004 | Preliminary mapping; not assessed |
| REQ-005 IT governance, risk, data protection, providers and audit | PADK OJK 1/2026 | CTRL-001–003 (partial mapping only) | Preliminary mapping; not assessed |
| REQ-006 BI cybersecurity obligations | PBI 2/2024 and PADG 24/2024 as amended | CTRL-001–003 (conditional mapping) | Applicability not established |

See `TEST-005-regulatory-requirements.csv` for machine-readable mapping and `TEST-005-regulatory-sources.csv` for official source register.

## 3. What has and has not been verified

**Verified at source-register level:** the official OJK and BI webpages identify the regulations, titles, issuers, and key effective dates/scope summaries described above.

**Not yet verified:** exact paragraph/letter citations for each requirement, full legal text interpretation, applicability to a defined hypothetical bank profile, control design adequacy, and evidence of operating effectiveness. This project has not reviewed a real bank's license, activities, risk profile, or regulatory correspondence.

## 4. Test evidence interpretation

- **TEST-001:** synthetic MFA baseline FAIL and synthetic retest PASS. This demonstrates a synthetic configuration change only.
- **TEST-002:** PASS for two defined synthetic login-detection scenarios only.
- **TEST-003:** PENDING; recovery governance/approval evidence remains unverified.
- **TEST-004:** PENDING; escalation governance/acknowledgements remain unverified.
- **TEST-005:** PENDING; no clause-level legal applicability review or independent regulatory assessment has been completed.

## 5. Required closure actions

1. Read the official full text and annexes for SEOJK 29/2022, POJK 11/2022, and PADK OJK 1/2026.
2. Replace broad source-area labels with exact chapter/paragraph references only after checking the relevant text.
3. Define the hypothetical institution's business model and activities; establish whether any BI-regulated activity is in scope.
4. Map each applicable requirement to a control objective, test procedure, evidence item, owner, and assessment result.
5. Have the mapping reviewed by a qualified independent reviewer; preserve comments and response evidence.

## 6. Conclusion

**REGULATORY COMPLIANCE: NOT ASSESSED.**

This is a preliminary regulatory source and gap-mapping exercise, not a legal opinion, regulatory compliance certification, or finding against any actual bank. The presence of an official regulation in the source register does not prove compliance with it.
