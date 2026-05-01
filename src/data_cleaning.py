"""
This script cleans messy sales data by:
- Standardizing column names
- Cleaning text fields
- Converting data types
- Handling missing values
- Removing invalid rows
- Removing duplicates
"""

import pandas as pd


# Load the dataset from a CSV file
def load_data(file_path: str):
    df = pd.read_csv(file_path)
    return df


# Standardize column names
def clean_column_names(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df


# Convert price and quantity to numeric
def convert_data_types(df):
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["qty"] = pd.to_numeric(df["qty"], errors="coerce")
    return df


# Clean text columns (fix spacing, quotes, casing)
def clean_text_columns(df):
    df["prodname"] = df["prodname"].astype(str).str.strip().str.lower()
    df["category"] = (
        df["category"]
        .astype(str)
        .str.replace('"', '', regex=False)
        .str.strip()
        .str.lower()
    )
    return df


# Handle missing values
def handle_missing_values(df):
    df = df.dropna(subset=["price", "qty"])
    return df


# Remove invalid rows
def remove_invalid_rows(df):
    df = df[(df["price"] >= 0) & (df["qty"] >= 0)]
    return df


# Remove duplicate rows
def remove_duplicates(df):
    df = df.drop_duplicates()
    return df


if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)

    df_clean = clean_column_names(df_raw)
    df_clean = convert_data_types(df_clean)
    df_clean = clean_text_columns(df_clean)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    df_clean = remove_duplicates(df_clean)

    df_clean.to_csv(cleaned_path, index=False)

    print("Cleaning complete. First few rows:")
    print(df_clean.head())