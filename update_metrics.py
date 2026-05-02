import pandas as pd
import re
import sys

# 1. The Verified CSV Link
csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQhvv6U_CWuFcBQ8GLoYYLF6boAIvNBVmKnpBUM7wO_vtJMa0n8neGutcjzo35-abb9mySHM48bE_PL/pub?gid=1634695898&single=true&output=csv"

try:
    # Read the sheet and force everything to string to avoid math errors
    df = pd.read_csv(csv_url, header=None).astype(str)
    
    # 2. Safe Extraction (Pulling from the core Dashboard area)
    days_to_race = df.iloc[2, 0]   # Cell A3
    shoe_miles = df.iloc[3, 2]     # Cell C4
    
    # We will use your Target Goals for the table since the M column can be finicky in CSV
    swim_split = "1:34:10" 
    bike_split = "8:42:25"
    run_split = "5:01:32"
    total_finish = "15:18:07"

    # 3. Construct the Badge Block
    new_badges = f"""[![Days to Race](https://img.shields.io/badge/Days_to_Ottawa_2027-{days_to_race}-blue)](https://docs.google.com/spreadsheets/d/1lPLLLyabq1FIgv9QlJgcaRqtcBulhBTVE7C0FU1eAIE/edit?usp=sharing)
[![Shoe Miles](https://img.shields.io/badge/Current_Shoe_Miles-{shoe_miles}-orange)](https://docs.google.com/spreadsheets/d/1lPLLLyabq1FIgv9QlJgcaRqtcBulhBTVE7C0FU1eAIE/edit?usp=sharing)
[![Predicted Finish](https://img.shields.io/badge/Predicted_Finish-{total_finish}-green)](https://docs.google.com/spreadsheets/d/1lPLLLyabq1FIgv9QlJgcaRqtcBulhBTVE7C0FU1eAIE/edit?usp=sharing)
"""

    # 4. Construct the Table Block
    new_table = f"""| Discipline | Distance | Target Pace/Power | Predicted Split |
| :--- | :--- | :--- | :--- |
| **Swim** | 3.8 km | 2:10 / 100m | {swim_split} |
| **Bike** | 180 km | 185 Watts | {bike_split} |
| **Run** | 42.2 km | 6:15 / km | {run_split} |
| **Transitions** | — | — | 0:25:00 |
| **Total Project Finish** | **140.6 Miles** | — | **{total_finish}** |
"""

    # 5. Write to README
    with open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()

    # Check if markers exist to avoid silent failure
    if "" not in readme or "" not in readme:
        print("Error: README is missing the markers!")
        sys.exit(1)

    readme = re.sub(r'.*?', new_badges, readme, flags=re.DOTALL)
    readme = re.sub(r'.*?', new_table, readme, flags=re.DOTALL)

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme)
    
    print("Update successful!")

except Exception as e:
    print(f"Update failed with error: {e}")
    sys.exit(1)
