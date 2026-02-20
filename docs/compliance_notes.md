# TenderScan — Compliance Notes

## Legal & Ethical Framework

### 1. Data Sourcing

| Portal | Scraping Approach | Attribution |
|---|---|---|
| eTenders.gov.za (National Treasury) | Public metadata only | "Data sourced from National Treasury eTender Portal" |
| Provincial bulletins | Public metadata only | Attribute relevant provincial authority |
| SETA portals | Public metadata only | Attribute relevant SETA |

**We never:**
- Download, store, or redistribute official tender documents (PDFs, specifications)
- Bypass authentication or access non-public pages
- Scrape personal contact data beyond publicly listed procurement officers

### 2. Rate Limiting & robots.txt

- All scrapers implement `time.sleep(2)` between requests
- `robots.txt` is checked and honoured before scraping any portal
- Maximum concurrent requests: 1 (sequential, never parallel)

### 3. POPIA Compliance (Protection of Personal Information Act)

| Requirement | Implementation |
|---|---|
| Lawful processing | Users explicitly consent to data collection at sign-up |
| Purpose limitation | User data used only for tender matching and alerts |
| Data minimisation | Only fields necessary for filtering are stored |
| Accuracy | Users can update/correct their profile at any time |
| Storage limitation | Inactive accounts deleted after 12 months |
| Integrity & confidentiality | Passwords hashed (bcrypt); data encrypted at rest (AES-256) |
| Data subject rights | Users can request full data export or deletion via in-app form |

### 4. Terms of Service Summary

Users of TenderScan agree that:

- TenderScan is a **discovery tool only** — not a submission platform
- Users are solely responsible for verifying eligibility requirements
- Users must submit applications via official portals
- TenderScan makes no guarantees regarding tender accuracy or completeness

### 5. Disclaimer

> Data sourced from the National Treasury eTender Portal and related public portals. TenderScan does not host, reproduce, or redistribute official tender documents. All metadata is used for informational purposes only. Users must verify all information at the official source before submitting any application.

## CSD & Compliance Checklist (For Users)

| Requirement | Description | Status |
|---|---|---|
| CSD Registration | Central Supplier Database registration | 🔲 User responsibility |
| Tax Clearance | Valid SARS Tax Clearance Certificate | 🔲 User responsibility |
| B-BBEE Certificate | Broad-Based Black Economic Empowerment rating | 🔲 User responsibility |
| CIDB Grading | Construction Industry Development Board registration (contractors) | 🔲 User responsibility |
| Company Registration | CIPC registration documents | 🔲 User responsibility |
| Professional Memberships | e.g. ECSA, SACPCMP (where applicable) | 🔲 User responsibility |

> **Note:** TenderScan's Compliance Tracker feature (Phase 3+) will allow users to track their own compliance document expiry dates. TenderScan does not verify or store these documents.
