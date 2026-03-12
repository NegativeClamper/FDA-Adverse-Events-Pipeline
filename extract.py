import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_fda_data(limit):
    url = os.getenv("url")
    final_url = f"{url}?limit={limit}"

    try:
        response = requests.get(final_url, timeout= 10)
        response.raise_for_status()
        data = response.json()
        return data.get('results', [])

    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return None

if __name__ == "__main__":
    test_data = fetch_fda_data(5)
    if test_data:
        print(f"Successfully extracted {len(test_data)} records!")

