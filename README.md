# 📊 Habit Tracker Analyzer (Python)

A Python-based habit tracking and analysis tool that transforms daily behavioral data into actionable insights.
The project combines data processing, statistical analysis, and visualization to evaluate consistency, streaks, and overall habit performance.

This project demonstrates an end-to-end data workflow:

* CSV data ingestion
* analytical computation (NumPy)
* visualization (Matplotlib)
* reporting and export

---

## ✨ Features

* 📥 Load habit data from CSV files
* 📊 Compute key metrics:

  * Habit completion rates
  * Current streaks
  * Longest streaks
* 🔥 GitHub-style habit heatmap visualization
* 💾 Generate structured reports in CSV format
* 🧠 Clean, modular project structure (data / src / outputs)

---

## 🧱 Project Structure

```
habit-tracker-analyzer/
│
├── data/              # Raw input data
├── src/               # Core logic
│   ├── data_loader.py
│   ├── analysis.py
│   ├── visualization.py
│
├── outputs/           # Generated files (plots, exports)
├── main.py            # Entry point
├── README.md
```

---

## 📸 Example Output

![Habit Heatmap](outputs/heatmap.png)

---

## ⚙️ Tech Stack

* Python 3.14
* NumPy
* Matplotlib

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🎯 Purpose

This project demonstrates:

* Processing and analyzing behavioral data in Python
* Designing modular and scalable project structures
* Applying NumPy for efficient numerical computation
* Building insightful visualizations with Matplotlib
* Creating reproducible personal analytics workflows

---

## 🔮 Future Improvements

* Interactive visualizations (mplcursors / Plotly)
* CLI interface (argparse / Typer)
* Database integration (SQLite / PostgreSQL)
* Streamlit dashboard
* Automated habit tracking pipeline

---

## 📜 License

CC0-1.0
