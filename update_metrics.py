import pandas as pd
import re
import sys

# Your validated CSV link
csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQhvv6U_CWuFcBQ8GLoYYLF6boAIvNBVmKnpBUM7wO_vtJMa0n8neGutcjzo35-abb9mySHM48bE_PL/pub?gid=1634695898&single=true&output=csv"

try:
    # Read the data and clean it
    df = pd.read_csv(csv_url, header=None).fillna("0").astype(str)
    
    # Extraction (Indices based on your Carlos Dashboard sheet)
    days_to_race = df.iloc[2, 0]   # Cell A3
    shoe_miles = df.iloc[3, 2]     # Cell C4
    total_finish = df.iloc[10, 3]  # Cell D11
    
    swim_split = df.iloc[7, 3]     # D8
    bike_split = df.iloc[8, 3]     # D9
    run_split = df.iloc[9, 3]      # D10

    # 1. Create the Badge HTML
    new_badges = f"""[![Days to Race](https://img.shields.io/badge/Days_to_Ottawa_2027-{days_to_race}-blue)](https://docs.google.com/spreadsheets/d/1lPLLLyabq1FIgv9QlJgcaRqtcBulhBTVE7C0FU1eAIE/edit?usp=sharing)
[![Shoe Miles](https://img.shields.io/badge/Current_Shoe_Miles-{shoe_miles}-orange)](https://docs.google.com/spreadsheets/d/1lPLLLyabq1FIgv9QlJgcaRqtcBulhBTVE7C0FU1eAIE/edit?usp=sharing)
[![Predicted Finish](https://img.shields.io/badge/Predicted_Finish-{total_finish}-green)](https://docs.google.com/spreadsheets/d/1lPLLLyabq1FIgv9QlJgcaRqtcBulhBTVE7C0FU1eAIE/edit?usp=sharing)
"""

    # 2. Create the Table HTML
    new_table = f"""| Discipline | Distance | Target Pace/Power | Predicted Split |
| :--- | :--- | :--- | :--- |
| **Swim** | 3.8 km | 2:10 / 100m | {swim_split} |
| **Bike** | 180 km | 185 Watts | {bike_split} |
| **Run** | 42.2 km | 6:15 / km | {run_split} |
| **Total Finish** | **140.6 mi** | — | **{total_finish}** |
"""

    # 3. Apply to README
    with open('README.md', 'r') as f:
        readme = f.read()

    if "" not in readme:
        print("❌ CRITICAL ERROR: Could not find markers in README.md. Please copy Step 1 above.")
        sys.exit(1)

    readme = re.sub(r'.*?', new_badges, readme, flags=re.DOTALL)
    readme = re.sub(r'.*?', new_table, readme, flags=re.DOTALL)

    with open('README.md', 'w') as f:
        f.write(readme)
    
    print("✅ Success! README updated.")

except Exception as e:
    print(f"❌ Automation Failed: {e}")
    sys.exit(1)
