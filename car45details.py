from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Load the CSV file containing car detail URLs
car_data = pd.read_csv("new_cars_data.csv")
# car_data = car_data.head()
car_urls = car_data["details_url"].tolist()

# Define the path to ChromeDriver
path = "chromedriver.exe"

# Set up the service and driver
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

# Initialize lists for car details
make = []
model = []
year_of_manufacture = []
color = []
car_condition = []
mileage = []
engine_size = []
registered_city = []
selling_condition = []
bought_condition = []
transmission_system = []


# Function to extract car details with error handling for missing elements
def extract_car_details(url):
    try:
        driver.get(url)
        time.sleep(2)  # Wait for the page to load

        # Extract the information from the car detail page
        try:
            transmission = driver.find_element(
                By.XPATH, "//div[contains(@class, 'main-details__tags')]//span[2]"
            ).text
        except Exception:
            transmission = "N/A"
        transmission_system.append(transmission)

        try:
            make_value = driver.find_element(
                By.XPATH, "//div//span[text()='Make']//preceding-sibling::p"
            ).text
        except Exception:
            make_value = "N/A"
        make.append(make_value)

        try:
            model_value = driver.find_element(
                By.XPATH, "//div//span[text()='Model']//preceding-sibling::p"
            ).text
        except Exception:
            model_value = "N/A"
        model.append(model_value)

        try:
            year_value = driver.find_element(
                By.XPATH,
                "//div//span[text()='Year of manufacture']//preceding-sibling::p",
            ).text
        except Exception:
            year_value = "N/A"
        year_of_manufacture.append(year_value)

        try:
            color_value = driver.find_element(
                By.XPATH, "//div//span[text()='Colour']//preceding-sibling::p"
            ).text
        except Exception:
            color_value = "N/A"
        color.append(color_value)

        try:
            condition_value = driver.find_element(
                By.XPATH, "//div//span[text()='Condition']//preceding-sibling::p"
            ).text
        except Exception:
            condition_value = "N/A"
        car_condition.append(condition_value)

        try:
            mileage_value = driver.find_element(
                By.XPATH, "//div//span[text()='Mileage']//preceding-sibling::p"
            ).text
        except Exception:
            mileage_value = "N/A"
        mileage.append(mileage_value)

        try:
            engine_size_value = driver.find_element(
                By.XPATH, "//div//span[text()='Engine Size']//preceding-sibling::p"
            ).text
        except Exception:
            engine_size_value = "N/A"
        engine_size.append(engine_size_value)

        try:
            registered_city_value = driver.find_element(
                By.XPATH, "//div//span[text()='Registered city']//preceding-sibling::p"
            ).text
        except Exception:
            registered_city_value = "N/A"
        registered_city.append(registered_city_value)

        try:
            selling_condition_value = driver.find_element(
                By.XPATH,
                "//div//span[text()='Selling Condition']//preceding-sibling::p",
            ).text
        except Exception:
            selling_condition_value = "N/A"
        selling_condition.append(selling_condition_value)

        try:
            bought_condition_value = driver.find_element(
                By.XPATH, "//div//span[text()='Bought Condition']//preceding-sibling::p"
            ).text
        except Exception:
            bought_condition_value = "N/A"
        bought_condition.append(bought_condition_value)

    except Exception as e:
        print(f"Error extracting details from {url}: {e}")


# Loop through all car URLs and extract details
for url in car_urls:
    extract_car_details(url)

# Convert the data to a DataFrame
df = pd.DataFrame(
    {
        "make": make,
        "model": model,
        "year_of_manufacture": year_of_manufacture,
        "color": color,
        "condition": car_condition,
        "mileage": mileage,
        "engine_size": engine_size,
        "registered_city": registered_city,
        "selling_condition": selling_condition,
        "bought_condition": bought_condition,
        "transmission_system": transmission_system,
    }
)

# Save the data to a CSV file
df.to_csv("car_details_data.csv", index=False, encoding="utf-8")

# Quit the driver
driver.quit()
