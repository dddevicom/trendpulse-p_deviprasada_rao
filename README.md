#📊 TrendPulse: Real-Time Data Pipeline
TrendPulse is a modular Python-based data pipeline designed to extract, process, analyze, and visualize live trending stories from the HackerNews API. This project demonstrates the full lifecycle of data—from raw API response to meaningful visual insights.
---

##🔹 Project Architecture
The pipeline is split into four distinct tasks to ensure a clean, modular workflow:

1. Task 1: Data Collection (task1_data_collection.py)
   Uses requests and ThreadPoolExecutor to fetch top stories concurrently from the HackerNews API.
2. Task 2: Data Cleaning (task2_data_processing.py)
   Cleans the raw JSON, removes duplicates, filters low-score stories (Score < 5), and exports a structured CSV.
3. Task 3: Statistical Analysis (task3_analysis.py)
   Calculates global and category-wise performance metrics using NumPy and Pandas.
4. Task 4: Data Visualization (task4_visualization.py)
   Generates a visual report consisting of a bar chart for engagement and a pie chart for distribution.
---

## 🔹 Technologies Used

* Python
* Pandas
* Numpy
* Requests
* Datetime
* ThreadPoolExecutor
* Json
* Os
* Matplotlib
* Seaborn


---

## 🔹 Project Structure

trendpulse-yourname/
│── task1_data_collection.py
│── task2_data_processing.py
│── task3_analysis.py
│── task4_visualization.py
│── data/
│   ├── trends_YYYYMMDD.json  (Raw data)
│   └── trends_clean.csv      (Processed data)
│── visuals/
│   └── trendpulse_report.png (Generated charts)
└── README.md
---

## 🔹 How to Run the Project

### Step 1: Fetch Data

```bash
python fetch_data.py
```

### Step 2: Clean Data

```bash
python clean_data.py
```

### Step 3: Analyze Data

```bash
python analyze_data.py
```

### Step 4: Visualize Data

```bash
python visualize.py
```

---

## 🔹 Output
* Raw dataset from API
* Cleaned dataset
* Statistical summary
* Visualization chart
---

## 🔹 Key Features
* Concurrency: Fetches 500 story details efficiently using multi-threading.
* Compliance: Respects API rate limits with built-in delays between category loops.
* Robust Cleaning: Strips whitespace and handles missing values for reliable results.
* Insightful Visuals: Modern, publish-ready charts created with Seaborn styling.
---

## 🔹 Conclusion

This project demonstrates how a real-world data pipeline works by integrating data extraction, cleaning, analysis, and visualization into a single workflow. It helps in understanding how raw data can be transformed into meaningful insights.

---

## 🔹 Author

Pasupureddy Deviprasada Rao (iitp_aimlt_2601778 )
