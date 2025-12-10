# 🏠 Real Estate Investment Analysis & Streamlit Dashboard (Python)

## 📌 Project Overview
This project analyzes real estate housing data to help users understand pricing trends and make better investment decisions.  
The complete project is built using **Python**, and includes:

- ✅ Data Preprocessing
- ✅ Exploratory Data Analysis (EDA)
- ✅ Interactive Streamlit Dashboard

## ⚙️ Tools & Libraries Used

| Library | Purpose |
|----------|----------|
| pandas | Data loading, cleaning, and manipulation |
| matplotlib | Data visualization |
| seaborn | Statistical visualizations |
| streamlit | Interactive dashboard creation |
| VS Code | Code editor for development |

# ✅ STEP 1: Data Preprocessing

### 📍 Where?
File used:
step1-preprocessing/step1-preprocessing.py

### 🎯 Why?
To clean the raw dataset so that it becomes:
- Error-free
- Analysis-ready
- Suitable for visualization

### 🛠 Which Library & Why?
- **pandas** → Used to load the CSV file, handle missing values, remove duplicates, and create new columns.

### ✅ What Was Done in This Step?
- Loaded the raw CSV dataset using `pandas.read_csv()`
- Checked missing values using `isnull().sum()`
- Filled missing:
  - Numerical values using **median**
  - Categorical values using **mode**
- Removed duplicate rows
- Created a new feature:
  - `price_per_sqft`
- Saved the cleaned data as:
data/cleaned_data.csv

# ✅ STEP 2: Exploratory Data Analysis (EDA)

### 📍 Where?
File used:
step2_eda/step2_eda.py

### 🎯 Why?
To understand:
- Price distribution
- Relationship between size and price
- City-wise and category-wise patterns
- Numerical relationships between columns

### 🛠 Which Libraries & Why?
- **pandas** → Data loading
- **matplotlib** → Basic plotting
- **seaborn** → Statistical & advanced charts

### ✅ What Was Done in This Step?
- Displayed dataset structure and summary using:
  - `df.info()`  
  - `df.describe()`
- Created the following charts:
  - Price Distribution (Histogram)
  - Size vs Price (Scatter Plot)
  - Category / Property Type Count
  - Correlation Heatmap (Only numeric columns)
- All visualizations helped in identifying:
  - Pricing trends
  - Investment patterns
  - Feature relationships

# ✅ STEP 3: Streamlit Interactive Dashboard

### 📍 Where?
File used:
step5_dashboard/app.py

### 🎯 Why?
To convert the analysis into a **user-friendly web application** where:
- Users can explore property data
- Enter price values
- Get future price predictions
- Receive an investment decision

### 🛠 Which Libraries & Why?
- **streamlit** → To create the web dashboard
- **pandas** → To load and filter data
- **matplotlib & seaborn** → To show charts inside the dashboard

### ✅ What This Dashboard Does:
- Displays dataset preview
- Allows city selection using dropdown
- Takes user input for property price
- Predicts future price after 5 years using 8% annual growth
- Shows:
  - ✅ Good Investment
  - ❌ Not a Good Investment
- Displays the following charts:
  - Price Distribution
  - City-wise Average Price
  - Category / Property Type Count


# ▶️ How to Run This Project

### 1️⃣ Install Required Libraries
pip install pandas matplotlib seaborn streamlit

### 2️⃣ Run Data Preprocessing
python step1_preprocessing/step1_preprocessing.py

### 3️⃣ Run EDA
python step2_eda/step2_eda.py

### 4️⃣ Run Streamlit Dashboard
streamlit run step5_dashboard/app.py
