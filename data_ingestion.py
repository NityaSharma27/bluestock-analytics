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





# =====================
# TASK 6 - Fund Master Exploration
# =====================

print("\n" + "=" * 60)
print("TASK 6 - FUND MASTER EXPLORATION")
print("=" * 60)

fm = pd.read_csv("data/raw/01_fund_master.csv")

print("\n1. Unique Fund Houses:")
for fh in fm['fund_house'].unique():
    print(f"   - {fh}")

print(f"\n   Total: {fm['fund_house'].nunique()} Fund Houses")

print("\n2. Unique Categories:")
for cat in fm['category'].unique():
    print(f"   - {cat}")

print(f"\n   Total: {fm['category'].nunique()} Categories")

print("\n3. Unique Sub-Categories:")
for sub in fm['sub_category'].unique():
    print(f"   - {sub}")

print(f"\n   Total: {fm['sub_category'].nunique()} Sub-Categories")

print("\n4. Unique Risk Grades:")
for risk in fm['risk_category'].unique():
    print(f"   - {risk}")

print(f"\n   Total: {fm['risk_category'].nunique()} Risk Grades")

print("\n5. AMFI Scheme Code Structure:")
print(f"   - Total Schemes : {fm['amfi_code'].nunique()}")
print(f"   - Code Range    : {fm['amfi_code'].min()} to {fm['amfi_code'].max()}")
print(f"   - Sample Codes  : {list(fm['amfi_code'].head())}")