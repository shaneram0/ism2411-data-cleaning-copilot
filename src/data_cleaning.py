"""
This script cleans messy sales data by standardizing column names,
handling missing values, and removing invalid rows.
"""

import pandas as pd


def load_data(file_path: str):
# Load data from a CSV file
    try:
        df = pd.read_csv(file_path)
        print(f"CSV file data loaded successfully! {file_path}")
        return df
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        return None

def clean_column_names(df):
# Standardize column names by converting to lowercase and replacing spaces with underscores
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df

def handle_missing_values(df):
# Handle missing values in the DataFrame."""
    df = df.dropna()
    return df

def remove_invalid_rows(df):
# Remove rows with invalid data
    df = df[df['price'] >= 0]
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