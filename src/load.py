import boto3
import os
from dotenv import load_dotenv

# .env file se configurations load karein
load_dotenv()

def upload_to_s3(file_path):
    # AWS Credentials
    s3_client = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_REGION')
    )
    
    bucket_name = os.getenv('S3_BUCKET_NAME')
    file_name = os.path.basename(file_path)
    
    try:
        print(f"Uploading {file_name} to S3 bucket {bucket_name}...")
        s3_client.upload_file(file_path, bucket_name, file_name)
        print("✅ Upload Successful!")
    except Exception as e:
        print(f"❌ Error uploading to S3: {e}")

if __name__ == "__main__":
    # Jo file extract.py ne banayi thi, uska path yahan likhein
    # Misal ke taur par:
    latest_file = "data/raw_rates_20260307_145906.json" 
    upload_to_s3(latest_file)