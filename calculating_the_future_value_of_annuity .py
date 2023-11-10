import pandas as pd


# Function to calculate future value of an annuity with different compounding frequencies
def future_value_annuity(periodic_payment, interest_rate, periods, compounding_frequency='annual'):
    if compounding_frequency == 'annual':
        compounding_periods = 1
    elif compounding_frequency == 'semi-annual':
        compounding_periods = 2
    elif compounding_frequency == 'quarterly':
        compounding_periods = 4
    elif compounding_frequency == 'monthly':
        compounding_periods = 12
    else:
        raise ValueError("Invalid compounding frequency")

    effective_rate = interest_rate / compounding_periods
    total_periods = periods * compounding_periods

    return periodic_payment * ((1 + effective_rate) ** total_periods - 1) / effective_rate

def process_dataset(file_path, payment_col, rate_col, period_col, compounding_col):
    try:
        # Read the dataset
        dataset = pd.read_csv(file_path)

        # Validate and calculate future value for each entry
        dataset['Future_Value'] = dataset.apply(
            lambda row: future_value_annuity(
                row[payment_col],
                row[rate_col],
                row[period_col],
                row[compounding_col]),
            axis=1
        )

        # Optionally: Save the dataset with the new Future Value column
        # dataset.to_csv('path_to_save_modified_dataset.csv', index=False)

        return dataset
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
file_path = 'large_financial_dataset.csv'  # Replace with your dataset path
result = process_dataset(file_path, 'Periodic_Payment', 'Interest_Rate', 'Periods', 'Compounding_Frequency')
if result is not None:
    print(result)
