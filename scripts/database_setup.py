import sqlite3
import pandas as pd
from sqlalchemy import create_engine
import os

print("=" * 60)
print("TASK 4 & 5 - DATABASE SETUP + DATA LOAD")
print("=" * 60)

# Database path
os.makedirs("data/db", exist_ok=True)
DB_PATH = "data/db/bluestock_mf.db"
engine = create_engine(f"sqlite:///{DB_PATH}")

# Step 1 - Schema create karo
print("\nCreating database schema...")
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

with open("sql/schema.sql", "r") as f:
    schema = f.read()

cursor.executescript(schema)
conn.commit()
print(" Schema created successfully!")

# Step 2 - Data load karo
print("\nLoading data into database...")

# dim_fund
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
fund_master.to_sql("dim_fund", engine,
                   if_exists="replace", index=False)
print(f" dim_fund loaded: {len(fund_master)} rows")

# fact_nav
clean_nav = pd.read_csv("data/processed/clean_nav.csv")
clean_nav.columns = ['amfi_code', 'nav_date', 'nav']
clean_nav.to_sql("fact_nav", engine,
                 if_exists="replace", index=False)
print(f" fact_nav loaded: {len(clean_nav)} rows")

# fact_transactions
clean_txn = pd.read_csv("data/processed/clean_transactions.csv")
clean_txn.to_sql("fact_transactions", engine,
                 if_exists="replace", index=False)
print(f" fact_transactions loaded: {len(clean_txn)} rows")

# fact_performance
clean_perf = pd.read_csv("data/processed/clean_performance.csv")
clean_perf.to_sql("fact_performance", engine,
                  if_exists="replace", index=False)
print(f" fact_performance loaded: {len(clean_perf)} rows")

# fact_aum
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
aum.to_sql("fact_aum", engine,
           if_exists="replace", index=False)
print(f" fact_aum loaded: {len(aum)} rows")

# Step 3 - Verify karo
print("\n" + "=" * 60)
print("VERIFICATION - Tables in Database")
print("=" * 60)

cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

for table in tables:
    table_name = table[0]
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    print(f" {table_name}: {count} rows")

conn.close()
print(f"\n Database saved: {DB_PATH}")