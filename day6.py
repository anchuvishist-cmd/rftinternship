import csv

# Sample dataset (can be replaced with CSV file reading)
data = [
    ["A", 2, 100],
    ["B", 1, 200],
    ["A", 3, 100],
    ["C", 5, 50]
]

# Dictionary to store total sales per product
sales = {}

# Column-based operation in O(n)
for product, qty, price in data:
    total = qty * price
    sales[product] = sales.get(product, 0) + total

# Calculate total revenue
total_revenue = sum(sales.values())

# Find top-selling product
top_product = max(sales, key=sales.get)

# Bonus: Add TOTAL column
for row in data:
    row.append(row[1] * row[2])

# Sort by revenue (descending)
sorted_sales = sorted(sales.items(), key=lambda x: x[1], reverse=True)

# Output
print("Total Sales per Product:", sales)
print("Total Revenue:", total_revenue)
print("Top-Selling Product:", top_product)
print("Data with TOTAL column:", data)
print("Sorted by Revenue:", sorted_sales)
