# TDW_HR082025_CLEANED_DATA
Repository for storing and managing cleaned datasets prepared during the Data Engineering role at TopDataWork.

# 🧹 Data Cleaning Project

This project is all about cleaning and preparing raw data for further use.  
The original dataset was messy, and I used **Python and Pandas** to process it into a clean, structured format.

---

## 🔧 Tech Stack
- **Python** 🐍  
- **Pandas** (for data manipulation and cleaning)  
- **NumPy** (for handling numerical operations)  
- **Jupyter Notebook / VS Code** (for implementation)  

---
## 📁 Folder Structure

- `raw_data`: Original, unprocessed datasets.
- `clean_data`: Final cleaned CSVs ready for use.
- `Python_scripts`: Contains all scripts used for cleaning and organizing the data.

> **Note:** Due to GitHub's size limits, large CSV files may not display as tables in the UI. For best results, download and open raw files with a spreadsheet editor or pandas.


Quickly access raw files for reference, clean files for analysis, and scripts to review or reuse the cleaning steps.


## 📌 Data Cleaning Process

Here’s the step-by-step process I followed:

1. **Imported the Raw Dataset**  
   - Loaded the uncleaned `.csv` file using `pandas.read_csv()`.

2. **Checked the Data**  
   - Used functions like `.head()`, `.info()`, `.describe()` to understand the structure and detect issues.

3. **Handled Missing Values**  
   - Found null/missing values using `.isnull().sum()`.  
   - Filled or dropped values where necessary depending on the column.

4. **Removed Duplicates**  
   - Detected duplicate rows with `.duplicated()`.  
   - Dropped them using `.drop_duplicates()`.

5. **Fixed Inconsistencies**  
   - Standardized column names (like removing extra spaces, making them lowercase).  
   - Corrected inconsistent text values (e.g., `"Male"/"male"` → `"Male"`).

6. **Outlier Handling**  
   - Detected outliers using statistical methods.  
   - Cleaned/replaced extreme values where they didn’t make sense.

7. **Data Type Conversion**  
   - Converted columns to appropriate types (e.g., strings to dates, floats to integers where needed).

8. **Exported the Clean Data**  
   - Saved the cleaned dataset back into `.csv` format for further analysis.

---

## 📂 Output
At the end, I had a **well-structured, clean CSV file** that can be directly used for:
- Analysis  
- Visualization  
- Machine learning models  

---
