import pandas as pd

#-------------------------Part 1: Reading & Inspecting Your Dataset ----------------------------------

# You must add the filename at the end of the path
file_path = r"C:\Users\user\Documents\ACCESS_SAP_Data_Science_Track_Assignment_solutions\Week 2\Warehouse_and_Retail_Sales.csv"

# Reading the dataset of  first 5 rows
df_warh_head = pd.read_csv(file_path)

# Display the first 5 rows
print(df_warh_head.head())

# reading the dataset of  last 5 rows
df_warh_tail = pd.read_csv(file_path)

# Display the last 5 rows
print(df_warh_tail.tail())

#display information about the dataframe
df_info = pd.read_csv(file_path)
print(df_info.info())

#Describe the dataframe
df_describe = pd.read_csv(file_path)
print(df_describe.describe())

#columns of the dataframe
df_columns = pd.read_csv(file_path)
print(df_columns.columns)

#shape of the dataframe
df_shape = pd.read_csv(file_path)
print(df_shape.shape)


#--------------------------Part 2: Column Selection & Basic Filtering----------------------------------

#A. Selecting Columns
#Select any two numerical columns and display them.
df_numerical = pd.read_csv(file_path)
print(df_numerical[['RETAIL SALES', 'RETAIL TRANSFERS']])
#Select any two categorical columns and display them.
df_categorical = pd.read_csv(file_path)
print(df_categorical[['SUPPLIER', 'ITEM DESCRIPTION']])

#B. Filtering Rows


df_filtered = pd.read_csv(file_path)
filtered_data = df_filtered[df_filtered['RETAIL SALES'] > 50000]
print(filtered_data)
filtered_data_age = df_filtered[df_filtered['WAREHOUSE SALES'] < 25]
print(filtered_data_age)
filtered_data_rating = df_filtered[df_filtered['RETAIL TRANSFERS'] == 5]
print(filtered_data_rating)


df_loc = pd.read_csv(file_path)
loc_filtered = df_loc.loc[(df_loc['RETAIL SALES'] > 50000) & (df_loc['WAREHOUSE SALES'] < 30), ['SUPPLIER', 'RETAIL SALES', 'WAREHOUSE SALES']]
print(loc_filtered)

#C. Using .iloc[]

df_iloc  = pd.read_csv(file_path)
first_5_rows_and_first_3_columns = df_iloc.iloc[0:5, 0:3]
print(first_5_rows_and_first_3_columns)
Rows_10_20_and_columns_2_4 = df_iloc.iloc[10:21, 2:5]
print(Rows_10_20_and_columns_2_4)



#--------------------------PART 3 Part 3: Grouping & Aggregation (Critical Skill) ----------------------------------
df_grouped = pd.read_csv(file_path)
grouped_data = df_grouped.groupby('SUPPLIER')['RETAIL SALES'].sum()
print(grouped_data)
# question - What is the total retail sales for each supplier?

    
df_agg = pd.read_csv(file_path)
total_retail_sales_per_supplier = df_agg.groupby('SUPPLIER')['RETAIL SALES'].sum()
print(total_retail_sales_per_supplier)

df_multi_agg = pd.read_csv(file_path)
metrics_per_supplier = df_multi_agg.groupby('SUPPLIER')['RETAIL SALES'].agg(['sum', 'mean', 'max', 'count'])
print(metrics_per_supplier)