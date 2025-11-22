import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("/mnt/data/sales_data.db")
query = """
SELECT 
    product,
    SUM(quantity) AS total_qty,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC
"""
df = pd.read_sql_query(query, conn)
conn.close()

print(df)

plt.figure(figsize=(7,4))
plt.bar(df['product'], df['revenue'])
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()
plt.savefig("/mnt/data/sales_chart.png")
