📘 Advanced Book Web Scraper

A powerful, production-ready Python scraper that extracts structured book data (title, price, availability) from [BooksToScrape.com](https://books.toscrape.com). This project showcases advanced scraping features such as pagination, polite scraping practices, logging, and clean CSV export — all designed for real-world freelance or business use cases.

---

 🔍 Project Purpose

This repository is part of my **Web Scraping Portfolio** — a curated collection of professional-grade Python scraping tools that automate data collection from various domains like e-commerce, job boards, and product catalogs.

---

 💡 Features

- ✅ Multi-page scraping (pagination supported)
- ✅ Customizable page limits via CLI
- ✅ Polite scraping (randomized delay, headers)
- ✅ Robust error handling and logging
- ✅ Structured data export to CSV
- ✅ Clean, production-ready code with comments

---

 🛠 Tech Stack

| Tool          | Purpose                          |
|---------------|----------------------------------|
| `requests`    | Fetches raw HTML content         |
| `BeautifulSoup` | Parses and navigates HTML       |
| `pandas`      | Stores and exports structured data |
| `logging`     | Tracks process and errors        |
| `argparse`    | Handles command-line arguments   |

---
 🧪 Sample Output

All book data is saved in a clean CSV format: `books_multi_page.csv`

| Title                  | Price   | Availability |
|------------------------|---------|--------------|
| A Light in the Attic   | £51.77  | In stock     |
| Tipping the Velvet     | £53.74  | In stock     |

---

 ⚙️ Usage

 🔧 Step 1 – Install requirements
```bash
pip install requests beautifulsoup4 pandas
python book_scraper_pro.py --pages 5

