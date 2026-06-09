# Data Dictionary — Bluestock MF Analytics Platform

## 01_fund_master.csv / dim_fund

| Column | Type | Description | Example |
|---|---|---|---|
| amfi_code | INTEGER | AMFI unique scheme code | 119551 |
| fund_house | TEXT | AMC name | SBI Mutual Fund |
| scheme_name | TEXT | Full fund name | SBI Bluechip Fund |
| category | TEXT | Equity / Debt | Equity |
| sub_category | TEXT | Large Cap / Mid Cap etc | Large Cap |
| plan | TEXT | Regular or Direct | Direct |
| launch_date | TEXT | Fund launch date | 2013-01-01 |
| benchmark | TEXT | Official benchmark index | Nifty 100 |
| expense_ratio_pct | REAL | Annual expense % | 0.66 |
| exit_load_pct | REAL | Exit load % | 1.0 |
| min_sip_amount | INTEGER | Minimum SIP amount | 500 |
| min_lumpsum_amount | INTEGER | Minimum lumpsum | 5000 |
| fund_manager | TEXT | Fund manager name | Dinesh Balachandran |
| risk_category | TEXT | SEBI risk grade | Moderate |
| sebi_category_code | TEXT | Internal SEBI code | EC01 |

---

## 02_nav_history.csv / fact_nav

| Column | Type | Description | Example |
|---|---|---|---|
| amfi_code | INTEGER | FK to dim_fund | 119551 |
| date | DATE | NAV date | 2022-01-03 |
| nav | REAL | NAV in Rs | 54.3856 |

---

## 07_scheme_performance.csv / fact_performance

| Column | Type | Description | Example |
|---|---|---|---|
| amfi_code | INTEGER | FK to dim_fund | 119551 |
| return_1yr_pct | REAL | 1 year return % | 18.5 |
| return_3yr_pct | REAL | 3 year CAGR % | 23.39 |
| return_5yr_pct | REAL | 5 year CAGR % | 19.2 |
| benchmark_3yr_pct | REAL | Benchmark 3yr CAGR | 15.2 |
| alpha | REAL | Excess return over benchmark | 1.23 |
| beta | REAL | Market sensitivity | 0.95 |
| sharpe_ratio | REAL | Risk adjusted return | 0.94 |
| sortino_ratio | REAL | Downside risk adjusted return | 1.12 |
| std_dev_ann_pct | REAL | Annualised std deviation % | 18.5 |
| max_drawdown_pct | REAL | Worst peak to trough decline | -28.4 |
| morningstar_rating | INTEGER | 1-5 star rating | 4 |
| risk_grade | TEXT | Low/Moderate/High/Very High | Moderate |

---

## 08_investor_transactions.csv / fact_transactions

| Column | Type | Description | Example |
|---|---|---|---|
| investor_id | TEXT | Unique investor ID | INV003054 |
| transaction_date | DATE | Transaction date | 2024-01-01 |
| amfi_code | INTEGER | FK to dim_fund | 119092 |
| transaction_type | TEXT | SIP/LUMPSUM/REDEMPTION | SIP |
| amount_inr | INTEGER | Amount in rupees | 5000 |
| state | TEXT | Investor state | Maharashtra |
| city | TEXT | Investor city | Mumbai |
| city_tier | TEXT | T30 or B30 | T30 |
| age_group | TEXT | Age band | 26-35 |
| gender | TEXT | Male/Female | Male |
| annual_income_lakh | REAL | Annual income in lakh | 12.5 |
| payment_mode | TEXT | UPI/Cheque/Mandate | UPI |
| kyc_status | TEXT | Verified/Pending | Verified |

---

## 03_aum_by_fund_house.csv / fact_aum

| Column | Type | Description | Example |
|---|---|---|---|
| date | TEXT | Quarter end date | 2022-03-31 |
| fund_house | TEXT | AMC name | SBI Mutual Fund |
| aum_lakh_crore | REAL | AUM in lakh crore | 6.05 |
| aum_crore | INTEGER | AUM in crore | 605000 |
| num_schemes | INTEGER | Number of schemes | 186 |

---

## Data Quality Notes

| File | Status | Notes |
|---|---|---|
| 01_fund_master |  Clean | No issues |
| 02_nav_history |  Clean | Forward filled for weekends |
| 03_aum_by_fund_house |  Clean | No issues |
| 04_monthly_sip_inflows |  Minor | 12 NaN in yoy_growth_pct — expected |
| 05_category_inflows |  Clean | No issues |
| 06_industry_folio_count |  Clean | No issues |
| 07_scheme_performance |  Clean | No issues |
| 08_investor_transactions |  Clean | No issues |
| 09_portfolio_holdings |  Clean | No issues |
| 10_benchmark_indices |  Clean | No issues |