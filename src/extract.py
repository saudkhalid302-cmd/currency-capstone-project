import boto3
import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def extract_to_s3():
    # 1. API se data lena
    url = "https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/USD"
    data = requests.get(url).json()
    
    # 2. File name banana
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"raw_rates_{timestamp}.json"
    
    # 3. S3 mein upload karna
    s3 = boto3.client('s3')
    bucket = "capstone-currency-data-saud-final-2026"
    
    s3.put_object(
        Bucket=bucket,
        Key=filename,
        Body=json.dumps(data)
    )
    print(f"✅ Success! Uploaded {filename} to S3 bucket: {bucket}")

if __name__ == "__main__":
    extract_to_s3()