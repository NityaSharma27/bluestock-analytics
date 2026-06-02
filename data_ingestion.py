import pandas as pd
import os

# =====================
# TASK 3 - Load All 10 CSV Files
# =====================

print("=" * 60)
print("TASK 3 - LOADING ALL 10 CSV DATASETS")
print("=" * 60)

csv_files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

anomalies = []

for file in csv_files:
    path = f"data/raw/{file}"

    print(f"\n{'='*60}")
    print(f"FILE: {file}")
    print(f"{'='*60}")

    if os.path.exists(path):
        df = pd.read_csv(path)

        # Shape
        print(f"\nShape (Rows x Columns): {df.shape}")

        # Dtypes
        print(f"\nColumn Data Types:")
        print(df.dtypes)

        # Head
        print(f"\nFirst 5 Rows:")
        print(df.head())

        # Anomaly Check
        missing = df.isnull().sum()
        missing_cols = missing[missing > 0]

        if not missing_cols.empty:
            anomalies.append(f"{file} - Missing values in: {list(missing_cols.index)}")
            print(f"\nMissing Values Found:")
            print(missing_cols)
        else:
            print(f"\nNo missing values found")

    else:
        print(f"❌ File NOT FOUND: {path}")
        anomalies.append(f"{file} - File not found")

# Anomaly Summary
print(f"\n{'='*60}")
print("ANOMALY SUMMARY")
print(f"{'='*60}")

if anomalies:
    for a in anomalies:
        print(f"⚠️  {a}")
else:
    print("No anomalies found in any file!")