import pandas as pd
import boto3
import json
import os
from dotenv import load_dotenv

load_dotenv()

def transform_data(file_key):
    s3 = boto3.client('s3')
    bucket = os.getenv('S3_BUCKET_NAME')
    
    # 1. S3 se file read karna
    print(f"Reading {file_key} from S3...")
    response = s3.get_object(Bucket=bucket, Key=file_key)
    raw_data = json.loads(response['Body'].read().decode('utf-8'))
    
    # 2. Rates nikalna
    rates = raw_data['conversion_rates']
    
    # 3. Pandas DataFrame banana (SAARI currencies ke liye)
    df = pd.DataFrame(list(rates.items()), columns=['Currency', 'Rate_to_USD'])
    df['Last_Updated'] = raw_data['time_last_update_utc']
    
    print("--- Transformed Data (First 5 rows) ---")
    print(df.head())
    
    # 4. CSV mein convert karke local save karna
    output_file = "data/cleaned_rates.csv"
    df.to_csv(output_file, index=False)
    print(f"✅ Success! Cleaned data saved to {output_file}")

if __name__ == "__main__":
    # S3 bucket mein maujood file ka naam (wahi jo extract.py ne banayi thi)
    file_on_s3 = "raw_rates_20260307_145906.json"
    transform_data(file_on_s3)