import pandas as pd
import re
import sys

csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQhvv6U_CWuFcBQ8GLoYYLF6boAIvNBVmKnpBUM7wO_vtJMa0n8neGutcjzo35-abb9mySHM48bE_PL/pub?gid=1634695898&single=true&output=csv"

try:
    df = pd.read_csv(csv_url, header=None).fillna("0")
    
    # Safe data extraction
    days_to_race = df.iloc[2, 0] if len(df) > 2 else "TBD"
    shoe_miles = df.iloc[3, 2] if len(df) > 3 else "0"
    
    # Static fallbacks for the table if specific cells fail
    swim_split, bike_split, run_split, total_finish = "1:34:10", "8:42:25", "5:01:32", "15:18:07"

    new_badges = f"""[![Days to Race](https://img.shields.io/badge/Days_to_Ottawa_2027-{days_to_race}-blue)](https://docs.google.com/spreadsheets/d/1lPLLLyabq1FIgv9QlJgcaRqtcBulhBTVE7C0FU1eAIE/edit?usp=sharing)
[![Shoe Miles](https://img.shields.io/badge/Current_Shoe_Miles-{shoe_miles}-orange)](https://docs.google.com/spreadsheets/d/1lPLLLyabq1FIgv9QlJgcaRqtcBulhBTVE7C0FU1eAIE/edit?usp=sharing)
[![Predicted Finish](https://img.shields.io/badge/Predicted_Finish-{total_finish}-green)](https://docs.google.com/spreadsheets/d/1lPLLLyabq1FIgv9QlJgcaRqtcBulhBTVE7C0FU1eAIE/edit?usp=sharing)
"""

    new_table = f"""| Discipline | Distance | Target Pace/Power | Predicted Split |
| :--- | :--- | :--- | :--- |
| **Swim** | 3.8 km | 2:10 / 100m | {swim_split} |
| **Bike** | 180 km | 185 Watts | {bike_split} |
| **Run** | 42.2 km | 6:15 / km | {run_split} |
| **Total Project Finish** | **140.6 Miles** | — | **{total_finish}** |
"""

    with open('README.md', 'r') as f:
        content = f.read()

    if "" in content:
        content = re.sub(r'.*?', new_badges, content, flags=re.DOTALL)
        content = re.sub(r'.*?', new_table, content, flags=re.DOTALL)
        
        with open('README.md', 'w') as f:
            f.write(content)
        print("Successfully updated README.")
    else:
        print("Markers not found in README.md")
        sys.exit(1)

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
