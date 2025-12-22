
# You must add the filename at the end of the path
file_path = r"C:\Users\user\Documents\ACCESS_SAP_Data_Science_Track_Assignment_solutions\Week 2\Warehouse_and_Retail_Sales.csv"
import pandas as pd

# Handle missing values and duplicates.
df = pd.read_csv(file_path)
df_head = df.head()
# Check for missing values
missing_values =  df.isna().sum()
print("Missing values in each columns:\n", missing_values)
# cleaning the dataset
df_clean = df.dropna(subset=['RETAIL SALES', 'WAREHOUSE SALES'])
print("After removing missing values, dataset shape:\n", df_clean)

# filling missing dataset
df['RETAIL SALES'].fillna('Unknown', inplace=True)
df['WAREHOUSE SALES'].fillna('Unknown', inplace=True)
df_head_2 = df.head(100)
print("After filling missing values, dataset head:\n", df_head_2)
df['SUPPLIER'].fillna('Unknown', inplace=True)
print("After filling missing values in SUPPLIER, dataset head:\n", df.head(100))
df_head_3 = df.head()
print(df_head_3)


df_clean.duplicated()
print(df_clean.duplicated())

df_clean.duplicated().sum()
print(df_clean.duplicated().sum())

# Remove duplicate rows (keeping first occurrence)
df_clean = df_clean.drop_duplicates()
print(df_clean)
print(f"Shape after removing duplicates: {df_clean.shape}")
# checking year column
df_year = df_clean['YEAR']
print(df_year)
# checking month column
df_month = df_clean['MONTH']
print(df_month)
df.head()
print(df.head())
# checking retail sales column
df_retail_sales = df_clean['RETAIL SALES']
print(f" Retail Sales: {df_retail_sales}")
df.head_retail_sales = df_clean['RETAIL SALES'].head(100)
print(df.head_retail_sales)

df.columns = df.columns.str.strip().str.upper()
print(df.columns)

# checking item code data set
df_item_code = df_clean['ITEM CODE']
print(f" Item Code: {df_item_code}")

# 1. Target rows where 'ITEM CODE' is exactly 'WC' and set them to 0
df_clean.loc[df_clean['ITEM CODE'] == 'WC', 'ITEM CODE'] = 0

# 2. Verify the change
print(df_clean['ITEM CODE'].value_counts())
df_item_code_updated = df_clean['ITEM CODE']
print(f" Updated Item Code: {df_item_code_updated}")

df.columns = df.columns.str.strip().str.upper()
print(df.columns)

# checking item description data set
df_item_description = df_clean['ITEM DESCRIPTION']
print(f" Item Description : {df_item_description}") # This is okay for now


df.columns = df.columns.str.strip().str.upper()
print(df.columns)

# checking item types
df_item_type = df_clean['ITEM TYPE']
print(f" Item type : {df_item_type}")

# 1. Target rows where 'ITEM TYPE' is exactly 'REF' and set them to others
df_clean.loc[df_clean['ITEM TYPE'] == 'REF', 'ITEM TYPE'] = 'Others'

# 2. Verify the change
print(df_clean['ITEM TYPE'].value_counts())
df_item_type_updated = df_clean['ITEM TYPE']
print(f" Updated Item type: {df_item_type_updated}") # This is okay for now


df.columns = df.columns.str.strip().str.upper()
print(df.columns)

# checking retail sales column
df_retail_sales = df_clean['RETAIL SALES']
print(f" Retail Sales : {df_retail_sales}")

df.columns = df.columns.str.strip().str.upper()
print(df.columns)

# checking warehouse sales column
df_warehouse_sales = df_clean['WAREHOUSE SALES']
print(f" Warehouse Sales : {df_warehouse_sales}")

# View all rows where sales are negative
negatives = df_clean[df_clean['RETAIL SALES'] < 0]
print(negatives[['ITEM CODE', 'WAREHOUSE SALES', 'RETAIL SALES']].head())

# Part 2 Create at least two new derived columns (e.g., performance ratios or total campaign success).

# Create a new column 'TOTAL SALES' as the sum of 'RETAIL SALES' and 'WAREHOUSE SALES'
df_clean['TOTAL SALES'] = df_clean['RETAIL SALES'] + df_clean['WAREHOUSE SALES']
print(df_clean['TOTAL SALES'].head())

# Retail sales  to warehouse sales ratio
df_clean['RET_T0_WHS_RATIO'] = df_clean['RETAIL SALES'] / df_clean['WAREHOUSE SALES']
print(f" Retail sales to warehouse sales ratio: {df_clean['RET_T0_WHS_RATIO'].head()}")
# verify the new columns
df.columns = df.columns.str.strip().str.upper()
print(df.columns)
df_clean.head(20)
print(df_clean.head(20))

# Save to CSV
df_clean.to_csv('Warehouse_and_Retail_Sales.csv', index=False)
# Verify saved file
df_verified = pd.read_csv('Warehouse_and_Retail_Sales.csv')
print(df_verified.head())

# THE END