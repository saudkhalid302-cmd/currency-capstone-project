import snowflake.connector
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def load_to_snowflake():
    # Connection setup
    conn = snowflake.connector.connect(
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        warehouse='COMPUTE_WH',
        database='MY_PROJECT_DB',
        schema='PUBLIC'
    )
    
    cursor = conn.cursor()
    
    # 1. Pehle purana NULL wala data saaf karein (Sirf test ke liye)
    cursor.execute("TRUNCATE TABLE EXCHANGE_RATES")
    
    # 2. Local CSV read karein
    df = pd.read_csv("data/cleaned_rates.csv")
    
    print("Loading data into Snowflake...")
    
    # 3. Explicit Insert (Column names ke sath taake NULL ka sawal hi na paida ho)
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO EXCHANGE_RATES (CURRENCY, RATE, TIMESTAMP) VALUES (%s, %s, %s)",
            (row['CURRENCY'], row['RATE'], row['TIMESTAMP'])
        )
    
    print(f"✅ Data successfully loaded! {len(df)} rows inserted with Timestamps.")
    
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    load_to_snowflake()