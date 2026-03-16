import os
import json
import requests
from datetime import datetime

def fetch_and_save_data():
    # Data directory create karna (Best practice)
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        
    # API se data fetch karna
    api_url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Unique timestamp ke saath file save karna
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(data_dir, f"raw_rates_{timestamp}.json")
        
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
            
        print(f"✅ Data successfully saved to {file_path}")
    else:
        print(f"❌ Error: API request failed with status code {response.status_code}")

if __name__ == "__main__":
    fetch_and_save_data()