import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# ===========================
# Project: Book Scraper
# Website: https://books.toscrape.com
# Goal: Scrape Title, Price, and Availability from multiple pages
# ===========================

# Step 1: Set up a session with retry logic
session = requests.Session()
retries = Retry(total=3, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
session.mount('https://', HTTPAdapter(max_retries=retries))

# Step 2: Define the base URL with a placeholder for page number
base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

# Step 3: Create an empty list to store all books
all_books = []

# Step 4: Scrape pages 1 to 5 with error handling
try:
    for page in range(1, 6):  # Loop through pages 1 to 5
        print(f"🔄 Scraping page {page}...")

        # Step 5: Construct the URL for the current page
        url = base_url.format(page)

        # Step 6: Send a request to the page with retries
        try:
            response = session.get(url, timeout=10)
            response.raise_for_status()  # Check for HTTP errors

            # Step 7: Parse the HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            # Step 8: Find all book containers on the page
            books = soup.find_all('article', class_='product_pod')

            # Step 9: Loop through books and collect details
            for book in books:
                try:
                    title = book.h3.a['title']
                    price = book.find('p', class_='price_color').text
                    availability = book.find('p', class_='instock availability').text.strip()

                    # Print details (for feedback while running)
                    print(f'Title: {title}')
                    print(f'Price: {price}')
                    print(f'Availability: {availability}')
                    print('-' * 30)

                    # Store each book as a dictionary in the list
                    all_books.append({
                        'Title': title,
                        'Price': price,
                        'Availability': availability
                    })
                except AttributeError as e:
                    print(f"Error extracting book details on page {page}: {e}")
                    continue

            # Step 10: Pause 2–4 seconds to avoid getting blocked
            delay = random.uniform(2, 4)  # Increased delay
            print(f"Pausing for {delay:.2f} seconds...")
            time.sleep(delay)

        except requests.RequestException as e:
            print(f"Error fetching page {page}: {e}")
            continue

    # Step 11: Save all collected data to CSV
    if all_books:  # Check if we collected any books
        df = pd.DataFrame(all_books)
        df.to_csv('books_multi_page.csv', index=False)
        print(f"✅ All done! Saved {len(all_books)} books to books_multi_page.csv")
    else:
        print("⚠️ No books were collected. Check for errors above.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")