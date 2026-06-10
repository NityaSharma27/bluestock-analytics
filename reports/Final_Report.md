# Bluestock Fintech — Mutual Fund Analytics Platform
## Final Project Report

**Intern:** Nitya Sharma  
**Company:** Bluestock Fintech Pvt. Ltd.  
**Submission:** PDF Report + Dashboard + GitHub Repository

---

## 1. Executive Summary

This capstone project builds a full-stack Mutual Fund 
Analytics Platform using publicly available Indian mutual 
fund data. The platform ingests data from AMFI India and 
mfapi.in, cleans and stores it in a SQLite database, 
performs comprehensive analytics, and presents insights 
via an interactive Power BI dashboard.

**Key Achievements:**
- Ingested and cleaned 97,268 rows across 10 datasets
- Built 5-table SQLite star schema database
- Created 17+ analytical charts
- Computed Sharpe, Sortino, Alpha, Beta, VaR for 40 funds
- Built 4-page interactive Power BI dashboard
- Developed fund recommendation system

---

## 2. Problem Statement

Indian mutual fund data is fragmented across multiple 
sources. Investors lack unified analytics platforms for 
data-driven fund selection. This project solves:

- **P1:** Data fragmentation — unified ETL pipeline
- **P2:** Performance comparison — risk-adjusted metrics
- **P3:** No benchmark tracking — NAV vs Nifty comparison
- **P4:** Investor behaviour blind spot — demographic analysis
- **P5:** Slow reporting — live self-service dashboard

---

## 3. Data Sources & Datasets

| File | Rows | Description |
|---|---|---|
| 01_fund_master | 40 | 40 AMFI schemes |
| 02_nav_history | 46,000 | Daily NAV 2022-2026 |
| 03_aum_by_fund_house | 90 | Quarterly AUM |
| 04_monthly_sip_inflows | 48 | SIP inflow data |
| 05_category_inflows | 144 | Category net flows |
| 06_industry_folio_count | 21 | Industry folios |
| 07_scheme_performance | 40 | Risk-return metrics |
| 08_investor_transactions | 32,778 | Investor transactions |
| 09_portfolio_holdings | 322 | Stock holdings |
| 10_benchmark_indices | 8,050 | Index prices |

---

## 4. System Architecture & ETL Pipeline

**Layer 1 — Extract:** mfapi.in API + Local CSVs  
**Layer 2 — Transform:** Pandas cleaning, type casting,
forward-fill missing NAVs  
**Layer 3 — Load:** SQLite via SQLAlchemy ORM  
**Layer 4 — Analyse:** Jupyter notebooks  
**Layer 5 — Visualise:** Power BI dashboard  

### Database Schema (Star Schema)
- dim_fund (40 rows)
- fact_nav (64,320 rows)
- fact_transactions (32,778 rows)
- fact_performance (40 rows)
- fact_aum (90 rows)

---

## 5. EDA Key Findings

1. SBI Mutual Fund dominates with ₹12.5L Cr AUM
2. SIP inflows grew 2.8x — ₹11,000 Cr to ₹31,002 Cr
3. Small Cap funds showed highest NAV growth 2022-2026
4. Industry folios doubled — 13.26 Cr to 26.12 Cr
5. 26-35 age group dominates investor base (43%)
6. Punjab leads state-wise transactions
7. T30 cities contribute 56% of transactions
8. Large Cap funds highly correlated (>0.85)
9. Banking sector largest portfolio weight
10. ELSS inflows peak in Jan-Mar (tax season)

---

## 6. Performance Analytics Results

| Metric | Best Fund | Value |
|---|---|---|
| 3yr CAGR | SBI Small Cap | 23.39% |
| Sharpe Ratio | ICICI Pru Liquid | 7.68 |
| Alpha | SBI Small Cap | 30.34% |
| Lowest VaR | Liquid Funds | ~0.01% |
| Highest VaR | Small Cap | ~-2.5% |

---

## 7. Advanced Analytics Insights

1. Small Cap funds have highest VaR — most risky
2. Liquid funds safest — VaR near zero
3. 2024 cohort investors have higher avg SIP than 2025
4. ~30% active SIP investors are at-risk (gap > 35 days)
5. Several funds show high HHI — concentrated in Banking

---

## 8. Dashboard Overview

**Page 1 — Industry Overview:**
KPI cards for AUM, SIP, Folios + growth charts

**Page 2 — Fund Performance:**
Risk-return scatter, scorecard table, NAV trends

**Page 3 — Investor Analytics:**
State distribution, demographics, transaction patterns

**Page 4 — SIP & Market Trends:**
SIP growth, category inflows, market correlation

---

## 9. Recommendations

1. **Investors:** SBI Small Cap for high-risk, long-term
2. **Low-risk investors:** ICICI Pru Liquid for stability
3. **Tax saving:** ELSS funds before March deadline
4. **AMCs:** Focus on B30 cities — growing 2.5x faster
5. **Data:** Fix AMFI code mismatches in API

---

## 10. Limitations

1. API scheme codes mismatch with task sheet
2. Beta values low due to date alignment issues
3. Investor transaction data is simulated
4. Dashboard requires Power BI Desktop to view
5. NAV forward-fill adds synthetic weekend data

---

## 11. Conclusion

This project successfully built an end-to-end Mutual Fund 
Analytics Platform mirroring real fintech workflows used 
at Zerodha, Groww, and Paytm Money. All 8 objectives were 
met within 7 working days.

---

**Prepared by:** Nitya Sharma  
**Date:** June 2026  
**GitHub:** github.com/NityaSharma27/bluestock-analytics