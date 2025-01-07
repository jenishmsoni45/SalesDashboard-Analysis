import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the dataset
file_path = '/Users/jenishmayurkumarsoni/Desktop/SalesDashboard/superstore_sales.csv'
data = pd.read_csv(file_path, encoding='latin1')


# Print columns to confirm dataset structure
print("Columns in the dataset:")
print(data.columns)

# Step 1: Profit by Region
if 'Region' in data.columns and 'Profit' in data.columns:
    region_profit = data.groupby('Region')['Profit'].sum()
    print("\nProfit by Region:")
    print(region_profit)

    plt.figure(figsize=(8, 6))
    region_profit.plot(kind='bar', color='orange')
    plt.title('Profit by Region')
    plt.xlabel('Region')
    plt.ylabel('Total Profit')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('/Users/jenishmayurkumarsoni/Desktop/SalesDashboard/profit_by_region.png')
    print("Chart saved as profit_by_region.png")
    plt.close()
else:
    print("Error: 'Region' or 'Profit' column not found.")

# Step 2: Sales Trend Over Time
if 'Order Date' in data.columns and 'Sales' in data.columns:
    data['Order Date'] = pd.to_datetime(data['Order Date'], errors='coerce')
    sales_trend = data.groupby(data['Order Date'].dt.to_period('M'))['Sales'].sum()

    print("\nSales Trend Over Time:")
    print(sales_trend)

    plt.figure(figsize=(12, 6))
    sales_trend.plot(kind='line', marker='o', color='blue')
    plt.title('Sales Trend Over Time')
    plt.xlabel('Time (Month-Year)')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('/Users/jenishmayurkumarsoni/Desktop/SalesDashboard/sales_trend_over_time.png')
    print("Chart saved as sales_trend_over_time.png")
    plt.close()
else:
    print("Error: 'Order Date' or 'Sales' column not found.")

# Step 3: Top 10 Products by Profit
if 'Product Name' in data.columns and 'Profit' in data.columns:
    top_products_profit = data.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)
    print("\nTop 10 Products by Profit:")
    print(top_products_profit)

    plt.figure(figsize=(10, 6))
    top_products_profit.plot(kind='barh', color='purple')
    plt.title('Top 10 Products by Profit')
    plt.xlabel('Total Profit')
    plt.ylabel('Product Name')
    plt.tight_layout()
    plt.savefig('/Users/jenishmayurkumarsoni/Desktop/SalesDashboard/top_products_profit.png')
    print("Chart saved as top_products_profit.png")
    plt.close()
else:
    print("Error: 'Product Name' or 'Profit' column not found.")
