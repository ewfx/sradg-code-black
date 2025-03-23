import ollama
import pandas as pd

def load_historical_data(csv_path, account_number):
    """
    Loads historical transactions for a given account number.

    Args:
        csv_path (str): Path to the dataset (CSV file).
        account_number (str): The account number to filter historical data.

    Returns:
        str: A formatted string containing historical transaction details.
    """
    try:
        df = pd.read_csv(csv_path)
        historical_records = df[df["account_number"] == account_number]

        if historical_records.empty:
            return "No historical data available for this account."

        return historical_records.to_string(index=False)  # Convert DataFrame to readable text

    except Exception as e:
        return f"Error loading historical data: {str(e)}"

def query_mistral(csv_path, real_time_data, classification_result):
    """
    Queries Mistral 7B to analyze an anomaly using classification results and historical data.

    Args:
        csv_path (str): Path to the dataset.
        real_time_data (dict): The real-time transaction data (single row from CSV).
        classification_result (dict): The classification output, e.g.,
                                      {'record_id': 123, 'predicted_label': 'Anomaly Type A'}

    Returns:
        str: Mistral's response explaining why this transaction is an anomaly.
    """
    account_number = real_time_data.get("account_number")
    
    if not account_number:
        return "Error: Account number missing in real-time data."

    # Load historical transactions for the same account
    historical_data = load_historical_data(csv_path, account_number)

    # Construct the prompt dynamically
    prompt = f"""
    You are an AI helping with anomaly detection in financial reconciliation.

    Here is a real-time transaction:
    {real_time_data}

    Classification result from the ML model:
    {classification_result}

    Historical transactions for the same account:
    {historical_data}

    Based on the historical data and classification result, explain why this might be an anomaly.
    """

    # Query Mistral
    response = ollama.chat(model='mistral', messages=[{"role": "user", "content": prompt}])

    return response['message']['content']
