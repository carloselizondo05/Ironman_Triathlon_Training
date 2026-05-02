import pandas as pd
import re

# 1. Download your published Google Sheet as a CSV
# Note: I changed your URL from 'pubhtml' to 'pub?output=csv'
csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQhvv6U_CWuFcBQ8GLoYYLF6boAIvNBVmKnpBUM7wO_vtJMa0n8neGutcjzo35-abb9mySHM48bE_PL/pub?gid=1634695898&single=true&output=csv"
df = pd.read_csv(csv_url, header=None)

# 2. Extract your metrics (We will need to adjust the exact row/column numbers)
# df.iloc[row_index, column_index]
days_to_race = df.iloc[1, 1]  # Example: grabs cell B2
total_miles = df.iloc[2, 1]   # Example: grabs cell B3
phase = "Base_Building"       # We can automate this too!

# 3. Create the updated badges block
new_badges = f"""[![Days to Race](https://img.shields.io/badge/Days_to_Ottawa_2027-{days_to_race}-blue)](https://docs.google.com/spreadsheets/d/1lPLLLyabq1FIgv9QlJgcaRqtcBulhBTVE7C0FU1eAIE/edit?usp=sharing)
[![Current Miles](https://img.shields.io/badge/Total_Run_Miles-{total_miles}-orange)](https://docs.google.com/spreadsheets/d/1lPLLLyabq1FIgv9QlJgcaRqtcBulhBTVE7C0FU1eAIE/edit?usp=sharing)
[![Training Phase](https://img.shields.io/badge/Phase-{phase}-green)](https://docs.google.com/spreadsheets/d/1lPLLLyabq1FIgv9QlJgcaRqtcBulhBTVE7C0FU1eAIE/edit?usp=sharing)
"""

# 4. Read the current README, replace the old block, and save
with open('README.md', 'r', encoding='utf-8') as file:
    readme_content = file.read()

updated_readme = re.sub(
    r'.*?', 
    new_badges, 
    readme_content, 
    flags=re.DOTALL
)

with open('README.md', 'w', encoding='utf-8') as file:
    file.write(updated_readme)

print("Successfully updated README metrics!")
