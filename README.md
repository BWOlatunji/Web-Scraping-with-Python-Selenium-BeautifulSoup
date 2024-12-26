# Web Scraping Project Description

## Project Overview

This project involved web scraping car listing data from the Cars45 website using Python and Selenium. The goal was to extract detailed information about cars, such as price, make, model, year of manufacture, color, mileage, condition, engine size, registered city, selling condition, and bought condition. The extracted data was stored in a CSV file for further analysis or use.

The project was divided into two phases:

1. Scraping car details from each listing page across multiple pages.
2. Navigating to individual car detail pages to gather specific attributes.

### Tools & Technologies

- **Python**: Used for scripting and data processing.
- **Selenium**: A web automation tool to interact with the website, navigate through pages, and extract the required information.
- **Pandas**: Data manipulation and saving results to CSV files.
- **Regular Expressions (re)**: Clean up extracted data where necessary.

## Project Phases

### Phase 1: Extracting Car Listings

The project started by accessing the Cars45 website and retrieving car listings across multiple pages. The process included:

- Loading each listing page by incrementing the page number in the URL.
- Extracting basic details such as price, car name, region, condition, mileage, and the image URL.
- Capturing the URL for each car detail page for further scraping.

### Phase 2: Extracting Detailed Car Information

In this phase, we used the URLs collected in Phase 1 to navigate to individual car detail pages and scrape the following information:

- Make
- Model
- Year of Manufacture
- Color
- Condition
- Mileage
- Engine Size
- Registered City
- Selling Condition
- Bought Condition
- Transmission System

Each car detail page was scraped using custom XPaths, and error handling was implemented to ensure data consistency in cases where some details were missing for some cars.

## Error Handling & Data Quality

We implemented error handling to ensure the scraping process continued even if some elements were missing from the page. When fewer than 11 expected details were found, the script automatically appended 'N/A' for the missing data, ensuring the output remained consistent.

## Final Output

The final output was saved as a CSV file containing columns for car details, including pricing, car condition, mileage, and more. This dataset can be used for analysis, reporting, or ML projects.

## Conclusion

This project demonstrated the effective use of Selenium for automating web data extraction and Python's Pandas library for handling and saving data. The extracted information can be valuable for marketing, sales, or business intelligence purposes, especially when looking to analyze car markets, customer preferences, or price comparisons.


