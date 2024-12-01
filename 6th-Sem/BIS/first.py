import pandas as pd
from sklearn.linear_model import LinearRegression

# Load data
file_path = 'Data.csv'
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