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
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["qty"] = pd.to_numeric(df["qty"], errors="coerce")
    return df


def clean_text_columns(df):
# Clean text columns by stripping whitespace and converting to lowercase
    df["prodname"] = df["prodname"].astype(str).str.strip().str.lower()
    df["category"] = (
        df["category"]
        .astype(str)
        .str.replace('"', '', regex=False)
        .str.strip()
        .str.lower()
    )
    return df


def handle_missing_values(df):
# Handling missing values by dropping rows with missing price or quantity
    df = df.dropna(subset=["price", "qty"])
    return df


def remove_invalid_rows(df):
# Remove rows with negative price or quantity
    df = df[(df["price"] >= 0) & (df["qty"] >= 0)]
    return df


def remove_duplicates(df):
# Remove duplicate rows
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