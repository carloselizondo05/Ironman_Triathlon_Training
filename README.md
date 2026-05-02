# 🏊‍♂️ Ironman Canada (Ottawa) 2027: Predictive Performance Dashboard

**Target Race:** Ironman Canada 140.6 · Ottawa, ON · August 2027  
**Project Status:** Active Training & Data Collection  
**Tools:** Google Sheets · ARRAYFORMULA · VLOOKUP · Custom Time-Conversion Scripts

[![Training Phase](https://img.shields.io/badge/Phase-Base_Building-green)](https://docs.google.com/spreadsheets/d/e/2PACX-1vQhvv6U_CWuFcBQ8GLoYYLF6boAIvNBVmKnpBUM7wO_vtJMa0n8neGutcjzo35-abb9mySHM48bE_PL/pubhtml?gid=1634695898&single=true)

> **[View the Live Google Sheets Training Dashboard →](https://docs.google.com/spreadsheets/d/1lPLLLyabq1FIgv9QlJgcaRqtcBulhBTVE7C0FU1eAIE/edit?usp=sharing)**

---

## 📋 Project Overview

Rather than relying on generic fitness apps, I built this custom dashboard to manage my 18-month journey toward completing Ironman Canada 140.6. It integrates volume tracking with performance forecasting, tailored specifically to the Ottawa course profile — river swim, closed parkway bike, and Parliament Hill finish.

The model treats race-day performance as a data problem: current training paces across all three disciplines feed into a projected finish time that updates as cardiovascular efficiency improves throughout the 2026/2027 build phases.

---

## ⏱️ Current Race-Day Projections

*Live figures are tracked in the Google Sheets dashboard linked above. The table below reflects current projections as of last update.*

| Discipline | Distance | Target Pace / Power | Projected Split |
| :--- | :--- | :--- | :--- |
| **Swim** | 3.8 km | 2:10 / 100m | 1:22:20 |
| **Bike** | 180 km | 185 Watts | 6:15:00 |
| **Run** | 42.2 km | 6:15 / km | 4:23:45 |
| **Transitions** | — | — | 0:25:00 |
| **Projected Finish** | **140.6 Miles** | — | **12:26:05** |

---

## 📊 Key Analytics & Predictive Features

**Segment-Specific Race Prediction:** Uses current 100m (swim), power/cadence (bike), and pace/km (run) averages to calculate a dynamic projected finish time that updates as training progresses.

**Volume & Fatigue Management:** Monitors weekly time on feet and saddle time to enforce a 10% maximum weekly volume increase, mitigating injury risk across a long-term build.

**Course-Adjusted Modeling (Upcoming):** Building a module to adjust predicted bike splits based on the Ottawa Parkway's elevation profile and historical wind data.

**Peer Benchmarking (Upcoming):** Once 2025/2026 Ottawa finisher data is available, will import that dataset to compare predicted Zone 2 efforts against real-world finisher percentiles.

---

## 🛠️ Data Stack

**Engine:** Google Sheets — logic-heavy architecture using `ARRAYFORMULA`, `VLOOKUP`, and custom time-conversion scripts to handle pace and power calculations across disciplines.

**Data Source:** Manual entry integrated with exported metrics from training devices.

**Visualization:** Trend-line analysis tracking cardiovascular efficiency (Heart Rate vs. Power/Pace) over time to measure aerobic adaptation.

---

## 🎯 Portfolio Significance

This project sits at the intersection of data analytics and long-term performance planning:

**Iterative Forecasting:** The model updates as fitness improves — it's a living document demonstrating gap analysis between current state and a fixed future goal.

**Constraint-Based Planning:** Managing a 140.6-mile race requires quantifying variables like fueling (calories/hr), pacing strategy, and discipline-specific efficiency. All of these are tracked and modeled in the dashboard.

**Data Integrity:** The project requires maintaining a consistent, clean dataset across 18+ months of training — demonstrating the discipline of long-term data stewardship alongside the technical build.

---

## 🤝 Contributing & License

This is a personal performance project — feedback and suggestions welcome via issues.

Licensed under the [MIT License](LICENSE).
