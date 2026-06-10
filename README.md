# Bluestock Fintech — Mutual Fund Analytics Platform

## Project Overview
A full-stack Mutual Fund Analytics Platform built using 
publicly available Indian mutual fund data from AMFI India 
and mfapi.in. The platform ingests raw NAV, AUM, and SIP 
data, cleans and loads it into a relational database, 
performs exploratory and performance analytics, and 
presents insights via an interactive Power BI dashboard.

## Tech Stack
- Python 3.14, Pandas, NumPy, Matplotlib, Seaborn, Plotly
- SQLite3, SQLAlchemy
- SciPy, Jupyter Lab
- Power BI Desktop
- Git + GitHub

## Project Structure
bluestock-analytics/
├── data/
│   ├── raw/          # Original CSV files
│   ├── processed/    # Cleaned CSVs
│   └── db/           # SQLite database
├── notebooks/        # Jupyter analysis notebooks
├── scripts/          # Python ETL scripts
├── sql/              # SQL schema and queries
├── charts/           # Generated charts
├── dashboard/        # Power BI dashboard
├── reports/          # Final report and presentation
└── docs/             # Data dictionary

## Datasets
| File | Rows | Description |
|---|---|---|
| 01_fund_master.csv | 40 | Fund details |
| 02_nav_history.csv | 46,000 | Daily NAV |
| 03_aum_by_fund_house.csv | 90 | AUM data |
| 04_monthly_sip_inflows.csv | 48 | SIP inflows |
| 05_category_inflows.csv | 144 | Category flows |
| 06_industry_folio_count.csv | 21 | Folio count |
| 07_scheme_performance.csv | 40 | Performance |
| 08_investor_transactions.csv | 32,778 | Transactions |
| 09_portfolio_holdings.csv | 322 | Holdings |
| 10_benchmark_indices.csv | 8,050 | Benchmarks |

## How to Run

### 1. Setup Environment
```bash
git clone https://github.com/NityaSharma27/bluestock-analytics
cd bluestock-analytics
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run ETL Pipeline
```bash
python scripts/data_cleaning.py
python scripts/database_setup.py
```

### 3. Run SQL Queries
```bash
python scripts/run_queries.py
```

### 4. Open Jupyter Notebooks
```bash
python -m jupyter notebook
```
Open notebooks in this order:
- notebooks/EDA_Analysis.ipynb
- notebooks/Performance_Analytics.ipynb  
- notebooks/Advanced_Analytics.ipynb

### 5. Open Dashboard
Open `dashboard/bluestock_mf_dashboard.pbix` 
in Power BI Desktop

### 6. Fund Recommender
```bash
python scripts/recommender.py
```

## Key Findings
1. SBI Mutual Fund dominates with ₹12.5L Cr AUM
2. SIP inflows grew 2.8x — ₹11,000 Cr to ₹31,002 Cr
3. Small Cap funds gave highest 3yr CAGR (~23%)
4. Industry folios doubled — 13.26 Cr to 26.12 Cr
5. 26-35 age group dominates investor base (43%)

## Deliverables
- ✅ ETL Pipeline Scripts
- ✅ SQLite Database (97,268 rows)
- ✅ EDA Notebook (15+ charts)
- ✅ Performance Analytics Notebook
- ✅ Advanced Analytics Notebook
- ✅ Power BI Dashboard (4 pages)
- ✅ Final Report PDF
- ✅ 12-slide Presentation

## Author
**Nitya Sharma**  
Data Analytics Intern — Bluestock Fintech  
June 2026

## Data Sources
- AMFI India: www.amfiindia.com
- mfapi.in: api.mfapi.in
- NSE India: nseindia.com