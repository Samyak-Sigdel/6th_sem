import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load updated data
updated_file_path = 'Updated_Data.csv'
data = pd.read_csv(updated_file_path)

# Prepare features for plotting
X = data[['Sales']].values
profit_model = LinearRegression().fit(X, data['Profit'])
transactions_model = LinearRegression().fit(X, data['Transactions'])

# Visualization: Subplots for Profit and Transactions
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Subplot 1: Profit
axes[0].scatter(data['Sales'], data['Profit'], color='blue', label='Actual Profit')
x_line = data['Sales'].values.reshape(-1, 1)
y_line_profit = profit_model.predict(x_line)
axes[0].plot(data['Sales'], y_line_profit, color='blue', linestyle='--', label='Regression Line (Profit)')
axes[0].set_title('Sales vs Predicted Profit')
axes[0].set_xlabel('Sales')
axes[0].set_ylabel('Profit')
axes[0].legend()
axes[0].grid()

# Subplot 2: Transactions
axes[1].scatter(data['Sales'], data['Transactions'], color='green', label='Actual Transactions')
y_line_transactions = transactions_model.predict(x_line)
axes[1].plot(data['Sales'], y_line_transactions, color='green', linestyle='--', label='Regression Line (Transactions)')
axes[1].set_title('Sales vs Predicted Transactions')
axes[1].set_xlabel('Sales')
axes[1].set_ylabel('Transactions')
axes[1].legend()
axes[1].grid()

# Save and display the plots
plt.tight_layout()
plt.savefig('Profit_and_Transactions_Predictions.png')
plt.show()
