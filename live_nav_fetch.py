import requests
import pandas as pd
import os

# 5 Funds ki list
funds = {
    "119551": "SBI Bluechip",
    "120503": "ICICI Bluechip",
    "118632": "Nippon Large Cap",
    "119092": "Axis Bluechip",
    "120841": "Kotak Bluechip"
}

for code, name in funds.items():
    print(f"\nfetching: {name} (Code: {code})")
    url = f"https://api.mfapi.in/mf/{code}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("Fund name: ", data['meta']['scheme_name'])
        print("Fund House: ", data['meta']['fund_house'])
        print("Category: ", data['meta']['scheme_category'])

        nav_df = pd.DataFrame(data['data'])
        print("Shape     :", nav_df.shape)
        print(nav_df.head(3))
        
        # CSV save karo
        filename = name.lower().replace(" ", "_") + "_nav.csv"
        nav_df.to_csv(f"data/raw/{filename}", index=False)
        print(f"Saved: data/raw/{filename}")
        
    else:
        print(f"Error for {name}: Status {response.status_code}")

print("\nAll 5 funds fetched successfully!")
