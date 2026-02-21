# 📊 TenderScan: Executive Summary & Overview

Automated Government Tender Intelligence for South African Tenderpreneurs

- **Prepared for:** GT Thosago, Katlego Thosago, Arehone
- **Date:** 20 February 2026
- **Prepared by:** Kabelo Matlakala, DSA Partnership Lead

## 🎯 Executive Summary

TenderScan is a lightweight automation initiative designed to reduce tender discovery time for South African SMMEs, contractors, and service providers from hours to minutes.

By scraping public tender portals (`eTenders.gov.za`, SETA portals, provincial bulletins), filtering opportunities by user profile (sector, CIDB grade, location, keywords), and delivering personalised alerts, TenderScan enables tenderpreneurs to focus on winning submissions rather than manual searching.

**Current status:**

- ✅ Manual tracker compiled (ICT, Civil, Electrical tenders + SETA grants)
- 🟡 Automation prototype in development
- 🔲 SaaS platform (future vision)

**Immediate value delivered:**

- 50+ live tender opportunities identified and categorised (Feb–Mar 2026 closing dates)
- Search-optimized tracking system deployed (Google Sheets + Drive)
- Clear pipeline for MICT SETA, Services SETA, SEDFA, and provincial opportunities
- Technical foundation laid for scalable automation (Python + Jupyter + Next.js stack)

## 📋 Project Objectives

| Objective | Description | Success Metric |
|---|---|---|
| 1. Reduce Discovery Time | Automate tender scanning across National Treasury, SETAs, and provincial portals | Users save 5+ hours/week on manual searching |
| 2. Improve Relevance | Filter opportunities by user profile (sector, CIDB, location, keywords) | 80%+ of alerts match user eligibility |
| 3. Enable Collaboration | Shared tracker + workflow for DSA team (Kabelo + Khothatso) | Real-time updates, clear ownership, weekly syncs |
| 4. Build Scalable Foundation | Prototype automation with Python/Jupyter; plan SaaS migration | MVP scraper functional; architecture documented |
| 5. Support DSA Mission | Prioritise digital skills, youth empowerment, rural Limpopo opportunities | 70%+ of tracked tenders align with DSA focus areas |

## 🔍 Current Achievements (Feb 2026)

### ✅ Manual Tracking System Deployed

- Google Sheets tracker with tabs: Pipeline, Compliance Checklist, Portal Logins
- Search-optimized fields: keywords, entity clues, closing dates, contact info, relevance scoring
- Shared Drive structure for active opportunities, compliance docs, and templates
- Collaboration workflow with real-time updates, mentions, and weekly sync protocol

### ✅ Opportunity Intelligence Compiled

| Category | Opportunities Identified | High-Priority Examples |
|---|---|---|
| ICT / Digital Skills Tenders | 15+ live tenders | Info Security Training (27 Feb), Website Dev (27 Feb), Creative Cloud Licenses (26 Feb) |
| Civil Engineering Tenders | 50+ listings (filtered) | Ba-Phalaborwa Panels (Limpopo), Polokwane Airport Maintenance |
| Electrical Tenders | 150+ listings (filtered) | GIS System for Farms, 36MW Solar PV + Training (Tutuka), Digital Radio Equipment |
| SETA Discretionary Grants | 6 SETAs mapped | MICT SETA (mid-2026), Services SETA (late-2026), W&RSETA (emerging occupations) |
| Provincial (Limpopo) Tenders | 10+ local opportunities | Community Shared Network, Mogalakwena Training Panel, Polokwane AV System |

### ✅ Technical Foundation Laid

- Repo created: <https://github.com/kpmatlakala/tenderscan-mvp> (Private)
- `README.md` drafted: mission, tech stack, compliance notes, roadmap
- Prototype environment ready: Python + Jupyter Notebook + Google Colab
- POPIA-aware, public-metadata-only compliance framework documented

## 🛠️ Technical Approach

### Phase 1: Manual + Semi-Automated (Current)

`User → Manual portal search → Google Sheet tracking → Manual filtering → Email alerts`

- Tools: Google Sheets, Google Drive, WhatsApp/Email collaboration
- Pros: Immediate value, no development time, flexible
- Cons: Time-intensive, not scalable, prone to human error

### Phase 2: Prototype Automation (Next 4–8 Weeks)

`Public Portals → Python Scraper (BeautifulSoup/Selenium) → CSV/PostgreSQL → Filter Engine → Email Alerts`

- Stack: Python 3.10+, Jupyter Notebook, `requests`, `BeautifulSoup`, `Selenium`
- Hosting: Google Colab (prototype) → VPS/Cloud Function (production)
- Key feature: keyword-guided search instructions for eTenders “no direct links” limitation

### Phase 3: SaaS Platform (Future Vision)

`User Dashboard (Next.js) ← API (Django/Node) ← PostgreSQL ← Scheduled Scrapers`

Outputs include personalised alerts, compliance tracking, and application workflow support.

Monetisation direction:

- Freemium → Tiered subscriptions (R199–R1,499/month)
- White-label path for associations and partners

## ⚠️ Key Constraints & Mitigations

| Constraint | Impact | Mitigation Strategy |
|---|---|---|
| eTenders.gov.za no direct document links | Users must manually download PDFs | Store search keywords + metadata and route users to official portal |
| Rate limiting / IP blocking risk | Scrapers can be blocked | Add delays (`time.sleep`), respect `robots.txt`, use rotating proxies in production |
| POPIA compliance | User data must be protected | Encrypt at rest, collect minimal data, privacy policy + deletion support |
| SETA accreditation requirements | Some grants require accredited SDP status | Start ETDP SETA accreditation process; partner short-term with accredited providers |
| Resource constraints (time/budget) | MVP scope pressure | Prioritise highest-ROI features (alerts + dashboard), defer payment integration |

## 🗓️ Roadmap & Next Steps

### Immediate (This Week)

- Share tracker with Katlego Thosago (Civil + Electrical tabs) ✅ Done
- Align with Arehone on technical scraping approach (meeting scheduled)
- Finalise Google Sheets detail fields (Tender Number, Contact Info, Briefing Details)
- Begin Jupyter prototype for Civil + Electrical tenders with CSV validation

### Short-Term (Next 4 Weeks)

- Build profile-based filter engine (sector, CIDB, location)
- Implement email alerts for new matched tenders
- Draft one-page SaaS concept note (for GT/Katlego review)
- Create dashboard wireframe/prototype for stakeholder feedback

### Medium-Term (Weeks 5–12)

- Migrate to PostgreSQL for users + tenders + applications
- Add user auth and multi-tenant support
- Integrate subscription payments (Stripe/PayFast)
- Run beta with DSA network + mLab contacts

### Long-Term (Beyond 12 Weeks)

- Public launch with partnerships and content strategy
- Expand sources: SETA portals, provincial bulletins, private aggregators
- Add advanced features: AI relevance scoring, compliance automation, application workflow

## 💰 Business Model Overview

| Model | Pricing | Target Customer | Pros | Cons |
|---|---|---|---|---|
| Freemium | Free (5 alerts/month), paid R299–R999/month | Early-stage tenderpreneurs | Low barrier, potential viral growth | Higher support load, conversion risk |
| Tiered Subscription | Starter R199, Pro R499, Enterprise R1,499/month | SMMEs to mid-sized firms | Predictable recurring revenue | Requires clear feature differentiation |
| White-Label | R2,000–R10,000/month | Associations, SETAs, NGOs | High-value contracts, bulk users | Longer sales cycle, customization effort |

**Recommended path:** Start with a freemium + tiered hybrid. Seed adoption via DSA partner access, then monetise external users.

## 🤝 Stakeholder Alignment

| Stakeholder | Role | Key Interest | Next Action |
|---|---|---|---|
| GT Thosago | Project Sponsor | Strategic direction, ROI, compliance | Review concept note and approve MVP scope |
| Katlego Thosago | Stakeholder / Potential User | Practical value, ease of use, mobile access | Test tracker and provide prototype feedback |
| Arehone | Technical Advisor | Feasibility, scalability, compliance | Review technical spec and scraper architecture |
| Khothatso | Collaboration Partner | Workflow efficiency, shared ownership | Use tracker and provide real-world alert feedback |
| DSA Network | Early Adopters | Relevant opportunities, time savings | Beta test MVP and provide testimonials |
