import requests

FEDRAMP_DATA_URL = "https://raw.githubusercontent.com/GSA/marketplace-fedramp-gov-data/refs/heads/main/data.json"

def fetch_fedramp_data():
    """
    Fetches the FedRAMP marketplace data from the remote JSON source.
    Returns the parsed JSON as a Python dictionary.
    """
    response = requests.get(FEDRAMP_DATA_URL)
    response.raise_for_status()
    return response.json()

# Load data at module import
fedramp_data = fetch_fedramp_data()
