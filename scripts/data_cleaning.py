import pandas as pd
import numpy as np
import os

# Output folder
os.makedirs("data/processed", exist_ok=True)

print("=" * 60)
print("TASK 1 - CLEANING NAV HISTORY")
print("=" * 60)

# Load karo
nav = pd.read_csv("data/raw/02_nav_history.csv")

print(f"\nBefore Cleaning:")
print(f"Shape : {nav.shape}")
print(f"Dtypes:\n{nav.dtypes}")

# Step 1 - Date ko datetime mein convert karo
nav['date'] = pd.to_datetime(nav['date'])
print(f"\n Dates converted to datetime")

# Step 2 - Sort karo amfi_code + date se
nav = nav.sort_values(['amfi_code', 'date']).reset_index(drop=True)
print(f" Sorted by amfi_code and date")

# Step 3 - Duplicates remove karo
before = len(nav)
nav = nav.drop_duplicates(subset=['amfi_code', 'date'])
after = len(nav)
print(f" Duplicates removed: {before - after} rows dropped")

# Step 4 - NAV > 0 validate karo
invalid_nav = nav[nav['nav'] <= 0]
print(f"Invalid NAV rows (<=0): {len(invalid_nav)}")
nav = nav[nav['nav'] > 0]

# Step 5 - Forward fill missing NAV (weekends/holidays)
# Step 5 - Forward fill missing NAV (weekends/holidays)
filled_dfs = []
for code, group in nav.groupby('amfi_code'):
    group = group.set_index('date')[['nav']]
    full_range = pd.date_range(group.index.min(), group.index.max(), freq='D')
    group = group.reindex(full_range)
    group['nav'] = group['nav'].ffill()
    group['amfi_code'] = int(code)
    group.index.name = 'date'
    group = group.reset_index()
    filled_dfs.append(group)

nav = pd.concat(filled_dfs, ignore_index=True)
nav = nav[['amfi_code', 'date', 'nav']]
nav['nav'] = nav['nav'].astype(float)
print(f" Forward fill applied for weekends/holidays")

print(f"\nAfter Cleaning:")
print(f"Shape : {nav.shape}")
print(f"Dtypes:\n{nav.dtypes}")
print(f"\nFirst 5 Rows:")
print(nav.head())

# Save karo
nav.to_csv("data/processed/clean_nav.csv", index=False)
print(f"\nSaved: data/processed/clean_nav.csv")

print("\n" + "=" * 60)
print("TASK 2 - CLEANING INVESTOR TRANSACTIONS")
print("=" * 60)

txn = pd.read_csv("data/raw/08_investor_transactions.csv")

print(f"\nBefore Cleaning:")
print(f"Shape : {txn.shape}")

# Step 1 - Date fix karo
txn['transaction_date'] = pd.to_datetime(txn['transaction_date'])
print(f" Dates converted to datetime")

# Step 2 - Transaction type standardize karo
txn['transaction_type'] = txn['transaction_type'].str.strip().str.upper()
print(f" Transaction types standardized")
print(f"   Unique types: {txn['transaction_type'].unique()}")

# Step 3 - Amount > 0 validate karo
before = len(txn)
txn = txn[txn['amount_inr'] > 0]
after = len(txn)
print(f" Invalid amounts removed: {before - after} rows dropped")

# Step 4 - KYC status check karo
print(f" KYC Status values: {txn['kyc_status'].unique()}")
txn = txn[txn['kyc_status'].isin(['Verified', 'Pending'])]
print(f" KYC Status cleaned")

# Step 5 - Duplicates remove karo
before = len(txn)
txn = txn.drop_duplicates()
after = len(txn)
print(f" Duplicates removed: {before - after} rows dropped")

print(f"\nAfter Cleaning:")
print(f"Shape : {txn.shape}")
print(f"\nFirst 5 Rows:")
print(txn.head())

# Save karo
txn.to_csv("data/processed/clean_transactions.csv", index=False)
print(f"\n Saved: data/processed/clean_transactions.csv")


print("\n" + "=" * 60)
print("TASK 3 - CLEANING SCHEME PERFORMANCE")
print("=" * 60)

perf = pd.read_csv("data/raw/07_scheme_performance.csv")

print(f"\nBefore Cleaning:")
print(f"Shape : {perf.shape}")

# Step 1 - Numeric columns validate karo
numeric_cols = ['return_1yr_pct', 'return_3yr_pct', 'return_5yr_pct',
                'sharpe_ratio', 'alpha', 'beta', 'std_dev_ann_pct',
                'max_drawdown_pct']

for col in numeric_cols:
    perf[col] = pd.to_numeric(perf[col], errors='coerce')

print(f" Numeric columns validated")

# Step 2 - Negative Sharpe ratio flag karo
negative_sharpe = perf[perf['sharpe_ratio'] < 0]
print(f" Funds with negative Sharpe ratio: {len(negative_sharpe)}")
if len(negative_sharpe) > 0:
    print(f"   Funds: {list(negative_sharpe['scheme_name'])}")

# Step 3 - Expense ratio range check karo (0.1% to 2.5%)
invalid_expense = perf[
    (perf['expense_ratio_pct'] < 0.1) |
    (perf['expense_ratio_pct'] > 2.5)
]
print(f" Funds with invalid expense ratio: {len(invalid_expense)}")
if len(invalid_expense) > 0:
    print(f"   Funds: {list(invalid_expense['scheme_name'])}")

# Step 4 - Missing values check
missing = perf.isnull().sum()
missing_cols = missing[missing > 0]
if not missing_cols.empty:
    print(f"⚠️  Missing values found:\n{missing_cols}")
else:
    print(f" No missing values found")

# Step 5 - Duplicates remove karo
before = len(perf)
perf = perf.drop_duplicates()
after = len(perf)
print(f" Duplicates removed: {before - after} rows dropped")

print(f"\nAfter Cleaning:")
print(f"Shape : {perf.shape}")
print(f"\nSharpe Ratio Summary:")
print(perf['sharpe_ratio'].describe())
print(f"\nExpense Ratio Summary:")
print(perf['expense_ratio_pct'].describe())
print(f"\nFirst 5 Rows:")
print(perf[['scheme_name', 'return_1yr_pct',
            'sharpe_ratio', 'expense_ratio_pct']].head())

# Save karo
perf.to_csv("data/processed/clean_performance.csv", index=False)
print(f"\n Saved: data/processed/clean_performance.csv")