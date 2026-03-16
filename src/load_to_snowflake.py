import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

try:
    ctx = snowflake.connector.connect(
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        warehouse='COMPUTE_WH',
        database='MY_PROJECT_DB',
        schema='PUBLIC',
        login_timeout=60,
        network_timeout=60,
        client_session_keep_alive=True,
        insecure_mode=True
    )
    
    df = pd.read_csv('data/cleaned_rates.csv')
    
    # Yahan columns ko UPPERCASE kar dein taake Snowflake se match ho sake
    df.columns = ['CURRENCY', 'RATE', 'TIMESTAMP']
    
    print("Loading data into Snowflake table 'EXCHANGE_RATES'...")
    
    # Ab load karein
    success, nchunks, nrows, _ = write_pandas(ctx, df, 'EXCHANGE_RATES', auto_create_table=False)
    
    if success:
        print(f"✅ Data successfully loaded! {nrows} rows inserted.")
    
    ctx.close()

except Exception as e:
    print(f"❌ Error occurred: {e}")