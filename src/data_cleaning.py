"""
This script cleans messy sales data by standardizing column names,
handling missing values, and removing invalid rows.
"""

import pandas as pd


def load_data(file_path: str):
#load the data from the CSV file
    try: 
        df = pd.read_csv(file_path)
        print(f"Sales Data loaded from {file_path}!")
        return df
    except Exception as e:
        print(f"Error loading data, Data Invalid: {e}")
        return None
def clean_column_names(df):
# Standardize column names by converting to lowercase and replacing spaces with underscores
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df
def convert_data_types(df):
# Convert price and quanity to numeric values
    df["price"] = pd.to_numeric(df["price"])
    df["qty"] = pd.to_numeric(df["qty"])
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

def remove_invalid_rows(df):
# Remove rows with negative price or quantity
    def remove_invalid_rows(df):
    df = df[(df["price"] >= 0) & (df["qty"] >= 0)]
    return df

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())