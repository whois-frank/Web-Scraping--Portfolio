 Web-Scraping--Portfolio
 A curated collection of Python-based web scraping tools and projects that automate data extraction, cleaning, and export from real-world websites like e-commerce, job boards, and book catalogs.
Advanced Book Web Scraper

 Overview
This Python scraper extracts detailed book data from [BooksToScrape.com](https://books.toscrape.com), demonstrating advanced scraping techniques like pagination, user-agent rotation, error handling, and logging. Ideal for building real-world scraping projects or freelance gigs.

 Features
- Multi-page scraping with customizable page limit (CLI support)
- - Polite scraping: custom headers & randomized delays
  - - Robust error handling & logging for troubleshooting
    - - Output clean CSV file ready for analysis or client delivery
     
      -  Tech Stack
      - - Python 3.x
        - - requests, BeautifulSoup4, pandas
          - - logging module for progress and error tracking
           
            -  Usage
            - ```bash
              pip install -r requirements.txt
              python book_scraper_pro.py --pages 10
