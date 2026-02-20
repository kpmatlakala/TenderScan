"""
TenderScan - eTenders Scraper
Scrapes public tender metadata from eTenders.gov.za and saves to CSV/JSON.

Usage:
    python scraper.py

Note:
    This script scrapes only public metadata. No documents are downloaded or hosted.
    Data is attributed to the National Treasury eTender Portal.
"""

import csv
import json
import time
import os
from datetime import datetime

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.etenders.gov.za/Home/opportunities"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
REQUEST_DELAY = 2  # seconds between requests, to respect rate limits


def fetch_page(url: str, params: dict = None) -> BeautifulSoup | None:
    """Fetch a page and return a BeautifulSoup object, or None on failure."""
    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        return BeautifulSoup(response.text, "lxml")
    except requests.RequestException as e:
        print(f"[ERROR] Failed to fetch {url}: {e}")
        return None


def parse_tenders(soup: BeautifulSoup) -> list[dict]:
    """Parse tender listings from a results page and return a list of records."""
    tenders = []
    rows = soup.select("table tbody tr")
    for row in rows:
        cells = row.find_all("td")
        if len(cells) < 5:
            continue
        tender = {
            "reference_number": cells[0].get_text(strip=True),
            "description": cells[1].get_text(strip=True),
            "advertised_by": cells[2].get_text(strip=True),
            "closing_date": cells[3].get_text(strip=True),
            "category": cells[4].get_text(strip=True),
            "source": "National Treasury eTender Portal",
            "scraped_at": datetime.utcnow().isoformat(),
        }
        tenders.append(tender)
    return tenders


def save_to_csv(tenders: list[dict], filename: str) -> None:
    """Save tender records to a CSV file."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filepath = os.path.join(OUTPUT_DIR, filename)
    if not tenders:
        print("[INFO] No tenders to save.")
        return
    fieldnames = list(tenders[0].keys())
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tenders)
    print(f"[INFO] Saved {len(tenders)} tenders to {filepath}")


def save_to_json(tenders: list[dict], filename: str) -> None:
    """Save tender records to a JSON file."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(tenders, f, indent=2, ensure_ascii=False)
    print(f"[INFO] Saved {len(tenders)} tenders to {filepath}")


def scrape(max_pages: int = 5) -> list[dict]:
    """Scrape tender listings across multiple pages."""
    all_tenders = []
    for page in range(1, max_pages + 1):
        print(f"[INFO] Scraping page {page}...")
        soup = fetch_page(BASE_URL, params={"page": page})
        if soup is None:
            break
        tenders = parse_tenders(soup)
        if not tenders:
            print(f"[INFO] No tenders found on page {page}. Stopping.")
            break
        all_tenders.extend(tenders)
        time.sleep(REQUEST_DELAY)
    return all_tenders


if __name__ == "__main__":
    tenders = scrape(max_pages=5)
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    save_to_csv(tenders, f"tenders_{timestamp}.csv")
    save_to_json(tenders, f"tenders_{timestamp}.json")
