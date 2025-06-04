import pandas as pd
import numpy as np


def print_welcome():
    print(" Welcome to Mini Data Scientist: Excel Analyzer!\n")


def load_excel_file():
    while True:
        path = input("Enter the path to your Excel (.xlsx) file: ").strip()
        try:
            df = pd.read_excel(path)
            print("\n File loaded successfully!\n")
            return df
        except Exception as e:
            print(f" Error loading file: {e}\nPlease try again.\n")


def choose_column(df):
    print(" Available columns:")
    for col in df.columns:
        print(f" - {col}")
    print()

    while True:
        col_name = input("Which numeric column would you like to analyze? ").strip()
        if col_name in df.columns:
            if pd.api.types.is_numeric_dtype(df[col_name]):
                return col_name
            else:
                print(" Selected column is not numeric. Please choose another.\n")
        else:
            print("  Column not found. Try again.\n")


def compute_statistics(series):
    mean = round(series.mean(), 2)
    median = round(series.median(), 2)
    std_dev = round(series.std(), 2)

    return mean, median, std_dev


def display_histogram(series):
    print("\n  Histogram (ASCII):")

    bins = np.histogram_bin_edges(series, bins=5)
    hist, _ = np.histogram(series, bins=bins)

    for i in range(len(hist)):
        lower = round(bins[i], 2)
        upper = round(bins[i + 1], 2)
        bar = "#" * hist[i]
        print(f"{lower:.2f} - {upper:.2f}: {bar}")


def main():
    print_welcome()
    df = load_excel_file()
    column = choose_column(df)
    data = df[column].dropna()

    mean, median, std_dev = compute_statistics(data)

    print(f"\n Results for column: {column}")
    print(f" - Mean: {mean}")
    print(f" - Median: {median}")
    print(f" - Standard Deviation: {std_dev}")

    display_histogram(data)


if __name__ == "__main__":
    main()
