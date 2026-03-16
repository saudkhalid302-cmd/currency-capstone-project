<<<<<<< HEAD
import os
import json
import requests
from datetime import datetime

def fetch_and_save_data():
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        
    api_url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(data_dir, f"raw_rates_{timestamp}.json")
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        print(f"✅ Data saved to {file_path}")
    else:
        print(f"❌ Error: {response.status_code}")

if __name__ == "__main__":
    fetch_and_save_data()
=======
import requests
import os

def fetch_data():
    print("Fetching currency exchange rates...")
    # Example API call structure
    url = "https://api.exchangerate.host/latest"
    print("Connection successful!")

if __name__ == "__main__":
    fetch_data()
>>>>>>> fd711e00b6991d8c07c8896ba470bbfa271be207
