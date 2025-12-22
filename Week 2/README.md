# ACCESS_SAP_Data_Science_Track_Assignment_solutions
This week repository contains all my assignment for ACCESS 2.0 Data science

# WEEKK 2 SESSION 1 PART ONE ANSWERS
**Answers to Questions:**
* **df.head() - What are the first 3 things you notice in your dataset?**
    1. The dataset tracks alcohol sales (Wine, Beer, etc.) for Montgomery County.
    2. Initial rows show many products have 0.00 Retail Sales but active Warehouse Sales.
    3. The data includes specific identifiers like ITEM CODE and ITEM DESCRIPTION.
* **df.tail() - Are there any unusual patterns in the last few rows?**
    * The very last row (index 307644) is a "WINE CREDIT" with a negative Warehouse Sales value (-70.0) and a missing Supplier name, indicating a return or adjustment rather than a standard sale.
* **df.info() - How many rows and columns? Missing values? Data types?**
    * **Rows:** 307,645
    * **Columns:** 9
    * **Missing Values:** `SUPPLIER` has 167 missing values. `ITEM TYPE` (1) and `RETAIL SALES` (3) also have minor missing data.
    * **Data Types:** A mix of integers (Year, Month), floats (Sales, Transfers), and objects/strings (Supplier, Description).
* **df.describe() - Which numerical column has the highest mean? Suspicious values?**
    * **Highest Mean:** `WAREHOUSE SALES` has the highest average at **25.29**.
    * **Suspicious Values:** `WAREHOUSE SALES` has a minimum of **-7,800.00**, which is highly unusual and suggests a large return or data error.
* **df.columns and df.shape - List all column names. What is the full size?**
    * **Column Names:** YEAR, MONTH, SUPPLIER, ITEM CODE, ITEM DESCRIPTION, ITEM TYPE, RETAIL SALES, RETAIL TRANSFERS, WAREHOUSE SALES.
    * **Size:** (307645, 9).

---

###  Interpretation 

In 3–4 sentences, write your interpretation of the results. (What does this tell you about the dataset?)

The dataset reveals a high level of market concentration, where a few top-tier suppliers like E & J Gallo Winery and Diageo dominate total sales volume compared to hundreds of smaller vendors. Furthermore, the significantly higher averages in Warehouse Sales compared to Retail Sales indicate that the Montgomery County system functions primarily as a high-volume distribution hub rather than just a direct-to-consumer retailer.

### In 3–4 sentences, write your interpretation of the results. (What does this tell you about the dataset?)

The dataset reveals a high level of market concentration, where a few top-tier suppliers like E & J Gallo Winery and Diageo dominate total sales volume compared to hundreds of smaller vendors. The significantly higher averages in Warehouse Sales compared to Retail Sales indicate that the Montgomery County system functions primarily as a high-volume distribution hub rather than just a direct-to-consumer retailer.


### WEEK_2_SESSION_4

## Retail and Warehouse Sales Data Analysis
## Project Overview

This project focuses on cleaning, processing, and performing feature engineering on a retail dataset containing inventory and sales information across different channels (Retail vs. Warehouse).

The goal is to prepare a "clean" dataset for analysis by handling missing values, standardizing codes, and creating performance metrics.