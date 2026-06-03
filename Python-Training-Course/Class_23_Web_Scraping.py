# Class 23 - Web Scraping with BeautifulSoup

# First install the libraries
# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

# Get a webpage
url = "https://books.toscrape.com"
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    print("Page loaded successfully!")
else:
    print("Failed to load page")

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Get page title
print(soup.title.text)

# Get all book titles
books = soup.find_all("h3")
for book in books[:5]:      # first 5 books only
    print(book.a["title"])

# Get all prices
prices = soup.find_all("p", class_="price_color")
for price in prices[:5]:    # first 5 prices
    print(price.text)
