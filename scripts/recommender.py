
import pandas as pd

def recommend_funds(risk_appetite, top_n=3):
    """
    Mutual Fund Recommender
    Input : risk_appetite = Low / Moderate / High
    Output: Top N funds by Sharpe ratio
    """
    perf_df = pd.read_csv("data/processed/clean_performance.csv")

    risk_map = {
        "Low"     : ["Low"],
        "Moderate": ["Moderate", "Moderately High"],
        "High"    : ["High", "Very High"]
    }

    valid_grades = risk_map.get(risk_appetite, ["Moderate"])
    filtered = perf_df[perf_df["risk_grade"].isin(valid_grades)]

    top_funds = filtered.nlargest(top_n, "sharpe_ratio")[
        ["scheme_name", "fund_house", "risk_grade",
         "sharpe_ratio", "return_3yr_pct", "expense_ratio_pct"]
    ].reset_index(drop=True)

    top_funds.index += 1
    return top_funds

if __name__ == "__main__":
    print("Bluestock MF Fund Recommender")
    print("=" * 40)
    risk = input("Enter risk appetite (Low/Moderate/High): ")
    result = recommend_funds(risk)
    if result is not None:
        print(f"\nTop 3 Recommended Funds for {risk} Risk:")
        print(result.to_string())
