import pandas as pd
import boto3
import json
import os
from dotenv import load_dotenv

load_dotenv()

def transform_data(file_key):
    s3 = boto3.client('s3')
    bucket = os.getenv('S3_BUCKET_NAME')
    
    print(f"Reading {file_key} from S3...")
    response = s3.get_object(Bucket=bucket, Key=file_key)
    raw_data = json.loads(response['Body'].read().decode('utf-8'))
    
    rates = raw_data['conversion_rates']
    df = pd.DataFrame(list(rates.items()), columns=['Currency', 'Rate_to_USD'])
    df['Last_Updated'] = raw_data['time_last_update_utc']
    
    print("--- Transformed Data (First 5 rows) ---")
    print(df.head())
    
    output_file = "data/cleaned_rates.csv"
    df.to_csv(output_file, index=False)
    print(f"✅ Success! Cleaned data saved to {output_file}")

if __name__ == "__main__":
    # Updated to the latest file from March 18
    file_on_s3 = "raw_rates_20260318_162445.json"
    transform_data(file_on_s3)