from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re
import time

# Define the website and path to ChromeDriver
base_url = "https://www.cars45.com/listing?page="
path = "chromedriver.exe"

# Set up the service and driver
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

# Initialize lists to hold car details
car_amount = []
car_name = []
car_region = []
car_condition = []
car_mileage = []
car_image = []
car_details_url = []


# Function to extract car details from the current page
def extract_car_details():
    # Locate the cars on the page
    cars = driver.find_elements(By.XPATH, "//section[@class='cars-grid grid']//a")

    # Loop through each car and extract the details
    for car in cars:
        try:
            # Extract the car amount (e.g., ₦5,000,000)
            amount = car.find_element(
                By.XPATH,
                ".//div[@class='car-feature__details']//p[@class='car-feature__amount']",
            ).text

            # Use regular expressions to extract only the numeric part (removing ₦ and commas)
            numeric_value = re.sub(r"[^\d]", "", amount)
            car_amount.append(numeric_value)

            name = car.find_element(
                By.XPATH,
                ".//div[@class='car-feature__details']//p[@class = 'car-feature__name']",
            ).text
            car_name.append(name)

            region = car.find_element(
                By.XPATH,
                ".//div[@class='car-feature__details']//p[@class = 'car-feature__region']",
            ).text
            car_region.append(region)

            condition = car.find_element(
                By.XPATH,
                ".//div[@class='car-feature__details']//div[@class='car-feature__others']//span[@class = 'car-feature__others__item']",
            ).text
            car_condition.append(condition)

            mileage = car.find_element(
                By.XPATH,
                ".//div[@class='car-feature__details']//div[@class='car-feature__others']//span[@class = 'car-feature__others__item'][last()]",
            ).text
            car_mileage.append(mileage)

            image = car.find_element(
                by=By.XPATH, value=".//div[@class = 'car-feature__image']//img"
            ).get_attribute("src")  # Extract image URL
            car_image.append(image)

            car_url = car.get_attribute("href")  # Extract car details URL
            car_details_url.append(car_url)

        except Exception as e:
            print(f"Error retrieving car details: {e}")


# Open the website's first page
driver.get(base_url + "1")

# Wait for the page to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//section[@class='cars-grid grid']//a"))
)

# Get the total number of pages from the last page link
last_page_link = driver.find_element(
    By.XPATH, "//div[@class = 'pagination__button h-flex-center']/a[last()-1]"
)
total_pages = int(last_page_link.text)  # Extract the number of the last page
print(f"Total number of pages: {total_pages}")

# Loop through all pages
for page_num in range(1, total_pages + 1):
    try:
        # Navigate to the current page URL
        current_url = base_url + str(page_num)
        driver.get(current_url)
        print(f"Scraping page {page_num}...")

        # Wait for the page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//section[@class='cars-grid grid']//a")
            )
        )

        # Extract car details from the current page
        extract_car_details()

        # Wait before moving to the next page (if needed)
        time.sleep(2)

    except Exception as e:
        print(f"Error scraping page {page_num}: {e}")
        break

# Convert the data to a DataFrame
df = pd.DataFrame(
    {
        "amount": car_amount,
        "name": car_name,
        "region": car_region,
        "condition": car_condition,
        "mileage": car_mileage,
        "image_url": car_image,
        "details_url": car_details_url,
    }
)

# Save the data to a CSV file
df.to_csv("new_cars_data.csv", index=False, encoding="utf-8")

# Quit the driver
driver.quit()
