import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

# Environment variables load karein
load_dotenv()

def fetch_currency_data():
    api_key = os.getenv('CURRENCY_API_KEY')
    # API se latest rates fetch karna [cite: 46, 57]
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Raw data ko 'data' folder mein save karna 
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"data/raw_rates_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(data, f)
            
        print(f"✅ Success! Data saved to {filename}")
        return filename
    else:
        print(f"❌ Error: {response.status_code}")
        return None

if __name__ == "__main__":
    fetch_currency_data()