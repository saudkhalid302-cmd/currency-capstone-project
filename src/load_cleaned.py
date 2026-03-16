import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def upload_cleaned_to_s3(file_path):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_REGION')
    )
    
    bucket_name = os.getenv('S3_BUCKET_NAME')
    # Hum file ko S3 mein "processed/" folder ke andar rakhenge
    s3_key = "processed/cleaned_rates.csv"
    
    try:
        print(f"Uploading cleaned data to {bucket_name}/{s3_key}...")
        s3_client.upload_file(file_path, bucket_name, s3_key)
        print("✅ Final Upload Successful!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    upload_cleaned_to_s3("data/cleaned_rates.csv")
    