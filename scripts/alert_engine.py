"""
TenderScan - Alert Engine
Filters scraped tender data against a user profile and sends email notifications.

Usage:
    python alert_engine.py

Configuration:
    Copy .env.example to .env and fill in SMTP credentials before running.
"""

import csv
import json
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()

SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASS = os.getenv("SMTP_PASS", "")
ALERT_FROM = os.getenv("ALERT_FROM", SMTP_USER)

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")


def load_tenders(filepath: str) -> list[dict]:
    """Load tender records from a CSV or JSON file."""
    if filepath.endswith(".json"):
        with open(filepath, encoding="utf-8") as f:
            return json.load(f)
    records = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        records = list(reader)
    return records


def filter_tenders(tenders: list[dict], profile: dict) -> list[dict]:
    """
    Filter tenders against a user profile.

    Profile keys (all optional):
        keywords  (list[str]): match against description
        category  (str):       exact category match
        province  (str):       substring match against advertised_by
    """
    keywords = [kw.lower() for kw in profile.get("keywords", [])]
    category = profile.get("category", "").lower()
    province = profile.get("province", "").lower()

    matched = []
    for tender in tenders:
        description = tender.get("description", "").lower()
        tender_category = tender.get("category", "").lower()
        advertised_by = tender.get("advertised_by", "").lower()

        if keywords and not any(kw in description for kw in keywords):
            continue
        if category and category not in tender_category:
            continue
        if province and province not in advertised_by:
            continue
        matched.append(tender)
    return matched


def build_email_body(tenders: list[dict]) -> str:
    """Build a plain-text email body listing matched tenders."""
    if not tenders:
        return "No matching tenders found in the latest scan."
    lines = ["TenderScan — Matching Opportunities\n", "=" * 40]
    for t in tenders:
        lines.append(f"\nRef:     {t.get('reference_number', 'N/A')}")
        lines.append(f"Title:   {t.get('description', 'N/A')}")
        lines.append(f"By:      {t.get('advertised_by', 'N/A')}")
        lines.append(f"Closes:  {t.get('closing_date', 'N/A')}")
        lines.append(f"Source:  {t.get('source', 'National Treasury eTender Portal')}")
        lines.append("-" * 40)
    lines.append(
        "\nVisit https://www.etenders.gov.za to view full details and download documents."
    )
    return "\n".join(lines)


def send_alert(recipient: str, tenders: list[dict]) -> None:
    """Send an email alert with matched tenders to a recipient."""
    if not SMTP_USER or not SMTP_PASS:
        print("[WARN] SMTP credentials not configured. Skipping email send.")
        print(build_email_body(tenders))
        return

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"TenderScan Alert — {len(tenders)} new matching tender(s)"
    msg["From"] = ALERT_FROM
    msg["To"] = recipient
    body = build_email_body(tenders)
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.ehlo()
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(ALERT_FROM, recipient, msg.as_string())
        print(f"[INFO] Alert sent to {recipient} with {len(tenders)} tender(s).")
    except smtplib.SMTPException as e:
        print(f"[ERROR] Failed to send email to {recipient}: {e}")


def run(tender_file: str, profile: dict, recipient: str) -> None:
    """Load, filter, and alert for a given tender file and user profile."""
    print(f"[INFO] Loading tenders from {tender_file}...")
    tenders = load_tenders(tender_file)
    print(f"[INFO] {len(tenders)} tenders loaded. Filtering...")
    matched = filter_tenders(tenders, profile)
    print(f"[INFO] {len(matched)} tenders matched the profile.")
    send_alert(recipient, matched)


if __name__ == "__main__":
    import glob

    json_files = sorted(glob.glob(os.path.join(DATA_DIR, "tenders_*.json")))
    if not json_files:
        print("[ERROR] No tender data files found. Run scraper.py first.")
    else:
        latest_file = json_files[-1]
        example_profile = {
            "keywords": ["ICT", "software", "digital"],
            "province": "limpopo",
        }
        example_recipient = os.getenv("ALERT_RECIPIENT", "user@example.com")
        run(latest_file, example_profile, example_recipient)
