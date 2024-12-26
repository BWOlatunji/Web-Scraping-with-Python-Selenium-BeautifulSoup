from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the website and path to ChromeDriver
web = "https://www.audible.com/search"
path = "chromedriver.exe"

# Set up the service and driver
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

# Open the website
driver.get(web)

# Wait for the page to load (adjust as necessary)
time.sleep(5)

# Locate the product list items
products = driver.find_elements(By.XPATH, "//li[contains(@class, 'productListItem')]")

# Initialize lists to hold data
book_title = []
book_subtitle = []
book_author = []
book_runtime = []
book_reg_price = []
book_release_date = []
book_ratings = []  # List to hold ratings

# Loop over each product and extract information
for product in products:
    try:
        # Extract the book title
        title = product.find_element(
            By.XPATH, ".//h3[contains(@class, 'bc-heading')]//a"
        ).text
        book_title.append(title)

        # Extract the subtitle (if available)
        try:
            subtitle = product.find_element(
                By.XPATH, ".//li[contains(@class, 'subtitle')]//span"
            ).text
        except:  # noqa: E722
            subtitle = None
        book_subtitle.append(subtitle)

        # Extract the author (if available)
        try:
            author = product.find_element(
                By.XPATH, ".//li[contains(@class, 'authorLabel')]//a"
            ).text
        except:  # noqa: E722
            author = None
        book_author.append(author)

        # Extract the runtime (if available)
        try:
            runtime = product.find_element(
                By.XPATH, ".//li[contains(@class, 'runtimeLabel')]//span"
            ).text
        except:  # noqa: E722
            runtime = None
        book_runtime.append(runtime)

        # Extract the regular price (if available)
        try:
            reg_price = product.find_element(
                By.XPATH, ".//p[contains(@id,'buybox-regular-price')]//span[2]"
            ).text
        except:  # noqa: E722
            reg_price = None
        book_reg_price.append(reg_price)

        # Extract the release date (if available)
        try:
            release_date = product.find_element(
                By.XPATH, ".//li[contains(@class, 'releaseDateLabel')]//span"
            ).text
        except:  # noqa: E722
            release_date = None
        book_release_date.append(release_date)

        # Extract the ratings (if available)
        try:
            ratings = product.find_element(
                By.XPATH,
                ".//li[contains(@class, 'ratingsLabel')]//span[contains(@class, 'bc-pub-offscreen')]",
            ).text
        except:  # noqa: E722
            ratings = None
        book_ratings.append(ratings)

    except Exception as e:
        print(f"Error processing product: {e}")

# Quit the driver
driver.quit()

# Check if any data was scraped
if book_title:
    # Create a DataFrame and save it as a CSV file
    df_books = pd.DataFrame(
        {
            "title": book_title,
            "subtitle": book_subtitle,
            "author": book_author,
            "runtime": book_runtime,
            "regular_price": book_reg_price,
            "release_date": book_release_date,
            "ratings": book_ratings,
        }
    )

    # Save to CSV
    df_books.to_csv("books.csv", index=False)
    print("CSV file 'books.csv' saved successfully.")
else:
    print("No data scraped.")
