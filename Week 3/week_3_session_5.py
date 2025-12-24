#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

file_path = r"C:\Users\user\Documents\ACCESS_SAP_Data_Science_Track_Assignment_solutions\Week 3\Warehouse_and_Retail_Sales.csv"




#---------------------------PART A - Data Overview & Inspection------------------------------------------
#Display the first 5 rows of the dataset
df_head = pd.read_csv(file_path )
print("First 5 rows of the dataset:\n", df_head.head())
#Display the last 5 rows of the dataset
df_tail = pd.read_csv(file_path)
print(f" Last 5 rows of the dataset : {df_tail.tail()}")

# Checking the following 

# number of rows and columns in the dataset
df_shape = pd.read_csv(file_path)
print(f" Numbers of rows and columns are : {df_shape.shape}")

# column names in the dataset
df_columns = pd.read_csv(file_path)
print(f" Columns names are : {df_columns.columns}")

# Data types
df_info = pd.read_csv(file_path)
print(f" Data types are as follows :: {df_info.dtypes}")

# Use .describe() on numerical columns.
df_describe = pd.read_csv(file_path)
print("Description of the dataset:\n", df_describe.describe())

# Answer the following questions:

# Are there values that suggest possible outliers?
df_outliers = pd.read_csv(file_path)
outliers = np.abs(stats.zscore(df_outliers.select_dtypes(include=[np.number])))
print(f"outliers", outliers)
print("Outlier values :\n", np.where(outliers > 3))
#Answers - yes there are many outliers

# Which column(s) might contain unusually large values?





# -----------------------------------PART B - Univariate Analysis---------------------------------
# Numerical Analysis

# Select one numerical column related to sales or quantity.
df_read = pd.read_csv(file_path)
print(f" The first five columns of the dataset are : {df_read.head()}")

# selecting 'RETAIL SALES' column for histogram and box plot
retail_sales = df_read['RETAIL SALES']
# Create a histogram to visualize the distribution of values in this column.
plt.figure(figsize=(10, 5))
sns.histplot(df_read['RETAIL SALES'], bins = 30, kde = True)
plt.title('Histogram of Retail Sales')
plt.xlabel('Retail Sales')
plt.ylabel('Frequency')     
plt.show()

# create a box plot to visualize the distribution of values in this column
plt.figure(figsize=(7, 5))
sns.boxplot(x = df_read['RETAIL SALES'], color='lightblue')

plt.title('Box Plot of Retail Sales')
plt.xlabel('Retail Sales')
plt.show()

# Write a short explanation:

#What does the distribution look like?
#Answer - The distribution of the 'RETAIL SALES' column is highly right-skewed, with a massive peak at the lower end of the scale and a long tail extending to the right.
#Are there possible outliers?
#Answer - Yes, there are many significant outliers in this dataset.


# Categorical Analysis
# Select one categorical column (e.g. product type, location, or warehouse).
# targetting  supplier column for categorical analysis

df_read_suppliers = df_read['SUPPLIER'].value_counts()

# Select only the top 10 to keep the chart clean
top_10_suppliers = df_read_suppliers.head(10)

plt.figure(figsize=(12, 6))

# use the index (names) for x and the values (counts) for y
sns.barplot(x=top_10_suppliers.index, y=top_10_suppliers.values, palette='viridis')

plt.title('Top 10 Suppliers by Frequency')
plt.xlabel('Supplier Name')
plt.ylabel('Number of Transactions')

#  Rotate labels so they are readable
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()

# Write a short explanation:

#Which category appears most often?
# Answer- Repulic national distribution and co.

#What could this mean for the business?
# Answer- This could indicate that this supplier is a major partner for the business, potentially offering favorable terms, reliable delivery, or a wide range of products that meet the business's needs effectively.





#-----------------------------------PART C - Bivariate Analysis---------------------------------
pd_read = pd.read_csv(file_path)
print(f" The first 10 columns of the dataset are : {pd_read.head(10)}")
# Select two numerical columns related to sales and quantity.
# selecting  RETAIL SALES for the numerical column and ITEM TYPE for categorical column
plt.figure(figsize=(12, 6))
sns.barplot(x='ITEM TYPE', y='RETAIL SALES', data=pd_read, palette='coolwarm')
plt.title('Average Retail Sales by Item Type')
plt.xlabel('Item Type')
plt.ylabel('Average Retail Sales')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
# Write a short explanation:


#Answer:

#Does spending/sales vary across categories?
#Which category appears to generate higher values?
# Answer- Yes, spending/sales vary significantly across different item types. 
# The category 'Non-Alcoholic' appears to generate higher average retail sales compared to other item types.





#-----------------------------------PART D - Outlier Detection--------------------------------

# using .describe
df_outliers_desc = pd.read_csv(file_path)
print(f"Describing the outliers :  {df_outliers_desc.describe()}")# yep many outliers

# using boxplot
plt.figure(figsize=(7, 5))
sns.boxplot(x = df_read['WAREHOUSE SALES'], color='lightgreen')
plt.title('Box Plot for Outlier Detection')
plt.xlabel('Values')
plt.show()# yep many outliers in warehouse sales

# Answer:

#Why might these outliers exist?
#Outliers in warehouse sales could be due to large orders, seasonal fluctuations, or one-time events such as bulk purchases or promotional campaigns.
#Are they likely errors or genuine business events?
# They are likely genuine business events, reflecting the variability in sales volumes that can occur in a warehouse setting.





# -----------------------------------PART E - Correlation Analysis---------------------------------
df_corr = pd.read_csv(file_path)
# select 2 numerical columns and compute their correlation
df_corr_subset = df_corr[['RETAIL SALES', 'WAREHOUSE SALES']]
correlation = df_corr_subset.corr()
print("Correlation of Retail Sales and Warehouse Sales:\n", correlation)


plt.figure(figsize = (10,4))
sns.heatmap(df_corr_subset.corr(numeric_only = True), annot = True)
plt.title("Correlation Heatmap")
plt.show()
#Answer:

#Is the correlation weak, moderate, or strong?
# The correlation between Retail Sales and Warehouse Sales appears to be moderate

#How could this information be useful in business analysis?
# Strategic Pricing: Since price has a strong link to revenue, small price adjustments




#----------------------------------------PART F - Business Questions & Insights---------------------------------
#Develop and answer THREE (3) business questions, such as:



#Number 1
#Which warehouse/location records the highest sales?
# Aggregate sales by Item Type
df_read['TOTAL SALES'] = df_read['RETAIL SALES'] + df_read['WAREHOUSE SALES']
sales_by_type = df_read.groupby('ITEM TYPE')['TOTAL SALES'].sum().sort_values(ascending=False).reset_index()

# Visualization
plt.figure(figsize=(10, 6))
sns.barplot(data=sales_by_type, x='ITEM TYPE', y='TOTAL SALES', palette='viridis')
plt.title('Total Sales by Product Category')
plt.xlabel('Item Type')
plt.ylabel('Total Sales Volume')
plt.show()
# Bussuiness Insight:
# Beer is the dominant product category, generating over 7.1 million in total sales. 
# This is significantly higher than Wine (1.9M) and Liquor (897k).



# Numeber 2
#Are there products with consistently high sales?

# Calculate totals for each channel
total_retail = df_read['RETAIL SALES'].sum()
total_warehouse = df_read['WAREHOUSE SALES'].sum()

# Visualization
plt.figure(figsize=(8, 6))
sns.barplot(x=['Retail Sales', 'Warehouse Sales'], y=[total_retail, total_warehouse], palette='magma')
plt.title('Sales Volume: Retail vs. Warehouse')
plt.ylabel('Total Sales Volume')
plt.show()
# Business Insight:
# Warehouse Sales (7.7M) vastly outperform Retail Sales (2.1M), 
# accounting for nearly 78% of total volume.



#Number 3
#Are there periods with unusually high sales volumes?

# Group by Month to see seasonality
monthly_sales = df_read.groupby('MONTH')['TOTAL SALES'].sum().reset_index()

# Visualization
plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_sales, x='MONTH', y='TOTAL SALES', marker='o', linewidth=2.5, color='blue')
plt.title('Monthly Sales Trends (Seasonality)')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(range(1, 13)) 
plt.grid(True)
plt.show()
# Business Insight:
# There are distinct seasonal peaks in July and September, 
# where monthly sales top 1.2 million.



#Number 4
#Which product category generates the most sales?

# Group by Supplier and sum total sales, taking the top 5
top_suppliers = df_read.groupby('SUPPLIER')['TOTAL SALES'].sum().sort_values(ascending=False).head(5).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=top_suppliers, x='TOTAL SALES', y='SUPPLIER', palette='coolwarm')
plt.title('Top 5 Suppliers by Total Revenue')
plt.xlabel('Total Revenue ($)')
plt.show()
# Business Insight:
#Crown Imports is the top supplier (1.7M revenue), followed by Miller Brewing and Anheuser Busch. 
# The top 4 suppliers are all major beer distributors.


#Number 5
#Which store type performs better?

# Group by Item Description to find top sellers
top_items = df_read.groupby('ITEM DESCRIPTION')['TOTAL SALES'].sum().sort_values(ascending=False).head(5).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=top_items, x='TOTAL SALES', y='ITEM DESCRIPTION', palette='mako')
plt.title('Top 5 Best-Selling Specific Items')
plt.xlabel('Total Revenue ($)')
plt.show()
# Business Insight:
# The single highest-grossing item is Corona Extra (Loose Bottles), 
# followed by Corona Extra (12-packs) and Heineken.


#Number 6
#Are there seasonal sales patterns

# Analyze Retail Transfers by Item Type
transfers_by_type = df_read.groupby('ITEM TYPE')['RETAIL TRANSFERS'].sum().sort_values(ascending=False).reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=transfers_by_type, x='ITEM TYPE', y='RETAIL TRANSFERS', palette='Reds')
plt.title('Volume of Retail Transfers by Category')
plt.ylabel('Total Value of Transfers')
plt.show()
# Business Insight:
# While Beer sells the most, 
# Liquor and Wine have the highest transfer values 
# (approx. 794k and 734k respectively).