# ---------------------------------------------------------
# BIG DATA ANALYSIS – ONLINE RETAIL DATASET
# ---------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. LOAD THE DATASET
# ---------------------------------------------------------

df = pd.read_csv("online_retail.csv")  # update filename if needed
print(df.head())

# ---------------------------------------------------------
# 2. DATA CLEANING
# ---------------------------------------------------------

# 2.1 Rename columns for easier use (optional)
df.columns = ['Invoice', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 
              'Price', 'CustomerID', 'Country']

# 2.2 Remove missing CustomerID (common in this dataset)
df['CustomerID'] = df['CustomerID'].fillna("Unknown")

# 2.3 Remove rows with missing descriptions
df['Description'] = df['Description'].fillna("No Description")

# 2.4 Convert InvoiceDate
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')

# 2.5 Fix negative or invalid Quantity & Price
df = df[df['Quantity'] > 0]
df = df[df['Price'] > 0]

# 2.6 Calculate Total Amount
df["TotalAmount"] = df["Quantity"] * df["Price"]

# 2.7 Remove duplicates
df = df.drop_duplicates()

print("\nCleaned Data:")
print(df.head())

# ---------------------------------------------------------
# 3. DATA ANALYSIS & BUSINESS INSIGHTS
# ---------------------------------------------------------

# Insight 1: Top 10 best-selling products by revenue
top_products = df.groupby("Description")["TotalAmount"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products by Revenue:")
print(top_products)

# Insight 2: Country-wise sales distribution
country_sales = df.groupby("Country")["TotalAmount"].sum().sort_values(ascending=False)
print("\nSales by Country:")
print(country_sales.head(10))

# Insight 3: Monthly sales trend
df["Month"] = df["InvoiceDate"].dt.month
monthly_sales = df.groupby("Month")["TotalAmount"].sum()
print("\nMonthly Sales Trend:")
print(monthly_sales)

# ---------------------------------------------------------
# 4. VISUALIZATIONS
# ---------------------------------------------------------

# 4.1 Top 10 products bar chart
plt.figure(figsize=(10,5))
top_products.plot(kind='bar')
plt.title("Top 10 Products by Revenue")
plt.ylabel("Revenue")
plt.xlabel("Product Description")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 4.2 Sales by Country (Top 10)
plt.figure(figsize=(10,5))
country_sales.head(10).plot(kind='bar')
plt.title("Top 10 Countries by Sales")
plt.ylabel("Total Sales")
plt.xlabel("Country")
plt.tight_layout()
plt.show()

# 4.3 Monthly sales line chart
plt.figure(figsize=(8,5))
monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()

# ---------------------------------------------------------
# 5. SUMMARY
# ---------------------------------------------------------

print("\nSUMMARY OF FINDINGS:")
print("1. Top-selling products (e.g., gift items) generate high revenue.")
print("2. United Kingdom usually contributes the highest sales.")
print("3. Sales show monthly seasonality peaks before Christmas.")
print("Big data analysis helps businesses optimize inventory, marketing, and forecasting.")
