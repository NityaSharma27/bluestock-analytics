import sqlite3
import pandas as pd

DB_PATH = "data/db/bluestock_mf.db"
conn = sqlite3.connect(DB_PATH)

queries = {
    "Q1 - Top 5 Funds by AUM": """
        SELECT fund_house, scheme_name, aum_crore
        FROM fact_performance
        ORDER BY aum_crore DESC LIMIT 5""",

    "Q2 - Avg NAV Per Month (Sample)": """
        SELECT amfi_code,
        strftime('%Y-%m', nav_date) AS month,
        ROUND(AVG(nav), 2) AS avg_nav
        FROM fact_nav
        GROUP BY amfi_code, month
        ORDER BY amfi_code, month LIMIT 5""",

    "Q3 - Transactions by State": """
        SELECT state, COUNT(*) AS total_transactions,
        ROUND(SUM(amount_inr)/1000000.0, 2) AS total_amount_millions
        FROM fact_transactions
        GROUP BY state
        ORDER BY total_transactions DESC""",

    "Q4 - Funds with Expense Ratio < 1%": """
        SELECT scheme_name, fund_house, expense_ratio_pct
        FROM dim_fund
        WHERE expense_ratio_pct < 1.0
        ORDER BY expense_ratio_pct ASC""",

    "Q5 - Top 5 by Sharpe Ratio": """
        SELECT scheme_name, fund_house, sharpe_ratio, return_3yr_pct
        FROM fact_performance
        ORDER BY sharpe_ratio DESC LIMIT 5""",

    "Q6 - SIP vs Lumpsum vs Redemption": """
        SELECT transaction_type, COUNT(*) AS total_count,
        ROUND(SUM(amount_inr)/10000000.0, 2) AS total_crore
        FROM fact_transactions
        GROUP BY transaction_type""",

    "Q7 - Fund Count per Category": """
        SELECT category, sub_category, COUNT(*) AS num_funds,
        ROUND(AVG(expense_ratio_pct), 2) AS avg_expense_ratio
        FROM dim_fund
        GROUP BY category, sub_category
        ORDER BY category, num_funds DESC""",

    "Q8 - Top 5 by 3yr Return": """
        SELECT scheme_name, fund_house, return_3yr_pct, alpha, sharpe_ratio
        FROM fact_performance
        ORDER BY return_3yr_pct DESC LIMIT 5""",

    "Q9 - Investors by Age and Gender": """
        SELECT age_group, gender,
        COUNT(DISTINCT investor_id) AS investors,
        ROUND(AVG(amount_inr), 0) AS avg_investment
        FROM fact_transactions
        GROUP BY age_group, gender
        ORDER BY age_group, gender""",

    "Q10 - AUM by Fund House": """
        SELECT fund_house,
        ROUND(AVG(aum_crore), 0) AS avg_aum_crore
        FROM fact_aum
        GROUP BY fund_house
        ORDER BY avg_aum_crore DESC"""
}

print("=" * 60)
print("10 SQL QUERIES - RESULTS")
print("=" * 60)

for name, query in queries.items():
    print(f"\n{name}")
    print("-" * 40)
    df = pd.read_sql_query(query, conn)
    print(df.to_string(index=False))

conn.close()
print("\n All queries executed successfully!")