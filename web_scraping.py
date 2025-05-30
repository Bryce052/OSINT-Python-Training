# web_scraping.py

"""
Sections 4 & 5: Gathering, Parsing, Cleaning, and Storing OSINT Data

This script demonstrates:
- How to scrape and crawl web pages (Section 4)
- How to parse and clean scraped data (Section 5)
- How to save data to CSV and SQLite databases

Always scrape responsibly and legally!
"""

import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import sqlite3

# -------------------------
# Section 4: Web scraping and crawling

def scrape_quotes_page(url):
    """
    Scrape quotes and authors from a single page.
    Returns a list of [quote, author] pairs.
    """
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve {url}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    quotes_data = []

    # Each quote is inside a div with class 'quote'
    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        quotes_data.append([text, author])

    return quotes_data

def crawl_quotes(base_url):
    """
    Crawl through multiple pages of the quotes website.
    Returns a list of all [quote, author] pairs found.
    """
    all_quotes = []
    page = 1

    while True:
        url = f"{base_url}page/{page}/"
        print(f"Scraping Page {page}: {url}")

        quotes = scrape_quotes_page(url)

        if not quotes:
            print("No more quotes found or reached end of pages.")
            break

        all_quotes.extend(quotes)
        page += 1

    return all_quotes

# -------------------------
# Section 5: Parsing, cleaning, and storing

def save_quotes_to_csv(quotes, filename):
    """
    Save list of [quote, author] pairs to a CSV file.
    """
    with open(filename, mode="w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author"])  # header
        writer.writerows(quotes)
    print(f"Quotes saved to {filename}")

def clean_quotes_csv(input_csv, output_csv):
    """
    Load CSV, clean quotes and authors, and save cleaned data.
    """
    df = pd.read_csv(input_csv)

    # Remove fancy quotes and extra whitespace
    df["Quote"] = df["Quote"].str.replace("“|”", "", regex=True)
    df["Quote"] = df["Quote"].str.strip()
    df["Author"] = df["Author"].str.strip()

    df.to_csv(output_csv, index=False)
    print(f"Cleaned quotes saved to {output_csv}")

def save_to_sqlite(csv_file, db_file):
    """
    Load cleaned CSV into SQLite database.
    """
    df = pd.read_csv(csv_file)

    conn = sqlite3.connect(db_file)
    df.to_sql("quotes", conn, if_exists="replace", index=False)
    print(f"Data saved to SQLite database '{db_file}'")

    # Example queries
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM quotes;")
    total = cursor.fetchone()[0]
    print(f"Total quotes in the database: {total}")

    cursor.execute("SELECT * FROM quotes LIMIT 5;")
    rows = cursor.fetchall()

    print("\nHere are 5 sample quotes:")
    for row in rows:
        print(row)

    conn.close()

# -------------------------
# Main execution

if __name__ == "__main__":
    base_url = "https://quotes.toscrape.com/"

    print("Starting web scraping and crawling...")
    quotes = crawl_quotes(base_url)

    csv_file = "quotes.csv"
    cleaned_csv_file = "quotes_cleaned.csv"
    sqlite_db_file = "osint_quotes.db"

    save_quotes_to_csv(quotes, csv_file)
    clean_quotes_csv(csv_file, cleaned_csv_file)
    save_to_sqlite(cleaned_csv_file, sqlite_db_file)

    print("\nAll done! You can open the CSV files or the SQLite database with your preferred tools.")
