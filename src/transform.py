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
    
    # Check if API returned an error
    if raw_data.get('result') == 'error':
        print(f"❌ API Error Found: {raw_data.get('error-type')}")
        print("Please check your API Key in src/extract.py")
        return

    # Flexible Key Check (conversion_rates or rates)
    rates = raw_data.get('conversion_rates') or raw_data.get('rates')
    
    if not rates:
        print(f"❌ Error: Could not find 'conversion_rates' in JSON. Keys present: {list(raw_data.keys())}")
        return

    # Data Transformation
    df = pd.DataFrame(list(rates.items()), columns=['Currency', 'Rate_to_USD'])
    df['Last_Updated'] = raw_data.get('time_last_update_utc', 'N/A')
    
    # Save locally for reference
    output_file = "data/cleaned_rates.csv"
    os.makedirs('data', exist_ok=True)
    df.to_csv(output_file, index=False)
    
    print(f"✅ Success! Transformed {len(df)} rows.")
    print(f"📂 Cleaned data saved to {output_file}")

if __name__ == "__main__":
    s3 = boto3.client('s3')
    bucket = os.getenv('S3_BUCKET_NAME')
    
    # List objects and find the latest one
    response = s3.list_objects_v2(Bucket=bucket)
    
    if 'Contents' in response:
        objs = response['Contents']
        last_added = sorted(objs, key=lambda x: x['LastModified'], reverse=True)[0]
        file_on_s3 = last_added['Key']
        print(f"Latest file found in S3: {file_on_s3}")
        transform_data(file_on_s3)
    else:
        print(f"❌ Error: S3 Bucket '{bucket}' is EMPTY!")