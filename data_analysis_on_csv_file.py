import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define CSV file path as a variable
csv_file_path = r"C:\Users\Pratyak Das\Downloads\sales_data.csv"

# Load the CSV file
df = pd.read_csv(csv_file_path)
df['date'] = pd.to_datetime(df['date'])
df['total_sales'] = df['quantity'] * df['price']

# Group by product and calculate total sales and quantity
product_summary = df.groupby('product').agg({
    'total_sales': 'sum',
    'quantity': 'sum'
}).reset_index()
print("Product Summary:")
print(product_summary)

# Group by date and calculate daily sales
daily_sales = df.groupby('date').agg({'total_sales': 'sum'}).reset_index()
print("\nDaily Sales:")
print(daily_sales)

# Bar plot of total sales by product
plt.figure(figsize=(8, 5))
plt.bar(product_summary['product'], product_summary['total_sales'], color='skyblue')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales ($)')
plt.show()

# Line plot of daily sales
plt.figure(figsize=(8, 5))
plt.plot(daily_sales['date'], daily_sales['total_sales'], marker='o', color='green')
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()