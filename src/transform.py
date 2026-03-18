import pandas as pd
import boto3
import io
from datetime import datetime

def transform_data():
    s3 = boto3.client('s3')
    bucket_name = "capstone-currency-data-saud-final-2026"
    
    # S3 se latest file pakadna
    response = s3.list_objects_v2(Bucket=bucket_name)
    all_files = sorted(response.get('Contents', []), key=lambda x: x['LastModified'], reverse=True)
    latest_file = all_files[0]['Key']
    
    print(f"Reading {latest_file} from S3...")
    obj = s3.get_object(Bucket=bucket_name, Key=latest_file)
    raw_data = pd.read_json(io.BytesIO(obj['Body'].read()))
    
    # Transformation Logic
    rates = raw_data['rates']
    df = pd.DataFrame(list(rates.items()), columns=['CURRENCY', 'RATE'])
    
    # TIMESTAMP column (Capital letters mein taake Snowflake se match kare)
    df['TIMESTAMP'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Local save karna taake load script utha sakay
    df.to_csv("data/cleaned_rates.csv", index=False)
    print(f"✅ Success! Transformed {len(df)} rows and saved to data/cleaned_rates.csv")

if __name__ == "__main__":
    transform_data()