#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

file_path = r"C:\Users\user\Documents\ACCESS_SAP_Data_Science_Track_Assignment_solutions\Week 3\retail_sales_dataset.csv"

df = pd.read_csv(file_path)
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M').astype(str)

sns.set_theme(style="whitegrid")

fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Monthly Sales Trend
monthly_sales = df.groupby('Month')['Total Amount'].sum().reset_index()
sns.lineplot(ax=axes[0,0], data=monthly_sales, x='Month', y='Total Amount', marker='o', color='b')
axes[0,0].set_title('1. Monthly Sales Trend (2023)')
axes[0,0].tick_params(axis='x', rotation=45)

# Revenue by Product Category
category_sales = df.groupby('Product Category')['Total Amount'].sum().sort_values(ascending=False).reset_index()
sns.barplot(ax=axes[0,1], data=category_sales, x='Product Category', y='Total Amount', palette='viridis')
axes[0,1].set_title('2. Total Revenue by Category')

# Sales Distribution by Gender
gender_sales = df.groupby('Gender')['Total Amount'].sum()
axes[1,0].pie(gender_sales, labels=gender_sales.index, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff'])
axes[1,0].set_title('3. Revenue Contribution by Gender')

# Average Spending per Age Group
bins = [18, 30, 45, 60, 100]
labels = ['18-30', '31-45', '46-60', '60+']
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
age_group_sales = df.groupby('Age Group')['Total Amount'].mean().reset_index()
sns.barplot(ax=axes[1,1], data=age_group_sales, x='Age Group', y='Total Amount', palette='coolwarm')
axes[1,1].set_title('4. Average Spending per Age Group')

plt.tight_layout()
plt.savefig('retail_business_story.png')
plt.show()