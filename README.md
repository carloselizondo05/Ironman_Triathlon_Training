# 🏊‍♂️ Ironman Canada (Ottawa) 2027: Predictive Performance Dashboard
**Target Race:** August 2027 (Ottawa, ON)

### 📊 Training Status (Live)
---

### ⏱️ Race-Day Projections (Dynamic)
---

### 📋 Project Overview
This repository contains the data architecture and predictive modeling used to manage my journey toward completing the **Ironman Canada 140.6**. 

**[Link to Google Sheets Training Dashboard](https://docs.google.com/spreadsheets/d/1lPLLLyabq1FIgv9QlJgcaRqtcBulhBTVE7C0FU1eAIE/edit?usp=sharing)**


---

# Ironman Triathlon Training 2027

## 🏊‍♂️ Ironman Canada (Ottawa) 2027: Predictive Performance Dashboard
**Project Status:** Active Training & Data Collection  
**Target Race:** August 2027 (Ottawa, ON)

### 📋 Project Overview
This repository contains the data architecture and predictive modeling used to manage my 18-month journey toward completing the **Ironman Canada 140.6** in Ottawa. Rather than relying on generic fitness apps, I built this custom dashboard to integrate volume tracking with performance forecasting, specifically tailored to the Ottawa course profile (river swim, closed parkway bike, and Parliament Hill finish).

**[[Link to Google Sheets Training Dashboard](https://docs.google.com/spreadsheets/d/1lPLLLyabq1FIgv9QlJgcaRqtcBulhBTVE7C0FU1eAIE/edit?usp=sharing)]**

[![Days to Race](https://img.shields.io/badge/Days_to_Ottawa_2027-456-blue)](https://docs.google.com/spreadsheets/d/e/2PACX-1vQhvv6U_CWuFcBQ8GLoYYLF6boAIvNBVmKnpBUM7wO_vtJMa0n8neGutcjzo35-abb9mySHM48bE_PL/pubhtml?gid=1634695898&single=true)
[![Current Miles](https://img.shields.io/badge/Total_Run_Miles-4.0-orange)](https://docs.google.com/spreadsheets/d/e/2PACX-1vQhvv6U_CWuFcBQ8GLoYYLF6boAIvNBVmKnpBUM7wO_vtJMa0n8neGutcjzo35-abb9mySHM48bE_PL/pubhtml?gid=1634695898&single=true)
[![Training Phase](https://img.shields.io/badge/Phase-Base_Building-green)](https://docs.google.com/spreadsheets/d/e/2PACX-1vQhvv6U_CWuFcBQ8GLoYYLF6boAIvNBVmKnpBUM7wO_vtJMa0n8neGutcjzo35-abb9mySHM48bE_PL/pubhtml?gid=1634695898&single=true)


### ⏱️ Race-Day Projections
The following table represents the core predictive logic of the dashboard. It calculates my estimated finish time for **Ironman Canada (Ottawa)** by aggregating current training paces across all three disciplines.

| Discipline | Distance | Target Pace/Power | Predicted Split |
| :--- | :--- | :--- | :--- |
| **Swim** | 3.8 km | 2:10 / 100m | 1:22:20 |
| **Bike** | 180 km | 185 Watts | 6:15:00 |
| **Run** | 42.2 km | 6:15 / km | 4:23:45 |
| **Transitions** | — | — | 0:25:00 |
| **Total Project Finish** | **140.6 Miles** | — | **12:26:05** |

> *Note: These figures update automatically as my cardiovascular efficiency (Heart Rate vs. Power) improves during the 2026/2027 build phases.*
---

### 📊 Key Analytics & Predictive Features
* **Segment-Specific Race Prediction:** Uses current 100m (swim), power/cadence (bike), and km (run) averages to calculate a dynamic "Projected Finish Time."
* **Volume & Fatigue Management:** Monitors weekly "Time on Feet" and "Saddle Time" to ensure a 10% maximum weekly volume increase, mitigating injury risk over a long-term build.
* **Course-Adjusted Modeling:** (Upcoming) I am building a module to adjust my predicted bike splits based on the Ottawa Parkway's elevation profile and historical wind data.
* **Peer Benchmarking:** Once 2025/2026 finisher data for the Ottawa course is available, I will be importing that dataset to compare my predicted "Zone 2" efforts against real-world finisher percentiles.

---

### 🛠️ Data Stack
* **Engine:** Google Sheets (Logic-heavy architecture using `ARRAYFORMULA`, `VLOOKUP`, and custom time-conversion scripts).
* **Data Source:** Manual entry integrated with exported metrics from training devices.
* **Visualization:** Trend-line analysis for cardiovascular efficiency (Heart Rate vs. Power/Pace over time).

---

### 🎯 Portfolio Significance
This project demonstrates a unique intersection of **Data Analytics** and **High-Performance Athletics**:
1.  **Iterative Forecasting:** The model updates as I get fitter. It’s a living document that proves the value of "Current State vs. Future Goal" gap analysis.
2.  **Constraint-Based Planning:** Managing the logistics of a 140.6-mile race requires handling variables like fueling (calories/hr) and pacing—all of which are quantified in this dashboard.
3.  **Data Integrity:** Shows the ability to maintain a consistent, long-term dataset (18+ months) with clean entry and actionable outputs.
