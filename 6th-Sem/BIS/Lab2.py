import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# Load data
file_path = r'E:\samyak\6th-Sem\6th-Sem\BIS\Lab_2_Data.csv'
data = pd.read_csv(file_path)


# Preprocessing: Separate complete and incomplete data
complete_data = data.dropna(subset=['Profit', 'Transactions'])

# Prepare features and target variables for training
X = complete_data[['Sales']].values
y_profit = complete_data['Profit'].values
y_transactions = complete_data['Transactions'].values

# Train models
profit_model = LinearRegression().fit(X, y_profit)
transactions_model = LinearRegression().fit(X, y_transactions)

# Predict missing values specifically for the last two rows using y = mx + c
last_two_rows = data.tail(2).copy()
if last_two_rows['Profit'].isna().any():
    # Calculate predicted Profit using y = mx + c
    slope_profit = profit_model.coef_[0]
    intercept_profit = profit_model.intercept_
    last_two_rows['Predicted_Profit'] = (
        slope_profit * last_two_rows['Sales'] + intercept_profit
    )
    data.loc[data.tail(2).index, 'Profit'] = last_two_rows['Predicted_Profit']

if last_two_rows['Transactions'].isna().any():
    # Calculate predicted Transactions using y = mx + c
    slope_transactions = transactions_model.coef_[0]
    intercept_transactions = transactions_model.intercept_
    last_two_rows['Predicted_Transactions'] = (
        slope_transactions * last_two_rows['Sales'] + intercept_transactions
    )
    data.loc[data.tail(2).index, 'Transactions'] = last_two_rows[
        'Predicted_Transactions'
    ]

# Reset the index to start numbering from 1
data.index = range(1, len(data) + 1)

# Calculate overall predicted sales and transactions
overall_predicted_sales = last_two_rows['Sales'].sum()
overall_predicted_transactions = last_two_rows['Predicted_Transactions'].sum()

# Save the updated dataset (optional)
output_file = 'Updated_Data.csv'
data.to_csv(output_file, index=False)

# Display the updated data
print(data)

# Display overall predictions using y = mx + c
print("\nOverall Predicted Sales (last two rows):", overall_predicted_sales)
print("Overall Predicted Transactions (last two rows):", overall_predicted_transactions)


X = data[['Sales']].values
profit_model = LinearRegression().fit(X, data['Profit'])
transactions_model = LinearRegression().fit(X, data['Transactions'])

# Visualization: Subplots for Profit and Transactions
fig, axes = plt.subplots(2, 1, figsize=(16, 6))

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
