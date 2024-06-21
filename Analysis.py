import pandas as pd
import matplotlib.pyplot as plt

# Load data from Excel file
df = pd.read_excel('stocks.xlsx')

# Display first few rows to check data


# Plot stock prices
plt.figure(figsize=(10, 6))
plt.bar(df['Ticker Symbol'], df['Stock Price'], color='skyblue')
plt.xlabel('Ticker Symbol')
plt.ylabel('Stock Price')
plt.title('Stock Prices')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Save summary statistics to a new Excel sheet
summary_stats = df.describe()
summary_stats.to_excel('stock_summary_statistics.xlsx', index=True)
