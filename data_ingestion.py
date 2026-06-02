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





# =====================
# TASK 7 - AMFI Code Validation
# =====================

print("\n" + "=" * 60)
print("TASK 7 - AMFI CODE VALIDATION")
print("=" * 60)

nav = pd.read_csv("data/raw/02_nav_history.csv")

# Dono files se codes nikalo
fm_codes = set(fm['amfi_code'].unique())
nav_codes = set(nav['amfi_code'].unique())

# Comparison
matched = fm_codes & nav_codes
missing_in_nav = fm_codes - nav_codes
extra_in_nav = nav_codes - fm_codes

print(f"\nTotal codes in fund_master  : {len(fm_codes)}")
print(f"Total codes in nav_history  : {len(nav_codes)}")
print(f"Codes matched               : {len(matched)}")
print(f"Codes missing in nav        : {len(missing_in_nav)}")
print(f"Extra codes in nav          : {len(extra_in_nav)}")

if missing_in_nav:
    print(f"\n⚠️  Missing Codes: {missing_in_nav}")
else:
    print("\n✅ All fund_master codes exist in nav_history!")

if extra_in_nav:
    print(f"\n⚠️  Extra codes in nav not in fund_master: {extra_in_nav}")
else:
    print("✅ No extra codes in nav_history!")

# Data Quality Summary
print("\n" + "=" * 60)
print("DATA QUALITY SUMMARY")
print("=" * 60)
print("1. 9/10 files are completely clean with no missing values")
print("2. 04_monthly_sip_inflows.csv has 12 missing values in")
print("   yoy_growth_pct — expected, first 12 months have no")
print("   previous year data to compare")
print(f"3. AMFI code match: {len(matched)}/{len(fm_codes)} codes verified")
print("4. date columns are stored as string — needs conversion")
print("   in processing stage")