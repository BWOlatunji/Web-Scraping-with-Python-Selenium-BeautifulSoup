# Load necessary libraries
library(rvest)
library(dplyr)

# Define the URL of the Audible search page
url <- "https://www.audible.com/search"

# Read the HTML from the page
webpage <- read_html(url)

# Extract book titles
book_title <- webpage %>%
  html_nodes(xpath = "//li[contains(@class, 'productListItem')]//h3[contains(@class, 'bc-heading')]//a") %>%
  html_text(trim = TRUE)

# Extract subtitles (if available)
book_subtitle <- webpage %>%
  html_nodes(xpath = "//li[contains(@class, 'productListItem')]//li[contains(@class, 'subtitle')]//span") %>%
  html_text(trim = TRUE)

# Extract authors (if available)
book_author <- webpage %>%
  html_nodes(xpath = "//li[contains(@class, 'productListItem')]//li[contains(@class, 'authorLabel')]//span//a") %>%
  html_text(trim = TRUE)

# Extract runtime (if available)
book_runtime <- webpage %>%
  html_nodes(xpath = "//li[contains(@class, 'productListItem')]//li[contains(@class, 'runtimeLabel')]//span") %>%
  html_text(trim = TRUE)

# Extract regular prices (if available)
book_reg_price <- webpage %>%
  html_nodes(xpath = "//li[contains(@class, 'productListItem')]//p[contains(@id, 'buybox-regular-price')]//span[2]") %>%
  html_text(trim = TRUE)

# Extract release dates (if available)
book_release_date <- webpage %>%
  html_nodes(xpath = "//li[contains(@class, 'productListItem')]//li[contains(@class, 'releaseDateLabel')]//span") %>%
  html_text(trim = TRUE)

# Extract ratings (if available)
book_ratings <- webpage %>%
  html_nodes(xpath = "//li[contains(@class, 'productListItem')]//li[contains(@class, 'ratingsLabel')]//span[contains(@class, 'bc-pub-offscreen')]") %>%
  html_text(trim = TRUE)

# Combine all the data into a data frame
df_books <- data.frame(
  title = book_title,
  subtitle = book_subtitle,
  author = book_author,
  runtime = book_runtime,
  regular_price = book_reg_price,
  release_date = book_release_date,
  ratings = book_ratings,
  stringsAsFactors = FALSE
)

# Save the data to a CSV file
write.csv(df_books, "rbooks.csv", row.names = FALSE)

# Output a message when the CSV is successfully saved
cat("CSV file 'books.csv' saved successfully.\n")
