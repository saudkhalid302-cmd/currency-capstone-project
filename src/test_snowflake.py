import snowflake.connector
import os
from dotenv import load_dotenv

# Yeh line aapki .env file se details utha legi
load_dotenv()

try:
    # Snowflake connection setup
    conn = snowflake.connector.connect(
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
        database=os.getenv('SNOWFLAKE_DATABASE'),
        schema=os.getenv('SNOWFLAKE_SCHEMA')
    )
    
    print("✅ Connection Successful!")
    conn.close()

except Exception as e:
    print(f"❌ Error aaya hai: {e}")