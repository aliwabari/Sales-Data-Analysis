# E-Commerce Sales Data Cleaning & Analysis

## Project Overview
This project takes a dirty e-commerce sales dataset (530+ rows, 16 columns) and walks through a complete data cleaning and analysis pipeline.

## Dataset
- **Source:** Simulated e-commerce sales data with 19 types of real-world data quality issues
- **Columns:** Order_ID, Customer Name, Email, Product, Category, Quantity, Unit Price, Total, Order Date, Ship Date, City, Country, Payment Method, Status, Discount%, Region

## Data Issues Found
1. Missing values across multiple columns
2. Inconsistent text casing (names, categories, countries)
3. Typos in payment methods and product names
4. Invalid emails (missing @, double @@, no domain)
5. Mixed date formats (DD/MM/YYYY, MM-DD-YYYY, YYYY/MM/DD)
6. Negative quantities and prices
7. Outlier prices (10x data entry errors)
8. Wrong totals (Total ≠ Qty × Price)
9. Duplicate rows and duplicate Order_IDs
10. Ship dates before order dates
11. City-country mismatches
12. Invalid discounts (>100% or negative)
13. Junk/test rows (empty, "TEST", placeholder data)

## Project Structure
```
ecommerce_project/
├── data/
│   ├── raw/                  # Original dirty data (never modify)
│   ├── cleaned/              # Output after cleaning
│   └── processed/            # Final analysis-ready data
├── notebooks/
│   ├── 01_exploration.ipynb  # Initial data exploration & profiling
│   ├── 02_cleaning.ipynb     # Step-by-step data cleaning
│   ├── 03_analysis.ipynb     # Statistical analysis
│   └── 04_visualization.ipynb# Charts and visual insights
├── scripts/
│   ├── clean_data.py         # Reusable cleaning functions
│   ├── analyze.py            # Analysis helper functions
│   └── utils.py              # General utility functions
├── outputs/
│   ├── charts/               # Saved chart images
│   └── reports/              # Summary reports
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Place the dirty dataset in `data/raw/`
3. Run notebooks in order: 01 → 02 → 03 → 04
4. Find cleaned data in `data/cleaned/` and results in `outputs/`

## Tools Used
- Python 3.x
- pandas, openpyxl, matplotlib, seaborn
