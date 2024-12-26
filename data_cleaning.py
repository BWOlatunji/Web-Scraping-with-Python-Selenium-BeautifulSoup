import pandas as pd

# Load the CSV file containing car detail URLs
car_data = pd.read_csv("new_cars_data.csv")

# split the Name column into two columns
car_data[["registered_state", "registered_city"]] = car_data["region"].str.split(
    ", ", expand=True
)
# Drop columns "region", "condition", and "mileage"
car_data = car_data.drop(["region", "condition", "mileage"], axis=1)

# Load the CSV file containing car detail URLs
car_details_data = pd.read_csv("car_details_data.csv")


# Drop rows that have complete missing data
# car_details_data.dropna(axis=0, inplace=True, how="all")

# Find the indices of rows where all elements are NaN
na_rows_indices = car_details_data[car_details_data.isna().all(axis=1)].index.tolist()

# Output the indices
print(f"Indices of rows with all NAs: {na_rows_indices}")

car_details_data["details_url"] = car_data["details_url"]
# Drop columns "registered_city"
car_details_data = car_details_data.drop("registered_city", axis=1)
# merge on details_url
combined_car_data = car_data.merge(car_details_data, on="details_url", how="inner")

# Remove rows with complete NaN values using the indices
combined_car_data_cleaned = combined_car_data.drop(na_rows_indices)

# Save the data to a CSV file
combined_car_data_cleaned.to_csv(
    "combined_car_data_cleaned.csv", index=False, encoding="utf-8"
)
# Write DataFrame to Parquet
combined_car_data_cleaned.to_parquet("combined_car_data_cleaned.parquet")

print(car_data.shape)
print(car_details_data.shape)
print(combined_car_data.shape)
# Output the cleaned DataFrame
print(combined_car_data_cleaned.shape)
