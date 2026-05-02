import pandas as pd
import re

# Download as CSV (Specific GID for Carlos Dashboard)
csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQhvv6U_CWuFcBQ8GLoYYLF6boAIvNBVmKnpBUM7wO_vtJMa0n8neGutcjzo35-abb9mySHM48bE_PL/pub?gid=1634695898&single=true&output=csv"
df = pd.read_csv(csv_url, header=None)

# Extracting from confirmed cells
days_to_race = df.iloc[2, 0]   # Cell A3
shoe_miles = df.iloc[3, 2]     # Cell C4
phase = "Base Build"           # Manual tag for now

# Create the updated badges
new_badges = f"""[![Days to Race](https://img.shields.io/badge/Days_to_Ottawa_2027-{days_to_race}-blue)](https://docs.google.com/spreadsheets/d/1lPLLLyabq1FIgv9QlJgcaRqtcBulhBTVE7C0FU1eAIE/edit?usp=sharing)
[![Shoe Miles](https://img.shields.io/badge/Current_Shoe_Miles-{shoe_miles}-orange)](https://docs.google.com/spreadsheets/d/1lPLLLyabq1FIgv9QlJgcaRqtcBulhBTVE7C0FU1eAIE/edit?usp=sharing)
[![Training Phase](https://img.shields.io/badge/Phase-{phase}-green)](https://docs.google.com/spreadsheets/d/1lPLLLyabq1FIgv9QlJgcaRqtcBulhBTVE7C0FU1eAIE/edit?usp=sharing)
"""

# Update README
with open('README.md', 'r', encoding='utf-8') as file:
    readme_content = file.read()

updated_readme = re.sub(r'.*?', new_badges, readme_content, flags=re.DOTALL)

with open('README.md', 'w', encoding='utf-8') as file:
    file.write(updated_readme)
