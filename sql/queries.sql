-- =====================
-- BLUESTOCK MF - 10 SQL QUERIES
-- =====================

-- Query 1: Top 5 funds by AUM
SELECT fund_house, scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Query 2: Average NAV per month
SELECT
    amfi_code,
    strftime('%Y-%m', nav_date) AS month,
    ROUND(AVG(nav), 2) AS avg_nav
FROM fact_nav
GROUP BY amfi_code, month
ORDER BY amfi_code, month;

-- Query 3: SIP inflow YoY growth
SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM fact_sip_industry
ORDER BY month;

-- Query 4: Transactions by state
SELECT
    state,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr) / 1000000.0, 2) AS total_amount_millions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- Query 5: Funds with expense ratio < 1%
SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct,
    category
FROM dim_fund
WHERE expense_ratio_pct < 1.0
ORDER BY expense_ratio_pct ASC;

-- Query 6: Top 5 funds by Sharpe Ratio
SELECT
    scheme_name,
    fund_house,
    sharpe_ratio,
    return_3yr_pct
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- Query 7: SIP vs Lumpsum vs Redemption count
SELECT
    transaction_type,
    COUNT(*) AS total_count,
    ROUND(SUM(amount_inr) / 10000000.0, 2) AS total_crore
FROM fact_transactions
GROUP BY transaction_type;

-- Query 8: Fund count per category
SELECT
    category,
    sub_category,
    COUNT(*) AS num_funds,
    ROUND(AVG(expense_ratio_pct), 2) AS avg_expense_ratio
FROM dim_fund
GROUP BY category, sub_category
ORDER BY category, num_funds DESC;

-- Query 9: Top 5 funds by 3 year return
SELECT
    scheme_name,
    fund_house,
    return_3yr_pct,
    alpha,
    sharpe_ratio
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 5;

-- Query 10: Investors by age group and gender
SELECT
    age_group,
    gender,
    COUNT(DISTINCT investor_id) AS investors,
    ROUND(AVG(amount_inr), 0) AS avg_investment
FROM fact_transactions
GROUP BY age_group, gender
ORDER BY age_group, gender;